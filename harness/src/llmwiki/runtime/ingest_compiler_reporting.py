"""Findings and reports for the single ingest compiler."""

from __future__ import annotations

from collections import Counter

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
) -> tuple[CompilerFinding, ...]:
    findings: list[CompilerFinding] = []
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
    return tuple(findings)


def rejected_page_ids(findings: tuple[CompilerFinding, ...]) -> tuple[str, ...]:
    return tuple(dict.fromkeys(finding.page_id for finding in findings if finding.page_id))


def compiler_report(
    source_locator: str,
    artifact_set: IngestArtifactSet,
    findings: tuple[CompilerFinding, ...],
) -> str:
    top_codes = ", ".join(
        f"{code}={count}"
        for code, count in Counter(f.finding_code for f in findings).most_common(5)
    )
    suffix = f" Top compiler findings: {top_codes}." if top_codes else ""
    return (
        f"Ingest compiler run {artifact_set.ingest_artifact_set_id} for raw/{source_locator}.\n"
        f"Accepted pages: {len(artifact_set.accepted_page_ids)}; "
        f"rejected pages: {len(artifact_set.rejected_page_ids)}.{suffix}"
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
