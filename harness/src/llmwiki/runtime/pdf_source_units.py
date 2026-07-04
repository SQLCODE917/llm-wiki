"""Map normalized PDF source maps into page-plan extracted units."""

from __future__ import annotations

from pathlib import Path

from llmwiki.domain.objects import ExtractedUnit, RawSource
from llmwiki.domain.planning_analysis import build_extracted_unit
from llmwiki.domain.source_map import (
    NormalizedSourceMap,
    PromptWindow,
    SourceBlock,
    build_prompt_windows,
)
from llmwiki.pdf.chunking import CHUNK_TOKEN_BUDGET, estimate_tokens
from llmwiki.pdf.pipeline import read_source_map


def extracted_units_from_pdf_cache(
    raw_source: RawSource, cache_dir: Path
) -> tuple[ExtractedUnit, ...]:
    source_map = read_source_map(cache_dir)
    if source_map is None:
        raise ValueError(f"missing normalized source map in {cache_dir}")
    return extracted_units_from_source_map(raw_source, source_map)


def extracted_units_from_source_map(
    raw_source: RawSource,
    source_map: NormalizedSourceMap,
    *,
    budget_tokens: int = CHUNK_TOKEN_BUDGET,
) -> tuple[ExtractedUnit, ...]:
    windows = build_prompt_windows(
        source_map,
        budget_tokens=budget_tokens,
        estimate_tokens=estimate_tokens,
    )
    blocks_by_id = source_map.source_blocks_by_id
    return tuple(
        _unit_from_window(raw_source, blocks_by_id, window)
        for window in windows
        if window.text.strip()
    )


def _unit_from_window(
    raw_source: RawSource,
    blocks_by_id: dict[str, SourceBlock],
    window: PromptWindow,
) -> ExtractedUnit:
    blocks = tuple(
        block
        for block_id in window.source_block_ids
        if (block := blocks_by_id.get(block_id)) is not None
    )
    return build_extracted_unit(
        unit_id=window.prompt_window_id,
        raw_source=raw_source,
        locator=_page_locator(blocks),
        heading_path=_heading_path(blocks),
        text=window.text,
    )


def _page_locator(blocks: tuple[SourceBlock, ...]) -> str:
    starts = [block.page_span[0] for block in blocks if block.page_span[0] > 0]
    ends = [block.page_span[1] for block in blocks if block.page_span[1] > 0]
    if not starts or not ends:
        return "document"
    start, end = min(starts), max(ends)
    return f"p.{start}" if start == end else f"p.{start}-{end}"


def _heading_path(blocks: tuple[SourceBlock, ...]) -> str:
    for block in blocks:
        if block.block_type != "heading" and block.section_path != "Document":
            return block.section_path
    for block in blocks:
        if block.section_path:
            return block.section_path
    return "Document"
