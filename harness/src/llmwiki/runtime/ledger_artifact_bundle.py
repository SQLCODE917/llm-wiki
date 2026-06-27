"""Serialize claim-ledger ingest artifacts and their portable manifest."""

from __future__ import annotations

from dataclasses import dataclass

from llmwiki.domain.ledger.artifacts import (
    BlockedWriteDiagnosticArtifact,
    ClaimLedgerArtifact,
    DocumentStructureArtifact,
    LedgerQualityReportArtifact,
    PortableArtifactMember,
    PortableArtifactSet,
    ProjectionCoverageArtifact,
    QualityCheckCatalogArtifact,
    SourceCoverageArtifact,
    build_portable_artifact_set,
)
from llmwiki.domain.ledger.canonical import canonical_json
from llmwiki.domain.ledger.section_planning import SectionGroundedPlan
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
    section_plan: SectionGroundedPlan,
    topic_index: TopicIndex,
    source_coverage_artifact: SourceCoverageArtifact | None,
    blocked: BlockedWriteDiagnosticArtifact | None,
) -> SerializedLedgerArtifacts:
    members = _artifact_members(
        ds_artifact,
        ledger_artifact,
        catalog_artifact,
        ledger_report_artifact,
        projection_report_artifact,
        coverage_artifact,
        section_plan,
        source_coverage_artifact,
        blocked,
    )
    artifact_files = _artifact_files(
        ds_artifact,
        ledger_artifact,
        catalog_artifact,
        ledger_report_artifact,
        projection_report_artifact,
        coverage_artifact,
        section_plan,
        topic_index,
        source_coverage_artifact,
        blocked,
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
    section_plan: SectionGroundedPlan,
    source_coverage_artifact: SourceCoverageArtifact | None,
    blocked: BlockedWriteDiagnosticArtifact | None,
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
            "section-grounded-plan-artifact",
            section_plan.section_grounded_plan_id,
            section_plan.section_grounded_plan_fingerprint,
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
    section_plan: SectionGroundedPlan,
    topic_index: TopicIndex,
    source_coverage_artifact: SourceCoverageArtifact | None,
    blocked: BlockedWriteDiagnosticArtifact | None,
) -> dict[str, str]:
    artifact_files = {
        "document-structure.json": canonical_json(ds_artifact, indent=2),
        "claim-ledger.json": canonical_json(ledger_artifact, indent=2),
        "quality-check-catalog.json": canonical_json(catalog_artifact, indent=2),
        "ledger-quality-report.json": canonical_json(ledger_report_artifact, indent=2),
        "projection-quality-report.json": canonical_json(projection_report_artifact, indent=2),
        "projection-coverage.json": canonical_json(coverage_artifact, indent=2),
        "section-plan.json": canonical_json(section_plan, indent=2),
        "topics.json": canonical_json(topic_index, indent=2),
    }
    if source_coverage_artifact is not None:
        artifact_files["source-coverage.json"] = canonical_json(source_coverage_artifact, indent=2)
    if blocked is not None:
        artifact_files["blocked-write-diagnostic.json"] = canonical_json(blocked, indent=2)
    return artifact_files


def _member(kind: str, target_id: str, fingerprint: str) -> PortableArtifactMember:
    return PortableArtifactMember(kind, target_id, fingerprint)
