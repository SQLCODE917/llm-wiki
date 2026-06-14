"""ChatStore: SQLite persistence for conversations (sessions + turns).

The preservation guarantee lives here: turns are stored verbatim and
append-only; everything navigational (labels, latest, listings) is derived
by query, never duplicated into stored state. Conversations are never
"closed" — only dormant, resumable forever.
"""

from __future__ import annotations

import sqlite3
from dataclasses import dataclass
from pathlib import Path

from llmwiki.domain.chatwindow import QAPair

SCHEMA_VERSION = 1

_SCHEMA = """
CREATE TABLE IF NOT EXISTS sessions (
    id             TEXT PRIMARY KEY,
    created_at     TEXT NOT NULL,
    last_active_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS turns (
    session_id      TEXT NOT NULL REFERENCES sessions(id),
    idx             INTEGER NOT NULL,
    question        TEXT NOT NULL,
    answer          TEXT NOT NULL,
    transcript_path TEXT NOT NULL,
    token_estimate  INTEGER NOT NULL,
    created_at      TEXT NOT NULL,
    PRIMARY KEY (session_id, idx)
);
"""


@dataclass(frozen=True)
class SessionInfo:
    session_id: str
    created_at: str
    last_active_at: str
    turn_count: int
    first_question: str  # derived label; empty for a fresh conversation


class ChatStoreError(Exception):
    """Chat persistence failure; message is safe to show the user."""


class ChatStore:
    def __init__(self, db_path: Path) -> None:
        db_path.parent.mkdir(parents=True, exist_ok=True)
        self._conn = sqlite3.connect(db_path)
        self._conn.executescript(_SCHEMA)
        if self._conn.execute("PRAGMA user_version").fetchone()[0] == 0:
            self._conn.execute(f"PRAGMA user_version = {SCHEMA_VERSION}")
        self._conn.commit()

    def close(self) -> None:
        self._conn.close()

    # -- conversations -------------------------------------------------------

    def create_session(self, session_id: str, now_iso: str) -> str:
        try:
            self._conn.execute(
                "INSERT INTO sessions (id, created_at, last_active_at) VALUES (?, ?, ?)",
                (session_id, now_iso, now_iso),
            )
        except sqlite3.IntegrityError as exc:
            raise ChatStoreError(f"conversation {session_id!r} already exists") from exc
        self._conn.commit()
        return session_id

    def session_exists(self, session_id: str) -> bool:
        row = self._conn.execute("SELECT 1 FROM sessions WHERE id = ?", (session_id,)).fetchone()
        return row is not None

    def latest_session_id(self) -> str | None:
        row = self._conn.execute(
            "SELECT id FROM sessions ORDER BY last_active_at DESC, id DESC LIMIT 1"
        ).fetchone()
        return row[0] if row else None

    def list_sessions(self) -> list[SessionInfo]:
        rows = self._conn.execute(
            """
            SELECT s.id, s.created_at, s.last_active_at,
                   (SELECT COUNT(*) FROM turns t WHERE t.session_id = s.id),
                   COALESCE((SELECT t.question FROM turns t
                             WHERE t.session_id = s.id AND t.idx = 1), '')
            FROM sessions s
            ORDER BY s.last_active_at DESC, s.id DESC
            """
        ).fetchall()
        return [SessionInfo(*row) for row in rows]

    # -- turns ----------------------------------------------------------------

    def history(self, session_id: str) -> list[QAPair]:
        rows = self._conn.execute(
            "SELECT question, answer FROM turns WHERE session_id = ? ORDER BY idx",
            (session_id,),
        ).fetchall()
        return [QAPair(question=q, answer=a) for q, a in rows]

    def turn_count(self, session_id: str) -> int:
        row = self._conn.execute(
            "SELECT COUNT(*) FROM turns WHERE session_id = ?", (session_id,)
        ).fetchone()
        return int(row[0])

    def append_turn(
        self,
        session_id: str,
        question: str,
        answer: str,
        transcript_path: str,
        token_estimate: int,
        now_iso: str,
    ) -> int:
        """Persist one completed turn verbatim; returns its 1-based index."""
        if not self.session_exists(session_id):
            raise ChatStoreError(f"no conversation {session_id!r}")
        idx = self.turn_count(session_id) + 1
        self._conn.execute(
            "INSERT INTO turns (session_id, idx, question, answer, transcript_path,"
            " token_estimate, created_at) VALUES (?, ?, ?, ?, ?, ?, ?)",
            (session_id, idx, question, answer, transcript_path, token_estimate, now_iso),
        )
        self._conn.execute(
            "UPDATE sessions SET last_active_at = ? WHERE id = ?", (now_iso, session_id)
        )
        self._conn.commit()
        return idx
