"""Source-agnostic knowledge-shape classification.

Knowledge shapes are derived from authored structure plus typed ledger
evidence. The classifier does not key off domain nouns or source-specific
phrases; headings label the resulting objects, but do not decide their kind.
"""

from __future__ import annotations

from llmwiki.domain.ledger.atoms import TechnicalAtom
from llmwiki.domain.ledger.canonical import content_fingerprint, deterministic_id
from llmwiki.domain.ledger.entries import LedgerEntry
from llmwiki.domain.ledger.knowledge_shape_evidence import (
    UnitEvidence,
    code_atoms,
    example_atoms,
    roles_for_evidence,
    unit_has_branch,
    unit_transforms_state,
)
from llmwiki.domain.ledger.knowledge_shape_models import (
    KnowledgeShapeCandidate,
    KnowledgeShapeCatalog,
)
from llmwiki.domain.ledger.knowledge_shape_structure import (
    has_catalog_child_sequence,
    is_unanchored_container,
    leaf_shape_kind,
    procedure_child_units,
)
from llmwiki.domain.ledger.ledger import ClaimLedger
from llmwiki.domain.ledger.procedure_evidence_index import (
    atoms_by_node,
    entries_by_node,
    rollup_atoms,
    rollup_entries,
    section_nodes,
)
from llmwiki.domain.ledger.procedure_language import action_type, has_task_noun
from llmwiki.domain.ledger.structure import DocumentStructure, StructureNode

__all__ = [
    "KnowledgeShapeCandidate",
    "KnowledgeShapeCatalog",
    "build_knowledge_shape_catalog",
]


def build_knowledge_shape_catalog(
    ledger: ClaimLedger, structure: DocumentStructure
) -> KnowledgeShapeCatalog:
    grouped_entries = entries_by_node(ledger)
    grouped_atoms = atoms_by_node(ledger, structure)
    procedure_candidates = _procedure_candidates(ledger, structure, grouped_entries, grouped_atoms)
    procedure_scope = _procedure_scope_node_ids(structure, procedure_candidates)
    section_container_candidates = _section_container_candidates(
        ledger,
        structure,
        grouped_entries,
        grouped_atoms,
        procedure_scope,
    )
    flat_shape_candidates = _flat_shape_candidates(
        ledger,
        structure,
        grouped_entries,
        grouped_atoms,
        procedure_scope,
    )
    candidates = tuple(
        sorted(
            (*procedure_candidates, *section_container_candidates, *flat_shape_candidates),
            key=lambda item: item.knowledge_shape_id,
        )
    )
    fingerprint = content_fingerprint((ledger.source_locator, ledger.source_hash, candidates))
    return KnowledgeShapeCatalog(
        knowledge_shape_catalog_id=deterministic_id(
            "knowledge-shape-catalog", ledger.source_hash, fingerprint
        ),
        knowledge_shape_catalog_fingerprint=fingerprint,
        source_locator=ledger.source_locator,
        source_hash=ledger.source_hash,
        candidates=candidates,
    )

def _procedure_candidates(
    ledger: ClaimLedger,
    structure: DocumentStructure,
    grouped_entries: dict[str, tuple[LedgerEntry, ...]],
    grouped_atoms: dict[str, tuple[TechnicalAtom, ...]],
) -> tuple[KnowledgeShapeCandidate, ...]:
    candidates: list[KnowledgeShapeCandidate] = []
    for node in section_nodes(structure):
        direct_unit = _direct_unit(grouped_entries, grouped_atoms, node)
        if is_unanchored_container(node, direct_unit):
            continue
        child_units = tuple(
            _rolled_unit(structure, grouped_entries, grouped_atoms, child)
            for child in structure.children(node.structure_node_id)
        )
        child_units = tuple(unit for unit in child_units if unit.has_evidence)
        if len(child_units) < 2:
            continue
        step_units = procedure_child_units(node, child_units)
        if len(step_units) < 2:
            continue
        if has_catalog_child_sequence(node, child_units):
            continue
        state_units = tuple(
            unit for unit in step_units if _unit_transforms_procedure_state(unit)
        )
        branch_units = tuple(unit for unit in step_units if unit_has_branch(unit))
        if len(state_units) < 2:
            continue
        if (
            not branch_units
            and not any("procedure" in unit.roles for unit in step_units)
            and not has_task_noun(node.heading_text)
        ):
            continue
        entries = rollup_entries(structure, grouped_entries, node)
        atoms = rollup_atoms(structure, grouped_atoms, node)
        roles = roles_for_evidence(entries, atoms, step_units)
        score = len(step_units) + len(state_units) + len(branch_units)
        candidates.append(
            _candidate(
                "procedure",
                ledger,
                node,
                entries,
                atoms,
                tuple(unit.node.structure_node_id for unit in step_units),
                roles,
                score,
            )
        )
    return tuple(candidates)


def _unit_transforms_procedure_state(unit: UnitEvidence) -> bool:
    return unit_transforms_state(unit) or bool(action_type(unit.node.heading_text))

def _section_container_candidates(
    ledger: ClaimLedger,
    structure: DocumentStructure,
    grouped_entries: dict[str, tuple[LedgerEntry, ...]],
    grouped_atoms: dict[str, tuple[TechnicalAtom, ...]],
    procedure_scope: frozenset[str],
) -> tuple[KnowledgeShapeCandidate, ...]:
    candidates: list[KnowledgeShapeCandidate] = []
    for node in section_nodes(structure):
        if node.structure_node_id in procedure_scope:
            continue
        children = tuple(
            _rolled_unit(structure, grouped_entries, grouped_atoms, child)
            for child in structure.children(node.structure_node_id)
        )
        children = tuple(unit for unit in children if unit.has_evidence)
        if len(children) < 2:
            continue
        unit = _direct_unit(grouped_entries, grouped_atoms, node)
        if not unit.has_evidence and not children:
            continue
        entries = rollup_entries(structure, grouped_entries, node)
        atoms = rollup_atoms(structure, grouped_atoms, node)
        roles = roles_for_evidence(entries, atoms, children)
        score = len(children) + len(entries) + len(atoms)
        candidates.append(
            _candidate(
                "section-container",
                ledger,
                node,
                entries,
                atoms,
                tuple(child.node.structure_node_id for child in children),
                roles,
                score,
            )
        )
    return tuple(candidates)

def _flat_shape_candidates(
    ledger: ClaimLedger,
    structure: DocumentStructure,
    grouped_entries: dict[str, tuple[LedgerEntry, ...]],
    grouped_atoms: dict[str, tuple[TechnicalAtom, ...]],
    procedure_scope: frozenset[str],
) -> tuple[KnowledgeShapeCandidate, ...]:
    candidates: list[KnowledgeShapeCandidate] = []
    sibling_shapes = _sibling_leaf_shape_counts(structure, grouped_entries, grouped_atoms)
    for node in section_nodes(structure):
        if node.structure_node_id in procedure_scope or structure.children(node.structure_node_id):
            continue
        unit = _direct_unit(grouped_entries, grouped_atoms, node)
        shape_kind = leaf_shape_kind(node, unit)
        if shape_kind is None:
            continue
        sibling_count = sibling_shapes.get(node.parent_structure_node_id, 0)
        if shape_kind == "recipe" and sibling_count < 3 and len(code_atoms(unit.atoms)) < 2:
            continue
        roles = roles_for_evidence(unit.entries, unit.atoms, ())
        score = len(unit.entries) + (2 * len(example_atoms(unit.atoms))) + sibling_count
        candidates.append(
            _candidate(
                shape_kind,
                ledger,
                node,
                unit.entries,
                unit.atoms,
                (),
                roles,
                score,
            )
        )
    candidates.sort(key=lambda item: (item.shape_kind, -item.score, item.label))
    return tuple(candidates)


def _sibling_leaf_shape_counts(
    structure: DocumentStructure,
    grouped_entries: dict[str, tuple[LedgerEntry, ...]],
    grouped_atoms: dict[str, tuple[TechnicalAtom, ...]],
) -> dict[str, int]:
    counts: dict[str, int] = {}
    for node in section_nodes(structure):
        if structure.children(node.structure_node_id):
            continue
        unit = _direct_unit(grouped_entries, grouped_atoms, node)
        if leaf_shape_kind(node, unit) is not None:
            counts[node.parent_structure_node_id] = counts.get(node.parent_structure_node_id, 0) + 1
    return counts


def _procedure_scope_node_ids(
    structure: DocumentStructure, candidates: tuple[KnowledgeShapeCandidate, ...]
) -> frozenset[str]:
    scoped: set[str] = set()
    for candidate in candidates:
        scoped.add(candidate.structure_node_id)
        scoped.update(
            child.structure_node_id for child in structure.descendants(candidate.structure_node_id)
        )
    return frozenset(scoped)


def _rolled_unit(
    structure: DocumentStructure,
    grouped_entries: dict[str, tuple[LedgerEntry, ...]],
    grouped_atoms: dict[str, tuple[TechnicalAtom, ...]],
    node: StructureNode,
) -> UnitEvidence:
    entries = rollup_entries(structure, grouped_entries, node)
    atoms = rollup_atoms(structure, grouped_atoms, node)
    return UnitEvidence(node, entries, atoms, frozenset(roles_for_evidence(entries, atoms, ())))


def _direct_unit(
    grouped_entries: dict[str, tuple[LedgerEntry, ...]],
    grouped_atoms: dict[str, tuple[TechnicalAtom, ...]],
    node: StructureNode,
) -> UnitEvidence:
    entries = grouped_entries.get(node.structure_node_id, ())
    atoms = grouped_atoms.get(node.structure_node_id, ())
    return UnitEvidence(node, entries, atoms, frozenset(roles_for_evidence(entries, atoms, ())))


def _candidate(
    shape_kind: str,
    ledger: ClaimLedger,
    node: StructureNode,
    entries: tuple[LedgerEntry, ...],
    atoms: tuple[TechnicalAtom, ...],
    child_node_ids: tuple[str, ...],
    roles: tuple[str, ...],
    score: int,
) -> KnowledgeShapeCandidate:
    return KnowledgeShapeCandidate(
        shape_kind=shape_kind,
        knowledge_shape_id=deterministic_id(
            "knowledge-shape", ledger.source_hash, shape_kind, node.structure_node_id
        ),
        label=node.heading_text.strip(),
        structure_node_id=node.structure_node_id,
        source_range_id=node.source_range_id,
        entry_ids=tuple(entry.ledger_entry_id for entry in entries),
        atom_ids=tuple(atom.technical_atom_id for atom in atoms),
        child_structure_node_ids=child_node_ids,
        evidence_roles=roles,
        score=score,
    )
