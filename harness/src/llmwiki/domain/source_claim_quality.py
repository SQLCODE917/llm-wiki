"""Deterministic source-claim quality classification and reports."""

from __future__ import annotations

from llmwiki.domain.objects import SourceClaim
from llmwiki.domain.planning_analysis import tokens
from llmwiki.domain.source_claim_heuristics import (
    is_code_fragment,
    is_narrative_frame,
    is_rhetorical_example,
    is_source_furniture,
)
from llmwiki.domain.source_claim_roles import (
    CLAIM_ROLE_WEIGHTS,
    SOURCE_FRAMING_PREFIXES,
    claim_role_tags,
)

__all__ = ("SOURCE_FRAMING_PREFIXES", "claim_role_tags")

CLAIM_ELIGIBLE = "eligible"
INELIGIBLE_CLAIM_ELIGIBILITIES = frozenset(
    {
        "analogy",
        "rhetorical-example",
        "narrative-frame",
        "source-furniture",
        "code-fragment",
        "source-framing",
    }
)
def claim_eligibility(statement: str, role_tags: tuple[str, ...]) -> str:
    lowered = statement.lower().strip()
    if "source-framing" in role_tags:
        return "source-framing"
    if is_code_fragment(statement):
        return "code-fragment"
    if is_source_furniture(lowered):
        return "source-furniture"
    if is_rhetorical_example(lowered):
        return "rhetorical-example"
    if is_narrative_frame(lowered):
        return "narrative-frame"
    if "analogy" in role_tags:
        return "analogy"
    return CLAIM_ELIGIBLE


def claim_centrality(statement: str, heading_path: str) -> float:
    heading_terms = set(tokens(heading_path))
    statement_terms = set(tokens(statement))
    if not heading_terms or not statement_terms:
        return 0.0
    return round(len(heading_terms & statement_terms) / len(heading_terms), 3)


def claim_salience(
    statement: str,
    role_tags: tuple[str, ...],
    eligibility: str = CLAIM_ELIGIBLE,
    centrality: float = 0.0,
) -> float:
    role_score = max((CLAIM_ROLE_WEIGHTS.get(role, 0.12) for role in role_tags), default=0.08)
    length_score = min(len(tokens(statement)) / 80, 0.18)
    centrality_score = min(centrality * 0.20, 0.20)
    eligibility_penalty = 0.36 if eligibility in INELIGIBLE_CLAIM_ELIGIBILITIES else 0.0
    score = 0.38 + role_score + length_score + centrality_score - eligibility_penalty
    return round(max(0.0, min(1.0, score)), 3)


def claim_certainty(role_tags: tuple[str, ...]) -> str:
    if "source-uncertainty" in role_tags:
        return "uncertain"
    if "negative-evidence" in role_tags:
        return "negative-evidence"
    return "supported"


def eligible_claims(claims: list[SourceClaim] | tuple[SourceClaim, ...]) -> list[SourceClaim]:
    return [claim for claim in claims if claim.claim_eligibility == CLAIM_ELIGIBLE]


def eligible_or_source_fallback_claims(
    claims: list[SourceClaim] | tuple[SourceClaim, ...],
    source_has_eligible_claims: bool,
    prefer_central_eligible_claims: bool,
) -> list[SourceClaim]:
    eligible = eligible_claims(claims)
    central = [claim for claim in eligible if is_central_source_summary_claim(claim)]
    if central:
        return central
    if prefer_central_eligible_claims:
        return []
    if eligible:
        return eligible
    if source_has_eligible_claims:
        return []
    return list(claims)


def unit_source_summary_fallback_claims(claims: list[SourceClaim]) -> list[SourceClaim]:
    if eligible_claims(claims):
        return []
    return [
        claim
        for claim in claims
        if claim.claim_eligibility == "code-fragment" and is_central_source_summary_claim(claim)
    ]


def unit_has_source_summary_coverage_candidate(claims: list[SourceClaim]) -> bool:
    has_central_eligible = any(
        is_central_source_summary_claim(claim) for claim in eligible_claims(claims)
    )
    return has_central_eligible or bool(unit_source_summary_fallback_claims(claims))


def is_central_source_summary_claim(claim: SourceClaim) -> bool:
    return bool(claim.claim_role_tags) or claim.claim_centrality > 0


def source_summary_selection_key(claim: SourceClaim) -> tuple[int, float, float, int]:
    is_eligible = 1 if claim.claim_eligibility == CLAIM_ELIGIBLE else 0
    return (is_eligible, claim.claim_centrality, claim.claim_salience, -len(claim.statement))
