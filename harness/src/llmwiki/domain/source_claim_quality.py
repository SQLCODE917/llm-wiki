"""Deterministic source-claim quality classification and reports."""

from __future__ import annotations

import re

from llmwiki.domain.objects import SourceClaim
from llmwiki.domain.planning_analysis import tokens
from llmwiki.domain.source_claim_heuristics import (
    is_code_fragment,
    is_narrative_frame,
    is_rhetorical_example,
    is_source_furniture,
)

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
SOURCE_FRAMING_PREFIXES = (
    "the source discusses",
    "the source describes",
    "the source mentions",
    "the source notes",
    "the source lists",
    "the source provides",
    "this source discusses",
    "this source describes",
    "the text discusses",
    "the text describes",
    "the text mentions",
    "the text notes",
    "the section discusses",
    "the section describes",
    "the book discusses",
    "the book describes",
)

_ROLE_PATTERNS: tuple[tuple[str, tuple[str, ...]], ...] = (
    (
        "source-uncertainty",
        (
            r"\bdoes not\b.+\b(specify|state|identify|confirm|establish|explain|include)\b",
            r"\bnot\b.+\b(specified|stated|identified|confirmed|established|known|resolved)\b",
            r"\bnot fully confirm\b",
            r"\bnot confirmed\b",
            r"\bnot ingested\b",
            r"\bunknown\b",
            r"\bunclear\b",
            r"\bunresolved\b",
            r"\bunconfirmed\b",
            r"\bopen question\b",
            r"\[verify\]",
        ),
    ),
    (
        "ordinary-modality",
        (
            r"\bmay\b",
            r"\bmight\b",
            r"\bpossibly\b",
            r"\bpossible\b",
            r"\bcould\b",
            r"\bshould\b",
            r"\bsuggest\w*\b",
            r"\bmore to\b",
        ),
    ),
    (
        "source-framing",
        tuple(rf"\b{re.escape(prefix)}\b" for prefix in SOURCE_FRAMING_PREFIXES)
        + (
            r"\bwhen discussing\b",
            r"\btakes(?: \w+)? delight in explaining\b",
            r"\bthis is exactly how\b.+\bworks\b",
        ),
    ),
    (
        "analogy",
        (
            r"\banalogy\b",
            r"\bmetaphor\b",
            r"\bsimilar to\b",
            r"\bakin to\b",
            r"\bas if\b",
            r"\blike a\b",
            r"\blike an\b",
            r"\blike most\b",
            r"\bcompared to\b",
            r"\bjust as\b",
            r"\bmuch like\b",
        ),
    ),
    ("worked-example", (r"\bfor example\b", r"\bexample\b", r"\bsuppose\b", r"\bconsider\b")),
    (
        "negative-evidence",
        (r"\bno\b.+\bfound\b", r"\bnot\b.+\bfound\b", r"\bdoes not\b", r"\bwithout\b"),
    ),
    ("limitation", (r"\blimit\w*\b", r"\bunless\b", r"\bexcept\b", r"\bonly\b", r"\bcannot\b")),
    (
        "method",
        (
            r"\bused\b",
            r"\busing\b",
            r"\bstudy\b",
            r"\banalys\w*\b",
            r"\btest\w*\b",
            r"\bexplor\w*\b",
        ),
    ),
    ("evidence", (r"\bevidence\b", r"\binscription\w*\b", r"\bcitation\b", r"\brecord\b")),
    ("provenance", (r"\bfrom\b", r"\borigin\w*\b", r"\bretrieved\b", r"\bdiscovered\b")),
    ("temporal", (r"\b\d{3,4}\b", r"\bbc\b", r"\bad\b", r"\byear\b", r"\bcentur\w*\b")),
    ("quantitative", (r"\b\d+\b", r"\bat least\b", r"\bmore than\b", r"\broughly\b")),
    (
        "function",
        (
            r"\btrack\w*\b",
            r"\bpredict\w*\b",
            r"\badvance\b",
            r"\bshow\w*\b",
            r"\brepresent\w*\b",
            r"\bencode\w*\b",
            r"\breturn\w*\b",
            r"\bcombine\w*\b",
            r"\bcall\w*\b",
            r"\btransform\w*\b",
        ),
    ),
    ("mechanism", (r"\bconsists\b", r"\bgear\w*\b", r"\bcase\b", r"\bcrank\b", r"\bthrough\b")),
    ("comparison", (r"\bmatched\b", r"\bsurpass\w*\b", r"\bcompared\b", r"\bthan\b")),
    ("relationship", (r"\blink\w*\b", r"\bconnect\w*\b", r"\bbetween\b", r"\bwith\b")),
    ("requirement", (r"\bmust\b", r"\brequire\w*\b", r"\bshall\b", r"\bshould\b")),
    ("procedure", (r"\bturn\w*\b", r"\bstep\b", r"\bprocess\b", r"\bworkflow\b")),
    ("definition", (r"\bdefined as\b", r"\bmeans\b", r"\brefers to\b")),
    ("identity", (r"\bis\b", r"\bare\b", r"\bknown as\b", r"\bdescribed as\b")),
    ("attribute", (r"\bhas\b", r"\bhave\b", r"\bcontains\b", r"\bhoused\b", r"\bsize\b")),
    ("open-question", (r"\bopen question\b", r"\bunclear\b", r"\bunresolved\b")),
)
_ROLE_SCAN_CHAR_LIMIT = 4096
_ROLE_REGEXES = tuple(
    (role, tuple(re.compile(pattern) for pattern in patterns))
    for role, patterns in _ROLE_PATTERNS
)

_ROLE_WEIGHTS = {
    "source-uncertainty": 0.30,
    "ordinary-modality": 0.08,
    "negative-evidence": 0.34,
    "limitation": 0.31,
    "method": 0.27,
    "function": 0.30,
    "mechanism": 0.25,
    "provenance": 0.22,
    "temporal": 0.18,
    "identity": 0.22,
    "definition": 0.22,
    "comparison": 0.20,
    "evidence": 0.20,
    "quantitative": 0.16,
    "analogy": 0.05,
    "worked-example": 0.10,
    "source-framing": 0.03,
}


def claim_role_tags(statement: str) -> tuple[str, ...]:
    lowered = statement.lower()[:_ROLE_SCAN_CHAR_LIMIT]
    return tuple(
        dict.fromkeys(
            role
            for role, patterns in _ROLE_REGEXES
            if any(pattern.search(lowered) for pattern in patterns)
        )
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
    role_score = max((_ROLE_WEIGHTS.get(role, 0.12) for role in role_tags), default=0.08)
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
