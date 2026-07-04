"""Serialize superseded claim-ledger ingest artifacts.

Do not use this bundle from production ingest. `IngestCompiler` writes the
current source-scoped artifact set. This module is retained only for validation
comparisons and is scheduled for removal after compiler/evidence-pack
validation.
"""

from __future__ import annotations

from dataclasses import dataclass

from llmwiki.domain.ledger.article_lint_artifacts import ArticleLintArtifact
from llmwiki.domain.ledger.artifacts import (
    BlockedWriteDiagnosticArtifact,
    ClaimLedgerArtifact,
    DocumentStructureArtifact,
    LedgerQualityReportArtifact,
    PageSynthesisFindingsArtifact,
    PageSynthesisPlanArtifact,
    PortableArtifactMember,
    PortableArtifactSet,
    ProjectionContextArtifact,
    ProjectionCoverageArtifact,
    QualityCheckCatalogArtifact,
    SourceCoverageArtifact,
    build_portable_artifact_set,
    claim_ledger_artifact_to_json,
)
from llmwiki.domain.ledger.canonical import canonical_json
from llmwiki.domain.ledger.evidence_pack import EvidencePackSet
from llmwiki.domain.ledger.human_article_artifacts import (
    HumanArticleArtifact,
    HumanArticleFindingsArtifact,
)
from llmwiki.domain.ledger.knowledge_shapes import KnowledgeShapeCatalog
from llmwiki.domain.ledger.page_publication import (
    PagePublicationPlan,
    PublicationWalkabilityReport,
)
from llmwiki.domain.ledger.page_publication_planning import render_publication_walkability_report
from llmwiki.domain.ledger.section_planning import SectionGroundedPlan
from llmwiki.domain.ledger.staged_contracts import (
    LedgerExtractionResult,
    ProjectionLintRun,
    PublishRun,
    SourcePlan,
    StagedWikiPageSet,
)
from llmwiki.domain.ledger.topic_models import TopicIndex


@dataclass(frozen=True)
class SerializedLedgerArtifacts:
    artifact_files: dict[str, str]
    portable_artifact_set: PortableArtifactSet


def build_serialized_artifact_bundle(
    *,
    ds_artifact: DocumentStructureArtifact,
    ledger_artifact: ClaimLedgerArtifact,
    catalog_artifact: QualityCheckCatalogArtifact,
    ledger_report_artifact: LedgerQualityReportArtifact,
    projection_report_artifact: LedgerQualityReportArtifact,
    coverage_artifact: ProjectionCoverageArtifact,
    projection_context_artifact: ProjectionContextArtifact,
    page_synthesis_plan_artifact: PageSynthesisPlanArtifact,
    page_synthesis_findings_artifact: PageSynthesisFindingsArtifact,
    human_article_artifact: HumanArticleArtifact,
    human_article_findings_artifact: HumanArticleFindingsArtifact,
    article_lint_artifact: ArticleLintArtifact,
    page_publication_plan: PagePublicationPlan,
    publication_walkability_report: PublicationWalkabilityReport,
    evidence_pack_set: EvidencePackSet,
    section_plan: SectionGroundedPlan,
    knowledge_shape_catalog: KnowledgeShapeCatalog,
    topic_index: TopicIndex,
    source_coverage_artifact: SourceCoverageArtifact | None,
    blocked: BlockedWriteDiagnosticArtifact | None,
    source_plan: SourcePlan,
    extraction_result: LedgerExtractionResult,
    staged_page_set: StagedWikiPageSet,
    lint_run: ProjectionLintRun,
    publish_run: PublishRun,
) -> SerializedLedgerArtifacts:
    members = _artifact_members(
        ds_artifact,
        ledger_artifact,
        catalog_artifact,
        ledger_report_artifact,
        projection_report_artifact,
        coverage_artifact,
        projection_context_artifact,
        page_synthesis_plan_artifact,
        page_synthesis_findings_artifact,
        human_article_artifact,
        human_article_findings_artifact,
        article_lint_artifact,
        page_publication_plan,
        evidence_pack_set,
        section_plan,
        knowledge_shape_catalog,
        source_coverage_artifact,
        blocked,
        source_plan,
        extraction_result,
        staged_page_set,
        lint_run,
        publish_run,
    )
    artifact_files = _artifact_files(
        ds_artifact,
        ledger_artifact,
        catalog_artifact,
        ledger_report_artifact,
        projection_report_artifact,
        coverage_artifact,
        projection_context_artifact,
        page_synthesis_plan_artifact,
        page_synthesis_findings_artifact,
        human_article_artifact,
        human_article_findings_artifact,
        article_lint_artifact,
        page_publication_plan,
        publication_walkability_report,
        evidence_pack_set,
        section_plan,
        knowledge_shape_catalog,
        topic_index,
        source_coverage_artifact,
        blocked,
        source_plan,
        extraction_result,
        staged_page_set,
        lint_run,
        publish_run,
    )
    manifest = build_portable_artifact_set(tuple(members))
    artifact_files["portable-artifact-set.json"] = canonical_json(manifest, indent=2)
    return SerializedLedgerArtifacts(artifact_files, manifest)


def _artifact_members(
    ds_artifact: DocumentStructureArtifact,
    ledger_artifact: ClaimLedgerArtifact,
    catalog_artifact: QualityCheckCatalogArtifact,
    ledger_report_artifact: LedgerQualityReportArtifact,
    projection_report_artifact: LedgerQualityReportArtifact,
    coverage_artifact: ProjectionCoverageArtifact,
    projection_context_artifact: ProjectionContextArtifact,
    page_synthesis_plan_artifact: PageSynthesisPlanArtifact,
    page_synthesis_findings_artifact: PageSynthesisFindingsArtifact,
    human_article_artifact: HumanArticleArtifact,
    human_article_findings_artifact: HumanArticleFindingsArtifact,
    article_lint_artifact: ArticleLintArtifact,
    page_publication_plan: PagePublicationPlan,
    evidence_pack_set: EvidencePackSet,
    section_plan: SectionGroundedPlan,
    knowledge_shape_catalog: KnowledgeShapeCatalog,
    source_coverage_artifact: SourceCoverageArtifact | None,
    blocked: BlockedWriteDiagnosticArtifact | None,
    source_plan: SourcePlan,
    extraction_result: LedgerExtractionResult,
    staged_page_set: StagedWikiPageSet,
    lint_run: ProjectionLintRun,
    publish_run: PublishRun,
) -> list[PortableArtifactMember]:
    members = [
        _member(
            "document-structure-artifact",
            ds_artifact.document_structure_artifact_id,
            ds_artifact.document_structure_fingerprint,
        ),
        _member(
            "claim-ledger-artifact",
            ledger_artifact.claim_ledger_id,
            ledger_artifact.claim_ledger_fingerprint,
        ),
        _member(
            "quality-check-catalog-artifact",
            catalog_artifact.quality_check_catalog_artifact_id,
            catalog_artifact.quality_check_catalog_fingerprint,
        ),
        _member(
            "ledger-quality-report-artifact",
            ledger_report_artifact.ledger_quality_report_artifact_id,
            ledger_report_artifact.ledger_quality_report_fingerprint,
        ),
        _member(
            "ledger-quality-report-artifact",
            projection_report_artifact.ledger_quality_report_artifact_id,
            projection_report_artifact.ledger_quality_report_fingerprint,
        ),
        _member(
            "projection-coverage-artifact",
            coverage_artifact.projection_coverage_artifact_id,
            coverage_artifact.projection_coverage_fingerprint,
        ),
        _member(
            "projection-context-artifact",
            projection_context_artifact.projection_context_artifact_id,
            projection_context_artifact.projection_context_fingerprint,
        ),
        _member(
            "page-synthesis-plan-artifact",
            page_synthesis_plan_artifact.page_synthesis_plan_artifact_id,
            page_synthesis_plan_artifact.page_synthesis_plan_fingerprint,
        ),
        _member(
            "page-synthesis-findings-artifact",
            page_synthesis_findings_artifact.page_synthesis_findings_artifact_id,
            page_synthesis_findings_artifact.page_synthesis_findings_fingerprint,
        ),
        _member(
            "human-article-artifact",
            human_article_artifact.human_article_artifact_id,
            human_article_artifact.human_article_fingerprint,
        ),
        _member(
            "human-article-findings-artifact",
            human_article_findings_artifact.human_article_findings_artifact_id,
            human_article_findings_artifact.human_article_findings_fingerprint,
        ),
        _member(
            "article-lint-artifact",
            article_lint_artifact.article_lint_artifact_id,
            article_lint_artifact.article_lint_fingerprint,
        ),
        _member(
            "page-publication-plan-artifact",
            page_publication_plan.page_publication_plan_id,
            page_publication_plan.page_publication_plan_fingerprint,
        ),
        _member(
            "evidence-pack-set-artifact",
            evidence_pack_set.evidence_pack_set_id,
            evidence_pack_set.evidence_pack_set_fingerprint,
        ),
        _member(
            "section-grounded-plan-artifact",
            section_plan.section_grounded_plan_id,
            section_plan.section_grounded_plan_fingerprint,
        ),
        _member(
            "knowledge-shape-catalog-artifact",
            knowledge_shape_catalog.knowledge_shape_catalog_id,
            knowledge_shape_catalog.knowledge_shape_catalog_fingerprint,
        ),
        _member(
            "source-plan-artifact",
            source_plan.source_plan_id,
            source_plan.source_plan_fingerprint,
        ),
        _member(
            "extraction-result-artifact",
            extraction_result.extraction_result_id,
            extraction_result.extraction_result_fingerprint,
        ),
        _member(
            "staged-wiki-page-set-artifact",
            staged_page_set.staged_page_set_id,
            staged_page_set.staged_page_set_fingerprint,
        ),
        _member(
            "projection-lint-run-artifact",
            lint_run.lint_run_id,
            lint_run.lint_run_fingerprint,
        ),
        _member(
            "publish-run-artifact",
            publish_run.publish_run_id,
            publish_run.publish_run_fingerprint,
        ),
    ]
    if source_coverage_artifact is not None:
        members.append(
            _member(
                "source-coverage-artifact",
                source_coverage_artifact.source_coverage_artifact_id,
                source_coverage_artifact.source_coverage_fingerprint,
            )
        )
    if blocked is not None:
        members.append(
            _member(
                "blocked-write-diagnostic-artifact",
                blocked.blocked_write_diagnostic_artifact_id,
                blocked.blocked_write_diagnostic_fingerprint,
            )
        )
    return members


def _artifact_files(
    ds_artifact: DocumentStructureArtifact,
    ledger_artifact: ClaimLedgerArtifact,
    catalog_artifact: QualityCheckCatalogArtifact,
    ledger_report_artifact: LedgerQualityReportArtifact,
    projection_report_artifact: LedgerQualityReportArtifact,
    coverage_artifact: ProjectionCoverageArtifact,
    projection_context_artifact: ProjectionContextArtifact,
    page_synthesis_plan_artifact: PageSynthesisPlanArtifact,
    page_synthesis_findings_artifact: PageSynthesisFindingsArtifact,
    human_article_artifact: HumanArticleArtifact,
    human_article_findings_artifact: HumanArticleFindingsArtifact,
    article_lint_artifact: ArticleLintArtifact,
    page_publication_plan: PagePublicationPlan,
    publication_walkability_report: PublicationWalkabilityReport,
    evidence_pack_set: EvidencePackSet,
    section_plan: SectionGroundedPlan,
    knowledge_shape_catalog: KnowledgeShapeCatalog,
    topic_index: TopicIndex,
    source_coverage_artifact: SourceCoverageArtifact | None,
    blocked: BlockedWriteDiagnosticArtifact | None,
    source_plan: SourcePlan,
    extraction_result: LedgerExtractionResult,
    staged_page_set: StagedWikiPageSet,
    lint_run: ProjectionLintRun,
    publish_run: PublishRun,
) -> dict[str, str]:
    artifact_files = {
        "document-structure.json": canonical_json(ds_artifact, indent=2),
        "claim-ledger.json": claim_ledger_artifact_to_json(
            ledger_artifact,
            entry_ids=_topic_entry_ids(topic_index),
            atom_ids=_topic_atom_ids(topic_index),
        ),
        "quality-check-catalog.json": canonical_json(catalog_artifact, indent=2),
        "ledger-quality-report.json": canonical_json(ledger_report_artifact, indent=2),
        "projection-quality-report.json": canonical_json(projection_report_artifact, indent=2),
        "projection-coverage.json": canonical_json(coverage_artifact, indent=2),
        "projection-context.json": canonical_json(projection_context_artifact, indent=2),
        "page-synthesis-plan.json": canonical_json(page_synthesis_plan_artifact, indent=2),
        "page-synthesis-findings.json": canonical_json(
            page_synthesis_findings_artifact, indent=2
        ),
        "human-article.json": canonical_json(human_article_artifact, indent=2),
        "human-article-findings.json": canonical_json(
            human_article_findings_artifact, indent=2
        ),
        "article-lint-runs.json": canonical_json(article_lint_artifact, indent=2),
        "page-publication-plan.json": canonical_json(page_publication_plan, indent=2),
        "evidence-pack-set.json": canonical_json(evidence_pack_set, indent=2),
        "publication-walkability-report.md": render_publication_walkability_report(
            publication_walkability_report
        ),
        "section-plan.json": canonical_json(section_plan, indent=2),
        "knowledge-shapes.json": canonical_json(knowledge_shape_catalog, indent=2),
        "topics.json": canonical_json(topic_index, indent=2),
        "source-plan.json": canonical_json(source_plan, indent=2),
        "extraction-result.json": canonical_json(extraction_result, indent=2),
        "staged-pages.json": canonical_json(staged_page_set, indent=2),
        "lint-run.json": canonical_json(lint_run, indent=2),
        "publish-run.json": canonical_json(publish_run, indent=2),
    }
    if source_coverage_artifact is not None:
        artifact_files["source-coverage.json"] = canonical_json(source_coverage_artifact, indent=2)
    if blocked is not None:
        artifact_files["blocked-write-diagnostic.json"] = canonical_json(blocked, indent=2)
    return artifact_files


def _member(kind: str, target_id: str, fingerprint: str) -> PortableArtifactMember:
    return PortableArtifactMember(kind, target_id, fingerprint)


def _topic_entry_ids(topic_index: TopicIndex) -> tuple[str, ...]:
    return tuple(
        dict.fromkeys(entry_id for topic in topic_index.topics for entry_id in topic.entry_ids)
    )


def _topic_atom_ids(topic_index: TopicIndex) -> tuple[str, ...]:
    return tuple(
        dict.fromkeys(atom_id for topic in topic_index.topics for atom_id in topic.atom_ids)
    )
