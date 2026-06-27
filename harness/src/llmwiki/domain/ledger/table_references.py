"""Detect source text that refers to a named table artifact."""

from __future__ import annotations

from llmwiki.domain.ledger.atoms import TablePayload
from llmwiki.domain.ledger.ledger import ClaimLedger
from llmwiki.domain.ledger.structure import DocumentStructure
from llmwiki.domain.ledger.table_identity import (
    explicit_forward_reference,
    has_matching_table_name,
    named_table_references,
    table_identity_names,
)


def unresolved_table_reference_entry_ids(
    ledger: ClaimLedger, structure: DocumentStructure | None = None
) -> tuple[str, ...]:
    """Ledger entries that refer to named tables not materialized as table atoms."""
    table_names = table_identity_names(ledger, structure)
    source_order = _source_order(structure)
    unresolved: list[str] = []
    for entry in ledger.entries:
        if entry.ledger_entry_kind == "technical-atom":
            continue
        refs = named_table_references(entry.source_text)
        if not refs:
            continue
        named_match = any(has_matching_table_name(ref, table_names) for ref in refs)
        nearby_table = _following_table_within(ledger, entry.source_range_id, source_order, 8)
        forward_table = explicit_forward_reference(entry.source_text) and _following_table_within(
            ledger, entry.source_range_id, source_order, 32
        )
        if not (named_match or nearby_table or forward_table):
            unresolved.append(entry.ledger_entry_id)
    return tuple(unresolved)


def _source_order(structure: DocumentStructure | None) -> dict[str, int]:
    if structure is None:
        return {}
    return {
        disposition.source_range_id: disposition.source_order
        for disposition in structure.dispositions
    }


def _following_table_within(
    ledger: ClaimLedger, source_range_id: str, source_order: dict[str, int], distance: int
) -> bool:
    if not source_order or source_range_id not in source_order:
        return False
    entry_order = source_order[source_range_id]
    for atom in ledger.technical_atoms:
        if atom.technical_atom_kind != "table" or not isinstance(atom.payload, TablePayload):
            continue
        atom_order = source_order.get(atom.source_range_id)
        if atom_order is not None and entry_order < atom_order <= entry_order + distance:
            return True
    return False
