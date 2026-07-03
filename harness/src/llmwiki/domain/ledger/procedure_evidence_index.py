"""Source-node evidence lookup helpers for procedure planning."""

from __future__ import annotations

import re

from llmwiki.domain.ledger.atoms import TechnicalAtom
from llmwiki.domain.ledger.entries import LedgerEntry
from llmwiki.domain.ledger.ledger import ClaimLedger
from llmwiki.domain.ledger.structure import DocumentStructure, StructureNode

_SECTION_NODE_KINDS = {"chapter", "section", "heading"}


def section_nodes(structure: DocumentStructure) -> tuple[StructureNode, ...]:
    return tuple(
        node
        for node in sorted(
            (item for item in structure.structure_nodes if isinstance(item, StructureNode)),
            key=lambda item: item.source_order,
        )
        if node.structure_node_kind in _SECTION_NODE_KINDS and node.structure_node_kind != "root"
    )


def entries_by_node(ledger: ClaimLedger) -> dict[str, tuple[LedgerEntry, ...]]:
    grouped: dict[str, list[LedgerEntry]] = {}
    for entry in ledger.usable_entries:
        if entry.ledger_entry_kind == "technical-atom":
            continue
        if entry.structure_node_ids:
            grouped.setdefault(entry.structure_node_ids[0], []).append(entry)
    return {node_id: tuple(entries) for node_id, entries in grouped.items()}


def atoms_by_node(
    ledger: ClaimLedger, structure: DocumentStructure
) -> dict[str, tuple[TechnicalAtom, ...]]:
    grouped: dict[str, list[TechnicalAtom]] = {}
    sections_by_source = _section_nodes_by_source(structure)
    for entry in ledger.usable_entries:
        if entry.ledger_entry_kind != "technical-atom" or not entry.technical_atom_id:
            continue
        atom = ledger.atom(entry.technical_atom_id)
        if atom is None or not entry.structure_node_ids:
            continue
        grouped.setdefault(entry.structure_node_ids[0], []).append(atom)
    for context in ledger.technical_atom_contexts:
        atom = ledger.atom(context.technical_atom_id)
        if atom is None:
            continue
        for entry_id in context.context_entry_ids:
            context_entry = ledger.entry(entry_id)
            if context_entry is None:
                continue
            for node_id in context_entry.structure_node_ids:
                grouped.setdefault(node_id, []).append(atom)
    for atom in ledger.technical_atoms:
        node = _nearest_preceding_section_node(sections_by_source, atom)
        if node is not None:
            grouped.setdefault(node.structure_node_id, []).append(atom)
    return {node_id: tuple(atoms) for node_id, atoms in grouped.items()}


def rollup_entries(
    structure: DocumentStructure,
    grouped_entries: dict[str, tuple[LedgerEntry, ...]],
    node: StructureNode,
) -> tuple[LedgerEntry, ...]:
    node_ids = (
        node.structure_node_id,
        *(child.structure_node_id for child in structure.descendants(node.structure_node_id)),
    )
    return tuple(entry for node_id in node_ids for entry in grouped_entries.get(node_id, ()))


def rollup_atoms(
    structure: DocumentStructure,
    grouped_atoms: dict[str, tuple[TechnicalAtom, ...]],
    node: StructureNode,
) -> tuple[TechnicalAtom, ...]:
    node_ids = (
        node.structure_node_id,
        *(child.structure_node_id for child in structure.descendants(node.structure_node_id)),
    )
    return tuple(atom for node_id in node_ids for atom in grouped_atoms.get(node_id, ()))


def _section_nodes_by_source(
    structure: DocumentStructure,
) -> dict[str, tuple[StructureNode, ...]]:
    grouped: dict[str, list[StructureNode]] = {}
    for node in section_nodes(structure):
        grouped.setdefault(node.source_locator, []).append(node)
    return {
        source_locator: tuple(sorted(nodes, key=lambda node: node.source_order))
        for source_locator, nodes in grouped.items()
    }


def _nearest_preceding_section_node(
    sections_by_source: dict[str, tuple[StructureNode, ...]], atom: TechnicalAtom
) -> StructureNode | None:
    atom_order = _source_order_from_range_id(atom.source_range_id)
    if atom_order is None:
        return None
    for node in reversed(sections_by_source.get(atom.source_locator, ())):
        if node.source_order <= atom_order:
            return node
    return None


def _source_order_from_range_id(source_range_id: str) -> int | None:
    match = re.search(r"-(\d+)$", source_range_id)
    if match is None:
        return None
    return int(match.group(1))
