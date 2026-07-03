"""Markdown table rendering helpers for PDF recovery."""

from __future__ import annotations


def pipe_table(rows: tuple[tuple[str, ...], ...]) -> str:
    width = max(len(row) for row in rows)
    padded = [tuple((*row, *("" for _ in range(width - len(row))))) for row in rows]
    header = padded[0]
    lines = [
        "| " + " | ".join(header) + " |",
        "| " + " | ".join("---" for _ in header) + " |",
    ]
    lines.extend("| " + " | ".join(row) + " |" for row in padded[1:])
    return "\n".join(lines)
