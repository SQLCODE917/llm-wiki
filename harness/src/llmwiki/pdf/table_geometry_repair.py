"""Render detected PDF table cells from original page word geometry."""

from __future__ import annotations

from typing import Any

from llmwiki.pdf.layout_lines import TextLine, WordBox, join_words, page_lines, page_words
from llmwiki.pdf.table_forward_repair import is_numbered_row_marker_line, numbered_table_text

_CELL_PAD = 2.0


def geometry_table_rows(page: Any, table: Any) -> tuple[tuple[str, ...], ...]:
    """Return table rows by reading words whose centers fall in each cell bbox."""
    words = page_words(page)
    rows: list[tuple[str, ...]] = []
    for row in getattr(table, "rows", ()) or ():
        cells = getattr(row, "cells", ()) or ()
        rendered = tuple(_cell_text(words, cell) for cell in cells)
        if any(cell.strip() for cell in rendered):
            rows.append(rendered)
    return tuple(rows)


def preface_numbered_table_text(
    page: Any, table: Any, rows: tuple[tuple[str, ...], ...], next_page: Any | None = None
) -> str:
    if not _has_spanning_preface_row(rows):
        return ""
    lines = _table_lines(page, table, next_page)
    if sum(1 for line in lines if is_numbered_row_marker_line(line)) < 2:
        return ""
    preface = " ".join(line.text for line in _leading_non_marker_lines(lines)).strip()
    body = numbered_table_text(lines, include_leading_text=False)
    if _line_count(body) < 2:
        return ""
    return f"{preface}\n{body}" if preface else body


def _cell_text(words: tuple[WordBox, ...], cell: Any) -> str:
    if cell is None:
        return ""
    try:
        x0, y0, x1, y1 = (float(value) for value in cell)
    except (TypeError, ValueError):
        return ""
    contained = tuple(word for word in words if _in_cell(word, x0, y0, x1, y1))
    return join_words(contained)


def _in_cell(word: WordBox, x0: float, y0: float, x1: float, y1: float) -> bool:
    cx = (word.x0 + word.x1) / 2.0
    return x0 - _CELL_PAD <= cx <= x1 + _CELL_PAD and y0 - _CELL_PAD <= word.cy <= y1 + _CELL_PAD


def _has_spanning_preface_row(rows: tuple[tuple[str, ...], ...]) -> bool:
    if not rows or len(rows[0]) < 3:
        return False
    return (
        not rows[0][0].strip()
        and not rows[0][1].strip()
        and any(cell.strip() for cell in rows[0][2:])
    )


def _table_lines(page: Any, table: Any, next_page: Any | None) -> tuple[TextLine, ...]:
    bbox = getattr(table, "bbox", None)
    if bbox is None:
        return ()
    try:
        x0, y0, x1, y1 = (float(value) for value in bbox)
    except (TypeError, ValueError):
        return ()
    clipped: list[TextLine] = []
    for line in page_lines(page, 0):
        words = tuple(word for word in line.words if _in_cell(word, x0, y0, x1, y1))
        if words:
            clipped.append(
                TextLine(0, min(word.y0 for word in words), max(word.y1 for word in words), words)
            )
    if next_page is not None and _near_page_bottom(page, y1):
        clipped.extend(_continuation_lines(next_page, x0, x1, float(page.rect.height)))
    return tuple(clipped)


def _near_page_bottom(page: Any, y1: float) -> bool:
    return y1 >= float(page.rect.height) * 0.9


def _continuation_lines(
    next_page: Any, x0: float, x1: float, y_offset: float
) -> tuple[TextLine, ...]:
    selected: list[TextLine] = []
    marker_seen = False
    top_limit = max(120.0, float(next_page.rect.height) * 0.18)
    for line in page_lines(next_page, 0):
        if line.y0 > top_limit:
            break
        words = tuple(word for word in line.words if x0 - _CELL_PAD <= word.x0 <= x1 + _CELL_PAD)
        if not words:
            continue
        clipped = _shift_line(
            TextLine(0, min(word.y0 for word in words), max(word.y1 for word in words), words),
            y_offset,
        )
        if marker_seen and _looks_like_heading(clipped):
            break
        selected.append(clipped)
        marker_seen = marker_seen or is_numbered_row_marker_line(clipped)
    return tuple(selected) if marker_seen else ()


def _shift_line(line: TextLine, y_offset: float) -> TextLine:
    words = tuple(
        WordBox(word.x0, word.y0 + y_offset, word.x1, word.y1 + y_offset, word.text)
        for word in line.words
    )
    return TextLine(line.page_index, line.y0 + y_offset, line.y1 + y_offset, words)


def _looks_like_heading(line: TextLine) -> bool:
    if not 1 <= len(line.words) <= 6:
        return False
    text = line.text.strip()
    if any(char.isdigit() for char in text) or text.endswith((".", ",", ";", ":")):
        return False
    return all(word.text[:1].isupper() for word in line.words if word.text)


def _leading_non_marker_lines(lines: tuple[TextLine, ...]) -> tuple[TextLine, ...]:
    leading: list[TextLine] = []
    for line in lines:
        if is_numbered_row_marker_line(line):
            break
        leading.append(line)
    return tuple(leading)


def _line_count(text: str) -> int:
    return sum(1 for line in text.splitlines() if line.strip())
