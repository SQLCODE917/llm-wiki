"""Single source ingest compiler runtime."""

from __future__ import annotations

import hashlib
from collections.abc import Callable
from dataclasses import dataclass
from pathlib import Path

from llmwiki.domain.ingest_compiler import (
    CompilerFinding,
    CompilerStage,
    IngestCompilation,
    IngestCompilerInput,
    build_diagnostic_question_set,
    build_ingest_artifact_set,
)
from llmwiki.domain.ledger.article_lint_artifacts import build_article_lint_artifact
from llmwiki.domain.ledger.canonical import canonical_json, deterministic_id, short_digest
from llmwiki.domain.ledger.evidence_pack import build_evidence_pack_set
from llmwiki.domain.ledger.human_article import ArticleWriter
from llmwiki.domain.ledger.human_article_artifacts import (
    build_human_article_artifact,
    build_human_article_findings_artifact,
)
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
from llmwiki.domain.typed_evidence_io import evidence_record_set_to_json
from llmwiki.domain.typed_evidence_producer import DeterministicTypedEvidenceProducer
from llmwiki.pdf.pipeline import ExtractionResult, read_source_map, save_manifest
from llmwiki.runtime.compiler_page_candidates import build_compiler_page_candidates
from llmwiki.runtime.compiler_source_manifest import build_compiler_source_manifest
from llmwiki.runtime.ingest_compiler_artifacts import compiler_artifact_files
from llmwiki.runtime.ingest_compiler_reporting import (
    compiler_findings,
    compiler_report,
    rejected_page_ids,
)
from llmwiki.runtime.ledger_human_article_pages import build_human_article_linked_pages
from llmwiki.runtime.markdown_source_map import markdown_source_map
from llmwiki.store import WikiStore


@dataclass(frozen=True)
class IngestCompiler:
    store: WikiStore
    today: str
    run_id: str
    extract_pdf: Callable[[Path, str, bool], ExtractionResult] | None = None
    article_writer: ArticleWriter | None = None

    def compile(self, compiler_input: IngestCompilerInput) -> IngestCompilation:
        source_locator = compiler_input.source_locator
        source_page_id = slugify(source_locator.rsplit(".", 1)[0])
        source_map = self._source_map(source_locator, compiler_input.reextract)
        if source_map is None:
            return self._blocked_missing_source_map(source_locator, source_page_id)
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
        budget = conservative_publication_budget(source_profile.source_profile.profile_id)
        publication_plan = plan_publication(
            source_id=source_page_id,
            source_hash=source_map.source_hash,
            source_profile_kind=budget.source_profile_kind,
            budget=budget,
            candidates=candidate_inputs.candidates,
        )
        publication_report = publication_walkability_report(publication_plan)
        pack_set = build_evidence_pack_set(
            publication_plan=publication_plan,
            evidence_record_set=record_set,
            source_map=source_map,
        )
        human_articles = build_human_article_linked_pages(
            evidence_pack_set=pack_set,
            source_locator=source_locator,
            today=self.today,
            article_writer=self.article_writer,
        )
        article_lint = build_article_lint_artifact(
            source_hash=source_map.source_hash,
            runs=human_articles.article_lint_runs,
        )
        diagnostics = build_diagnostic_question_set(
            source_id=source_page_id,
            source_hash=source_map.source_hash,
            packs=pack_set.packs,
        )
        findings = compiler_findings(publication_plan, pack_set, human_articles, article_lint)
        linked_pages = human_articles.pages
        source_page = build_compiler_source_manifest(
            page_id=source_page_id,
            source_locator=source_locator,
            today=self.today,
            source_map=source_map,
            source_profile=source_profile,
            record_set=record_set,
            publication_plan=publication_plan,
            evidence_pack_set=pack_set,
            article_lint_artifact=article_lint,
            diagnostics=diagnostics,
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
        artifact_files, artifact_set = compiler_artifact_files(
            source_locator=source_locator,
            source_page_id=source_page_id,
            source_hash=source_map.source_hash,
            run_id=self.run_id or self.today,
            source_map=source_map,
            payloads={
                "source-profile.json": source_profile_artifact_to_json(source_profile),
                "evidence-extraction-plan.json": evidence_extraction_plan_to_json(
                    evidence_plan
                ),
                "evidence-record-set.json": evidence_record_set_to_json(record_set),
                "page-publication-plan.json": canonical_json(publication_plan, indent=2),
                "publication-walkability-report.md": render_publication_walkability_report(
                    publication_report
                ),
                "evidence-pack-set.json": canonical_json(pack_set, indent=2),
                "human-article.json": canonical_json(
                    build_human_article_artifact(
                        source_hash=source_map.source_hash,
                        records=human_articles.article_output.records,
                    ),
                    indent=2,
                ),
                "human-article-findings.json": canonical_json(
                    build_human_article_findings_artifact(
                        source_hash=source_map.source_hash,
                        findings=human_articles.article_output.findings,
                    ),
                    indent=2,
                ),
                "article-lint-runs.json": canonical_json(article_lint, indent=2),
                "diagnostic-question-set.json": canonical_json(diagnostics, indent=2),
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
            report=compiler_report(source_locator, artifact_set, findings),
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


def _raw_hash(path: Path) -> str:
    if not path.is_file():
        return short_digest(str(path), 64)
    return hashlib.sha256(path.read_bytes()).hexdigest()
