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
class DraftEvidenceRef:
    support_kind: str
    support_id: str

    @property
    def code(self) -> str:
        return f"{self.support_kind}:{self.support_id}"


@dataclass(frozen=True)
class DraftEvidenceCard:
    evidence_ref: DraftEvidenceRef
    source_locator: str
    source_range_id: str
    summary: str
    exact_text: str = ""
    section_label: str = ""
    citation: str = ""


@dataclass(frozen=True)
class PageOutlineSection:
    heading: str
    purpose: str
    support_refs: tuple[DraftEvidenceRef, ...]
    block_kind: str = "bullet-list"


@dataclass(frozen=True)
class PageSynthesisRelatedLink:
    page_id: str
    label: str
    relation: str
    support_refs: tuple[DraftEvidenceRef, ...] = ()


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
    selected_evidence: tuple[DraftEvidenceCard, ...]
    related_links: tuple[PageSynthesisRelatedLink, ...] = ()

    @property
    def selected_support_codes(self) -> frozenset[str]:
        return frozenset(card.evidence_ref.code for card in self.selected_evidence)


@dataclass(frozen=True)
class DraftClaim:
    claim_id: str
    sentence: str
    support_refs: tuple[DraftEvidenceRef, ...]


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


def ledger_ref(ledger_entry_id: str) -> DraftEvidenceRef:
    return DraftEvidenceRef("ledger", ledger_entry_id)


def atom_ref(technical_atom_id: str) -> DraftEvidenceRef:
    return DraftEvidenceRef("atom", technical_atom_id)


def anchor_ref(stable_atom_anchor: str) -> DraftEvidenceRef:
    return DraftEvidenceRef("anchor", stable_atom_anchor)
