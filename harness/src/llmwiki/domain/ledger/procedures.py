"""Procedure ontology and source-grounded procedure page projection."""

from __future__ import annotations

import re
from dataclasses import dataclass

from llmwiki.domain.ledger.atoms import TechnicalAtom, atom_raw_text
from llmwiki.domain.ledger.entries import LedgerEntry
from llmwiki.domain.ledger.ledger import ClaimLedger
from llmwiki.domain.ledger.procedure_decisions import DecisionPoint, plan_decision_points
from llmwiki.domain.ledger.procedure_language import (
    action_type,
    clean_title,
    goal_sentence,
    goal_title,
    has_condition,
    has_task_noun,
    is_step_heading,
    step_title,
)
from llmwiki.domain.ledger.procedure_state_flow import (
    ProcedureStateFlow,
    ProcedureStepEvidence,
    build_procedure_state_flow,
)
from llmwiki.domain.ledger.section_navigation import section_page_id
from llmwiki.domain.ledger.structure import DocumentStructure, StructureNode
from llmwiki.domain.pages import slugify

PAGE_FAMILY_PROCEDURE_GUIDE = "procedure-guide"

_SECTION_NODE_KINDS = {"chapter", "section", "heading"}
_MAX_PROCEDURE_PAGES = 64
_STRUCTURAL_CONTAINER_PREFIX = re.compile(
    r"^(chapter|part|appendix|volume|book)\b(?:\s+[ivxlcdm\d]+)?\s*:?\s*(.*)$",
    re.IGNORECASE,
)


@dataclass(frozen=True)
class ProcedureStep:
    sequence: int
    title: str
    action_type: str
    heading_action_type: str
    section_page_id: str
    claims: tuple[LedgerEntry, ...]
    technical_atoms: tuple[TechnicalAtom, ...]


@dataclass(frozen=True)
class ProcedureGuide:
    procedure_id: str
    title: str
    goal: str
    source_node: StructureNode
    source_section_page_id: str
    steps: tuple[ProcedureStep, ...]
    decision_points: tuple[DecisionPoint, ...]
    technical_atoms: tuple[TechnicalAtom, ...]
    state_flow: ProcedureStateFlow


def plan_procedure_guides(
    ledger: ClaimLedger, structure: DocumentStructure, *, source_page_id: str
) -> tuple[ProcedureGuide, ...]:
    entries_by_node = _entries_by_node(ledger)
    atoms_by_node = _atoms_by_node(ledger, structure)
    guides: list[ProcedureGuide] = []
    for node in _section_nodes(structure):
        direct_entries = entries_by_node.get(node.structure_node_id, ())
        direct_atoms = atoms_by_node.get(node.structure_node_id, ())
        if _is_unanchored_structural_container(node, direct_entries, direct_atoms):
            continue
        entries = _rollup_entries(structure, entries_by_node, node)
        atoms = _rollup_atoms(structure, atoms_by_node, node)
        children = tuple(child for child in structure.children(node.structure_node_id))
        steps = _steps_for_children(
            structure,
            entries_by_node,
            atoms_by_node,
            children,
            source_page_id,
        )
        if _candidate_score(node, entries, atoms, steps) < 6:
            continue
        if len(steps) < 2:
            continue
        state_flow = _state_flow(steps)
        if not state_flow.has_state_flow:
            continue
        guides.append(
            ProcedureGuide(
                procedure_id=slugify(f"{source_page_id}-procedure-{goal_title(node.heading_text)}"),
                title=goal_title(node.heading_text),
                goal=goal_sentence(node.heading_text),
                source_node=node,
                source_section_page_id=section_page_id(source_page_id, structure, node),
                steps=steps,
                decision_points=plan_decision_points(entries, atoms),
                technical_atoms=_relevant_atoms(atoms),
                state_flow=state_flow,
            )
        )
    guides.sort(key=lambda guide: (-len(guide.steps), guide.source_node.source_order))
    return tuple(guides[:_MAX_PROCEDURE_PAGES])


def procedure_aliases(guide: ProcedureGuide) -> tuple[str, ...]:
    return tuple(
        dict.fromkeys((slugify(guide.goal), slugify(clean_title(guide.source_node.heading_text))))
    )


def _steps_for_children(
    structure: DocumentStructure,
    entries_by_node: dict[str, tuple[LedgerEntry, ...]],
    atoms_by_node: dict[str, tuple[TechnicalAtom, ...]],
    children: tuple[StructureNode, ...],
    source_page_id: str,
) -> tuple[ProcedureStep, ...]:
    steps: list[ProcedureStep] = []
    index = 0
    while index < len(children):
        child = children[index]
        entries = _rollup_entries(structure, entries_by_node, child)
        atoms = _rollup_atoms(structure, atoms_by_node, child)
        if not is_step_heading(child.heading_text):
            index += 1
            continue
        title_heading = _best_step_heading(structure, child)
        evidence_node = child
        continuation = _next_heading_continuation(
            structure, entries_by_node, atoms_by_node, children, index
        )
        if not entries and continuation is not None:
            entries = _rollup_entries(structure, entries_by_node, continuation)
            atoms = (*atoms, *_rollup_atoms(structure, atoms_by_node, continuation))
            title_heading = f"{child.heading_text} {continuation.heading_text}"
            evidence_node = continuation
            index += 1
        if not _has_step_evidence(entries, atoms):
            index += 1
            continue
        heading_action = action_type(child.heading_text)
        action = heading_action or action_type(_entry_excerpt(entries)) or "step"
        steps.append(
            ProcedureStep(
                sequence=len(steps) + 1,
                title=step_title(title_heading),
                action_type=action,
                heading_action_type=heading_action,
                section_page_id=section_page_id(source_page_id, structure, evidence_node),
                claims=_unique_entries(entries),
                technical_atoms=_unique_atoms(atoms),
            )
        )
        index += 1
    return tuple(steps)


def _state_flow(steps: tuple[ProcedureStep, ...]) -> ProcedureStateFlow:
    return build_procedure_state_flow(
        tuple(
            ProcedureStepEvidence(
                sequence=step.sequence,
                title=step.title,
                action_type=step.action_type,
                heading_action_type=step.heading_action_type,
                claim_texts=tuple(_entry_text(entry) for entry in step.claims),
                claim_role_tags=tuple(
                    tag for entry in step.claims for tag in entry.claim_role_tags
                ),
                technical_atom_kinds=tuple(
                    atom.technical_atom_kind for atom in step.technical_atoms
                ),
                technical_atom_texts=tuple(
                    atom_raw_text(atom.payload) for atom in step.technical_atoms
                ),
            )
            for step in steps
        )
    )


def _candidate_score(
    node: StructureNode,
    entries: tuple[LedgerEntry, ...],
    atoms: tuple[TechnicalAtom, ...],
    steps: tuple[ProcedureStep, ...],
) -> int:
    text = f"{node.heading_text} {' '.join(_entry_text(entry) for entry in entries[:12])}"
    action_types = {step.action_type for step in steps if step.action_type != "step"}
    has_task = has_task_noun(node.heading_text)
    has_role = _has_procedure_role(entries)
    has_atoms = _has_procedure_atoms(atoms)
    has_decisions = has_condition(text)
    score = len(steps)
    if len(steps) >= 2:
        score += 2
    if has_task:
        score += 1
    if len(action_types) >= 3 and (has_task or has_role or has_atoms or has_decisions):
        score += 1
    if has_role:
        score += 2
    if has_atoms:
        score += 2
    if has_decisions:
        score += 1
    return score


def _section_nodes(structure: DocumentStructure) -> tuple[StructureNode, ...]:
    return tuple(
        node
        for node in sorted(
            (item for item in structure.structure_nodes if isinstance(item, StructureNode)),
            key=lambda item: item.source_order,
        )
        if node.structure_node_kind in _SECTION_NODE_KINDS and node.structure_node_kind != "root"
    )


def _entries_by_node(ledger: ClaimLedger) -> dict[str, tuple[LedgerEntry, ...]]:
    grouped: dict[str, list[LedgerEntry]] = {}
    for entry in ledger.usable_entries:
        if entry.ledger_entry_kind == "technical-atom":
            continue
        if entry.structure_node_ids:
            grouped.setdefault(entry.structure_node_ids[0], []).append(entry)
    return {node_id: tuple(entries) for node_id, entries in grouped.items()}


def _atoms_by_node(
    ledger: ClaimLedger, structure: DocumentStructure
) -> dict[str, tuple[TechnicalAtom, ...]]:
    grouped: dict[str, list[TechnicalAtom]] = {}
    section_nodes_by_source = _section_nodes_by_source(structure)
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
        node = _nearest_preceding_section_node(section_nodes_by_source, atom)
        if node is not None:
            grouped.setdefault(node.structure_node_id, []).append(atom)
    return {node_id: tuple(atoms) for node_id, atoms in grouped.items()}


def _section_nodes_by_source(
    structure: DocumentStructure,
) -> dict[str, tuple[StructureNode, ...]]:
    grouped: dict[str, list[StructureNode]] = {}
    for node in _section_nodes(structure):
        grouped.setdefault(node.source_locator, []).append(node)
    return {
        source_locator: tuple(sorted(nodes, key=lambda node: node.source_order))
        for source_locator, nodes in grouped.items()
    }


def _nearest_preceding_section_node(
    section_nodes_by_source: dict[str, tuple[StructureNode, ...]], atom: TechnicalAtom
) -> StructureNode | None:
    atom_order = _source_order_from_range_id(atom.source_range_id)
    if atom_order is None:
        return None
    for node in reversed(section_nodes_by_source.get(atom.source_locator, ())):
        if node.source_order <= atom_order:
            return node
    return None


def _source_order_from_range_id(source_range_id: str) -> int | None:
    match = re.search(r"-(\d+)$", source_range_id)
    if match is None:
        return None
    return int(match.group(1))


def _rollup_entries(
    structure: DocumentStructure,
    entries_by_node: dict[str, tuple[LedgerEntry, ...]],
    node: StructureNode,
) -> tuple[LedgerEntry, ...]:
    node_ids = (
        node.structure_node_id,
        *(child.structure_node_id for child in structure.descendants(node.structure_node_id)),
    )
    return tuple(entry for node_id in node_ids for entry in entries_by_node.get(node_id, ()))


def _rollup_atoms(
    structure: DocumentStructure,
    atoms_by_node: dict[str, tuple[TechnicalAtom, ...]],
    node: StructureNode,
) -> tuple[TechnicalAtom, ...]:
    node_ids = (
        node.structure_node_id,
        *(child.structure_node_id for child in structure.descendants(node.structure_node_id)),
    )
    return tuple(atom for node_id in node_ids for atom in atoms_by_node.get(node_id, ()))


def _has_step_evidence(entries: tuple[LedgerEntry, ...], atoms: tuple[TechnicalAtom, ...]) -> bool:
    return bool(entries or _has_procedure_atoms(atoms))


def _has_procedure_role(entries: tuple[LedgerEntry, ...]) -> bool:
    return any(
        "procedure" in entry.claim_role_tags or "method" in entry.claim_role_tags
        for entry in entries
    )


def _has_procedure_atoms(atoms: tuple[TechnicalAtom, ...]) -> bool:
    return any(atom.technical_atom_kind in {"table", "formula", "procedure"} for atom in atoms)


def _has_local_procedure_anchor(
    entries: tuple[LedgerEntry, ...], atoms: tuple[TechnicalAtom, ...]
) -> bool:
    return _has_procedure_role(entries) or any(
        atom.technical_atom_kind == "procedure" for atom in atoms
    )


def _is_unanchored_structural_container(
    node: StructureNode,
    direct_entries: tuple[LedgerEntry, ...],
    direct_atoms: tuple[TechnicalAtom, ...],
) -> bool:
    title = clean_title(node.heading_text)
    match = _STRUCTURAL_CONTAINER_PREFIX.match(title)
    if match is None:
        return False
    remainder = match.group(2).strip()
    if remainder and (has_task_noun(remainder) or action_type(remainder)):
        return False
    return not _has_local_procedure_anchor(direct_entries, direct_atoms)


def _relevant_atoms(atoms: tuple[TechnicalAtom, ...]) -> tuple[TechnicalAtom, ...]:
    return _unique_atoms(
        tuple(
            atom
            for atom in atoms
            if atom.technical_atom_kind
            in {"table", "formula", "procedure", "rule", "worked-example"}
        )
    )


def _unique_entries(entries: tuple[LedgerEntry, ...]) -> tuple[LedgerEntry, ...]:
    seen: set[tuple[str, str]] = set()
    unique: list[LedgerEntry] = []
    for entry in entries:
        key = (entry.source_range_id, _entry_text(entry))
        if key in seen:
            continue
        seen.add(key)
        unique.append(entry)
    return tuple(unique)


def _unique_atoms(atoms: tuple[TechnicalAtom, ...]) -> tuple[TechnicalAtom, ...]:
    seen: set[tuple[str, str, str]] = set()
    unique: list[TechnicalAtom] = []
    for atom in atoms:
        key = (atom.technical_atom_id, atom.source_range_id, atom_label(atom))
        if key in seen:
            continue
        seen.add(key)
        unique.append(atom)
    return tuple(unique)


def _best_step_heading(structure: DocumentStructure, node: StructureNode) -> str:
    children = structure.children(node.structure_node_id)
    if len(children) != 1:
        return node.heading_text
    node_title = clean_title(node.heading_text).lower()
    child_title = clean_title(children[0].heading_text).lower()
    if node_title and child_title.startswith(node_title):
        return children[0].heading_text
    if _is_heading_fragment(children[0]):
        return f"{node.heading_text} {children[0].heading_text}"
    return node.heading_text


def _next_heading_continuation(
    structure: DocumentStructure,
    entries_by_node: dict[str, tuple[LedgerEntry, ...]],
    atoms_by_node: dict[str, tuple[TechnicalAtom, ...]],
    children: tuple[StructureNode, ...],
    index: int,
) -> StructureNode | None:
    if index + 1 >= len(children):
        return None
    candidate = children[index + 1]
    if not _is_heading_fragment(candidate):
        return None
    entries = _rollup_entries(structure, entries_by_node, candidate)
    atoms = _rollup_atoms(structure, atoms_by_node, candidate)
    return candidate if _has_step_evidence(entries, atoms) else None


def _is_heading_fragment(node: StructureNode) -> bool:
    title = clean_title(node.heading_text)
    return bool(title and not is_step_heading(node.heading_text) and len(title.split()) <= 4)


def _entry_excerpt(entries: tuple[LedgerEntry, ...]) -> str:
    return " ".join(_entry_text(e) for e in entries[:3])


def _entry_text(entry: LedgerEntry) -> str:
    normalized = entry.normalized_text.strip()
    source = entry.source_text.strip()
    if source and len(normalized.split()) < 3:
        return source
    return normalized or source


def atom_label(atom: TechnicalAtom) -> str:
    text = atom_raw_text(atom.payload)
    first = next((line.strip() for line in text.splitlines() if line.strip()), "")
    return first[:120] if first else atom.technical_atom_id
