"""Deterministic SourceClaim extraction and grouping."""

from __future__ import annotations

from llmwiki.domain.objects import (
    Evidence,
    ExtractedUnit,
    Schema,
    SourceClaim,
    SourceClaimGroup,
)
from llmwiki.domain.pages import slugify
from llmwiki.domain.planning_analysis import top_terms
from llmwiki.domain.source_claim_quality import (
    claim_centrality,
    claim_certainty,
    claim_eligibility,
    claim_role_tags,
    claim_salience,
)
from llmwiki.domain.source_claim_sentences import claim_sentences


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
