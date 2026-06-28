"""Evidence-led per-source topic planning.

Exact authored headings are projected as source-section pages. Topic pages are
reserved for emergent concepts, repeated terms, and heading components that add
navigation value without restating the same source section.
"""

from __future__ import annotations

import re
from collections import Counter

from llmwiki.domain.ledger.atom_context import atom_context_matches
from llmwiki.domain.ledger.atom_projection import atom_is_topic_projectable
from llmwiki.domain.ledger.concepts import concept_topic_keys
from llmwiki.domain.ledger.entries import LedgerEntry
from llmwiki.domain.ledger.ledger import ClaimLedger
from llmwiki.domain.ledger.section_planning import SectionGroundedPlan
from llmwiki.domain.ledger.structure import DocumentStructure
from llmwiki.domain.ledger.topic_atom_match import atom_ids_matching_table_payload
from llmwiki.domain.ledger.topic_candidates import (
    TopicCandidate,
    repeated_section_candidates,
    section_component_candidates,
)
from llmwiki.domain.ledger.topic_evidence import (
    entry_supports_topic,
    topic_entry_rank,
)
from llmwiki.domain.ledger.topic_models import SourceTopic
from llmwiki.domain.ledger.topic_terms import (
    content_terms,
    single_term_topic_candidate_allowed,
    topic_matcher,
)

_TOPIC_KINDS = ("claim", "event", "concept")
_MIN_TERM_FREQUENCY = 4
_MIN_MATCHES = 3
_MAX_TOPICS = 96
_HEADING_BONUS = 3.0
_CONCEPT_BONUS = 2.0
_REPEATED_SECTION_BONUS = 12.0
_MAX_STATEMENT_WORDS = 45


def plan_source_topics(
    ledger: ClaimLedger,
    structure: DocumentStructure,
    *,
    section_plan: SectionGroundedPlan | None = None,
    max_topics: int = _MAX_TOPICS,
    min_matches: int = _MIN_MATCHES,
) -> tuple[SourceTopic, ...]:
    entries = [
        entry
        for entry in ledger.usable_entries
        if entry.ledger_entry_kind in _TOPIC_KINDS and (entry.subject or entry.normalized_text)
    ]
    candidates = (
        repeated_section_candidates(section_plan)
        + section_component_candidates(section_plan)
        + _concept_candidates(entries)
        + _term_candidates(entries)
    )
    protected_topic_keys = {
        candidate.topic_key
        for candidate in candidates
        if candidate.evidence_kind == "section-repeat"
    }
    topics: dict[str, SourceTopic] = {}
    for candidate in candidates:
        if candidate.topic_key in topics:
            continue
        topic = _aggregate(candidate, entries, ledger, structure)
        if topic is None:
            continue
        minimum = 1 if candidate.from_heading or candidate.evidence_entry_ids else min_matches
        if len(topic.entry_ids) + len(topic.atom_ids) >= minimum:
            topics[candidate.topic_key] = topic
    ranked = sorted(topics.values(), key=lambda t: (-t.salience, t.topic_key))
    protected = [topic for topic in ranked if topic.topic_key in protected_topic_keys]
    regular = [topic for topic in ranked if topic.topic_key not in protected_topic_keys]
    remaining = max(0, max_topics - len(protected))
    return tuple((*protected, *regular[:remaining]))


def _concept_candidates(entries: list[LedgerEntry]) -> list[TopicCandidate]:
    keyed: dict[str, tuple[str, tuple[str, ...], list[str]]] = {}
    for entry in entries:
        if entry.ledger_entry_kind != "concept" or not entry.concept_facets:
            continue
        for facet in entry.concept_facets:
            keys = concept_topic_keys((facet,))
            if not keys:
                continue
            terms = tuple(content_terms(facet))
            if not terms:
                continue
            label, existing_terms, entry_ids = keyed.get(keys[0], (facet.title(), terms, []))
            entry_ids.append(entry.ledger_entry_id)
            keyed[keys[0]] = (label, existing_terms, entry_ids)
    return [
        TopicCandidate(
            topic_key=key,
            label=label,
            terms=terms,
            evidence_kind="concept",
            evidence_entry_ids=tuple(entry_ids),
        )
        for key, (label, terms, entry_ids) in keyed.items()
    ]


def _term_candidates(entries: list[LedgerEntry]) -> list[TopicCandidate]:
    counts: Counter[str] = Counter()
    for entry in entries:
        for token in content_terms(entry.subject):
            counts[token] += 1
    candidates: list[TopicCandidate] = []
    for term, frequency in counts.most_common():
        if frequency < _MIN_TERM_FREQUENCY:
            break
        if not single_term_topic_candidate_allowed(term):
            continue
        candidates.append(
            TopicCandidate(
                topic_key=term,
                label=term.title(),
                terms=(term,),
                evidence_kind="subject-term",
            )
        )
    return candidates


def _aggregate(
    candidate: TopicCandidate,
    entries: list[LedgerEntry],
    ledger: ClaimLedger,
    structure: DocumentStructure,
) -> SourceTopic | None:
    matcher = topic_matcher(candidate.terms)
    if matcher is None:
        return None
    if candidate.evidence_kind in ("section", "section-repeat"):
        evidence_ids = set(candidate.evidence_entry_ids)
        matched = [entry for entry in entries if entry.ledger_entry_id in evidence_ids]
        atom_ids = candidate.evidence_atom_ids
    elif candidate.evidence_kind == "section-component":
        evidence_ids = set(candidate.evidence_entry_ids)
        matched = [
            entry
            for entry in entries
            if entry.ledger_entry_id in evidence_ids and entry_supports_topic(entry, matcher)
        ]
        atom_ids = tuple(
            atom_id
            for atom_id in candidate.evidence_atom_ids
            if _atom_has_matching_context(ledger, atom_id, matcher)
        )
    elif candidate.evidence_kind == "concept":
        matched = _entries_for_concept(candidate, entries, matcher)
        atom_ids = _atom_ids_near_entries(ledger, matched, matcher)
    else:
        matched = _entries_for_subject_term(entries, matcher)
        atom_ids = _atom_ids_near_entries(ledger, matched, matcher)
    if candidate.evidence_kind not in ("section", "section-repeat", "section-component"):
        atom_ids = tuple(
            dict.fromkeys((*atom_ids, *atom_ids_matching_table_payload(ledger, matcher, structure)))
        )
    matched = [
        entry
        for entry in matched
        if len((entry.normalized_text or entry.source_text).split()) <= _MAX_STATEMENT_WORDS
    ]
    matched.sort(key=lambda entry: topic_entry_rank(entry, matcher, ledger))
    entry_ids = tuple(entry.ledger_entry_id for entry in matched)
    salience = (
        len(entry_ids)
        + 1.5 * len(atom_ids)
        + (_HEADING_BONUS if candidate.from_heading else 0.0)
        + (_CONCEPT_BONUS if candidate.evidence_entry_ids else 0.0)
        + (_REPEATED_SECTION_BONUS if candidate.evidence_kind == "section-repeat" else 0.0)
    )
    return SourceTopic(
        topic_key=candidate.topic_key,
        label=candidate.label,
        page_kind="concept",
        match_terms=candidate.terms,
        entry_ids=entry_ids,
        atom_ids=atom_ids,
        from_heading=candidate.from_heading,
        salience=salience,
    )


def _entries_for_concept(
    candidate: TopicCandidate, entries: list[LedgerEntry], matcher: re.Pattern[str]
) -> list[LedgerEntry]:
    evidence_ids = set(candidate.evidence_entry_ids)
    evidence_nodes = {
        node_id
        for entry in entries
        if entry.ledger_entry_id in evidence_ids
        for node_id in entry.structure_node_ids[:1]
    }
    matched: list[LedgerEntry] = []
    for entry in entries:
        if entry.ledger_entry_id in evidence_ids:
            matched.append(entry)
            continue
        if not evidence_nodes.intersection(entry.structure_node_ids):
            continue
        if matcher.search(entry.subject) or matcher.search(entry.object_value):
            matched.append(entry)
    return matched


def _entries_for_subject_term(
    entries: list[LedgerEntry], matcher: re.Pattern[str]
) -> list[LedgerEntry]:
    return [entry for entry in entries if matcher.search(entry.subject)]


def _atom_ids_near_entries(
    ledger: ClaimLedger, entries: list[LedgerEntry], matcher: re.Pattern[str]
) -> tuple[str, ...]:
    nodes = {node_id for entry in entries for node_id in entry.structure_node_ids[:1]}
    ids: list[str] = []
    for entry in ledger.usable_entries:
        if entry.ledger_entry_kind != "technical-atom" or not entry.technical_atom_id:
            continue
        if nodes and not nodes.intersection(entry.structure_node_ids):
            continue
        if _atom_has_matching_context(ledger, entry.technical_atom_id, matcher):
            ids.append(entry.technical_atom_id)
    return tuple(dict.fromkeys(ids))


def _atom_has_matching_context(ledger: ClaimLedger, atom_id: str, matcher: re.Pattern[str]) -> bool:
    atom = ledger.atom(atom_id)
    return (
        atom is not None
        and atom_is_topic_projectable(atom, ledger.source_profile)
        and atom_context_matches(ledger.atom_contexts(atom_id), matcher)
    )
