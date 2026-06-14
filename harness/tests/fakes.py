"""A scripted LLMClient fake — the only mock at the network boundary."""

from __future__ import annotations

from typing import Any

from forge.core.workflow import LLMResponse


class FakeClient:
    """Plays back a fixed script of LLMResponse objects, one per send()."""

    api_format = "openai"
    model = "fake-model"

    def __init__(self, script: list[LLMResponse]) -> None:
        self._script = list(script)
        self.sent: list[list[dict[str, Any]]] = []

    async def send(
        self, messages: list[dict[str, Any]], tools: Any = None, **kwargs: Any
    ) -> LLMResponse:
        self.sent.append(messages)
        if not self._script:
            raise AssertionError("FakeClient script exhausted — workflow took an extra turn")
        return self._script.pop(0)

    async def send_stream(self, *args: Any, **kwargs: Any) -> Any:
        raise NotImplementedError("tests run the batch path")

    async def get_context_length(self) -> int | None:
        return None

    async def aclose(self) -> None:
        pass
