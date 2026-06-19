"""Tools specific to filing durable syntheses from chat."""

from __future__ import annotations

import re

from forge.core.workflow import ToolDef

from llmwiki.store import WikiStore, WikiStoreError
from llmwiki.workflows.tools import WritePageParams, write_page_tool

_WIKI_LINK_RE = re.compile(r"\[\[[^\]]+\]\]")
_RAW_CITATION_RE = re.compile(r"\braw/[A-Za-z0-9._@+\-/]+")
_CHAT_AS_EVIDENCE_RE = re.compile(
    r"\b(chat|conversation|previous answer|prior answer)\b", re.IGNORECASE
)


def chat_file_write_page_tool(
    store: WikiStore,
    today: str,
    read_tracker: set[str],
    prerequisites: list[str | dict[str, str]] | None = None,
) -> ToolDef:
    """Write a synthesis page, rejecting chat history as cited evidence."""

    base = write_page_tool(
        store,
        today,
        prerequisites=prerequisites,
        read_tracker=read_tracker,
    )

    def _write_page(**kwargs: object) -> str:
        params = WritePageParams(**kwargs)  # type: ignore[arg-type]
        evidence_text = "\n".join([params.page_body, *params.sources])
        slug_sources = [source for source in params.sources if _looks_like_wiki_slug(source)]
        if slug_sources:
            joined = ", ".join(slug_sources)
            raise WikiStoreError(
                "write_page sources must be raw source paths, not wiki page "
                f"names: {joined}. Link wiki evidence in the body with [[page]] "
                "and list only raw files in sources."
            )
        if _CHAT_AS_EVIDENCE_RE.search(evidence_text):
            raise WikiStoreError(
                "Chat history is context, not source evidence. Re-read current "
                "wiki pages and cite those pages or raw sources instead."
            )
        if (
            _WIKI_LINK_RE.search(params.page_body) is None
            and _RAW_CITATION_RE.search(params.page_body) is None
        ):
            raise WikiStoreError(
                "Filed chat syntheses must cite current wiki pages with [[page]] "
                "links or raw sources with raw/<source_locator> citations."
            )
        return str(base.callable(**kwargs))

    return ToolDef(spec=base.spec, callable=_write_page, prerequisites=base.prerequisites)


def _looks_like_wiki_slug(source: str) -> bool:
    return "/" not in source and "." not in source
