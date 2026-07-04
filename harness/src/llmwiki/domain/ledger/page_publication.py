"""Publication-planning records and conservative source-profile budgets."""

from __future__ import annotations

from dataclasses import dataclass

from llmwiki.domain.ledger.canonical import deterministic_id
from llmwiki.domain.ledger.page_title_lint import PageTitleFinding

PAGE_FAMILY_TOPIC_CONCEPT = "topic-concept"
PAGE_FAMILY_BROAD_TOPIC = "broad-topic"
PAGE_FAMILY_PROCEDURE_GUIDE = "procedure-guide"
PAGE_FAMILY_RECIPE_PATTERN = "recipe-pattern"
PAGE_FAMILY_COLLECTION_PAGE = "collection-page"
PAGE_FAMILY_SECTION_REFERENCE = "section-reference"

SOURCE_PROFILES = {"rpg-rules", "programming-prose", "reference", "general-prose"}
FAMILY_PRIORITY = {
    PAGE_FAMILY_PROCEDURE_GUIDE: 0,
    PAGE_FAMILY_RECIPE_PATTERN: 1,
    PAGE_FAMILY_TOPIC_CONCEPT: 2,
    PAGE_FAMILY_COLLECTION_PAGE: 3,
    PAGE_FAMILY_BROAD_TOPIC: 4,
    PAGE_FAMILY_SECTION_REFERENCE: 9,
}
FAMILY_RECORD_TYPES = {
    PAGE_FAMILY_TOPIC_CONCEPT: {
        "argument",
        "code_example",
        "definition",
        "entity_fact",
        "formula",
        "rule",
        "table_fact",
    },
    PAGE_FAMILY_BROAD_TOPIC: {
        "argument",
        "code_example",
        "definition",
        "entity_fact",
        "formula",
        "rule",
        "table_fact",
    },
    PAGE_FAMILY_PROCEDURE_GUIDE: {"entity_fact", "formula", "procedure_step", "rule", "table_fact"},
    PAGE_FAMILY_RECIPE_PATTERN: {"argument", "code_example", "definition", "procedure_step"},
    PAGE_FAMILY_COLLECTION_PAGE: {"definition", "entity_fact", "rule", "table_fact"},
    PAGE_FAMILY_SECTION_REFERENCE: {
        "argument",
        "code_example",
        "definition",
        "entity_fact",
        "formula",
        "procedure_step",
        "rule",
        "table_fact",
    },
}
MINIMUM_SUPPORT_COUNTS = {
    PAGE_FAMILY_TOPIC_CONCEPT: 2,
    PAGE_FAMILY_PROCEDURE_GUIDE: 2,
    PAGE_FAMILY_RECIPE_PATTERN: 2,
    PAGE_FAMILY_COLLECTION_PAGE: 3,
    PAGE_FAMILY_BROAD_TOPIC: 8,
    PAGE_FAMILY_SECTION_REFERENCE: 1,
}


@dataclass(frozen=True)
class PageCandidate:
    page_candidate_id: str
    source_id: str
    source_hash: str
    source_profile_kind: str
    page_id: str
    title: str
    page_kind: str
    page_family: str
    origin: str
    rank_score: float
    source_order: int
    supporting_evidence_record_ids: tuple[str, ...] = ()
    title_findings: tuple[PageTitleFinding, ...] = ()

    def __post_init__(self) -> None:
        object.__setattr__(
            self,
            "supporting_evidence_record_ids",
            tuple(dict.fromkeys(self.supporting_evidence_record_ids)),
        )
        object.__setattr__(self, "title_findings", tuple(self.title_findings))


@dataclass(frozen=True)
class PublicationBudget:
    publication_budget_id: str
    source_profile_kind: str
    max_public_pages: int
    max_pages_per_family: tuple[tuple[str, int], ...]
    minimum_support_counts: tuple[tuple[str, int], ...]
    explicit_section_page_ids: tuple[str, ...] = ()

    @property
    def family_caps(self) -> dict[str, int]:
        return dict(self.max_pages_per_family)

    @property
    def support_minimums(self) -> dict[str, int]:
        return dict(self.minimum_support_counts)


@dataclass(frozen=True)
class RejectedPageCandidate:
    candidate_id: str
    source_id: str
    page_id: str
    title: str
    page_family: str
    rejection_code: str
    supporting_evidence_record_ids: tuple[str, ...]
    message: str


@dataclass(frozen=True)
class PagePublicationPlan:
    page_publication_plan_id: str
    page_publication_plan_fingerprint: str
    source_id: str
    source_hash: str
    source_profile_kind: str
    publication_budget_id: str
    accepted_candidates: tuple[PageCandidate, ...]
    rejected_candidates: tuple[RejectedPageCandidate, ...]
    public_counts: tuple[tuple[str, int], ...]

    @property
    def accepted_page_ids(self) -> tuple[str, ...]:
        return tuple(candidate.page_id for candidate in self.accepted_candidates)


@dataclass(frozen=True)
class PublicationWalkabilityReport:
    source_id: str
    source_profile_kind: str
    accepted_count: int
    rejected_count: int
    family_counts: tuple[tuple[str, int], ...]
    budget_rejection_count: int


def conservative_publication_budget(
    source_profile_kind: str, *, explicit_section_page_ids: tuple[str, ...] = ()
) -> PublicationBudget:
    profile = source_profile_kind if source_profile_kind in SOURCE_PROFILES else "general-prose"
    total, caps = _profile_budget(profile)
    caps = {**caps, PAGE_FAMILY_SECTION_REFERENCE: len(explicit_section_page_ids)}
    return PublicationBudget(
        publication_budget_id=deterministic_id(
            "publication-budget", profile, ",".join(explicit_section_page_ids)
        ),
        source_profile_kind=profile,
        max_public_pages=total,
        max_pages_per_family=tuple(sorted(caps.items())),
        minimum_support_counts=tuple(sorted(MINIMUM_SUPPORT_COUNTS.items())),
        explicit_section_page_ids=explicit_section_page_ids,
    )


def _profile_budget(source_profile_kind: str) -> tuple[int, dict[str, int]]:
    return {
        "rpg-rules": (
            24,
            {
                PAGE_FAMILY_PROCEDURE_GUIDE: 8,
                PAGE_FAMILY_TOPIC_CONCEPT: 10,
                PAGE_FAMILY_BROAD_TOPIC: 2,
                PAGE_FAMILY_COLLECTION_PAGE: 4,
                PAGE_FAMILY_RECIPE_PATTERN: 0,
            },
        ),
        "programming-prose": (
            18,
            {
                PAGE_FAMILY_RECIPE_PATTERN: 6,
                PAGE_FAMILY_TOPIC_CONCEPT: 8,
                PAGE_FAMILY_BROAD_TOPIC: 2,
                PAGE_FAMILY_COLLECTION_PAGE: 2,
                PAGE_FAMILY_PROCEDURE_GUIDE: 2,
            },
        ),
        "reference": (
            12,
            {
                PAGE_FAMILY_COLLECTION_PAGE: 6,
                PAGE_FAMILY_TOPIC_CONCEPT: 4,
                PAGE_FAMILY_BROAD_TOPIC: 2,
            },
        ),
        "general-prose": (
            10,
            {
                PAGE_FAMILY_TOPIC_CONCEPT: 6,
                PAGE_FAMILY_BROAD_TOPIC: 2,
                PAGE_FAMILY_COLLECTION_PAGE: 2,
            },
        ),
    }[source_profile_kind]
