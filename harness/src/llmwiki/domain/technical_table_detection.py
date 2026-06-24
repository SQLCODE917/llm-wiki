"""Source-agnostic technical table detection from extracted Markdown."""

from __future__ import annotations

import re
from dataclasses import dataclass

from llmwiki.domain.evidence_registry import SourceRange, SourceText
from llmwiki.domain.source_citations import source_citation


@dataclass(frozen=True)
class DetectedTableBlock:
    block_index: int
    source_citation: str
    page_range: tuple[int, int] | None
    line_range: tuple[int, int] | None
    markdown: str
    row_count: int
    column_count: int


@dataclass(frozen=True)
class DetectedTable:
    title: str
    blocks: tuple[DetectedTableBlock, ...]


@dataclass(frozen=True)
class _RawBlock:
    unit_start_line: int
    unit_end_line: int
    title: str
    lines: tuple[str, ...]


_PAGE_MARKER_RE = re.compile(r"^\s*(?P<page>[0-9]{1,5})\s*$")


def detect_technical_tables(
    *,
    unit_text: str,
    source_text: SourceText | None,
    source_range: SourceRange,
) -> tuple[DetectedTable, ...]:
    raw_blocks = _raw_table_blocks(unit_text)
    if not raw_blocks:
        return ()
    source_lines = source_text.lines if source_text is not None else ()
    groups = _group_blocks(raw_blocks, unit_text.splitlines())
    search_start = 0
    tables: list[DetectedTable] = []
    for group in groups:
        blocks: list[DetectedTableBlock] = []
        for raw_block in group:
            line_range, search_start = _line_range(raw_block.lines, source_lines, search_start)
            page_range = _page_range(source_text, source_range, line_range)
            markdown = "\n".join(raw_block.lines)
            blocks.append(
                DetectedTableBlock(
                    block_index=len(blocks) + 1,
                    source_citation=source_citation(
                        source_range,
                        page_range=page_range,
                        line_range=None if page_range is not None else line_range,
                    ),
                    page_range=page_range,
                    line_range=line_range,
                    markdown=markdown,
                    row_count=len(raw_block.lines),
                    column_count=_column_count(raw_block.lines),
                )
            )
        tables.append(DetectedTable(title=_title(group), blocks=tuple(blocks)))
    return tuple(tables)


def _raw_table_blocks(unit_text: str) -> tuple[_RawBlock, ...]:
    lines = unit_text.splitlines()
    blocks: list[_RawBlock] = []
    current: list[str] = []
    start_line = 0
    for index, line in enumerate(lines, start=1):
        if _is_table_line(line):
            if not current:
                start_line = index
            current.append(line.strip())
            continue
        if current:
            _append_block(blocks, lines, start_line, index - 1, tuple(current))
            current = []
    if current:
        _append_block(blocks, lines, start_line, len(lines), tuple(current))
    return tuple(blocks)


def _append_block(
    blocks: list[_RawBlock],
    lines: list[str],
    start_line: int,
    end_line: int,
    table_lines: tuple[str, ...],
) -> None:
    if len(table_lines) < 2 or not any(not _is_separator_line(line) for line in table_lines):
        return
    blocks.append(
        _RawBlock(
            unit_start_line=start_line,
            unit_end_line=end_line,
            title=_caption_before(lines, start_line),
            lines=table_lines,
        )
    )


def _group_blocks(
    blocks: tuple[_RawBlock, ...], unit_lines: list[str]
) -> tuple[tuple[_RawBlock, ...], ...]:
    groups: list[list[_RawBlock]] = []
    for block in blocks:
        if not groups or not _is_continuation(groups[-1][-1], block, unit_lines):
            groups.append([block])
        else:
            groups[-1].append(block)
    return tuple(tuple(group) for group in groups)


def _is_continuation(left: _RawBlock, right: _RawBlock, unit_lines: list[str]) -> bool:
    separator = tuple(unit_lines[left.unit_end_line : right.unit_start_line - 1])
    if not separator or not all(not line.strip() or _page_marker(line) for line in separator):
        return False
    return bool(_table_terms(left.lines) & _table_terms(right.lines))


def _is_table_line(line: str) -> bool:
    stripped = line.strip()
    return stripped.startswith("|") and stripped.endswith("|") and stripped.count("|") >= 2


def _is_separator_line(line: str) -> bool:
    stripped = line.strip()
    return bool(stripped) and set(stripped) <= {"|", "-", ":", " "}


def _line_range(
    block_lines: tuple[str, ...], source_lines: tuple[str, ...], search_start: int
) -> tuple[tuple[int, int] | None, int]:
    if not source_lines:
        return None, search_start
    normalized = tuple(line.strip() for line in block_lines)
    for index in range(search_start, len(source_lines) - len(normalized) + 1):
        candidate = tuple(line.strip() for line in source_lines[index : index + len(normalized)])
        if candidate == normalized:
            line_range = (index + 1, index + len(normalized))
            return line_range, index + len(normalized)
    return None, search_start


def _page_range(
    source_text: SourceText | None,
    source_range: SourceRange,
    line_range: tuple[int, int] | None,
) -> tuple[int, int] | None:
    if source_range.line_range == line_range and source_range.page_range is not None:
        return source_range.page_range
    if source_text is None or source_text.source_text_kind != "pdf-cache" or line_range is None:
        return None
    page = _nearest_page_marker(source_text.lines, line_range[0])
    return (page, page) if page is not None else None


def _nearest_page_marker(lines: tuple[str, ...], line_number: int) -> int | None:
    for index in range(min(line_number - 1, len(lines) - 1), -1, -1):
        page = _page_marker(lines[index])
        if page is not None:
            return page
    return None


def _caption_before(lines: list[str], start_line: int) -> str:
    for line in reversed(lines[max(0, start_line - 4) : start_line - 1]):
        stripped = line.strip().strip("*_")
        if stripped and not _is_table_line(stripped) and not _page_marker(stripped):
            return stripped[:120]
    return ""


def _title(group: tuple[_RawBlock, ...]) -> str:
    for block in group:
        if block.title:
            return block.title
    terms = tuple(sorted(_table_terms(group[0].lines)))[:6]
    return "table: " + " ".join(terms) if terms else "table"


def _table_terms(lines: tuple[str, ...]) -> frozenset[str]:
    return frozenset(
        term
        for line in lines[:3]
        for term in re.findall(r"[a-z][a-z0-9-]{2,}|[0-9]{1,3}", line.lower())
        if term not in {"the", "and"}
    )


def _column_count(lines: tuple[str, ...]) -> int:
    return max(len(line.strip().strip("|").split("|")) for line in lines)


def _page_marker(line: str) -> int | None:
    match = _PAGE_MARKER_RE.match(line)
    if match is None:
        return None
    return int(match.group("page"))
