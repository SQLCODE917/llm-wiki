"""Build page synthesis plans from existing projection plans."""

from __future__ import annotations

from llmwiki.domain.ledger.collection_pages import CollectionPlan
from llmwiki.domain.ledger.ledger import ClaimLedger
from llmwiki.domain.ledger.page_synthesis import (
    PageEvidenceItem,
    PageEvidenceSet,
    PageOutlineSection,
    PageSynthesisPlan,
)
from llmwiki.domain.ledger.page_synthesis_evidence import (
    atom_item,
    atom_section_label,
    citation,
    entry_item,
    entry_section_label,
    evidence_block_items_for_entries,
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
    entry_items = evidence_block_items_for_entries(ledger, structure, topic.entry_ids)[
        :_MAX_TOPIC_EVIDENCE
    ]
    if not entry_items:
        entry_items = tuple(
            entry_item(entry, entry_section_label(structure, entry))
            for entry_id in topic.entry_ids[:_MAX_TOPIC_EVIDENCE]
            if (entry := ledger.entry(entry_id)) is not None
        )
    atom_items = tuple(
        atom_item(
            atom,
            atom_section_label(structure, ledger, atom),
        )
        for atom_id in topic.atom_ids[:4]
        if (atom := ledger.atom(atom_id)) is not None
    )
    evidence = (*entry_items, *atom_items)
    evidence_set = PageEvidenceSet(page_id, evidence)
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
                "Draft readable source-backed statements about this topic.",
                tuple(item.support_ref for item in entry_items),
                "bullet-list",
            ),
            PageOutlineSection(
                "Technical Evidence",
                "List selected technical atom payloads for this topic.",
                tuple(item.support_ref for item in atom_items),
                "bullet-list",
            ),
        ),
        evidence_set=evidence_set,
        related_links=related_links(related_pages, evidence),
    )


def procedure_synthesis_plan(
    guide: ProcedureGuide,
    *,
    source_page_id: str,
    source_locator: str,
) -> PageSynthesisPlan:
    step_items: list[PageEvidenceItem] = []
    for step in guide.steps[:_MAX_PROCEDURE_STEPS]:
        ref, locator, range_id, exact = step_support(step.claims, step.technical_atoms)
        if ref is None:
            continue
        step_items.append(
            PageEvidenceItem(
                support_ref=ref,
                evidence_kind=ref.support_kind,
                source_locator=locator,
                source_range_ids=(range_id,),
                evidence_text=exact,
                section_label=step.section_page_id,
                citation=citation(locator, range_id),
                ledger_entry_ids=(ref.support_id,) if ref.support_kind == "ledger" else (),
                technical_atom_id=ref.support_id if ref.support_kind == "atom" else "",
            )
        )
    atom_items = tuple(
        atom_item(
            atom,
        )
        for atom in guide.technical_atoms[:6]
    )
    evidence = (*step_items, *atom_items)
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
                tuple(item.support_ref for item in step_items[:1]),
                "paragraph",
            ),
            PageOutlineSection(
                "Procedure Steps",
                "Render ordered source-backed steps.",
                tuple(item.support_ref for item in step_items),
                "numbered-list",
            ),
            PageOutlineSection(
                "Tables And Formulas",
                "List technical references needed by the procedure.",
                tuple(item.support_ref for item in atom_items),
                "bullet-list",
            ),
        ),
        evidence_set=PageEvidenceSet(guide.procedure_id, evidence),
    )


def recipe_synthesis_plan(
    pattern: RecipePattern,
    *,
    source_page_id: str,
    source_locator: str,
) -> PageSynthesisPlan:
    claim_items = tuple(
        entry_item(claim, pattern.source_node.heading_text)
        for claim in pattern.claims[:_MAX_RECIPE_EVIDENCE]
    )
    atom_items = tuple(
        atom_item(atom)
        for atom in pattern.technical_atoms[:4]
    )
    evidence = (*claim_items, *atom_items)
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
                tuple(item.support_ref for item in claim_items[:2] or atom_items[:1]),
                "bullet-list",
            ),
            PageOutlineSection(
                "Applicability And Rationale",
                "Summarize why the pattern applies.",
                tuple(item.support_ref for item in claim_items),
                "bullet-list",
            ),
            PageOutlineSection(
                "Technical Atoms",
                "Preserve technical references as source-backed payloads.",
                tuple(item.support_ref for item in atom_items),
                "bullet-list",
            ),
        ),
        evidence_set=PageEvidenceSet(pattern.recipe_id, evidence),
    )


def collection_synthesis_plan(
    plan: CollectionPlan,
    ledger: ClaimLedger,
    *,
    source_page_id: str,
    source_locator: str,
) -> PageSynthesisPlan:
    items: list[PageEvidenceItem] = []
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
            items.append(
                entry_item(
                    entry,
                    member.section_page_id,
                )
            )
        elif atom is not None:
            items.append(
                atom_item(
                    atom,
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
                tuple(item.support_ref for item in items),
                "bullet-list",
            ),
        ),
        evidence_set=PageEvidenceSet(plan.collection_page_id, tuple(items)),
    )
