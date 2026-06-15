"""Chat REPL: command dispatch and turn orchestration.

The line-handling logic lives here, testable without a terminal; the thin
input loop lives in the CLI. A failed turn is reported and the REPL
continues — nothing was persisted for it, so the conversation stays
consistent.
"""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass, field
from datetime import datetime

from llmwiki.domain.chatwindow import build_window, estimate_tokens
from llmwiki.runtime.session import Session
from llmwiki.store.chat_store import ChatStore

_HELP = """commands:
  /new            start a new conversation
  /sessions       list conversations (most recent first)
  /switch <id>    make another conversation active
  /file <page>    file the latest answer as a durable synthesis page
  /ingest <file>  ingest a raw source (own workflow, warm server)
  /lint           health-check the wiki (own workflow, warm server)
  /help           this text
  /exit           leave chat (Ctrl-C and Ctrl-D work too)
anything else is a question for the wiki."""


def _now_iso() -> str:
    return datetime.now().isoformat(timespec="seconds")


def _new_session_id() -> str:
    return datetime.now().strftime("%Y%m%d-%H%M%S")


@dataclass
class ChatRepl:
    """One REPL run: an active conversation, counters for the log entry."""

    session: Session
    chat_store: ChatStore
    emit: Callable[[str], None] = print
    active_id: str = ""
    turns: int = 0
    conversations_touched: set[str] = field(default_factory=set)

    def start(self, resume: str | None) -> None:
        if resume is not None:
            target = self.chat_store.latest_session_id() if resume == "latest" else resume
            if target is None or not self.chat_store.session_exists(target):
                self.emit(f"no conversation to resume ({resume}); starting a new one")
                self._create()
            else:
                self.active_id = target
                self.emit(f"resumed conversation {target}")
        else:
            self._create()
        self.emit("type /help for commands")

    async def handle(self, line: str) -> bool:
        """Process one line; returns False when the REPL should exit."""
        text = line.strip()
        if not text:
            return True
        if text == "/exit":
            return False
        if text == "/help":
            self.emit(_HELP)
        elif text == "/new":
            self._create()
        elif text == "/sessions":
            self._list_sessions()
        elif text.startswith("/switch"):
            self._switch(text.removeprefix("/switch").strip())
        elif text.startswith("/file"):
            await self._file(text.removeprefix("/file").strip())
        elif text.startswith("/ingest"):
            await self._operation("ingest", text.removeprefix("/ingest").strip())
        elif text == "/lint":
            await self._operation("lint", "")
        elif text.startswith("/"):
            self.emit(f"unknown command {text.split()[0]!r} — /help lists commands")
        else:
            await self._turn(text)
        return True

    def finish(self) -> None:
        """Graceful-shutdown bookkeeping: one log entry per REPL run."""
        if self.turns:
            count = len(self.conversations_touched)
            self.session.store.append_log(
                self.session.today,
                "chat",
                f"{self.turns} turns across {count} conversation{'s' if count != 1 else ''}",
                f"Conversations: {', '.join(sorted(self.conversations_touched))}. "
                "History in harness/chat.db; transcripts per turn in harness/runs/.",
            )

    # -- internals -------------------------------------------------------------

    def _create(self) -> None:
        base = _new_session_id()
        candidate = base
        suffix = 2
        while self.chat_store.session_exists(candidate):  # same-second /new
            candidate = f"{base}-{suffix}"
            suffix += 1
        self.active_id = self.chat_store.create_session(candidate, _now_iso())
        self.emit(f"new conversation {self.active_id}")

    def _list_sessions(self) -> None:
        sessions = self.chat_store.list_sessions()
        if not sessions:
            self.emit("no conversations yet")
            return
        for info in sessions:
            marker = "*" if info.session_id == self.active_id else " "
            label = info.first_question or "(empty)"
            self.emit(
                f"{marker} {info.session_id}  [{info.turn_count} turns, "
                f"last active {info.last_active_at}]  {label[:60]}"
            )

    def _switch(self, session_id: str) -> None:
        if not session_id:
            self.emit("usage: /switch <id> — /sessions lists ids")
        elif not self.chat_store.session_exists(session_id):
            self.emit(f"no conversation {session_id!r} — /sessions lists ids")
        else:
            self.active_id = session_id
            self.emit(f"switched to {session_id}")

    async def _turn(self, question: str) -> None:
        history = self.chat_store.history(self.active_id)
        window = build_window(history)
        tag = f"chat-{self.active_id}-{self.chat_store.turn_count(self.active_id) + 1:04d}"
        try:
            answer, transcript = await self.session.chat_turn(
                question, window, grounded=not history, tag=tag
            )
        except Exception as exc:  # a failed turn must not kill the REPL
            self.emit(f"[turn failed, nothing persisted] {type(exc).__name__}: {exc}")
            return
        self.chat_store.append_turn(
            self.active_id,
            question,
            answer,
            str(transcript) if transcript else "",
            estimate_tokens(question + answer),
            _now_iso(),
        )
        self.turns += 1
        self.conversations_touched.add(self.active_id)
        self.emit(answer)

    async def _file(self, argument: str) -> None:
        parts = argument.split(maxsplit=1)
        if not parts:
            self.emit("usage: /file <page-name> [scope]")
            return
        history = self.chat_store.history(self.active_id)
        if not history:
            self.emit("nothing to file yet — ask a question first")
            return
        latest = history[-1]
        page_name = parts[0]
        scope = parts[1] if len(parts) > 1 else ""
        tag = f"chat-file-{self.active_id}-{self.chat_store.turn_count(self.active_id):04d}"
        try:
            result = await self.session.file_chat_synthesis(
                page_name=page_name,
                question=latest.question,
                answer=latest.answer,
                scope=scope,
                tag=tag,
            )
        except Exception as exc:  # filing failure must not kill the REPL
            self.emit(f"[file failed] {type(exc).__name__}: {exc}")
            return
        self.conversations_touched.add(self.active_id)
        self.emit(result.output)

    async def _operation(self, op: str, argument: str) -> None:
        if op == "ingest" and not argument:
            self.emit("usage: /ingest <file relative to raw/>")
            return
        try:
            result = (
                await self.session.ingest(argument) if op == "ingest" else await self.session.lint()
            )
            self.emit(result.output)
        except Exception as exc:  # operation failure must not kill the REPL
            self.emit(f"[{op} failed] {type(exc).__name__}: {exc}")
