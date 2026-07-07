"""Pre-publish diagnostic answering, judging, and repair orchestration."""

from __future__ import annotations

from dataclasses import dataclass

from llmwiki.domain.diagnostic_contracts import (
    DiagnosticAnswerer,
    DiagnosticAnswerSet,
    DiagnosticFinding,
    DiagnosticFindingSet,
    DiagnosticJudge,
    DiagnosticQuestionSet,
    DiagnosticReport,
    RepairRun,
    RepairTaskSet,
)
from llmwiki.domain.diagnostic_defaults import CorpusDiagnosticAnswerer, EvidenceDiagnosticJudge
from llmwiki.domain.diagnostics import (
    answer_diagnostic_questions,
    build_diagnostic_question_set,
    build_diagnostic_report,
    build_repair_run,
    build_repair_task_set,
    diagnostic_answer_corpus_from_pages,
    judge_diagnostic_answers,
)
from llmwiki.domain.ledger.article_lint_artifacts import (
    ArticleLintArtifact,
    build_article_lint_artifact,
)
from llmwiki.domain.ledger.evidence_pack import EvidencePack, EvidencePackSet
from llmwiki.domain.ledger.human_article import (
    ArticleFinding,
    ArticleWriter,
    HumanArticleOutput,
    RejectingArticleWriter,
)
from llmwiki.domain.ledger.human_article_artifacts import (
    build_human_article_artifact,
    build_human_article_findings_artifact,
)
from llmwiki.domain.ledger.page_publication import PagePublicationPlan
from llmwiki.domain.pages import WikiPage
from llmwiki.runtime.ledger_human_article_pages import (
    HumanArticleLinkedPages,
    article_metadata,
    write_human_article_page,
)


@dataclass(frozen=True)
class DiagnosticRepairLoopResult:
    question_set: DiagnosticQuestionSet
    answer_set: DiagnosticAnswerSet
    finding_set: DiagnosticFindingSet
    report: DiagnosticReport
    task_set: RepairTaskSet
    repair_run: RepairRun
    initial_human_articles: HumanArticleLinkedPages
    initial_article_lint: ArticleLintArtifact
    final_human_articles: HumanArticleLinkedPages
    final_article_lint: ArticleLintArtifact


def run_diagnostic_repair_loop(
    *,
    source_locator: str,
    source_id: str,
    source_hash: str,
    today: str,
    publication_plan: PagePublicationPlan,
    pack_set: EvidencePackSet,
    initial_human_articles: HumanArticleLinkedPages,
    initial_article_lint: ArticleLintArtifact,
    article_writer: ArticleWriter | None,
    diagnostic_answerer: DiagnosticAnswerer | None = None,
    diagnostic_judge: DiagnosticJudge | None = None,
) -> DiagnosticRepairLoopResult:
    answerer = diagnostic_answerer or CorpusDiagnosticAnswerer()
    judge = diagnostic_judge or EvidenceDiagnosticJudge()
    question_set = build_diagnostic_question_set(
        source_id=source_id,
        source_hash=source_hash,
        pack_set=pack_set,
        publication_plan=publication_plan,
        page_ids=frozenset(page.page_id for page in initial_human_articles.pages),
    )
    corpus = diagnostic_answer_corpus_from_pages(initial_human_articles.pages)
    answer_set = answer_diagnostic_questions(question_set, corpus, answerer)
    finding_set = judge_diagnostic_answers(question_set, answer_set, pack_set, judge)
    task_set = build_repair_task_set(finding_set)
    final_articles, repair_run = _repair_articles(
        source_locator=source_locator,
        source_id=source_id,
        source_hash=source_hash,
        today=today,
        pack_set=pack_set,
        initial=initial_human_articles,
        task_set=task_set,
        findings=finding_set.blocking_findings,
        article_writer=article_writer,
    )
    final_lint = build_article_lint_artifact(
        source_hash=source_hash,
        runs=final_articles.article_lint_runs,
    )
    report = build_diagnostic_report(
        question_set,
        answer_set,
        finding_set,
        repaired_count=len(repair_run.changed_page_ids),
    )
    return DiagnosticRepairLoopResult(
        question_set,
        answer_set,
        finding_set,
        report,
        task_set,
        repair_run,
        initial_human_articles,
        initial_article_lint,
        final_articles,
        final_lint,
    )


def diagnostic_article_artifacts(
    result: DiagnosticRepairLoopResult, source_hash: str
) -> dict[str, object]:
    return {
        "human-article-initial": build_human_article_artifact(
            source_hash=source_hash,
            records=result.initial_human_articles.article_output.records,
        ),
        "human-article-findings-initial": build_human_article_findings_artifact(
            source_hash=source_hash,
            findings=result.initial_human_articles.article_output.findings,
        ),
        "article-lint-runs-initial": result.initial_article_lint,
        "human-article": build_human_article_artifact(
            source_hash=source_hash,
            records=result.final_human_articles.article_output.records,
        ),
        "human-article-findings": build_human_article_findings_artifact(
            source_hash=source_hash,
            findings=result.final_human_articles.article_output.findings,
        ),
        "article-lint-runs": result.final_article_lint,
    }


def _repair_articles(
    *,
    source_locator: str,
    source_id: str,
    source_hash: str,
    today: str,
    pack_set: EvidencePackSet,
    initial: HumanArticleLinkedPages,
    task_set: RepairTaskSet,
    findings: tuple[DiagnosticFinding, ...],
    article_writer: ArticleWriter | None,
) -> tuple[HumanArticleLinkedPages, RepairRun]:
    pages = {page.page_id: page for page in initial.pages}
    records = {record.article.page_id: record for record in initial.article_output.records}
    lint_runs = {run.page_id: run for run in initial.article_lint_runs}
    article_findings = list(initial.article_output.findings)
    changed: list[str] = []
    rejected: list[str] = []
    writer = article_writer or RejectingArticleWriter()
    packs = {pack.page_id: pack for pack in pack_set.packs}
    findings_by_page = _findings_by_page(findings)
    for task in task_set.tasks:
        pack = packs.get(task.target_page_id)
        if pack is None or task.repair_kind != "rewrite-human-article":
            rejected.append(task.target_page_id)
            continue
        attempt = write_human_article_page(
            pack,
            article_metadata(pack, source_locator, today),
            writer,
            max_attempts=1,
            initial_findings=_article_findings(pack, findings_by_page.get(pack.page_id, ())),
        )
        if attempt.lint_run is not None:
            lint_runs[pack.page_id] = attempt.lint_run
        if attempt.page is None or attempt.record is None:
            article_findings.extend(attempt.findings)
            rejected.append(pack.page_id)
            continue
        pages[pack.page_id] = attempt.page
        records[pack.page_id] = attempt.record
        changed.append(pack.page_id)
    final = HumanArticleLinkedPages(
        pages=tuple(_ordered_pages(initial.pages, pages)),
        collection_plans=initial.collection_plans,
        article_output=HumanArticleOutput(tuple(records.values()), tuple(article_findings)),
        article_lint_runs=tuple(lint_runs.values()),
    )
    repair_run = build_repair_run(
        source_id=source_id,
        source_hash=source_hash,
        task_set=task_set,
        changed_page_ids=tuple(dict.fromkeys(changed)),
        accepted_page_ids=tuple(page.page_id for page in final.pages),
        rejected_page_ids=tuple(dict.fromkeys(rejected)),
        article_lint_run_ids=tuple(run.article_lint_run_id for run in final.article_lint_runs),
    )
    return final, repair_run


def _findings_by_page(
    findings: tuple[DiagnosticFinding, ...]
) -> dict[str, tuple[DiagnosticFinding, ...]]:
    grouped: dict[str, list[DiagnosticFinding]] = {}
    for finding in findings:
        grouped.setdefault(finding.page_id, []).append(finding)
    return {page_id: tuple(items) for page_id, items in grouped.items()}


def _article_findings(
    pack: EvidencePack, findings: tuple[DiagnosticFinding, ...]
) -> tuple[ArticleFinding, ...]:
    return tuple(
        ArticleFinding(
            "blocking",
            finding.finding_code,
            pack.page_id,
            finding.message,
            support_ref=finding.support_ref,
        )
        for finding in findings
    )


def _ordered_pages(
    existing: tuple[WikiPage, ...], pages: dict[str, WikiPage]
) -> tuple[WikiPage, ...]:
    ordered = [pages[page.page_id] for page in existing if page.page_id in pages]
    existing_ids = {page.page_id for page in existing}
    ordered.extend(
        page for page_id, page in pages.items() if page_id not in existing_ids
    )
    return tuple(ordered)
