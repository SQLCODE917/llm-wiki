"""Load persisted per-source topic indexes into the cross-source read model."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any

from llmwiki.domain.ledger.cross_source import SourcePosition


@dataclass(frozen=True)
class LoadedTopic:
    source_locator: str
    source_hash: str
    projection_source_support_id: str
    topic_key: str
    label: str
    page_kind: str
    entry_ids: tuple[str, ...]
    atom_ids: tuple[str, ...]
    position: SourcePosition


@dataclass(frozen=True)
class LoadedSource:
    source_locator: str
    source_hash: str
    projection_source_support_id: str
    topics: tuple[LoadedTopic, ...]

    @property
    def positions(self) -> tuple[SourcePosition, ...]:
        return tuple(topic.position for topic in self.topics)


@dataclass(frozen=True)
class LoadedLedger:
    source_locator: str
    entries: dict[str, dict[str, Any]]
    atoms: dict[str, dict[str, Any]]
    atom_contexts: dict[str, tuple[dict[str, Any], ...]]


@dataclass(frozen=True)
class LoadedSources:
    sources: tuple[LoadedSource, ...]
    ledgers: dict[str, LoadedLedger]

    @property
    def positions(self) -> tuple[SourcePosition, ...]:
        return tuple(position for source in self.sources for position in source.positions)


def load_sources(
    topic_index_jsons: tuple[str, ...], claim_ledger_jsons: tuple[str, ...]
) -> LoadedSources:
    sources = tuple(load_source_positions(text) for text in topic_index_jsons)
    ledgers = {
        ledger.source_locator: ledger
        for ledger in (load_claim_ledger(text) for text in claim_ledger_jsons)
    }
    return LoadedSources(sources, ledgers)


def load_source_positions(topic_index_json: str) -> LoadedSource:
    index = json.loads(topic_index_json)
    source_locator = index["source_locator"]
    source_hash = index["source_hash"]
    support_id = index["projection_source_support_id"]
    topics = tuple(
        _topic(topic, source_locator, source_hash, support_id)
        for topic in index.get("topics", ())
        if topic.get("topic_key")
    )
    return LoadedSource(source_locator, source_hash, support_id, topics)


def load_claim_ledger(claim_ledger_json: str) -> LoadedLedger:
    artifact = json.loads(claim_ledger_json)
    ledger = artifact["ledger"]
    entries = {
        entry["ledger_entry_id"]: entry
        for entry in ledger.get("entries", ())
        if entry.get("ledger_entry_id")
    }
    atoms = {
        atom["technical_atom_id"]: atom
        for atom in ledger.get("technical_atoms", ())
        if atom.get("technical_atom_id")
    }
    contexts: dict[str, list[dict[str, Any]]] = {}
    for context in ledger.get("technical_atom_contexts", ()):
        atom_id = context.get("technical_atom_id")
        if atom_id:
            contexts.setdefault(atom_id, []).append(context)
    return LoadedLedger(
        source_locator=ledger["source_locator"],
        entries=entries,
        atoms=atoms,
        atom_contexts={key: tuple(value) for key, value in contexts.items()},
    )


def _topic(
    topic: dict[str, Any], source_locator: str, source_hash: str, support_id: str
) -> LoadedTopic:
    return LoadedTopic(
        source_locator=source_locator,
        source_hash=source_hash,
        projection_source_support_id=support_id,
        topic_key=topic["topic_key"],
        label=topic.get("label", topic["topic_key"].replace("-", " ").title()),
        page_kind=topic.get("page_kind", "concept"),
        entry_ids=tuple(str(entry_id) for entry_id in topic.get("entry_ids", ())),
        atom_ids=tuple(str(atom_id) for atom_id in topic.get("atom_ids", ())),
        position=_position(topic, source_locator, source_hash, support_id),
    )


def _position(
    topic: dict[str, Any], source_locator: str, source_hash: str, support_id: str
) -> SourcePosition:
    representative = topic.get("representative") or {}
    return SourcePosition(
        source_locator=source_locator,
        source_hash=source_hash,
        projection_source_support_id=support_id,
        ledger_entry_id=representative.get("ledger_entry_id", f"topic-{topic['topic_key']}"),
        ledger_entry_kind="concept",
        subject=representative.get("subject", ""),
        predicate=representative.get("predicate", ""),
        polarity=representative.get("polarity", ""),
        claim_force=representative.get("claim_force", ""),
        condition_scope=representative.get("condition_scope", "unconditional"),
        has_scope=bool(representative.get("has_scope", False)),
        normalized_text=representative.get("normalized_text", topic.get("label", "")),
        concept_facets=(topic["topic_key"],),
        topic_keys=(topic["topic_key"],),
        evidence_ids=(),
        citation_label=representative.get("citation_label", source_locator),
    )
