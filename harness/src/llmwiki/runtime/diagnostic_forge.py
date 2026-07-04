"""Forge-backed diagnostic answerer and judge adapters."""

from __future__ import annotations

import asyncio
from collections.abc import Callable, Coroutine
from concurrent.futures import ThreadPoolExecutor
from typing import Any, Protocol

from forge.context import ContextManager
from forge.core.messages import Message
from forge.core.runner import WorkflowRunner

from llmwiki.domain.diagnostic_contracts import (
    DiagnosticAnswer,
    DiagnosticAnswerCorpus,
    DiagnosticFinding,
    DiagnosticQuestion,
)
from llmwiki.domain.ledger.evidence_pack import EvidencePack
from llmwiki.workflows.diagnostic_answer import (
    build_diagnostic_answer_workflow,
    diagnostic_answer_from_json,
    render_diagnostic_answer_prompt,
)
from llmwiki.workflows.diagnostic_judge import (
    build_diagnostic_judge_workflow,
    diagnostic_findings_from_json,
    render_diagnostic_judge_prompt,
)


class _ForgeDiagnosticAdapter(Protocol):
    client: Any
    context_manager: ContextManager
    max_iterations: int
    on_message: Callable[[Message], None] | None


class ForgeDiagnosticAnswerer:
    def __init__(
        self,
        *,
        client: Any,
        context_manager: ContextManager,
        schema_text: str,
        max_iterations: int = 3,
        on_message: Callable[[Message], None] | None = None,
    ) -> None:
        self.client = client
        self.context_manager = context_manager
        self.schema_text = schema_text
        self.max_iterations = max_iterations
        self.on_message = on_message

    def answer_diagnostic_question(
        self, question: DiagnosticQuestion, corpus: DiagnosticAnswerCorpus
    ) -> DiagnosticAnswer:
        return _run_answer(self._answer_async(question, corpus))

    async def _answer_async(
        self, question: DiagnosticQuestion, corpus: DiagnosticAnswerCorpus
    ) -> DiagnosticAnswer:
        runner = _runner(self, "Reply with exactly one record_diagnostic_answer tool call.")
        result = await runner.run(
            build_diagnostic_answer_workflow(question, corpus),
            render_diagnostic_answer_prompt(question, corpus),
            prompt_vars={"schema": self.schema_text},
        )
        return diagnostic_answer_from_json(str(result))


class ForgeDiagnosticJudge:
    def __init__(
        self,
        *,
        client: Any,
        context_manager: ContextManager,
        schema_text: str,
        max_iterations: int = 3,
        on_message: Callable[[Message], None] | None = None,
    ) -> None:
        self.client = client
        self.context_manager = context_manager
        self.schema_text = schema_text
        self.max_iterations = max_iterations
        self.on_message = on_message

    def judge_diagnostic_answer(
        self,
        question: DiagnosticQuestion,
        answer: DiagnosticAnswer,
        pack: EvidencePack | None,
    ) -> tuple[DiagnosticFinding, ...]:
        return _run_findings(self._judge_async(question, answer, pack))

    async def _judge_async(
        self,
        question: DiagnosticQuestion,
        answer: DiagnosticAnswer,
        pack: EvidencePack | None,
    ) -> tuple[DiagnosticFinding, ...]:
        runner = _runner(self, "Reply with exactly one record_diagnostic_judgment tool call.")
        result = await runner.run(
            build_diagnostic_judge_workflow(question, answer, pack),
            render_diagnostic_judge_prompt(question, answer, pack),
            prompt_vars={"schema": self.schema_text},
        )
        return diagnostic_findings_from_json(str(result))


def _runner(adapter: _ForgeDiagnosticAdapter, retry_nudge: str) -> WorkflowRunner:
    return WorkflowRunner(
        client=adapter.client,
        context_manager=adapter.context_manager,
        max_iterations=adapter.max_iterations,
        max_tool_errors=1,
        on_message=_message_writer(adapter.on_message),
        retry_nudge=retry_nudge,
    )


def _run_answer(coro: Coroutine[Any, Any, DiagnosticAnswer]) -> DiagnosticAnswer:
    with ThreadPoolExecutor(max_workers=1) as executor:
        return executor.submit(lambda: asyncio.run(coro)).result()


def _run_findings(
    coro: Coroutine[Any, Any, tuple[DiagnosticFinding, ...]]
) -> tuple[DiagnosticFinding, ...]:
    with ThreadPoolExecutor(max_workers=1) as executor:
        return executor.submit(lambda: asyncio.run(coro)).result()


def _message_writer(
    callback: Callable[[Message], None] | None,
) -> Callable[[Message], None] | None:
    if callback is None:
        return None

    def _write(message: Message) -> None:
        callback(message)

    return _write
