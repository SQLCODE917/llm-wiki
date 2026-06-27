"""Claim-ledger ingest pipeline adapter/orchestrator."""

from __future__ import annotations

from dataclasses import dataclass

from llmwiki.domain.ledger.artifacts import (
    BlockedWriteDiagnosticArtifact,
    PortableArtifactSet,
    build_blocked_write_diagnostic_artifact,
    build_claim_ledger_artifact,
    build_document_structure_artifact,
    build_ledger_quality_report_artifact,
    build_projection_coverage_artifact,
    build_quality_check_catalog_artifact,
    build_source_coverage_artifact,
)
from llmwiki.domain.ledger.builder import build_claim_ledger, default_schema_bundle
from llmwiki.domain.ledger.canonical import deterministic_id
from llmwiki.domain.ledger.pointers import (
    claim_ledger_pointer,
    document_structure_pointer,
    ledger_quality_report_pointer,
    quality_check_catalog_pointer,
)
from llmwiki.domain.ledger.projection import ProjectionSourceSupport, plan_source_page
from llmwiki.domain.ledger.quality import (
    LedgerQualityReport,
    build_ledger_quality_report,
    build_projection_quality_report,
    page_write_decision,
)
from llmwiki.domain.ledger.quality_catalog import (
    default_quality_check_catalog,
    default_reason_applicability_policy,
    default_severity_policy,
)
from llmwiki.domain.ledger.renderer import render_source_page
from llmwiki.domain.ledger.section_pages import build_section_pages
from llmwiki.domain.ledger.section_planning import build_section_grounded_plan
from llmwiki.domain.ledger.source_coverage import build_source_coverage
from llmwiki.domain.ledger.topics import build_topic_index, plan_source_topics
from llmwiki.domain.objects import Schema
from llmwiki.domain.pages import WikiPage, slugify
from llmwiki.pdf.document import DocumentModel
from llmwiki.runtime.document_model_segmentation import segment_document_model
from llmwiki.runtime.ledger_artifact_bundle import build_serialized_artifact_bundle
from llmwiki.runtime.ledger_pages import (
    build_source_wiki_page,
    build_topic_pages,
    ledger_summary,
    source_element_records,
    source_title,
)
from llmwiki.runtime.ledger_segmentation import ChunkText, segment_chunks


@dataclass(frozen=True)
class SourceLedgerResult:
    page_id: str
    wiki_page: WikiPage | None
    topic_pages: tuple[WikiPage, ...]
    page_write_decision: str
    ledger_report: LedgerQualityReport
    projection_report: LedgerQualityReport
    blocked_write_diagnostic: BlockedWriteDiagnosticArtifact | None
    artifact_files: dict[str, str]
    portable_artifact_set: PortableArtifactSet
    summary: str


def build_source_ledger(
    *,
    source_locator: str,
    source_hash: str,
    evidence_registry_hash: str,
    chunks: tuple[ChunkText, ...],
    document_model: DocumentModel | None = None,
    today: str,
    schema: Schema | None = None,
) -> SourceLedgerResult:
    resolved_schema = schema or Schema()
    bundle = default_schema_bundle()
    if document_model is None:
        inputs, profiles = segment_chunks(
            chunks, source_locator=source_locator, source_hash=source_hash, schema=resolved_schema
        )
    else:
        inputs, profiles = segment_document_model(
            document_model,
            source_locator=source_locator,
            source_hash=source_hash,
            schema=resolved_schema,
        )
    built = build_claim_ledger(
        source_locator=source_locator,
        source_hash=source_hash,
        evidence_registry_hash=evidence_registry_hash,
        segments=inputs,
        profiles=profiles,
        schema=bundle,
    )
    ledger, structure = built.ledger, built.document_structure

    catalog = default_quality_check_catalog()
    applicability = default_reason_applicability_policy()
    severity = default_severity_policy()
    catalog_artifact = build_quality_check_catalog_artifact(catalog, applicability, severity)
    catalog_pointer = quality_check_catalog_pointer(
        catalog_artifact.quality_check_catalog_artifact_id,
        catalog_artifact.quality_check_catalog_fingerprint,
    )

    ledger_report = build_ledger_quality_report(
        ledger, structure, catalog=catalog, severity=severity, catalog_pointer=catalog_pointer
    )
    ledger_report_artifact = build_ledger_quality_report_artifact(ledger_report)
    ds_artifact = build_document_structure_artifact(structure, source_hash)
    ds_pointer = document_structure_pointer(
        ds_artifact.document_structure_artifact_id, ds_artifact.document_structure_fingerprint
    )
    ledger_artifact = build_claim_ledger_artifact(
        ledger,
        ds_pointer,
        ledger_quality_report_pointer(
            ledger_report_artifact.ledger_quality_report_artifact_id,
            ledger_report_artifact.ledger_quality_report_fingerprint,
        ),
    )
    source_coverage_artifact = None
    if document_model is not None:
        source_coverage = build_source_coverage(
            source_locator=source_locator,
            source_hash=source_hash,
            elements=source_element_records(document_model),
            segments=inputs,
            ledger=ledger,
            structure=structure,
        )
        source_coverage_artifact = build_source_coverage_artifact(source_coverage)

    page_id = slugify(source_locator.rsplit(".", 1)[0])
    title = source_title(source_locator, structure)
    support = ProjectionSourceSupport(
        projection_source_support_id=deterministic_id(
            "projection-source-support", source_hash, ledger_artifact.claim_ledger_id
        ),
        source_hash=source_hash,
        source_locator=source_locator,
        claim_ledger_pointer=claim_ledger_pointer(
            ledger_artifact.claim_ledger_id, ledger_artifact.claim_ledger_fingerprint
        ),
        document_structure_pointer=ds_pointer,
    )
    plan = plan_source_page(
        ledger, structure, wiki_page_locator=page_id, title=title, source_support=support
    )
    rendered = render_source_page(plan, ledger)

    projection_report = build_projection_quality_report(
        plan,
        rendered.coverage,
        rendered.page_body,
        ledger,
        catalog=catalog,
        severity=severity,
        catalog_pointer=catalog_pointer,
    )
    projection_report_artifact = build_ledger_quality_report_artifact(projection_report)
    coverage_artifact = build_projection_coverage_artifact(
        wiki_page_locator=page_id,
        page_body_hash=rendered.page_body_hash,
        support_set=(support,),
        coverage=rendered.coverage,
        ledger_quality_report_pointer=ledger_quality_report_pointer(
            projection_report_artifact.ledger_quality_report_artifact_id,
            projection_report_artifact.ledger_quality_report_fingerprint,
        ),
    )

    section_plan = build_section_grounded_plan(ledger, structure)
    topics = plan_source_topics(ledger, structure, section_plan=section_plan)
    topic_index = build_topic_index(
        ledger,
        topics,
        source_locator=source_locator,
        source_hash=source_hash,
        projection_source_support_id=support.projection_source_support_id,
    )

    decision = page_write_decision(ledger_report, projection_report)
    blocked = None
    wiki_page: WikiPage | None = None
    topic_pages: tuple[WikiPage, ...] = ()
    if decision == "block-authoritative-write":
        blocked = build_blocked_write_diagnostic_artifact(
            wiki_page_locator=page_id,
            claim_ledger_pointer=support.claim_ledger_pointer,
            ledger_quality_report_pointer=ledger_quality_report_pointer(
                projection_report_artifact.ledger_quality_report_artifact_id,
                projection_report_artifact.ledger_quality_report_fingerprint,
            ),
        )
    else:
        topic_pages = build_topic_pages(topics, ledger, page_id, source_locator, today)
        topic_pages += build_section_pages(
            ledger,
            structure,
            source_page_id=page_id,
            source_locator=source_locator,
            today=today,
        )
        wiki_page = build_source_wiki_page(
            page_id,
            source_locator,
            title,
            ledger_summary(ledger, decision, len(topic_pages)),
            today,
            rendered.page_body,
            coverage_artifact,
        )
    summary = ledger_summary(ledger, decision, len(topic_pages))

    artifact_bundle = build_serialized_artifact_bundle(
        ds_artifact=ds_artifact,
        ledger_artifact=ledger_artifact,
        catalog_artifact=catalog_artifact,
        ledger_report_artifact=ledger_report_artifact,
        projection_report_artifact=projection_report_artifact,
        coverage_artifact=coverage_artifact,
        section_plan=section_plan,
        topic_index=topic_index,
        source_coverage_artifact=source_coverage_artifact,
        blocked=blocked,
    )

    return SourceLedgerResult(
        page_id=page_id,
        wiki_page=wiki_page,
        topic_pages=topic_pages,
        page_write_decision=decision,
        ledger_report=ledger_report,
        projection_report=projection_report,
        blocked_write_diagnostic=blocked,
        artifact_files=artifact_bundle.artifact_files,
        portable_artifact_set=artifact_bundle.portable_artifact_set,
        summary=summary,
    )
