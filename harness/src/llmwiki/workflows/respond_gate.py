"""Query response guardrails that Forge cannot express as native steps."""

from __future__ import annotations

from forge.core.workflow import ToolDef
from forge.tools.respond import respond_tool

from llmwiki.domain.chat_response_gate import (
    ChatResponseEvidenceState,
    ChatResponseGateConfig,
    decide_chat_response,
)
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
    missing_focus_reports: set[str] | None = None,
) -> ToolDef:
    """Return respond, gated on reading wiki evidence first."""

    base = respond_tool()

    def _respond(message: str) -> str:
        decision = decide_chat_response(
            message,
            config=ChatResponseGateConfig(
                allow_index_response=allow_index_response,
                require_wiki_read=require_wiki_read,
                require_read_page_citation=require_read_page_citation,
                require_procedure_execution=require_procedure_execution,
            ),
            evidence=ChatResponseEvidenceState(
                missing_focus_reports=frozenset(missing_focus_reports or ()),
                read_page_ids=frozenset(read_tracker - {"index.md"}),
                index_was_read="index.md" in read_tracker,
                procedure_execution_satisfied=(
                    procedure_execution_state is not None
                    and procedure_execution_state.has_valid_execution
                ),
            ),
        )
        if not decision.allowed:
            raise WikiStoreError(decision.message)
        return str(base.callable(message=message))

    return ToolDef(spec=base.spec, callable=_respond, prerequisites=base.prerequisites)
