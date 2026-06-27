"""Materialize source-equivalent table payloads."""

from __future__ import annotations

import re

from llmwiki.domain.ledger.atoms import TableCell, TableColumn, TablePayload, TableRow
from llmwiki.domain.ledger.common import ReviewReason
from llmwiki.domain.ledger.segments import SourceSegment
from llmwiki.domain.ledger.tabular import inline_row_marker_spans, range_value_entries

_ENUMERATED_LINE = re.compile(r"^\s*(?:[-*]\s*)?(\d+)[\s.)]+(.*)$")
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
    grid = [tuple(cell.strip() for cell in line.strip().strip("|").split("|")) for line in rows]
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
    return tuple(cell.strip() for cell in re.split(r"\s{2,}", line.strip()) if cell.strip())


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
    line_entries: list[tuple[str, str]] = []
    pending_prefix: list[str] = []
    for line in raw.splitlines():
        line = line.strip()
        if not line:
            continue
        multi = _inline_entries(line, minimum=2)
        if multi:
            line_entries.extend(multi)
            pending_prefix = []
            continue
        match = _ENUMERATED_LINE.match(line)
        if match and match.group(2).strip():
            content = match.group(2).strip()
            if pending_prefix:
                content = f"{' '.join(pending_prefix)} {content}"
                pending_prefix = []
            line_entries.append((match.group(1), content))
        elif line_entries and _looks_like_next_row_prefix(line):
            pending_prefix.append(line)
        elif line_entries:
            key, content = line_entries[-1]
            line_entries[-1] = (key, f"{content} {line}".strip())
    if len(line_entries) >= 2:
        return tuple(line_entries)
    flat = " ".join(raw.split())
    ranged = range_value_entries(flat)
    if ranged:
        return ranged
    return _inline_entries(flat, minimum=3)


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


def _looks_like_next_row_prefix(line: str) -> bool:
    words = line.split()
    if len(words) > 14:
        return False
    if ":" in line:
        return True
    return not line.endswith((".", "!", "?"))


def _table_caption(raw: str) -> str:
    for line in raw.splitlines()[:3]:
        match = _TABLE_CAPTION.match(line.strip())
        if match is not None:
            return " ".join(line.split())
    return ""
