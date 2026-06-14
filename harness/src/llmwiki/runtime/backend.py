"""llama-server lifecycle and client construction via forge.

forge's ServerManager invokes `llama-server` from PATH (symlinked from
llama.cpp/build/bin). Sampling follows the Qwen3 model card via forge's
recommended_sampling map, keyed on the GGUF stem (Qwen3-14B-Q4_K_M).
"""

from __future__ import annotations

from dataclasses import dataclass

from forge.clients.llamafile import LlamafileClient
from forge.context import ContextManager
from forge.server import BudgetMode, ServerManager, setup_backend

from llmwiki.config import BackendConfig


@dataclass
class ActiveBackend:
    server: ServerManager
    context_manager: ContextManager
    client: LlamafileClient

    async def aclose(self) -> None:
        await self.client.aclose()
        await self.server.stop()


async def start_backend(config: BackendConfig) -> ActiveBackend:
    client = LlamafileClient(
        gguf_path=config.gguf_path,
        base_url=f"http://localhost:{config.port}/v1",
        mode="native",
        recommended_sampling=True,
    )
    server, context_manager = await setup_backend(
        backend="llamaserver",
        gguf_path=config.gguf_path,
        budget_mode=BudgetMode.MANUAL,
        manual_tokens=config.context_tokens,
        mode="native",
        port=config.port,
    )
    return ActiveBackend(server=server, context_manager=context_manager, client=client)
