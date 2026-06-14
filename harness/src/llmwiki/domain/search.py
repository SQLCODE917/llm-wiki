"""Naive full-text search over wiki pages.

Index-first navigation is the design default (docs/llm-wiki.md); this gives
the model a second, content-level signal without any embedding
infrastructure. Upgrade path: qmd (see design doc alternatives).
"""

from __future__ import annotations

import re
from collections.abc import Mapping
from dataclasses import dataclass

_WORD_RE = re.compile(r"[a-z0-9]+")
_SNIPPET_CHARS = 160
_NAME_WEIGHT = 3


@dataclass(frozen=True)
class SearchHit:
    name: str
    score: int
    snippet: str


def _tokens(text: str) -> list[str]:
    return _WORD_RE.findall(text.lower())


def search_pages(pages: Mapping[str, str], query: str, limit: int = 8) -> list[SearchHit]:
    terms = set(_tokens(query))
    if not terms:
        return []
    hits: list[SearchHit] = []
    for name, text in pages.items():
        body_tokens = _tokens(text)
        name_tokens = set(_tokens(name))
        score = sum(1 for tok in body_tokens if tok in terms)
        score += _NAME_WEIGHT * len(terms & name_tokens)
        if score == 0:
            continue
        hits.append(SearchHit(name=name, score=score, snippet=_snippet(text, terms)))
    hits.sort(key=lambda h: (-h.score, h.name))
    return hits[:limit]


def _snippet(text: str, terms: set[str]) -> str:
    lower = text.lower()
    first = min(
        (pos for pos in (lower.find(t) for t in terms) if pos >= 0),
        default=0,
    )
    start = max(0, first - _SNIPPET_CHARS // 4)
    raw = text[start : start + _SNIPPET_CHARS]
    return " ".join(raw.split())


def render_hits(hits: list[SearchHit]) -> str:
    if not hits:
        return "No pages matched. Try different terms, or check the index with read_page."
    lines = [f"[[{h.name}]] (score {h.score}): {h.snippet}" for h in hits]
    return "\n".join(lines)
