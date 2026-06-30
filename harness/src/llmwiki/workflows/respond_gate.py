"""Query response guardrails that Forge cannot express as native steps."""

from __future__ import annotations

from forge.core.workflow import ToolDef
from forge.tools.respond import respond_tool

from llmwiki.domain.chat_grounding import ChatResponseCitationPolicy
from llmwiki.store import WikiStoreError
from llmwiki.workflows.procedure_execution_tools import ProcedureExecutionState


def respond_after_wiki_read_tool(
    read_tracker: set[str],
    *,
    allow_index_response: bool = True,
    require_wiki_read: bool = True,
    require_read_page_citation: bool = False,
    procedure_execution_state: ProcedureExecutionState | None = None,
    require_procedure_execution: bool = False,
) -> ToolDef:
    """Return respond, gated on reading wiki evidence first."""

    base = respond_tool()

    def _respond(message: str) -> str:
        if (
            require_procedure_execution
            and procedure_execution_state is not None
            and not procedure_execution_state.has_valid_execution
        ):
            raise WikiStoreError(
                "Call submit_procedure_execution with a valid ProcedureExecution "
                "before respond. A procedure execution answer must be validated "
                "against the deterministic task evidence pack first."
            )
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
