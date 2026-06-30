"""Wiki-page helper functions for claim-ledger ingest."""

from __future__ import annotations

from llmwiki.domain.ledger.artifacts import ProjectionCoverageArtifact
from llmwiki.domain.ledger.ledger import ClaimLedger
from llmwiki.domain.ledger.projection_context import ProjectionContext
from llmwiki.domain.ledger.projection_policy import (
    PAGE_FAMILY_SOURCE_MANIFEST,
    topic_projection_policy,
)
from llmwiki.domain.ledger.source_coverage import SourceElementRecord
from llmwiki.domain.ledger.structure import DocumentStructure
from llmwiki.domain.ledger.topic_relations import RelatedTopicLink, related_topic_links
from llmwiki.domain.ledger.topic_render import render_topic_page
from llmwiki.domain.ledger.topics import SourceTopic
from llmwiki.domain.ledger.walkability import audit_related_links
from llmwiki.domain.pages import PageMetadata, WikiPage, slugify
from llmwiki.pdf.document import DocumentModel


def build_topic_pages(
    topics: tuple[SourceTopic, ...],
    ledger: ClaimLedger,
    source_page_id: str,
    source_locator: str,
    today: str,
    related_pages_by_topic: dict[str, tuple[RelatedTopicLink, ...]] | None = None,
    projection_context: ProjectionContext | None = None,
) -> tuple[WikiPage, ...]:
    pages: list[WikiPage] = []
    related_by_topic = related_topic_links(topics, source_page_id=source_page_id)
    extra_related = related_pages_by_topic or {}
    for topic in topics:
        topic_page_id = slugify(f"{source_page_id}-{topic.topic_key}")
        related_pages = tuple(
            dict.fromkeys(
                (
                    *related_by_topic.get(topic.topic_key, ()),
                    *extra_related.get(topic.topic_key, ()),
                )
            )
        )
        walkability = audit_related_links(
            topic_page_id,
            related_pages,
            ledger,
            projection_context=projection_context,
        )
        policy = topic_projection_policy(topic, ledger, projection_context)
        rendered = render_topic_page(
            topic,
            ledger,
            wiki_page_locator=topic_page_id,
            source_page_id=source_page_id,
            related_pages=walkability.accepted_links,
            projection_context=projection_context,
            projection_policy=policy,
        )
        metadata = PageMetadata(
            page_id=topic_page_id,
            page_kind=topic.page_kind,
            page_family=policy.page_family,
            summary=(
                f"{topic.label}: {len(topic.entry_ids)} statement(s) and "
                f"{len(topic.atom_ids)} atom(s) from raw/{source_locator}."
            ),
            sources=(f"raw/{source_locator}",),
            updated=today,
            domain=source_page_id,
            category_path=f"{topic.page_kind}s",
            projection_coverage_pointer=f"topic-{topic_page_id}@{rendered.page_body_hash}",
        )
        pages.append(WikiPage.from_metadata(metadata, rendered.page_body))
    return tuple(pages)


def build_source_wiki_page(
    page_id: str,
    source_locator: str,
    title: str,
    summary: str,
    today: str,
    page_body: str,
    coverage_artifact: ProjectionCoverageArtifact,
) -> WikiPage:
    pointer = (
        f"{coverage_artifact.projection_coverage_artifact_id}"
        f"@{coverage_artifact.projection_coverage_fingerprint}"
    )
    metadata = PageMetadata(
        page_id=page_id,
        page_kind="source",
        page_family=PAGE_FAMILY_SOURCE_MANIFEST,
        summary=summary,
        sources=(f"raw/{source_locator}",),
        updated=today,
        domain=page_id,
        category_path="sources",
        source_id=source_locator,
        projection_coverage_pointer=pointer,
    )
    return WikiPage.from_metadata(metadata, page_body)


def source_element_records(model: DocumentModel) -> tuple[SourceElementRecord, ...]:
    return tuple(
        SourceElementRecord(
            source_element_id=element.element_id,
            element_kind=element.element_kind,
            body_state=element.body_state,
            heading_path=element.heading_path,
            page_locator=_page_locator(element.page_start, element.page_end),
            has_source_text=bool((element.text or element.markdown).strip()),
        )
        for element in model.elements
    )


def source_title(source_locator: str, structure: DocumentStructure) -> str:
    for node in structure.structure_nodes:
        if node.structure_node_kind == "chapter" and node.heading_text.strip():
            return node.heading_text.strip()
    stem = source_locator.rsplit(".", 1)[0].replace("_", " ").replace("-", " ")
    return stem.title()


def ledger_summary(ledger: ClaimLedger, decision: str, linked_page_count: int = 0) -> str:
    usable = len(ledger.usable_entries)
    atoms = len(ledger.technical_atoms)
    review = len(ledger.needs_review_entries)
    label = ledger.source_family_assignment.top_label
    return (
        f"Claim-ledger projection ({label}): {usable} usable entries, {atoms} technical atoms, "
        f"{review} needs-review, {linked_page_count} linked page(s); write decision {decision}."
    )


def _page_locator(page_start: int, page_end: int) -> str:
    if page_start <= 0 or page_end <= 0:
        return "document"
    return f"p.{page_start}" if page_start == page_end else f"p.{page_start}-{page_end}"
