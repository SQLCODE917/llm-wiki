"""Package current-artifact claim ledgers as portable ledger artifacts."""

from __future__ import annotations

from dataclasses import dataclass

from llmwiki.domain.evidence_registry import EvidenceRegistry
from llmwiki.domain.ledger.artifacts import (
    ClaimLedgerArtifact,
    DocumentStructureArtifact,
    LedgerQualityReportArtifact,
    PortableArtifactMember,
    PortableArtifactSet,
    ProjectionCoverageArtifact,
    QualityCheckCatalogArtifact,
    build_claim_ledger_artifact,
    build_document_structure_artifact,
    build_ledger_quality_report_artifact,
    build_portable_artifact_set,
    build_projection_coverage_artifact,
    build_quality_check_catalog_artifact,
)
from llmwiki.domain.ledger.canonical import canonical_json
from llmwiki.domain.ledger.current_ledger import build_current_claim_ledger
from llmwiki.domain.ledger.current_projection import (
    build_current_projection_coverage,
    build_projection_source_support,
)
from llmwiki.domain.ledger.current_structure import (
    build_current_document_structure,
    current_source_hash,
)
from llmwiki.domain.ledger.current_topics import build_current_topic_index
from llmwiki.domain.ledger.ledger import ClaimLedger
from llmwiki.domain.ledger.pointers import (
    document_structure_pointer,
    ledger_quality_report_pointer,
    quality_check_catalog_pointer,
)
from llmwiki.domain.ledger.quality import LedgerQualityReport, build_ledger_quality_report
from llmwiki.domain.ledger.quality_catalog import (
    default_quality_check_catalog,
    default_reason_applicability_policy,
    default_severity_policy,
)
from llmwiki.domain.ledger.structure import DocumentStructure
from llmwiki.domain.ledger.topic_models import TopicIndex
from llmwiki.domain.objects import PagePlan
from llmwiki.domain.technical_atoms import TechnicalAtomCatalog


@dataclass(frozen=True)
class CurrentLedgerArtifacts:
    document_structure: DocumentStructure
    ledger: ClaimLedger
    ledger_quality_report: LedgerQualityReport
    document_structure_artifact: DocumentStructureArtifact
    claim_ledger_artifact: ClaimLedgerArtifact
    quality_check_catalog_artifact: QualityCheckCatalogArtifact
    ledger_quality_report_artifact: LedgerQualityReportArtifact
    projection_coverage_artifact: ProjectionCoverageArtifact
    topic_index: TopicIndex
    portable_artifact_set: PortableArtifactSet

    @property
    def artifact_files(self) -> dict[str, str]:
        return {
            "document-structure.json": canonical_json(self.document_structure_artifact, indent=2),
            "claim-ledger.json": canonical_json(self.claim_ledger_artifact, indent=2),
            "quality-check-catalog.json": canonical_json(
                self.quality_check_catalog_artifact, indent=2
            ),
            "ledger-quality-report.json": canonical_json(
                self.ledger_quality_report_artifact, indent=2
            ),
            "projection-coverage.json": canonical_json(self.projection_coverage_artifact, indent=2),
            "topics.json": canonical_json(self.topic_index, indent=2),
            "portable-artifact-set.json": canonical_json(self.portable_artifact_set, indent=2),
        }


def build_current_ledger_artifacts(
    *,
    source_locator: str,
    page_plan: PagePlan,
    evidence_registry: EvidenceRegistry,
    technical_atom_catalog: TechnicalAtomCatalog,
) -> CurrentLedgerArtifacts:
    source_hash = current_source_hash(source_locator, page_plan, evidence_registry)
    structure = build_current_document_structure(
        source_locator=source_locator,
        source_hash=source_hash,
        page_plan=page_plan,
        evidence_registry=evidence_registry,
    )
    ledger = build_current_claim_ledger(
        source_locator=source_locator,
        source_hash=source_hash,
        page_plan=page_plan,
        evidence_registry=evidence_registry,
        document_structure=structure,
        technical_atom_catalog=technical_atom_catalog,
    )
    return _artifacts(source_locator, source_hash, page_plan, evidence_registry, structure, ledger)


def _artifacts(
    source_locator: str,
    source_hash: str,
    page_plan: PagePlan,
    evidence_registry: EvidenceRegistry,
    structure: DocumentStructure,
    ledger: ClaimLedger,
) -> CurrentLedgerArtifacts:
    catalog_artifact = build_quality_check_catalog_artifact(
        default_quality_check_catalog(),
        default_reason_applicability_policy(),
        default_severity_policy(),
    )
    catalog_pointer = quality_check_catalog_pointer(
        catalog_artifact.quality_check_catalog_artifact_id,
        catalog_artifact.quality_check_catalog_fingerprint,
    )
    report = build_ledger_quality_report(
        ledger,
        structure,
        catalog=catalog_artifact.quality_check_catalog,
        severity=catalog_artifact.quality_finding_severity_policy,
        catalog_pointer=catalog_pointer,
    )
    report_artifact = build_ledger_quality_report_artifact(report)
    structure_artifact = build_document_structure_artifact(structure, source_hash)
    ledger_artifact = build_claim_ledger_artifact(
        ledger,
        document_structure_pointer(
            structure_artifact.document_structure_artifact_id,
            structure_artifact.document_structure_fingerprint,
        ),
        ledger_quality_report_pointer(
            report_artifact.ledger_quality_report_artifact_id,
            report_artifact.ledger_quality_report_fingerprint,
        ),
    )
    projection_support = build_projection_source_support(
        source_locator=source_locator,
        source_hash=source_hash,
        claim_ledger_id=ledger_artifact.claim_ledger_id,
        claim_ledger_fingerprint=ledger_artifact.claim_ledger_fingerprint,
        document_structure_id=structure_artifact.document_structure_artifact_id,
        document_structure_fingerprint=structure_artifact.document_structure_fingerprint,
    )
    projection_coverage = build_current_projection_coverage(
        page_plan=page_plan,
        evidence_registry=evidence_registry,
        ledger=ledger,
        source_support=projection_support,
    )
    projection_coverage_artifact = build_projection_coverage_artifact(
        wiki_page_locator=f"planned-projection:{page_plan.plan_id}",
        page_body_hash=projection_coverage.page_body_hash,
        support_set=(projection_support,),
        coverage=projection_coverage.coverage,
        ledger_quality_report_pointer=ledger_quality_report_pointer(
            report_artifact.ledger_quality_report_artifact_id,
            report_artifact.ledger_quality_report_fingerprint,
        ),
    )
    topic_index = build_current_topic_index(
        source_locator=source_locator,
        source_hash=source_hash,
        projection_source_support_id=projection_support.projection_source_support_id,
        page_plan=page_plan,
        evidence_registry=evidence_registry,
        ledger=ledger,
    )
    manifest = build_portable_artifact_set(
        (
            _member("document-structure-artifact", structure_artifact),
            PortableArtifactMember(
                "claim-ledger-artifact",
                ledger_artifact.claim_ledger_id,
                ledger_artifact.claim_ledger_fingerprint,
            ),
            _member("quality-check-catalog-artifact", catalog_artifact),
            _member("ledger-quality-report-artifact", report_artifact),
            PortableArtifactMember(
                "projection-coverage-artifact",
                projection_coverage_artifact.projection_coverage_artifact_id,
                projection_coverage_artifact.projection_coverage_fingerprint,
            ),
        )
    )
    return CurrentLedgerArtifacts(
        structure,
        ledger,
        report,
        structure_artifact,
        ledger_artifact,
        catalog_artifact,
        report_artifact,
        projection_coverage_artifact,
        topic_index,
        manifest,
    )


def _member(kind: str, artifact: object) -> PortableArtifactMember:
    target_id = next(value for name, value in vars(artifact).items() if name.endswith("_id"))
    fingerprint = next(
        value for name, value in vars(artifact).items() if name.endswith("_fingerprint")
    )
    return PortableArtifactMember(kind, str(target_id), str(fingerprint))
