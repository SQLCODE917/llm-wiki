"""Evidence-backed related-page links for source topic pages."""

from __future__ import annotations

from dataclasses import dataclass

from llmwiki.domain.ledger.topic_models import SourceTopic
from llmwiki.domain.ledger.topic_terms import source_label_terms, topic_term_role
from llmwiki.domain.pages import slugify


@dataclass(frozen=True)
class RelatedTopicLink:
    page_id: str
    label: str
    relation: str
    shared_entry_ids: tuple[str, ...] = ()
    shared_atom_ids: tuple[str, ...] = ()
    explanation: str = ""

    @property
    def shared_entry_count(self) -> int:
        return len(self.shared_entry_ids)

    @property
    def shared_atom_count(self) -> int:
        return len(self.shared_atom_ids)


def related_topic_links(
    topics: tuple[SourceTopic, ...], *, source_page_id: str
) -> dict[str, tuple[RelatedTopicLink, ...]]:
    """Build reciprocal related-page links for every topic in one source."""
    page_ids = {topic.topic_key: slugify(f"{source_page_id}-{topic.topic_key}") for topic in topics}
    links: dict[str, list[RelatedTopicLink]] = {topic.topic_key: [] for topic in topics}
    for left_index, left in enumerate(topics):
        for right in topics[left_index + 1 :]:
            left_link = _link(left, right, page_ids[right.topic_key])
            right_link = _link(right, left, page_ids[left.topic_key])
            if left_link is None or right_link is None:
                continue
            links[left.topic_key].append(left_link)
            links[right.topic_key].append(right_link)
    return {key: tuple(sorted(value, key=_link_sort_key)) for key, value in links.items()}


def _link(current: SourceTopic, other: SourceTopic, other_page_id: str) -> RelatedTopicLink | None:
    other_entry_ids = set(other.entry_ids)
    other_atom_ids = set(other.atom_ids)
    shared_entries = tuple(
        entry_id for entry_id in current.entry_ids if entry_id in other_entry_ids
    )
    shared_atoms = tuple(atom_id for atom_id in current.atom_ids if atom_id in other_atom_ids)
    relation = _hierarchy_relation(current, other) or _shared_evidence_relation(
        len(shared_entries), len(shared_atoms)
    )
    if relation is None:
        return None
    return RelatedTopicLink(
        page_id=other_page_id,
        label=other.label,
        relation=relation,
        shared_entry_ids=shared_entries,
        shared_atom_ids=shared_atoms,
    )


def _hierarchy_relation(current: SourceTopic, other: SourceTopic) -> str | None:
    current_terms = _topic_terms(current)
    other_terms = _topic_terms(other)
    if not current_terms or not other_terms or current_terms == other_terms:
        return None
    if current_terms < other_terms:
        return "narrower topic"
    if other_terms < current_terms:
        return "broader topic"
    return None


def _shared_evidence_relation(shared_entries: int, shared_atoms: int) -> str | None:
    if shared_entries and shared_atoms:
        return "shared statements and technical atoms"
    if shared_atoms:
        return "shared technical atoms"
    if shared_entries:
        return "shared statements"
    return None


def _topic_terms(topic: SourceTopic) -> frozenset[str]:
    terms: list[str] = []
    terms.extend(topic.match_terms)
    terms.extend(source_label_terms(topic.label))
    terms.extend(source_label_terms(topic.topic_key.replace("-", " ")))
    return frozenset(
        term
        for term in terms
        if topic_term_role(term) not in ("discourse-container", "structural-container")
    )


def _link_sort_key(link: RelatedTopicLink) -> tuple[int, int, str]:
    relation_order = {
        "broader topic": 0,
        "narrower topic": 1,
        "shared statements and technical atoms": 2,
        "shared technical atoms": 3,
        "shared statements": 4,
    }
    evidence = link.shared_entry_count + (2 * link.shared_atom_count)
    return (relation_order.get(link.relation, 99), -evidence, link.page_id)
