"""Source segmentation choices for claim-ledger ingest."""

from __future__ import annotations

from llmwiki.domain.ledger.builder import SegmentInput
from llmwiki.domain.ledger.extraction import ExtractedUnitProfile
from llmwiki.domain.objects import Schema
from llmwiki.domain.source_summary import SourceClaim
from llmwiki.pdf.document import DocumentModel
from llmwiki.runtime.document_model_segmentation import segment_document_model
from llmwiki.runtime.ledger_segmentation import (
    ChunkText,
    segment_chunks,
    segment_page_plan_claim_chunks,
)


def source_ledger_segments(
    *,
    source_locator: str,
    source_hash: str,
    chunks: tuple[ChunkText, ...],
    document_model: DocumentModel | None,
    source_claims: tuple[SourceClaim, ...],
    schema: Schema,
) -> tuple[tuple[SegmentInput, ...], dict[str, ExtractedUnitProfile]]:
    if document_model is not None and source_claims:
        return segment_document_model(
            document_model,
            source_locator=source_locator,
            source_hash=source_hash,
            schema=schema,
            source_claims_by_heading=_source_claims_by_heading(chunks, source_claims),
        )
    if source_claims:
        return segment_page_plan_claim_chunks(
            chunks,
            source_claims,
            source_locator=source_locator,
            source_hash=source_hash,
        )
    if document_model is None:
        return segment_chunks(
            chunks, source_locator=source_locator, source_hash=source_hash, schema=schema
        )
    return segment_document_model(
        document_model,
        source_locator=source_locator,
        source_hash=source_hash,
        schema=schema,
    )


def _source_claims_by_heading(
    chunks: tuple[ChunkText, ...], source_claims: tuple[SourceClaim, ...]
) -> dict[str, tuple[SourceClaim, ...]]:
    heading_by_unit = {chunk.unit_id: chunk.heading_path for chunk in chunks}
    grouped: dict[str, list[SourceClaim]] = {}
    for claim in source_claims:
        heading = heading_by_unit.get(claim.extracted_unit_id)
        if heading:
            grouped.setdefault(heading, []).append(claim)
    return {heading: tuple(claims) for heading, claims in grouped.items()}
