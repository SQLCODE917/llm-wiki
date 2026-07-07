"""Single source ingest compiler runtime."""

from __future__ import annotations

import hashlib
from collections.abc import Callable
from dataclasses import dataclass
from pathlib import Path

from llmwiki.domain.compiler_candidate_admission import (
    CandidateAdmissionFinding,
    admit_compiler_page_candidates,
)
from llmwiki.domain.diagnostic_contracts import DiagnosticAnswerer, DiagnosticJudge
from llmwiki.domain.diagnostics import render_diagnostic_report
from llmwiki.domain.ingest_compiler import (
    CompilerFinding,
    CompilerStage,
    IngestCompilation,
    IngestCompilerInput,
    build_ingest_artifact_set,
)
from llmwiki.domain.ledger.article_lint_artifacts import build_article_lint_artifact
from llmwiki.domain.ledger.canonical import canonical_json, deterministic_id, short_digest
from llmwiki.domain.ledger.evidence_pack import build_evidence_pack_set
from llmwiki.domain.ledger.human_article import ArticleWriter
from llmwiki.domain.ledger.page_publication import conservative_publication_budget
from llmwiki.domain.ledger.page_publication_planning import (
    plan_publication,
    publication_walkability_report,
    render_publication_walkability_report,
)
from llmwiki.domain.ledger.staged_flow import (
    accepted_pages,
    build_lint_run,
    build_publish_run,
    build_source_plan,
    build_staged_page_set,
)
from llmwiki.domain.pages import slugify
from llmwiki.domain.source_map import NormalizedSourceMap
from llmwiki.domain.source_profile_io import (
    evidence_extraction_plan_to_json,
    source_profile_artifact_to_json,
)
from llmwiki.domain.source_profile_selector import select_source_profile
from llmwiki.domain.source_profiles import build_evidence_extraction_plan
from llmwiki.domain.source_records import build_source_record_plan
from llmwiki.domain.source_structure_integrity import build_source_structure_integrity_report
from llmwiki.domain.typed_evidence_io import evidence_record_set_to_json
from llmwiki.domain.typed_evidence_producer import DeterministicTypedEvidenceProducer
from llmwiki.pdf.pipeline import ExtractionResult, read_source_map, save_manifest
from llmwiki.runtime.compiler_page_candidates import build_compiler_page_candidates
from llmwiki.runtime.compiler_source_manifest import build_compiler_source_manifest
from llmwiki.runtime.diagnostic_repair_loop import (
    diagnostic_article_artifacts,
    run_diagnostic_repair_loop,
)
from llmwiki.runtime.ingest_compiler_artifacts import compiler_artifact_files
from llmwiki.runtime.ingest_compiler_reporting import (
    compiler_findings,
    compiler_report,
    rejected_page_ids,
)
from llmwiki.runtime.ledger_human_article_pages import build_human_article_linked_pages
from llmwiki.runtime.markdown_source_map import markdown_source_map
from llmwiki.store import WikiStore

_INITIAL_ARTICLE_PACK_BUDGET = 3


@dataclass(frozen=True)
class IngestCompiler:
    store: WikiStore
    today: str
    run_id: str
    extract_pdf: Callable[[Path, str, bool], ExtractionResult] | None = None
    article_writer: ArticleWriter | None = None
    diagnostic_answerer: DiagnosticAnswerer | None = None
    diagnostic_judge: DiagnosticJudge | None = None

    def compile(self, compiler_input: IngestCompilerInput) -> IngestCompilation:
        source_locator = compiler_input.source_locator
        source_page_id = slugify(source_locator.rsplit(".", 1)[0])
        source_map = self._source_map(source_locator, compiler_input.reextract)
        if source_map is None:
            return self._blocked_missing_source_map(source_locator, source_page_id)
        structure_report = build_source_structure_integrity_report(source_map)
        source_record_plan = build_source_record_plan(source_map)
        source_profile = select_source_profile(source_map)
        evidence_plan = build_evidence_extraction_plan(
            source_map,
            source_profile.source_profile,
            source_profile.evidence_vocabulary,
        )
        record_set = DeterministicTypedEvidenceProducer().build_record_set(
            source_map,
            source_profile,
            evidence_plan,
        )
        candidate_inputs = build_compiler_page_candidates(
            source_page_id=source_page_id,
            source_map=source_map,
            record_set=record_set,
            source_profile_kind=source_profile.source_profile.profile_id,
        )
        admission = admit_compiler_page_candidates(
            source_id=source_page_id,
            source_hash=source_map.source_hash,
            candidates=candidate_inputs.candidates,
            record_set=record_set,
            structure_report=structure_report,
            record_plan=source_record_plan,
        )
        budget = conservative_publication_budget(source_profile.source_profile.profile_id)
        publication_plan = plan_publication(
            source_id=source_page_id,
            source_hash=source_map.source_hash,
            source_profile_kind=budget.source_profile_kind,
            budget=budget,
            candidates=admission.accepted_candidates,
        )
        publication_report = publication_walkability_report(publication_plan)
        pack_set = build_evidence_pack_set(
            publication_plan=publication_plan,
            evidence_record_set=record_set,
            source_map=source_map,
        )
        initial_human_articles = build_human_article_linked_pages(
            evidence_pack_set=pack_set,
            source_locator=source_locator,
            today=self.today,
            article_writer=self.article_writer,
            max_article_packs=_INITIAL_ARTICLE_PACK_BUDGET,
            max_attempts_per_pack=1,
        )
        initial_article_lint = build_article_lint_artifact(
            source_hash=source_map.source_hash,
            runs=initial_human_articles.article_lint_runs,
        )
        diagnostic_loop = run_diagnostic_repair_loop(
            source_locator=source_locator,
            source_id=source_page_id,
            source_hash=source_map.source_hash,
            today=self.today,
            publication_plan=publication_plan,
            pack_set=pack_set,
            initial_human_articles=initial_human_articles,
            initial_article_lint=initial_article_lint,
            article_writer=self.article_writer,
            diagnostic_answerer=self.diagnostic_answerer,
            diagnostic_judge=self.diagnostic_judge,
        )
        findings = compiler_findings(
            publication_plan,
            pack_set,
            diagnostic_loop.final_human_articles,
            diagnostic_loop.final_article_lint,
            diagnostic_findings=diagnostic_loop.finding_set.findings,
            repair_run=diagnostic_loop.repair_run,
        )
        findings = (*_candidate_admission_findings(admission.report.findings), *findings)
        linked_pages = diagnostic_loop.final_human_articles.pages
        source_page = build_compiler_source_manifest(
            page_id=source_page_id,
            source_locator=source_locator,
            today=self.today,
            source_map=source_map,
            structure_report=structure_report,
            source_record_plan=source_record_plan,
            source_profile=source_profile,
            record_set=record_set,
            candidate_admission=admission.report,
            publication_plan=publication_plan,
            evidence_pack_set=pack_set,
            article_lint_artifact=diagnostic_loop.final_article_lint,
            diagnostics=diagnostic_loop.question_set,
            diagnostic_report=diagnostic_loop.report,
            repair_run=diagnostic_loop.repair_run,
            linked_pages=linked_pages,
            compiler_findings=findings,
        )
        source_plan = build_source_plan(
            source_locator=source_locator,
            source_hash=source_map.source_hash,
            source_page_id=source_page_id,
        )
        staged = build_staged_page_set(source_plan, (source_page, *linked_pages))
        lint_run = build_lint_run(
            source_plan=source_plan,
            staged_page_set=staged,
            upstream_write_decision="ingest-compiler",
        )
        publish_run = build_publish_run(source_plan, staged, lint_run)
        published = accepted_pages(staged, publish_run)
        article_artifacts = diagnostic_article_artifacts(
            diagnostic_loop, source_map.source_hash
        )
        artifact_files, artifact_set = compiler_artifact_files(
            source_locator=source_locator,
            source_page_id=source_page_id,
            source_hash=source_map.source_hash,
            run_id=self.run_id or self.today,
            source_map=source_map,
            payloads={
                "source-profile.json": source_profile_artifact_to_json(source_profile),
                "source-structure-integrity.json": canonical_json(
                    structure_report, indent=2
                ),
                "source-record-plan.json": canonical_json(source_record_plan, indent=2),
                "evidence-extraction-plan.json": evidence_extraction_plan_to_json(
                    evidence_plan
                ),
                "evidence-record-set.json": evidence_record_set_to_json(record_set),
                "candidate-admission-report.json": canonical_json(
                    admission.report, indent=2
                ),
                "page-publication-plan.json": canonical_json(publication_plan, indent=2),
                "publication-walkability-report.md": render_publication_walkability_report(
                    publication_report
                ),
                "evidence-pack-set.json": canonical_json(pack_set, indent=2),
                "human-article-initial.json": canonical_json(
                    article_artifacts["human-article-initial"], indent=2
                ),
                "human-article-findings-initial.json": canonical_json(
                    article_artifacts["human-article-findings-initial"], indent=2
                ),
                "article-lint-runs-initial.json": canonical_json(
                    article_artifacts["article-lint-runs-initial"], indent=2
                ),
                "human-article.json": canonical_json(
                    article_artifacts["human-article"], indent=2
                ),
                "human-article-findings.json": canonical_json(
                    article_artifacts["human-article-findings"], indent=2
                ),
                "article-lint-runs.json": canonical_json(
                    article_artifacts["article-lint-runs"], indent=2
                ),
                "diagnostic-question-set.json": canonical_json(
                    diagnostic_loop.question_set, indent=2
                ),
                "diagnostic-answer-set.json": canonical_json(
                    diagnostic_loop.answer_set, indent=2
                ),
                "diagnostic-finding-set.json": canonical_json(
                    diagnostic_loop.finding_set, indent=2
                ),
                "diagnostics-report.md": render_diagnostic_report(diagnostic_loop.report),
                "repair-task-set.json": canonical_json(diagnostic_loop.task_set, indent=2),
                "repair-run.json": canonical_json(diagnostic_loop.repair_run, indent=2),
                "source-plan.json": canonical_json(source_plan, indent=2),
                "staged-pages.json": canonical_json(staged, indent=2),
                "lint-run.json": canonical_json(lint_run, indent=2),
                "publish-run.json": canonical_json(publish_run, indent=2),
            },
            findings=findings,
            accepted_page_ids=tuple(page.page_id for page in published),
            rejected_page_ids=tuple(
                dict.fromkeys((*rejected_page_ids(findings), *publish_run.rejected_page_ids))
            ),
        )
        return IngestCompilation(
            source_locator=source_locator,
            source_page_id=source_page_id,
            source_hash=source_map.source_hash,
            accepted_pages=published,
            artifact_files=artifact_files,
            artifact_set=artifact_set,
            report=compiler_report(
                source_locator,
                artifact_set,
                findings,
                diagnostic_report=diagnostic_loop.report,
                repair_run=diagnostic_loop.repair_run,
            ),
        )

    def _source_map(
        self, source_locator: str, reextract: bool
    ) -> NormalizedSourceMap | None:
        if not source_locator.lower().endswith(".pdf"):
            return markdown_source_map(source_locator, self.store.read_source(source_locator))
        if self.extract_pdf is None or not callable(self.extract_pdf):
            return None
        result = self.extract_pdf(
            self.store.raw_source_path(source_locator),
            source_locator,
            reextract,
        )
        source_map = read_source_map(result.cache_dir)
        if source_map is not None:
            save_manifest(ExtractionResult(result.manifest.mark_integrated(), result.cache_dir))
        return source_map

    def _blocked_missing_source_map(
        self, source_locator: str, source_page_id: str
    ) -> IngestCompilation:
        source_hash = _raw_hash(self.store.raw_source_path(source_locator))
        finding = CompilerFinding(
            deterministic_id("compiler-finding", source_hash, "source-map-missing"),
            "source-map",
            "blocking",
            "source-map-missing",
            source_page_id,
            "",
            "NormalizedSourceMap could not be built or loaded.",
        )
        stages = (CompilerStage("source-map", (), (), "blocked", 0, 1),)
        artifact_set = build_ingest_artifact_set(
            source_id=source_page_id,
            source_locator=source_locator,
            source_hash=source_hash,
            run_id=self.run_id or self.today,
            stages=stages,
            artifacts=(),
            findings=(finding,),
            accepted_page_ids=(),
            rejected_page_ids=(source_page_id,),
        )
        files = {"ingest-artifact-set.json": canonical_json(artifact_set, indent=2)}
        return IngestCompilation(
            source_locator,
            source_page_id,
            source_hash,
            (),
            files,
            artifact_set,
            compiler_report(source_locator, artifact_set, (finding,)),
        )


def _candidate_admission_findings(
    findings: tuple[CandidateAdmissionFinding, ...],
) -> tuple[CompilerFinding, ...]:
    converted: list[CompilerFinding] = []
    for finding in findings:
        converted.append(
            CompilerFinding(
                finding_id=deterministic_id(
                    "compiler-finding",
                    "page-plan",
                    finding.finding_code,
                    finding.page_id,
                ),
                stage_name="page-plan",
                severity=finding.severity,
                finding_code=finding.finding_code,
                page_id=finding.page_id,
                source_anchor="",
                message=finding.message,
            )
        )
    return tuple(converted)


def _raw_hash(path: Path) -> str:
    if not path.is_file():
        return short_digest(str(path), 64)
    return hashlib.sha256(path.read_bytes()).hexdigest()
