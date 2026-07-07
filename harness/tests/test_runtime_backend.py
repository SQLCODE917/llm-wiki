"""Runtime backend construction without a live model server."""

from __future__ import annotations

import asyncio
from typing import Any

import pytest
from forge.clients.ollama import OllamaClient

from llmwiki.config import BackendConfig
from llmwiki.runtime import backend as backend_module
from llmwiki.runtime.async_thread import run_coroutine_in_daemon_thread
from llmwiki.runtime.ollama_client_scope import loop_local_ollama_client


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


@pytest.mark.asyncio
async def test_loop_local_ollama_client_clones_ollama_settings() -> None:
    client = OllamaClient(
        model="qwen3-coder:30b",
        base_url="http://127.0.0.1:11434",
        timeout=17.0,
        think=False,
    )
    client.set_num_ctx(12345)

    try:
        async with loop_local_ollama_client(client) as clone:
            assert clone is not client
            assert clone.model == "qwen3-coder:30b"
            assert clone.base_url == "http://127.0.0.1:11434"
            assert clone._num_ctx == 12345  # noqa: SLF001
            assert float(clone._http.timeout.read) == 17.0  # noqa: SLF001
    finally:
        await client.aclose()


@pytest.mark.asyncio
async def test_loop_local_ollama_client_passes_through_non_ollama_client() -> None:
    client = FakeClient(
        model="fake",
        base_url="memory://fake",
        timeout=1.0,
        think=False,
    )

    async with loop_local_ollama_client(client) as scoped_client:
        assert scoped_client is client
        assert client.closed is False


def test_run_coroutine_in_daemon_thread_returns_result() -> None:
    async def _value() -> str:
        return "ok"

    assert (
        run_coroutine_in_daemon_thread(
            _value(), timeout_seconds=1.0, label="test-runtime"
        )
        == "ok"
    )


def test_run_coroutine_in_daemon_thread_times_out() -> None:
    async def _slow() -> str:
        await asyncio.sleep(1.0)
        return "late"

    with pytest.raises(TimeoutError, match="test-timeout timed out after 0s"):
        run_coroutine_in_daemon_thread(
            _slow(), timeout_seconds=0.01, label="test-timeout"
        )
