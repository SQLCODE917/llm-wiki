"""Technical atom frames for readable page projection.

Technical atoms are exact source-equivalent payloads. Frames group adjacent
atoms that form one source record, such as a spell stat block or table record,
and attach the closest prose evidence block as projection context.
"""

from __future__ import annotations

from dataclasses import dataclass

from llmwiki.domain.ledger.canonical import deterministic_id
from llmwiki.domain.ledger.entries import LedgerEntry
from llmwiki.domain.ledger.evidence_blocks import EvidenceBlock
from llmwiki.domain.ledger.ledger import ClaimLedger
from llmwiki.domain.ledger.section_navigation import section_title
from llmwiki.domain.ledger.structure import DocumentStructure

_FRAMEABLE_ATOM_KINDS = {"formula"}
_CONTEXT_WINDOW = 8


@dataclass(frozen=True)
class TechnicalAtomFrame:
    atom_frame_id: str
    label: str
    atom_ids: tuple[str, ...]
    source_range_ids: tuple[str, ...]
    source_locator: str
    technical_atom_kind: str
    structure_node_ids: tuple[str, ...]
    source_order: int
    context_block_id: str = ""


def build_atom_frames(
    ledger: ClaimLedger,
    structure: DocumentStructure,
    evidence_blocks: tuple[EvidenceBlock, ...],
) -> tuple[TechnicalAtomFrame, ...]:
    entries = _technical_atom_entries(ledger)
    source_order_by_range = _source_order_by_range(structure)
    ordered = sorted(
        entries,
        key=lambda entry: (_source_order(source_order_by_range, entry), entry.source_range_id),
    )
    groups: list[list[LedgerEntry]] = []
    for entry in ordered:
        if groups and _can_join(groups[-1][-1], entry, source_order_by_range):
            groups[-1].append(entry)
        else:
            groups.append([entry])
    return tuple(
        _frame(ledger, structure, tuple(group), evidence_blocks, source_order_by_range)
        for group in groups
        if group
    )


def _technical_atom_entries(ledger: ClaimLedger) -> tuple[LedgerEntry, ...]:
    return tuple(
        entry
        for entry in ledger.usable_entries
        if entry.ledger_entry_kind == "technical-atom" and entry.technical_atom_id
    )


def _can_join(
    left: LedgerEntry,
    right: LedgerEntry,
    source_order_by_range: dict[str, int],
) -> bool:
    if left.technical_atom_kind not in _FRAMEABLE_ATOM_KINDS:
        return False
    if left.technical_atom_kind != right.technical_atom_kind:
        return False
    if _nearest_node(left) != _nearest_node(right):
        return False
    return (
        _source_order(source_order_by_range, right) - _source_order(source_order_by_range, left)
        <= 2
    )


def _frame(
    ledger: ClaimLedger,
    structure: DocumentStructure,
    entries: tuple[LedgerEntry, ...],
    evidence_blocks: tuple[EvidenceBlock, ...],
    source_order_by_range: dict[str, int],
) -> TechnicalAtomFrame:
    atoms = tuple(
        atom for entry in entries if (atom := ledger.atom(entry.technical_atom_id)) is not None
    )
    atom_ids = tuple(atom.technical_atom_id for atom in atoms)
    source_range_ids = tuple(atom.source_range_id for atom in atoms)
    first = entries[0]
    node_ids = first.structure_node_ids
    node_id = _nearest_node(first)
    label = _frame_label(structure, node_id)
    source_order = _source_order(source_order_by_range, first)
    frame_id = deterministic_id(
        "technical-atom-frame",
        ledger.source_hash,
        node_id,
        "|".join(atom_ids),
    )
    return TechnicalAtomFrame(
        atom_frame_id=frame_id,
        label=label,
        atom_ids=atom_ids,
        source_range_ids=source_range_ids,
        source_locator=ledger.source_locator,
        technical_atom_kind=first.technical_atom_kind,
        structure_node_ids=node_ids,
        source_order=source_order,
        context_block_id=_nearest_context_block_id(evidence_blocks, node_id, source_order),
    )


def _frame_label(structure: DocumentStructure, node_id: str) -> str:
    node = structure.node(node_id)
    if node is None:
        return "Source record"
    return section_title(structure, node)


def _nearest_context_block_id(
    evidence_blocks: tuple[EvidenceBlock, ...], node_id: str, source_order: int
) -> str:
    same_node = [
        block
        for block in evidence_blocks
        if block.structure_node_ids and block.structure_node_ids[0] == node_id
    ]
    following = [
        block for block in same_node if 0 < block.source_order - source_order <= _CONTEXT_WINDOW
    ]
    if following:
        return min(following, key=lambda block: block.source_order).evidence_block_id
    previous = [
        block for block in same_node if 0 < source_order - block.source_order <= _CONTEXT_WINDOW
    ]
    if previous:
        return max(previous, key=lambda block: block.source_order).evidence_block_id
    return ""


def _nearest_node(entry: LedgerEntry) -> str:
    return entry.structure_node_ids[0] if entry.structure_node_ids else ""


def _source_order_by_range(structure: DocumentStructure) -> dict[str, int]:
    return {
        disposition.source_range_id: disposition.source_order
        for disposition in structure.dispositions
    }


def _source_order(source_order_by_range: dict[str, int], entry: LedgerEntry) -> int:
    return source_order_by_range.get(entry.source_range_id, 0)
