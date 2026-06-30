"""Readable source evidence blocks for page projection.

The claim ledger keeps source-close atomic entries. Evidence blocks preserve
the source statement span those entries came from, so page renderers can show a
coherent passage instead of context-dependent sentence fragments.
"""

from __future__ import annotations

from dataclasses import dataclass, replace

from llmwiki.domain.ledger.canonical import deterministic_id
from llmwiki.domain.ledger.entries import LedgerEntry
from llmwiki.domain.ledger.ledger import ClaimLedger
from llmwiki.domain.ledger.section_navigation import section_title
from llmwiki.domain.ledger.structure import DocumentStructure

_PROJECTABLE_ENTRY_KINDS = {"claim", "event", "concept"}


@dataclass(frozen=True)
class EvidenceBlock:
    evidence_block_id: str
    source_statement_id: str
    source_range_id: str
    source_range_ids: tuple[str, ...]
    source_locator: str
    source_text: str
    entry_ids: tuple[str, ...]
    structure_node_ids: tuple[str, ...]
    source_order: int
    section_label: str = ""


def build_evidence_blocks(
    ledger: ClaimLedger, structure: DocumentStructure
) -> tuple[EvidenceBlock, ...]:
    entries_by_id = {entry.ledger_entry_id: entry for entry in ledger.usable_entries}
    used_entries: set[str] = set()
    blocks: list[EvidenceBlock] = []
    order_by_range = _source_order_by_range(structure)

    for fallback_order, statement in enumerate(ledger.source_statements, start=1):
        entries = tuple(
            entry
            for entry_id in statement.derived_entry_ids
            if (entry := entries_by_id.get(entry_id)) is not None
            and entry.ledger_entry_kind in _PROJECTABLE_ENTRY_KINDS
        )
        if not entries:
            continue
        used_entries.update(entry.ledger_entry_id for entry in entries)
        blocks.append(
            _block(
                ledger,
                statement.source_statement_id,
                statement.source_range_id,
                statement.source_text,
                entries,
                order_by_range.get(statement.source_range_id, fallback_order),
                structure,
            )
        )

    for entry in ledger.usable_entries:
        if (
            entry.ledger_entry_id in used_entries
            or entry.ledger_entry_kind not in _PROJECTABLE_ENTRY_KINDS
        ):
            continue
        blocks.append(
            _block(
                ledger,
                entry.source_statement_id,
                entry.source_range_id,
                entry.source_text,
                (entry,),
                order_by_range.get(entry.source_range_id, len(blocks) + 1),
                structure,
            )
        )

    ordered = tuple(sorted(blocks, key=lambda block: (block.source_order, block.evidence_block_id)))
    return _merge_continuation_blocks(ledger, ordered)


def _block(
    ledger: ClaimLedger,
    statement_id: str,
    source_range_id: str,
    source_text: str,
    entries: tuple[LedgerEntry, ...],
    source_order: int,
    structure: DocumentStructure,
) -> EvidenceBlock:
    entry_ids = tuple(entry.ledger_entry_id for entry in entries)
    node_ids = entries[0].structure_node_ids if entries else ()
    block_id = deterministic_id(
        "evidence-block", ledger.source_hash, source_range_id, "|".join(entry_ids)
    )
    return EvidenceBlock(
        evidence_block_id=block_id,
        source_statement_id=statement_id,
        source_range_id=source_range_id,
        source_range_ids=(source_range_id,),
        source_locator=ledger.source_locator,
        source_text=source_text,
        entry_ids=entry_ids,
        structure_node_ids=node_ids,
        source_order=source_order,
        section_label=_section_label(structure, node_ids),
    )


def _section_label(structure: DocumentStructure, node_ids: tuple[str, ...]) -> str:
    if not node_ids:
        return ""
    node = structure.node(node_ids[0])
    if node is None or node.structure_node_kind == "root":
        return ""
    return section_title(structure, node)


def _source_order_by_range(structure: DocumentStructure) -> dict[str, int]:
    return {
        disposition.source_range_id: disposition.source_order
        for disposition in structure.dispositions
    }


def _merge_continuation_blocks(
    ledger: ClaimLedger, blocks: tuple[EvidenceBlock, ...]
) -> tuple[EvidenceBlock, ...]:
    merged: list[EvidenceBlock] = []
    for block in blocks:
        if merged and _should_merge(merged[-1], block):
            merged[-1] = _merge_blocks(ledger, merged[-1], block)
            continue
        merged.append(block)
    return tuple(merged)


def _should_merge(previous: EvidenceBlock, current: EvidenceBlock) -> bool:
    return bool(
        previous.source_locator == current.source_locator
        and previous.section_label == current.section_label
        and previous.structure_node_ids[:1] == current.structure_node_ids[:1]
        and 0 < current.source_order - previous.source_order <= 3
        and not _ends_sentence(previous.source_text)
        and _starts_mid_sentence(current.source_text)
    )


def _merge_blocks(
    ledger: ClaimLedger, previous: EvidenceBlock, current: EvidenceBlock
) -> EvidenceBlock:
    source_range_ids = (*previous.source_range_ids, *current.source_range_ids)
    entry_ids = (*previous.entry_ids, *current.entry_ids)
    return replace(
        previous,
        evidence_block_id=deterministic_id(
            "evidence-block", ledger.source_hash, "|".join(source_range_ids), "|".join(entry_ids)
        ),
        source_statement_id="|".join((previous.source_statement_id, current.source_statement_id)),
        source_range_ids=source_range_ids,
        source_text=" ".join((previous.source_text.rstrip(), current.source_text.lstrip())),
        entry_ids=entry_ids,
    )


def _ends_sentence(text: str) -> bool:
    stripped = text.rstrip()
    if not stripped:
        return False
    return stripped[-1] in ".!?"


def _starts_mid_sentence(text: str) -> bool:
    for char in text.lstrip():
        if char.isalpha():
            return char.islower()
        if char.isdigit():
            return False
        if char in ",;:)":
            return True
    return False
