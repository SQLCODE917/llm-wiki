"""Universal projection policy for rendered wiki pages.

Projection policy is source-agnostic. It classifies pages by their rendered
role and classifies source-derived units by whether they may stand alone.
Renderers consume these decisions instead of rediscovering them locally.
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass

from llmwiki.domain.ledger.entries import LedgerEntry
from llmwiki.domain.ledger.evidence_blocks import EvidenceBlock
from llmwiki.domain.ledger.ledger import ClaimLedger
from llmwiki.domain.ledger.projection_context import ProjectionContext
from llmwiki.domain.ledger.projection_substance import entry_is_unresolved_context_pointer
from llmwiki.domain.ledger.topic_models import SourceTopic

PAGE_FAMILY_SOURCE_MANIFEST = "source-manifest"
PAGE_FAMILY_SECTION_REFERENCE = "section-reference"
PAGE_FAMILY_TOPIC_CONCEPT = "topic-concept"
PAGE_FAMILY_BROAD_TOPIC = "broad-topic"
PAGE_FAMILY_PROCEDURE_GUIDE = "procedure-guide"
PAGE_FAMILY_COLLECTION_PAGE = "collection-page"

PROJECTION_ELIGIBILITY_STANDALONE = "standalone-claim"
PROJECTION_ELIGIBILITY_CONTEXTUAL_ONLY = "contextual-only"
PROJECTION_ELIGIBILITY_TECHNICAL_FRAME_ONLY = "technical-frame-only"
PROJECTION_ELIGIBILITY_REVIEW_ONLY = "review-only"

_BROAD_TOPIC_MIN_ENTRIES = 48
_BROAD_TOPIC_MIN_SECTIONS = 12
_BROAD_TOPIC_MIN_SOURCE_ORDER_SPAN = 1_200
_BROAD_TOPIC_MAX_BLOCKS_PER_SECTION = 3
_BROAD_TOPIC_MAX_SECTIONS = 24


@dataclass(frozen=True)
class ProjectionBudget:
    broad_topic_min_entries: int = _BROAD_TOPIC_MIN_ENTRIES
    broad_topic_min_sections: int = _BROAD_TOPIC_MIN_SECTIONS
    broad_topic_min_source_order_span: int = _BROAD_TOPIC_MIN_SOURCE_ORDER_SPAN
    broad_topic_max_blocks_per_section: int = _BROAD_TOPIC_MAX_BLOCKS_PER_SECTION
    broad_topic_max_sections: int = _BROAD_TOPIC_MAX_SECTIONS


DEFAULT_PROJECTION_BUDGET = ProjectionBudget()


@dataclass(frozen=True)
class TopicProjectionPolicy:
    page_family: str
    source_order_span: int
    section_count: int
    selected_entry_count: int
    selected_atom_count: int
    max_blocks_per_section: int = 0
    max_sections: int = 0

    @property
    def is_broad_topic(self) -> bool:
        return self.page_family == PAGE_FAMILY_BROAD_TOPIC


def topic_projection_policy(
    topic: SourceTopic,
    ledger: ClaimLedger,
    projection_context: ProjectionContext | None,
    *,
    budget: ProjectionBudget | None = None,
) -> TopicProjectionPolicy:
    resolved_budget = budget or DEFAULT_PROJECTION_BUDGET
    orders = _topic_source_orders(topic, ledger, projection_context)
    span = max(orders) - min(orders) if orders else 0
    section_count = _topic_section_count(topic, projection_context)
    entry_count = len(topic.entry_ids)
    atom_count = len(topic.atom_ids)
    is_broad = (
        entry_count >= resolved_budget.broad_topic_min_entries
        or section_count >= resolved_budget.broad_topic_min_sections
        or span >= resolved_budget.broad_topic_min_source_order_span
    )
    if not is_broad:
        return TopicProjectionPolicy(
            page_family=PAGE_FAMILY_TOPIC_CONCEPT,
            source_order_span=span,
            section_count=section_count,
            selected_entry_count=entry_count,
            selected_atom_count=atom_count,
        )
    return TopicProjectionPolicy(
        page_family=PAGE_FAMILY_BROAD_TOPIC,
        source_order_span=span,
        section_count=section_count,
        selected_entry_count=entry_count,
        selected_atom_count=atom_count,
        max_blocks_per_section=resolved_budget.broad_topic_max_blocks_per_section,
        max_sections=resolved_budget.broad_topic_max_sections,
    )


def ledger_entry_projection_eligibility(entry: LedgerEntry) -> str:
    if not entry.is_usable:
        return PROJECTION_ELIGIBILITY_REVIEW_ONLY
    if entry.ledger_entry_kind == "technical-atom":
        return PROJECTION_ELIGIBILITY_TECHNICAL_FRAME_ONLY
    if entry_is_unresolved_context_pointer(entry):
        return PROJECTION_ELIGIBILITY_CONTEXTUAL_ONLY
    if (entry.normalized_text or entry.source_text).strip():
        return PROJECTION_ELIGIBILITY_STANDALONE
    return PROJECTION_ELIGIBILITY_REVIEW_ONLY


def entry_can_render_standalone(entry: LedgerEntry) -> bool:
    return ledger_entry_projection_eligibility(entry) == PROJECTION_ELIGIBILITY_STANDALONE


def select_evidence_blocks_for_policy(
    blocks: tuple[EvidenceBlock, ...], policy: TopicProjectionPolicy
) -> tuple[EvidenceBlock, ...]:
    if not policy.is_broad_topic or not policy.max_blocks_per_section:
        return blocks
    selected: list[EvidenceBlock] = []
    by_section: dict[str, list[EvidenceBlock]] = defaultdict(list)
    section_order: list[str] = []
    for block in blocks:
        section = str(getattr(block, "section_label", ""))
        if section not in by_section:
            section_order.append(section)
        by_section[section].append(block)
    for section in section_order[: policy.max_sections]:
        selected.extend(by_section[section][: policy.max_blocks_per_section])
    return tuple(selected)


def _topic_section_count(topic: SourceTopic, projection_context: ProjectionContext | None) -> int:
    if projection_context is None:
        return 0
    sections = {
        block.section_label
        for block in projection_context.blocks_for_entries(topic.entry_ids)
        if block.section_label
    }
    return len(sections)


def _topic_source_orders(
    topic: SourceTopic,
    ledger: ClaimLedger,
    projection_context: ProjectionContext | None,
) -> tuple[int, ...]:
    orders: list[int] = []
    if projection_context is not None:
        orders.extend(
            block.source_order for block in projection_context.blocks_for_entries(topic.entry_ids)
        )
        orders.extend(
            frame.source_order for frame in projection_context.frames_for_atoms(topic.atom_ids)
        )
    if orders:
        return tuple(order for order in orders if order > 0)
    order_by_range = {
        statement.source_range_id: index
        for index, statement in enumerate(ledger.source_statements, start=1)
    }
    for entry_id in topic.entry_ids:
        entry = ledger.entry(entry_id)
        if entry is not None:
            orders.append(order_by_range.get(entry.source_range_id, 0))
    for atom_id in topic.atom_ids:
        atom = ledger.atom(atom_id)
        if atom is not None:
            orders.append(order_by_range.get(atom.source_range_id, 0))
    return tuple(order for order in orders if order > 0)
