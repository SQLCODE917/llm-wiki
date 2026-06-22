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
from llmwiki.domain.source_claim_quality import (
    CLAIM_ELIGIBLE,
    claim_centrality,
    claim_certainty,
    claim_eligibility,
    claim_role_tags,
    claim_salience,
    eligible_claims,
    eligible_or_source_fallback_claims,
    is_central_source_summary_claim,
    unit_source_summary_fallback_claims,
)
from llmwiki.domain.source_claim_sentences import claim_sentences
from llmwiki.domain.source_summary import source_summary_claim_requirement

_SKILL_REFERENCE_RE = re.compile(r"\b([a-z][a-z0-9-]*)\s+skills?\b", re.IGNORECASE)
_CLASS_OR_PROFESSION_REFERENCE_RE = re.compile(
    r"\b([a-z][a-z0-9-]*)s?\s+(?:is|are)\s+(?:an?\s+)?(?:[a-z0-9-]+\s+){0,4}"
    r"(?:class|profession)\b",
    re.IGNORECASE,
)
_MAX_SOURCE_SUMMARY_CLAIMS = 5
_EARLY_CLAIM_WINDOW = 20
_TOPIC_FOCUS_GAP = 3
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


def source_claims(
    units: tuple[ExtractedUnit, ...],
    schema: Schema,
) -> tuple[SourceClaim, ...]:
    claims: list[SourceClaim] = []
    allowed_roles = {role.tag_name for role in schema.claim_role_tags}
    for unit in units:
        for index, statement in enumerate(claim_sentences(unit.text), start=1):
            role_tags = tuple(role for role in claim_role_tags(statement) if role in allowed_roles)
            eligibility = claim_eligibility(statement, role_tags)
            centrality = claim_centrality(statement, unit.heading_path)
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
                    claim_salience=claim_salience(statement, role_tags, eligibility, centrality),
                    claim_certainty=claim_certainty(role_tags),
                    subject_terms=top_terms(statement, 4),
                    claim_eligibility=eligibility,
                    claim_centrality=centrality,
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
    page_terms = _page_terms(page_id)
    min_claims = min(contract.min_claim_bullets or 3, len(claims))
    candidate_claims = _topic_focused_claims(page_terms, claims, min_claims)
    candidate_claim_ids = {claim.source_claim_id for claim in candidate_claims}
    claims_by_unit: dict[str, list[SourceClaim]] = {}
    for claim in candidate_claims:
        claims_by_unit.setdefault(claim.extracted_unit_id, []).append(claim)
    source_has_eligible_claims = bool(eligible_claims(candidate_claims))
    source_has_central_eligible_claims = any(
        is_central_source_summary_claim(claim) for claim in eligible_claims(candidate_claims)
    )
    selected: list[SourceClaim] = []
    first_relevant_position = _first_relevant_claim_position(page_terms, candidate_claims)

    unit_ids = tuple(dict.fromkeys(claim.extracted_unit_id for claim in candidate_claims))
    if len(unit_ids) <= _MAX_SOURCE_SUMMARY_CLAIMS:
        for unit_id in unit_ids:
            unit_claims = claims_by_unit.get(unit_id, [])
            candidates = eligible_claims(unit_claims)
            central_candidates = [
                claim for claim in candidates if is_central_source_summary_claim(claim)
            ]
            if central_candidates:
                candidates = central_candidates
            elif source_has_central_eligible_claims:
                candidates = []
            if not candidates:
                candidates = unit_source_summary_fallback_claims(unit_claims)
            if not candidates and not source_has_eligible_claims:
                candidates = unit_claims
            if candidates and len(selected) < _MAX_SOURCE_SUMMARY_CLAIMS:
                selected.append(
                    max(candidates, key=lambda claim: _selection_score(page_terms, claim))
                )

    def has_unselected_relevant_claims() -> bool:
        return any(
            claim not in selected and _page_overlap(page_terms, claim) > 0
            for claim in candidate_claims
        )

    def add_role_claim(*roles: str) -> None:
        candidates = [
            claim
            for claim in candidate_claims
            if any(role in claim.claim_role_tags for role in roles) and claim not in selected
        ]
        candidates = _without_competing_section_claims(page_terms, candidates)
        relevant_candidates = [
            claim for claim in candidates if _page_overlap(page_terms, claim) > 0
        ]
        if relevant_candidates:
            candidates = relevant_candidates
        elif page_terms:
            if has_unselected_relevant_claims():
                return
            early_candidates = [
                claim
                for claim in candidates
                if _claim_position(claim) <= _EARLY_CLAIM_WINDOW
                and _after_first_relevant_claim(first_relevant_position, claim)
            ]
            if not early_candidates:
                return
            candidates = early_candidates
        candidates = eligible_or_source_fallback_claims(
            candidates,
            source_has_eligible_claims,
            source_has_central_eligible_claims,
        )
        if candidates and len(selected) < _MAX_SOURCE_SUMMARY_CLAIMS:
            selected.append(max(candidates, key=lambda claim: _selection_score(page_terms, claim)))

    add_role_claim("identity", "definition")
    add_role_claim("function", "mechanism", "procedure", "requirement")
    add_role_claim("limitation")
    add_role_claim("negative-evidence")
    add_role_claim("source-uncertainty", "open-question")

    for group in groups:
        if len(selected) >= _MAX_SOURCE_SUMMARY_CLAIMS:
            break
        if any(claim.source_claim_id in group.source_claims for claim in selected):
            continue
        group_claims = [
            claims_by_id[claim_id]
            for claim_id in group.source_claims
            if claim_id in claims_by_id and claim_id in candidate_claim_ids
        ]
        group_claims = _without_competing_section_claims(page_terms, group_claims)
        if group_claims:
            relevant_group_claims = [
                claim for claim in group_claims if _page_overlap(page_terms, claim) > 0
            ]
            if relevant_group_claims:
                group_claims = relevant_group_claims
            elif page_terms:
                if has_unselected_relevant_claims():
                    continue
                if len(selected) >= min_claims:
                    continue
                early_group_claims = [
                    claim
                    for claim in group_claims
                    if _claim_position(claim) <= _EARLY_CLAIM_WINDOW
                    and _after_first_relevant_claim(first_relevant_position, claim)
                ]
                if not early_group_claims:
                    continue
                group_claims = early_group_claims
            candidates = eligible_or_source_fallback_claims(
                group_claims,
                source_has_eligible_claims,
                source_has_central_eligible_claims,
            )
            if candidates:
                selected.append(
                    max(candidates, key=lambda claim: _selection_score(page_terms, claim))
                )

    for claim in sorted(
        _without_competing_section_claims(page_terms, list(candidate_claims)),
        key=lambda claim: _selection_score(page_terms, claim),
        reverse=True,
    ):
        target_size = max(min_claims, min(_MAX_SOURCE_SUMMARY_CLAIMS, len(candidate_claims)))
        if len(selected) >= target_size:
            break
        if page_terms and len(selected) >= min_claims and _page_overlap(page_terms, claim) == 0:
            continue
        if (
            page_terms
            and _page_overlap(page_terms, claim) == 0
            and has_unselected_relevant_claims()
        ):
            continue
        if claim not in selected:
            if claim.claim_eligibility != CLAIM_ELIGIBLE and source_has_eligible_claims:
                continue
            if (
                claim.claim_eligibility == CLAIM_ELIGIBLE
                and source_has_central_eligible_claims
                and not is_central_source_summary_claim(claim)
            ):
                continue
            selected.append(claim)

    selected_ids = tuple(claim.source_claim_id for claim in selected[:_MAX_SOURCE_SUMMARY_CLAIMS])
    selected_requirements = tuple(
        source_summary_claim_requirement(claim)
        for claim in selected[:_MAX_SOURCE_SUMMARY_CLAIMS]
    )
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
        selected_claim_requirements=selected_requirements,
        required_claim_role_tags=selected_roles,
        required_source_claim_groups=selected_groups,
        required_source_citations=contract.required_source_citations,
        coverage_policy=contract.coverage_policy,
    )


def _selection_score(page_terms: frozenset[str], claim: SourceClaim) -> float:
    relevance = min(_page_overlap(page_terms, claim) * 0.12, 0.36)
    eligibility_bonus = 0.20 if claim.claim_eligibility == CLAIM_ELIGIBLE else -0.20
    centrality_bonus = min(claim.claim_centrality * 0.15, 0.15)
    return (
        claim.claim_salience
        + relevance
        + eligibility_bonus
        + centrality_bonus
        - min(_claim_position(claim) * 0.008, 0.65)
    )


def _page_overlap(page_terms: frozenset[str], claim: SourceClaim) -> int:
    if not page_terms:
        return 0
    claim_terms = _term_variants(tuple(tokens(claim.statement)))
    specific_page_terms = page_terms - _GENERIC_PAGE_MATCH_TERMS
    specific_overlap = specific_page_terms & claim_terms
    if specific_overlap:
        return len(specific_overlap)
    if specific_page_terms:
        return 0
    return len(page_terms & claim_terms)


def _topic_focused_claims(
    page_terms: frozenset[str],
    claims: tuple[SourceClaim, ...],
    min_claims: int,
) -> tuple[SourceClaim, ...]:
    if not page_terms or len(claims) <= _EARLY_CLAIM_WINDOW:
        return claims
    start_index = next(
        (index for index, claim in enumerate(claims) if _page_overlap(page_terms, claim) > 0),
        None,
    )
    if start_index is None:
        return claims
    focused: list[SourceClaim] = []
    gap = 0
    for claim in claims[start_index:]:
        if _page_overlap(page_terms, claim) > 0:
            gap = 0
        else:
            gap += 1
            if gap > _TOPIC_FOCUS_GAP:
                break
        focused.append(claim)
    if len(focused) < min_claims:
        return claims
    return tuple(focused)


def _first_relevant_claim_position(
    page_terms: frozenset[str],
    claims: tuple[SourceClaim, ...],
) -> int:
    positions = tuple(
        _claim_position(claim) for claim in claims if _page_overlap(page_terms, claim)
    )
    return min(positions) if positions else 0


def _after_first_relevant_claim(first_relevant_position: int, claim: SourceClaim) -> bool:
    return not first_relevant_position or _claim_position(claim) >= first_relevant_position


def _without_competing_section_claims(
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


def _page_terms(page_id: str) -> frozenset[str]:
    parts = page_id.split("-")
    for index in range(len(parts) - 1):
        if parts[index].isdigit() and parts[index + 1].isdigit():
            return _specific_page_terms(_page_title_tokens(tuple(parts[index + 2 :])))
    return _specific_page_terms(_page_title_tokens(tuple(parts)))


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


def _claim_position(claim: SourceClaim) -> int:
    match = re.search(r"-(\d{4})$", claim.source_claim_id)
    if match is None:
        return 0
    return int(match.group(1))


def _primary_claim_group_label(claim: SourceClaim) -> str:
    for role in (
        "source-uncertainty",
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
