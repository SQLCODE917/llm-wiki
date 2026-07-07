"""Loop-local Ollama client scope for synchronous compiler adapters."""

from __future__ import annotations

from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
from typing import Any

from forge.clients.ollama import OllamaClient


@asynccontextmanager
async def loop_local_ollama_client(client: Any) -> AsyncIterator[Any]:
    """Clone Ollama clients so async HTTP connections stay on one event loop."""

    if not isinstance(client, OllamaClient):
        yield client
        return
    timeout = client._http.timeout.read  # noqa: SLF001
    clone = OllamaClient(
        model=client.model,
        base_url=client.base_url,
        temperature=client.temperature,
        top_p=client.top_p,
        top_k=int(client.top_k) if client.top_k is not None else None,
        min_p=client.min_p,
        repeat_penalty=client.repeat_penalty,
        presence_penalty=client.presence_penalty,
        timeout=float(timeout) if timeout is not None else 300.0,
        think=client._think,  # noqa: SLF001
    )
    clone.set_num_ctx(client._num_ctx)  # noqa: SLF001
    try:
        yield clone
    finally:
        await clone.aclose()
