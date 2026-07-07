"""Source-block modality policy for typed evidence extraction."""

from __future__ import annotations

from llmwiki.domain.notation import standalone_formula_candidate_line
from llmwiki.domain.source_map import SourceBlock

_PROSE_RECORD_TYPES = frozenset(
    {"argument", "definition", "entity_fact", "navigation_note", "procedure_step", "rule"}
)
_BLOCK_TYPE_RECORD_TYPES: dict[str, frozenset[str]] = {
    "code": frozenset({"code_example"}),
    "table": frozenset({"table_fact"}),
    "figure": frozenset({"entity_fact", "navigation_note"}),
    "heading": frozenset(),
}


def allowed_record_types_for_source_block(block: SourceBlock) -> frozenset[str]:
    if block.block_type in _BLOCK_TYPE_RECORD_TYPES:
        return _BLOCK_TYPE_RECORD_TYPES[block.block_type]
    allowed = _PROSE_RECORD_TYPES
    if standalone_formula_candidate_line(block.source_text) is not None:
        allowed = allowed | frozenset({"formula"})
    return allowed


def record_type_allowed_for_source_block(block: SourceBlock, record_type: str) -> bool:
    return record_type in allowed_record_types_for_source_block(block)
