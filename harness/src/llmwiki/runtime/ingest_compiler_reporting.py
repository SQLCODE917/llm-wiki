"""Findings and reports for the single ingest compiler."""

from __future__ import annotations

from collections import Counter

from llmwiki.domain.diagnostic_contracts import DiagnosticFinding, DiagnosticReport, RepairRun
from llmwiki.domain.ingest_compiler import CompilerFinding, IngestArtifactSet
from llmwiki.domain.ledger.article_lint_artifacts import ArticleLintArtifact
from llmwiki.domain.ledger.canonical import deterministic_id
from llmwiki.domain.ledger.evidence_pack import EvidencePackSet
from llmwiki.domain.ledger.page_publication import PagePublicationPlan
from llmwiki.runtime.ledger_human_article_pages import HumanArticleLinkedPages


def compiler_findings(
    publication_plan: PagePublicationPlan,
    pack_set: EvidencePackSet,
    human_articles: HumanArticleLinkedPages,
    article_lint: ArticleLintArtifact,
    *,
    diagnostic_findings: tuple[DiagnosticFinding, ...] = (),
    repair_run: RepairRun | None = None,
) -> tuple[CompilerFinding, ...]:
    findings: list[CompilerFinding] = []
    repaired_page_ids = set(repair_run.changed_page_ids if repair_run is not None else ())
    for rejected in publication_plan.rejected_candidates:
        findings.append(
            _finding(
                "page-plan",
                "warning",
                rejected.rejection_code,
                rejected.page_id,
                rejected.message,
            )
        )
    for pack_finding in pack_set.findings:
        findings.append(
            _finding(
                "evidence-packs",
                "blocking" if pack_finding.severity == "blocker" else pack_finding.severity,
                pack_finding.finding_code,
                pack_finding.page_id,
                pack_finding.message,
            )
        )
    for article_finding in human_articles.article_output.findings:
        findings.append(
            _finding(
                "human-articles",
                article_finding.severity,
                article_finding.finding_type,
                article_finding.page_id,
                article_finding.message,
            )
        )
    for run in article_lint.runs:
        if run.publication_gate.decision != "blocked":
            continue
        findings.extend(
            _finding(
                "article-lint",
                "blocking",
                lint_finding.finding_code,
                lint_finding.page_id,
                lint_finding.message,
            )
            for lint_finding in run.findings
            if lint_finding.severity == "blocking"
        )
    for finding in diagnostic_findings:
        if finding.severity != "blocking":
            continue
        if finding.page_id in repaired_page_ids:
            continue
        findings.append(
            _finding(
                "diagnostics",
                "blocking",
                finding.finding_code,
                finding.page_id,
                finding.message,
            )
        )
    if repair_run is not None:
        findings.extend(
            _finding(
                "repair",
                "blocking",
                "repair-rejected-page",
                page_id,
                "diagnostic repair did not produce an accepted article page",
            )
            for page_id in repair_run.rejected_page_ids
        )
    return tuple(findings)


def rejected_page_ids(findings: tuple[CompilerFinding, ...]) -> tuple[str, ...]:
    return tuple(dict.fromkeys(finding.page_id for finding in findings if finding.page_id))


def compiler_report(
    source_locator: str,
    artifact_set: IngestArtifactSet,
    findings: tuple[CompilerFinding, ...],
    *,
    diagnostic_report: DiagnosticReport | None = None,
    repair_run: RepairRun | None = None,
) -> str:
    top_codes = ", ".join(
        f"{code}={count}"
        for code, count in Counter(f.finding_code for f in findings).most_common(5)
    )
    suffix = f" Top compiler findings: {top_codes}." if top_codes else ""
    diagnostic = ""
    if diagnostic_report is not None and repair_run is not None:
        diagnostic = (
            f" Diagnostics: answered {diagnostic_report.answered_count}/"
            f"{diagnostic_report.question_count}, missing {diagnostic_report.missing_count}, "
            f"unsupported {diagnostic_report.unsupported_count}; "
            f"repair {repair_run.status}, changed {len(repair_run.changed_page_ids)}."
        )
    return (
        f"Ingest compiler run {artifact_set.ingest_artifact_set_id} for raw/{source_locator}.\n"
        f"Accepted pages: {len(artifact_set.accepted_page_ids)}; "
        f"rejected pages: {len(artifact_set.rejected_page_ids)}.{diagnostic}{suffix}"
    )


def _finding(
    stage: str, severity: str, code: str, page_id: str, message: str
) -> CompilerFinding:
    return CompilerFinding(
        deterministic_id("compiler-finding", stage, code, page_id, message),
        stage,
        severity,
        code,
        page_id,
        "",
        message,
    )
