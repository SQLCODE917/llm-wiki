"""Ollama lifecycle and client construction via forge."""

from __future__ import annotations

from dataclasses import dataclass

from forge.clients.ollama import OllamaClient
from forge.context import ContextManager
from forge.server import BudgetMode, ServerManager, setup_backend

from llmwiki.config import BackendConfig


@dataclass
class ActiveBackend:
    server: ServerManager
    context_manager: ContextManager
    client: OllamaClient
    summary: str

    async def aclose(self) -> None:
        await self.client.aclose()
        await self.server.stop()


async def start_backend(config: BackendConfig) -> ActiveBackend:
    client = OllamaClient(
        model=config.model,
        base_url=config.endpoint,
        timeout=float(config.timeout_seconds),
        think=False,
    )
    server, context_manager = await setup_backend(
        backend=config.backend_kind,
        model=config.model,
        budget_mode=BudgetMode.MANUAL,
        manual_tokens=config.context_tokens,
        client=client,
    )
    return ActiveBackend(
        server=server,
        context_manager=context_manager,
        client=client,
        summary=config.summary(),
    )
