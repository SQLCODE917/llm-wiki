"""Synchronous timeout wrapper for async runtime adapters."""

from __future__ import annotations

import asyncio
from collections.abc import Coroutine
from dataclasses import dataclass
from queue import Empty, Queue
from threading import Thread
from typing import Any, cast


@dataclass(frozen=True)
class _ThreadResult[T]:
    value: T | None = None
    error: BaseException | None = None


def run_coroutine_in_daemon_thread[T](
    coro: Coroutine[Any, Any, T], *, timeout_seconds: float, label: str
) -> T:
    """Run an async adapter call from sync compiler code with a hard timeout."""

    result_queue: Queue[_ThreadResult[T]] = Queue(maxsize=1)

    def _target() -> None:
        try:
            result_queue.put(_ThreadResult(value=_run_without_executor_join(coro)))
        except BaseException as exc:  # noqa: BLE001
            result_queue.put(_ThreadResult(error=exc))

    thread = Thread(target=_target, name=f"llmwiki-{label}", daemon=True)
    thread.start()
    try:
        result = result_queue.get(timeout=timeout_seconds)
    except Empty as exc:
        raise TimeoutError(f"{label} timed out after {timeout_seconds:.0f}s") from exc
    if result.error is not None:
        raise result.error
    return cast(T, result.value)


def _run_without_executor_join[T](coro: Coroutine[Any, Any, T]) -> T:
    """Run a coroutine without asyncio.run's 300s default-executor shutdown wait."""

    loop = asyncio.new_event_loop()
    try:
        asyncio.set_event_loop(loop)
        return loop.run_until_complete(coro)
    finally:
        try:
            loop.run_until_complete(loop.shutdown_asyncgens())
        finally:
            asyncio.set_event_loop(None)
            loop.close()
