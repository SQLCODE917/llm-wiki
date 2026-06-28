"""Source-structure reference pages.

Topic pages are selective. These pages follow the source's own headings and are
therefore better for authoritative lookup inside a chapter or section.
"""

from __future__ import annotations

from dataclasses import dataclass

from llmwiki.domain.ledger.atom_context import best_atom_context
from llmwiki.domain.ledger.atoms import TechnicalAtom, atom_raw_text
from llmwiki.domain.ledger.canonical import short_digest
from llmwiki.domain.ledger.entries import LedgerEntry
from llmwiki.domain.ledger.ledger import ClaimLedger
from llmwiki.domain.ledger.renderer import atom_block, atom_context_block
from llmwiki.domain.ledger.section_navigation import (
    SectionPageRef,
    nodes_by_topic_key,
    related_section_links,
    section_page_id,
    section_title,
)
from llmwiki.domain.ledger.structure import DocumentStructure, StructureNode
from llmwiki.domain.ledger.table_identity import (
    has_matching_table_name,
    normalize_table_name,
    table_identity_names_by_atom_id,
)
from llmwiki.domain.ledger.topic_models import SourceTopic
from llmwiki.domain.ledger.topic_relations import RelatedTopicLink
from llmwiki.domain.pages import PageMetadata, WikiPage, slugify

_SECTION_NODE_KINDS = {"chapter", "section", "heading"}


@dataclass(frozen=True)
class _SectionProjection:
    node: StructureNode
    page_id: str
    title: str
    direct_entries: tuple[LedgerEntry, ...]
    rollup_entries: tuple[LedgerEntry, ...]
    atoms: tuple[TechnicalAtom, ...]

    @property
    def page_ref(self) -> SectionPageRef:
        return SectionPageRef(self.node, self.page_id, self.title)


def build_section_pages(
    ledger: ClaimLedger,
    structure: DocumentStructure,
    *,
    source_page_id: str,
    source_locator: str,
    today: str,
    topics: tuple[SourceTopic, ...] = (),
) -> tuple[WikiPage, ...]:
    projections = _section_projections(ledger, structure, source_page_id)
    by_node = {projection.node.structure_node_id: projection.page_ref for projection in projections}
    same_topic = nodes_by_topic_key(tuple(projection.node for projection in projections))
    topic_page_ids = {
        topic.topic_key: slugify(f"{source_page_id}-{topic.topic_key}") for topic in topics
    }
    pages: list[WikiPage] = []
    for projection in projections:
        related = related_section_links(
            projection.page_ref, structure, by_node, same_topic, topic_page_ids
        )
        body = _body(ledger, structure, projection, source_page_id, related)
        metadata = PageMetadata(
            page_id=projection.page_id,
            page_kind="source",
            summary=(
                f"{projection.title}: {len(projection.rollup_entries)} source-backed entries and "
                f"{len(projection.atoms)} atom(s) from raw/{source_locator}."
            ),
            sources=(f"raw/{source_locator}",),
            updated=today,
            domain=source_page_id,
            category_path=f"sources/{source_page_id}/sections",
            source_id=source_locator,
            projection_coverage_pointer=f"section-{projection.page_id}@{short_digest(body, 32)}",
        )
        pages.append(WikiPage.from_metadata(metadata, body))
    return tuple(pages)


def _body(
    ledger: ClaimLedger,
    structure: DocumentStructure,
    projection: _SectionProjection,
    source_page_id: str,
    related_links: tuple[RelatedTopicLink, ...],
) -> str:
    lines = [f"# {projection.title}", "", f"From [[{source_page_id}]].", ""]
    if related_links:
        lines.extend(("## Related pages", ""))
        for link in related_links:
            lines.append(f"- [[{link.page_id}]] - {link.relation}{_evidence_note(link)}")
        lines.append("")
    direct_claims = _claim_entries(projection.direct_entries)
    if direct_claims:
        lines.extend(("## Statements", ""))
        _append_claims(lines, direct_claims)
        lines.append("")
    grouped = _group_descendant_claims(structure, projection.node, projection.rollup_entries)
    if grouped:
        lines.extend(("## Statements by subsection", ""))
        for node, claims in grouped:
            lines.extend((f"### {section_title(structure, node)}", ""))
            _append_claims(lines, claims)
            lines.append("")
    if projection.atoms:
        lines.extend(("## Technical atoms", ""))
        for index, atom in enumerate(projection.atoms, start=1):
            lines.extend((f"### Technical atom {index}", ""))
            context = best_atom_context(ledger.atom_contexts(atom.technical_atom_id))
            if context is not None:
                lines.extend(atom_context_block(context, atom.source_locator).strip().splitlines())
                lines.append("")
            rendered = atom_block(atom.technical_atom_kind, atom.payload)
            citation = f"{atom.source_locator} ({atom.source_range_id})"
            lines.extend((f"**Atom:** _({citation})_", "", rendered, ""))
    return "\n".join(lines).strip() + "\n"


def _section_projections(
    ledger: ClaimLedger, structure: DocumentStructure, source_page_id: str
) -> tuple[_SectionProjection, ...]:
    projections: list[_SectionProjection] = []
    for node in _section_nodes(structure):
        rollup_entries = _entries_for_node(ledger, node.structure_node_id)
        atoms = _atoms_for_entries(ledger, rollup_entries, structure, node)
        if not rollup_entries and not atoms:
            continue
        projections.append(
            _SectionProjection(
                node=node,
                page_id=section_page_id(source_page_id, structure, node),
                title=section_title(structure, node),
                direct_entries=_direct_entries_for_node(ledger, node.structure_node_id),
                rollup_entries=rollup_entries,
                atoms=atoms,
            )
        )
    return tuple(projections)


def _section_nodes(structure: DocumentStructure) -> tuple[StructureNode, ...]:
    return tuple(
        node
        for node in sorted(structure.structure_nodes, key=lambda item: item.source_order)
        if node.structure_node_kind in _SECTION_NODE_KINDS
    )


def _claim_entries(entries: tuple[LedgerEntry, ...]) -> tuple[LedgerEntry, ...]:
    return tuple(entry for entry in entries if entry.ledger_entry_kind != "technical-atom")


def _append_claims(lines: list[str], claims: tuple[LedgerEntry, ...]) -> None:
    for entry in claims:
        text = entry.normalized_text or entry.source_text
        citation = f"{entry.source_locator} ({entry.source_range_id})"
        lines.append(f"- {text.strip()} _({citation})_")


def _group_descendant_claims(
    structure: DocumentStructure, node: StructureNode, entries: tuple[LedgerEntry, ...]
) -> tuple[tuple[StructureNode, tuple[LedgerEntry, ...]], ...]:
    grouped: dict[str, list[LedgerEntry]] = {}
    for entry in _claim_entries(entries):
        nearest = entry.structure_node_ids[0] if entry.structure_node_ids else ""
        if not nearest or nearest == node.structure_node_id:
            continue
        grouped.setdefault(nearest, []).append(entry)
    result: list[tuple[StructureNode, tuple[LedgerEntry, ...]]] = []
    for descendant in structure.descendants(node.structure_node_id):
        claims = tuple(grouped.get(descendant.structure_node_id, ()))
        if claims:
            result.append((descendant, claims))
    return tuple(result)


def _direct_entries_for_node(ledger: ClaimLedger, node_id: str) -> tuple[LedgerEntry, ...]:
    return tuple(
        entry
        for entry in ledger.usable_entries
        if entry.structure_node_ids[:1] == (node_id,)
        and (entry.normalized_text or entry.source_text or entry.technical_atom_id)
    )


def _entries_for_node(ledger: ClaimLedger, node_id: str) -> tuple[LedgerEntry, ...]:
    return tuple(
        entry
        for entry in ledger.usable_entries
        if node_id in entry.structure_node_ids
        and (entry.normalized_text or entry.source_text or entry.technical_atom_id)
    )


def _evidence_note(link: RelatedTopicLink) -> str:
    parts: list[str] = []
    if link.shared_entry_count:
        parts.append(f"{link.shared_entry_count} shared statement(s)")
    if link.shared_atom_count:
        parts.append(f"{link.shared_atom_count} shared atom(s)")
    return f" ({', '.join(parts)})" if parts else ""


def _atoms_for_entries(
    ledger: ClaimLedger,
    entries: tuple[LedgerEntry, ...],
    structure: DocumentStructure,
    node: StructureNode,
) -> tuple[TechnicalAtom, ...]:
    atom_ids = {
        entry.technical_atom_id
        for entry in entries
        if entry.ledger_entry_kind == "technical-atom" and entry.technical_atom_id
    }
    section_name = normalize_table_name(node.heading_text)
    if section_name:
        for atom_id, names in table_identity_names_by_atom_id(ledger, structure).items():
            if has_matching_table_name(section_name, names):
                atom_ids.add(atom_id)
    return tuple(
        atom
        for atom in ledger.technical_atoms
        if atom.technical_atom_id in atom_ids and atom_raw_text(atom.payload).strip()
    )
