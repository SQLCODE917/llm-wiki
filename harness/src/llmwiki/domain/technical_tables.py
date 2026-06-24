"""Preserved technical table domain objects."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class TechnicalTableBlock:
    technical_table_block_id: str
    block_index: int
    source_citation: str
    page_range: tuple[int, int] | None
    line_range: tuple[int, int] | None
    markdown: str
    row_count: int
    column_count: int

    def __post_init__(self) -> None:
        if not self.technical_table_block_id:
            raise ValueError("TechnicalTableBlock requires an id.")
        if self.block_index < 1:
            raise ValueError("TechnicalTableBlock block_index must be positive.")
        if not self.source_citation.strip():
            raise ValueError("TechnicalTableBlock requires a source citation.")
        if not self.markdown.strip():
            raise ValueError("TechnicalTableBlock requires markdown.")
        if self.row_count < 1 or self.column_count < 1:
            raise ValueError("TechnicalTableBlock requires row and column counts.")
        _validate_range(self.page_range, "page_range")
        _validate_range(self.line_range, "line_range")


@dataclass(frozen=True)
class TechnicalTable:
    technical_table_id: str
    source_locator: str
    page_id: str
    title: str
    blocks: tuple[TechnicalTableBlock, ...]
    source_claim_ids: tuple[str, ...]
    evidence_ids: tuple[str, ...]

    def __post_init__(self) -> None:
        if not self.technical_table_id:
            raise ValueError("TechnicalTable requires an id.")
        if not self.source_locator or not self.page_id:
            raise ValueError("TechnicalTable requires source and page ids.")
        if not self.title.strip():
            raise ValueError("TechnicalTable requires a title.")
        if not self.blocks:
            raise ValueError("TechnicalTable requires at least one block.")
        if not self.evidence_ids:
            raise ValueError("TechnicalTable requires at least one evidence id.")
        expected = tuple(range(1, len(self.blocks) + 1))
        actual = tuple(block.block_index for block in self.blocks)
        if actual != expected:
            raise ValueError("TechnicalTableBlock indexes must be contiguous.")

    @property
    def source_citation(self) -> str:
        return self.blocks[0].source_citation

    @property
    def markdown(self) -> str:
        return "\n\n".join(block.markdown for block in self.blocks)

    @property
    def block_count(self) -> int:
        return len(self.blocks)


def _validate_range(value: tuple[int, int] | None, field_name: str) -> None:
    if value is None:
        return
    start, end = value
    if start < 1 or end < start:
        raise ValueError(f"TechnicalTableBlock {field_name} must be positive and ordered.")
