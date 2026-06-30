"""Precomputed lexical evidence for topic matching."""

from __future__ import annotations

import re
from dataclasses import dataclass

from llmwiki.domain.ledger.entries import LedgerEntry
from llmwiki.domain.ledger.topic_terms import (
    topic_field_matches,
    topic_field_tokens,
    topic_tokens_match,
)


@dataclass(frozen=True)
class TopicEntryIndex:
    entry: LedgerEntry
    subject_tokens: frozenset[str]
    object_tokens: frozenset[str]
    text_tokens: frozenset[str]
    facet_tokens: tuple[frozenset[str], ...]


def topic_entry_index(entry: LedgerEntry) -> TopicEntryIndex:
    return TopicEntryIndex(
        entry=entry,
        subject_tokens=topic_field_tokens(entry.subject),
        object_tokens=topic_field_tokens(entry.object_value),
        text_tokens=topic_field_tokens(entry.normalized_text or entry.source_text),
        facet_tokens=tuple(topic_field_tokens(facet) for facet in entry.concept_facets),
    )


def topic_entry_index_supports_topic(
    index: TopicEntryIndex,
    matcher: re.Pattern[str],
    terms: tuple[str, ...],
    required_terms: tuple[str, ...],
) -> bool:
    return topic_entry_index_strongly_supports_topic(
        index, matcher, terms, required_terms
    ) or topic_field_index_matches(
        index.text_tokens,
        index.entry.normalized_text or index.entry.source_text,
        matcher,
        terms,
        required_terms,
    )


def topic_entry_index_strongly_supports_topic(
    index: TopicEntryIndex,
    matcher: re.Pattern[str],
    terms: tuple[str, ...],
    required_terms: tuple[str, ...],
) -> bool:
    return (
        entry_is_concept_or_definition(index.entry)
        and any(
            topic_field_index_matches(tokens, facet, matcher, terms, required_terms)
            for tokens, facet in zip(index.facet_tokens, index.entry.concept_facets, strict=True)
        )
    ) or bool(
        topic_field_index_matches(
            index.subject_tokens, index.entry.subject, matcher, terms, required_terms
        )
        or topic_field_index_matches(
            index.object_tokens, index.entry.object_value, matcher, terms, required_terms
        )
    )


def topic_field_index_matches(
    tokens: frozenset[str],
    text: str,
    matcher: re.Pattern[str],
    terms: tuple[str, ...],
    required_terms: tuple[str, ...],
) -> bool:
    if required_terms:
        return topic_tokens_match(tokens, required_terms)
    return topic_field_matches(text, matcher, terms, required_terms)


def entry_is_concept_or_definition(entry: LedgerEntry) -> bool:
    return bool(entry.concept_facets) or "definition" in entry.claim_role_tags
