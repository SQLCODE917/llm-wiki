"""Topic-index domain records."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class SourceTopic:
    topic_key: str
    label: str
    page_kind: str
    match_terms: tuple[str, ...]
    entry_ids: tuple[str, ...]
    atom_ids: tuple[str, ...]
    from_heading: bool
    salience: float


@dataclass(frozen=True)
class TopicRepresentative:
    """One source's representative statement for cross-source classification."""

    ledger_entry_id: str
    subject: str
    predicate: str
    polarity: str
    claim_force: str
    condition_scope: str
    has_scope: bool
    normalized_text: str
    citation_label: str


@dataclass(frozen=True)
class PersistedTopic:
    topic_key: str
    label: str
    page_kind: str
    entry_count: int
    atom_count: int
    entry_ids: tuple[str, ...]
    atom_ids: tuple[str, ...]
    representative: TopicRepresentative


@dataclass(frozen=True)
class TopicIndex:
    """A portable source topic index persisted for cross-source synthesis."""

    source_locator: str
    source_hash: str
    projection_source_support_id: str
    topics: tuple[PersistedTopic, ...]
