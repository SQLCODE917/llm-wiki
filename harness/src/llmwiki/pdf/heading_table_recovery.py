"""Recover heading-led numbered tables from source text geometry."""

from __future__ import annotations

import re
from statistics import median
from typing import Any

from llmwiki.pdf.layout_lines import TextLine, WordBox
from llmwiki.pdf.table_candidate_model import TableCandidate
from llmwiki.pdf.table_forward_repair import is_numbered_row_marker_line, numbered_table_text

_MAX_BODY_LINES = 90
_ROW_MARKER = re.compile(r"^\s*\d{1,3}(?:[-–]\d{1,3})?\s*$", re.MULTILINE)
_HEADING_CONNECTORS = frozenset({"a", "an", "and", "for", "in", "of", "or", "the", "to"})


def heading_numbered_table_candidates(
    doc: Any, lines_by_page: tuple[tuple[TextLine, ...], ...]
) -> tuple[TableCandidate, ...]:
    candidates: list[TableCandidate] = []
    for page_index, lines in enumerate(lines_by_page):
        for line_index, line in enumerate(lines):
            if not _header_line(line):
                continue
            body = _collect_body(doc, lines_by_page, page_index, line_index)
            if not _geometry_matches_header(line, body):
                continue
            caption = _caption(lines, line_index)
            rows = _plain_table_text(doc, page_index, caption, line, body)
            if _numbered_line_count(rows) < 3:
                rows = numbered_table_text(body, include_leading_text=True)
            if _row_count(rows) < 3:
                continue
            raw_text = rows
            all_lines = (line, *body)
            candidates.append(
                TableCandidate(
                    caption=caption or line.text,
                    page_start=page_index + 1,
                    page_end=max(item.page_index for item in all_lines) + 1,
                    y0=line.y0,
                    raw_text=raw_text,
                    extractor_stage="heading-numbered-layout",
                    anchor_text=caption,
                    insert_after_anchor=bool(caption),
                )
            )
    return tuple(candidates)


def _header_line(line: TextLine) -> bool:
    if not 2 <= len(line.words) <= 4:
        return False
    text = line.text.strip()
    if text.endswith((".", ",", ";", ":")):
        return False
    if is_numbered_row_marker_line(line):
        return False
    spread = max(word.x1 for word in line.words) - min(word.x0 for word in line.words)
    return spread >= 24.0 and all(len(word.text) <= 32 for word in line.words)


def _collect_body(
    doc: Any,
    lines_by_page: tuple[tuple[TextLine, ...], ...],
    page_index: int,
    header_index: int,
) -> tuple[TextLine, ...]:
    selected: list[TextLine] = []
    marker_count = 0
    page_offset = 0.0
    for current_page in range(page_index, len(lines_by_page)):
        lines = lines_by_page[current_page]
        start = header_index + 1 if current_page == page_index else 0
        if current_page > page_index:
            page_offset += float(doc[current_page - 1].rect.height)
        for line in lines[start:]:
            shifted = _shift_line(line, page_offset)
            if marker_count == 0 and len(selected) >= 3 and _section_heading(line):
                return tuple(selected)
            if marker_count >= 2 and _section_heading(line):
                return tuple(selected)
            selected.append(shifted)
            marker_count += 1 if is_numbered_row_marker_line(line) else 0
            if len(selected) >= _MAX_BODY_LINES:
                return tuple(selected)
        if (
            marker_count >= 2
            and selected
            and not _near_page_bottom(doc[current_page], selected[-1])
        ):
            return tuple(selected)
    return tuple(selected)


def _geometry_matches_header(header: TextLine, body: tuple[TextLine, ...]) -> bool:
    markers = tuple(line for line in body if is_numbered_row_marker_line(line))
    if len(markers) < 3:
        return False
    first_marker = next(index for index, line in enumerate(body) if line in markers)
    if first_marker > 8:
        return False
    marker_x = median(line.words[0].x0 for line in markers)
    content_x = _content_x(body, marker_x)
    return (
        abs(header.words[0].x0 - marker_x) <= 18.0
        and content_x is not None
        and abs(header.words[1].x0 - content_x) <= 48.0
    )


def _content_x(lines: tuple[TextLine, ...], marker_x: float) -> float | None:
    starts: list[float] = []
    for line in lines:
        words = tuple(word for word in line.words if not _marker_word(word))
        if is_numbered_row_marker_line(line) and len(line.words) >= 2:
            starts.append(line.words[1].x0)
        elif words and words[0].x0 > marker_x + 12.0:
            starts.append(words[0].x0)
    return median(starts) if starts else None


def _plain_table_text(
    doc: Any,
    page_index: int,
    caption: str,
    header: TextLine,
    body: tuple[TextLine, ...],
) -> str:
    if not body:
        return ""
    plain_lines = _plain_lines(doc, page_index, body[-1].page_index)
    start = _plain_start(plain_lines, caption, header)
    end = _plain_end(plain_lines, body[-1].text)
    if start is None or end is None or end <= start:
        return ""
    return "\n".join(plain_lines[start : end + 1]).strip()


def _plain_lines(doc: Any, page_start: int, page_end: int) -> tuple[str, ...]:
    lines: list[str] = []
    for page_index in range(page_start, page_end + 1):
        lines.extend(
            line.strip() for line in str(doc[page_index].get_text()).splitlines() if line.strip()
        )
    return tuple(lines)


def _plain_start(lines: tuple[str, ...], caption: str, header: TextLine) -> int | None:
    caption_key = _key(caption)
    if caption_key:
        for index, line in enumerate(lines):
            if _key(line) == caption_key:
                return index
    header_words = tuple(_key(word.text) for word in header.words if _key(word.text))
    if not header_words:
        return None
    for index in range(len(lines)):
        window = tuple(_key(line) for line in lines[index : index + len(header_words)])
        if window == header_words:
            return index
    header_key = _key(header.text)
    for index, line in enumerate(lines):
        if _key(line) == header_key:
            return index
    return None


def _plain_end(lines: tuple[str, ...], last_body_line: str) -> int | None:
    last_key = _key(last_body_line)
    for index in range(len(lines) - 1, -1, -1):
        if _key(lines[index]) == last_key:
            return index
    body_words = tuple(last_key.split())
    if len(body_words) < 3:
        return None
    suffix = " ".join(body_words[-4:])
    for index in range(len(lines) - 1, -1, -1):
        if suffix and suffix in _key(lines[index]):
            return index
    return None


def _caption(lines: tuple[TextLine, ...], header_index: int) -> str:
    if header_index <= 0:
        return ""
    previous = lines[header_index - 1]
    gap = lines[header_index].y0 - previous.y1
    if gap > 36.0 or not _section_heading(previous):
        return ""
    return previous.text


def _section_heading(line: TextLine) -> bool:
    if not 1 <= len(line.words) <= 6:
        return False
    text = line.text.strip()
    if is_numbered_row_marker_line(line) or text.endswith((".", ",", ";", ":")):
        return False
    content = [
        word.text.strip("()[]{}")
        for word in line.words
        if word.text.lower().strip("()[]{}") not in _HEADING_CONNECTORS
    ]
    return bool(content) and all(_title_token(word) for word in content)


def _title_token(text: str) -> bool:
    return text[:1].isupper() or bool(re.fullmatch(r"[dD]\d+", text))


def _near_page_bottom(page: Any, line: TextLine) -> bool:
    return line.y1 >= float(page.rect.height) * 0.88


def _row_count(raw_text: str) -> int:
    return sum(1 for line in raw_text.splitlines() if line.strip())


def _numbered_line_count(raw_text: str) -> int:
    return len(_ROW_MARKER.findall(raw_text))


def _key(text: str) -> str:
    return " ".join(text.lower().split())


def _marker_word(word: WordBox) -> bool:
    return word.text.isdigit()


def _shift_line(line: TextLine, y_offset: float) -> TextLine:
    if not y_offset:
        return line
    words = tuple(
        WordBox(word.x0, word.y0 + y_offset, word.x1, word.y1 + y_offset, word.text)
        for word in line.words
    )
    return TextLine(line.page_index, line.y0 + y_offset, line.y1 + y_offset, words)
