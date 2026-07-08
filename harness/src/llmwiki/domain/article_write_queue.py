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
    max_public_articles: int
    max_attempted_packs: int
    max_attempts_per_pack: int
    min_attempts_before_rate_gate: int = 8
    min_acceptance_rate: float = 0.25
    acceptance_rate_window: int = 8
    family_targets: tuple[tuple[str, int], ...] = ()
    family_caps: tuple[tuple[str, int], ...] = ()


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
    acceptance_rate: float
    rolling_acceptance_rate: float
    family_counts: tuple[tuple[str, int], ...]
    findings: tuple[ArticleWriteQueueFinding, ...]


def default_article_write_queue_policy(
    source_profile_kind: str, valid_pack_count: int = 0
) -> ArticleWriteQueuePolicy:
    return article_write_queue_policy_for_source(source_profile_kind, valid_pack_count)


def article_write_queue_policy_for_source(
    source_profile_kind: str, valid_pack_count: int
) -> ArticleWriteQueuePolicy:
    pack_count = max(0, valid_pack_count)
    if source_profile_kind == "programming-prose":
        return _policy(
            source_profile_kind,
            pack_count,
            target=3,
            max_public=24,
            max_attempted=48,
            family_targets=((PAGE_FAMILY_RECIPE_PATTERN, 6), (PAGE_FAMILY_TOPIC_CONCEPT, 4)),
            family_caps=(
                (PAGE_FAMILY_RECIPE_PATTERN, 14),
                (PAGE_FAMILY_TOPIC_CONCEPT, 10),
                (PAGE_FAMILY_COLLECTION_PAGE, 2),
            ),
        )
    if source_profile_kind == "rpg-rules":
        return _policy(
            source_profile_kind,
            pack_count,
            target=3,
            max_public=32,
            max_attempted=64,
            family_targets=(
                (PAGE_FAMILY_PROCEDURE_GUIDE, 8),
                (PAGE_FAMILY_TOPIC_CONCEPT, 8),
            ),
            family_caps=(
                (PAGE_FAMILY_PROCEDURE_GUIDE, 14),
                (PAGE_FAMILY_TOPIC_CONCEPT, 16),
                (PAGE_FAMILY_COLLECTION_PAGE, 2),
            ),
        )
    if source_profile_kind == "reference":
        return _policy(
            source_profile_kind,
            pack_count,
            target=3,
            max_public=18,
            max_attempted=36,
            family_targets=((PAGE_FAMILY_TOPIC_CONCEPT, 8), (PAGE_FAMILY_COLLECTION_PAGE, 4)),
            family_caps=((PAGE_FAMILY_TOPIC_CONCEPT, 12), (PAGE_FAMILY_COLLECTION_PAGE, 6)),
        )
    return _policy(
        source_profile_kind,
        pack_count,
        target=3,
        max_public=12,
        max_attempted=24,
        family_targets=((PAGE_FAMILY_TOPIC_CONCEPT, 6),),
        family_caps=((PAGE_FAMILY_TOPIC_CONCEPT, 10), (PAGE_FAMILY_COLLECTION_PAGE, 2)),
    )


def _policy(
    source_profile_kind: str,
    valid_pack_count: int,
    *,
    target: int,
    max_public: int,
    max_attempted: int,
    family_targets: tuple[tuple[str, int], ...],
    family_caps: tuple[tuple[str, int], ...],
) -> ArticleWriteQueuePolicy:
    public_cap = min(valid_pack_count, max_public)
    attempt_cap = min(valid_pack_count, max_attempted)
    return ArticleWriteQueuePolicy(
        source_profile_kind,
        min(target, public_cap),
        public_cap,
        attempt_cap,
        1,
        family_targets=tuple(
            (family, min(count, valid_pack_count)) for family, count in family_targets
        ),
        family_caps=tuple((family, min(count, public_cap)) for family, count in family_caps),
    )


def ordered_article_write_packs(
    packs: tuple[EvidencePack, ...], policy: ArticleWriteQueuePolicy
) -> tuple[EvidencePack, ...]:
    selected: list[EvidencePack] = []
    selected_ids: set[str] = set()
    for family, target_count in policy.family_targets:
        for pack in packs:
            if len([item for item in selected if item.page_family == family]) >= target_count:
                break
            if pack.page_family == family and pack.page_id not in selected_ids:
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
        acceptance_rate=acceptance_rate(len(accepted_page_ids), len(attempted_page_ids)),
        rolling_acceptance_rate=rolling_acceptance_rate(
            attempted_page_ids, accepted_page_ids, policy.acceptance_rate_window
        ),
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


def acceptance_rate(accepted_count: int, attempted_count: int) -> float:
    if attempted_count <= 0:
        return 0.0
    return accepted_count / attempted_count


def rolling_acceptance_rate(
    attempted_page_ids: tuple[str, ...],
    accepted_page_ids: tuple[str, ...],
    window: int,
) -> float:
    if window <= 0 or not attempted_page_ids:
        return acceptance_rate(len(accepted_page_ids), len(attempted_page_ids))
    accepted = set(accepted_page_ids)
    recent = attempted_page_ids[-window:]
    return acceptance_rate(len([page_id for page_id in recent if page_id in accepted]), len(recent))


def family_cap_reached(
    policy: ArticleWriteQueuePolicy,
    accepted_page_ids: tuple[str, ...],
    pack: EvidencePack,
    packs_by_page_id: dict[str, EvidencePack],
) -> bool:
    cap = dict(policy.family_caps).get(pack.page_family)
    if cap is None:
        return False
    accepted_count = len(
        [
            page_id
            for page_id in accepted_page_ids
            if (accepted_pack := packs_by_page_id.get(page_id)) is not None
            and accepted_pack.page_family == pack.page_family
        ]
    )
    return accepted_count >= cap


def all_available_family_caps_reached(
    policy: ArticleWriteQueuePolicy,
    accepted_page_ids: tuple[str, ...],
    packs_by_page_id: dict[str, EvidencePack],
) -> bool:
    available_families = {pack.page_family for pack in packs_by_page_id.values()}
    capped_families = set(dict(policy.family_caps))
    if not available_families or not available_families.issubset(capped_families):
        return False
    return all(
        family_cap_reached(policy, accepted_page_ids, pack, packs_by_page_id)
        for pack in packs_by_page_id.values()
    )


def acceptance_rate_gate_reached(
    policy: ArticleWriteQueuePolicy,
    attempted_page_ids: tuple[str, ...],
    accepted_page_ids: tuple[str, ...],
) -> bool:
    if len(attempted_page_ids) < policy.min_attempts_before_rate_gate:
        return False
    return (
        rolling_acceptance_rate(
            attempted_page_ids, accepted_page_ids, policy.acceptance_rate_window
        )
        < policy.min_acceptance_rate
    )


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
        for family, _target_count in policy.family_targets
        if family in available_families and family not in accepted_families
    )
