"""Deterministic retrieval over compiled wiki artifacts.

The wiki is already a structured, maintained knowledge layer. Retrieval should
therefore search authored identifiers, summaries, headings, page metadata, and
links before falling back to body text repetition.
"""

from __future__ import annotations

from collections.abc import Mapping

from llmwiki.domain.index import parse_index
from llmwiki.domain.links import extract_links
from llmwiki.domain.retrieval_models import (
    RetrievalCandidate,
    RetrievalSignal,
    WikiContextPack,
)
from llmwiki.domain.retrieval_scoring import (
    backlinks,
    candidate_for_page,
    detect_source_scope,
    in_source_scope,
    is_task_query,
    metadata_for_page,
    render_signals,
)
from llmwiki.domain.retrieval_tokens import (
    query_terms,
    token_key_counts,
    token_keys_for_text,
    tokens_for_text,
)

__all__ = [
    "RetrievalCandidate",
    "RetrievalSignal",
    "WikiContextPack",
    "query_terms",
    "render_context_pack",
    "retrieve_wiki_context",
    "token_key_counts",
    "token_keys_for_text",
    "tokens_for_text",
]


def retrieve_wiki_context(
    *,
    query: str,
    index_text: str,
    page_texts: Mapping[str, str],
    limit: int = 8,
    related_limit: int = 4,
) -> WikiContextPack:
    terms = query_terms(query)
    if not terms:
        return WikiContextPack(query=query, candidates=())
    task_query = is_task_query(query)
    index_entries = {entry.page_id: entry for entry in parse_index(index_text)}
    links_by_page = {page_id: extract_links(text) for page_id, text in page_texts.items()}
    page_backlinks = backlinks(links_by_page)
    metadata_by_page = {
        page_id: metadata_for_page(page_id, text, index_entries.get(page_id))
        for page_id, text in page_texts.items()
    }
    source_scope = detect_source_scope(terms, metadata_by_page)
    candidates = [
        candidate
        for page_id, text in page_texts.items()
        if in_source_scope(metadata_by_page[page_id], source_scope)
        if (
            candidate := candidate_for_page(
                page_id,
                text,
                terms,
                task_query,
                metadata_by_page[page_id],
                links_by_page,
                page_backlinks,
                related_limit,
            )
        )
        is not None
    ]
    candidates.sort(key=lambda candidate: (-candidate.score, candidate.page_id))
    return WikiContextPack(
        query=query,
        candidates=tuple(candidates[:limit]),
        source_scope=source_scope,
    )


def render_context_pack(pack: WikiContextPack) -> str:
    if not pack.candidates:
        return "No wiki retrieval candidates matched. Try search_wiki with alternate terms."
    lines = [
        "Wiki retrieval context:",
        "Use these page ids as starting points. Read pages before detailed answers.",
    ]
    if pack.source_scope:
        lines.append("Source scope: " + ", ".join(pack.source_scope))
    for index, candidate in enumerate(pack.candidates, start=1):
        lines.extend(
            [
                "",
                f"{index}. [[{candidate.page_id}]] "
                f"(score {candidate.score}, kind {candidate.page_kind})",
                f"   summary: {candidate.summary}",
                f"   why: {render_signals(candidate.signals)}",
                f"   excerpt: {candidate.snippet}",
            ]
        )
        if candidate.related_page_ids:
            related = ", ".join(f"[[{page_id}]]" for page_id in candidate.related_page_ids)
            lines.append(f"   nearby: {related}")
    return "\n".join(lines)
