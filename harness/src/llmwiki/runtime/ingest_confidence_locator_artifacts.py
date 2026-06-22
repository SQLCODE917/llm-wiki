"""Locator-index artifact helpers for ingest confidence."""

from __future__ import annotations

from llmwiki.domain.citations import Citation, inspect_citations
from llmwiki.domain.evidence_locator_builder import build_evidence_locator_index
from llmwiki.domain.evidence_locator_index import EvidenceLocatorIndex
from llmwiki.domain.evidence_registry import EvidenceRegistry
from llmwiki.runtime.ingest_confidence_page_scope import page_body
from llmwiki.store import WikiStore


def build_current_locator_index(
    store: WikiStore, source_locator: str, registry: EvidenceRegistry | None
) -> EvidenceLocatorIndex | None:
    if registry is None:
        return None
    citations: list[Citation] = []
    inventory = store.source_inventory()
    for page_id, text in store.page_texts().items():
        report = inspect_citations(page_id, page_body(text), inventory)
        citations.extend(
            citation
            for citation in report.citations
            if citation.source_path == f"raw/{source_locator}"
        )
    return build_evidence_locator_index(registry, tuple(citations))


def read_locator_index(store: WikiStore, source_locator: str) -> EvidenceLocatorIndex | None:
    try:
        return store.read_evidence_locator_index_artifact(source_locator)
    except Exception:
        return None
