"""Adapt accepted typed evidence records into current page-plan SourceClaims."""

from __future__ import annotations

from llmwiki.domain.objects import Evidence, RawSource, SourceClaim
from llmwiki.domain.planning_analysis import top_terms
from llmwiki.domain.source_claim_quality import (
    claim_centrality,
    claim_certainty,
    claim_eligibility,
    claim_salience,
)
from llmwiki.domain.source_map import NormalizedSourceMap, SourceBlock, build_prompt_windows
from llmwiki.domain.typed_evidence import EvidenceRecordSet, TypedEvidenceRecord
from llmwiki.pdf.chunking import CHUNK_TOKEN_BUDGET, estimate_tokens


def source_claims_from_typed_evidence(
    *,
    raw_source: RawSource,
    source_map: NormalizedSourceMap,
    record_set: EvidenceRecordSet,
) -> tuple[SourceClaim, ...]:
    block_units = _block_unit_ids(source_map)
    blocks_by_id = source_map.source_blocks_by_id
    claims: list[SourceClaim] = []
    for record in record_set.accepted_records:
        first_block_id = record.source_block_ids[0] if record.source_block_ids else ""
        block = blocks_by_id.get(first_block_id)
        unit_id = block_units.get(first_block_id, first_block_id or record.typed_evidence_record_id)
        statement = record.support_text.strip() or record.canonical_text.strip()
        if not statement:
            continue
        roles = _role_tags(record)
        eligibility = claim_eligibility(statement, roles)
        centrality = claim_centrality(statement, block.section_path if block else "")
        evidence = Evidence(
            raw_source=raw_source,
            locator=_record_locator(record, block),
            claim=statement,
        )
        claims.append(
            SourceClaim(
                source_claim_id=f"source-claim-{record.typed_evidence_record_id}",
                statement=statement,
                evidence=evidence,
                extracted_unit_id=unit_id,
                source_span=evidence.locator,
                claim_role_tags=roles,
                claim_salience=claim_salience(statement, roles, eligibility, centrality),
                claim_certainty=claim_certainty(roles),
                subject_terms=top_terms(statement, 4),
                claim_eligibility=eligibility,
                claim_centrality=centrality,
            )
        )
    return tuple(claims)


def _block_unit_ids(source_map: NormalizedSourceMap) -> dict[str, str]:
    windows = build_prompt_windows(
        source_map,
        budget_tokens=CHUNK_TOKEN_BUDGET,
        estimate_tokens=estimate_tokens,
    )
    return {
        block_id: window.prompt_window_id
        for window in windows
        for block_id in window.source_block_ids
    }


def _record_locator(record: TypedEvidenceRecord, block: SourceBlock | None) -> str:
    anchor = record.source_anchors[0] if record.source_anchors else None
    if anchor is not None:
        start, end = anchor.page_span
    elif block is not None:
        start, end = block.page_span
    else:
        start, end = (0, 0)
    page = "document" if start <= 0 else f"p.{start}" if start == end else f"p.{start}-{end}"
    return f"{record.source_locator} {page} typed-evidence:{record.typed_evidence_record_id}"


def _role_tags(record: TypedEvidenceRecord) -> tuple[str, ...]:
    return {
        "argument": ("evidence",),
        "code_example": ("function", "worked-example"),
        "definition": ("definition",),
        "entity_fact": ("identity",),
        "formula": ("quantitative",),
        "navigation_note": ("source-framing",),
        "procedure_step": ("procedure",),
        "rule": ("requirement",),
        "table_fact": ("quantitative",),
    }.get(record.evidence_record_type, ("evidence",))
