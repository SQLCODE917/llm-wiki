"""Page scoring helpers for deterministic wiki retrieval."""

from __future__ import annotations

import re
from collections import Counter
from collections.abc import Mapping

from llmwiki.domain.index import IndexEntry
from llmwiki.domain.pages import PageError, PageMetadata, parse_page
from llmwiki.domain.retrieval_models import RetrievalCandidate, RetrievalSignal
from llmwiki.domain.retrieval_tokens import (
    token_key_counts,
    token_keys,
    token_keys_for_text,
)

_SNIPPET_CHARS = 220
_TASK_QUERY_RE = re.compile(
    r"\b(how\s+do\s+i|how\s+to|steps?|procedure|workflow|create|make|build|set\s+up)\b",
    re.IGNORECASE,
)
_PROCEDURE_PAGE_BOOST = 250


def candidate_for_page(
    page_id: str,
    text: str,
    terms: set[str],
    task_query: bool,
    metadata: PageMetadata,
    links_by_page: Mapping[str, set[str]],
    backlinks: Mapping[str, set[str]],
    related_limit: int,
) -> RetrievalCandidate | None:
    body_counts = token_key_counts(text)
    signals = tuple(
        signal
        for signal in (
            _field_signal("page-id", 40, terms, page_id),
            _field_signal("summary", 18, terms, metadata.summary),
            _field_signal("heading", 20, terms, _headings_text(text)),
            _field_signal("metadata", 14, terms, _metadata_text(metadata)),
            _body_signal(terms, body_counts),
            _procedure_signal(task_query, metadata),
        )
        if signal is not None
    )
    score = sum(signal.score for signal in signals)
    if score == 0:
        return None
    return RetrievalCandidate(
        page_id=page_id,
        page_kind=metadata.page_kind,
        summary=metadata.summary,
        score=score,
        snippet=_snippet(text, terms),
        signals=signals,
        related_page_ids=related_pages(page_id, links_by_page, backlinks, related_limit),
    )


def metadata_for_page(page_id: str, text: str, index_entry: IndexEntry | None) -> PageMetadata:
    try:
        return parse_page(text).page_metadata
    except PageError:
        if index_entry is not None:
            return index_entry.page_metadata
        return PageMetadata(page_id=page_id, page_kind="concept", summary="Invalid page metadata.")


def detect_source_scope(
    terms: set[str], metadata_by_page: Mapping[str, PageMetadata]
) -> tuple[str, ...]:
    source_scores: Counter[str] = Counter()
    for metadata in metadata_by_page.values():
        if not metadata.sources:
            continue
        identity_keys = token_keys_for_text(_source_identity_text(metadata))
        matched_terms = {
            term for term in terms if len(term) >= 3 and token_keys_for_text(term) & identity_keys
        }
        if len(matched_terms) < 2:
            continue
        for source in metadata.sources:
            source_scores[source] += len(matched_terms)
    if not source_scores:
        return ()
    best_score = max(source_scores.values())
    return tuple(
        source for source, score in sorted(source_scores.items()) if score == best_score
    )


def in_source_scope(metadata: PageMetadata, source_scope: tuple[str, ...]) -> bool:
    return not source_scope or bool(set(metadata.sources) & set(source_scope))


def related_pages(
    page_id: str,
    links_by_page: Mapping[str, set[str]],
    backlinks: Mapping[str, set[str]],
    limit: int,
) -> tuple[str, ...]:
    related = sorted(
        (links_by_page.get(page_id, set()) | backlinks.get(page_id, set())) - {page_id}
    )
    return tuple(related[:limit])


def backlinks(links_by_page: Mapping[str, set[str]]) -> dict[str, set[str]]:
    result: dict[str, set[str]] = {}
    for source, targets in links_by_page.items():
        for target in targets:
            result.setdefault(target, set()).add(source)
    return result


def is_task_query(query: str) -> bool:
    return _TASK_QUERY_RE.search(query) is not None


def render_signals(signals: tuple[RetrievalSignal, ...]) -> str:
    ordered = sorted(signals, key=lambda signal: (-signal.score, signal.name))
    return "; ".join(f"{signal.name} matched {signal.detail}" for signal in ordered[:4])


def _field_signal(
    name: str, weight: int, terms: set[str], text: str
) -> RetrievalSignal | None:
    text_keys = token_keys_for_text(text)
    matches = {term for term in terms if token_keys(term) & text_keys}
    if not matches:
        return None
    score = weight * len(matches)
    return RetrievalSignal(name=name, score=score, detail=", ".join(sorted(matches)))


def _body_signal(terms: set[str], body_counts: Counter[str]) -> RetrievalSignal | None:
    matches = {term for term in terms if any(body_counts[key] > 0 for key in token_keys(term))}
    if not matches:
        return None
    capped_frequency = sum(
        min(sum(body_counts[key] for key in token_keys(term)), 4) for term in matches
    )
    score = (6 * len(matches)) + capped_frequency
    return RetrievalSignal("body", score=score, detail=", ".join(sorted(matches)))


def _procedure_signal(task_query: bool, metadata: PageMetadata) -> RetrievalSignal | None:
    if task_query and metadata.page_kind == "procedure":
        return RetrievalSignal(
            "procedure-kind",
            score=_PROCEDURE_PAGE_BOOST,
            detail="task query prefers procedure pages",
        )
    return None


def _metadata_text(metadata: PageMetadata) -> str:
    return " ".join(
        (
            metadata.domain,
            metadata.category_path,
            metadata.source_id,
            metadata.page_family,
            " ".join(metadata.sources),
            " ".join(metadata.tags),
            " ".join(metadata.aliases),
        )
    )


def _source_identity_text(metadata: PageMetadata) -> str:
    return " ".join(
        (
            metadata.domain,
            metadata.category_path,
            metadata.source_id,
            " ".join(metadata.sources),
        )
    )


def _headings_text(text: str) -> str:
    return " ".join(line.lstrip("#").strip() for line in text.splitlines() if line.startswith("#"))


def _snippet(text: str, terms: set[str]) -> str:
    body = _page_body_text(text)
    lower = body.lower()
    first = min((pos for pos in (lower.find(term) for term in terms) if pos >= 0), default=0)
    start = max(0, first - _SNIPPET_CHARS // 4)
    return " ".join(body[start : start + _SNIPPET_CHARS].split())


def _page_body_text(text: str) -> str:
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) == 3:
            return parts[2]
    return text
