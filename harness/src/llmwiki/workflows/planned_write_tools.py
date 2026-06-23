"""Planned write_page tool bound to one PagePlan target."""

from __future__ import annotations

from dataclasses import replace

from forge.core.workflow import ToolDef, ToolSpec
from pydantic import BaseModel, Field

from llmwiki.domain.evidence import EvidencePolicy
from llmwiki.domain.objects import PlannedPageWrite
from llmwiki.domain.page_body_contracts import (
    render_page_body_findings,
    validate_page_body,
)
from llmwiki.domain.pages import WikiPage
from llmwiki.store import WikiStore, WikiStoreError
from llmwiki.workflows.source_summary_write import (
    PlannedWriteSourceSummaryParams,
    page_body_contract_source_text,
    source_summary_body_contract,
    source_summary_page_body,
    strip_pipeline_markers,
    write_source_summary_draft_artifact,
)
from llmwiki.workflows.source_summary_write import (
    SourceSummaryBulletParams as SourceSummaryBulletParams,
)


class PlannedWritePageParams(BaseModel):
    page_body: str = Field(
        description="Full PageBody markdown for the planned target page. "
        "Link related pages inline with [[page_id]]. Do not include frontmatter."
    )


def planned_write_page_tool(
    store: WikiStore,
    today: str,
    planned_write: PlannedPageWrite,
    read_tracker: set[str] | None = None,
    write_log: list[str] | None = None,
    evidence_policy: EvidencePolicy | None = None,
) -> ToolDef:
    """write_page variant for PagePlan execution.

    PagePlan owns PageId, PageKind, PageMetadata, and PagePath. The model
    supplies only PageBody.
    """

    target_page = planned_write.page_metadata.page_id
    summary_plan = planned_write.source_summary_plan

    def _write_page_body(page_body: str, *, validate_body: bool = True) -> str:
        page_body = strip_pipeline_markers(page_body)
        body_contract = (
            source_summary_body_contract(planned_write)
            if summary_plan is not None
            else planned_write.resolved_page_body_contract
        )
        if validate_body:
            findings = validate_page_body(
                page_body,
                body_contract,
                source_text=page_body_contract_source_text(store, planned_write),
            )
            if findings:
                raise WikiStoreError(render_page_body_findings(findings, body_contract))
        policy = evidence_policy or EvidencePolicy()
        inventory = store.source_inventory() if policy.enabled else None
        resolver = store.source_resolver() if policy.enabled else None
        evidence = policy.check_page(target_page, page_body, inventory, resolver)
        if not evidence.allowed:
            raise WikiStoreError(
                evidence.render_for_tool(target_page)
                + "\nCorrect the citation path, range, or cited raw source before retrying."
            )
        if (
            read_tracker is not None
            and target_page not in read_tracker
            and target_page in store.list_pages()
        ):
            raise WikiStoreError(
                f"WikiPage '{target_page}' already exists and write_page replaces "
                f"it entirely. Call read_page(page_id='{target_page}') first, "
                "then rewrite it carrying forward the content you keep."
            )
        metadata = replace(planned_write.page_metadata, updated=today)
        page = WikiPage.from_metadata(metadata, page_body)
        store.write_page(page)
        if write_log is not None:
            write_log.append(target_page)
        response = f"Wrote wiki/{store.rendered_page_path(page)} and updated its index entry."
        if evidence.has_warnings:
            response += "\n\n" + evidence.render_for_tool(target_page)
        return response

    def _write_page(**kwargs: object) -> str:
        params = PlannedWritePageParams(**kwargs)  # type: ignore[arg-type]
        return _write_page_body(params.page_body)

    def _write_source_summary(**kwargs: object) -> str:
        params = PlannedWriteSourceSummaryParams(**kwargs)  # type: ignore[arg-type]
        if summary_plan is None:
            raise WikiStoreError("This PlannedPageWrite has no SourceSummaryPlan.")
        body, draft = source_summary_page_body(
            store,
            planned_write,
            params.source_record_text,
            params.claim_bullets,
        )
        result = _write_page_body(body, validate_body=False)
        write_source_summary_draft_artifact(store, planned_write, draft)
        return result

    if summary_plan is not None:
        return ToolDef(
            spec=ToolSpec(
                name="write_page",
                description=f"Write the planned source summary page [[{target_page}]]. "
                "The PagePlan supplies PageId, PageKind, PageMetadata, PagePath, and "
                "SourceSummaryPlan; provide SourceSummaryDraft fields only.",
                parameters=PlannedWriteSourceSummaryParams,
            ),
            callable=_write_source_summary,
        )

    return ToolDef(
        spec=ToolSpec(
            name="write_page",
            description=f"Write the planned target page [[{target_page}]]. "
            "The PagePlan supplies PageId, PageKind, PageMetadata, and PagePath.",
            parameters=PlannedWritePageParams,
        ),
        callable=_write_page,
    )
