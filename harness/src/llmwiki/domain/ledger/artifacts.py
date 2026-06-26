"""Portable artifacts and the PortableArtifactSet manifest.

Every artifact is a canonical JSON document with a deterministic id and one
typed artifact fingerprint that hashes its domain-relevant contents — excluding
its own id/fingerprint fields and any quality-report pointer (which is filled
after the fingerprint is fixed). The ``PortableArtifactSet`` is the first-class
manifest that addresses the child artifacts by id and fingerprint without
embedding their bodies.
"""

from __future__ import annotations

from dataclasses import dataclass, replace

from llmwiki.domain.ledger.canonical import (
    artifact_fingerprint,
    content_fingerprint,
    deterministic_id,
)
from llmwiki.domain.ledger.ledger import ClaimLedger
from llmwiki.domain.ledger.pointers import PortableArtifactPointer
from llmwiki.domain.ledger.quality import LedgerQualityReport
from llmwiki.domain.ledger.quality_catalog import (
    QualityCheckCatalog,
    QualityFindingSeverityPolicy,
    ReasonApplicabilityPolicy,
)
from llmwiki.domain.ledger.structure import DocumentStructure
from llmwiki.domain.ledger.vocab import ARTIFACT_FORMAT


@dataclass(frozen=True)
class DocumentStructureArtifact:
    document_structure_artifact_id: str
    document_structure_fingerprint: str
    artifact_format: str
    document_structure: DocumentStructure


@dataclass(frozen=True)
class ClaimLedgerArtifact:
    claim_ledger_id: str
    claim_ledger_fingerprint: str
    artifact_format: str
    document_structure_pointer: PortableArtifactPointer
    ledger_quality_report_pointer: PortableArtifactPointer
    ledger: ClaimLedger


@dataclass(frozen=True)
class QualityCheckCatalogArtifact:
    quality_check_catalog_artifact_id: str
    quality_check_catalog_fingerprint: str
    artifact_format: str
    quality_check_catalog: QualityCheckCatalog
    reason_applicability_policy: ReasonApplicabilityPolicy
    quality_finding_severity_policy: QualityFindingSeverityPolicy


@dataclass(frozen=True)
class LedgerQualityReportArtifact:
    ledger_quality_report_artifact_id: str
    ledger_quality_report_fingerprint: str
    artifact_format: str
    ledger_quality_report: LedgerQualityReport


@dataclass(frozen=True)
class PortableArtifactMember:
    portable_artifact_kind: str
    target_artifact_id: str
    target_artifact_fingerprint: str
    artifact_format: str = ARTIFACT_FORMAT


@dataclass(frozen=True)
class PortableArtifactSet:
    portable_artifact_set_id: str
    portable_artifact_set_fingerprint: str
    artifact_format: str
    members: tuple[PortableArtifactMember, ...]


def build_document_structure_artifact(
    structure: DocumentStructure, source_hash: str
) -> DocumentStructureArtifact:
    fingerprint = artifact_fingerprint(structure)
    return DocumentStructureArtifact(
        document_structure_artifact_id=deterministic_id(
            "document-structure", source_hash, fingerprint
        ),
        document_structure_fingerprint=fingerprint,
        artifact_format=ARTIFACT_FORMAT,
        document_structure=structure,
    )


def build_quality_check_catalog_artifact(
    catalog: QualityCheckCatalog,
    applicability: ReasonApplicabilityPolicy,
    severity: QualityFindingSeverityPolicy,
) -> QualityCheckCatalogArtifact:
    fingerprint = content_fingerprint((catalog, applicability, severity))
    return QualityCheckCatalogArtifact(
        quality_check_catalog_artifact_id=f"quality-check-catalog-{fingerprint}",
        quality_check_catalog_fingerprint=fingerprint,
        artifact_format=ARTIFACT_FORMAT,
        quality_check_catalog=catalog,
        reason_applicability_policy=applicability,
        quality_finding_severity_policy=severity,
    )


def build_ledger_quality_report_artifact(
    report: LedgerQualityReport,
) -> LedgerQualityReportArtifact:
    fingerprint = artifact_fingerprint(report)
    return LedgerQualityReportArtifact(
        ledger_quality_report_artifact_id=f"ledger-quality-report-{fingerprint}",
        ledger_quality_report_fingerprint=fingerprint,
        artifact_format=ARTIFACT_FORMAT,
        ledger_quality_report=report,
    )


def build_claim_ledger_artifact(
    ledger: ClaimLedger,
    document_structure_pointer: PortableArtifactPointer,
    ledger_quality_report_pointer: PortableArtifactPointer,
) -> ClaimLedgerArtifact:
    draft = ClaimLedgerArtifact(
        claim_ledger_id=ledger.claim_ledger_id,
        claim_ledger_fingerprint="",
        artifact_format=ARTIFACT_FORMAT,
        document_structure_pointer=document_structure_pointer,
        ledger_quality_report_pointer=ledger_quality_report_pointer,
        ledger=ledger,
    )
    fingerprint = artifact_fingerprint(
        draft, exclude=("claim_ledger_fingerprint", "ledger_quality_report_pointer")
    )
    return replace(draft, claim_ledger_fingerprint=fingerprint)


def build_portable_artifact_set(
    members: tuple[PortableArtifactMember, ...],
) -> PortableArtifactSet:
    for member in members:
        if member.portable_artifact_kind == "portable-artifact-set":
            raise ValueError("a PortableArtifactSet cannot list itself as a member")
    unique = tuple(
        dict.fromkeys(
            sorted(
                members,
                key=lambda m: (
                    m.portable_artifact_kind,
                    m.target_artifact_id,
                    m.target_artifact_fingerprint,
                ),
            )
        )
    )
    fingerprint = artifact_fingerprint({"members": unique})
    return PortableArtifactSet(
        portable_artifact_set_id=f"portable-artifact-set-{fingerprint}",
        portable_artifact_set_fingerprint=fingerprint,
        artifact_format=ARTIFACT_FORMAT,
        members=unique,
    )
