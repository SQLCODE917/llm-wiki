"""Render source manifest pages from compiler artifacts."""

from __future__ import annotations

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
    publication_plan: PagePublicationPlan,
    evidence_pack_set: EvidencePackSet,
    article_lint_artifact: ArticleLintArtifact,
    diagnostics: DiagnosticQuestionSet,
    diagnostic_report: DiagnosticReport,
    repair_run: RepairRun,
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
        publication_plan,
        evidence_pack_set,
        article_lint_artifact,
        diagnostics,
        diagnostic_report,
        repair_run,
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
    publication_plan: PagePublicationPlan,
    evidence_pack_set: EvidencePackSet,
    article_lint_artifact: ArticleLintArtifact,
    diagnostics: DiagnosticQuestionSet,
    diagnostic_report: DiagnosticReport,
    repair_run: RepairRun,
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
        f"- Publication budget: {len(publication_plan.accepted_candidates)} accepted, "
        f"{len(publication_plan.rejected_candidates)} rejected candidates",
        f"- Evidence packs: {len(evidence_pack_set.packs)} valid, "
        f"{evidence_pack_set.missing_pack_count} missing/invalid",
        f"- Article lint gates: {article_lint_artifact.accepted_count} accepted, "
        f"{article_lint_artifact.blocked_count} blocked",
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
