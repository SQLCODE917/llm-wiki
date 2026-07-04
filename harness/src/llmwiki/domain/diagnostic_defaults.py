"""Deterministic diagnostic answerer and judge fallbacks."""

from __future__ import annotations

from llmwiki.domain.diagnostic_contracts import (
    DiagnosticAnswer,
    DiagnosticAnswerCorpus,
    DiagnosticFinding,
    DiagnosticQuestion,
)
from llmwiki.domain.diagnostics import diagnostic_finding
from llmwiki.domain.ledger.evidence_pack import EvidencePack


class CorpusDiagnosticAnswerer:
    def answer_diagnostic_question(
        self, question: DiagnosticQuestion, corpus: DiagnosticAnswerCorpus
    ) -> DiagnosticAnswer:
        cited = tuple(page_id for page_id in question.page_ids if page_id in corpus.page_ids)
        text = " ".join(_first_paragraph(corpus.page_text(page_id)) for page_id in cited).strip()
        return DiagnosticAnswer(question.diagnostic_question_id, text, cited)


class EvidenceDiagnosticJudge:
    def judge_diagnostic_answer(
        self,
        question: DiagnosticQuestion,
        answer: DiagnosticAnswer,
        pack: EvidencePack | None,
    ) -> tuple[DiagnosticFinding, ...]:
        if not answer.answer_text.strip() or not answer.cited_page_ids:
            return (
                diagnostic_finding(
                    question,
                    "missing-answer",
                    "wiki snapshot did not answer the diagnostic question",
                ),
            )
        if pack is None:
            return (
                diagnostic_finding(
                    question,
                    "missing-page",
                    "diagnostic question has no evidence pack",
                ),
            )
        if _looks_unsupported(answer.answer_text):
            return (
                diagnostic_finding(
                    question,
                    "unsupported-answer",
                    "answer appears unsupported by evidence",
                ),
            )
        return ()


def _first_paragraph(text: str) -> str:
    for paragraph in text.split("\n\n"):
        cleaned = " ".join(line.strip() for line in paragraph.splitlines()).strip()
        if cleaned and not cleaned.startswith("---") and not cleaned.startswith("#"):
            return cleaned
    return ""


def _looks_unsupported(text: str) -> bool:
    lowered = text.casefold()
    return "unsupported" in lowered or "invented" in lowered or "cannot answer" in lowered
