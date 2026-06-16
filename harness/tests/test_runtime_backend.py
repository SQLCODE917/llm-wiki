"""Runtime backend construction without a live model server."""

from __future__ import annotations

from typing import Any

import pytest

from llmwiki.config import BackendConfig
from llmwiki.runtime import backend as backend_module


class FakeClient:
    def __init__(
        self,
        model: str,
        base_url: str,
        timeout: float,
        think: bool,
    ) -> None:
        self.model = model
        self.base_url = base_url
        self.timeout = timeout
        self.think = think
        self.closed = False

    async def aclose(self) -> None:
        self.closed = True


class FakeServer:
    def __init__(self) -> None:
        self.stopped = False

    async def stop(self) -> None:
        self.stopped = True


@pytest.mark.asyncio
async def test_start_backend_uses_ollama_profile(monkeypatch: pytest.MonkeyPatch) -> None:
    calls: dict[str, Any] = {}

    def fake_client(model: str, base_url: str, timeout: float, think: bool) -> FakeClient:
        calls["client"] = {
            "model": model,
            "base_url": base_url,
            "timeout": timeout,
            "think": think,
        }
        return FakeClient(model=model, base_url=base_url, timeout=timeout, think=think)

    async def fake_setup_backend(**kwargs: Any) -> tuple[FakeServer, object]:
        calls["setup"] = kwargs
        return FakeServer(), object()

    monkeypatch.setattr(backend_module, "OllamaClient", fake_client)
    monkeypatch.setattr(backend_module, "setup_backend", fake_setup_backend)

    config = BackendConfig(
        runtime_name="local-4090",
        backend_kind="ollama",
        model="qwen3-coder:30b",
        context_tokens=32768,
        endpoint="http://127.0.0.1:11434",
        timeout_seconds=1200,
    )
    active = await backend_module.start_backend(config)

    assert calls["client"] == {
        "model": "qwen3-coder:30b",
        "base_url": "http://127.0.0.1:11434",
        "timeout": 1200.0,
        "think": False,
    }
    assert calls["setup"]["backend"] == "ollama"
    assert calls["setup"]["model"] == "qwen3-coder:30b"
    assert calls["setup"]["manual_tokens"] == 32768
    assert calls["setup"]["client"] is active.client
    assert "local-4090" in active.summary
    assert "provider=ollama" in active.summary
