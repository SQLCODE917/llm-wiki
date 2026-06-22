"""Pure deterministic finding builders for ingest confidence gates."""

from __future__ import annotations

from llmwiki.domain.citations import inspect_citations
from llmwiki.domain.evidence import EvidencePolicy
from llmwiki.domain.evidence_locator_index import EvidenceLocatorIndex
from llmwiki.domain.evidence_registry import EvidenceRegistry
from llmwiki.domain.graph import build_wiki_graph, graph_status
from llmwiki.domain.index import index_page_ids
from llmwiki.domain.ingest_confidence import (
    FindingSeverity,
    GateKind,
    GateStatus,
    IngestConfidenceGate,
    ValidationFinding,
    validation_finding,
)
from llmwiki.domain.links import compute_findings
from llmwiki.domain.objects import PagePlan, SourceSummaryQualityReport
from llmwiki.domain.source_summary_quality import source_summary_quality_report
from llmwiki.domain.system_pages import ORPHAN_EXEMPT_PAGES
from llmwiki.runtime.ingest_confidence_page_scope import page_body
from llmwiki.store import WikiStore

_EVIDENCE_CODES = frozenset(
    {
        "evidence-canonicalized",
        "evidence-not-found",
        "evidence-outside-locator",
        "locator-out-of-range",
    }
)


def source_summary_findings(
    source_locator: str, plan: PagePlan, scoped_pages: dict[str, str]
) -> tuple[ValidationFinding, ...]:
    report = source_summary_quality_report(plan, scoped_pages)
    return _source_summary_report_findings(source_locator, report)


def source_summary_detail(plan: PagePlan, scoped_pages: dict[str, str]) -> str:
    report = source_summary_quality_report(plan, scoped_pages)
    return (
        f"Selected ineligible claims: {report.selected_ineligible_claims}\n"
        f"False source uncertainty claims: {report.false_source_uncertainty_claims}\n"
        f"Source-framing bullets: {report.source_framing_bullets}\n"
        f"Missing unit coverage: {report.missing_unit_coverage}"
    )


def citation_findings(
    source_locator: str, store: WikiStore, scoped_pages: dict[str, str]
) -> tuple[ValidationFinding, ...]:
    findings: list[ValidationFinding] = []
    if not scoped_pages:
        findings.append(
            validation_finding(
                severity="blocker",
                category="planning",
                source_locator=source_locator,
                message="No wiki pages currently declare this source.",
            )
        )
    inventory = store.source_inventory()
    for page_id, text in scoped_pages.items():
        report = inspect_citations(page_id, page_body(text), inventory)
        for citation_finding in report.findings:
            findings.append(
                validation_finding(
                    severity=_severity(citation_finding.severity),
                    category="citation",
                    source_locator=source_locator,
                    page_id=page_id,
                    message=f"{citation_finding.code}: {citation_finding.message}",
                )
            )
    return tuple(findings)


def evidence_registry_findings(
    source_locator: str, registry: EvidenceRegistry | None
) -> tuple[ValidationFinding, ...]:
    if registry is None:
        return (
            validation_finding(
                severity="blocker",
                category="evidence",
                source_locator=source_locator,
                message="EvidenceRegistry is missing.",
            ),
        )
    findings: list[ValidationFinding] = []
    if not registry.source_texts:
        findings.append(_evidence_finding(source_locator, "EvidenceRegistry has no SourceText."))
    if not registry.evidence_records:
        findings.append(
            validation_finding(
                severity="warning",
                category="evidence",
                source_locator=source_locator,
                message="EvidenceRegistry has no EvidenceRecord entries.",
            )
        )
    return tuple(findings)


def evidence_registry_detail(registry: EvidenceRegistry | None) -> str:
    if registry is None:
        return "No EvidenceRegistry available."
    return (
        f"Source texts: {len(registry.source_texts)}\n"
        f"Source ranges: {len(registry.source_ranges)}\n"
        f"Evidence records: {len(registry.evidence_records)}"
    )


def evidence_policy_findings(
    source_locator: str,
    store: WikiStore,
    scoped_pages: dict[str, str],
    registry: EvidenceRegistry | None,
    locator_index: EvidenceLocatorIndex | None,
    *,
    include_source_range: bool,
) -> tuple[ValidationFinding, ...]:
    if registry is None:
        return ()
    findings: list[ValidationFinding] = []
    policy = EvidencePolicy(mode="warn", registry=registry, locator_index=locator_index)
    for page_id, text in scoped_pages.items():
        report = policy.check_page(page_id, page_body(text), store.source_inventory())
        for citation_finding in report.findings:
            is_source_range = citation_finding.code == "source-range-violation"
            if is_source_range != include_source_range:
                continue
            if not include_source_range and citation_finding.code not in _EVIDENCE_CODES:
                continue
            findings.append(
                validation_finding(
                    severity="warning" if is_source_range else _severity(citation_finding.severity),
                    category="source-range" if is_source_range else "evidence",
                    source_locator=source_locator,
                    page_id=page_id,
                    message=f"{citation_finding.code}: {citation_finding.message}",
                )
            )
    return tuple(findings)


def graph_findings(
    source_locator: str,
    store: WikiStore,
    page_texts: dict[str, str],
    scoped_pages: dict[str, str],
    today: str,
) -> tuple[ValidationFinding, ...]:
    lint_run = compute_findings(
        page_texts,
        index_page_ids(store.read_index()),
        exempt_from_orphans=ORPHAN_EXEMPT_PAGES,
    )
    findings = [
        validation_finding(
            severity="warning",
            category="graph",
            source_locator=source_locator,
            page_id=page_id,
            message="Broken links: " + ", ".join(targets),
        )
        for page_id, targets in lint_run.broken_links.items()
        if page_id in scoped_pages
    ]
    status = graph_status(
        build_wiki_graph(page_texts, generated_date=today), store.read_graph_json()
    )
    if status.status != "current":
        findings.append(
            validation_finding(
                severity="warning",
                category="graph",
                source_locator=source_locator,
                message=f"Graph export is {status.status}: {status.message}",
            )
        )
    return tuple(findings)


def index_findings(
    source_locator: str,
    store: WikiStore,
    page_texts: dict[str, str],
    scoped_pages: dict[str, str],
) -> tuple[ValidationFinding, ...]:
    lint_run = compute_findings(
        page_texts,
        index_page_ids(store.read_index()),
        exempt_from_orphans=ORPHAN_EXEMPT_PAGES,
    )
    findings = [
        validation_finding(
            severity="warning",
            category="index",
            source_locator=source_locator,
            page_id=page_id,
            message="Page is missing from index.md.",
        )
        for page_id in lint_run.missing_from_index
        if page_id in scoped_pages
    ]
    findings.extend(
        validation_finding(
            severity="warning",
            category="index",
            source_locator=source_locator,
            page_id=page_id,
            message="index.md contains an entry whose page does not exist.",
        )
        for page_id in lint_run.stale_index_entries
    )
    return tuple(findings)


def confidence_gate(
    gate_id: str,
    gate_kind: GateKind,
    source_locator: str,
    status: GateStatus,
    findings: tuple[ValidationFinding, ...],
    detail: str = "",
) -> IngestConfidenceGate:
    return IngestConfidenceGate(
        gate_id=gate_id,
        gate_kind=gate_kind,
        scope=f"raw/{source_locator}",
        status=status,
        finding_ids=tuple(finding.finding_id for finding in findings),
        detail=detail,
    )


def _source_summary_report_findings(
    source_locator: str, report: SourceSummaryQualityReport
) -> tuple[ValidationFinding, ...]:
    checks = (
        ("selected_ineligible_claims", "Selected source-summary claims include ineligible claims."),
        (
            "false_source_uncertainty_claims",
            "Source-summary claims mark uncertainty without source-uncertainty evidence.",
        ),
        ("source_framing_bullets", "Source-summary bullets use source-framing prose."),
        ("missing_unit_coverage", "Source-summary plans omit covered source units."),
    )
    findings: list[ValidationFinding] = []
    for attr, message in checks:
        count = int(getattr(report, attr))
        if count:
            findings.append(
                validation_finding(
                    severity="warning",
                    category="source-summary",
                    source_locator=source_locator,
                    message=f"{message} Count: {count}.",
                )
            )
    return tuple(findings)


def _severity(severity: str) -> FindingSeverity:
    return "blocker" if severity == "fail" else "warning"


def _evidence_finding(source_locator: str, message: str) -> ValidationFinding:
    return validation_finding(
        severity="blocker",
        category="evidence",
        source_locator=source_locator,
        message=message,
    )
