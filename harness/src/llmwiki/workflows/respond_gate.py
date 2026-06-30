"""Query response guardrails that Forge cannot express as native steps."""

from __future__ import annotations

from forge.core.workflow import ToolDef
from forge.tools.respond import respond_tool

from llmwiki.domain.chat_grounding import ChatResponseCitationPolicy
from llmwiki.store import WikiStoreError


def respond_after_wiki_read_tool(
    read_tracker: set[str],
    *,
    allow_index_response: bool = True,
    require_wiki_read: bool = True,
    require_read_page_citation: bool = False,
) -> ToolDef:
    """Return respond, gated on reading wiki evidence first."""

    base = respond_tool()

    def _respond(message: str) -> str:
        if not require_wiki_read:
            return str(base.callable(message=message))
        page_reads = read_tracker - {"index.md"}
        if page_reads:
            if require_read_page_citation:
                citation_decision = ChatResponseCitationPolicy(
                    frozenset(page_reads)
                ).response_decision(message)
                if not citation_decision.allowed:
                    raise WikiStoreError(citation_decision.message)
            return str(base.callable(message=message))
        if allow_index_response and "index.md" in read_tracker:
            return str(base.callable(message=message))
        if allow_index_response:
            raise WikiStoreError(
                "Call read_page for a relevant wiki page, or read_index for a "
                "wiki coverage/catalog question, before respond. Search snippets "
                "alone are not enough evidence for an answer."
            )
        raise WikiStoreError(
            "Call read_page for a relevant wiki page before respond. The index "
            "and search snippets are discovery aids, not enough evidence for a "
            "substantive content answer."
        )

    return ToolDef(spec=base.spec, callable=_respond, prerequisites=base.prerequisites)
