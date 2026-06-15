"""The three wiki operations as forge Workflows.

Guardrail contracts (enforced by forge's StepEnforcer, not by prompting):
- ingest: must read_source, search_wiki, and write_page before finish_ingest;
  write_page is gated on a prior source read and wiki search.
- query: respond is gated on a prior read_page or read_index call; search is
  available for finding pages but is not forced after a valid index read.
- lint: must read_page before finish_lint (no drive-by sign-off).
"""

from __future__ import annotations

from forge.core.workflow import Workflow
from forge.tools.respond import respond_tool

from llmwiki.domain.contradictions import ContradictionFinding
from llmwiki.domain.evidence import EvidencePolicy
from llmwiki.store import WikiStore
from llmwiki.workflows import prompts
from llmwiki.workflows.contradiction_tools import record_contradiction_tool
from llmwiki.workflows.respond_gate import respond_after_wiki_read_tool
from llmwiki.workflows.tools import (
    finish_tool,
    link_orphan_tool,
    read_index_tool,
    read_page_tool,
    read_source_tool,
    search_wiki_tool,
    write_page_tool,
)


def build_ingest_workflow(
    store: WikiStore, today: str, evidence_policy: EvidencePolicy | None = None
) -> Workflow:
    seen: set[str] = set()  # read-before-rewrite contract, per run
    tools = [
        read_source_tool(store),
        search_wiki_tool(store),
        read_page_tool(store, read_tracker=seen),
        write_page_tool(
            store,
            today,
            prerequisites=["read_source", "search_wiki"],
            read_tracker=seen,
            evidence_policy=evidence_policy,
        ),
        finish_tool(
            "finish_ingest",
            "Finish the ingest after the wiki fully reflects the source. "
            "Report which pages were written or updated.",
        ),
    ]
    return Workflow(
        name="ingest",
        description="Integrate one raw source into the wiki.",
        tools={t.name: t for t in tools},
        required_steps=["read_source", "search_wiki", "write_page"],
        terminal_tool="finish_ingest",
        system_prompt_template=prompts.INGEST_TEMPLATE,
    )


def build_query_workflow(
    store: WikiStore, today: str, evidence_policy: EvidencePolicy | None = None
) -> Workflow:
    seen: set[str] = set()
    tools = [
        search_wiki_tool(store),
        read_index_tool(store, read_tracker=seen),
        read_page_tool(store, read_tracker=seen),
        write_page_tool(store, today, read_tracker=seen, evidence_policy=evidence_policy),
        respond_after_wiki_read_tool(seen),
    ]
    return Workflow(
        name="query",
        description="Answer a question from the wiki with citations.",
        tools={t.name: t for t in tools},
        required_steps=[],
        terminal_tool="respond",
        system_prompt_template=prompts.QUERY_TEMPLATE,
    )


def build_chat_workflow(store: WikiStore) -> Workflow:
    """Read-only by construction: no write tool exists in this workflow.

    Grounding is provisioned, not enforced: the orchestrator prepends the
    wiki index to a conversation's first message (pattern doc: read the
    index first, then drill into pages). A required-search step was tried
    and removed — live, it interrupted a correct index-first flow, forced
    a junk search, and the model answered from the junk (recency wins in
    a 14B).
    """
    tools = [
        search_wiki_tool(store),
        read_index_tool(store),
        read_page_tool(store),
        respond_tool(),
    ]
    return Workflow(
        name="chat",
        description="Converse over the wiki (read-only).",
        tools={t.name: t for t in tools},
        required_steps=[],
        terminal_tool="respond",
        system_prompt_template=prompts.CHAT_TEMPLATE,
    )


def build_lint_workflow(
    store: WikiStore, today: str, evidence_policy: EvidencePolicy | None = None
) -> Workflow:
    seen: set[str] = set()
    tools = [
        search_wiki_tool(store),
        read_page_tool(store, read_tracker=seen),
        link_orphan_tool(store, today),
        write_page_tool(store, today, read_tracker=seen, evidence_policy=evidence_policy),
        finish_tool(
            "finish_lint",
            "Finish the lint pass with a concise wiki health report: issues "
            "found, fixes applied, suggested next steps.",
        ),
    ]
    return Workflow(
        name="lint",
        description="Health-check the wiki and repair what page edits can repair.",
        tools={t.name: t for t in tools},
        required_steps=["read_page"],
        terminal_tool="finish_lint",
        system_prompt_template=prompts.LINT_TEMPLATE,
    )


def build_contradiction_workflow(
    store: WikiStore, findings: list[ContradictionFinding]
) -> Workflow:
    tools = [
        read_page_tool(store),
        record_contradiction_tool(store, findings),
        finish_tool(
            "finish_contradictions",
            "Finish the contradiction audit with scope, findings recorded, "
            "uncertainty, and curator next steps.",
        ),
    ]
    return Workflow(
        name="contradictions",
        description="Audit selected wiki page pairs for semantic contradictions.",
        tools={t.name: t for t in tools},
        required_steps=["read_page"],
        terminal_tool="finish_contradictions",
        system_prompt_template=prompts.CONTRADICTIONS_TEMPLATE,
    )
