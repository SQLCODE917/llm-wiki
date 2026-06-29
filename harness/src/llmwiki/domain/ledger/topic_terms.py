"""Reusable lexical helpers for topic planning."""

from __future__ import annotations

import re
from typing import Literal

from llmwiki.domain.ledger.stopwords import COMMON_WORDS

TOKEN = re.compile(r"[A-Za-z][A-Za-z0-9]{2,}")
LABEL_TOKEN = re.compile(r"[A-Za-z0-9][A-Za-z0-9]{1,}")
TopicTermRole = Literal["domain", "discourse-container", "structural-container", "ambiguous"]
GENERIC_TOPIC_TERMS = frozenset(
    {
        "herself",
        "himself",
        "itself",
        "myself",
        "ourselves",
        "themselves",
        "yourself",
        "yourselves",
    }
)
_DISCOURSE_CONTAINER_TERMS = frozenset(
    {
        "case",
        "conclusion",
        "discussion",
        "introduction",
        "overview",
        "preface",
        "summary",
    }
)
_STRUCTURAL_CONTAINER_TERMS = frozenset(
    {
        "appendix",
        "book",
        "chapter",
        "part",
        "section",
    }
)
_AMBIGUOUS_TOPIC_TERMS = frozenset(
    {
        "character",
        "code",
        "function",
        "target",
        "type",
        "value",
    }
)
_MAX_MATCH_TERMS = 24
_MAX_MATCH_TERM_LENGTH = 80


def content_terms(text: str) -> list[str]:
    terms = []
    for token in TOKEN.findall(text):
        lowered = singular(token.lower())
        if len(lowered) >= 4 and lowered not in COMMON_WORDS and lowered not in GENERIC_TOPIC_TERMS:
            terms.append(lowered)
    return list(dict.fromkeys(terms))


def source_label_terms(text: str) -> list[str]:
    """Page-identity terms from authored labels, preserving identifiers."""
    terms = []
    for token in LABEL_TOKEN.findall(text):
        lowered = token.lower()
        if lowered in COMMON_WORDS or lowered in GENERIC_TOPIC_TERMS:
            continue
        if lowered.isalpha() and len(lowered) < 3:
            continue
        terms.append(singular(lowered) if lowered.isalpha() else lowered)
    return list(dict.fromkeys(terms))


def topic_matcher(terms: tuple[str, ...]) -> re.Pattern[str] | None:
    parts = [re.escape(term) for term in _bounded_match_terms(terms)]
    if not parts:
        return None
    return re.compile(r"\b(?:" + "|".join(parts) + r")", re.IGNORECASE)


def topic_field_matches(
    text: str,
    matcher: re.Pattern[str],
    terms: tuple[str, ...] = (),
) -> bool:
    if not text.strip():
        return False
    required_terms = required_topic_terms(terms)
    if required_terms:
        matched_terms = matching_topic_terms(text, required_terms)
        if len(required_terms) <= 1:
            return bool(matched_terms)
        return len(matched_terms) >= required_topic_hit_count(required_terms)
    return matcher.search(text) is not None


def required_topic_terms(terms: tuple[str, ...]) -> tuple[str, ...]:
    return _bounded_match_terms(
        tuple(
            term
            for term in terms
            if term and topic_term_role(term) not in ("discourse-container", "structural-container")
        )
    )


def matching_topic_terms(text: str, terms: tuple[str, ...]) -> tuple[str, ...]:
    tokens = _match_tokens(text)
    return tuple(
        term
        for term in _bounded_match_terms(terms)
        if any(token.startswith(term) for token in tokens)
    )


def required_topic_hit_count(terms: tuple[str, ...]) -> int:
    if len(terms) <= 1:
        return len(terms)
    return max(2, (len(terms) * 3 + 4) // 5)


def topic_term_role(term: str) -> TopicTermRole:
    lowered = singular(term.lower())
    if lowered in _DISCOURSE_CONTAINER_TERMS:
        return "discourse-container"
    if lowered in _STRUCTURAL_CONTAINER_TERMS:
        return "structural-container"
    if lowered in _AMBIGUOUS_TOPIC_TERMS:
        return "ambiguous"
    return "domain"


def single_term_topic_candidate_allowed(term: str) -> bool:
    return topic_term_role(term) not in ("discourse-container", "structural-container")


def singular(token: str) -> str:
    if token in {"series", "species"}:
        return token
    if token.endswith("us"):
        return token
    if token.endswith("sses") and len(token) > 5:
        return token[:-2]
    if token.endswith(("ches", "shes", "xes", "zes")) and len(token) > 5:
        return token[:-2]
    if token.endswith("ies") and len(token) > 4:
        return token[:-3] + "y"
    if token.endswith("ss"):
        return token
    return token[:-1] if token.endswith("s") and len(token) > 4 else token


def _bounded_match_terms(terms: tuple[str, ...]) -> tuple[str, ...]:
    cleaned = (
        term.strip().lower()
        for term in terms
        if term and len(term.strip()) <= _MAX_MATCH_TERM_LENGTH
    )
    return tuple(dict.fromkeys(cleaned))[:_MAX_MATCH_TERMS]


def _match_tokens(text: str) -> tuple[str, ...]:
    tokens = []
    for token in LABEL_TOKEN.findall(text):
        lowered = token.lower()
        tokens.append(singular(lowered) if lowered.isalpha() else lowered)
    return tuple(dict.fromkeys(tokens))
