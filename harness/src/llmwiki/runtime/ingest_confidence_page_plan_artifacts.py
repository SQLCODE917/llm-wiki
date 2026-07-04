"""Build current PagePlan and EvidenceRegistry artifacts for confidence runs."""

from __future__ import annotations

from pathlib import Path

from llmwiki.domain.evidence_registry import (
    EvidenceRegistry,
    SourceText,
    build_evidence_registry,
    source_text_from_text,
)
from llmwiki.domain.ingest_profiles import IngestProfile, required_new_page_prefix
from llmwiki.domain.objects import (
    PagePlan,
    Schema,
    SourceBundle,
    SourcePlan,
)
from llmwiki.domain.pages import slugify
from llmwiki.domain.planning import build_markdown_page_plan, build_page_plan
from llmwiki.pdf.pipeline import ExtractionResult, read_source_text
from llmwiki.runtime.pdf_source_units import extracted_units_from_pdf_cache
from llmwiki.store import WikiStore


def build_current_page_plan(
    store: WikiStore,
    source_locator: str,
    today: str,
    profiles: tuple[IngestProfile, ...],
    pdf_result: ExtractionResult | None,
) -> PagePlan | None:
    raw_source = store.raw_source(source_locator)
    source_plan = SourcePlan(raw_source, raw_source.source_format, "plan-pages")
    if source_locator.lower().endswith(".pdf"):
        if pdf_result is None:
            return None
        try:
            units = extracted_units_from_pdf_cache(raw_source, pdf_result.cache_dir)
        except ValueError:
            return None
        return build_page_plan(
            plan_id=f"{today}-confidence-pdf-{slugify(Path(source_locator).stem)}",
            source_bundle=SourceBundle.one(raw_source),
            raw_source=raw_source,
            extracted_units=units,
            existing_pages=store.page_texts(),
            wiki_structure=store.structure,
            today=today,
            source_plan=source_plan,
            new_page_prefix=required_new_page_prefix(profiles, source_locator)
            or slugify(Path(source_locator).stem),
        )
    return build_markdown_page_plan(
        plan_id=f"{today}-confidence-source-{slugify(Path(source_locator).stem)}",
        source_bundle=SourceBundle.one(raw_source),
        raw_source=raw_source,
        source_text=store.read_source(source_locator),
        existing_pages=store.page_texts(),
        wiki_structure=store.structure,
        today=today,
        schema=Schema(),
        source_plan=source_plan,
        new_page_prefix=required_new_page_prefix(profiles, source_locator),
    )


def build_current_registry(
    store: WikiStore,
    source_locator: str,
    plan: PagePlan,
    pdf_result: ExtractionResult | None,
) -> EvidenceRegistry | None:
    source_text = _source_text_for_registry(store, source_locator, pdf_result)
    if source_text is None:
        return None
    return build_evidence_registry(plan, (source_text,))


def _source_text_for_registry(
    store: WikiStore, source_locator: str, pdf_result: ExtractionResult | None
) -> SourceText | None:
    if source_locator.lower().endswith(".pdf") and pdf_result is not None:
        text = read_source_text(pdf_result.cache_dir)
        return source_text_from_text(source_locator, text, "pdf-cache")
    return store.source_resolver().source_text(source_locator)
