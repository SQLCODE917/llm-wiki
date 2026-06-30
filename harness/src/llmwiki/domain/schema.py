"""Shared Schema defaults for local LLM-Wiki."""

from __future__ import annotations

PAGE_KINDS = ("source", "entity", "concept", "synthesis")

PAGE_FAMILIES = (
    "source-manifest",
    "source-summary",
    "section-reference",
    "topic-concept",
    "broad-topic",
    "entity-profile",
    "cross-source-synthesis",
)

PAGE_KIND_HEADINGS = {
    "source": "## Sources",
    "entity": "## Entities",
    "concept": "## Concepts",
    "synthesis": "## Syntheses",
}

PAGE_METADATA_FIELDS = (
    "PageId",
    "PageKind",
    "PageFamily",
    "Summary",
    "Sources",
    "Updated",
)
