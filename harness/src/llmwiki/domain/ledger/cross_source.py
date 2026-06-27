"""Cross-source projection: shared topics across two or more source ledgers.

A ``CrossSourceTopic`` groups usable claim/concept entries that several sources
address under a shared, source-neutral subject term. Each contributing source
gets one ``SourceBackedPosition`` (its own claim, its own citation — positions
are never merged), and the planner derives ``CrossSourceRelationship`` records
(``agrees-with`` / ``conflicts-with`` / ``qualifies`` / ``supersedes``) between
positions from different sources. This is the basis of concept and entity pages.
"""

from __future__ import annotations

import re
from dataclasses import dataclass

from llmwiki.domain.ledger.canonical import deterministic_id
from llmwiki.domain.ledger.topic_terms import content_terms

_SUCCESSION = re.compile(
    r"\b(supersed\w+|replac\w+|deprecat\w+|revised|newer edition|obsolet\w+)\b", re.IGNORECASE
)


@dataclass(frozen=True)
class SourcePosition:
    """A candidate cross-source position derived from one source ledger entry."""

    source_locator: str
    source_hash: str
    projection_source_support_id: str
    ledger_entry_id: str
    ledger_entry_kind: str
    subject: str
    predicate: str
    polarity: str
    claim_force: str
    condition_scope: str
    has_scope: bool
    normalized_text: str
    concept_facets: tuple[str, ...]
    topic_keys: tuple[str, ...]
    evidence_ids: tuple[str, ...]
    citation_label: str


@dataclass(frozen=True)
class SourceBackedPosition:
    source_backed_position_id: str
    source_locator: str
    projection_source_support_id: str
    ledger_entry_id: str
    text: str
    citation_label: str


@dataclass(frozen=True)
class CrossSourceRelationship:
    cross_source_relationship_id: str
    cross_source_relationship_kind: str
    related_position_ids: tuple[str, ...]
    related_entry_ids: tuple[str, ...]


@dataclass(frozen=True)
class CrossSourceTopic:
    topic_key: str
    label: str
    page_kind: str
    positions: tuple[SourceBackedPosition, ...]
    relationships: tuple[CrossSourceRelationship, ...]
    support_ids: tuple[str, ...]


def plan_cross_source_topics(
    positions: tuple[SourcePosition, ...],
    *,
    min_sources: int = 2,
    max_topics: int = 40,
) -> tuple[CrossSourceTopic, ...]:
    by_key: dict[str, list[SourcePosition]] = {}
    for position in positions:
        for key in position.topic_keys:
            by_key.setdefault(key, []).append(position)
    topics: list[CrossSourceTopic] = []
    for key, members in by_key.items():
        source_count = len({p.source_locator for p in members})
        if source_count < min_sources:
            continue
        topics.append(_build_topic(key, _representatives(members), "concept"))
    topics.sort(key=lambda t: (-len(t.positions), t.topic_key))
    return tuple(topics[:max_topics])


def classify_relationship(a: SourcePosition, b: SourcePosition) -> str | None:
    if _SUCCESSION.search(a.normalized_text) or _SUCCESSION.search(b.normalized_text):
        return "supersedes"
    if not _shared_predicate(a, b):
        return None
    if not _shared_statement_terms(a, b):
        return None
    if a.polarity != b.polarity:
        return "conflicts-with"
    if a.has_scope != b.has_scope or a.condition_scope != b.condition_scope:
        return "qualifies"
    return "agrees-with"


def _build_topic(key: str, members: list[SourcePosition], page_kind: str) -> CrossSourceTopic:
    positions = tuple(
        SourceBackedPosition(
            source_backed_position_id=deterministic_id(
                "source-backed-position", key, member.source_locator, member.ledger_entry_id
            ),
            source_locator=member.source_locator,
            projection_source_support_id=member.projection_source_support_id,
            ledger_entry_id=member.ledger_entry_id,
            text=member.normalized_text,
            citation_label=member.citation_label,
        )
        for member in members
    )
    position_id = {
        member.ledger_entry_id: positions[i].source_backed_position_id
        for i, member in enumerate(members)
    }
    relationships: list[CrossSourceRelationship] = []
    for i in range(len(members)):
        for j in range(i + 1, len(members)):
            a, b = members[i], members[j]
            if a.source_locator == b.source_locator:
                continue
            kind = classify_relationship(a, b)
            if kind is None:
                continue
            related = tuple(
                sorted((position_id[a.ledger_entry_id], position_id[b.ledger_entry_id]))
            )
            relationships.append(
                CrossSourceRelationship(
                    cross_source_relationship_id=deterministic_id(
                        "cross-source-relationship", key, kind, *related
                    ),
                    cross_source_relationship_kind=kind,
                    related_position_ids=related,
                    related_entry_ids=(a.ledger_entry_id, b.ledger_entry_id),
                )
            )
    support_ids = tuple(sorted({member.projection_source_support_id for member in members}))
    return CrossSourceTopic(
        topic_key=key,
        label=key.replace("-", " ").title(),
        page_kind=page_kind,
        positions=positions,
        relationships=tuple(relationships),
        support_ids=support_ids,
    )


def _representatives(members: list[SourcePosition]) -> list[SourcePosition]:
    by_source: dict[str, SourcePosition] = {}
    for member in members:
        current = by_source.get(member.source_locator)
        if current is None or _rank(member) > _rank(current):
            by_source[member.source_locator] = member
    return list(by_source.values())


def _rank(position: SourcePosition) -> tuple[int, int]:
    return (1 if position.ledger_entry_kind == "concept" else 0, len(position.normalized_text))


def _shared_predicate(a: SourcePosition, b: SourcePosition) -> bool:
    return bool(a.predicate) and a.predicate.lower() == b.predicate.lower()


def _shared_statement_terms(a: SourcePosition, b: SourcePosition) -> bool:
    a_terms = set(content_terms(a.normalized_text))
    b_terms = set(content_terms(b.normalized_text))
    return len(a_terms.intersection(b_terms)) >= 2
