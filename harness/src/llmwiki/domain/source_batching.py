"""Coverage-preserving batching for normalized source blocks."""

from __future__ import annotations

from dataclasses import dataclass

from llmwiki.domain.model_profile import DEFAULT_MODEL_PROFILE, ModelProfile
from llmwiki.domain.source_map import NormalizedSourceMap, SourceBlock


@dataclass(frozen=True)
class SourceBlockBatch:
    source_block_batch_id: str
    source_block_ids: tuple[str, ...]
    section_path: str
    token_estimate: int
    text: str


def estimate_tokens(text: str, model_profile: ModelProfile = DEFAULT_MODEL_PROFILE) -> int:
    return model_profile.estimate_tokens(text)


def source_block_batches(
    source_map: NormalizedSourceMap,
    *,
    budget_tokens: int | None = None,
    model_profile: ModelProfile = DEFAULT_MODEL_PROFILE,
) -> tuple[SourceBlockBatch, ...]:
    budget = budget_tokens or model_profile.source_chunk_tokens
    batches: list[SourceBlockBatch] = []
    current: list[SourceBlock] = []

    for block in _body_blocks(source_map):
        candidate = (*current, block)
        if current and model_profile.estimate_tokens(_batch_text(candidate)) > budget:
            _append_batch(batches, current, model_profile)
            current = []
        current.append(block)
    _append_batch(batches, current, model_profile)
    return tuple(batches)


def _body_blocks(source_map: NormalizedSourceMap) -> tuple[SourceBlock, ...]:
    return tuple(
        block
        for block in sorted(source_map.source_blocks, key=lambda item: item.source_order)
        if block.source_text.strip()
    )


def _append_batch(
    batches: list[SourceBlockBatch], blocks: list[SourceBlock], model_profile: ModelProfile
) -> None:
    if not blocks:
        return
    text = _batch_text(tuple(blocks))
    batches.append(
        SourceBlockBatch(
            source_block_batch_id=f"source-block-batch-{len(batches) + 1:04d}",
            source_block_ids=tuple(block.source_block_id for block in blocks),
            section_path=blocks[0].section_path,
            token_estimate=model_profile.estimate_tokens(text),
            text=text,
        )
    )


def _batch_text(blocks: tuple[SourceBlock, ...]) -> str:
    return "\n\n".join(block.source_text.strip() for block in blocks if block.source_text.strip())
