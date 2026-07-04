"""Diagnostic question, answer, judging, and repair services."""

from __future__ import annotations

import re
from dataclasses import replace

from llmwiki.domain.diagnostic_contracts import (
    DiagnosticAnswer,
    DiagnosticAnswerCorpus,
    DiagnosticAnswerer,
    DiagnosticAnswerSet,
    DiagnosticCorpusPage,
    DiagnosticFinding,
    DiagnosticFindingSet,
    DiagnosticJudge,
    DiagnosticQuestion,
    DiagnosticQuestionSet,
    DiagnosticReport,
    RepairRun,
    RepairTask,
    RepairTaskSet,
)
from llmwiki.domain.ledger.canonical import artifact_fingerprint, deterministic_id
from llmwiki.domain.ledger.evidence_pack import EvidencePack, EvidencePackSet
from llmwiki.domain.ledger.page_publication import PagePublicationPlan
from llmwiki.domain.ledger.vocab import ARTIFACT_FORMAT
from llmwiki.domain.pages import WikiPage


def diagnostic_answer_corpus_from_pages(pages: tuple[WikiPage, ...]) -> DiagnosticAnswerCorpus:
    return DiagnosticAnswerCorpus(
        tuple(DiagnosticCorpusPage(page.page_id, page.summary, page.page_body) for page in pages)
    )


def build_diagnostic_question_set(
    *,
    source_id: str,
    source_hash: str,
    pack_set: EvidencePackSet,
    publication_plan: PagePublicationPlan,
) -> DiagnosticQuestionSet:
    accepted = set(publication_plan.accepted_page_ids)
    questions = tuple(
        _question_for_pack(source_id, source_hash, pack)
        for pack in pack_set.packs
        if pack.page_id in accepted
    )
    draft = DiagnosticQuestionSet(
        deterministic_id("diagnostic-question-set", source_hash, source_id),
        "",
        ARTIFACT_FORMAT,
        source_id,
        source_hash,
        questions,
    )
    fingerprint = artifact_fingerprint(
        draft, exclude=("diagnostic_question_set_fingerprint",)
    )
    return replace(draft, diagnostic_question_set_fingerprint=fingerprint)


def answer_diagnostic_questions(
    question_set: DiagnosticQuestionSet,
    corpus: DiagnosticAnswerCorpus,
    answerer: DiagnosticAnswerer,
) -> DiagnosticAnswerSet:
    draft = DiagnosticAnswerSet(
        deterministic_id("diagnostic-answer-set", question_set.source_hash, question_set.source_id),
        "",
        ARTIFACT_FORMAT,
        question_set.source_id,
        question_set.source_hash,
        tuple(
            answerer.answer_diagnostic_question(question, corpus)
            for question in question_set.questions
        ),
    )
    fingerprint = artifact_fingerprint(draft, exclude=("diagnostic_answer_set_fingerprint",))
    return replace(draft, diagnostic_answer_set_fingerprint=fingerprint)


def judge_diagnostic_answers(
    question_set: DiagnosticQuestionSet,
    answer_set: DiagnosticAnswerSet,
    pack_set: EvidencePackSet,
    judge: DiagnosticJudge,
) -> DiagnosticFindingSet:
    answers = {answer.diagnostic_question_id: answer for answer in answer_set.answers}
    packs = {pack.page_id: pack for pack in pack_set.packs}
    findings = tuple(
        finding
        for question in question_set.questions
        for finding in judge.judge_diagnostic_answer(
            question,
            answers.get(question.diagnostic_question_id, _missing_answer(question)),
            _pack(question, packs),
        )
    )
    finding_set_id = deterministic_id(
        "diagnostic-finding-set",
        question_set.source_hash,
        question_set.source_id,
    )
    draft = DiagnosticFindingSet(
        finding_set_id,
        "",
        ARTIFACT_FORMAT,
        question_set.source_id,
        question_set.source_hash,
        findings,
    )
    fingerprint = artifact_fingerprint(
        draft, exclude=("diagnostic_finding_set_fingerprint",)
    )
    return replace(draft, diagnostic_finding_set_fingerprint=fingerprint)


def build_repair_task_set(
    finding_set: DiagnosticFindingSet, *, max_tasks: int = 4
) -> RepairTaskSet:
    grouped: dict[str, list[DiagnosticFinding]] = {}
    for finding in finding_set.blocking_findings:
        if finding.finding_code not in _REPAIRABLE_CODES:
            continue
        grouped.setdefault(finding.page_id, []).append(finding)
    tasks = tuple(
        _repair_task(page_id, findings)
        for page_id, findings in list(grouped.items())[:max_tasks]
    )
    draft = RepairTaskSet(
        deterministic_id("repair-task-set", finding_set.source_hash, finding_set.source_id),
        "",
        ARTIFACT_FORMAT,
        finding_set.source_id,
        finding_set.source_hash,
        tasks,
    )
    fingerprint = artifact_fingerprint(
        draft,
        exclude=("repair_task_set_fingerprint",),
    )
    return replace(draft, repair_task_set_fingerprint=fingerprint)


def build_diagnostic_report(
    question_set: DiagnosticQuestionSet,
    answer_set: DiagnosticAnswerSet,
    finding_set: DiagnosticFindingSet,
    *,
    repaired_count: int = 0,
) -> DiagnosticReport:
    codes = [finding.finding_code for finding in finding_set.findings]
    return DiagnosticReport(
        source_id=question_set.source_id,
        question_count=len(question_set.questions),
        answered_count=answer_set.answered_count,
        missing_count=codes.count("missing-answer"),
        unsupported_count=codes.count("unsupported-answer"),
        incoherent_count=codes.count("incoherent-answer"),
        repaired_count=repaired_count,
    )


def render_diagnostic_report(report: DiagnosticReport) -> str:
    return (
        "# Diagnostics Report\n\n"
        f"- Source: `{report.source_id}`\n"
        f"- Questions: {report.question_count}\n"
        f"- Answered: {report.answered_count}\n"
        f"- Missing: {report.missing_count}\n"
        f"- Unsupported: {report.unsupported_count}\n"
        f"- Incoherent: {report.incoherent_count}\n"
        f"- Repaired: {report.repaired_count}\n"
    )


def build_repair_run(
    *,
    source_id: str,
    source_hash: str,
    task_set: RepairTaskSet,
    changed_page_ids: tuple[str, ...],
    accepted_page_ids: tuple[str, ...],
    rejected_page_ids: tuple[str, ...],
    article_lint_run_ids: tuple[str, ...],
) -> RepairRun:
    status = "skipped" if not task_set.tasks else "completed"
    if rejected_page_ids:
        status = "partial" if changed_page_ids else "blocked"
    draft = RepairRun(
        deterministic_id(
            "repair-run",
            source_hash,
            source_id,
            ",".join(t.repair_task_id for t in task_set.tasks),
        ),
        "",
        ARTIFACT_FORMAT,
        source_id,
        source_hash,
        tuple(task.repair_task_id for task in task_set.tasks),
        changed_page_ids,
        accepted_page_ids,
        rejected_page_ids,
        article_lint_run_ids,
        status,
    )
    fingerprint = artifact_fingerprint(
        draft,
        exclude=("repair_run_fingerprint",),
    )
    return replace(draft, repair_run_fingerprint=fingerprint)


_REPAIRABLE_CODES = {"missing-answer", "unsupported-answer", "incoherent-answer", "missing-page"}
_INTERACTION_RE = re.compile(r"\b(?:interacts?|enters?|comes? into|opponent|will-o-wisp)\b", re.I)


def _question_for_pack(source_id: str, source_hash: str, pack: EvidencePack) -> DiagnosticQuestion:
    refs = tuple(item.support_ref.code for item in pack.items[:3])
    anchors = tuple(
        anchor.text_fingerprint
        for item in pack.items[:3]
        for anchor in item.source_anchors[:1]
        if anchor.text_fingerprint
    )
    text = _question_text(pack)
    return DiagnosticQuestion(
        deterministic_id("diagnostic-question", source_hash, pack.page_id, text, ",".join(refs)),
        source_id,
        (pack.page_id,),
        anchors,
        refs,
        text,
        _question_purpose(pack),
    )


def _question_text(pack: EvidencePack) -> str:
    evidence = " ".join(f"{item.source_text} {item.payload_text}" for item in pack.items)
    if "will-o-wisp" in evidence.casefold() and "shade" in pack.title.casefold():
        return "How does Shade interact with will-o-wisp?"
    if _INTERACTION_RE.search(evidence):
        return f"What interactions or conditions matter for {pack.title}?"
    if pack.page_family == "procedure-guide":
        return f"How does a reader perform {pack.title}?"
    if pack.page_family == "recipe-pattern":
        return f"How does the {pack.title} recipe work, and what code evidence supports it?"
    return f"What should a reader understand about {pack.title}?"


def _question_purpose(pack: EvidencePack) -> str:
    return {
        "procedure-guide": "procedure-walkability",
        "recipe-pattern": "recipe-code-walkability",
    }.get(pack.page_family, "accepted-page-coverage")


def _missing_answer(question: DiagnosticQuestion) -> DiagnosticAnswer:
    return DiagnosticAnswer(question.diagnostic_question_id, "", ())


def _pack(question: DiagnosticQuestion, packs: dict[str, EvidencePack]) -> EvidencePack | None:
    return next((packs.get(page_id) for page_id in question.page_ids if page_id in packs), None)


def _repair_task(page_id: str, findings: list[DiagnosticFinding]) -> RepairTask:
    support = tuple(dict.fromkeys(f.support_ref for f in findings if f.support_ref))
    finding_ids = tuple(f.diagnostic_finding_id for f in findings)
    return RepairTask(
        deterministic_id("repair-task", page_id, ",".join(finding_ids), ",".join(support)),
        finding_ids,
        "rewrite-human-article" if page_id else "review-page-plan",
        page_id,
        support,
        "planned",
    )


def diagnostic_finding(question: DiagnosticQuestion, code: str, message: str) -> DiagnosticFinding:
    support = question.expected_support_refs[0] if question.expected_support_refs else ""
    page_id = question.page_ids[0] if question.page_ids else ""
    return DiagnosticFinding(
        deterministic_id("diagnostic-finding", question.diagnostic_question_id, code, page_id),
        question.diagnostic_question_id,
        "blocking",
        code,
        support,
        page_id,
        message,
    )
