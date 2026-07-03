"""Grouping and budgets for related wiki page links."""

from __future__ import annotations

from dataclasses import dataclass

from llmwiki.domain.ledger.topic_relations import RelatedTopicLink

MAX_VISIBLE_PAGE_LINKS = 24
MAX_VISIBLE_GROUP_LINKS = 8

_GROUP_ORDER = {
    "source-order": 0,
    "source-structure": 1,
    "collection": 2,
    "procedure": 3,
    "shared-technical-atom": 4,
    "shared-claim": 5,
    "topic": 6,
    "other": 99,
}

_GROUP_TITLE = {
    "source-order": "Source order",
    "source-structure": "Source structure",
    "collection": "Collections",
    "procedure": "Procedures",
    "shared-technical-atom": "Shared technical atoms",
    "shared-claim": "Shared claims",
    "topic": "Topics",
    "other": "Other",
}


@dataclass(frozen=True)
class RelatedLinkGroup:
    group_kind: str
    title: str
    visible_links: tuple[RelatedTopicLink, ...]
    overflow_count: int = 0


def budget_related_links(
    links: tuple[RelatedTopicLink, ...],
    *,
    page_budget: int = MAX_VISIBLE_PAGE_LINKS,
    group_budget: int = MAX_VISIBLE_GROUP_LINKS,
) -> tuple[RelatedTopicLink, ...]:
    selected: list[RelatedTopicLink] = []
    for group in group_related_links(links, group_budget=group_budget):
        remaining = page_budget - len(selected)
        if remaining <= 0:
            break
        selected.extend(group.visible_links[:remaining])
    return tuple(selected)


def group_related_links(
    links: tuple[RelatedTopicLink, ...], *, group_budget: int = MAX_VISIBLE_GROUP_LINKS
) -> tuple[RelatedLinkGroup, ...]:
    grouped: dict[str, list[RelatedTopicLink]] = {}
    for link in links:
        grouped.setdefault(relation_group_kind(link.relation), []).append(link)
    result: list[RelatedLinkGroup] = []
    for group_kind, values in grouped.items():
        ordered = tuple(sorted(values, key=_link_sort_key))
        visible = ordered[:group_budget]
        result.append(
            RelatedLinkGroup(
                group_kind=group_kind,
                title=_GROUP_TITLE.get(group_kind, group_kind.replace("-", " ").title()),
                visible_links=visible,
                overflow_count=max(0, len(ordered) - len(visible)),
            )
        )
    return tuple(sorted(result, key=lambda group: _GROUP_ORDER.get(group.group_kind, 99)))


def relation_group_kind(relation: str) -> str:
    lowered = relation.lower()
    if "previous source section" in lowered or "next source section" in lowered:
        return "source-order"
    if "broader source section" in lowered or "narrower source section" in lowered:
        return "source-structure"
    if "collection" in lowered:
        return "collection"
    if "procedure" in lowered or "step" in lowered:
        return "procedure"
    if "technical atom" in lowered or "technical record" in lowered:
        return "shared-technical-atom"
    if "statement" in lowered or "claim" in lowered:
        return "shared-claim"
    if "topic" in lowered:
        return "topic"
    if "source section" in lowered:
        return "source-structure"
    return "other"


def _link_sort_key(link: RelatedTopicLink) -> tuple[int, int, str]:
    source_order_rank = {
        "previous source section": 0,
        "next source section": 1,
        "broader source section": 2,
        "narrower source section": 3,
    }
    evidence = link.shared_entry_count + (2 * link.shared_atom_count)
    return (source_order_rank.get(link.relation, 50), -evidence, link.page_id)
