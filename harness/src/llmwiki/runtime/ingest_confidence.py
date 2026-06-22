"""Report assembly and filing for source-level ingest confidence."""

from __future__ import annotations

from llmwiki.domain.claim_support import ClaimSupportAuditReport
from llmwiki.domain.ingest_confidence import (
    IngestConfidenceGate,
    IngestConfidenceReport,
    ValidationFinding,
    gate_status,
    validation_finding,
)
from llmwiki.domain.pages import PageMetadata, WikiPage
from llmwiki.domain.system_pages import INGEST_CONFIDENCE_PAGE
from llmwiki.runtime.ingest_confidence_artifacts import PreparedIngestArtifacts
from llmwiki.runtime.ingest_confidence_gates import DeterministicConfidence
from llmwiki.store import WikiStore


def skipped_claim_support_gate(
    source_locator: str, reason: str
) -> tuple[IngestConfidenceGate, tuple[ValidationFinding, ...]]:
    finding = validation_finding(
        severity="info",
        category="claim-support",
        source_locator=source_locator,
        message=reason,
    )
    return (
        IngestConfidenceGate(
            gate_id="claim-support",
            gate_kind="model-assisted",
            scope=f"raw/{source_locator}",
            status="skipped",
            finding_ids=(finding.finding_id,),
            detail=reason,
        ),
        (finding,),
    )


def claim_support_gate_from_audit(
    source_locator: str, audit: ClaimSupportAuditReport
) -> tuple[IngestConfidenceGate, tuple[ValidationFinding, ...]]:
    findings = _claim_support_findings(source_locator, audit)
    gate = IngestConfidenceGate(
        gate_id="claim-support",
        gate_kind="model-assisted",
        scope=f"raw/{source_locator}",
        status=gate_status(findings),
        finding_ids=tuple(finding.finding_id for finding in findings),
        detail=_claim_support_detail(audit),
    )
    return gate, findings


def render_ingest_confidence_report(
    *,
    run_id: str,
    source_locator: str,
    prepared: PreparedIngestArtifacts,
    deterministic: DeterministicConfidence,
    claim_support_gate: IngestConfidenceGate,
    claim_support_findings: tuple[ValidationFinding, ...],
) -> IngestConfidenceReport:
    return IngestConfidenceReport(
        run_id=run_id,
        source_locator=source_locator,
        artifact_decisions=prepared.decisions,
        gates=(*deterministic.gates, claim_support_gate),
        findings=(*deterministic.findings, *claim_support_findings),
    )


def file_ingest_confidence_report(
    store: WikiStore, report: IngestConfidenceReport, today: str
) -> None:
    store.write_page(
        WikiPage(
            page_metadata=PageMetadata(
                page_id=INGEST_CONFIDENCE_PAGE,
                page_kind="synthesis",
                summary=f"Ingest confidence report from {today}.",
                updated=today,
            ),
            page_body=report.render(),
        )
    )


def _claim_support_findings(
    source_locator: str, audit: ClaimSupportAuditReport
) -> tuple[ValidationFinding, ...]:
    findings: list[ValidationFinding] = []
    for finding in audit.selection.deterministic_findings:
        findings.append(
            validation_finding(
                severity=finding.severity,
                category="claim-support",
                source_locator=source_locator,
                page_id=finding.page_id,
                message=f"{finding.category}: {finding.message}",
                fingerprint=finding.finding_id,
            )
        )
    for verdict in audit.verdicts:
        candidate = _candidate_page(audit, verdict.candidate_id)
        findings.append(
            validation_finding(
                severity=verdict.severity,
                category="claim-support",
                source_locator=source_locator,
                page_id=candidate,
                message=f"{verdict.verdict}: {verdict.rationale}",
                fingerprint=verdict.candidate_id,
            )
        )
    return tuple(findings)


def _claim_support_detail(audit: ClaimSupportAuditReport) -> str:
    return (
        f"Claim candidates discovered: {audit.selection.candidate_count}\n"
        f"Selected for model judgment: {audit.selection.selected_count}\n"
        f"Skipped by deterministic findings: {audit.selection.deterministic_skipped_count}\n"
        f"Skipped by cap: {audit.selection.skipped_count}\n"
        f"Verdicts recorded: {len(audit.verdicts)}"
    )


def _candidate_page(audit: ClaimSupportAuditReport, candidate_id: str) -> str:
    candidates = (*audit.selection.candidates, *audit.selection.blocked_candidates)
    for candidate in candidates:
        if candidate.candidate_id == candidate_id:
            return candidate.page_id
    return ""
