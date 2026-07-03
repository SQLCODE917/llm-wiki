"""Materialize source-equivalent table payloads."""

from __future__ import annotations

import re

from llmwiki.domain.ledger.atoms import TableCell, TableColumn, TablePayload, TableRow
from llmwiki.domain.ledger.common import ReviewReason
from llmwiki.domain.ledger.segments import SourceSegment
from llmwiki.domain.ledger.table_cell_normalize import normalize_table_cell_text
from llmwiki.domain.ledger.tabular import inline_row_marker_spans, range_value_entries

_ENUMERATED_LINE = re.compile(r"^\s*(?:[-*]\s*)?(\d+)[\s.)]+(.*)$")
_NUMERIC_MARKER_LINE = re.compile(r"^\s*(?:[-*]\s*)?(\d+)\s*$")
_TABLE_CAPTION = re.compile(r"^\s*(?:table|tab\.)\s*(?:[-:.]|\d+\b)?\s*(.*)$", re.IGNORECASE)
_SPACED_COLUMN = re.compile(r"\S.*?\s{2,}\S")


def materialize_table(segment: SourceSegment) -> tuple[TablePayload, ReviewReason | None]:
    raw = segment.text
    caption = _table_caption(raw)
    columns, rows, cells, status = _parse_pipe_table(raw)
    if status == "parsed":
        return TablePayload(
            raw, status, segment.source_locator, columns, rows, cells, caption
        ), None
    columns, rows, cells = _parse_spaced_table(raw)
    if cells:
        reason = ReviewReason(
            "partial-parse", "table parsed from aligned text columns", segment.evidence_ids
        )
        return (
            TablePayload(
                raw, "partially-parsed", segment.source_locator, columns, rows, cells, caption
            ),
            reason,
        )
    columns, rows, cells = _parse_enumerated_table(raw)
    if cells:
        reason = ReviewReason(
            "partial-parse", "table parsed as enumerated rows", segment.evidence_ids
        )
        return (
            TablePayload(
                raw, "partially-parsed", segment.source_locator, columns, rows, cells, caption
            ),
            reason,
        )
    reason = ReviewReason(
        "unparsed", "table structure not recovered; raw text preserved", segment.evidence_ids
    )
    return TablePayload(raw, "unparsed", segment.source_locator, caption=caption), reason


def _parse_pipe_table(
    raw: str,
) -> tuple[tuple[TableColumn, ...], tuple[TableRow, ...], tuple[TableCell, ...], str]:
    rows = [line for line in raw.splitlines() if line.strip().startswith("|") or "|" in line]
    grid = [
        tuple(normalize_table_cell_text(cell) for cell in line.strip().strip("|").split("|"))
        for line in rows
    ]
    grid = [row for row in grid if any(cell for cell in row)]
    if len(grid) < 2 or not _is_separator(grid[1]):
        return (), (), (), "failed"
    headers = grid[0]
    columns = tuple(TableColumn(i, header) for i, header in enumerate(headers))
    body = grid[2:]
    table_rows = tuple(TableRow(i) for i in range(len(body)))
    cells = tuple(
        TableCell(r, c, value)
        for r, row in enumerate(body)
        for c, value in enumerate(row)
        if c < len(headers)
    )
    return columns, table_rows, cells, "parsed"


def _parse_spaced_table(
    raw: str,
) -> tuple[tuple[TableColumn, ...], tuple[TableRow, ...], tuple[TableCell, ...]]:
    lines = [line.rstrip() for line in raw.splitlines() if line.strip()]
    grid = [_split_spaced_row(line) for line in lines if _SPACED_COLUMN.search(line)]
    grid = [row for row in grid if len(row) >= 2]
    if len(grid) < 3:
        return (), (), ()
    header_index = next((index for index, row in enumerate(grid) if _header_like(row)), 0)
    headers = grid[header_index]
    body = [row for row in grid[header_index + 1 :] if len(row) >= 2]
    if len(body) < 2:
        return (), (), ()
    width = len(headers)
    columns = tuple(TableColumn(index, header) for index, header in enumerate(headers))
    rows = tuple(TableRow(index) for index in range(len(body)))
    cells = tuple(
        TableCell(row_index, column_index, cell)
        for row_index, row in enumerate(body)
        for column_index, cell in enumerate(row[:width])
    )
    return columns, rows, cells


def _split_spaced_row(line: str) -> tuple[str, ...]:
    return tuple(
        normalize_table_cell_text(cell)
        for cell in re.split(r"\s{2,}", line.strip())
        if cell.strip()
    )


def _header_like(row: tuple[str, ...]) -> bool:
    if len(row) < 2:
        return False
    alpha = sum(1 for cell in row if any(ch.isalpha() for ch in cell))
    return alpha >= max(2, len(row) - 1)


def _is_separator(row: tuple[str, ...]) -> bool:
    return all(set(cell) <= set("-: ") and "-" in cell for cell in row if cell)


def _parse_enumerated_table(
    raw: str,
) -> tuple[tuple[TableColumn, ...], tuple[TableRow, ...], tuple[TableCell, ...]]:
    entries = _enumerated_entries(raw)
    if len(entries) < 2:
        return (), (), ()
    columns = (TableColumn(0, "entry"), TableColumn(1, "content"))
    rows = tuple(TableRow(i) for i in range(len(entries)))
    cells = tuple(
        cell
        for i, (key, value) in enumerate(entries)
        for cell in (TableCell(i, 0, key), TableCell(i, 1, value))
    )
    return columns, rows, cells


def _enumerated_entries(raw: str) -> tuple[tuple[str, str], ...]:
    lines = [_clean_line(line) for line in raw.splitlines() if _clean_line(line)]
    entries = _line_enumerated_entries(lines)
    if len(entries) >= 2:
        return entries
    flat = " ".join(raw.split())
    ranged = range_value_entries(flat)
    if ranged:
        return ranged
    return _inline_entries(flat, minimum=3)


def _line_enumerated_entries(lines: list[str]) -> tuple[tuple[str, str], ...]:
    line_entries: list[tuple[str, str]] = []
    pending_prefix: list[str] = []
    current_key = ""
    current_parts: list[str] = []
    for index, line in enumerate(lines):
        if _punctuation_only(line):
            continue
        multi = _inline_entries(line, minimum=2)
        if multi:
            _flush_entry(line_entries, current_key, current_parts)
            current_key, current_parts = "", []
            line_entries.extend(multi)
            pending_prefix = []
            continue
        match = _ENUMERATED_LINE.match(line)
        if match and match.group(2).strip():
            _flush_entry(line_entries, current_key, current_parts)
            current_key, current_parts = "", []
            content = match.group(2).strip()
            if pending_prefix:
                content = f"{' '.join(pending_prefix)} {content}"
                pending_prefix = []
            line_entries.append((match.group(1), content))
            continue
        marker = _NUMERIC_MARKER_LINE.match(line)
        if marker is not None:
            _flush_entry(line_entries, current_key, current_parts)
            current_key = marker.group(1)
            current_parts = pending_prefix
            pending_prefix = []
            continue
        if current_key:
            if (
                current_parts
                and _looks_like_next_row_prefix(line, current_parts)
                and _next_marker_after_prefix(lines, index)
            ):
                _flush_entry(line_entries, current_key, current_parts)
                current_key, current_parts = "", []
                pending_prefix.append(line)
            else:
                current_parts.append(line)
        elif line_entries and _looks_like_next_row_prefix(line):
            pending_prefix.append(line)
        elif line_entries:
            key, content = line_entries[-1]
            line_entries[-1] = (key, f"{content} {line}".strip())
    _flush_entry(line_entries, current_key, current_parts)
    return tuple(line_entries)


def _flush_entry(entries: list[tuple[str, str]], key: str, parts: list[str]) -> None:
    content = " ".join(part for part in parts if part).strip()
    if key and content:
        entries.append((key, content))


def _inline_entries(text: str, *, minimum: int) -> tuple[tuple[str, str], ...]:
    markers = list(inline_row_marker_spans(text))
    if len(markers) < minimum:
        return ()
    entries: list[tuple[str, str]] = []
    for index, (value, _start, content_start) in enumerate(markers):
        content_end = markers[index + 1][1] if index + 1 < len(markers) else len(text)
        content = text[content_start:content_end].strip()
        if content:
            entries.append((str(value), content))
    return tuple(entries)


def _clean_line(line: str) -> str:
    return normalize_table_cell_text(line)


def _punctuation_only(line: str) -> bool:
    return bool(line) and not any(char.isalnum() for char in line)


def _next_marker_after_prefix(lines: list[str], index: int) -> bool:
    for line in lines[index + 1 : index + 4]:
        if _punctuation_only(line):
            continue
        return bool(_ENUMERATED_LINE.match(line) or _NUMERIC_MARKER_LINE.match(line))
    return False


def _looks_like_next_row_prefix(line: str, current_parts: list[str] | None = None) -> bool:
    if not line[:1].isalnum():
        return False
    if line[:1].islower():
        return False
    words = line.split()
    if len(words) > 14:
        return False
    if ":" in line:
        return True
    if not line.endswith((".", "!", "?")):
        return True
    return _parts_end_sentence(current_parts or [])


def _parts_end_sentence(parts: list[str]) -> bool:
    return bool(parts) and parts[-1].rstrip().endswith((".", "!", "?"))


def _table_caption(raw: str) -> str:
    for line in raw.splitlines()[:3]:
        match = _TABLE_CAPTION.match(line.strip())
        if match is not None:
            return " ".join(line.split())
    return ""
