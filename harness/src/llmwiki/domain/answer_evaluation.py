"""Deterministic checks for normal query answers in tests and smoke runs."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

AnswerEvaluationVerdict = Literal["pass", "fail"]


@dataclass(frozen=True)
class AnswerEvaluationCase:
    case_id: str
    source_locator: str
    question: str
    required_atom_ids: tuple[str, ...]
    required_fragments: tuple[str, ...]
    required_citations: tuple[str, ...]

    def __post_init__(self) -> None:
        if not self.case_id or not self.question:
            raise ValueError("AnswerEvaluationCase requires case_id and question.")


@dataclass(frozen=True)
class AnswerEvaluationReport:
    case_id: str
    verdict: AnswerEvaluationVerdict
    findings: tuple[str, ...]
    required_atom_ids: tuple[str, ...]
    covered_atom_ids: tuple[str, ...]
    missing_fragments: tuple[str, ...]


def evaluate_answer(answer: str, case: AnswerEvaluationCase) -> AnswerEvaluationReport:
    missing_fragments = tuple(
        fragment for fragment in case.required_fragments if fragment not in answer
    )
    missing_citations = tuple(
        citation for citation in case.required_citations if citation not in answer
    )
    findings = tuple(
        [*(f"missing fragment: {item}" for item in missing_fragments)]
        + [*(f"missing citation: {item}" for item in missing_citations)]
    )
    verdict: AnswerEvaluationVerdict = "fail" if findings else "pass"
    return AnswerEvaluationReport(
        case_id=case.case_id,
        verdict=verdict,
        findings=findings,
        required_atom_ids=case.required_atom_ids,
        covered_atom_ids=() if findings else case.required_atom_ids,
        missing_fragments=missing_fragments,
    )
