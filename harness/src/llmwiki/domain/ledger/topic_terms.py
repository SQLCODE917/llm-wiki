"""Reusable lexical helpers for topic planning."""

from __future__ import annotations

import re
from collections.abc import Iterable
from functools import cache
from typing import Literal

from llmwiki.domain.ledger.stopwords import COMMON_WORDS

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
_MAX_TOPIC_FIELD_CHARS = 12_000


def content_terms(text: str) -> list[str]:
    terms = []
    for token in _ascii_tokens(text, min_length=3, require_alpha_start=True):
        lowered = singular(token)
        if len(lowered) >= 4 and lowered not in COMMON_WORDS and lowered not in GENERIC_TOPIC_TERMS:
            terms.append(lowered)
    return list(dict.fromkeys(terms))


def source_label_terms(text: str) -> list[str]:
    """Page-identity terms from authored labels, preserving identifiers."""
    terms = []
    for lowered in _ascii_tokens(text, min_length=2, require_alpha_start=False):
        if not _has_ascii_alpha(lowered):
            continue
        if lowered in COMMON_WORDS or lowered in GENERIC_TOPIC_TERMS:
            continue
        if _is_ascii_alpha(lowered) and len(lowered) < 3:
            continue
        terms.append(singular(lowered) if _is_ascii_alpha(lowered) else lowered)
    return list(dict.fromkeys(terms))


def topic_matcher(terms: tuple[str, ...]) -> re.Pattern[str] | None:
    parts = [re.escape(term) for term in _bounded_match_terms(terms)]
    if not parts:
        return None
    return re.compile(r"\b(?:" + "|".join(parts) + r")\b", re.IGNORECASE)


def topic_field_matches(
    text: str,
    matcher: re.Pattern[str],
    terms: tuple[str, ...] = (),
    required_terms: tuple[str, ...] | None = None,
) -> bool:
    text = _bounded_topic_text(text)
    if not text.strip():
        return False
    if required_terms is None:
        required_terms = required_topic_terms(terms)
    if required_terms:
        return topic_tokens_match(topic_field_tokens(text), required_terms)
    return matcher.search(text) is not None


def topic_field_tokens(text: object) -> frozenset[str]:
    return frozenset(_match_tokens(text))


def topic_tokens_match(tokens: frozenset[str], required_terms: tuple[str, ...]) -> bool:
    matched = 0
    for term in required_terms:
        if term in tokens:
            matched += 1
    if len(required_terms) <= 1:
        return matched > 0
    return matched >= required_topic_hit_count(required_terms)


@cache
def required_topic_terms(terms: tuple[str, ...]) -> tuple[str, ...]:
    kept: list[str] = []
    for term in _iter_raw_terms(terms):
        if not isinstance(term, str) or not term:
            continue
        if not any(char.isalpha() for char in term):
            continue
        if topic_term_role(term) in ("discourse-container", "structural-container"):
            continue
        kept.append(term)
    return _bounded_match_terms(tuple(kept))


def matching_topic_terms(text: str, terms: tuple[str, ...]) -> tuple[str, ...]:
    tokens = set(_match_tokens(text))
    return tuple(
        term
        for term in _bounded_match_terms(terms)
        if term in tokens
    )


def required_topic_hit_count(terms: tuple[str, ...]) -> int:
    if len(terms) <= 1:
        return len(terms)
    return max(2, (len(terms) * 3 + 4) // 5)


@cache
def topic_term_role(term: str) -> TopicTermRole:
    lowered = singular(_ascii_term(term))
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
    if _suffix(token, 2) == "us":
        return token
    if _suffix(token, 4) == "sses" and len(token) > 5:
        return token[:-2]
    if _suffix(token, 4) in {"ches", "shes"} and len(token) > 5:
        return token[:-2]
    if _suffix(token, 3) in {"xes", "zes"} and len(token) > 5:
        return token[:-2]
    if _suffix(token, 3) == "ies" and len(token) > 4:
        return token[:-3] + "y"
    if _suffix(token, 2) == "ss":
        return token
    return token[:-1] if _suffix(token, 1) == "s" and len(token) > 4 else token


def _suffix(token: str, length: int) -> str:
    return token[-length:] if len(token) >= length else ""


def _bounded_match_terms(terms: object) -> tuple[str, ...]:
    bounded: list[str] = []
    seen: set[str] = set()
    for raw_term in _iter_raw_terms(terms):
        if not isinstance(raw_term, str):
            continue
        term = _ascii_term(raw_term.strip())
        if not term or len(term) > _MAX_MATCH_TERM_LENGTH or term in seen:
            continue
        bounded.append(term)
        seen.add(term)
        if len(bounded) >= _MAX_MATCH_TERMS:
            break
    return tuple(bounded)


def _iter_raw_terms(terms: object) -> Iterable[object]:
    if isinstance(terms, str):
        return (terms,)
    if isinstance(terms, Iterable):
        return terms
    return ()


def _bounded_topic_text(text: object) -> str:
    return (text if isinstance(text, str) else str(text))[:_MAX_TOPIC_FIELD_CHARS]


def _match_tokens(text: object) -> tuple[str, ...]:
    tokens = []
    for lowered in _ascii_tokens(text, min_length=2, require_alpha_start=False):
        tokens.append(singular(lowered))
    return tuple(dict.fromkeys(tokens))


def _ascii_tokens(
    text: object, *, min_length: int, require_alpha_start: bool
) -> tuple[str, ...]:
    tokens: list[str] = []
    current: list[str] = []
    for char in _bounded_topic_text(text):
        if len(char) != 1:
            continue
        normalized = _ascii_word_char(char)
        if normalized:
            current.append(normalized)
        elif current:
            _append_ascii_token(tokens, current, min_length, require_alpha_start)
            current = []
    if current:
        _append_ascii_token(tokens, current, min_length, require_alpha_start)
    return tuple(tokens)


def _append_ascii_token(
    tokens: list[str], chars: list[str], min_length: int, require_alpha_start: bool
) -> None:
    token = "".join(chars)
    if len(token) < min_length:
        return
    if require_alpha_start and not _is_ascii_alpha_char(token[0]):
        return
    tokens.append(token)


def _ascii_term(text: object) -> str:
    chars: list[str] = []
    raw = text if isinstance(text, str) else str(text)
    for char in raw[:_MAX_MATCH_TERM_LENGTH]:
        if len(char) != 1:
            continue
        normalized = _ascii_word_char(char)
        if normalized:
            chars.append(normalized)
    return "".join(chars)


def _ascii_word_char(char: str) -> str:
    if len(char) != 1:
        return ""
    codepoint = ord(char)
    if 48 <= codepoint <= 57 or 97 <= codepoint <= 122:
        return char
    if 65 <= codepoint <= 90:
        return chr(codepoint + 32)
    return ""


def _has_ascii_alpha(text: str) -> bool:
    return any(_is_ascii_alpha_char(char) for char in text)


def _is_ascii_alpha(text: str) -> bool:
    if not text:
        return False
    return all(_is_ascii_alpha_char(char) for char in text)


def _is_ascii_alpha_char(char: str) -> bool:
    if len(char) != 1:
        return False
    codepoint = ord(char)
    return 97 <= codepoint <= 122
