"""Render source manifest pages from compiler artifacts."""

from __future__ import annotations

from llmwiki.domain.article_viability import ArticleViabilityReport
from llmwiki.domain.article_write_queue import ArticleWriteQueueRun
from llmwiki.domain.compiler_candidate_admission import CandidateAdmissionReport
from llmwiki.domain.diagnostic_contracts import (
    DiagnosticQuestionSet,
    DiagnosticReport,
    RepairRun,
)
from llmwiki.domain.ingest_compiler import CompilerFinding
from llmwiki.domain.ledger.article_lint_artifacts import ArticleLintArtifact
from llmwiki.domain.ledger.evidence_pack import EvidencePackSet
from llmwiki.domain.ledger.page_publication import PagePublicationPlan
from llmwiki.domain.pages import PageMetadata, WikiPage
from llmwiki.domain.source_map import NormalizedSourceMap
from llmwiki.domain.source_profiles import SourceProfileArtifact
from llmwiki.domain.source_records import SourceRecordPlan
from llmwiki.domain.source_structure_integrity import SourceStructureIntegrityReport
from llmwiki.domain.typed_evidence import EvidenceRecordSet


def build_compiler_source_manifest(
    *,
    page_id: str,
    source_locator: str,
    today: str,
    source_map: NormalizedSourceMap,
    structure_report: SourceStructureIntegrityReport,
    source_record_plan: SourceRecordPlan,
    source_profile: SourceProfileArtifact,
    record_set: EvidenceRecordSet,
    candidate_admission: CandidateAdmissionReport,
    article_viability: ArticleViabilityReport,
    publication_plan: PagePublicationPlan,
    evidence_pack_set: EvidencePackSet,
    article_lint_artifact: ArticleLintArtifact,
    diagnostics: DiagnosticQuestionSet,
    diagnostic_report: DiagnosticReport,
    repair_run: RepairRun,
    article_write_queue_run: ArticleWriteQueueRun,
    linked_pages: tuple[WikiPage, ...],
    compiler_findings: tuple[CompilerFinding, ...],
) -> WikiPage:
    title = source_locator.rsplit(".", 1)[0].replace("-", " ").replace("_", " ").title()
    metadata = PageMetadata(
        page_id=page_id,
        page_kind="source",
        page_family="source-manifest",
        summary=f"{title}: compiler source manifest from raw/{source_locator}.",
        sources=(f"raw/{source_locator}",),
        updated=today,
        domain=page_id,
        category_path=f"sources/{page_id}",
        source_id=source_locator,
        projection_coverage_pointer=f"ingest-compiler:{source_map.source_hash}",
    )
    body = _body(
        title,
        source_locator,
        source_map,
        structure_report,
        source_record_plan,
        source_profile,
        record_set,
        candidate_admission,
        article_viability,
        publication_plan,
        evidence_pack_set,
        article_lint_artifact,
        diagnostics,
        diagnostic_report,
        repair_run,
        article_write_queue_run,
        linked_pages,
        compiler_findings,
    )
    return WikiPage.from_metadata(metadata, body)


def _body(
    title: str,
    source_locator: str,
    source_map: NormalizedSourceMap,
    structure_report: SourceStructureIntegrityReport,
    source_record_plan: SourceRecordPlan,
    source_profile: SourceProfileArtifact,
    record_set: EvidenceRecordSet,
    candidate_admission: CandidateAdmissionReport,
    article_viability: ArticleViabilityReport,
    publication_plan: PagePublicationPlan,
    evidence_pack_set: EvidencePackSet,
    article_lint_artifact: ArticleLintArtifact,
    diagnostics: DiagnosticQuestionSet,
    diagnostic_report: DiagnosticReport,
    repair_run: RepairRun,
    article_write_queue_run: ArticleWriteQueueRun,
    linked_pages: tuple[WikiPage, ...],
    compiler_findings: tuple[CompilerFinding, ...],
) -> str:
    lines = [
        f"# {title}",
        "",
        f"Source: raw/{source_locator}",
        "",
        "## Compiler Summary",
        "",
        f"- Source blocks: {len(source_map.source_blocks)}",
        f"- Source structure findings: {len(structure_report.findings)}",
        f"- Source records: {source_record_plan.record_count}",
        f"- Source profile: {source_profile.source_profile.profile_id} "
        f"({source_profile.source_profile.confidence:.2f})",
        f"- Typed evidence: {len(record_set.accepted_records)} accepted records",
        f"- Candidate admission: {len(candidate_admission.accepted_candidate_ids)} accepted, "
        f"{len(candidate_admission.rejected_candidate_ids)} rejected",
        f"- Article viability: {len(article_viability.accepted_candidate_ids)} accepted, "
        f"{len(article_viability.rejected_candidate_ids)} rejected",
        f"- Publication budget: {len(publication_plan.accepted_candidates)} accepted, "
        f"{len(publication_plan.rejected_candidates)} rejected candidates",
        f"- Evidence packs: {len(evidence_pack_set.packs)} valid, "
        f"{evidence_pack_set.missing_pack_count} missing/invalid",
        f"- Article production: {len(article_write_queue_run.accepted_page_ids)}/"
        f"{article_write_queue_run.policy.max_public_articles} accepted after "
        f"{len(article_write_queue_run.attempted_page_ids)} attempt(s); "
        f"acceptance rate {article_write_queue_run.acceptance_rate:.2f}; "
        f"stop {article_write_queue_run.exhausted_reason}; "
        f"{len(article_write_queue_run.skipped_page_ids)} skipped; "
        f"skip reasons {_skip_reason_counts_text(article_write_queue_run)}; "
        f"families {_family_counts_text(article_write_queue_run.family_counts)}",
        f"- Article lint gates: {article_lint_artifact.accepted_count} accepted, "
        f"{article_lint_artifact.blocked_count} blocked",
        f"- Required evidence coverage: "
        f"{article_lint_artifact.covered_required_evidence_count}/"
        f"{article_lint_artifact.required_evidence_count} "
        f"({article_lint_artifact.required_evidence_coverage_ratio:.2f}); "
        f"{article_lint_artifact.uncovered_required_evidence_count} uncovered",
        f"- Diagnostic questions: {len(diagnostics.questions)}; "
        f"{diagnostic_report.missing_count} missing, "
        f"{diagnostic_report.unsupported_count} unsupported",
        f"- Repair run: {repair_run.status}; {len(repair_run.changed_page_ids)} page(s) changed",
        f"- Compiler findings: {len(compiler_findings)}",
        "",
        "## Accepted Pages",
        "",
    ]
    if linked_pages:
        lines.extend(f"- [[{page.page_id}]] - {page.summary}" for page in linked_pages)
    else:
        lines.append("- No generated article pages were accepted for publication.")
    lines.extend(["", "## Rejected Candidates", ""])
    if publication_plan.rejected_candidates:
        lines.extend(
            f"- {candidate.title} ({candidate.page_family}): {candidate.rejection_code}"
            for candidate in publication_plan.rejected_candidates[:20]
        )
    else:
        lines.append("- No publication candidates were rejected.")
    if compiler_findings:
        lines.extend(["", "## Compiler Findings", ""])
        lines.extend(
            f"- {finding.stage_name}: {finding.finding_code} - {finding.message}"
            for finding in compiler_findings[:20]
        )
    return "\n".join(lines).rstrip() + "\n"


def _family_counts_text(family_counts: tuple[tuple[str, int], ...]) -> str:
    if not family_counts:
        return "none"
    return ", ".join(f"{family}={count}" for family, count in family_counts)


def _skip_reason_counts_text(article_write_queue_run: ArticleWriteQueueRun) -> str:
    skipped = set(article_write_queue_run.skipped_page_ids)
    counts: dict[str, int] = {}
    for finding in article_write_queue_run.findings:
        if finding.page_id in skipped:
            counts[finding.finding_code] = counts.get(finding.finding_code, 0) + 1
    if not counts:
        return "none"
    return ", ".join(f"{code}={count}" for code, count in sorted(counts.items()))
