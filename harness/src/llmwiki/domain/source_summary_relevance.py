"""Source-summary topic relevance and selection scoring."""

from __future__ import annotations

import re
from functools import lru_cache

from llmwiki.domain.objects import SourceClaim
from llmwiki.domain.planning_analysis import tokens
from llmwiki.domain.source_claim_quality import CLAIM_ELIGIBLE, eligible_claims

EARLY_CLAIM_WINDOW = 20
TOPIC_FOCUS_GAP = 3
STRONG_TOPIC_OVERLAP = 2
MAX_STRONG_FOCUS_LAG = EARLY_CLAIM_WINDOW

_SKILL_REFERENCE_RE = re.compile(r"\b([a-z][a-z0-9-]*)\s+skills?\b", re.IGNORECASE)
_CLASS_OR_PROFESSION_REFERENCE_RE = re.compile(
    r"\b([a-z][a-z0-9-]*)s?\s+(?:is|are)\s+(?:an?\s+)?(?:[a-z0-9-]+\s+){0,4}"
    r"(?:class|profession)\b",
    re.IGNORECASE,
)
_PAGE_TERM_STOPWORDS = frozenset(
    {
        "basic",
        "chapter",
        "complete",
        "edition",
        "for",
        "list",
        "part",
        "rpg",
        "rule",
        "rules",
        "section",
        "skill",
        "skills",
        "source",
        "sword",
        "world",
    }
)
_GENERIC_PAGE_MATCH_TERMS = frozenset(
    {
        "check",
        "checks",
        "chapter",
        "complete",
        "edition",
        "how",
        "list",
        "magic",
        "magical",
        "part",
        "rule",
        "rules",
        "section",
        "source",
        "sword",
        "type",
        "types",
        "world",
    }
)


def selection_score(page_terms: frozenset[str], claim: SourceClaim) -> float:
    relevance = min(page_overlap(page_terms, claim) * 0.12, 0.36)
    eligibility_bonus = 0.20 if claim.claim_eligibility == CLAIM_ELIGIBLE else -0.20
    centrality_bonus = min(claim.claim_centrality * 0.15, 0.15)
    return (
        claim.claim_salience
        + relevance
        + eligibility_bonus
        + centrality_bonus
        - min(claim_position(claim) * 0.008, 0.65)
    )


def page_overlap(page_terms: frozenset[str], claim: SourceClaim) -> int:
    if not page_terms:
        return 0
    claim_terms = _claim_term_variants(claim.statement)
    specific_page_terms = page_terms - _GENERIC_PAGE_MATCH_TERMS
    specific_overlap = specific_page_terms & claim_terms
    if specific_overlap:
        return len(specific_overlap)
    if specific_page_terms:
        return 0
    return len(page_terms & claim_terms)


def topic_focused_claims(
    page_terms: frozenset[str],
    claims: tuple[SourceClaim, ...],
    min_claims: int,
) -> tuple[SourceClaim, ...]:
    if not page_terms:
        return claims
    start_index = _topic_focus_start_index(page_terms, claims)
    if len(claims) <= EARLY_CLAIM_WINDOW and not start_index:
        return claims
    if start_index is None:
        return claims
    focused: list[SourceClaim] = []
    gap = 0
    for claim in claims[start_index:]:
        if page_overlap(page_terms, claim) > 0:
            gap = 0
        else:
            gap += 1
            if gap > TOPIC_FOCUS_GAP:
                break
        focused.append(claim)
    if len(focused) < min_claims:
        return claims
    if len(eligible_claims(focused)) < min(min_claims, len(eligible_claims(claims))):
        return claims
    return tuple(focused)


def _topic_focus_start_index(
    page_terms: frozenset[str], claims: tuple[SourceClaim, ...]
) -> int | None:
    first_overlap_index = next(
        (index for index, claim in enumerate(claims) if page_overlap(page_terms, claim) > 0),
        None,
    )
    if (
        first_overlap_index is not None
        and claim_position(claims[first_overlap_index]) > MAX_STRONG_FOCUS_LAG
    ):
        return None
    strong_overlap = min(STRONG_TOPIC_OVERLAP, len(page_terms))
    start_index = next(
        (
            index
            for index, claim in enumerate(claims)
            if page_overlap(page_terms, claim) >= strong_overlap
        ),
        None,
    )
    if start_index is not None:
        if (
            first_overlap_index is not None
            and start_index - first_overlap_index > MAX_STRONG_FOCUS_LAG
        ):
            return None
        return start_index
    return first_overlap_index


def first_relevant_claim_position(
    page_terms: frozenset[str],
    claims: tuple[SourceClaim, ...],
) -> int:
    positions = tuple(claim_position(claim) for claim in claims if page_overlap(page_terms, claim))
    return min(positions) if positions else 0


def after_first_relevant_claim(first_relevant_position: int, claim: SourceClaim) -> bool:
    return not first_relevant_position or claim_position(claim) >= first_relevant_position


def without_competing_section_claims(
    page_terms: frozenset[str],
    claims: list[SourceClaim],
) -> list[SourceClaim]:
    if not page_terms:
        return claims
    return [
        claim
        for claim in claims
        if not _has_competing_section_reference(page_terms, claim.statement)
    ]


def page_terms(page_id: str) -> frozenset[str]:
    parts = page_id.split("-")
    for index in range(len(parts) - 1):
        if parts[index].isdigit() and parts[index + 1].isdigit():
            return _specific_page_terms(_page_title_tokens(tuple(parts[index + 2 :])))
    return _specific_page_terms(_page_title_tokens(tuple(parts)))


def claim_position(claim: SourceClaim) -> int:
    match = re.search(r"-(\d{4})$", claim.source_claim_id)
    if match is None:
        return 0
    return int(match.group(1))


def _has_competing_section_reference(page_terms: frozenset[str], statement: str) -> bool:
    for match in _SKILL_REFERENCE_RE.finditer(statement):
        skill_terms = _term_variants((match.group(1).lower(),))
        if page_terms.isdisjoint(skill_terms):
            return True
    for match in _CLASS_OR_PROFESSION_REFERENCE_RE.finditer(statement):
        section_terms = _term_variants((match.group(1).lower(),))
        if page_terms.isdisjoint(section_terms):
            return True
    return False


def _page_title_tokens(parts: tuple[str, ...]) -> tuple[str, ...]:
    title_tokens = tuple(tokens(" ".join(parts)))
    if "magic" in parts and {"use", "using", "cast", "casting", "casts"} & set(parts):
        return title_tokens + ("cast", "casting")
    return title_tokens


def _specific_page_terms(page_terms: tuple[str, ...]) -> frozenset[str]:
    specific = tuple(term for term in page_terms if term not in _PAGE_TERM_STOPWORDS)
    return _term_variants(specific or page_terms)


def _term_variants(terms: tuple[str, ...]) -> frozenset[str]:
    variants: set[str] = set(terms)
    for term in terms:
        if len(term) > 3 and term.endswith("s"):
            variants.add(term[:-1])
        if len(term) > 5 and term.endswith("ing"):
            stem = term[:-3]
            if len(stem) >= 4:
                variants.add(stem)
        if term == "throwing":
            variants.add("thrown")
    return frozenset(variants)


@lru_cache(maxsize=20_000)
def _claim_term_variants(statement: str) -> frozenset[str]:
    return _term_variants(tuple(tokens(statement)))
