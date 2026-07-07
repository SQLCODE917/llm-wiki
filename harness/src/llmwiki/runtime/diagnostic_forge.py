"""Forge-backed diagnostic answerer and judge adapters."""

from __future__ import annotations

import asyncio
from collections.abc import Callable
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
from llmwiki.runtime.async_thread import run_coroutine_in_daemon_thread
from llmwiki.runtime.ollama_client_scope import loop_local_ollama_client
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

_DIAGNOSTIC_MODEL_TIMEOUT_SECONDS = 30.0


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
        return run_coroutine_in_daemon_thread(
            self._answer_async(question, corpus),
            timeout_seconds=_DIAGNOSTIC_MODEL_TIMEOUT_SECONDS + 5.0,
            label="diagnostic-answer",
        )

    async def _answer_async(
        self, question: DiagnosticQuestion, corpus: DiagnosticAnswerCorpus
    ) -> DiagnosticAnswer:
        async with loop_local_ollama_client(self.client) as client:
            runner = _runner(
                self,
                "Reply with exactly one record_diagnostic_answer tool call.",
                client=client,
            )
            result = await asyncio.wait_for(
                runner.run(
                    build_diagnostic_answer_workflow(question, corpus),
                    render_diagnostic_answer_prompt(question, corpus),
                    prompt_vars={"schema": self.schema_text},
                ),
                timeout=_DIAGNOSTIC_MODEL_TIMEOUT_SECONDS,
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
        return run_coroutine_in_daemon_thread(
            self._judge_async(question, answer, pack),
            timeout_seconds=_DIAGNOSTIC_MODEL_TIMEOUT_SECONDS + 5.0,
            label="diagnostic-judge",
        )

    async def _judge_async(
        self,
        question: DiagnosticQuestion,
        answer: DiagnosticAnswer,
        pack: EvidencePack | None,
    ) -> tuple[DiagnosticFinding, ...]:
        async with loop_local_ollama_client(self.client) as client:
            runner = _runner(
                self,
                "Reply with exactly one record_diagnostic_judgment tool call.",
                client=client,
            )
            result = await asyncio.wait_for(
                runner.run(
                    build_diagnostic_judge_workflow(question, answer, pack),
                    render_diagnostic_judge_prompt(question, answer, pack),
                    prompt_vars={"schema": self.schema_text},
                ),
                timeout=_DIAGNOSTIC_MODEL_TIMEOUT_SECONDS,
            )
        return diagnostic_findings_from_json(str(result))


def _runner(
    adapter: _ForgeDiagnosticAdapter, retry_nudge: str, *, client: Any | None = None
) -> WorkflowRunner:
    return WorkflowRunner(
        client=client or adapter.client,
        context_manager=adapter.context_manager,
        max_iterations=adapter.max_iterations,
        max_tool_errors=1,
        on_message=_message_writer(adapter.on_message),
        retry_nudge=retry_nudge,
    )


def _message_writer(
    callback: Callable[[Message], None] | None,
) -> Callable[[Message], None] | None:
    if callback is None:
        return None

    def _write(message: Message) -> None:
        callback(message)

    return _write
