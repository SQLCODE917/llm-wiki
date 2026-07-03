"""Source-neutral scope boundary detection."""

from __future__ import annotations

import re
from collections.abc import Sequence
from dataclasses import dataclass

from llmwiki.domain.objects import SourceClaim

SOURCE_SCOPE_TRANSITION_ELIGIBILITY = "scope-transition"
SOURCE_SCOPE_FUTURE_TRANSITION = "future-scope-transition"

_SOURCE_CLAIM_SENTENCE_RE = re.compile(r"\bs\.(\d+)\b")

_FUTURE_SCOPE_PATTERNS: tuple[tuple[re.Pattern[str], float, str], ...] = (
    (
        re.compile(
            r"\b(?:we|you|readers?|this\s+(?:section|chapter|source|text|document))\s+"
            r"(?:have(?:n't| not)|has(?:n't| not)|had(?:n't| not))\s+"
            r"(?:yet\s+)?(?:encountered|seen|introduced|covered|discussed|examined|considered)\b"
            r"(?=[^.!?]{0,120}\byet\b)",
            re.IGNORECASE,
        ),
        0.9,
        "The text says a subject has not yet been introduced or covered.",
    ),
    (
        re.compile(
            r"\b(?:we|you|readers?)\s+(?:will|'ll|shall)\s+"
            r"(?:see|encounter|discuss|cover|introduce|return\s+to|examine|consider|turn\s+to)\b"
            r"(?=[^.!?]{0,120}\b(?:later|next|following|below|subsequent)\b)",
            re.IGNORECASE,
        ),
        0.82,
        "The text points the reader to later coverage.",
    ),
    (
        re.compile(
            r"\b(?:next|following|subsequent|later)\s+"
            r"(?:section|chapter|example|case|part)\b",
            re.IGNORECASE,
        ),
        0.72,
        "The text names a later source segment.",
    ),
)


@dataclass(frozen=True)
class SourceScopeBoundary:
    unit_id: str
    boundary_claim_id: str
    sentence_index: int
    category: str
    confidence: float
    rationale: str


def source_scope_boundary_for_text(text: str) -> tuple[str, float, str] | None:
    normalized = " ".join(text.split())
    if not normalized:
        return None
    for pattern, confidence, rationale in _FUTURE_SCOPE_PATTERNS:
        if pattern.search(normalized):
            return SOURCE_SCOPE_FUTURE_TRANSITION, confidence, rationale
    return None


def is_source_scope_transition(text: str) -> bool:
    return source_scope_boundary_for_text(text) is not None


def source_scope_boundaries(
    source_claims: Sequence[SourceClaim],
) -> tuple[SourceScopeBoundary, ...]:
    boundaries: list[SourceScopeBoundary] = []
    for claim in source_claims:
        boundary = source_scope_boundary_for_text(claim.statement)
        if boundary is None:
            continue
        sentence_index = source_claim_sentence_index(claim.source_span, claim.source_claim_id)
        if sentence_index is None:
            continue
        category, confidence, rationale = boundary
        boundaries.append(
            SourceScopeBoundary(
                unit_id=claim.extracted_unit_id,
                boundary_claim_id=claim.source_claim_id,
                sentence_index=sentence_index,
                category=category,
                confidence=confidence,
                rationale=rationale,
            )
        )
    return tuple(boundaries)


def first_source_scope_boundary_index(texts: Sequence[str]) -> int | None:
    for index, text in enumerate(texts):
        if is_source_scope_transition(text):
            return index
    return None


def source_claim_sentence_index(source_span: str, source_claim_id: str = "") -> int | None:
    match = _SOURCE_CLAIM_SENTENCE_RE.search(source_span)
    if match:
        return int(match.group(1))
    suffix = source_claim_id.rsplit("-", 1)[-1]
    if suffix.isdigit():
        return int(suffix)
    return None
