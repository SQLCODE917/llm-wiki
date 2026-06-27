"""Per-source topic index facade.

Topic planning is evidence-led: lexical terms can suggest candidates, but
heading containment, concept facets, or repeated ledger subjects decide which
source-backed statements appear on a topic page. This module keeps the public
topic API stable for renderers, pipelines, and tests.
"""

from __future__ import annotations

from llmwiki.domain.ledger.ledger import ClaimLedger
from llmwiki.domain.ledger.topic_models import (
    PersistedTopic,
    SourceTopic,
    TopicIndex,
    TopicRepresentative,
)
from llmwiki.domain.ledger.topic_planner import plan_source_topics


def build_topic_index(
    ledger: ClaimLedger,
    topics: tuple[SourceTopic, ...],
    *,
    source_locator: str,
    source_hash: str,
    projection_source_support_id: str,
) -> TopicIndex:
    persisted = tuple(
        PersistedTopic(
            topic_key=topic.topic_key,
            label=topic.label,
            page_kind=topic.page_kind,
            entry_count=len(topic.entry_ids),
            atom_count=len(topic.atom_ids),
            entry_ids=topic.entry_ids,
            atom_ids=topic.atom_ids,
            representative=_representative(ledger, topic),
        )
        for topic in topics
    )
    return TopicIndex(source_locator, source_hash, projection_source_support_id, persisted)


def _representative(ledger: ClaimLedger, topic: SourceTopic) -> TopicRepresentative:
    for entry_id in topic.entry_ids:
        entry = ledger.entry(entry_id)
        if entry is None:
            continue
        has_scope = (
            entry.condition_scope in ("conditional", "exception")
            or entry.temporal_scope is not None
            or entry.spatial_scope is not None
        )
        return TopicRepresentative(
            ledger_entry_id=entry.ledger_entry_id,
            subject=entry.subject,
            predicate=entry.predicate,
            polarity=entry.polarity,
            claim_force=entry.claim_force,
            condition_scope=entry.condition_scope,
            has_scope=has_scope,
            normalized_text=entry.normalized_text or entry.source_text,
            citation_label=f"{entry.source_locator} ({entry.source_range_id})",
        )
    return TopicRepresentative(
        ledger_entry_id=f"topic-{topic.topic_key}",
        subject="",
        predicate="",
        polarity="",
        claim_force="",
        condition_scope="unconditional",
        has_scope=False,
        normalized_text=topic.label,
        citation_label=topic.label,
    )


__all__ = (
    "PersistedTopic",
    "SourceTopic",
    "TopicIndex",
    "TopicRepresentative",
    "build_topic_index",
    "plan_source_topics",
)
