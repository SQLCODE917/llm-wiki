"""Source-neutral table-grid reconstruction from PDF line geometry."""

from __future__ import annotations

import re
from dataclasses import dataclass

from llmwiki.pdf.layout_lines import TextLine, WordBox

_CAPTION = re.compile(r"^\s*(?:table|tab\.)\b", re.IGNORECASE)
_GROUP_WORD_LIMIT = 3


@dataclass(frozen=True)
class ReconstructedTableGrid:
    raw_text: str
    row_count: int
    column_count: int
    confidence: str
    issues: tuple[str, ...] = ()


@dataclass(frozen=True)
class _DataRow:
    group: str
    cells: tuple[str, ...]


def reconstruct_table_grid(lines: tuple[TextLine, ...]) -> ReconstructedTableGrid | None:
    """Rebuild a trustworthy markdown grid from stream-style table geometry."""
    if len(lines) < 4:
        return None
    caption, body = _split_caption(lines)
    header_index = _header_index(body)
    if header_index is None:
        return None
    spans = _header_spans(body[header_index])
    if len(spans) < 3:
        return None
    headers, data_start = _headers(body, header_index, spans)
    rows = _data_rows(body[data_start:], spans)
    if len(rows) < 2 or not _rows_trustworthy(rows):
        return None
    table = _markdown_table(headers, rows, _has_groups(rows))
    raw = f"{caption}\n{table}" if caption else table
    return ReconstructedTableGrid(raw, len(rows), len(headers), "high")


def _split_caption(lines: tuple[TextLine, ...]) -> tuple[str, tuple[TextLine, ...]]:
    if lines and _CAPTION.match(lines[0].text):
        return lines[0].text, lines[1:]
    return "", lines


def _header_index(lines: tuple[TextLine, ...]) -> int | None:
    candidates = [
        (index, _header_score(line))
        for index, line in enumerate(lines[:8])
        if _header_score(line) >= 3
    ]
    return max(candidates, key=lambda item: item[1])[0] if candidates else None


def _header_score(line: TextLine) -> int:
    words = [word for word in line.words if any(char.isalpha() for char in word.text)]
    if len(words) < 3:
        return 0
    spread = max(word.x1 for word in words) - min(word.x0 for word in words)
    return len(words) if spread >= 90.0 else 0


def _header_spans(line: TextLine) -> tuple[tuple[float, float], ...]:
    return tuple((word.x0, word.x1) for word in line.words)


def _headers(
    lines: tuple[TextLine, ...], header_index: int, spans: tuple[tuple[float, float], ...]
) -> tuple[tuple[str, ...], int]:
    headers = [_clean(word.text) for word in lines[header_index].words]
    index = header_index + 1
    while index < len(lines):
        cells = _line_cells(lines[index], spans)
        filled = _filled_columns(cells)
        if not filled:
            index += 1
            continue
        if 0 in filled or len(filled) > 2 or _line_has_data_value(lines[index]):
            break
        for column in filled:
            headers[column] = _join(headers[column], cells[column])
        index += 1
    return tuple(headers), index


def _data_rows(
    lines: tuple[TextLine, ...], spans: tuple[tuple[float, float], ...]
) -> tuple[_DataRow, ...]:
    records = tuple((line, _line_cells(line, spans)) for line in lines)
    row_specs: list[tuple[int, str]] = []
    current_group: list[str] = []
    group_indices: set[int] = set()
    for index, (line, cells) in enumerate(records):
        filled = _filled_columns(cells)
        if not filled:
            continue
        if _group_line(line, cells, filled):
            group_indices.add(index)
            current_group.append(cells[0])
            continue
        if _starts_data_row(cells, filled):
            row_specs.append((index, _join(*current_group)))
            current_group = []
    rows: list[_DataRow] = []
    row_indices = tuple(index for index, _group in row_specs)
    positions = _ordered_positions(tuple(line for line, _cells in records))
    for row_index, (_start_index, group) in enumerate(row_specs):
        assigned = [
            cells
            for index, (_line, cells) in enumerate(records)
            if index not in group_indices
            and _nearest_row(index, positions, row_indices) == row_index
        ]
        row = [""] * len(spans)
        for cells in assigned:
            _merge_cells(row, cells)
        rows.append(_DataRow(group, tuple(row)))
    return tuple(rows)


def _line_cells(line: TextLine, spans: tuple[tuple[float, float], ...]) -> tuple[str, ...]:
    buckets: list[list[WordBox]] = [[] for _ in spans]
    for word in line.words:
        buckets[_column_index(word, spans)].append(word)
    return tuple(_clean(" ".join(word.text for word in bucket)) for bucket in buckets)


def _column_index(word: WordBox, spans: tuple[tuple[float, float], ...]) -> int:
    return min(range(len(spans)), key=lambda index: abs(word.x0 - spans[index][0]))


def _filled_columns(cells: tuple[str, ...]) -> set[int]:
    return {index for index, cell in enumerate(cells) if cell}


def _starts_data_row(cells: tuple[str, ...], filled: set[int]) -> bool:
    return 0 in filled and len(filled) >= 2 and not _continues_first_cell(cells, filled)


def _continues_first_cell(cells: tuple[str, ...], filled: set[int]) -> bool:
    return 0 in filled and cells[0][:1].islower()


def _ordered_positions(lines: tuple[TextLine, ...]) -> tuple[float, ...]:
    positions: list[float] = []
    offset = 0.0
    previous_page = lines[0].page_index if lines else 0
    for line in lines:
        if positions and line.page_index != previous_page:
            offset = positions[-1] + 12.0 - line.cy
        positions.append(line.cy + offset)
        previous_page = line.page_index
    return tuple(positions)


def _nearest_row(
    index: int, positions: tuple[float, ...], row_indices: tuple[int, ...]
) -> int | None:
    if not row_indices:
        return None
    return min(
        range(len(row_indices)),
        key=lambda row_index: abs(positions[index] - positions[row_indices[row_index]]),
    )


def _group_line(line: TextLine, cells: tuple[str, ...], filled: set[int]) -> bool:
    words = cells[0].split()
    return (
        filled == {0}
        and 1 <= len(words) <= _GROUP_WORD_LIMIT
        and not _line_has_data_value(line)
        and all(word[:1].isupper() for word in words if word)
    )


def _line_has_data_value(line: TextLine) -> bool:
    return any(
        any(char.isdigit() for char in word.text) or word.text in {"-", "+", "+2"}
        for word in line.words
    )


def _merge_cells(target: list[str], cells: tuple[str, ...]) -> None:
    for index, cell in enumerate(cells):
        if cell:
            target[index] = _join(target[index], cell)


def _rows_trustworthy(rows: tuple[_DataRow, ...]) -> bool:
    useful = sum(1 for row in rows if sum(1 for cell in row.cells if cell) >= 2)
    return useful >= max(2, int(len(rows) * 0.8))


def _has_groups(rows: tuple[_DataRow, ...]) -> bool:
    return any(row.group for row in rows)


def _markdown_table(headers: tuple[str, ...], rows: tuple[_DataRow, ...], groups: bool) -> str:
    columns = ("Category", *headers) if groups else headers
    lines = [_markdown_row(columns), _markdown_row(tuple("---" for _ in columns))]
    for row in rows:
        values = (row.group, *row.cells) if groups else row.cells
        lines.append(_markdown_row(values))
    return "\n".join(lines)


def _markdown_row(values: tuple[str, ...]) -> str:
    return "| " + " | ".join(_escape(value) for value in values) + " |"


def _escape(value: str) -> str:
    return _clean(value).replace("|", "\\|")


def _join(*parts: str) -> str:
    return _clean(" ".join(part for part in parts if part))


def _clean(text: str) -> str:
    return " ".join(text.split())
