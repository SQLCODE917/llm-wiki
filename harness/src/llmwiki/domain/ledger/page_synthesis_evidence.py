"""Evidence helpers for page synthesis planning."""

from __future__ import annotations

from llmwiki.domain.ledger.atom_addressing import technical_atom_anchor_id
from llmwiki.domain.ledger.atoms import TechnicalAtom, atom_raw_text
from llmwiki.domain.ledger.entries import LedgerEntry
from llmwiki.domain.ledger.evidence_blocks import EvidenceBlock, build_evidence_blocks
from llmwiki.domain.ledger.ledger import ClaimLedger
from llmwiki.domain.ledger.page_synthesis import (
    EvidenceSupportRef,
    PageEvidenceItem,
    RelatedLinkPreview,
    atom_ref,
    evidence_block_ref,
    ledger_ref,
)
from llmwiki.domain.ledger.section_navigation import section_page_id, section_title
from llmwiki.domain.ledger.structure import DocumentStructure
from llmwiki.domain.ledger.topic_relations import RelatedTopicLink


def entry_item(entry: LedgerEntry, section_label: str = "") -> PageEvidenceItem:
    return PageEvidenceItem(
        support_ref=ledger_ref(entry.ledger_entry_id),
        evidence_kind="ledger-entry",
        source_locator=entry.source_locator,
        source_range_ids=(entry.source_range_id,),
        evidence_text=entry.source_text or entry.normalized_text,
        section_label=section_label,
        citation=citation(entry.source_locator, entry.source_range_id),
        ledger_entry_ids=(entry.ledger_entry_id,),
    )


def evidence_block_item(block: EvidenceBlock) -> PageEvidenceItem:
    return PageEvidenceItem(
        support_ref=evidence_block_ref(block.evidence_block_id),
        evidence_kind="evidence-block",
        source_locator=block.source_locator,
        source_range_ids=block.source_range_ids,
        evidence_text=block.source_text,
        section_label=block.section_label,
        citation=citation(block.source_locator, block.source_range_id),
        ledger_entry_ids=block.entry_ids,
        evidence_block_id=block.evidence_block_id,
    )


def atom_item(atom: TechnicalAtom, section_label: str = "") -> PageEvidenceItem:
    anchor = technical_atom_anchor_id(atom.technical_atom_id)
    return PageEvidenceItem(
        support_ref=atom_ref(atom.technical_atom_id),
        evidence_kind="technical-atom",
        source_locator=atom.source_locator,
        source_range_ids=(atom.source_range_id,),
        evidence_text=atom_raw_text(atom.payload),
        section_label=section_label,
        citation=citation(atom.source_locator, atom.source_range_id),
        technical_atom_id=atom.technical_atom_id,
        evidence_block_id=anchor,
    )


def step_support(
    claims: tuple[LedgerEntry, ...], atoms: tuple[TechnicalAtom, ...]
) -> tuple[EvidenceSupportRef | None, str, str, str]:
    if claims:
        claim = claims[0]
        return (
            ledger_ref(claim.ledger_entry_id),
            claim.source_locator,
            claim.source_range_id,
            claim.source_text,
        )
    if atoms:
        atom = atoms[0]
        return (
            atom_ref(atom.technical_atom_id),
            atom.source_locator,
            atom.source_range_id,
            atom_raw_text(atom.payload),
        )
    return None, "", "", ""


def related_links(
    related_pages: tuple[RelatedTopicLink, ...],
    evidence: tuple[PageEvidenceItem, ...],
) -> tuple[RelatedLinkPreview, ...]:
    selected = {item.support_ref.code for item in evidence}
    preview_by_ref = {
        item.support_ref.code: readable_preview(item.evidence_text) for item in evidence
    }
    links: list[RelatedLinkPreview] = []
    for related in related_pages:
        refs = tuple(
            ref
            for ref in (
                *map(ledger_ref, related.shared_entry_ids),
                *map(atom_ref, related.shared_atom_ids),
            )
            if ref.code in selected
        )
        previews = tuple(preview_by_ref[ref.code] for ref in refs if preview_by_ref.get(ref.code))
        preview = previews[0] if previews else related.relation
        links.append(
            RelatedLinkPreview(related.page_id, related.label, related.relation, preview, refs)
        )
    return tuple(links)


def evidence_block_items_for_entries(
    ledger: ClaimLedger,
    structure: DocumentStructure,
    entry_ids: tuple[str, ...],
) -> tuple[PageEvidenceItem, ...]:
    selected = set(entry_ids)
    items: list[PageEvidenceItem] = []
    for block in build_evidence_blocks(ledger, structure):
        if selected.intersection(block.entry_ids):
            items.append(evidence_block_item(block))
    return tuple(items)


def section_page_ids_for_entries(
    structure: DocumentStructure, source_page_id: str, entries: tuple[LedgerEntry, ...]
) -> tuple[str, ...]:
    page_ids: list[str] = []
    for entry in entries:
        if not entry.structure_node_ids:
            continue
        node = structure.node(entry.structure_node_ids[0])
        if node is None:
            continue
        page_id = section_page_id(source_page_id, structure, node)
        if page_id not in page_ids:
            page_ids.append(page_id)
    return tuple(page_ids[:4])


def entry_section_label(structure: DocumentStructure, entry: LedgerEntry) -> str:
    if not entry.structure_node_ids:
        return ""
    node = structure.node(entry.structure_node_ids[0])
    return section_title(structure, node) if node is not None else ""


def atom_section_label(
    structure: DocumentStructure, ledger: ClaimLedger, atom: TechnicalAtom
) -> str:
    entry = next(
        (
            entry
            for entry in ledger.usable_entries
            if entry.technical_atom_id == atom.technical_atom_id
        ),
        None,
    )
    return entry_section_label(structure, entry) if entry is not None else ""


def citation(source_locator: str, source_range_id: str) -> str:
    if source_range_id:
        return f"raw/{source_locator} ({source_range_id})"
    return f"raw/{source_locator}"


def readable_preview(text: str, *, max_chars: int = 160) -> str:
    cleaned = " ".join(text.split()).strip()
    if len(cleaned) <= max_chars:
        return cleaned
    return cleaned[:max_chars].rsplit(" ", 1)[0].rstrip(" ,;:") + "..."
