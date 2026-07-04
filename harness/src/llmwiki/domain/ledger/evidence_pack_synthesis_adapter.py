"""Temporary adapter from EvidencePack to current PageSynthesisPlan support."""

from __future__ import annotations

from dataclasses import replace

from llmwiki.domain.ledger.evidence_pack import EvidencePack, EvidencePackItem, SupportRef
from llmwiki.domain.ledger.page_synthesis import (
    EvidenceSupportRef,
    PageEvidenceItem,
    PageEvidenceSet,
    PageOutlineSection,
    PageSynthesisPlan,
)


def apply_evidence_pack_to_synthesis_plan(
    plan: PageSynthesisPlan, pack: EvidencePack
) -> PageSynthesisPlan:
    support_refs = tuple(_support_ref(item.support_ref) for item in pack.items)
    return replace(
        plan,
        evidence_set=PageEvidenceSet(
            page_id=plan.page_id,
            items=tuple(_evidence_item(item) for item in pack.items),
        ),
        outline=tuple(_outline_section(section, support_refs) for section in plan.outline),
    )


def _evidence_item(pack_item: EvidencePackItem) -> PageEvidenceItem:
    return PageEvidenceItem(
        support_ref=_support_ref(pack_item.support_ref),
        evidence_kind=pack_item.evidence_record_type,
        source_locator=_source_locator(pack_item.citation_label),
        source_range_ids=pack_item.source_block_ids,
        evidence_text=pack_item.source_text or pack_item.payload_text,
        section_label=pack_item.section_path,
        citation=pack_item.citation_label,
        evidence_block_id=pack_item.typed_evidence_record_id,
    )


def _outline_section(
    section: PageOutlineSection, support_refs: tuple[EvidenceSupportRef, ...]
) -> PageOutlineSection:
    return replace(section, support_refs=support_refs)


def _support_ref(ref: SupportRef) -> EvidenceSupportRef:
    return EvidenceSupportRef(ref.support_kind, ref.support_id)


def _source_locator(citation_label: str) -> str:
    raw = citation_label.removeprefix("raw/")
    return raw.split(" (", 1)[0].strip()
