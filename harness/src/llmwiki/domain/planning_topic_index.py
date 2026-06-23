"""Indexes for topic-cluster planning lookups."""

from __future__ import annotations

from llmwiki.domain.objects import CandidateClaim, ExtractedUnit, SourceClaimGroup


def candidate_claim_ids_by_unit(
    units: tuple[ExtractedUnit, ...], claims: tuple[CandidateClaim, ...]
) -> dict[str, tuple[str, ...]]:
    claim_ids: dict[str, list[str]] = {unit.unit_id: [] for unit in units}
    for claim in claims:
        for unit_id in claim_ids:
            if claim.claim_id.startswith(f"claim-{unit_id}-"):
                claim_ids[unit_id].append(claim.claim_id)
                break
    return {unit_id: tuple(items) for unit_id, items in claim_ids.items()}


def source_claim_group_ids_by_unit(
    groups: tuple[SourceClaimGroup, ...],
) -> dict[str, tuple[str, ...]]:
    group_ids: dict[str, list[str]] = {}
    for group in groups:
        for unit_id in group.extracted_units:
            group_ids.setdefault(unit_id, []).append(group.source_claim_group_id)
    return {unit_id: tuple(items) for unit_id, items in group_ids.items()}
