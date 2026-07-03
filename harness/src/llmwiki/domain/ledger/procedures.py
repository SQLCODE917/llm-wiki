"""Procedure ontology and source-grounded procedure page projection."""

from __future__ import annotations

from dataclasses import dataclass

from llmwiki.domain.ledger.atoms import TechnicalAtom, atom_raw_text
from llmwiki.domain.ledger.entries import LedgerEntry
from llmwiki.domain.ledger.knowledge_shapes import (
    KnowledgeShapeCatalog,
    build_knowledge_shape_catalog,
)
from llmwiki.domain.ledger.ledger import ClaimLedger
from llmwiki.domain.ledger.procedure_candidates import (
    has_step_evidence,
)
from llmwiki.domain.ledger.procedure_decisions import DecisionPoint, plan_decision_points
from llmwiki.domain.ledger.procedure_evidence_index import (
    atoms_by_node,
    entries_by_node,
    rollup_atoms,
    rollup_entries,
)
from llmwiki.domain.ledger.procedure_language import (
    action_type,
    clean_title,
    goal_sentence,
    goal_title,
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

_MAX_PROCEDURE_PAGES = 64


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
    ledger: ClaimLedger,
    structure: DocumentStructure,
    *,
    source_page_id: str,
    shape_catalog: KnowledgeShapeCatalog | None = None,
) -> tuple[ProcedureGuide, ...]:
    catalog = shape_catalog or build_knowledge_shape_catalog(ledger, structure)
    grouped_entries = entries_by_node(ledger)
    grouped_atoms = atoms_by_node(ledger, structure)
    guides: list[ProcedureGuide] = []
    for candidate in catalog.candidates_of_kind("procedure"):
        node = structure.node(candidate.structure_node_id)
        if node is None:
            continue
        entries = rollup_entries(structure, grouped_entries, node)
        atoms = rollup_atoms(structure, grouped_atoms, node)
        children = tuple(child for child in structure.children(node.structure_node_id))
        steps = _steps_for_children(
            structure,
            grouped_entries,
            grouped_atoms,
            children,
            source_page_id,
        )
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
                decision_points=plan_decision_points(entries, atoms, ledger.source_statements),
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
    grouped_entries: dict[str, tuple[LedgerEntry, ...]],
    grouped_atoms: dict[str, tuple[TechnicalAtom, ...]],
    children: tuple[StructureNode, ...],
    source_page_id: str,
) -> tuple[ProcedureStep, ...]:
    steps: list[ProcedureStep] = []
    index = 0
    while index < len(children):
        child = children[index]
        entries = rollup_entries(structure, grouped_entries, child)
        atoms = rollup_atoms(structure, grouped_atoms, child)
        if not is_step_heading(child.heading_text):
            index += 1
            continue
        title_heading = _best_step_heading(structure, child)
        evidence_node = child
        continuation = _next_heading_continuation(
            structure,
            grouped_entries,
            grouped_atoms,
            children,
            index,
        )
        if not entries and continuation is not None:
            entries = rollup_entries(structure, grouped_entries, continuation)
            atoms = (*atoms, *rollup_atoms(structure, grouped_atoms, continuation))
            title_heading = f"{child.heading_text} {continuation.heading_text}"
            evidence_node = continuation
            index += 1
        if not has_step_evidence(entries, atoms):
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
    grouped_entries: dict[str, tuple[LedgerEntry, ...]],
    grouped_atoms: dict[str, tuple[TechnicalAtom, ...]],
    children: tuple[StructureNode, ...],
    index: int,
) -> StructureNode | None:
    if index + 1 >= len(children):
        return None
    candidate = children[index + 1]
    if not _is_heading_fragment(candidate):
        return None
    entries = rollup_entries(structure, grouped_entries, candidate)
    atoms = rollup_atoms(structure, grouped_atoms, candidate)
    return candidate if has_step_evidence(entries, atoms) else None


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
