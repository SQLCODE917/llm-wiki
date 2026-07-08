"""Adaptive article write queue contracts."""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass, replace

from llmwiki.domain.ledger.canonical import artifact_fingerprint, deterministic_id
from llmwiki.domain.ledger.evidence_pack import EvidencePack

PAGE_FAMILY_PROCEDURE_GUIDE = "procedure-guide"
PAGE_FAMILY_RECIPE_PATTERN = "recipe-pattern"
PAGE_FAMILY_TOPIC_CONCEPT = "topic-concept"
PAGE_FAMILY_COLLECTION_PAGE = "collection-page"


@dataclass(frozen=True)
class ArticleWriteQueuePolicy:
    source_profile_kind: str
    target_accepted_articles: int
    max_attempted_packs: int
    max_attempts_per_pack: int
    preferred_families: tuple[str, ...] = ()


@dataclass(frozen=True)
class ArticleWriteQueueFinding:
    severity: str
    finding_code: str
    page_id: str
    message: str


@dataclass(frozen=True)
class ArticleWriteQueueRun:
    article_write_queue_run_id: str
    article_write_queue_fingerprint: str
    policy: ArticleWriteQueuePolicy
    attempted_page_ids: tuple[str, ...]
    accepted_page_ids: tuple[str, ...]
    skipped_page_ids: tuple[str, ...]
    exhausted_reason: str
    family_counts: tuple[tuple[str, int], ...]
    findings: tuple[ArticleWriteQueueFinding, ...]


def default_article_write_queue_policy(source_profile_kind: str) -> ArticleWriteQueuePolicy:
    return ArticleWriteQueuePolicy(
        source_profile_kind=source_profile_kind,
        target_accepted_articles=3,
        max_attempted_packs=8,
        max_attempts_per_pack=1,
        preferred_families=_preferred_families(source_profile_kind),
    )


def ordered_article_write_packs(
    packs: tuple[EvidencePack, ...], policy: ArticleWriteQueuePolicy
) -> tuple[EvidencePack, ...]:
    selected: list[EvidencePack] = []
    selected_ids: set[str] = set()
    for family in policy.preferred_families:
        pack = next(
            (
                item
                for item in packs
                if item.page_family == family and item.page_id not in selected_ids
            ),
            None,
        )
        if pack is not None:
            selected.append(pack)
            selected_ids.add(pack.page_id)
    remaining = tuple(pack for pack in packs if pack.page_id not in selected_ids)
    return (
        tuple(selected)
        + tuple(pack for pack in remaining if pack.page_family != PAGE_FAMILY_COLLECTION_PAGE)
        + tuple(pack for pack in remaining if pack.page_family == PAGE_FAMILY_COLLECTION_PAGE)
    )


def build_article_write_queue_run(
    *,
    source_hash: str,
    policy: ArticleWriteQueuePolicy,
    attempted_page_ids: tuple[str, ...],
    accepted_page_ids: tuple[str, ...],
    skipped_page_ids: tuple[str, ...],
    exhausted_reason: str,
    packs_by_page_id: dict[str, EvidencePack],
    findings: tuple[ArticleWriteQueueFinding, ...] = (),
) -> ArticleWriteQueueRun:
    family_counts = Counter(
        packs_by_page_id[page_id].page_family
        for page_id in accepted_page_ids
        if page_id in packs_by_page_id
    )
    all_findings = (
        *findings,
        *_family_mix_findings(policy, accepted_page_ids, packs_by_page_id),
    )
    draft = ArticleWriteQueueRun(
        article_write_queue_run_id=deterministic_id("article-write-queue-run", source_hash),
        article_write_queue_fingerprint="",
        policy=policy,
        attempted_page_ids=attempted_page_ids,
        accepted_page_ids=accepted_page_ids,
        skipped_page_ids=skipped_page_ids,
        exhausted_reason=exhausted_reason,
        family_counts=tuple(sorted(family_counts.items())),
        findings=all_findings,
    )
    fingerprint = artifact_fingerprint(
        draft, exclude=("article_write_queue_run_id", "article_write_queue_fingerprint")
    )
    return replace(
        draft,
        article_write_queue_run_id=deterministic_id(
            "article-write-queue-run", source_hash, fingerprint
        ),
        article_write_queue_fingerprint=fingerprint,
    )


def queue_finding(
    severity: str, code: str, page_id: str, message: str
) -> ArticleWriteQueueFinding:
    return ArticleWriteQueueFinding(severity, code, page_id, message)


def _preferred_families(source_profile_kind: str) -> tuple[str, ...]:
    if source_profile_kind == "programming-prose":
        return (PAGE_FAMILY_RECIPE_PATTERN, PAGE_FAMILY_TOPIC_CONCEPT)
    if source_profile_kind == "rpg-rules":
        return (PAGE_FAMILY_PROCEDURE_GUIDE, PAGE_FAMILY_TOPIC_CONCEPT)
    if source_profile_kind == "reference":
        return (PAGE_FAMILY_TOPIC_CONCEPT,)
    return (PAGE_FAMILY_TOPIC_CONCEPT,)


def _family_mix_findings(
    policy: ArticleWriteQueuePolicy,
    accepted_page_ids: tuple[str, ...],
    packs_by_page_id: dict[str, EvidencePack],
) -> tuple[ArticleWriteQueueFinding, ...]:
    accepted_families = {
        pack.page_family
        for page_id in accepted_page_ids
        if (pack := packs_by_page_id.get(page_id)) is not None
    }
    available_families = {pack.page_family for pack in packs_by_page_id.values()}
    return tuple(
        queue_finding(
            "info",
            "family-mix-unmet",
            "",
            f"preferred article family {family!r} was available but not accepted",
        )
        for family in policy.preferred_families
        if family in available_families and family not in accepted_families
    )
