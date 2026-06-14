"""log.md entries. Format defined in SCHEMA.md: grep-able `## [date] op | subject`."""

from __future__ import annotations

_SUBJECT_MAX = 80


def format_log_entry(date_iso: str, op: str, subject: str, detail: str) -> str:
    """Render one append-only log entry.

    The prefix is kept to a single line so that
    `grep "^## \\[" wiki/log.md | tail -5` lists recent activity.
    """
    one_line = " ".join(subject.split())
    if len(one_line) > _SUBJECT_MAX:
        one_line = one_line[: _SUBJECT_MAX - 1] + "…"
    body = detail.strip()
    return f"\n## [{date_iso}] {op} | {one_line}\n{body}\n"
