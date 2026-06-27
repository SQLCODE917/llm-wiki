"""Source-local evidence rules for topic planning.

The rules here classify reusable evidence patterns: definitions, subject/object
use, and technical atoms whose source context names the candidate. They never
key off a particular source passage.
"""

from __future__ import annotations

import re
from dataclasses import dataclass

from llmwiki.domain.ledger.entries import LedgerEntry
from llmwiki.domain.ledger.ledger import ClaimLedger
from llmwiki.domain.ledger.topic_terms import topic_term_role


@dataclass(frozen=True)
class TopicEvidenceDecision:
    accepted: bool
    reason: str
    evidence_entry_ids: tuple[str, ...] = ()
    evidence_atom_ids: tuple[str, ...] = ()


def heading_topic_decision(
    terms: tuple[str, ...],
    entries: list[LedgerEntry],
    atom_ids: tuple[str, ...],
    matcher: re.Pattern[str],
) -> TopicEvidenceDecision:
    evidence = tuple(entry for entry in entries if entry_supports_topic(entry, matcher))
    strong = tuple(entry for entry in evidence if entry_strongly_supports_topic(entry, matcher))
    concept = tuple(entry for entry in evidence if _is_concept_or_definition(entry))
    if not evidence and not atom_ids:
        return TopicEvidenceDecision(False, "no-source-local-topic-evidence")
    if _all_container_terms(terms) and not (concept or len(strong) >= 2 or atom_ids):
        return TopicEvidenceDecision(False, "container-heading-has-weak-topic-evidence")
    return TopicEvidenceDecision(
        True,
        "source-local-topic-evidence",
        tuple(entry.ledger_entry_id for entry in evidence),
        atom_ids,
    )


def entry_supports_topic(entry: LedgerEntry, matcher: re.Pattern[str]) -> bool:
    return (
        entry_strongly_supports_topic(entry, matcher)
        or matcher.search(entry.normalized_text or entry.source_text) is not None
    )


def entry_strongly_supports_topic(entry: LedgerEntry, matcher: re.Pattern[str]) -> bool:
    return (
        _is_concept_or_definition(entry)
        and any(matcher.search(facet) for facet in entry.concept_facets)
    ) or bool(matcher.search(entry.subject) or matcher.search(entry.object_value))


def topic_entry_rank(
    entry: LedgerEntry,
    matcher: re.Pattern[str],
    ledger: ClaimLedger,
) -> tuple[int, int, int, int, int, int, int, int, str]:
    is_concept = entry.ledger_entry_kind == "concept"
    is_definition = _is_concept_or_definition(entry)
    subject_match = bool(matcher.search(entry.subject))
    object_match = bool(matcher.search(entry.object_value))
    facet_match = any(matcher.search(facet) for facet in entry.concept_facets)
    text_match = bool(matcher.search(entry.normalized_text or entry.source_text))
    strong_match = subject_match or object_match or facet_match
    return (
        0 if strong_match else 1,
        0 if is_concept else 1,
        0 if is_definition else 1,
        0 if subject_match else 1,
        0 if object_match else 1,
        0 if facet_match else 1,
        0 if text_match else 1,
        _source_order(ledger, entry),
        entry.ledger_entry_id,
    )


def _is_concept_or_definition(entry: LedgerEntry) -> bool:
    return bool(entry.concept_facets) or "definition" in entry.claim_role_tags


def _all_container_terms(terms: tuple[str, ...]) -> bool:
    return all(
        topic_term_role(term) in ("discourse-container", "structural-container") for term in terms
    )


def _source_order(ledger: ClaimLedger, entry: LedgerEntry) -> int:
    for index, statement in enumerate(ledger.source_statements):
        if statement.source_range_id == entry.source_range_id:
            return index
    return len(ledger.source_statements)
