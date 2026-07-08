"""Coverage contract between evidence packs and human articles."""

from __future__ import annotations

from dataclasses import dataclass

from llmwiki.domain.ledger.canonical import deterministic_id
from llmwiki.domain.ledger.evidence_pack import EvidencePack, EvidencePackItem, SupportRef
from llmwiki.domain.ledger.human_article import ArticleClaim, HumanArticle
from llmwiki.domain.ledger.page_synthesis_text import canonical_text

EvidenceItemGroups = tuple[tuple[EvidencePackItem, ...], ...]


@dataclass(frozen=True)
class ArticleCoverageRequirement:
    requirement_id: str
    page_id: str
    required: bool
    evidence_record_types: tuple[str, ...]
    support_refs: tuple[SupportRef, ...]
    representative_text: str
    requirement_reason: str


@dataclass(frozen=True)
class ArticleEvidenceCoverage:
    requirement_id: str
    required: bool
    support_refs: tuple[SupportRef, ...]
    article_claim_ids: tuple[str, ...]
    coverage_status: str


@dataclass(frozen=True)
class ArticleEvidenceCoverageMetrics:
    page_id: str
    required_evidence_count: int
    covered_required_evidence_count: int
    uncovered_required_evidence_count: int
    total_used_support_count: int
    required_coverage_ratio: float


_RECIPE_REQUIRED_CONTEXT_COUNT = 2
_TOPIC_SUPPORT_REQUIRED_COUNT = 6
_BROAD_TOPIC_SUPPORT_REQUIRED_COUNT = 8
_COLLECTION_REQUIRED_COUNT = 4


def build_article_coverage_requirements(
    pack: EvidencePack,
) -> tuple[ArticleCoverageRequirement, ...]:
    groups = _group_duplicate_items(pack.items)
    if not groups:
        return ()
    required_codes = _required_support_codes(pack.page_family, groups)
    return tuple(
        _requirement_for_group(
            pack,
            index,
            group,
            required=any(item.support_ref.code in required_codes for item in group),
        )
        for index, group in enumerate(groups, start=1)
    )


def compute_article_evidence_coverage(
    pack: EvidencePack, article: HumanArticle
) -> tuple[ArticleEvidenceCoverage, ...]:
    claims_by_support = _claims_by_support(article.claims)
    coverage: list[ArticleEvidenceCoverage] = []
    for requirement in build_article_coverage_requirements(pack):
        claim_ids = _claim_ids_for(requirement.support_refs, claims_by_support)
        coverage.append(
            ArticleEvidenceCoverage(
                requirement.requirement_id,
                requirement.required,
                requirement.support_refs,
                claim_ids,
                "covered" if claim_ids else "uncovered",
            )
        )
    return tuple(coverage)


def article_evidence_coverage_metrics(
    pack: EvidencePack, article: HumanArticle
) -> ArticleEvidenceCoverageMetrics:
    coverage = compute_article_evidence_coverage(pack, article)
    required = tuple(item for item in coverage if item.required)
    covered = tuple(item for item in required if item.coverage_status == "covered")
    used = {ref.code for claim in article.claims for ref in claim.support_refs}
    ratio = len(covered) / len(required) if required else 1.0
    return ArticleEvidenceCoverageMetrics(
        page_id=pack.page_id,
        required_evidence_count=len(required),
        covered_required_evidence_count=len(covered),
        uncovered_required_evidence_count=len(required) - len(covered),
        total_used_support_count=len(used),
        required_coverage_ratio=ratio,
    )


def uncovered_required_evidence(
    pack: EvidencePack, article: HumanArticle
) -> tuple[ArticleCoverageRequirement, ...]:
    uncovered_ids = {
        item.requirement_id
        for item in compute_article_evidence_coverage(pack, article)
        if item.required and item.coverage_status == "uncovered"
    }
    return tuple(
        requirement
        for requirement in build_article_coverage_requirements(pack)
        if requirement.requirement_id in uncovered_ids
    )


def _required_support_codes(page_family: str, groups: EvidenceItemGroups) -> frozenset[str]:
    if page_family == "recipe-pattern":
        required = [
            *(_groups_of_type(groups, {"code_example"})),
            *(_groups_of_type(groups, {"definition"})),
            *(_groups_of_type(groups, {"argument", "procedure_step"})[
                :_RECIPE_REQUIRED_CONTEXT_COUNT
            ]),
        ]
        return _codes(required)
    if page_family == "procedure-guide":
        return _codes(
            [
                *_groups_of_type(groups, {"procedure_step"}),
                *_groups_of_type(groups, {"rule", "formula", "table_fact"}),
                *_groups_of_type(groups, {"definition", "entity_fact"}),
            ]
        )
    if page_family in {"topic-concept", "broad-topic"}:
        support_count = (
            _BROAD_TOPIC_SUPPORT_REQUIRED_COUNT
            if page_family == "broad-topic"
            else _TOPIC_SUPPORT_REQUIRED_COUNT
        )
        definitions = _groups_of_type(groups, {"definition"})
        support = _groups_of_type(
            groups, {"rule", "code_example", "table_fact", "formula"}
        )[:support_count]
        required = [*definitions, *support]
        if not required:
            required = list(groups[: min(4, len(groups))])
        return _codes(required)
    if page_family == "collection-page":
        return _codes(groups[: min(_COLLECTION_REQUIRED_COUNT, len(groups))])
    return _codes(groups)


def _requirement_for_group(
    pack: EvidencePack,
    index: int,
    group: tuple[EvidencePackItem, ...],
    *,
    required: bool,
) -> ArticleCoverageRequirement:
    text = _representative_text(group)
    record_types = tuple(dict.fromkeys(item.evidence_record_type for item in group))
    support_refs = tuple(item.support_ref for item in group)
    return ArticleCoverageRequirement(
        requirement_id=deterministic_id(
            "article-coverage-requirement",
            pack.source_hash,
            pack.page_id,
            str(index),
            _evidence_key(group[0]),
        ),
        page_id=pack.page_id,
        required=required,
        evidence_record_types=record_types,
        support_refs=support_refs,
        representative_text=text,
        requirement_reason="required-by-page-family" if required else "optional-context",
    )


def _group_duplicate_items(
    items: tuple[EvidencePackItem, ...]
) -> EvidenceItemGroups:
    groups: dict[str, list[EvidencePackItem]] = {}
    order: list[str] = []
    for item in items:
        key = _evidence_key(item)
        if key not in groups:
            groups[key] = []
            order.append(key)
        groups[key].append(item)
    return tuple(tuple(groups[key]) for key in order)


def _evidence_key(item: EvidencePackItem) -> str:
    text = item.payload_text.strip() or item.source_text.strip()
    return canonical_text(text)


def _groups_of_type(
    groups: EvidenceItemGroups, record_types: set[str]
) -> EvidenceItemGroups:
    return tuple(
        group
        for group in groups
        if any(item.evidence_record_type in record_types for item in group)
    )


def _codes(groups: EvidenceItemGroups | list[tuple[EvidencePackItem, ...]]) -> frozenset[str]:
    return frozenset(item.support_ref.code for group in groups for item in group)


def _claims_by_support(claims: tuple[ArticleClaim, ...]) -> dict[str, tuple[str, ...]]:
    claim_ids_by_support: dict[str, list[str]] = {}
    for claim in claims:
        for support_ref in claim.support_refs:
            claim_ids_by_support.setdefault(support_ref.code, []).append(claim.claim_id)
    return {
        support_ref: tuple(dict.fromkeys(claim_ids))
        for support_ref, claim_ids in claim_ids_by_support.items()
    }


def _claim_ids_for(
    support_refs: tuple[SupportRef, ...], claims_by_support: dict[str, tuple[str, ...]]
) -> tuple[str, ...]:
    claim_ids: list[str] = []
    for support_ref in support_refs:
        claim_ids.extend(claims_by_support.get(support_ref.code, ()))
    return tuple(dict.fromkeys(claim_ids))


def _representative_text(group: tuple[EvidencePackItem, ...]) -> str:
    item = group[0]
    text = item.payload_text.strip() or item.source_text.strip()
    return " ".join(text.split())[:240]
