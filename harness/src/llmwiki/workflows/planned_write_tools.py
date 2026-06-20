"""Planned write_page tool bound to one PagePlan target."""

from __future__ import annotations

from dataclasses import replace

from forge.core.workflow import ToolDef, ToolSpec
from pydantic import BaseModel, Field

from llmwiki.domain.evidence import EvidencePolicy
from llmwiki.domain.objects import PlannedPageWrite
from llmwiki.domain.page_body_contracts import render_page_body_findings, validate_page_body
from llmwiki.domain.pages import WikiPage
from llmwiki.pdf.intermediate import OCR_MARKER
from llmwiki.store import WikiStore, WikiStoreError


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

    def _write_page(**kwargs: object) -> str:
        params = PlannedWritePageParams(**kwargs)  # type: ignore[arg-type]
        page_body = _strip_pipeline_markers(params.page_body)
        findings = validate_page_body(
            page_body,
            planned_write.resolved_page_body_contract,
            source_text=_page_body_contract_source_text(store, planned_write),
        )
        if findings:
            raise WikiStoreError(
                render_page_body_findings(findings, planned_write.resolved_page_body_contract)
            )
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

    return ToolDef(
        spec=ToolSpec(
            name="write_page",
            description=f"Write the planned target page [[{target_page}]]. "
            "The PagePlan supplies PageId, PageKind, PageMetadata, and PagePath.",
            parameters=PlannedWritePageParams,
        ),
        callable=_write_page,
    )


def _page_body_contract_source_text(store: WikiStore, planned_write: PlannedPageWrite) -> str:
    if not planned_write.evidence:
        return ""
    raw_source = planned_write.evidence[0].raw_source
    if raw_source.source_format != "markdown":
        return ""
    return store.read_source(raw_source.source_locator)


def _strip_pipeline_markers(page_body: str) -> str:
    return "\n".join(line for line in page_body.splitlines() if OCR_MARKER not in line)
