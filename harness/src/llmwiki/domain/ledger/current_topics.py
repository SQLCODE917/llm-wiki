"""Evidence-led topic index for the current claim-ledger path."""

from __future__ import annotations

from collections import Counter

from llmwiki.domain.evidence_registry import EvidenceRegistry, SourceRange
from llmwiki.domain.ledger.current_projection import (
    claim_entry_by_source_claim_id,
    write_source_range_ids,
)
from llmwiki.domain.ledger.current_structure import source_range_by_unit
from llmwiki.domain.ledger.entries import LedgerEntry
from llmwiki.domain.ledger.ledger import ClaimLedger
from llmwiki.domain.ledger.topic_models import (
    PersistedTopic,
    SourceTopic,
    TopicIndex,
    TopicRepresentative,
)
from llmwiki.domain.objects import PagePlan, PlannedPageWrite
from llmwiki.domain.pages import PageError, slugify
from llmwiki.domain.planning_analysis import top_terms

_MAX_TOPICS = 32
_MIN_TERM_FREQUENCY = 2


def build_current_topic_index(
    *,
    source_locator: str,
    source_hash: str,
    projection_source_support_id: str,
    page_plan: PagePlan,
    evidence_registry: EvidenceRegistry,
    ledger: ClaimLedger,
) -> TopicIndex:
    ranges_by_unit = source_range_by_unit(page_plan, evidence_registry.source_ranges)
    entries_by_claim = claim_entry_by_source_claim_id(page_plan, evidence_registry, ledger)
    topics = _rank_topics(
        tuple(
            _planned_write_topics(page_plan, ranges_by_unit, entries_by_claim, ledger)
            + _claim_group_topics(page_plan, entries_by_claim, ledger)
            + _term_topics(page_plan, entries_by_claim, ledger)
        )
    )
    persisted = tuple(_persisted_topic(ledger, topic) for topic in topics[:_MAX_TOPICS])
    return TopicIndex(source_locator, source_hash, projection_source_support_id, persisted)


def _planned_write_topics(
    page_plan: PagePlan,
    ranges_by_unit: dict[str, SourceRange],
    entries_by_claim: dict[str, LedgerEntry],
    ledger: ClaimLedger,
) -> list[SourceTopic]:
    topics: list[SourceTopic] = []
    for write in page_plan.planned_writes:
        claim_ids = _write_claim_ids(page_plan, write)
        entry_ids = tuple(
            entry.ledger_entry_id
            for claim_id in claim_ids
            if (entry := entries_by_claim.get(claim_id)) is not None
        )
        atom_ids = _atom_ids_for_write(write, ranges_by_unit, ledger)
        if not entry_ids and not atom_ids:
            continue
        topics.append(
            SourceTopic(
                topic_key=write.page_metadata.page_id,
                label=_topic_label(write),
                page_kind=write.page_metadata.page_kind,
                match_terms=top_terms(_topic_label(write), 6),
                entry_ids=entry_ids,
                atom_ids=atom_ids,
                from_heading=True,
                salience=len(entry_ids) + 1.5 * len(atom_ids) + 2.0,
            )
        )
    return topics


def _claim_group_topics(
    page_plan: PagePlan, entries_by_claim: dict[str, LedgerEntry], ledger: ClaimLedger
) -> list[SourceTopic]:
    topics: list[SourceTopic] = []
    for group in page_plan.source_claim_groups:
        entry_ids = tuple(
            entry.ledger_entry_id
            for claim_id in group.source_claims
            if (entry := entries_by_claim.get(claim_id)) is not None
        )
        if len(entry_ids) < 2:
            continue
        topics.append(
            SourceTopic(
                topic_key=_safe_slug(group.label),
                label=group.label,
                page_kind="concept",
                match_terms=top_terms(group.label, 6),
                entry_ids=entry_ids,
                atom_ids=_atom_ids_near_entries(ledger, entry_ids),
                from_heading=False,
                salience=len(entry_ids) + group.claim_salience,
            )
        )
    return topics


def _term_topics(
    page_plan: PagePlan, entries_by_claim: dict[str, LedgerEntry], ledger: ClaimLedger
) -> list[SourceTopic]:
    claim_by_id = {claim.source_claim_id: claim for claim in page_plan.source_claims}
    counts: Counter[str] = Counter(
        term for claim in claim_by_id.values() for term in claim.subject_terms
    )
    topics: list[SourceTopic] = []
    for term, frequency in counts.most_common():
        if frequency < _MIN_TERM_FREQUENCY:
            break
        claim_ids = tuple(
            claim.source_claim_id for claim in claim_by_id.values() if term in claim.subject_terms
        )
        entry_ids = tuple(
            entry.ledger_entry_id
            for claim_id in claim_ids
            if (entry := entries_by_claim.get(claim_id)) is not None
        )
        if len(entry_ids) < _MIN_TERM_FREQUENCY:
            continue
        topics.append(
            SourceTopic(
                topic_key=_safe_slug(term),
                label=term.title(),
                page_kind="concept",
                match_terms=(term,),
                entry_ids=entry_ids,
                atom_ids=_atom_ids_near_entries(ledger, entry_ids),
                from_heading=False,
                salience=float(len(entry_ids)),
            )
        )
    return topics


def _rank_topics(topics: tuple[SourceTopic, ...]) -> tuple[SourceTopic, ...]:
    merged: dict[str, SourceTopic] = {}
    for topic in topics:
        existing = merged.get(topic.topic_key)
        if existing is None:
            merged[topic.topic_key] = topic
            continue
        merged[topic.topic_key] = SourceTopic(
            topic_key=existing.topic_key,
            label=existing.label,
            page_kind=existing.page_kind,
            match_terms=tuple(dict.fromkeys((*existing.match_terms, *topic.match_terms))),
            entry_ids=tuple(dict.fromkeys((*existing.entry_ids, *topic.entry_ids))),
            atom_ids=tuple(dict.fromkeys((*existing.atom_ids, *topic.atom_ids))),
            from_heading=existing.from_heading or topic.from_heading,
            salience=max(existing.salience, topic.salience)
            + 0.25 * (len(topic.entry_ids) + len(topic.atom_ids)),
        )
    return tuple(sorted(merged.values(), key=lambda item: (-item.salience, item.topic_key)))


def _persisted_topic(ledger: ClaimLedger, topic: SourceTopic) -> PersistedTopic:
    return PersistedTopic(
        topic_key=topic.topic_key,
        label=topic.label,
        page_kind=topic.page_kind,
        entry_count=len(topic.entry_ids),
        atom_count=len(topic.atom_ids),
        entry_ids=topic.entry_ids,
        atom_ids=topic.atom_ids,
        representative=_representative(ledger, topic),
    )


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


def _atom_ids_for_write(
    write: PlannedPageWrite, ranges_by_unit: dict[str, SourceRange], ledger: ClaimLedger
) -> tuple[str, ...]:
    write_ranges = write_source_range_ids(write, ranges_by_unit)
    return tuple(
        dict.fromkeys(
            entry.technical_atom_id
            for entry in ledger.usable_entries
            if entry.ledger_entry_kind == "technical-atom"
            and entry.technical_atom_id
            and entry.source_range_id in write_ranges
        )
    )


def _atom_ids_near_entries(ledger: ClaimLedger, entry_ids: tuple[str, ...]) -> tuple[str, ...]:
    source_ranges = {
        entry.source_range_id
        for entry_id in entry_ids
        if (entry := ledger.entry(entry_id)) is not None
    }
    return tuple(
        dict.fromkeys(
            entry.technical_atom_id
            for entry in ledger.usable_entries
            if entry.ledger_entry_kind == "technical-atom"
            and entry.technical_atom_id
            and entry.source_range_id in source_ranges
        )
    )


def _write_claim_ids(page_plan: PagePlan, write: PlannedPageWrite) -> tuple[str, ...]:
    if write.source_summary_plan is not None:
        return write.source_summary_plan.selected_source_claims
    unit_ids = frozenset(write.extracted_units)
    return tuple(
        claim.source_claim_id
        for claim in page_plan.source_claims
        if claim.extracted_unit_id in unit_ids
    )


def _topic_label(write: PlannedPageWrite) -> str:
    return write.page_metadata.summary or write.page_metadata.page_id.replace("-", " ").title()


def _safe_slug(label: str) -> str:
    try:
        return slugify(label)
    except PageError:
        return "topic"
