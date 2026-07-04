"""Forge workflow for judging diagnostic answers against evidence packs."""

from __future__ import annotations

import json
from typing import Any

from forge.core.workflow import ToolDef, ToolSpec, Workflow
from pydantic import BaseModel, Field, model_validator

from llmwiki.domain.diagnostic_contracts import (
    DiagnosticAnswer,
    DiagnosticFinding,
    DiagnosticQuestion,
)
from llmwiki.domain.diagnostics import diagnostic_finding
from llmwiki.domain.ledger.evidence_pack import EvidencePack


class DiagnosticFindingParams(BaseModel):
    severity: str = "blocking"
    finding_code: str
    support_ref: str = ""
    page_id: str = ""
    message: str


class DiagnosticJudgmentParams(BaseModel):
    diagnostic_question_id: str
    findings: list[DiagnosticFindingParams] = Field(default_factory=list)

    @model_validator(mode="before")
    @classmethod
    def rescue_singleton_finding(cls, value: object) -> object:
        if not isinstance(value, dict):
            return value
        data: dict[str, Any] = {str(key): item for key, item in value.items()}
        if isinstance(data.get("findings"), dict):
            data["findings"] = [data["findings"]]
        return data


_SYSTEM_PROMPT = """Judge whether the diagnostic answer is supported.

Compare the answer with the provided EvidencePack source text and payload text.
Record no findings when the answer is complete and supported. Record blocking
findings for missing-answer, unsupported-answer, incoherent-answer, or
missing-page. Diagnostics are not public evidence.

Schema:
{schema}
"""


def build_diagnostic_judge_workflow(
    question: DiagnosticQuestion, answer: DiagnosticAnswer, pack: EvidencePack | None
) -> Workflow:
    tool = diagnostic_judgment_tool(question, answer, pack)
    return Workflow(
        name="diagnostic-judge",
        description="Judge one diagnostic answer against selected evidence.",
        tools={tool.name: tool},
        required_steps=[],
        terminal_tool="record_diagnostic_judgment",
        system_prompt_template=_SYSTEM_PROMPT,
    )


def diagnostic_judgment_tool(
    question: DiagnosticQuestion, answer: DiagnosticAnswer, pack: EvidencePack | None
) -> ToolDef:
    selected_refs = set(question.expected_support_refs)

    def _record_diagnostic_judgment(**kwargs: object) -> str:
        params = DiagnosticJudgmentParams(**kwargs)  # type: ignore[arg-type]
        if params.diagnostic_question_id != question.diagnostic_question_id:
            raise ValueError("diagnostic judgment must reference the selected question id")
        findings = tuple(
            _finding_from_params(question, item, selected_refs) for item in params.findings
        )
        return diagnostic_findings_to_json(findings)

    return ToolDef(
        spec=ToolSpec(
            name="record_diagnostic_judgment",
            description="Record diagnostic findings for one diagnostic answer.",
            parameters=DiagnosticJudgmentParams,
        ),
        callable=_record_diagnostic_judgment,
    )


def render_diagnostic_judge_prompt(
    question: DiagnosticQuestion, answer: DiagnosticAnswer, pack: EvidencePack | None
) -> str:
    payload = {
        "question": {
            "diagnostic_question_id": question.diagnostic_question_id,
            "question_text": question.question_text,
            "expected_support_refs": list(question.expected_support_refs),
        },
        "answer": {
            "answer_text": answer.answer_text,
            "cited_page_ids": list(answer.cited_page_ids),
            "cited_support_refs": list(answer.cited_support_refs),
        },
        "evidence_pack": None if pack is None else _pack_payload(pack),
    }
    return json.dumps(payload, ensure_ascii=True, indent=2)


def diagnostic_findings_from_json(text: str) -> tuple[DiagnosticFinding, ...]:
    data = json.loads(text)
    return tuple(
        DiagnosticFinding(
            item["diagnostic_finding_id"],
            item["diagnostic_question_id"],
            item["severity"],
            item["finding_code"],
            item.get("support_ref", ""),
            item.get("page_id", ""),
            item["message"],
        )
        for item in data.get("findings", ())
    )


def diagnostic_findings_to_json(findings: tuple[DiagnosticFinding, ...]) -> str:
    return json.dumps(
        {
            "findings": [
                {
                    "diagnostic_finding_id": finding.diagnostic_finding_id,
                    "diagnostic_question_id": finding.diagnostic_question_id,
                    "severity": finding.severity,
                    "finding_code": finding.finding_code,
                    "support_ref": finding.support_ref,
                    "page_id": finding.page_id,
                    "message": finding.message,
                }
                for finding in findings
            ]
        },
        ensure_ascii=True,
        sort_keys=True,
    )


def _finding_from_params(
    question: DiagnosticQuestion, params: DiagnosticFindingParams, selected_refs: set[str]
) -> DiagnosticFinding:
    support_ref = params.support_ref if params.support_ref in selected_refs else ""
    page_id = params.page_id or (question.page_ids[0] if question.page_ids else "")
    finding = diagnostic_finding(question, params.finding_code, params.message)
    return DiagnosticFinding(
        finding.diagnostic_finding_id,
        finding.diagnostic_question_id,
        params.severity,
        params.finding_code,
        support_ref,
        page_id,
        params.message,
    )


def _pack_payload(pack: EvidencePack) -> dict[str, object]:
    return {
        "page_id": pack.page_id,
        "title": pack.title,
        "items": [
            {
                "support_ref": item.support_ref.code,
                "source_text": item.source_text,
                "payload_text": item.payload_text,
                "citation_label": item.citation_label,
            }
            for item in pack.items
        ],
    }
