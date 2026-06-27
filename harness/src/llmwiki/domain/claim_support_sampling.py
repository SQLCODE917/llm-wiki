"""Sampling and coverage analysis for claim-support candidates."""

from __future__ import annotations

import math
import re
from collections import Counter, defaultdict, deque
from collections.abc import Sequence
from dataclasses import replace

from llmwiki.domain.claim_support import (
    ClaimSupportCandidate,
    ClaimSupportCoverageCount,
    ClaimSupportSampleCoverage,
    ClaimSupportSampleStrategy,
)

_NUMERIC_TOKEN_RE = re.compile(r"^\d+$")
_RISK_PATTERNS: tuple[tuple[str, tuple[str, ...]], ...] = (
    ("requirement", (r"\bmust\b", r"\brequire\w*\b", r"\bshall\b", r"\bshould\b")),
    ("limitation", (r"\bcannot\b", r"\bcan only\b", r"\bonly\b", r"\bexcept\b", r"\bunless\b")),
    ("quantitative", (r"\b\d+\b", r"\bbonus\b", r"\bpenalty\b", r"\bscore\b", r"\bpoints?\b")),
    ("procedure", (r"\broll\b", r"\bcheck\b", r"\bstep\b", r"\bcompare\b", r"\bcalculate\b")),
    ("mechanism", (r"\beffect\b", r"\bdamage\b", r"\bresist\b", r"\bduration\b", r"\btarget\b")),
    ("negative-evidence", (r"\bno\b", r"\bnot\b", r"\bwithout\b")),
)
_RISK_REGEXES = tuple(
    (tag, tuple(re.compile(pattern) for pattern in patterns)) for tag, patterns in _RISK_PATTERNS
)


def prepare_claim_support_candidates(
    candidates: Sequence[ClaimSupportCandidate],
) -> tuple[ClaimSupportCandidate, ...]:
    return tuple(
        replace(candidate, risk_tags=claim_support_risk_tags(candidate.claim_text))
        for candidate in candidates
    )


def claim_support_risk_tags(claim_text: str) -> tuple[str, ...]:
    lowered = claim_text.lower()
    return tuple(
        tag
        for tag, patterns in _RISK_REGEXES
        if any(pattern.search(lowered) for pattern in patterns)
    )


def sample_claim_support_candidates(
    candidates: Sequence[ClaimSupportCandidate],
    *,
    sample_strategy: ClaimSupportSampleStrategy,
) -> tuple[ClaimSupportCandidate, ...]:
    prepared = prepare_claim_support_candidates(candidates)
    if sample_strategy == "ordered":
        return prepared
    bucket_by_candidate = source_buckets_for_candidates(prepared)
    seeded = _seed_candidate_kinds(prepared)
    seeded_ids = {candidate.candidate_id for candidate in seeded}
    buckets = _bucket_round_robin_candidates(
        tuple(candidate for candidate in prepared if candidate.candidate_id not in seeded_ids),
        bucket_by_candidate,
    )
    return (*seeded, *_round_robin_buckets(buckets))


def claim_support_sample_coverage(
    available: Sequence[ClaimSupportCandidate],
    sampled: Sequence[ClaimSupportCandidate],
    *,
    sample_strategy: ClaimSupportSampleStrategy,
) -> ClaimSupportSampleCoverage:
    available_prepared = prepare_claim_support_candidates(available)
    sampled_prepared = prepare_claim_support_candidates(sampled)
    available_buckets = source_buckets_for_candidates(available_prepared)
    sampled_bucket_labels = {
        available_buckets[candidate.candidate_id]
        for candidate in sampled_prepared
        if candidate.candidate_id in available_buckets
    }
    available_pages = {candidate.page_id for candidate in available_prepared}
    sampled_pages = {candidate.page_id for candidate in sampled_prepared}
    return ClaimSupportSampleCoverage(
        sample_strategy=sample_strategy,
        available_candidates=len(available_prepared),
        sampled_candidates=len(sampled_prepared),
        available_pages=len(available_pages),
        sampled_pages=len(sampled_pages),
        available_source_buckets=len(set(available_buckets.values())),
        sampled_source_buckets=len(sampled_bucket_labels),
        candidate_kind_counts=_coverage_counts(
            tuple(candidate.candidate_kind for candidate in available_prepared),
            tuple(candidate.candidate_kind for candidate in sampled_prepared),
        ),
        risk_tag_counts=_coverage_counts(
            _risk_labels(available_prepared),
            _risk_labels(sampled_prepared),
        ),
    )


def source_buckets_for_candidates(
    candidates: Sequence[ClaimSupportCandidate],
) -> dict[str, str]:
    page_ids = tuple(dict.fromkeys(candidate.page_id for candidate in candidates))
    numeric_buckets = {page_id: _numeric_source_bucket(page_id) for page_id in page_ids}
    if len(set(numeric_buckets.values())) > 1:
        return {
            candidate.candidate_id: numeric_buckets[candidate.page_id] for candidate in candidates
        }
    page_buckets = _page_band_buckets(page_ids)
    return {candidate.candidate_id: page_buckets[candidate.page_id] for candidate in candidates}


def _seed_candidate_kinds(
    candidates: tuple[ClaimSupportCandidate, ...],
) -> tuple[ClaimSupportCandidate, ...]:
    if len({candidate.candidate_kind for candidate in candidates}) < 2:
        return ()
    seeded: list[ClaimSupportCandidate] = []
    seen: set[str] = set()
    for candidate in sorted(
        candidates,
        key=lambda candidate: (
            candidate.candidate_kind != "source-summary",
            -len(candidate.risk_tags),
        ),
    ):
        if candidate.candidate_kind in seen:
            continue
        seeded.append(candidate)
        seen.add(candidate.candidate_kind)
    return tuple(seeded)


def _bucket_round_robin_candidates(
    candidates: tuple[ClaimSupportCandidate, ...],
    bucket_by_candidate: dict[str, str],
) -> dict[str, deque[ClaimSupportCandidate]]:
    pages_by_bucket: dict[str, dict[str, list[ClaimSupportCandidate]]] = defaultdict(
        lambda: defaultdict(list)
    )
    page_order_by_bucket: dict[str, list[str]] = defaultdict(list)
    for candidate in candidates:
        bucket = bucket_by_candidate[candidate.candidate_id]
        if candidate.page_id not in pages_by_bucket[bucket]:
            page_order_by_bucket[bucket].append(candidate.page_id)
        pages_by_bucket[bucket][candidate.page_id].append(candidate)
    result: dict[str, deque[ClaimSupportCandidate]] = {}
    for bucket, pages in pages_by_bucket.items():
        page_queues = {
            page_id: deque(sorted(page_candidates, key=_candidate_priority))
            for page_id, page_candidates in pages.items()
        }
        ordered: deque[ClaimSupportCandidate] = deque()
        while any(page_queues.values()):
            for page_id in page_order_by_bucket[bucket]:
                if page_queues[page_id]:
                    ordered.append(page_queues[page_id].popleft())
        result[bucket] = ordered
    return result


def _round_robin_buckets(
    buckets: dict[str, deque[ClaimSupportCandidate]],
) -> tuple[ClaimSupportCandidate, ...]:
    ordered: list[ClaimSupportCandidate] = []
    bucket_order = sorted(buckets, key=_bucket_sort_key)
    while any(buckets.values()):
        for bucket in bucket_order:
            if buckets[bucket]:
                ordered.append(buckets[bucket].popleft())
    return tuple(ordered)


def _candidate_priority(candidate: ClaimSupportCandidate) -> tuple[int, int]:
    return (-len(candidate.risk_tags), 0 if candidate.candidate_kind == "source-summary" else 1)


def _numeric_source_bucket(page_id: str) -> str:
    parts = page_id.split("-")
    for index, part in enumerate(parts):
        if _NUMERIC_TOKEN_RE.match(part) and index + 1 < len(parts):
            return f"section-{int(part)}"
    return "front"


def _page_band_buckets(page_ids: tuple[str, ...]) -> dict[str, str]:
    if not page_ids:
        return {}
    bucket_count = min(10, len(page_ids))
    band_size = max(1, math.ceil(len(page_ids) / bucket_count))
    return {
        page_id: f"page-band-{index // band_size + 1:02d}" for index, page_id in enumerate(page_ids)
    }


def _bucket_sort_key(bucket: str) -> tuple[int, int, str]:
    if bucket == "front":
        return (0, -1, bucket)
    if bucket.startswith("section-"):
        return (1, int(bucket.removeprefix("section-")), bucket)
    if bucket.startswith("page-band-"):
        return (2, int(bucket.removeprefix("page-band-")), bucket)
    return (3, 0, bucket)


def _coverage_counts(
    available_labels: Sequence[str],
    sampled_labels: Sequence[str],
) -> tuple[ClaimSupportCoverageCount, ...]:
    available = Counter(available_labels)
    sampled = Counter(sampled_labels)
    return tuple(
        ClaimSupportCoverageCount(label, available[label], sampled.get(label, 0))
        for label in sorted(available)
    )


def _risk_labels(candidates: Sequence[ClaimSupportCandidate]) -> tuple[str, ...]:
    labels: list[str] = []
    for candidate in candidates:
        labels.extend(candidate.risk_tags or ("unclassified",))
    return tuple(labels)
