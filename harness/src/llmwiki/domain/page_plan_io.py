"""Explicit PagePlan JSON payloads without recursive dataclass copying."""

from __future__ import annotations

import json
from functools import lru_cache
from typing import Any

from llmwiki.domain.objects import (
    CandidateClaim,
    CandidateEntity,
    CandidateTopic,
    ClaimComparison,
    Evidence,
    ExtractedUnit,
    PagePlan,
    PlannedPageWrite,
    ProjectionMetadata,
    RawSource,
    SourceBundle,
    SourceClaim,
    SourceClaimGroup,
    SourcePageGroup,
    SourceSummaryClaimRequirement,
    SourceSummaryPlan,
    TopicCluster,
    WikiMatch,
)
from llmwiki.domain.page_body_contracts import ResolvedPageBodyContract
from llmwiki.domain.pages import PageMetadata


def page_plan_to_json_text(plan: PagePlan) -> str:
    return json.dumps(_page_plan_payload(plan), indent=2, ensure_ascii=False, sort_keys=True)


def _page_plan_payload(plan: PagePlan) -> dict[str, Any]:
    return {
        "plan_id": plan.plan_id,
        "source_bundle": _source_bundle_payload(plan.source_bundle),
        "extracted_units": [_extracted_unit_payload(unit) for unit in plan.extracted_units],
        "source_claims": [_source_claim_payload(claim) for claim in plan.source_claims],
        "source_claim_groups": [
            _source_claim_group_payload(group) for group in plan.source_claim_groups
        ],
        "candidate_claims": [_candidate_claim_payload(claim) for claim in plan.candidate_claims],
        "candidate_topics": [_candidate_topic_payload(topic) for topic in plan.candidate_topics],
        "candidate_entities": [
            _candidate_entity_payload(entity) for entity in plan.candidate_entities
        ],
        "topic_clusters": [_topic_cluster_payload(cluster) for cluster in plan.topic_clusters],
        "wiki_matches": [_wiki_match_payload(match) for match in plan.wiki_matches],
        "claim_comparisons": [
            _claim_comparison_payload(comparison) for comparison in plan.claim_comparisons
        ],
        "planned_writes": [_planned_write_payload(write) for write in plan.planned_writes],
        "source_page_groups": [
            _source_page_group_payload(group) for group in plan.source_page_groups
        ],
    }


def _raw_source_payload(source: RawSource) -> dict[str, Any]:
    return _raw_source_payload_cached(
        source.source_locator,
        source.source_format,
        source.source_content,
        source.source_assets,
        source.immutable,
    )


@lru_cache(maxsize=128)
def _raw_source_payload_cached(
    source_locator: str,
    source_format: str,
    source_content: str,
    source_assets: tuple[str, ...],
    immutable: bool,
) -> dict[str, Any]:
    return {
        "source_locator": source_locator,
        "source_format": source_format,
        "source_content": source_content,
        "source_assets": list(source_assets),
        "immutable": immutable,
    }


def _source_bundle_payload(bundle: SourceBundle) -> dict[str, Any]:
    return {"raw_sources": [_raw_source_payload(source) for source in bundle.raw_sources]}


def _evidence_payload(evidence: Evidence) -> dict[str, Any]:
    return {
        "raw_source": _raw_source_payload(evidence.raw_source),
        "locator": evidence.locator,
        "page_id": evidence.page_id,
        "claim": evidence.claim,
    }


def _extracted_unit_payload(unit: ExtractedUnit) -> dict[str, Any]:
    return {
        "unit_id": unit.unit_id,
        "raw_source": _raw_source_payload(unit.raw_source),
        "locator": unit.locator,
        "heading_path": unit.heading_path,
        "text": unit.text,
        "extraction_status": unit.extraction_status,
        "source_hash": unit.source_hash,
    }


def _source_claim_payload(claim: SourceClaim) -> dict[str, Any]:
    return {
        "source_claim_id": claim.source_claim_id,
        "statement": claim.statement,
        "evidence": _evidence_payload(claim.evidence),
        "extracted_unit_id": claim.extracted_unit_id,
        "source_span": claim.source_span,
        "claim_role_tags": list(claim.claim_role_tags),
        "claim_salience": claim.claim_salience,
        "claim_certainty": claim.claim_certainty,
        "subject_terms": list(claim.subject_terms),
        "claim_eligibility": claim.claim_eligibility,
        "claim_centrality": claim.claim_centrality,
    }


def _source_claim_group_payload(group: SourceClaimGroup) -> dict[str, Any]:
    return {
        "source_claim_group_id": group.source_claim_group_id,
        "label": group.label,
        "source_claims": list(group.source_claims),
        "extracted_units": list(group.extracted_units),
        "claim_role_tags": list(group.claim_role_tags),
        "claim_salience": group.claim_salience,
    }


def _candidate_claim_payload(claim: CandidateClaim) -> dict[str, Any]:
    return {
        "claim_id": claim.claim_id,
        "statement": claim.statement,
        "evidence": _evidence_payload(claim.evidence),
        "confidence": claim.confidence,
    }


def _candidate_topic_payload(topic: CandidateTopic) -> dict[str, Any]:
    return {
        "topic_id": topic.topic_id,
        "label": topic.label,
        "candidate_claims": list(topic.candidate_claims),
    }


def _candidate_entity_payload(entity: CandidateEntity) -> dict[str, Any]:
    return {
        "entity_id": entity.entity_id,
        "label": entity.label,
        "candidate_claims": list(entity.candidate_claims),
    }


def _topic_cluster_payload(cluster: TopicCluster) -> dict[str, Any]:
    return {
        "cluster_id": cluster.cluster_id,
        "label": cluster.label,
        "extracted_units": list(cluster.extracted_units),
        "candidate_claims": list(cluster.candidate_claims),
        "candidate_topics": list(cluster.candidate_topics),
        "candidate_entities": list(cluster.candidate_entities),
        "source_claim_groups": list(cluster.source_claim_groups),
    }


def _wiki_match_payload(match: WikiMatch) -> dict[str, Any]:
    return {
        "page_id": match.page_id,
        "score": match.score,
        "match_reason": match.match_reason,
        "page_excerpt": match.page_excerpt,
    }


def _claim_comparison_payload(comparison: ClaimComparison) -> dict[str, Any]:
    return {
        "candidate_claim": comparison.candidate_claim,
        "existing_claim": comparison.existing_claim,
        "relation": comparison.relation,
        "page_id": comparison.page_id,
    }


def _page_metadata_payload(metadata: PageMetadata) -> dict[str, Any]:
    return {
        "page_id": metadata.page_id,
        "page_kind": metadata.page_kind,
        "summary": metadata.summary,
        "sources": list(metadata.sources),
        "updated": metadata.updated,
        "domain": metadata.domain,
        "category_path": metadata.category_path,
        "project_id": metadata.project_id,
        "source_id": metadata.source_id,
        "tags": list(metadata.tags),
        "aliases": list(metadata.aliases),
    }


def _projection_payload(projection: ProjectionMetadata | None) -> dict[str, Any] | None:
    if projection is None:
        return None
    return {
        "page_metadata": _page_metadata_payload(projection.page_metadata),
        "page_path": projection.page_path,
    }


def _resolved_contract_payload(contract: ResolvedPageBodyContract) -> dict[str, Any]:
    return {
        "contract_id": contract.contract_id,
        "required_sections": list(contract.required_sections),
        "required_markdown_shape": contract.required_markdown_shape,
        "min_claim_bullets": contract.min_claim_bullets,
        "max_claim_bullets": contract.max_claim_bullets,
        "coverage_policy": contract.coverage_policy,
        "max_words": contract.max_words,
        "max_source_word_ratio": contract.max_source_word_ratio,
        "max_copied_ngram_ratio": contract.max_copied_ngram_ratio,
        "required_link_page_ids": list(contract.required_link_page_ids),
        "required_source_citations": list(contract.required_source_citations),
        "required_uncertainty_terms": list(contract.required_uncertainty_terms),
    }


def _source_summary_requirement_payload(
    requirement: SourceSummaryClaimRequirement,
) -> dict[str, Any]:
    return {
        "source_claim_id": requirement.source_claim_id,
        "claim_role_tags": list(requirement.claim_role_tags),
        "claim_eligibility": requirement.claim_eligibility,
        "claim_centrality": requirement.claim_centrality,
        "cue_terms": list(requirement.cue_terms),
    }


def _source_summary_plan_payload(plan: SourceSummaryPlan | None) -> dict[str, Any] | None:
    if plan is None:
        return None
    return {
        "source_summary_plan_id": plan.source_summary_plan_id,
        "page_id": plan.page_id,
        "selected_source_claims": list(plan.selected_source_claims),
        "selected_claim_requirements": [
            _source_summary_requirement_payload(requirement)
            for requirement in plan.selected_claim_requirements
        ],
        "required_claim_role_tags": list(plan.required_claim_role_tags),
        "required_source_claim_groups": list(plan.required_source_claim_groups),
        "required_source_citations": list(plan.required_source_citations),
        "coverage_policy": plan.coverage_policy,
    }


def _planned_write_payload(write: PlannedPageWrite) -> dict[str, Any]:
    return {
        "write_id": write.write_id,
        "action": write.action,
        "page_metadata": _page_metadata_payload(write.page_metadata),
        "extracted_units": list(write.extracted_units),
        "evidence": [_evidence_payload(evidence) for evidence in write.evidence],
        "wiki_matches": [_wiki_match_payload(match) for match in write.wiki_matches],
        "claim_comparisons": [
            _claim_comparison_payload(comparison) for comparison in write.claim_comparisons
        ],
        "projection": _projection_payload(write.projection),
        "existing_page_id": write.existing_page_id,
        "resolved_page_body_contract": _resolved_contract_payload(
            write.resolved_page_body_contract
        ),
        "source_summary_plan": _source_summary_plan_payload(write.source_summary_plan),
    }


def _source_page_group_payload(group: SourcePageGroup) -> dict[str, Any]:
    return {
        "source_page_group_id": group.source_page_group_id,
        "raw_source": _raw_source_payload(group.raw_source),
        "page_id": group.page_id,
        "extracted_units": list(group.extracted_units),
        "first_heading": group.first_heading,
        "last_heading": group.last_heading,
        "first_locator": group.first_locator,
        "last_locator": group.last_locator,
        "token_estimate": group.token_estimate,
    }
