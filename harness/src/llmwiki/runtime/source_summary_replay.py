"""Replay accepted source-summary drafts into current generated pages."""

from __future__ import annotations

from dataclasses import dataclass, replace
from pathlib import Path

from llmwiki.domain.objects import PagePlan, PlannedPageWrite, SourceSummaryDraft
from llmwiki.domain.pages import WikiPage, slugify
from llmwiki.pdf.manifest import ChunkRecord
from llmwiki.store import WikiStore, WikiStoreError
from llmwiki.workflows.source_summary_write import source_summary_page_body_from_draft


@dataclass(frozen=True)
class SourceSummaryReplay:
    page_ids: tuple[str, ...]
    notes: str


def replay_source_summary_work_unit(
    store: WikiStore,
    today: str,
    source_locator: str,
    page_plan: PagePlan,
    records: tuple[ChunkRecord, ...],
) -> SourceSummaryReplay | None:
    hub_page_id = slugify(Path(source_locator).stem)
    writes = _source_summary_writes(page_plan, records, hub_page_id)
    if not writes:
        return None
    draft_index = _drafts_by_write_id(store, source_locator)
    rendered_pages: list[WikiPage] = []
    for write in writes:
        draft = draft_index.get(write.write_id)
        if draft is None:
            return None
        if not _draft_claims_match_plan(write, draft):
            return None
        try:
            body, _ = source_summary_page_body_from_draft(
                store, write, draft, allow_accepted_artifact_shape=True
            )
        except WikiStoreError:
            return None
        rendered_pages.append(
            WikiPage(
                page_metadata=replace(write.page_metadata, updated=today),
                page_body=body,
            )
        )
    for page in rendered_pages:
        store.write_page(page)
    page_ids = tuple(page.page_metadata.page_id for page in rendered_pages)
    return SourceSummaryReplay(
        page_ids=page_ids,
        notes="Replayed accepted source-summary draft artifact(s): " + ", ".join(page_ids),
    )


def _source_summary_writes(
    page_plan: PagePlan, records: tuple[ChunkRecord, ...], hub_page_id: str
) -> tuple[PlannedPageWrite, ...]:
    unit_ids = {f"unit-{record.chunk_id:04d}" for record in records}
    writes = tuple(
        write
        for write in page_plan.planned_writes
        if write.action != "defer"
        and write.page_metadata.page_id != hub_page_id
        and write.source_summary_plan is not None
        and unit_ids.intersection(write.extracted_units)
    )
    expected_page_ids = {
        write.page_metadata.page_id
        for write in page_plan.planned_writes
        if write.action != "defer"
        and write.page_metadata.page_id != hub_page_id
        and unit_ids.intersection(write.extracted_units)
    }
    if {write.page_metadata.page_id for write in writes} != expected_page_ids:
        return ()
    return tuple(dict.fromkeys(writes))


def _drafts_by_write_id(store: WikiStore, source_locator: str) -> dict[str, SourceSummaryDraft]:
    return {
        artifact.write_id: artifact.draft
        for artifact in store.read_source_summary_draft_artifacts(source_locator)
    }


def _draft_claims_match_plan(write: PlannedPageWrite, draft: SourceSummaryDraft) -> bool:
    if write.source_summary_plan is None:
        return False
    selected = set(write.source_summary_plan.selected_source_claims)
    covered = {
        claim_id for bullet in draft.claim_bullets for claim_id in bullet.covered_source_claims
    }
    return not covered or covered <= selected
