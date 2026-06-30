"""Chat-specific tool adapters."""

from __future__ import annotations

from forge.core.workflow import ToolDef, ToolSpec

from llmwiki.domain.chat_grounding import ChatEvidenceScope
from llmwiki.domain.pages import parse_page
from llmwiki.store import WikiStore, WikiStoreError
from llmwiki.workflows.tools import ReadPageParams


def chat_read_page_tool(
    store: WikiStore,
    *,
    evidence_scope: ChatEvidenceScope | None = None,
    read_tracker: set[str] | None = None,
) -> ToolDef:
    def _read_page(**kwargs: object) -> str:
        params = ReadPageParams(**kwargs)  # type: ignore[arg-type]
        text = store.read_page(params.page_id)
        if evidence_scope is not None:
            metadata = parse_page(text).page_metadata
            decision = evidence_scope.read_decision(metadata)
            if not decision.allowed:
                raise WikiStoreError(decision.message)
        if read_tracker is not None:
            read_tracker.add(params.page_id)
        return text

    return ToolDef(
        spec=ToolSpec(
            name="read_page",
            description=(
                "Read the full text of one wiki page. For focused chat lookups, "
                "broad aggregate pages may be rejected when more focused pages "
                "are available."
            ),
            parameters=ReadPageParams,
        ),
        callable=_read_page,
    )
