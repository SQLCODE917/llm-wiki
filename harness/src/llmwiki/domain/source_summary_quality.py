"""Deterministic source-summary quality reporting."""

from __future__ import annotations

from llmwiki.domain.objects import PagePlan, SourceClaim, SourceSummaryQualityReport
from llmwiki.domain.source_claim_quality import (
    CLAIM_ELIGIBLE,
    SOURCE_FRAMING_PREFIXES,
    eligible_claims,
    unit_has_source_summary_coverage_candidate,
)


def source_summary_quality_report(
    plan: PagePlan, wiki_pages: dict[str, str] | None = None
) -> SourceSummaryQualityReport:
    claims_by_id = {claim.source_claim_id: claim for claim in plan.source_claims}
    claims_by_unit: dict[str, list[SourceClaim]] = {}
    for claim in plan.source_claims:
        claims_by_unit.setdefault(claim.extracted_unit_id, []).append(claim)

    selected_ineligible: list[str] = []
    false_uncertainty: list[str] = []
    missing_unit_coverage: list[str] = []

    for write in plan.planned_writes:
        summary_plan = write.source_summary_plan
        if summary_plan is None:
            continue
        selected = tuple(
            claims_by_id[claim_id]
            for claim_id in summary_plan.selected_source_claims
            if claim_id in claims_by_id
        )
        selected_unit_ids = {claim.extracted_unit_id for claim in selected}
        for claim in selected:
            unit_claims = claims_by_unit.get(claim.extracted_unit_id, [])
            if claim.claim_eligibility != CLAIM_ELIGIBLE and eligible_claims(unit_claims):
                selected_ineligible.append(
                    f"{write.page_metadata.page_id}: {claim.source_claim_id} "
                    f"{claim.claim_eligibility}"
                )
            if (
                claim.claim_certainty == "uncertain"
                and "source-uncertainty" not in claim.claim_role_tags
            ):
                false_uncertainty.append(f"{write.page_metadata.page_id}: {claim.source_claim_id}")
        if len(write.extracted_units) <= 5:
            for unit_id in write.extracted_units:
                unit_claims = claims_by_unit.get(unit_id, [])
                if (
                    unit_has_source_summary_coverage_candidate(unit_claims)
                    and unit_id not in selected_unit_ids
                ):
                    missing_unit_coverage.append(f"{write.page_metadata.page_id}: {unit_id}")

    framing_examples = source_framing_bullet_examples(wiki_pages or {})
    return SourceSummaryQualityReport(
        selected_ineligible_claims=len(selected_ineligible),
        false_source_uncertainty_claims=len(false_uncertainty),
        source_framing_bullets=len(framing_examples),
        missing_unit_coverage=len(missing_unit_coverage),
        selected_ineligible_examples=tuple(selected_ineligible[:10]),
        false_source_uncertainty_examples=tuple(false_uncertainty[:10]),
        source_framing_examples=tuple(framing_examples[:10]),
        missing_unit_coverage_examples=tuple(missing_unit_coverage[:10]),
    )


def source_framing_bullet_examples(wiki_pages: dict[str, str]) -> tuple[str, ...]:
    examples: list[str] = []
    for page_id, page_text in wiki_pages.items():
        for line in page_text.splitlines():
            stripped = line.strip()
            if not stripped.startswith(("-", "*")):
                continue
            bullet_text = stripped[1:].strip().lower()
            if any(bullet_text.startswith(prefix) for prefix in SOURCE_FRAMING_PREFIXES):
                examples.append(f"{page_id}: {stripped}")
    return tuple(examples)
