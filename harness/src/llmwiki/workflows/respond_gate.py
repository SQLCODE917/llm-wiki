"""Query response guardrails that Forge cannot express as native steps."""

from __future__ import annotations

from forge.core.workflow import ToolDef
from forge.tools.respond import respond_tool

from llmwiki.store import WikiStoreError


def respond_after_wiki_read_tool(read_tracker: set[str]) -> ToolDef:
    """Return respond, gated on reading either a page or the index first."""

    base = respond_tool()

    def _respond(message: str) -> str:
        if not read_tracker:
            raise WikiStoreError(
                "Call read_page for a relevant wiki page, or read_index for a "
                "wiki coverage/catalog question, before respond. Search snippets "
                "alone are not enough evidence for an answer."
            )
        return str(base.callable(message=message))

    return ToolDef(spec=base.spec, callable=_respond, prerequisites=base.prerequisites)
