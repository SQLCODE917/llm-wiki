"""Source claim inventory and source summary domain objects."""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

from llmwiki.domain.page_body_contracts import ResolvedPageBodyContract

if TYPE_CHECKING:
    from llmwiki.domain.objects import Evidence


@dataclass(frozen=True)
class ClaimRoleTag:
    tag_name: str


def default_claim_role_tags() -> tuple[ClaimRoleTag, ...]:
    return tuple(
        ClaimRoleTag(tag_name)
        for tag_name in (
            "identity",
            "definition",
            "attribute",
            "function",
            "mechanism",
            "method",
            "evidence",
            "provenance",
            "temporal",
            "quantitative",
            "relationship",
            "comparison",
            "requirement",
            "procedure",
            "limitation",
            "source-uncertainty",
            "ordinary-modality",
            "negative-evidence",
            "open-question",
            "analogy",
            "worked-example",
            "source-framing",
        )
    )


@dataclass(frozen=True)
class SourceClaim:
    source_claim_id: str
    statement: str
    evidence: Evidence
    extracted_unit_id: str
    source_span: str
    claim_role_tags: tuple[str, ...] = ()
    claim_salience: float = 0.0
    claim_certainty: str = "supported"
    subject_terms: tuple[str, ...] = ()
    claim_eligibility: str = "eligible"
    claim_centrality: float = 0.0


@dataclass(frozen=True)
class SourceClaimGroup:
    source_claim_group_id: str
    label: str
    source_claims: tuple[str, ...]
    extracted_units: tuple[str, ...] = ()
    claim_role_tags: tuple[str, ...] = ()
    claim_salience: float = 0.0


@dataclass(frozen=True)
class SourceSummaryPlan:
    source_summary_plan_id: str
    page_id: str
    selected_source_claims: tuple[str, ...]
    required_claim_role_tags: tuple[str, ...] = ()
    required_source_claim_groups: tuple[str, ...] = ()
    required_source_citations: tuple[str, ...] = ()
    coverage_policy: str = ""


@dataclass(frozen=True)
class SourceSummaryBullet:
    bullet_text: str
    covered_source_claims: tuple[str, ...]


@dataclass(frozen=True)
class SourceSummaryDraft:
    source_record_text: str
    claim_bullets: tuple[SourceSummaryBullet, ...]


@dataclass(frozen=True)
class SourceClaimQualityFixture:
    fixture_id: str
    source_locator: str
    heading_path: str
    statement: str
    expected_claim_eligibility: str
    expected_claim_role_tags: tuple[str, ...] = ()


@dataclass(frozen=True)
class SourceSummaryQualityReport:
    selected_ineligible_claims: int = 0
    false_source_uncertainty_claims: int = 0
    source_framing_bullets: int = 0
    missing_unit_coverage: int = 0
    selected_ineligible_examples: tuple[str, ...] = ()
    false_source_uncertainty_examples: tuple[str, ...] = ()
    source_framing_examples: tuple[str, ...] = ()
    missing_unit_coverage_examples: tuple[str, ...] = ()


def should_create_source_summary_plan(contract: ResolvedPageBodyContract) -> bool:
    return contract.contract_id == "source-summary"
