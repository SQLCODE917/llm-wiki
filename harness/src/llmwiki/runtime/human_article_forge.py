"""Forge-backed ArticleWriter runtime adapter."""

from __future__ import annotations

import asyncio
from collections.abc import Callable
from typing import Any

from forge.context import ContextManager
from forge.core.messages import Message
from forge.core.runner import WorkflowRunner

from llmwiki.domain.ledger.evidence_pack import EvidencePack
from llmwiki.domain.ledger.human_article import ArticleFinding, HumanArticle
from llmwiki.runtime.async_thread import run_coroutine_in_daemon_thread
from llmwiki.runtime.ollama_client_scope import loop_local_ollama_client
from llmwiki.workflows.human_article_write import (
    build_human_article_workflow,
    human_article_from_json,
    render_human_article_prompt,
)

_ARTICLE_MODEL_TIMEOUT_SECONDS = 90.0


class ForgeHumanArticleWriter:
    """Write structured human articles through Forge's tool-calling runner."""

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

    def write_article(
        self,
        pack: EvidencePack,
        findings: tuple[ArticleFinding, ...] = (),
    ) -> HumanArticle:
        return run_coroutine_in_daemon_thread(
            self._write_article_async(pack, findings),
            timeout_seconds=_ARTICLE_MODEL_TIMEOUT_SECONDS + 5.0,
            label="write-article",
        )

    async def _write_article_async(
        self,
        pack: EvidencePack,
        findings: tuple[ArticleFinding, ...],
    ) -> HumanArticle:
        async with loop_local_ollama_client(self.client) as client:
            runner = WorkflowRunner(
                client=client,
                context_manager=self.context_manager,
                max_iterations=self.max_iterations,
                max_tool_errors=1,
                on_message=_message_writer(self.on_message),
                retry_nudge=(
                    "Reply with exactly one write_article tool call. Every factual sentence "
                    "must have an ArticleClaim with support_refs using evidence aliases from "
                    "the prompt, such as S1 or S2. Each ArticleClaim.sentence must be one "
                    "complete sentence in your own words, not copied source text, not a "
                    "colon-ended fragment, and not a semicolon-joined list."
                ),
            )
            result = await asyncio.wait_for(
                runner.run(
                    build_human_article_workflow(pack),
                    render_human_article_prompt(pack, findings),
                    prompt_vars={"schema": self.schema_text},
                ),
                timeout=_ARTICLE_MODEL_TIMEOUT_SECONDS,
            )
        return human_article_from_json(str(result))


def _message_writer(
    callback: Callable[[Message], None] | None,
) -> Callable[[Message], None] | None:
    if callback is None:
        return None

    def _write(message: Message) -> None:
        callback(message)

    return _write
