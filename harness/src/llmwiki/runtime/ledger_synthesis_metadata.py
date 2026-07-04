"""Metadata helpers for synthesized ledger projection pages."""

from __future__ import annotations

import re

from llmwiki.domain.ledger.collection_pages import CollectionPlan
from llmwiki.domain.ledger.coverage import RenderedPage
from llmwiki.domain.ledger.page_synthesis import PageSynthesisPlan
from llmwiki.domain.ledger.procedures import ProcedureGuide, procedure_aliases
from llmwiki.domain.ledger.topic_models import SourceTopic
from llmwiki.domain.pages import PageMetadata, slugify


def topic_metadata(
    plan: PageSynthesisPlan, topic: SourceTopic, source_locator: str, today: str
) -> PageMetadata:
    return PageMetadata(
        page_id=plan.page_id,
        page_kind=plan.page_kind,
        page_family=plan.page_family,
        summary=f"{topic.label}: synthesized source-backed topic page from raw/{source_locator}.",
        sources=(f"raw/{source_locator}",),
        updated=today,
        domain=plan.source_page_id,
        category_path=f"{topic.page_kind}s",
    )


def procedure_metadata(
    plan: PageSynthesisPlan, guide: ProcedureGuide, source_locator: str, today: str
) -> PageMetadata:
    return PageMetadata(
        page_id=plan.page_id,
        page_kind="procedure",
        page_family=plan.page_family,
        summary=f"{plan.title}: synthesized procedure guide from raw/{source_locator}.",
        sources=(f"raw/{source_locator}",),
        updated=today,
        domain=plan.source_page_id,
        category_path=f"procedures/{plan.source_page_id}",
        source_id=source_locator,
        aliases=procedure_aliases(guide),
    )


def recipe_metadata(
    plan: PageSynthesisPlan, title: str, source_locator: str, today: str
) -> PageMetadata:
    return PageMetadata(
        page_id=plan.page_id,
        page_kind="recipe",
        page_family=plan.page_family,
        summary=f"{title}: synthesized recipe pattern from raw/{source_locator}.",
        sources=(f"raw/{source_locator}",),
        updated=today,
        domain=plan.source_page_id,
        category_path=f"recipes/{plan.source_page_id}",
        source_id=source_locator,
        aliases=(slugify(title),),
    )


def collection_metadata(
    plan: PageSynthesisPlan, collection: CollectionPlan, source_locator: str, today: str
) -> PageMetadata:
    return PageMetadata(
        page_id=plan.page_id,
        page_kind="source",
        page_family=plan.page_family,
        summary=f"{collection.title}: synthesized collection page from raw/{source_locator}.",
        sources=(f"raw/{source_locator}",),
        updated=today,
        domain=plan.source_page_id,
        category_path=f"sources/{plan.source_page_id}/collections",
        source_id=source_locator,
    )


def with_synthesis_coverage(
    metadata: PageMetadata, plan: PageSynthesisPlan, rendered: RenderedPage
) -> PageMetadata:
    return PageMetadata(
        page_id=metadata.page_id,
        page_kind=metadata.page_kind,
        summary=_navigation_summary_from_accepted_page(plan, rendered),
        page_family=metadata.page_family,
        sources=metadata.sources,
        updated=metadata.updated,
        domain=metadata.domain,
        category_path=metadata.category_path,
        project_id=metadata.project_id,
        source_id=metadata.source_id,
        tags=metadata.tags,
        aliases=metadata.aliases,
        projection_coverage_pointer=f"page-synthesis-{plan.page_id}@{rendered.page_body_hash}",
    )


def _navigation_summary_from_accepted_page(
    plan: PageSynthesisPlan, rendered: RenderedPage
) -> str:
    for line in rendered.page_body.splitlines():
        cleaned = _navigation_preview_line(line)
        if cleaned and cleaned != plan.title:
            return _trim_preview(f"{plan.title}: {cleaned}")
    return f"{plan.title}: accepted synthesized page from raw/{plan.source_locator}."


_MARKDOWN_LINK_RE = re.compile(r"\[\[([^\]]+)]]")
_CITATION_RE = re.compile(r"\s+_\([^_]*\)_")


def _navigation_preview_line(line: str) -> str:
    stripped = line.strip()
    if not stripped or stripped.startswith("#"):
        return ""
    if stripped.startswith("- Source ") or stripped.startswith("## Source Trail"):
        return ""
    stripped = re.sub(r"^\d+\.\s+", "", stripped)
    stripped = stripped.removeprefix("- ").strip()
    stripped = _CITATION_RE.sub("", stripped)
    stripped = _MARKDOWN_LINK_RE.sub(r"\1", stripped)
    return " ".join(stripped.split()).strip()


def _trim_preview(text: str, max_chars: int = 180) -> str:
    if len(text) <= max_chars:
        return text
    return text[:max_chars].rsplit(" ", 1)[0].rstrip(" ,;:") + "..."
