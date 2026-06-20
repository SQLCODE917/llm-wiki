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
from llmwiki.domain.ingest_profiles import (
    IngestProfile,
    compose_prompt,
    prevents_singular_plural_siblings,
)
from llmwiki.domain.ingest_route_plan import IngestRouteContext, IngestRoutePlanState
from llmwiki.domain.pages import slugify
from llmwiki.store import WikiStore
from llmwiki.workflows import prompts
from llmwiki.workflows.fixed_page_tools import write_fixed_source_page_tool
from llmwiki.workflows.ingest_route_tools import plan_pages_tool
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
    source_locator: str = "",
    new_page_prefix: str | None = None,
    chunk_id: int | None = None,
    ingest_route_plan_state: IngestRoutePlanState | None = None,
    recoverable_tool_errors: bool = False,
) -> Workflow:
    seen: set[str] = set()  # read-before-rewrite contract, per run
    prevent_siblings = prevents_singular_plural_siblings(profiles)
    if ingest_route_plan_state is None:
        ingest_route_plan_state = IngestRoutePlanState(
            IngestRouteContext(
                source_locator=source_locator,
                scope="pdf-chunk",
                profile_ids=tuple(profile.id for profile in profiles),
                chunk_id=chunk_id,
                existing_pages=frozenset(store.list_pages()),
                new_page_prefix=new_page_prefix,
                prevent_singular_plural_siblings=prevent_siblings,
            )
        )
    tools = [
        search_wiki_tool(store),
        read_page_tool(
            store,
            read_tracker=seen,
            max_chars=2000,
            track_truncated_reads=False,
        ),
        plan_pages_tool(ingest_route_plan_state, recoverable_errors=recoverable_tool_errors),
        write_page_tool(
            store,
            today,
            prerequisites=["search_wiki", "plan_pages"],
            read_tracker=seen,
            write_log=write_log,
            evidence_policy=evidence_policy,
            new_page_prefix=new_page_prefix,
            prevent_singular_plural_siblings=prevent_siblings,
            ingest_route_plan_state=ingest_route_plan_state,
            recoverable_errors=recoverable_tool_errors,
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
        required_steps=["search_wiki", "plan_pages", "write_page"],
        terminal_tool="finish_chunk",
        system_prompt_template=compose_prompt(
            prompts.MAP_TEMPLATE,
            profiles,
            "pdf_map",
            source_locator,
        ),
    )


def build_integrate_workflow(
    store: WikiStore,
    today: str,
    evidence_policy: EvidencePolicy | None = None,
    profiles: tuple[IngestProfile, ...] = (),
    source_locator: str = "",
    new_page_prefix: str | None = None,
    required_link_targets: tuple[str, ...] = (),
    min_required_links: int = 0,
    ingest_route_plan_state: IngestRoutePlanState | None = None,
    recoverable_tool_errors: bool = False,
) -> Workflow:
    seen: set[str] = set()
    hub_page = slugify(source_locator.rsplit(".", maxsplit=1)[0]) if source_locator else ""
    if ingest_route_plan_state is None:
        ingest_route_plan_state = IngestRoutePlanState(
            IngestRouteContext(
                source_locator=source_locator,
                scope="pdf-integrate",
                profile_ids=tuple(profile.id for profile in profiles),
                existing_pages=frozenset(store.list_pages()),
                new_page_prefix=new_page_prefix,
                prevent_singular_plural_siblings=prevents_singular_plural_siblings(profiles),
            )
        )
    tools = [
        search_wiki_tool(store),
        read_page_tool(
            store,
            read_tracker=seen,
            max_chars=4000,
            track_truncated_reads=False,
        ),
        plan_pages_tool(ingest_route_plan_state, recoverable_errors=recoverable_tool_errors),
        write_fixed_source_page_tool(
            store,
            today,
            page_id=hub_page,
            read_tracker=seen,
            evidence_policy=evidence_policy,
            new_page_prefix=new_page_prefix,
            required_link_targets=required_link_targets,
            min_required_links=min_required_links,
            ingest_route_plan_state=ingest_route_plan_state,
            recoverable_errors=recoverable_tool_errors,
        ),
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
        required_steps=["plan_pages", "write_page"],
        terminal_tool="finish_ingest",
        system_prompt_template=compose_prompt(
            prompts.INTEGRATE_TEMPLATE,
            profiles,
            "pdf_integrate",
            source_locator,
        ),
    )
