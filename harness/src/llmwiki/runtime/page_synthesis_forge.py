"""Forge-backed PageDraftProducer runtime adapter."""

from __future__ import annotations

import asyncio
from collections.abc import Callable, Coroutine
from concurrent.futures import ThreadPoolExecutor
from typing import Any

from forge.context import ContextManager
from forge.core.messages import Message
from forge.core.runner import WorkflowRunner

from llmwiki.domain.ledger.page_synthesis import (
    PageDraft,
    PageSynthesisFinding,
    PageSynthesisPlan,
)
from llmwiki.workflows.page_synthesis_draft import (
    build_page_synthesis_draft_workflow,
    page_draft_from_json,
    render_page_synthesis_prompt,
)


class ForgePageDraftProducer:
    """Draft synthesized pages through Forge's tool-calling runner."""

    def __init__(
        self,
        *,
        client: Any,
        context_manager: ContextManager,
        schema_text: str,
        max_iterations: int = 4,
        on_message: Callable[[Message], None] | None = None,
    ) -> None:
        self.client = client
        self.context_manager = context_manager
        self.schema_text = schema_text
        self.max_iterations = max_iterations
        self.on_message = on_message

    def draft_page(
        self,
        plan: PageSynthesisPlan,
        findings: tuple[PageSynthesisFinding, ...] = (),
    ) -> PageDraft:
        return _run_in_thread(self._draft_page_async(plan, findings))

    async def _draft_page_async(
        self,
        plan: PageSynthesisPlan,
        findings: tuple[PageSynthesisFinding, ...],
    ) -> PageDraft:
        writer = _message_writer(self.on_message)
        runner = WorkflowRunner(
            client=self.client,
            context_manager=self.context_manager,
            max_iterations=self.max_iterations,
            max_tool_errors=1,
            on_message=writer,
            retry_nudge=(
                "Reply with exactly one draft_page tool call. Every factual sentence "
                "must have a DraftClaim with selected support_refs."
            ),
        )
        result = await runner.run(
            build_page_synthesis_draft_workflow(plan),
            render_page_synthesis_prompt(plan, findings),
            prompt_vars={"schema": self.schema_text},
        )
        return page_draft_from_json(str(result))


def _run_in_thread(coro: Coroutine[Any, Any, PageDraft]) -> PageDraft:
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
