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
    canonical_json,
    content_fingerprint,
    deterministic_id,
    short_digest,
)
from llmwiki.domain.ledger.coverage import ProjectionCoverage
from llmwiki.domain.ledger.ledger import ClaimLedger
from llmwiki.domain.ledger.page_synthesis import (
    PageDraftRecord,
    PageSynthesisFinding,
    PageSynthesisPlan,
)
from llmwiki.domain.ledger.pointers import PortableArtifactPointer
from llmwiki.domain.ledger.projection import ProjectionSourceSupport
from llmwiki.domain.ledger.projection_context import ProjectionContext
from llmwiki.domain.ledger.quality import LedgerQualityReport
from llmwiki.domain.ledger.quality_catalog import (
    QualityCheckCatalog,
    QualityFindingSeverityPolicy,
    ReasonApplicabilityPolicy,
)
from llmwiki.domain.ledger.source_coverage import SourceCoverage, source_coverage_id
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
class ProjectionCoverageArtifact:
    projection_coverage_artifact_id: str
    projection_coverage_fingerprint: str
    artifact_format: str
    wiki_page_locator: str
    page_body_hash: str
    ledger_quality_report_pointer: PortableArtifactPointer
    projection_source_support_set: tuple[ProjectionSourceSupport, ...]
    projection_coverage: ProjectionCoverage


@dataclass(frozen=True)
class ProjectionContextArtifact:
    projection_context_artifact_id: str
    projection_context_fingerprint: str
    artifact_format: str
    source_locator: str
    source_hash: str
    projection_context: ProjectionContext


@dataclass(frozen=True)
class SourceCoverageArtifact:
    source_coverage_artifact_id: str
    source_coverage_fingerprint: str
    artifact_format: str
    source_coverage: SourceCoverage


@dataclass(frozen=True)
class PageSynthesisPlanArtifact:
    page_synthesis_plan_artifact_id: str
    page_synthesis_plan_fingerprint: str
    artifact_format: str
    plans: tuple[PageSynthesisPlan, ...]


@dataclass(frozen=True)
class PageDraftArtifact:
    page_draft_artifact_id: str
    page_draft_fingerprint: str
    artifact_format: str
    draft_records: tuple[PageDraftRecord, ...]


@dataclass(frozen=True)
class PageSynthesisFindingsArtifact:
    page_synthesis_findings_artifact_id: str
    page_synthesis_findings_fingerprint: str
    artifact_format: str
    findings: tuple[PageSynthesisFinding, ...]


@dataclass(frozen=True)
class BlockedWriteDiagnosticArtifact:
    blocked_write_diagnostic_artifact_id: str
    blocked_write_diagnostic_fingerprint: str
    artifact_format: str
    page_write_decision: str
    wiki_page_locator: str
    claim_ledger_pointer: PortableArtifactPointer
    ledger_quality_report_pointer: PortableArtifactPointer


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
    fingerprint = _ledger_quality_report_fingerprint(report)
    return LedgerQualityReportArtifact(
        ledger_quality_report_artifact_id=f"ledger-quality-report-{fingerprint}",
        ledger_quality_report_fingerprint=fingerprint,
        artifact_format=ARTIFACT_FORMAT,
        ledger_quality_report=report,
    )


def _ledger_quality_report_fingerprint(report: LedgerQualityReport) -> str:
    finding_rows = tuple(
        (
            finding.quality_check_id,
            finding.quality_report_scope,
            finding.quality_finding_severity,
            finding.quality_finding_reason,
            finding.quality_finding_subject.quality_finding_subject_kind,
            finding.quality_finding_subject.quality_finding_subject_id,
            finding.quality_finding_subject.quality_finding_subject_field,
            finding.quality_finding_locator.quality_finding_locator_kind,
            finding.quality_finding_locator.quality_finding_subject_id,
            finding.quality_finding_locator.source_range_id,
            finding.quality_finding_locator.wiki_page_locator,
            finding.review_reason.reason_kind if finding.review_reason else "",
        )
        for finding in report.findings
    )
    return content_fingerprint(
        (
            report.quality_report_scope,
            report.quality_check_catalog_pointer,
            finding_rows,
        )
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
    fingerprint = claim_ledger_artifact_fingerprint(draft)
    return replace(draft, claim_ledger_fingerprint=fingerprint)


def claim_ledger_artifact_fingerprint(artifact: ClaimLedgerArtifact) -> str:
    members = _claim_ledger_artifact_json_members(
        artifact,
        ledger_json=_claim_ledger_fingerprint_json(artifact.ledger),
    )
    members.pop("claim_ledger_fingerprint", None)
    members.pop("ledger_quality_report_pointer", None)
    return short_digest(_canonical_object_json(members))


def claim_ledger_artifact_to_json(
    artifact: ClaimLedgerArtifact,
    *,
    entry_ids: tuple[str, ...] = (),
    atom_ids: tuple[str, ...] = (),
) -> str:
    return _canonical_object_json(
        _claim_ledger_artifact_json_members(
            artifact,
            ledger_json=_claim_ledger_json(artifact.ledger, entry_ids=entry_ids, atom_ids=atom_ids),
        )
    )


def _claim_ledger_artifact_json_members(
    artifact: ClaimLedgerArtifact, *, ledger_json: str
) -> dict[str, str]:
    return {
        "artifact_format": canonical_json(artifact.artifact_format),
        "claim_ledger_fingerprint": canonical_json(artifact.claim_ledger_fingerprint),
        "claim_ledger_id": canonical_json(artifact.claim_ledger_id),
        "document_structure_pointer": canonical_json(artifact.document_structure_pointer),
        "ledger": ledger_json,
        "ledger_quality_report_pointer": canonical_json(artifact.ledger_quality_report_pointer),
    }


def _claim_ledger_json(
    ledger: ClaimLedger,
    *,
    entry_ids: tuple[str, ...] = (),
    atom_ids: tuple[str, ...] = (),
) -> str:
    entry_id_set = set(entry_ids)
    atom_id_set = set(atom_ids)
    entries = (
        tuple(entry for entry in ledger.entries if entry.ledger_entry_id in entry_id_set)
        if entry_id_set
        else ledger.entries
    )
    atoms = (
        tuple(atom for atom in ledger.technical_atoms if atom.technical_atom_id in atom_id_set)
        if atom_id_set
        else ledger.technical_atoms
    )
    contexts = (
        tuple(
            context
            for context in ledger.technical_atom_contexts
            if context.technical_atom_id in atom_id_set
        )
        if atom_id_set
        else ledger.technical_atom_contexts
    )
    return _canonical_object_json(
        {
            "claim_ledger_id": canonical_json(ledger.claim_ledger_id),
            "entries": _canonical_array_json(entries),
            "evidence_registry_hash": canonical_json(ledger.evidence_registry_hash),
            "extractor_decisions": "[]",
            "rejected_candidates": "[]",
            "source_family_assignment": canonical_json(ledger.source_family_assignment),
            "source_hash": canonical_json(ledger.source_hash),
            "source_locator": canonical_json(ledger.source_locator),
            "source_profile": canonical_json(ledger.source_profile),
            "source_statements": "[]",
            "technical_atom_contexts": _canonical_array_json(contexts),
            "technical_atoms": _canonical_array_json(atoms),
        }
    )


def _claim_ledger_fingerprint_json(ledger: ClaimLedger) -> str:
    return _canonical_object_json(
        {
            "claim_ledger_id": canonical_json(ledger.claim_ledger_id),
            "entry_ids": canonical_json(tuple(entry.ledger_entry_id for entry in ledger.entries)),
            "evidence_registry_hash": canonical_json(ledger.evidence_registry_hash),
            "source_hash": canonical_json(ledger.source_hash),
            "source_locator": canonical_json(ledger.source_locator),
            "technical_atom_ids": canonical_json(
                tuple(atom.technical_atom_id for atom in ledger.technical_atoms)
            ),
        }
    )


def _canonical_array_json(items: tuple[object, ...]) -> str:
    return "[" + ",".join(canonical_json(item) for item in items) + "]"


def _canonical_object_json(members: dict[str, str]) -> str:
    return "{" + ",".join(f"{canonical_json(key)}:{members[key]}" for key in sorted(members)) + "}"


def build_projection_coverage_artifact(
    *,
    wiki_page_locator: str,
    page_body_hash: str,
    support_set: tuple[ProjectionSourceSupport, ...],
    coverage: ProjectionCoverage,
    ledger_quality_report_pointer: PortableArtifactPointer,
) -> ProjectionCoverageArtifact:
    artifact_id = deterministic_id(
        "projection-coverage",
        wiki_page_locator,
        page_body_hash,
        "|".join(support.projection_source_support_id for support in support_set),
    )
    draft = ProjectionCoverageArtifact(
        projection_coverage_artifact_id=artifact_id,
        projection_coverage_fingerprint="",
        artifact_format=ARTIFACT_FORMAT,
        wiki_page_locator=wiki_page_locator,
        page_body_hash=page_body_hash,
        ledger_quality_report_pointer=ledger_quality_report_pointer,
        projection_source_support_set=support_set,
        projection_coverage=coverage,
    )
    fingerprint = artifact_fingerprint(
        draft, exclude=("projection_coverage_fingerprint", "ledger_quality_report_pointer")
    )
    return replace(draft, projection_coverage_fingerprint=fingerprint)


def build_source_coverage_artifact(coverage: SourceCoverage) -> SourceCoverageArtifact:
    draft = SourceCoverageArtifact(
        source_coverage_artifact_id=source_coverage_id(coverage),
        source_coverage_fingerprint="",
        artifact_format=ARTIFACT_FORMAT,
        source_coverage=coverage,
    )
    fingerprint = artifact_fingerprint(draft, exclude=("source_coverage_fingerprint",))
    return replace(draft, source_coverage_fingerprint=fingerprint)


def build_page_synthesis_plan_artifact(
    *, source_hash: str, plans: tuple[PageSynthesisPlan, ...]
) -> PageSynthesisPlanArtifact:
    draft = PageSynthesisPlanArtifact(
        page_synthesis_plan_artifact_id=deterministic_id("page-synthesis-plan", source_hash),
        page_synthesis_plan_fingerprint="",
        artifact_format=ARTIFACT_FORMAT,
        plans=plans,
    )
    fingerprint = artifact_fingerprint(
        draft,
        exclude=("page_synthesis_plan_artifact_id", "page_synthesis_plan_fingerprint"),
    )
    return replace(
        draft,
        page_synthesis_plan_artifact_id=deterministic_id(
            "page-synthesis-plan", source_hash, fingerprint
        ),
        page_synthesis_plan_fingerprint=fingerprint,
    )


def build_page_draft_artifact(
    *, source_hash: str, draft_records: tuple[PageDraftRecord, ...]
) -> PageDraftArtifact:
    draft = PageDraftArtifact(
        page_draft_artifact_id=deterministic_id("page-draft", source_hash),
        page_draft_fingerprint="",
        artifact_format=ARTIFACT_FORMAT,
        draft_records=draft_records,
    )
    fingerprint = artifact_fingerprint(
        draft,
        exclude=("page_draft_artifact_id", "page_draft_fingerprint"),
    )
    return replace(
        draft,
        page_draft_artifact_id=deterministic_id("page-draft", source_hash, fingerprint),
        page_draft_fingerprint=fingerprint,
    )


def build_page_synthesis_findings_artifact(
    *, source_hash: str, findings: tuple[PageSynthesisFinding, ...]
) -> PageSynthesisFindingsArtifact:
    draft = PageSynthesisFindingsArtifact(
        page_synthesis_findings_artifact_id=deterministic_id(
            "page-synthesis-findings", source_hash
        ),
        page_synthesis_findings_fingerprint="",
        artifact_format=ARTIFACT_FORMAT,
        findings=findings,
    )
    fingerprint = artifact_fingerprint(
        draft,
        exclude=(
            "page_synthesis_findings_artifact_id",
            "page_synthesis_findings_fingerprint",
        ),
    )
    return replace(
        draft,
        page_synthesis_findings_artifact_id=deterministic_id(
            "page-synthesis-findings", source_hash, fingerprint
        ),
        page_synthesis_findings_fingerprint=fingerprint,
    )


def build_projection_context_artifact(
    *,
    source_locator: str,
    source_hash: str,
    projection_context: ProjectionContext,
) -> ProjectionContextArtifact:
    fingerprint = artifact_fingerprint(
        {
            "source_hash": source_hash,
            "source_locator": source_locator,
            "projection_context": projection_context,
        }
    )
    return ProjectionContextArtifact(
        projection_context_artifact_id=deterministic_id(
            "projection-context", source_hash, source_locator, fingerprint
        ),
        projection_context_fingerprint=fingerprint,
        artifact_format=ARTIFACT_FORMAT,
        source_locator=source_locator,
        source_hash=source_hash,
        projection_context=projection_context,
    )


def build_blocked_write_diagnostic_artifact(
    *,
    wiki_page_locator: str,
    claim_ledger_pointer: PortableArtifactPointer,
    ledger_quality_report_pointer: PortableArtifactPointer,
) -> BlockedWriteDiagnosticArtifact:
    artifact_id = deterministic_id(
        "blocked-write-diagnostic",
        wiki_page_locator,
        claim_ledger_pointer.target_artifact_id,
        "block-authoritative-write",
    )
    draft = BlockedWriteDiagnosticArtifact(
        blocked_write_diagnostic_artifact_id=artifact_id,
        blocked_write_diagnostic_fingerprint="",
        artifact_format=ARTIFACT_FORMAT,
        page_write_decision="block-authoritative-write",
        wiki_page_locator=wiki_page_locator,
        claim_ledger_pointer=claim_ledger_pointer,
        ledger_quality_report_pointer=ledger_quality_report_pointer,
    )
    fingerprint = artifact_fingerprint(
        draft, exclude=("blocked_write_diagnostic_fingerprint", "ledger_quality_report_pointer")
    )
    return replace(draft, blocked_write_diagnostic_fingerprint=fingerprint)


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
