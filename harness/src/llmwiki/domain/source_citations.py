"""Render source range citations for generated wiki details."""

from __future__ import annotations

from llmwiki.domain.evidence_registry import SourceRange


def source_citation(
    source_range: SourceRange,
    *,
    page_range: tuple[int, int] | None = None,
    line_range: tuple[int, int] | None = None,
) -> str:
    source = source_range.source_path
    if page_range is None and line_range is None:
        page_range = source_range.page_range
        line_range = source_range.line_range
    if page_range is not None:
        start, end = page_range
        suffix = f"p.{start}" if start == end else f"p.{start}-{end}"
        return f"{source} {suffix}"
    if line_range is not None:
        start, end = line_range
        suffix = f"normalized:L{start}" if start == end else f"normalized:L{start}-L{end}"
        return f"{source} {suffix}"
    return source
