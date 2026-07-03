"""Claim-ledger ingest pipeline adapter/orchestrator."""

from __future__ import annotations

from llmwiki.domain.ledger.artifacts import (
    build_blocked_write_diagnostic_artifact,
    build_claim_ledger_artifact,
    build_document_structure_artifact,
    build_ledger_quality_report_artifact,
    build_page_draft_artifact,
    build_page_synthesis_findings_artifact,
    build_page_synthesis_plan_artifact,
    build_projection_context_artifact,
    build_projection_coverage_artifact,
    build_quality_check_catalog_artifact,
    build_source_coverage_artifact,
)
from llmwiki.domain.ledger.builder import build_claim_ledger, default_schema_bundle
from llmwiki.domain.ledger.canonical import deterministic_id
from llmwiki.domain.ledger.knowledge_shapes import build_knowledge_shape_catalog
from llmwiki.domain.ledger.pointers import (
    claim_ledger_pointer,
    document_structure_pointer,
    ledger_quality_report_pointer,
    quality_check_catalog_pointer,
)
from llmwiki.domain.ledger.projection import ProjectionSourceSupport, plan_source_page
from llmwiki.domain.ledger.projection_context import build_projection_context
from llmwiki.domain.ledger.quality import (
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
from llmwiki.domain.ledger.section_planning import build_section_grounded_plan
from llmwiki.domain.ledger.source_coverage import build_source_coverage
from llmwiki.domain.ledger.staged_flow import (
    accepted_pages,
    build_extraction_result,
    build_lint_run,
    build_publish_run,
    build_source_plan,
    build_staged_page_set,
)
from llmwiki.domain.ledger.topics import build_topic_index, plan_source_topics
from llmwiki.domain.objects import Schema
from llmwiki.domain.pages import WikiPage, slugify
from llmwiki.domain.source_summary import SourceClaim
from llmwiki.pdf.document import DocumentModel
from llmwiki.runtime.ledger_artifact_bundle import build_serialized_artifact_bundle
from llmwiki.runtime.ledger_linked_pages import build_linked_page_projection
from llmwiki.runtime.ledger_pages import ledger_summary, source_element_records, source_title
from llmwiki.runtime.ledger_result import SourceLedgerResult
from llmwiki.runtime.ledger_segmentation import ChunkText
from llmwiki.runtime.ledger_source_segmentation import source_ledger_segments


def build_source_ledger(
    *,
    source_locator: str,
    source_hash: str,
    evidence_registry_hash: str,
    chunks: tuple[ChunkText, ...],
    document_model: DocumentModel | None = None,
    source_claims: tuple[SourceClaim, ...] = (),
    today: str,
    schema: Schema | None = None,
) -> SourceLedgerResult:
    resolved_schema = schema or Schema()
    bundle = default_schema_bundle()
    inputs, profiles = source_ledger_segments(
        source_locator=source_locator,
        source_hash=source_hash,
        chunks=chunks,
        document_model=document_model,
        source_claims=source_claims,
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
    page_id = slugify(source_locator.rsplit(".", 1)[0])
    title = source_title(source_locator, structure)
    source_plan = build_source_plan(
        source_locator=source_locator,
        source_hash=source_hash,
        source_page_id=page_id,
    )
    ledger_artifact = build_claim_ledger_artifact(
        ledger,
        ds_pointer,
        ledger_quality_report_pointer(
            ledger_report_artifact.ledger_quality_report_artifact_id,
            ledger_report_artifact.ledger_quality_report_fingerprint,
        ),
    )
    extraction_result = build_extraction_result(
        source_plan=source_plan,
        ledger=ledger,
        structure=structure,
        document_structure_artifact_id=ds_artifact.document_structure_artifact_id,
        claim_ledger_id=ledger_artifact.claim_ledger_id,
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
    shape_catalog = build_knowledge_shape_catalog(ledger, structure)
    projection_context = build_projection_context(ledger, structure)
    projection_context_artifact = build_projection_context_artifact(
        source_locator=source_locator,
        source_hash=source_hash,
        projection_context=projection_context,
    )
    topics = plan_source_topics(ledger, structure, section_plan=section_plan)
    topic_index = build_topic_index(
        ledger,
        topics,
        source_locator=source_locator,
        source_hash=source_hash,
        projection_source_support_id=support.projection_source_support_id,
    )

    decision = page_write_decision(ledger_report, projection_report)
    page_synthesis_plan_artifact = build_page_synthesis_plan_artifact(
        source_hash=source_hash, plans=()
    )
    page_draft_artifact = build_page_draft_artifact(source_hash=source_hash, draft_records=())
    page_synthesis_findings_artifact = build_page_synthesis_findings_artifact(
        source_hash=source_hash, findings=()
    )
    blocked = None
    wiki_page: WikiPage | None = None
    topic_pages: tuple[WikiPage, ...] = ()
    staged_pages: tuple[WikiPage, ...] = ()
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
        linked_projection = build_linked_page_projection(
            ledger=ledger,
            structure=structure,
            section_plan=section_plan,
            shape_catalog=shape_catalog,
            projection_context=projection_context,
            topics=topics,
            page_id=page_id,
            title=title,
            source_locator=source_locator,
            today=today,
            decision=decision,
            rendered=rendered,
            support=support,
            projection_report_artifact=projection_report_artifact,
        )
        wiki_page = linked_projection.source_page
        topic_pages = linked_projection.linked_pages
        coverage_artifact = linked_projection.coverage_artifact
        page_synthesis_plan_artifact = linked_projection.page_synthesis_plan_artifact
        page_draft_artifact = linked_projection.page_draft_artifact
        page_synthesis_findings_artifact = linked_projection.page_synthesis_findings_artifact
        staged_pages = (wiki_page, *topic_pages)
    staged_page_set = build_staged_page_set(source_plan, staged_pages)
    lint_run = build_lint_run(
        source_plan=source_plan,
        staged_page_set=staged_page_set,
        upstream_write_decision=decision,
    )
    publish_run = build_publish_run(source_plan, staged_page_set, lint_run)
    published_pages = accepted_pages(staged_page_set, publish_run)
    wiki_page = next((page for page in published_pages if page.page_id == page_id), None)
    topic_pages = tuple(page for page in published_pages if page.page_id != page_id)
    summary = ledger_summary(ledger, decision, len(topic_pages))

    artifact_bundle = build_serialized_artifact_bundle(
        ds_artifact=ds_artifact,
        ledger_artifact=ledger_artifact,
        catalog_artifact=catalog_artifact,
        ledger_report_artifact=ledger_report_artifact,
        projection_report_artifact=projection_report_artifact,
        coverage_artifact=coverage_artifact,
        projection_context_artifact=projection_context_artifact,
        page_synthesis_plan_artifact=page_synthesis_plan_artifact,
        page_draft_artifact=page_draft_artifact,
        page_synthesis_findings_artifact=page_synthesis_findings_artifact,
        section_plan=section_plan,
        knowledge_shape_catalog=shape_catalog,
        topic_index=topic_index,
        source_coverage_artifact=source_coverage_artifact,
        blocked=blocked,
        source_plan=source_plan,
        extraction_result=extraction_result,
        staged_page_set=staged_page_set,
        lint_run=lint_run,
        publish_run=publish_run,
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
        source_plan=source_plan,
        extraction_result=extraction_result,
        staged_page_set=staged_page_set,
        lint_run=lint_run,
        publish_run=publish_run,
        summary=summary,
    )
