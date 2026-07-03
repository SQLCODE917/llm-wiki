"""Evidence-card helpers for page synthesis planning."""

from __future__ import annotations

from llmwiki.domain.ledger.atom_addressing import technical_atom_anchor_id
from llmwiki.domain.ledger.atoms import TechnicalAtom, atom_raw_text
from llmwiki.domain.ledger.entries import LedgerEntry
from llmwiki.domain.ledger.ledger import ClaimLedger
from llmwiki.domain.ledger.page_synthesis import (
    DraftEvidenceCard,
    DraftEvidenceRef,
    PageSynthesisRelatedLink,
    atom_ref,
    ledger_ref,
)
from llmwiki.domain.ledger.recipe_pages import RecipePattern
from llmwiki.domain.ledger.section_navigation import section_page_id, section_title
from llmwiki.domain.ledger.structure import DocumentStructure
from llmwiki.domain.ledger.topic_relations import RelatedTopicLink


def entry_card(entry: LedgerEntry, summary: str, section_label: str = "") -> DraftEvidenceCard:
    return DraftEvidenceCard(
        evidence_ref=ledger_ref(entry.ledger_entry_id),
        source_locator=entry.source_locator,
        source_range_id=entry.source_range_id,
        summary=summary,
        exact_text=entry.source_text or entry.normalized_text,
        section_label=section_label,
        citation=citation(entry.source_locator, entry.source_range_id),
    )


def atom_card(atom: TechnicalAtom, summary: str, section_label: str = "") -> DraftEvidenceCard:
    anchor = technical_atom_anchor_id(atom.technical_atom_id)
    return DraftEvidenceCard(
        evidence_ref=atom_ref(atom.technical_atom_id),
        source_locator=atom.source_locator,
        source_range_id=atom.source_range_id,
        summary=f"{summary} at #{anchor}",
        exact_text=atom_raw_text(atom.payload),
        section_label=section_label,
        citation=citation(atom.source_locator, atom.source_range_id),
    )


def entry_summary(entry: LedgerEntry, fallback_subject: str) -> str:
    subject = short_phrase(entry.subject) or fallback_subject
    predicate = short_phrase(entry.predicate.replace("-", " "))
    obj = short_phrase(entry.object_value)
    if subject and predicate and obj:
        return f"{subject} {predicate} {obj}"
    if entry.ledger_entry_kind == "concept":
        return f"{fallback_subject} is treated as a source-backed concept"
    return f"The source gives support for {fallback_subject}"


def recipe_claim_summary(pattern: RecipePattern, claim: LedgerEntry) -> str:
    summary = entry_summary(claim, pattern.title)
    if summary.startswith("The source gives support"):
        return f"{pattern.title} has applicability evidence"
    return summary


def atom_summary(atom: TechnicalAtom, topic_label: str) -> str:
    return f"{topic_label} uses a {atom.technical_atom_kind.replace('-', ' ')} technical record"


def step_support(
    claims: tuple[LedgerEntry, ...], atoms: tuple[TechnicalAtom, ...]
) -> tuple[DraftEvidenceRef | None, str, str, str]:
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
    evidence: tuple[DraftEvidenceCard, ...],
) -> tuple[PageSynthesisRelatedLink, ...]:
    selected = {card.evidence_ref.code for card in evidence}
    links: list[PageSynthesisRelatedLink] = []
    for related in related_pages:
        refs = tuple(
            ref
            for ref in (
                *map(ledger_ref, related.shared_entry_ids),
                *map(atom_ref, related.shared_atom_ids),
            )
            if ref.code in selected
        )
        links.append(
            PageSynthesisRelatedLink(related.page_id, related.label, related.relation, refs)
        )
    return tuple(links)


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


def short_phrase(text: str, *, max_words: int = 6) -> str:
    words = tuple(word.strip(" ,;:.") for word in text.split() if word.strip(" ,;:."))
    return " ".join(words[:max_words])


def citation(source_locator: str, source_range_id: str) -> str:
    if source_range_id:
        return f"raw/{source_locator} ({source_range_id})"
    return f"raw/{source_locator}"
