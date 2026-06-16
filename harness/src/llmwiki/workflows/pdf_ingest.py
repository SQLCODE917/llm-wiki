"""Map and integrate workflows for chunked (PDF) ingest.

Guardrail contracts:
- map: must search_wiki and write_page before finish_chunk — every chunk
  leaves real knowledge in the wiki, not just notes. No read_source tool,
  so the model cannot pull the whole book into context.
- integrate: must write_page (the hub source page) before finish_ingest.
"""

from __future__ import annotations

from forge.core.workflow import Workflow

from llmwiki.domain.evidence import EvidencePolicy
from llmwiki.domain.ingest_profiles import IngestProfile, compose_prompt
from llmwiki.store import WikiStore
from llmwiki.workflows import prompts
from llmwiki.workflows.tools import (
    finish_tool,
    read_page_tool,
    search_wiki_tool,
    write_page_tool,
)


def build_map_workflow(
    store: WikiStore,
    today: str,
    write_log: list[str] | None = None,
    evidence_policy: EvidencePolicy | None = None,
    profiles: tuple[IngestProfile, ...] = (),
    source_path: str = "",
) -> Workflow:
    seen: set[str] = set()  # read-before-rewrite contract, per run
    tools = [
        search_wiki_tool(store),
        read_page_tool(store, read_tracker=seen),
        write_page_tool(
            store,
            today,
            read_tracker=seen,
            write_log=write_log,
            evidence_policy=evidence_policy,
        ),
        finish_tool(
            "finish_chunk",
            "Finish this chunk after the wiki reflects it. Report concise "
            "notes: key claims, entities touched, pages written.",
        ),
    ]
    return Workflow(
        name="pdf-map",
        description="Integrate one chunk of a larger source into the wiki.",
        tools={t.name: t for t in tools},
        required_steps=["search_wiki", "write_page"],
        terminal_tool="finish_chunk",
        system_prompt_template=compose_prompt(
            prompts.MAP_TEMPLATE,
            profiles,
            "pdf_map",
            source_path,
        ),
    )


def build_integrate_workflow(
    store: WikiStore,
    today: str,
    evidence_policy: EvidencePolicy | None = None,
    profiles: tuple[IngestProfile, ...] = (),
    source_path: str = "",
) -> Workflow:
    seen: set[str] = set()
    tools = [
        search_wiki_tool(store),
        read_page_tool(store, read_tracker=seen),
        write_page_tool(store, today, read_tracker=seen, evidence_policy=evidence_policy),
        finish_tool(
            "finish_ingest",
            "Finish the chunked ingest after the hub source page exists and "
            "cross-links are in place. Report the final page structure.",
        ),
    ]
    return Workflow(
        name="pdf-integrate",
        description="Consolidate a chunked ingest into a coherent source hub.",
        tools={t.name: t for t in tools},
        required_steps=["write_page"],
        terminal_tool="finish_ingest",
        system_prompt_template=compose_prompt(
            prompts.INTEGRATE_TEMPLATE,
            profiles,
            "pdf_integrate",
            source_path,
        ),
    )
