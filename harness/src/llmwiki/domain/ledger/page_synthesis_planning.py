"""Build page synthesis plans from existing projection plans."""

from __future__ import annotations

from llmwiki.domain.ledger.collection_pages import CollectionPlan
from llmwiki.domain.ledger.ledger import ClaimLedger
from llmwiki.domain.ledger.page_synthesis import (
    DraftEvidenceCard,
    PageOutlineSection,
    PageSynthesisPlan,
)
from llmwiki.domain.ledger.page_synthesis_evidence import (
    atom_card,
    atom_section_label,
    atom_summary,
    citation,
    entry_card,
    entry_section_label,
    entry_summary,
    recipe_claim_summary,
    related_links,
    section_page_ids_for_entries,
    step_support,
)
from llmwiki.domain.ledger.procedures import ProcedureGuide
from llmwiki.domain.ledger.recipe_pages import RecipePattern
from llmwiki.domain.ledger.structure import DocumentStructure
from llmwiki.domain.ledger.topic_models import SourceTopic
from llmwiki.domain.ledger.topic_relations import RelatedTopicLink

_MAX_TOPIC_EVIDENCE = 8
_MAX_PROCEDURE_STEPS = 16
_MAX_RECIPE_EVIDENCE = 8
_MAX_COLLECTION_MEMBERS = 24


def topic_synthesis_plan(
    topic: SourceTopic,
    ledger: ClaimLedger,
    structure: DocumentStructure,
    *,
    page_id: str,
    page_family: str,
    source_page_id: str,
    source_locator: str,
    related_pages: tuple[RelatedTopicLink, ...] = (),
) -> PageSynthesisPlan:
    entry_cards = tuple(
        entry_card(entry, entry_summary(entry, topic.label), entry_section_label(structure, entry))
        for entry_id in topic.entry_ids[:_MAX_TOPIC_EVIDENCE]
        if (entry := ledger.entry(entry_id)) is not None
    )
    atom_cards = tuple(
        atom_card(
            atom,
            atom_summary(atom, topic.label),
            atom_section_label(structure, ledger, atom),
        )
        for atom_id in topic.atom_ids[:4]
        if (atom := ledger.atom(atom_id)) is not None
    )
    evidence = (*entry_cards, *atom_cards)
    section_ids = section_page_ids_for_entries(
        structure,
        source_page_id,
        tuple(
            entry
            for entry_id in topic.entry_ids
            if (entry := ledger.entry(entry_id)) is not None
        ),
    )
    return PageSynthesisPlan(
        page_id=page_id,
        page_kind=topic.page_kind,
        page_family=page_family,
        title=topic.label,
        source_page_id=source_page_id,
        source_locator=source_locator,
        source_section_page_ids=section_ids,
        outline=(
            PageOutlineSection(
                "Source-Backed View",
                "Summarize selected statements about this topic.",
                tuple(card.evidence_ref for card in entry_cards),
                "bullet-list",
            ),
            PageOutlineSection(
                "Technical Evidence",
                "Summarize selected technical atoms for this topic.",
                tuple(card.evidence_ref for card in atom_cards),
                "bullet-list",
            ),
        ),
        selected_evidence=evidence,
        related_links=related_links(related_pages, evidence),
    )


def procedure_synthesis_plan(
    guide: ProcedureGuide,
    *,
    source_page_id: str,
    source_locator: str,
) -> PageSynthesisPlan:
    step_cards: list[DraftEvidenceCard] = []
    for step in guide.steps[:_MAX_PROCEDURE_STEPS]:
        ref, locator, range_id, exact = step_support(step.claims, step.technical_atoms)
        if ref is None:
            continue
        step_cards.append(
            DraftEvidenceCard(
                evidence_ref=ref,
                source_locator=locator,
                source_range_id=range_id,
                summary=(
                    f"Step {step.sequence} uses the {step.action_type.replace('-', ' ')} "
                    f"action {step.title.lower()}"
                ),
                exact_text=exact,
                section_label=step.section_page_id,
                citation=citation(locator, range_id),
            )
        )
    atom_cards = tuple(
        atom_card(
            atom,
            f"{guide.title} uses a {atom.technical_atom_kind.replace('-', ' ')} reference",
        )
        for atom in guide.technical_atoms[:6]
    )
    evidence = (*step_cards, *atom_cards)
    return PageSynthesisPlan(
        page_id=guide.procedure_id,
        page_kind="procedure",
        page_family="procedure-guide",
        title=guide.title,
        source_page_id=source_page_id,
        source_locator=source_locator,
        source_section_page_ids=(guide.source_section_page_id,),
        outline=(
            PageOutlineSection(
                "Goal",
                "Describe the procedure goal.",
                tuple(card.evidence_ref for card in step_cards[:1]),
                "paragraph",
            ),
            PageOutlineSection(
                "Procedure Steps",
                "Render ordered source-backed steps.",
                tuple(card.evidence_ref for card in step_cards),
                "numbered-list",
            ),
            PageOutlineSection(
                "Tables And Formulas",
                "List technical references needed by the procedure.",
                tuple(card.evidence_ref for card in atom_cards),
                "bullet-list",
            ),
        ),
        selected_evidence=evidence,
    )


def recipe_synthesis_plan(
    pattern: RecipePattern,
    *,
    source_page_id: str,
    source_locator: str,
) -> PageSynthesisPlan:
    claim_cards = tuple(
        entry_card(claim, recipe_claim_summary(pattern, claim), pattern.source_node.heading_text)
        for claim in pattern.claims[:_MAX_RECIPE_EVIDENCE]
    )
    atom_cards = tuple(
        atom_card(atom, f"{pattern.title} includes a {atom.technical_atom_kind.replace('-', ' ')}")
        for atom in pattern.technical_atoms[:4]
    )
    evidence = (*claim_cards, *atom_cards)
    return PageSynthesisPlan(
        page_id=pattern.recipe_id,
        page_kind="recipe",
        page_family="recipe-pattern",
        title=pattern.title,
        source_page_id=source_page_id,
        source_locator=source_locator,
        source_section_page_ids=(pattern.source_section_page_id,),
        outline=(
            PageOutlineSection(
                "Pattern",
                "Explain the reusable source-backed pattern.",
                tuple(card.evidence_ref for card in claim_cards[:2] or atom_cards[:1]),
                "bullet-list",
            ),
            PageOutlineSection(
                "Applicability And Rationale",
                "Summarize why the pattern applies.",
                tuple(card.evidence_ref for card in claim_cards),
                "bullet-list",
            ),
            PageOutlineSection(
                "Technical Atoms",
                "Preserve technical references as source-backed summaries.",
                tuple(card.evidence_ref for card in atom_cards),
                "bullet-list",
            ),
        ),
        selected_evidence=evidence,
    )


def collection_synthesis_plan(
    plan: CollectionPlan,
    ledger: ClaimLedger,
    *,
    source_page_id: str,
    source_locator: str,
) -> PageSynthesisPlan:
    cards: list[DraftEvidenceCard] = []
    for member in plan.members[:_MAX_COLLECTION_MEMBERS]:
        entry = next(
            (
                entry
                for entry_id in member.entry_ids
                if (entry := ledger.entry(entry_id)) is not None
            ),
            None,
        )
        atom = next(
            (atom for atom_id in member.atom_ids if (atom := ledger.atom(atom_id)) is not None),
            None,
        )
        if entry is not None:
            cards.append(
                entry_card(
                    entry,
                    (
                        f"{member.title} is a collection member with {member.entry_count} "
                        f"statement(s) and {member.atom_count} technical atom(s)"
                    ),
                    member.section_page_id,
                )
            )
        elif atom is not None:
            cards.append(
                atom_card(
                    atom,
                    (
                        f"{member.title} is a collection member with {member.entry_count} "
                        f"statement(s) and {member.atom_count} technical atom(s)"
                    ),
                    member.section_page_id,
                )
            )
    return PageSynthesisPlan(
        page_id=plan.collection_page_id,
        page_kind="source",
        page_family="collection-page",
        title=plan.title,
        source_page_id=source_page_id,
        source_locator=source_locator,
        source_section_page_ids=(plan.source_section_page_id,),
        outline=(
            PageOutlineSection(
                "Collection Signals",
                "Describe the source-backed collection members.",
                tuple(card.evidence_ref for card in cards),
                "bullet-list",
            ),
        ),
        selected_evidence=tuple(cards),
    )
