"""Per-run JSONL transcript of the model conversation.

Every wiki edit stays traceable to the model turn that produced it
(design doc, "Observability"). Wired into WorkflowRunner's on_message.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import IO

from forge.core.messages import Message


class TranscriptWriter:
    def __init__(self, path: Path) -> None:
        self._path = path
        self._fh: IO[str] | None = None

    @property
    def path(self) -> Path:
        return self._path

    def on_message(self, message: Message) -> None:
        if self._fh is None:
            self._path.parent.mkdir(parents=True, exist_ok=True)
            self._fh = self._path.open("a", encoding="utf-8")
        record = {
            "role": message.role.value,
            "type": message.metadata.type.value,
            "content": message.content,
            "tool_name": message.tool_name,
            "tool_calls": [{"name": tc.name, "args": tc.args} for tc in (message.tool_calls or [])],
        }
        self._fh.write(json.dumps(record, ensure_ascii=False) + "\n")
        self._fh.flush()

    def close(self) -> None:
        if self._fh is not None:
            self._fh.close()
            self._fh = None
