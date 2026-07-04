"""Diagnostic and repair domain contracts."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol

from llmwiki.domain.ledger.evidence_pack import EvidencePack


@dataclass(frozen=True)
class DiagnosticQuestion:
    diagnostic_question_id: str
    source_id: str
    page_ids: tuple[str, ...]
    source_anchors: tuple[str, ...]
    expected_support_refs: tuple[str, ...]
    question_text: str
    purpose: str


@dataclass(frozen=True)
class DiagnosticQuestionSet:
    diagnostic_question_set_id: str
    diagnostic_question_set_fingerprint: str
    artifact_format: str
    source_id: str
    source_hash: str
    questions: tuple[DiagnosticQuestion, ...]


@dataclass(frozen=True)
class DiagnosticAnswer:
    diagnostic_question_id: str
    answer_text: str
    cited_page_ids: tuple[str, ...]
    cited_support_refs: tuple[str, ...] = ()


@dataclass(frozen=True)
class DiagnosticAnswerSet:
    diagnostic_answer_set_id: str
    diagnostic_answer_set_fingerprint: str
    artifact_format: str
    source_id: str
    source_hash: str
    answers: tuple[DiagnosticAnswer, ...]

    @property
    def answered_count(self) -> int:
        return sum(1 for answer in self.answers if answer.answer_text.strip())


@dataclass(frozen=True)
class DiagnosticFinding:
    diagnostic_finding_id: str
    diagnostic_question_id: str
    severity: str
    finding_code: str
    support_ref: str
    page_id: str
    message: str


@dataclass(frozen=True)
class DiagnosticFindingSet:
    diagnostic_finding_set_id: str
    diagnostic_finding_set_fingerprint: str
    artifact_format: str
    source_id: str
    source_hash: str
    findings: tuple[DiagnosticFinding, ...]

    @property
    def blocking_findings(self) -> tuple[DiagnosticFinding, ...]:
        return tuple(finding for finding in self.findings if finding.severity == "blocking")


@dataclass(frozen=True)
class DiagnosticReport:
    source_id: str
    question_count: int
    answered_count: int
    missing_count: int
    unsupported_count: int
    incoherent_count: int
    repaired_count: int = 0


@dataclass(frozen=True)
class RepairTask:
    repair_task_id: str
    finding_ids: tuple[str, ...]
    repair_kind: str
    target_page_id: str
    required_support_refs: tuple[str, ...]
    status: str


@dataclass(frozen=True)
class RepairTaskSet:
    repair_task_set_id: str
    repair_task_set_fingerprint: str
    artifact_format: str
    source_id: str
    source_hash: str
    tasks: tuple[RepairTask, ...]


@dataclass(frozen=True)
class RepairRun:
    repair_run_id: str
    repair_run_fingerprint: str
    artifact_format: str
    source_id: str
    source_hash: str
    repair_task_ids: tuple[str, ...]
    changed_page_ids: tuple[str, ...]
    accepted_page_ids: tuple[str, ...]
    rejected_page_ids: tuple[str, ...]
    article_lint_run_ids: tuple[str, ...]
    status: str


@dataclass(frozen=True)
class DiagnosticCorpusPage:
    page_id: str
    summary: str
    page_body: str


@dataclass(frozen=True)
class DiagnosticAnswerCorpus:
    pages: tuple[DiagnosticCorpusPage, ...]

    @property
    def page_ids(self) -> frozenset[str]:
        return frozenset(page.page_id for page in self.pages)

    def page_text(self, page_id: str) -> str:
        return next((page.page_body for page in self.pages if page.page_id == page_id), "")


class DiagnosticAnswerer(Protocol):
    def answer_diagnostic_question(
        self, question: DiagnosticQuestion, corpus: DiagnosticAnswerCorpus
    ) -> DiagnosticAnswer: ...


class DiagnosticJudge(Protocol):
    def judge_diagnostic_answer(
        self,
        question: DiagnosticQuestion,
        answer: DiagnosticAnswer,
        pack: EvidencePack | None,
    ) -> tuple[DiagnosticFinding, ...]: ...
