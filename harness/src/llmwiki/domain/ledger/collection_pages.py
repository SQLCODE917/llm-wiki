"""Collection-page projection for repeated source peer structures."""

from __future__ import annotations

from dataclasses import dataclass

from llmwiki.domain.ledger.atoms import TechnicalAtom
from llmwiki.domain.ledger.canonical import short_digest
from llmwiki.domain.ledger.entries import LedgerEntry
from llmwiki.domain.ledger.knowledge_shapes import KnowledgeShapeCatalog
from llmwiki.domain.ledger.ledger import ClaimLedger
from llmwiki.domain.ledger.procedure_evidence_index import (
    atoms_by_node,
    entries_by_node,
    rollup_atoms,
    rollup_entries,
)
from llmwiki.domain.ledger.projection_policy import PAGE_FAMILY_COLLECTION_PAGE
from llmwiki.domain.ledger.section_navigation import section_page_id, section_title
from llmwiki.domain.ledger.structure import DocumentStructure, StructureNode
from llmwiki.domain.pages import PageMetadata, WikiPage, slugify

_MEMBER_SHAPES = {"catalog-entry", "reference-field"}
_MIN_MEMBERS = 3
_MAX_VISIBLE_MEMBERS = 80


@dataclass(frozen=True)
class CollectionMember:
    structure_node_id: str
    title: str
    section_page_id: str
    entry_count: int
    atom_count: int


@dataclass(frozen=True)
class CollectionPlan:
    collection_page_id: str
    title: str
    source_section_page_id: str
    source_node_id: str
    members: tuple[CollectionMember, ...]
    peer_signal_kinds: tuple[str, ...]


def build_collection_pages(
    ledger: ClaimLedger,
    structure: DocumentStructure,
    *,
    source_page_id: str,
    source_locator: str,
    today: str,
    shape_catalog: KnowledgeShapeCatalog,
) -> tuple[WikiPage, ...]:
    return tuple(
        _page(plan, source_page_id, source_locator, today)
        for plan in collection_plans(ledger, structure, source_page_id, shape_catalog)
    )


def collection_plans(
    ledger: ClaimLedger,
    structure: DocumentStructure,
    source_page_id: str,
    shape_catalog: KnowledgeShapeCatalog,
) -> tuple[CollectionPlan, ...]:
    shape_by_node = {item.structure_node_id: item.shape_kind for item in shape_catalog.candidates}
    grouped_entries = entries_by_node(ledger)
    grouped_atoms = atoms_by_node(ledger, structure)
    plans: list[CollectionPlan] = []
    for candidate in shape_catalog.candidates_of_kind("section-container"):
        node = structure.node(candidate.structure_node_id)
        if node is None:
            continue
        members = _members(
            structure,
            grouped_entries,
            grouped_atoms,
            source_page_id,
            node,
            shape_by_node,
        )
        if len(members) < _MIN_MEMBERS:
            continue
        signals = _peer_signals(members, candidate.child_structure_node_ids, shape_by_node)
        if len(signals) < 2:
            continue
        title = section_title(structure, node)
        plans.append(
            CollectionPlan(
                collection_page_id=slugify(
                    f"{source_page_id}-collection-{title}-{short_digest(node.structure_node_id, 8)}"
                ),
                title=title,
                source_section_page_id=section_page_id(source_page_id, structure, node),
                source_node_id=node.structure_node_id,
                members=members,
                peer_signal_kinds=signals,
            )
        )
    plans.sort(key=lambda plan: (structure.node(plan.source_node_id).source_order, plan.title))  # type: ignore[union-attr]
    return tuple(plans)


def _page(
    plan: CollectionPlan, source_page_id: str, source_locator: str, today: str
) -> WikiPage:
    body = _body(plan, source_page_id)
    metadata = PageMetadata(
        page_id=plan.collection_page_id,
        page_kind="source",
        page_family=PAGE_FAMILY_COLLECTION_PAGE,
        summary=(
            f"{plan.title}: {len(plan.members)} collection member(s) from raw/{source_locator}."
        ),
        sources=(f"raw/{source_locator}",),
        updated=today,
        domain=source_page_id,
        category_path=f"sources/{source_page_id}/collections",
        source_id=source_locator,
        projection_coverage_pointer=(
            f"collection-{plan.collection_page_id}@{short_digest(body, 32)}"
        ),
    )
    return WikiPage.from_metadata(metadata, body)


def _body(plan: CollectionPlan, source_page_id: str) -> str:
    lines = [
        f"# {plan.title}",
        "",
        f"From [[{source_page_id}]].",
        f"Broader source section: [[{plan.source_section_page_id}]].",
        "",
        "## Collection Signals",
        "",
    ]
    for signal in plan.peer_signal_kinds:
        lines.append(f"- {signal.replace('-', ' ')}")
    lines.extend(
        ("", "## Members", "", "| Member | Source section | Evidence |", "| --- | --- | --- |")
    )
    for member in plan.members[:_MAX_VISIBLE_MEMBERS]:
        evidence = f"{member.entry_count} statement(s), {member.atom_count} atom(s)"
        lines.append(f"| {member.title} | [[{member.section_page_id}]] | {evidence} |")
    if len(plan.members) > _MAX_VISIBLE_MEMBERS:
        lines.append(
            f"\n_{len(plan.members) - _MAX_VISIBLE_MEMBERS} additional member(s) omitted._"
        )
    return "\n".join(lines).strip() + "\n"


def _members(
    structure: DocumentStructure,
    grouped_entries: dict[str, tuple[LedgerEntry, ...]],
    grouped_atoms: dict[str, tuple[TechnicalAtom, ...]],
    source_page_id: str,
    node: StructureNode,
    shape_by_node: dict[str, str],
) -> tuple[CollectionMember, ...]:
    members: list[CollectionMember] = []
    for child in structure.children(node.structure_node_id):
        entries = rollup_entries(structure, grouped_entries, child)
        atoms = rollup_atoms(structure, grouped_atoms, child)
        if shape_by_node.get(child.structure_node_id) not in _MEMBER_SHAPES and not atoms:
            continue
        if not entries and not atoms:
            continue
        members.append(
            CollectionMember(
                structure_node_id=child.structure_node_id,
                title=section_title(structure, child),
                section_page_id=section_page_id(source_page_id, structure, child),
                entry_count=len(entries),
                atom_count=len(atoms),
            )
        )
    return tuple(members)


def _peer_signals(
    members: tuple[CollectionMember, ...],
    child_node_ids: tuple[str, ...],
    shape_by_node: dict[str, str],
) -> tuple[str, ...]:
    signals = ["sibling-structure"] if len(child_node_ids) >= _MIN_MEMBERS else []
    member_shapes = {
        shape_by_node.get(member.structure_node_id, "")
        for member in members
        if shape_by_node.get(member.structure_node_id, "") in _MEMBER_SHAPES
    }
    if member_shapes:
        signals.append("repeated-peer-shape")
    if any(member.atom_count for member in members):
        signals.append("structured-technical-atoms")
    return tuple(signals)
