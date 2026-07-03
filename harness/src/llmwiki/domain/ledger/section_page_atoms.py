"""Technical atom selection for section-reference pages."""

from __future__ import annotations

from llmwiki.domain.ledger.atom_context import atom_context_matches
from llmwiki.domain.ledger.atoms import TechnicalAtom, atom_raw_text
from llmwiki.domain.ledger.entries import LedgerEntry
from llmwiki.domain.ledger.ledger import ClaimLedger
from llmwiki.domain.ledger.structure import DocumentStructure, StructureNode
from llmwiki.domain.ledger.table_authority import accepted_table_atom_ids
from llmwiki.domain.ledger.table_identity import (
    has_matching_table_name,
    named_table_references,
    normalize_table_name,
    table_forward_target_node_ids_by_atom_id,
    table_identity_names_by_atom_id,
    table_structure_node_ids_by_atom_id,
)
from llmwiki.domain.ledger.topic_terms import source_label_terms, topic_matcher


def atoms_for_section_entries(
    ledger: ClaimLedger,
    entries: tuple[LedgerEntry, ...],
    structure: DocumentStructure,
    node: StructureNode,
) -> tuple[TechnicalAtom, ...]:
    accepted_tables = accepted_table_atom_ids(ledger.technical_atoms)
    atom_ids = _context_supported_atom_ids(ledger, entries, node)
    atom_ids = {
        atom_id
        for atom_id in atom_ids
        if (atom := ledger.atom(atom_id)) is None
        or atom.technical_atom_kind != "table"
        or atom_id in accepted_tables
    }
    section_name = normalize_table_name(node.heading_text)
    if section_name:
        atom_node_ids = table_structure_node_ids_by_atom_id(ledger)
        forward_node_ids = table_forward_target_node_ids_by_atom_id(ledger, structure)
        section_node_ids = {
            node.structure_node_id,
            *(
                descendant.structure_node_id
                for descendant in structure.descendants(node.structure_node_id)
            ),
        }
        for atom_id, names in table_identity_names_by_atom_id(ledger, structure).items():
            valid_nodes = (*atom_node_ids.get(atom_id, ()), *forward_node_ids.get(atom_id, ()))
            if not has_matching_table_name(section_name, names):
                continue
            if section_node_ids.intersection(valid_nodes) or _forward_names_table(
                entries, ledger, structure, atom_id, names
            ):
                atom_ids.add(atom_id)
    return tuple(
        atom
        for atom in ledger.technical_atoms
        if atom.technical_atom_id in atom_ids and atom_raw_text(atom.payload).strip()
        and (atom.technical_atom_kind != "table" or atom.technical_atom_id in accepted_tables)
    )


def _context_supported_atom_ids(
    ledger: ClaimLedger, entries: tuple[LedgerEntry, ...], node: StructureNode
) -> set[str]:
    terms = tuple(source_label_terms(node.heading_text))
    matcher = topic_matcher(terms)
    return {
        entry.technical_atom_id
        for entry in entries
        if entry.ledger_entry_kind == "technical-atom"
        and entry.technical_atom_id
        and (
            matcher is None
            or atom_context_matches(ledger.atom_contexts(entry.technical_atom_id), matcher, terms)
        )
    }


def _forward_names_table(
    entries: tuple[LedgerEntry, ...],
    ledger: ClaimLedger,
    structure: DocumentStructure,
    atom_id: str,
    table_names: tuple[str, ...],
) -> bool:
    atom = ledger.atom(atom_id)
    if atom is None:
        return False
    table_order = _source_order(structure, atom.source_range_id)
    if table_order <= 0:
        return False
    for entry in entries:
        entry_order = _source_order(structure, entry.source_range_id)
        if entry_order <= 0 or entry_order >= table_order or table_order - entry_order > 32:
            continue
        references = named_table_references(entry.normalized_text or entry.source_text)
        if any(has_matching_table_name(reference, table_names) for reference in references):
            return True
    return False


def _source_order(structure: DocumentStructure, source_range_id: str) -> int:
    for disposition in structure.dispositions:
        if disposition.source_range_id == source_range_id:
            return disposition.source_order
    return 0
