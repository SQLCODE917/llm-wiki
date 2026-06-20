"""Deterministic SourceClaim extraction and source-summary planning."""

from __future__ import annotations

import re

from llmwiki.domain.objects import (
    Evidence,
    ExtractedUnit,
    Schema,
    SourceClaim,
    SourceClaimGroup,
    SourceSummaryPlan,
)
from llmwiki.domain.page_body_contracts import ResolvedPageBodyContract
from llmwiki.domain.pages import slugify
from llmwiki.domain.planning_analysis import tokens, top_terms

_SENTENCE_RE = re.compile(r"(?<=[.!?])\s+")
_MAX_SOURCE_SUMMARY_CLAIMS = 5

_ROLE_PATTERNS: tuple[tuple[str, tuple[str, ...]], ...] = (
    ("uncertainty", (r"\bmay\b", r"\bmight\b", r"\bpossible\b", r"\bsuggest\w*\b", r"\bunknown\b")),
    (
        "negative-evidence",
        (r"\bno\b.+\bfound\b", r"\bnot\b.+\bfound\b", r"\bdoes not\b", r"\bwithout\b"),
    ),
    ("limitation", (r"\blimit\w*\b", r"\bunless\b", r"\bexcept\b", r"\bonly\b")),
    ("method", (r"\bused\b", r"\busing\b", r"\bstudy\b", r"\banalys\w*\b", r"\btest\w*\b")),
    ("evidence", (r"\bevidence\b", r"\binscription\w*\b", r"\bcitation\b", r"\brecord\b")),
    ("provenance", (r"\bfrom\b", r"\borigin\w*\b", r"\bretrieved\b", r"\bdiscovered\b")),
    ("temporal", (r"\b\d{3,4}\b", r"\bbc\b", r"\bad\b", r"\byear\b", r"\bcentur\w*\b")),
    ("quantitative", (r"\b\d+\b", r"\bat least\b", r"\bmore than\b", r"\broughly\b")),
    (
        "function",
        (r"\btrack\w*\b", r"\bpredict\w*\b", r"\badvance\b", r"\bshow\w*\b", r"\bcould\b"),
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

_ROLE_WEIGHTS = {
    "uncertainty": 0.33,
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
}


def source_claims(
    units: tuple[ExtractedUnit, ...],
    schema: Schema,
) -> tuple[SourceClaim, ...]:
    claims: list[SourceClaim] = []
    allowed_roles = {role.tag_name for role in schema.claim_role_tags}
    for unit in units:
        for index, statement in enumerate(_claim_sentences(unit.text), start=1):
            role_tags = tuple(role for role in _claim_role_tags(statement) if role in allowed_roles)
            evidence = Evidence(
                raw_source=unit.raw_source,
                locator=f"{unit.locator} s.{index}".strip(),
                claim=statement,
            )
            claims.append(
                SourceClaim(
                    source_claim_id=f"source-claim-{unit.unit_id}-{index:04d}",
                    statement=statement,
                    evidence=evidence,
                    extracted_unit_id=unit.unit_id,
                    source_span=evidence.locator,
                    claim_role_tags=role_tags,
                    claim_salience=_claim_salience(statement, role_tags),
                    claim_certainty=_claim_certainty(role_tags),
                    subject_terms=top_terms(statement, 4),
                )
            )
    return tuple(claims)


def source_claim_groups(
    claims: tuple[SourceClaim, ...],
) -> tuple[SourceClaimGroup, ...]:
    grouped: dict[str, list[SourceClaim]] = {}
    for claim in claims:
        grouped.setdefault(_primary_claim_group_label(claim), []).append(claim)
    result: list[SourceClaimGroup] = []
    for label, label_claims in grouped.items():
        roles = tuple(sorted({role for claim in label_claims for role in claim.claim_role_tags}))
        units = tuple(dict.fromkeys(claim.extracted_unit_id for claim in label_claims))
        result.append(
            SourceClaimGroup(
                source_claim_group_id=f"source-claim-group-{slugify(label)}",
                label=label,
                source_claims=tuple(claim.source_claim_id for claim in label_claims),
                extracted_units=units,
                claim_role_tags=roles,
                claim_salience=round(max(claim.claim_salience for claim in label_claims), 3),
            )
        )
    return tuple(sorted(result, key=lambda group: (-group.claim_salience, group.label)))


def source_summary_plan(
    *,
    page_id: str,
    contract: ResolvedPageBodyContract,
    claims: tuple[SourceClaim, ...],
    groups: tuple[SourceClaimGroup, ...],
) -> SourceSummaryPlan | None:
    if contract.contract_id != "source-summary" or not claims:
        return None
    claims_by_id = {claim.source_claim_id: claim for claim in claims}
    selected: list[SourceClaim] = []

    def add_role_claim(*roles: str) -> None:
        candidates = [
            claim
            for claim in claims
            if any(role in claim.claim_role_tags for role in roles) and claim not in selected
        ]
        if candidates and len(selected) < _MAX_SOURCE_SUMMARY_CLAIMS:
            selected.append(max(candidates, key=lambda claim: claim.claim_salience))

    add_role_claim("identity", "definition")
    add_role_claim("function", "mechanism", "procedure", "requirement")
    add_role_claim("limitation")
    add_role_claim("negative-evidence")
    add_role_claim("uncertainty", "open-question")

    for group in groups:
        if len(selected) >= _MAX_SOURCE_SUMMARY_CLAIMS:
            break
        if any(claim.source_claim_id in group.source_claims for claim in selected):
            continue
        group_claims = [
            claims_by_id[claim_id] for claim_id in group.source_claims if claim_id in claims_by_id
        ]
        if group_claims:
            selected.append(max(group_claims, key=lambda claim: claim.claim_salience))

    min_claims = min(contract.min_claim_bullets or 3, len(claims))
    for claim in sorted(claims, key=lambda item: -item.claim_salience):
        target_size = max(min_claims, min(_MAX_SOURCE_SUMMARY_CLAIMS, len(claims)))
        if len(selected) >= target_size:
            break
        if claim not in selected:
            selected.append(claim)

    selected_ids = tuple(claim.source_claim_id for claim in selected[:_MAX_SOURCE_SUMMARY_CLAIMS])
    selected_roles = tuple(sorted({role for claim in selected for role in claim.claim_role_tags}))
    selected_groups = tuple(
        group.source_claim_group_id
        for group in groups
        if any(claim_id in group.source_claims for claim_id in selected_ids)
    )
    return SourceSummaryPlan(
        source_summary_plan_id=f"source-summary-plan-{page_id}",
        page_id=page_id,
        selected_source_claims=selected_ids,
        required_claim_role_tags=selected_roles,
        required_source_claim_groups=selected_groups,
        required_source_citations=contract.required_source_citations,
        coverage_policy=contract.coverage_policy,
    )


def _claim_sentences(text: str) -> tuple[str, ...]:
    paragraphs: list[str] = []
    current_lines: list[str] = []
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            if current_lines:
                paragraphs.append(" ".join(current_lines))
                current_lines = []
            continue
        current_lines.append(stripped)
    if current_lines:
        paragraphs.append(" ".join(current_lines))
    sentences: list[str] = []
    for paragraph in paragraphs:
        for sentence in _SENTENCE_RE.split(paragraph):
            normalized = " ".join(sentence.split()).strip()
            if len(tokens(normalized)) >= 3:
                sentences.append(normalized)
    return tuple(sentences)


def _claim_role_tags(statement: str) -> tuple[str, ...]:
    lowered = statement.lower()
    roles = [
        role
        for role, patterns in _ROLE_PATTERNS
        if any(re.search(pattern, lowered) for pattern in patterns)
    ]
    return tuple(dict.fromkeys(roles))


def _claim_salience(statement: str, role_tags: tuple[str, ...]) -> float:
    role_score = max((_ROLE_WEIGHTS.get(role, 0.12) for role in role_tags), default=0.08)
    length_score = min(len(tokens(statement)) / 80, 0.18)
    return round(min(1.0, 0.38 + role_score + length_score), 3)


def _claim_certainty(role_tags: tuple[str, ...]) -> str:
    if "uncertainty" in role_tags:
        return "uncertain"
    if "negative-evidence" in role_tags:
        return "negative-evidence"
    return "supported"


def _primary_claim_group_label(claim: SourceClaim) -> str:
    for role in (
        "uncertainty",
        "negative-evidence",
        "limitation",
        "function",
        "mechanism",
        "method",
        "provenance",
        "identity",
        "temporal",
        "requirement",
        "procedure",
    ):
        if role in claim.claim_role_tags:
            return role
    return claim.subject_terms[0] if claim.subject_terms else "general"
