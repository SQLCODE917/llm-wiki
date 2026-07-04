"""Forge workflow for answering diagnostic questions from wiki pages only."""

from __future__ import annotations

import json
from typing import Any

from forge.core.workflow import ToolDef, ToolSpec, Workflow
from pydantic import BaseModel, Field, model_validator

from llmwiki.domain.diagnostic_contracts import (
    DiagnosticAnswer,
    DiagnosticAnswerCorpus,
    DiagnosticQuestion,
)


class DiagnosticAnswerParams(BaseModel):
    diagnostic_question_id: str
    answer_text: str
    cited_page_ids: list[str] = Field(default_factory=list)
    cited_support_refs: list[str] = Field(default_factory=list)

    @model_validator(mode="before")
    @classmethod
    def rescue_singletons(cls, value: object) -> object:
        if not isinstance(value, dict):
            return value
        data: dict[str, Any] = {str(key): item for key, item in value.items()}
        for key in ("cited_page_ids", "cited_support_refs"):
            if isinstance(data.get(key), str):
                data[key] = [data[key]]
        return data


_SYSTEM_PROMPT = """Answer one diagnostic question from the provided wiki pages only.

Do not use raw source text, evidence packs, or outside knowledge. If the wiki
pages do not answer the question, submit an empty answer_text. Cite only page
ids that appear in the wiki_page_corpus payload.

Schema:
{schema}
"""


def build_diagnostic_answer_workflow(
    question: DiagnosticQuestion, corpus: DiagnosticAnswerCorpus
) -> Workflow:
    tool = diagnostic_answer_tool(question, corpus)
    return Workflow(
        name="diagnostic-answer",
        description="Answer one diagnostic question from staged wiki pages.",
        tools={tool.name: tool},
        required_steps=[],
        terminal_tool="record_diagnostic_answer",
        system_prompt_template=_SYSTEM_PROMPT,
    )


def diagnostic_answer_tool(
    question: DiagnosticQuestion, corpus: DiagnosticAnswerCorpus
) -> ToolDef:
    allowed_pages = corpus.page_ids

    def _record_diagnostic_answer(**kwargs: object) -> str:
        params = DiagnosticAnswerParams(**kwargs)  # type: ignore[arg-type]
        if params.diagnostic_question_id != question.diagnostic_question_id:
            raise ValueError("diagnostic answer must reference the selected question id")
        unknown = tuple(
            page_id for page_id in params.cited_page_ids if page_id not in allowed_pages
        )
        if unknown:
            raise ValueError("diagnostic answer cited pages outside the wiki corpus")
        return diagnostic_answer_to_json(
            DiagnosticAnswer(
                params.diagnostic_question_id,
                params.answer_text,
                tuple(params.cited_page_ids),
                tuple(params.cited_support_refs),
            )
        )

    return ToolDef(
        spec=ToolSpec(
            name="record_diagnostic_answer",
            description="Submit one wiki-only diagnostic answer.",
            parameters=DiagnosticAnswerParams,
        ),
        callable=_record_diagnostic_answer,
    )


def render_diagnostic_answer_prompt(
    question: DiagnosticQuestion, corpus: DiagnosticAnswerCorpus
) -> str:
    payload = {
        "question": {
            "diagnostic_question_id": question.diagnostic_question_id,
            "question_text": question.question_text,
            "page_ids": list(question.page_ids),
            "purpose": question.purpose,
        },
        "wiki_page_corpus": [
            {"page_id": page.page_id, "summary": page.summary, "page_body": page.page_body}
            for page in corpus.pages
        ],
    }
    return json.dumps(payload, ensure_ascii=True, indent=2)


def diagnostic_answer_from_json(text: str) -> DiagnosticAnswer:
    data = json.loads(text)
    return DiagnosticAnswer(
        data["diagnostic_question_id"],
        data["answer_text"],
        tuple(data.get("cited_page_ids", ())),
        tuple(data.get("cited_support_refs", ())),
    )


def diagnostic_answer_to_json(answer: DiagnosticAnswer) -> str:
    return json.dumps(
        {
            "diagnostic_question_id": answer.diagnostic_question_id,
            "answer_text": answer.answer_text,
            "cited_page_ids": list(answer.cited_page_ids),
            "cited_support_refs": list(answer.cited_support_refs),
        },
        ensure_ascii=True,
        sort_keys=True,
    )
