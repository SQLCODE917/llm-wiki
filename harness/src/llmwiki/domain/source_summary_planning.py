"""Deterministic source-summary planning from extracted SourceClaims."""

from __future__ import annotations

from llmwiki.domain.objects import SourceClaim, SourceClaimGroup, SourceSummaryPlan
from llmwiki.domain.page_body_contracts import ResolvedPageBodyContract
from llmwiki.domain.source_claim_quality import (
    CLAIM_ELIGIBLE,
    eligible_claims,
    eligible_or_source_fallback_claims,
    is_central_source_summary_claim,
    unit_source_summary_fallback_claims,
)
from llmwiki.domain.source_summary import source_summary_claim_requirement
from llmwiki.domain.source_summary_relevance import (
    EARLY_CLAIM_WINDOW,
    after_first_relevant_claim,
    claim_position,
    first_relevant_claim_position,
    page_overlap,
    page_terms,
    selection_score,
    topic_focused_claims,
    without_competing_section_claims,
)

MAX_SOURCE_SUMMARY_CLAIMS = 5


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
    terms = page_terms(page_id)
    min_claims = min(contract.min_claim_bullets or 3, len(claims))
    candidate_claims = topic_focused_claims(terms, claims, min_claims)
    candidate_claims = _prefer_summary_worthy_claims(candidate_claims, min_claims)
    candidate_claim_ids = {claim.source_claim_id for claim in candidate_claims}
    claims_by_unit: dict[str, list[SourceClaim]] = {}
    for claim in candidate_claims:
        claims_by_unit.setdefault(claim.extracted_unit_id, []).append(claim)
    source_has_eligible_claims = bool(eligible_claims(candidate_claims))
    central_eligible_claims = [
        claim
        for claim in eligible_claims(candidate_claims)
        if is_central_source_summary_claim(claim)
    ]
    prefer_central_eligible_claims = len(central_eligible_claims) >= min_claims
    selected: list[SourceClaim] = []
    first_relevant_position = first_relevant_claim_position(terms, candidate_claims)

    _select_unit_coverage_claims(
        terms,
        claims_by_unit,
        source_has_eligible_claims,
        prefer_central_eligible_claims,
        selected,
    )
    _select_role_claims(
        terms,
        candidate_claims,
        source_has_eligible_claims,
        prefer_central_eligible_claims,
        first_relevant_position,
        selected,
    )
    _select_group_claims(
        terms,
        groups,
        claims_by_id,
        candidate_claim_ids,
        source_has_eligible_claims,
        prefer_central_eligible_claims,
        min_claims,
        first_relevant_position,
        selected,
        candidate_claims,
    )
    _fill_remaining_claims(
        terms,
        candidate_claims,
        source_has_eligible_claims,
        prefer_central_eligible_claims,
        min_claims,
        selected,
    )

    selected_ids = tuple(
        claim.source_claim_id for claim in selected[:MAX_SOURCE_SUMMARY_CLAIMS]
    )
    selected_requirements = tuple(
        source_summary_claim_requirement(claim)
        for claim in selected[:MAX_SOURCE_SUMMARY_CLAIMS]
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


def _select_unit_coverage_claims(
    terms: frozenset[str],
    claims_by_unit: dict[str, list[SourceClaim]],
    source_has_eligible_claims: bool,
    prefer_central_eligible_claims: bool,
    selected: list[SourceClaim],
) -> None:
    unit_ids = tuple(claims_by_unit)
    if len(unit_ids) > MAX_SOURCE_SUMMARY_CLAIMS:
        return
    for unit_id in unit_ids:
        unit_claims = claims_by_unit.get(unit_id, [])
        candidates = eligible_claims(unit_claims)
        central_candidates = [
            claim for claim in candidates if is_central_source_summary_claim(claim)
        ]
        if central_candidates:
            candidates = central_candidates
        elif prefer_central_eligible_claims:
            candidates = []
        if not candidates:
            candidates = unit_source_summary_fallback_claims(unit_claims)
        if not candidates and not source_has_eligible_claims:
            candidates = unit_claims
        if candidates and len(selected) < MAX_SOURCE_SUMMARY_CLAIMS:
            selected.append(max(candidates, key=lambda claim: selection_score(terms, claim)))


def _prefer_summary_worthy_claims(
    claims: tuple[SourceClaim, ...], min_claims: int
) -> tuple[SourceClaim, ...]:
    preferred = tuple(claim for claim in claims if not _is_low_summary_value_claim(claim))
    if len(preferred) < min_claims:
        return claims
    if len(eligible_claims(preferred)) < min(min_claims, len(eligible_claims(claims))):
        return claims
    return preferred


def _is_low_summary_value_claim(claim: SourceClaim) -> bool:
    if claim.claim_centrality > 0:
        return False
    lowered = claim.statement.lower()
    if lowered.startswith("therefore,") or " will best " in lowered:
        return True
    roles = set(claim.claim_role_tags)
    if "worked-example" in roles:
        return True
    return bool(roles) and roles <= {"relationship"}


def _select_role_claims(
    terms: frozenset[str],
    candidate_claims: tuple[SourceClaim, ...],
    source_has_eligible_claims: bool,
    prefer_central_eligible_claims: bool,
    first_relevant_position: int,
    selected: list[SourceClaim],
) -> None:
    def add_role_claim(*roles: str) -> None:
        selected_ids = _selected_claim_ids(selected)
        candidates = [
            claim
            for claim in candidate_claims
            if any(role in claim.claim_role_tags for role in roles)
            and claim.source_claim_id not in selected_ids
        ]
        candidates = without_competing_section_claims(terms, candidates)
        relevant_candidates = [claim for claim in candidates if page_overlap(terms, claim) > 0]
        if relevant_candidates:
            candidates = relevant_candidates
        elif terms:
            if _has_unselected_relevant_claims(
                terms, candidate_claims, source_has_eligible_claims, selected
            ):
                return
            early_candidates = [
                claim
                for claim in candidates
                if claim_position(claim) <= EARLY_CLAIM_WINDOW
                and after_first_relevant_claim(first_relevant_position, claim)
            ]
            if not early_candidates:
                return
            candidates = early_candidates
        candidates = eligible_or_source_fallback_claims(
            candidates,
            source_has_eligible_claims,
            prefer_central_eligible_claims,
        )
        if candidates and len(selected) < MAX_SOURCE_SUMMARY_CLAIMS:
            selected.append(max(candidates, key=lambda claim: selection_score(terms, claim)))

    add_role_claim("identity", "definition")
    add_role_claim("function", "mechanism", "procedure", "requirement")
    add_role_claim("limitation")
    add_role_claim("negative-evidence")
    add_role_claim("source-uncertainty", "open-question")


def _select_group_claims(
    terms: frozenset[str],
    groups: tuple[SourceClaimGroup, ...],
    claims_by_id: dict[str, SourceClaim],
    candidate_claim_ids: set[str],
    source_has_eligible_claims: bool,
    prefer_central_eligible_claims: bool,
    min_claims: int,
    first_relevant_position: int,
    selected: list[SourceClaim],
    candidate_claims: tuple[SourceClaim, ...],
) -> None:
    for group in groups:
        if len(selected) >= MAX_SOURCE_SUMMARY_CLAIMS:
            break
        if any(claim.source_claim_id in group.source_claims for claim in selected):
            continue
        group_claims = [
            claims_by_id[claim_id]
            for claim_id in group.source_claims
            if claim_id in claims_by_id and claim_id in candidate_claim_ids
        ]
        group_claims = without_competing_section_claims(terms, group_claims)
        if not group_claims:
            continue
        relevant_group_claims = [claim for claim in group_claims if page_overlap(terms, claim) > 0]
        if relevant_group_claims:
            group_claims = relevant_group_claims
        elif terms:
            if _has_unselected_relevant_claims(
                terms, candidate_claims, source_has_eligible_claims, selected
            ):
                continue
            if len(selected) >= min_claims:
                continue
            early_group_claims = [
                claim
                for claim in group_claims
                if claim_position(claim) <= EARLY_CLAIM_WINDOW
                and after_first_relevant_claim(first_relevant_position, claim)
            ]
            if not early_group_claims:
                continue
            group_claims = early_group_claims
        candidates = eligible_or_source_fallback_claims(
            group_claims,
            source_has_eligible_claims,
            prefer_central_eligible_claims,
        )
        if candidates:
            selected.append(max(candidates, key=lambda claim: selection_score(terms, claim)))


def _fill_remaining_claims(
    terms: frozenset[str],
    candidate_claims: tuple[SourceClaim, ...],
    source_has_eligible_claims: bool,
    prefer_central_eligible_claims: bool,
    min_claims: int,
    selected: list[SourceClaim],
) -> None:
    for claim in sorted(
        without_competing_section_claims(terms, list(candidate_claims)),
        key=lambda claim: selection_score(terms, claim),
        reverse=True,
    ):
        target_size = max(min_claims, min(MAX_SOURCE_SUMMARY_CLAIMS, len(candidate_claims)))
        if len(selected) >= target_size:
            break
        if terms and len(selected) >= min_claims and page_overlap(terms, claim) == 0:
            continue
        if (
            terms
            and page_overlap(terms, claim) == 0
            and _has_unselected_relevant_claims(
                terms, candidate_claims, source_has_eligible_claims, selected
            )
        ):
            continue
        if claim.source_claim_id in _selected_claim_ids(selected):
            continue
        if claim.claim_eligibility != CLAIM_ELIGIBLE and source_has_eligible_claims:
            continue
        if (
            claim.claim_eligibility == CLAIM_ELIGIBLE
            and prefer_central_eligible_claims
            and not is_central_source_summary_claim(claim)
        ):
            continue
        selected.append(claim)


def _has_unselected_relevant_claims(
    terms: frozenset[str],
    candidate_claims: tuple[SourceClaim, ...],
    source_has_eligible_claims: bool,
    selected: list[SourceClaim],
) -> bool:
    selected_ids = _selected_claim_ids(selected)
    return any(
        claim.source_claim_id not in selected_ids
        and page_overlap(terms, claim) > 0
        and (claim.claim_eligibility == CLAIM_ELIGIBLE or not source_has_eligible_claims)
        for claim in candidate_claims
    )


def _selected_claim_ids(selected: list[SourceClaim]) -> frozenset[str]:
    return frozenset(claim.source_claim_id for claim in selected)
