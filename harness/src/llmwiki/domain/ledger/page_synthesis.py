"""Page synthesis domain contracts.

The synthesis layer sits between the claim ledger and final markdown. A
``PageSynthesisPlan`` selects the only evidence a draft may cite. A
``PageDraft`` carries prose and sentence-level ``DraftClaim`` records. The
renderer turns an accepted draft into markdown and projection coverage.
"""

from __future__ import annotations

from dataclasses import dataclass

from llmwiki.domain.ledger.coverage import ProjectionCoverage

SYNTHESIZED_PAGE_FAMILIES = frozenset(
    {
        "procedure-guide",
        "recipe-pattern",
        "topic-concept",
        "broad-topic",
        "collection-page",
    }
)


@dataclass(frozen=True)
class EvidenceSupportRef:
    support_kind: str
    support_id: str

    @property
    def code(self) -> str:
        return f"{self.support_kind}:{self.support_id}"


@dataclass(frozen=True)
class PageEvidenceItem:
    support_ref: EvidenceSupportRef
    evidence_kind: str
    source_locator: str
    source_range_ids: tuple[str, ...]
    evidence_text: str
    section_label: str = ""
    citation: str = ""
    ledger_entry_ids: tuple[str, ...] = ()
    technical_atom_id: str = ""
    evidence_block_id: str = ""

    @property
    def source_range_id(self) -> str:
        return self.source_range_ids[0] if self.source_range_ids else ""


@dataclass(frozen=True)
class NavigationSummary:
    target_page_id: str
    summary_text: str
    summary_kind: str
    page_body_hash: str = ""


@dataclass(frozen=True)
class PromptContextDigest:
    digest_text: str
    support_refs: tuple[EvidenceSupportRef, ...]
    renderable: bool = False


@dataclass(frozen=True)
class PageEvidenceSet:
    page_id: str
    items: tuple[PageEvidenceItem, ...]
    navigation_summaries: tuple[NavigationSummary, ...] = ()
    prompt_context_digests: tuple[PromptContextDigest, ...] = ()

    @property
    def selected_support_codes(self) -> frozenset[str]:
        return frozenset(item.support_ref.code for item in self.items)

    @property
    def support_text_by_code(self) -> dict[str, str]:
        return {item.support_ref.code: item.evidence_text for item in self.items}


@dataclass(frozen=True)
class PageOutlineSection:
    heading: str
    purpose: str
    support_refs: tuple[EvidenceSupportRef, ...]
    block_kind: str = "bullet-list"


@dataclass(frozen=True)
class RelatedLinkPreview:
    page_id: str
    label: str
    relation: str
    preview_text: str = ""
    support_refs: tuple[EvidenceSupportRef, ...] = ()


@dataclass(frozen=True)
class PageSynthesisPlan:
    page_id: str
    page_kind: str
    page_family: str
    title: str
    source_page_id: str
    source_locator: str
    source_section_page_ids: tuple[str, ...]
    outline: tuple[PageOutlineSection, ...]
    evidence_set: PageEvidenceSet
    related_links: tuple[RelatedLinkPreview, ...] = ()

    @property
    def selected_support_codes(self) -> frozenset[str]:
        return self.evidence_set.selected_support_codes


@dataclass(frozen=True)
class DraftClaim:
    claim_id: str
    sentence: str
    support_refs: tuple[EvidenceSupportRef, ...]


@dataclass(frozen=True)
class DraftBlock:
    block_id: str
    block_kind: str
    heading: str = ""
    text: str = ""
    items: tuple[str, ...] = ()
    table_rows: tuple[tuple[str, ...], ...] = ()


@dataclass(frozen=True)
class PageDraft:
    page_id: str
    title: str
    blocks: tuple[DraftBlock, ...]
    claims: tuple[DraftClaim, ...]


@dataclass(frozen=True)
class PageSynthesisFinding:
    severity: str
    finding_type: str
    page_id: str
    message: str
    claim_id: str = ""
    support_ref: str = ""
    block_id: str = ""


@dataclass(frozen=True)
class DraftValidationResult:
    accepted: bool
    findings: tuple[PageSynthesisFinding, ...]


@dataclass(frozen=True)
class PageDraftCoverage:
    page_id: str
    page_body_hash: str
    projection_coverage: ProjectionCoverage


@dataclass(frozen=True)
class PageDraftRecord:
    draft: PageDraft
    coverage: PageDraftCoverage


@dataclass(frozen=True)
class PageSynthesisOutput:
    plans: tuple[PageSynthesisPlan, ...]
    draft_records: tuple[PageDraftRecord, ...]
    findings: tuple[PageSynthesisFinding, ...]


def ledger_ref(ledger_entry_id: str) -> EvidenceSupportRef:
    return EvidenceSupportRef("ledger", ledger_entry_id)


def atom_ref(technical_atom_id: str) -> EvidenceSupportRef:
    return EvidenceSupportRef("atom", technical_atom_id)


def anchor_ref(stable_atom_anchor: str) -> EvidenceSupportRef:
    return EvidenceSupportRef("anchor", stable_atom_anchor)


def evidence_block_ref(evidence_block_id: str) -> EvidenceSupportRef:
    return EvidenceSupportRef("evidence-block", evidence_block_id)
