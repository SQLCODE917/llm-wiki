"""Token normalization for deterministic wiki retrieval."""

from __future__ import annotations

import re
from collections import Counter

_WORD_RE = re.compile(r"[a-z0-9]+")
_QUERY_STOPWORDS = frozenset(
    {
        "a",
        "about",
        "an",
        "and",
        "are",
        "as",
        "at",
        "be",
        "by",
        "can",
        "did",
        "do",
        "does",
        "for",
        "from",
        "how",
        "in",
        "is",
        "it",
        "new",
        "of",
        "on",
        "or",
        "that",
        "the",
        "this",
        "to",
        "was",
        "were",
        "what",
        "when",
        "where",
        "which",
        "who",
        "why",
        "with",
    }
)


def query_terms(query: str) -> set[str]:
    tokens = tokens_for_text(query)
    content_terms = [token for token in tokens if token not in _QUERY_STOPWORDS]
    return set(content_terms or tokens)


def tokens_for_text(text: str) -> list[str]:
    return _WORD_RE.findall(text.lower())


def token_keys_for_text(text: str) -> set[str]:
    keys: set[str] = set()
    for token in tokens_for_text(text):
        keys.update(token_keys(token))
    return keys


def token_key_counts(text: str) -> Counter[str]:
    counts: Counter[str] = Counter()
    for token in tokens_for_text(text):
        counts.update(token_keys(token))
    return counts


def token_keys(token: str) -> set[str]:
    keys = {token}
    if len(token) <= 4:
        return keys
    for suffix in ("ing", "ed", "es", "s", "e"):
        if token.endswith(suffix) and len(token) > len(suffix) + 3:
            keys.add(token[: -len(suffix)])
    if token.endswith("ion") and len(token) > 6:
        keys.add(token[:-3])
    return keys
