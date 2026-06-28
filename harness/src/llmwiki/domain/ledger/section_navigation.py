"""Navigation helpers for source-structure section pages."""

from __future__ import annotations

import re
from dataclasses import dataclass

from llmwiki.domain.ledger.canonical import short_digest
from llmwiki.domain.ledger.section_planning import SectionGroundedPlan
from llmwiki.domain.ledger.structure import DocumentStructure, StructureNode
from llmwiki.domain.ledger.topic_relations import RelatedTopicLink
from llmwiki.domain.ledger.topic_terms import source_label_terms
from llmwiki.domain.pages import PageError, slugify

_MARKDOWN_DECORATION = re.compile(r"[*_`]+")
_HEADING_NUMBER = re.compile(
    r"^(?:(?:chapter|part|section|appendix|book)\s+)?\d+(?:\.\d+)*\s*[-:.]?\s*",
    re.IGNORECASE,
)


@dataclass(frozen=True)
class SectionPageRef:
    node: StructureNode
    page_id: str
    title: str


def section_page_id(source_page_id: str, structure: DocumentStructure, node: StructureNode) -> str:
    label = _safe_slug(" ".join(section_path(structure, node)))[:96]
    suffix = short_digest(node.structure_node_id, 8)
    return slugify(f"{source_page_id}-section-{label or 'section'}-{suffix}")


def section_title(structure: DocumentStructure, node: StructureNode) -> str:
    return " / ".join(section_path(structure, node))


def section_topic_key(text: str) -> str:
    return "-".join(source_label_terms(_plain_heading(_without_leading_number(text))))


def nodes_by_topic_key(nodes: tuple[StructureNode, ...]) -> dict[str, tuple[str, ...]]:
    grouped: dict[str, list[str]] = {}
    for node in nodes:
        key = section_topic_key(node.heading_text)
        if key:
            grouped.setdefault(key, []).append(node.structure_node_id)
    return {key: tuple(value) for key, value in grouped.items() if len(value) > 1}


def section_links_by_topic(
    section_plan: SectionGroundedPlan,
    structure: DocumentStructure,
    *,
    source_page_id: str,
) -> dict[str, tuple[RelatedTopicLink, ...]]:
    links: dict[str, list[RelatedTopicLink]] = {}
    for target in section_plan.page_targets:
        node = structure.node(target.structure_node_id)
        if node is None or not target.topic_key:
            continue
        links.setdefault(target.topic_key, []).append(
            RelatedTopicLink(
                page_id=section_page_id(source_page_id, structure, node),
                label=section_title(structure, node),
                relation="source section",
                shared_entry_ids=target.entry_ids,
                shared_atom_ids=target.atom_ids,
            )
        )
    return {key: tuple(dict.fromkeys(value)) for key, value in links.items()}


def related_section_links(
    ref: SectionPageRef,
    structure: DocumentStructure,
    by_node: dict[str, SectionPageRef],
    same_topic: dict[str, tuple[str, ...]],
    topic_page_ids: dict[str, str],
) -> tuple[RelatedTopicLink, ...]:
    links: list[RelatedTopicLink] = []
    parent = structure.parent(ref.node.structure_node_id)
    if parent is not None and parent.structure_node_id in by_node:
        parent_ref = by_node[parent.structure_node_id]
        links.append(
            RelatedTopicLink(parent_ref.page_id, parent_ref.title, "broader source section")
        )
    for child in structure.children(ref.node.structure_node_id):
        child_ref = by_node.get(child.structure_node_id)
        if child_ref is not None:
            links.append(
                RelatedTopicLink(child_ref.page_id, child_ref.title, "narrower source section")
            )
    topic_key = section_topic_key(ref.node.heading_text)
    if topic_key in topic_page_ids:
        links.append(
            RelatedTopicLink(
                topic_page_ids[topic_key], topic_key.replace("-", " ").title(), "topic hub"
            )
        )
    for related_node_id in same_topic.get(topic_key, ()):
        if related_node_id == ref.node.structure_node_id:
            continue
        related = by_node.get(related_node_id)
        if related is not None:
            links.append(RelatedTopicLink(related.page_id, related.title, "same source heading"))
    return tuple(dict.fromkeys(links))


def section_path(structure: DocumentStructure, node: StructureNode) -> tuple[str, ...]:
    labels: list[str] = []
    for label in structure.label_path(node.structure_node_id):
        plain = _plain_heading(label)
        if not plain or _is_number_marker(plain):
            continue
        if labels and _without_leading_number(labels[-1]).casefold() == plain.casefold():
            continue
        labels.append(plain)
    return tuple(labels or (_plain_heading(node.heading_text),))


def _plain_heading(text: str) -> str:
    return re.sub(r"\s+", " ", _MARKDOWN_DECORATION.sub("", text)).strip()


def _without_leading_number(text: str) -> str:
    return _HEADING_NUMBER.sub("", _plain_heading(text), count=1).strip()


def _is_number_marker(text: str) -> bool:
    return bool(re.fullmatch(r"\d+(?:\.\d+)*", text.strip()))


def _safe_slug(text: str) -> str:
    try:
        return slugify(text)
    except PageError:
        return "section"
