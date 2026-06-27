"""High-recall table candidates recovered from PDF page geometry."""

from __future__ import annotations

import re
from multiprocessing import get_context
from pathlib import Path
from queue import Empty
from typing import Any

import pymupdf

from llmwiki.pdf.document import DocumentModel
from llmwiki.pdf.layout_lines import TextLine, layout_text, page_lines
from llmwiki.pdf.table_candidate_dedupe import dedupe_table_candidates
from llmwiki.pdf.table_candidate_model import TableCandidate
from llmwiki.pdf.table_forward_repair import forward_table_text, is_forward_table_cue
from llmwiki.pdf.table_geometry_repair import geometry_table_rows, preface_numbered_table_text

_CAPTION = re.compile(r"^\s*(?:table|tab\.)\s*(?:([-:.])|(\d+\b))?\s*(.*)$", re.IGNORECASE)
_TOC = re.compile(r"\btable\s+of\s+contents\b", re.IGNORECASE)
_HEADING_CONNECTORS = frozenset({"a", "an", "and", "for", "in", "into", "of", "out", "the", "to"})
_FIND_TABLES_TIMEOUT_SECONDS = 45.0


def table_candidates(pdf_path: Path, model: DocumentModel) -> tuple[TableCandidate, ...]:
    """Return source-neutral table candidates not already in the document model."""
    with pymupdf.open(pdf_path) as doc:  # type: ignore[no-untyped-call]
        lines_by_page = tuple(page_lines(page, page_index) for page_index, page in enumerate(doc))
        candidates = list(_find_tables_candidates_isolated(pdf_path))
        candidates.extend(_caption_layout_candidates(doc, lines_by_page))
        candidates.extend(_forward_cue_layout_candidates(lines_by_page))
    return dedupe_table_candidates(tuple(candidates), model)


def _find_tables_candidates_isolated(pdf_path: Path) -> tuple[TableCandidate, ...]:
    """Run PyMuPDF's native table detector out-of-process.

    ``page.find_tables`` can segfault in MuPDF for some layouts and under some
    instrumentation. A subprocess gives the detector a chance to contribute
    high-precision geometry without letting a native crash kill ingestion.
    """
    context = get_context("spawn")
    queue = context.Queue()
    process = context.Process(target=_find_tables_worker, args=(str(pdf_path), queue))
    process.start()
    process.join(_FIND_TABLES_TIMEOUT_SECONDS)
    if process.is_alive():
        process.terminate()
        process.join()
        return ()
    if process.exitcode != 0:
        return ()
    try:
        result = queue.get_nowait()
    except Empty:
        return ()
    return result if isinstance(result, tuple) else ()


def _find_tables_worker(pdf_path: str, queue: Any) -> None:
    try:
        with pymupdf.open(pdf_path) as doc:  # type: ignore[no-untyped-call]
            queue.put(_find_tables_candidates(doc))
    except Exception:
        queue.put(())


def _find_tables_candidates(doc: Any) -> tuple[TableCandidate, ...]:
    candidates: list[TableCandidate] = []
    for page_index, page in enumerate(doc):
        finder = getattr(page, "find_tables", None)
        if not callable(finder):
            continue
        try:
            tables = tuple(finder().tables)
        except Exception:
            continue
        for table in tables:
            extracted_rows = tuple(tuple(cell or "" for cell in row) for row in table.extract())
            rows = _preferred_rows(geometry_table_rows(page, table), extracted_rows)
            next_page = doc[page_index + 1] if page_index + 1 < len(doc) else None
            numbered_text = preface_numbered_table_text(page, table, rows, next_page)
            if numbered_text:
                caption = ""
                raw_text = numbered_text
            else:
                caption, rows = _remove_caption_row(rows)
                if len(rows) < 2:
                    continue
                raw_text = _pipe_table(rows)
            if caption:
                raw_text = f"{caption}\n{raw_text}"
            candidates.append(
                TableCandidate(
                    caption=caption,
                    page_start=page_index + 1,
                    page_end=page_index + 1,
                    y0=float(table.bbox[1]) if getattr(table, "bbox", None) else 0.0,
                    raw_text=raw_text,
                    extractor_stage="pymupdf-find-tables",
                )
            )
    return tuple(candidates)


def _remove_caption_row(
    rows: tuple[tuple[str, ...], ...],
) -> tuple[str, tuple[tuple[str, ...], ...]]:
    if len(rows) < 3:
        return "", rows
    filled = tuple(cell.strip() for cell in rows[0] if cell.strip())
    if len(filled) != 1:
        return "", rows
    caption = _caption(filled[0])
    if caption is None:
        return "", rows
    return caption, rows[1:]


def _preferred_rows(
    geometry_rows: tuple[tuple[str, ...], ...], extracted_rows: tuple[tuple[str, ...], ...]
) -> tuple[tuple[str, ...], ...]:
    if len(geometry_rows) < 2:
        return extracted_rows
    if _filled_cell_count(geometry_rows) < max(2, int(_filled_cell_count(extracted_rows) * 0.6)):
        return extracted_rows
    return geometry_rows


def _filled_cell_count(rows: tuple[tuple[str, ...], ...]) -> int:
    return sum(1 for row in rows for cell in row if cell.strip())


def _caption_layout_candidates(
    doc: Any, lines_by_page: tuple[tuple[TextLine, ...], ...]
) -> tuple[TableCandidate, ...]:
    candidates: list[TableCandidate] = []
    for page_index, lines in enumerate(lines_by_page):
        for line_index, line in enumerate(lines):
            caption = _caption(line.text)
            if caption is None:
                continue
            body = _collect_table_body(doc, lines_by_page, page_index, line_index)
            if _table_like_count(body) < 2:
                continue
            all_lines = (line, *body)
            candidates.append(
                TableCandidate(
                    caption=caption,
                    page_start=page_index + 1,
                    page_end=max(item.page_index for item in all_lines) + 1,
                    y0=line.y0,
                    raw_text=layout_text(all_lines),
                    extractor_stage="caption-layout",
                    anchor_text=line.text,
                )
            )
    return tuple(candidates)


def _forward_cue_layout_candidates(
    lines_by_page: tuple[tuple[TextLine, ...], ...],
) -> tuple[TableCandidate, ...]:
    candidates: list[TableCandidate] = []
    for page_index, lines in enumerate(lines_by_page):
        for line_index, line in enumerate(lines):
            if not is_forward_table_cue(line.text):
                continue
            raw_text = forward_table_text(lines, line_index)
            if _row_text_count(raw_text) < 2:
                continue
            candidates.append(
                TableCandidate(
                    caption="",
                    page_start=page_index + 1,
                    page_end=page_index + 1,
                    y0=line.y0,
                    raw_text=raw_text,
                    extractor_stage="forward-cue-layout",
                    anchor_text=line.text,
                    insert_after_anchor=True,
                )
            )
    return tuple(candidates)


def _row_text_count(raw_text: str) -> int:
    return sum(1 for line in raw_text.splitlines() if line.strip())


def _caption(text: str) -> str | None:
    if _TOC.search(text):
        return None
    match = _CAPTION.match(text)
    if match is None:
        return None
    remainder = " ".join(match.group(3).split())
    if not (match.group(1) or match.group(2)) and not _caption_remainder_title_like(remainder):
        return None
    caption = " ".join(text.split())
    return caption if len(caption.split()) <= 12 else None


def _caption_remainder_title_like(text: str) -> bool:
    words = [word.strip(":-") for word in text.split() if word.strip(":-")]
    if not words or len(words) > 6 or text.endswith((".", ",", ";")):
        return False
    content = [word for word in words if word.lower() not in _HEADING_CONNECTORS]
    return bool(content) and all(word[:1].isupper() for word in content)


def _collect_table_body(
    doc: Any,
    lines_by_page: tuple[tuple[TextLine, ...], ...],
    page_index: int,
    line_index: int,
) -> tuple[TextLine, ...]:
    collected = list(_collect_same_page(lines_by_page[page_index], line_index + 1))
    if collected and _near_page_bottom(doc[page_index], collected[-1]):
        for next_index in range(page_index + 1, len(lines_by_page)):
            continuation = _collect_continuation_page(doc[next_index], lines_by_page[next_index])
            if not continuation:
                break
            collected.extend(continuation)
            if not _near_page_bottom(doc[next_index], continuation[-1]):
                break
    return tuple(collected)


def _collect_same_page(lines: tuple[TextLine, ...], start: int) -> tuple[TextLine, ...]:
    selected: list[TextLine] = []
    table_like = 0
    previous_y = lines[start - 1].y1 if start else 0.0
    for index in range(start, len(lines)):
        line = lines[index]
        if _caption(line.text) is not None and selected:
            break
        line_like = _is_table_like_line(line)
        next_like = index + 1 < len(lines) and _is_table_like_line(lines[index + 1])
        continues = _line_before_table(lines, index)
        gap = line.y0 - previous_y
        if table_like >= 2 and not (line_like or next_like or continues):
            break
        if table_like >= 2 and line_like and _looks_like_heading(line) and not next_like:
            break
        if table_like >= 2 and gap > 22.0 and not (line_like or next_like or continues):
            break
        selected.append(line)
        table_like += 1 if line_like else 0
        previous_y = line.y1
    return tuple(selected)


def _collect_continuation_page(page: Any, lines: tuple[TextLine, ...]) -> tuple[TextLine, ...]:
    selected: list[TextLine] = []
    top_limit = float(page.rect.height) * 0.18
    for index, line in enumerate(lines):
        if line.y0 > top_limit or _caption(line.text) is not None:
            break
        next_like = index + 1 < len(lines) and _is_table_like_line(lines[index + 1])
        if selected and not (next_like or _is_table_like_line(line)):
            break
        if selected and _is_table_like_line(line) and _looks_like_heading(line) and not next_like:
            break
        if _is_table_like_line(line) or (_is_short_label(line) and next_like):
            selected.append(line)
            continue
        break
    return tuple(selected)


def _is_table_like_line(line: TextLine) -> bool:
    words = line.words
    if len(words) < 3:
        return False
    if len(words) > 10:
        return False
    if len(words) > 6 and not any(_has_table_value(word.text) for word in words):
        return False
    if line.text.endswith(".") and not any(_has_table_value(word.text) for word in words):
        return False
    spread = max(word.x1 for word in words) - min(word.x0 for word in words)
    return spread >= 90.0


def _has_table_value(text: str) -> bool:
    return any(char.isdigit() for char in text) or text in {"-", "+", "+2"}


def _is_short_label(line: TextLine) -> bool:
    return 1 <= len(line.words) <= 3 and not line.text.endswith(".")


def _line_before_table(lines: tuple[TextLine, ...], index: int) -> bool:
    if len(lines[index].words) > 5:
        return False
    return any(_is_table_like_line(line) for line in lines[index + 1 : index + 5])


def _looks_like_heading(line: TextLine) -> bool:
    words = [word.text.strip(":-") for word in line.words if word.text.strip(":-")]
    if not 2 <= len(words) <= 8:
        return False
    if any(any(char.isdigit() for char in word) for word in words):
        return False
    content_words = [word for word in words if word.lower() not in _HEADING_CONNECTORS]
    return len(content_words) >= 2 and all(word[:1].isupper() for word in content_words)


def _table_like_count(lines: tuple[TextLine, ...]) -> int:
    return sum(1 for line in lines if _is_table_like_line(line))


def _near_page_bottom(page: Any, line: TextLine) -> bool:
    return line.y1 >= float(page.rect.height) * 0.88


def _pipe_table(rows: tuple[tuple[str, ...], ...]) -> str:
    width = max(len(row) for row in rows)
    padded = [tuple((*row, *("" for _ in range(width - len(row))))) for row in rows]
    header = padded[0]
    lines = [
        "| " + " | ".join(header) + " |",
        "| " + " | ".join("---" for _ in header) + " |",
    ]
    lines.extend("| " + " | ".join(row) + " |" for row in padded[1:])
    return "\n".join(lines)
