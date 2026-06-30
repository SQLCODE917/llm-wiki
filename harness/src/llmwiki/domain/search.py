"""Naive full-text search over wiki pages.

Index-first navigation is the design default (docs/llm-wiki.md); this gives
the model a second, content-level signal without any embedding
infrastructure. Upgrade path: qmd (see design doc alternatives).
"""

from __future__ import annotations

import re
from collections import Counter
from collections.abc import Mapping
from dataclasses import dataclass

_WORD_RE = re.compile(r"[a-z0-9]+")
_SNIPPET_CHARS = 160
_NAME_WEIGHT = 20
_ALL_TERMS_WEIGHT = 20
_BODY_PHRASE_WEIGHT = 200
_NAME_PHRASE_WEIGHT = 400
_TERM_COUNT_CAP = 5


@dataclass(frozen=True)
class SearchHit:
    name: str
    score: int
    snippet: str


def _tokens(text: str) -> list[str]:
    return _WORD_RE.findall(text.lower())


def search_pages(pages: Mapping[str, str], query: str, limit: int = 8) -> list[SearchHit]:
    query_tokens = _tokens(query)
    terms = set(query_tokens)
    if not terms:
        return []
    phrase = " ".join(query_tokens) if len(query_tokens) > 1 else ""
    hits: list[SearchHit] = []
    for name, text in pages.items():
        body_tokens = _tokens(text)
        body_counts = Counter(body_tokens)
        body_terms = set(body_tokens)
        name_tokens = set(_tokens(name))
        normalized_body = " ".join(body_tokens)
        normalized_name = " ".join(_tokens(name))
        score = sum(min(body_counts[tok], _TERM_COUNT_CAP) for tok in terms)
        score += _NAME_WEIGHT * len(terms & name_tokens)
        if terms <= body_terms:
            score += _ALL_TERMS_WEIGHT
        if phrase and phrase in normalized_body:
            score += _BODY_PHRASE_WEIGHT
        if phrase and phrase in normalized_name:
            score += _NAME_PHRASE_WEIGHT
        if score == 0:
            continue
        hits.append(SearchHit(name=name, score=score, snippet=_snippet(text, terms, phrase)))
    hits.sort(key=lambda h: (-h.score, h.name))
    return hits[:limit]


def _snippet(text: str, terms: set[str], phrase: str = "") -> str:
    lower = text.lower()
    phrase_pos = lower.find(phrase) if phrase else -1
    first = min(
        (pos for pos in (lower.find(t) for t in terms) if pos >= 0),
        default=0,
    )
    if phrase_pos >= 0:
        first = phrase_pos
    start = max(0, first - _SNIPPET_CHARS // 4)
    raw = text[start : start + _SNIPPET_CHARS]
    return " ".join(raw.split())


def render_hits(hits: list[SearchHit]) -> str:
    if not hits:
        return "No pages matched. Try different terms, or check the index with read_index."
    lines = [f"[[{h.name}]] (score {h.score}): {h.snippet}" for h in hits]
    return "\n".join(lines)
