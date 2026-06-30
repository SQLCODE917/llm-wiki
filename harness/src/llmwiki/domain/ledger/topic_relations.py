"""Evidence-backed related-page links for source topic pages."""

from __future__ import annotations

from dataclasses import dataclass

from llmwiki.domain.ledger.topic_models import SourceTopic
from llmwiki.domain.ledger.topic_terms import source_label_terms, topic_term_role
from llmwiki.domain.pages import slugify

_MAX_RELATED_LINKS_PER_TOPIC = 24


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


@dataclass(frozen=True)
class _PreparedTopic:
    topic: SourceTopic
    page_id: str
    terms: frozenset[str]
    entry_ids: frozenset[str]
    atom_ids: frozenset[str]


def related_topic_links(
    topics: tuple[SourceTopic, ...], *, source_page_id: str
) -> dict[str, tuple[RelatedTopicLink, ...]]:
    """Build reciprocal related-page links for every topic in one source."""
    links: dict[str, list[RelatedTopicLink]] = {topic.topic_key: [] for topic in topics}
    prepared = tuple(_prepare_topic(topic, source_page_id) for topic in topics)
    for left_index, left in enumerate(prepared):
        for right in prepared[left_index + 1 :]:
            left_link = _link(left, right)
            right_link = _link(right, left)
            if left_link is None or right_link is None:
                continue
            _append_bounded(links[left.topic.topic_key], left_link)
            _append_bounded(links[right.topic.topic_key], right_link)
    return {key: tuple(value) for key, value in links.items()}


def _prepare_topic(topic: SourceTopic, source_page_id: str) -> _PreparedTopic:
    return _PreparedTopic(
        topic=topic,
        page_id=slugify(f"{source_page_id}-{topic.topic_key}"),
        terms=_topic_terms(topic),
        entry_ids=frozenset(topic.entry_ids),
        atom_ids=frozenset(topic.atom_ids),
    )


def _link(current: _PreparedTopic, other: _PreparedTopic) -> RelatedTopicLink | None:
    shared_entries = tuple(
        entry_id for entry_id in current.topic.entry_ids if entry_id in other.entry_ids
    )
    shared_atoms = tuple(atom_id for atom_id in current.topic.atom_ids if atom_id in other.atom_ids)
    relation = _hierarchy_relation(current, other) or _shared_evidence_relation(
        len(shared_entries), len(shared_atoms)
    )
    if relation is None:
        return None
    return RelatedTopicLink(
        page_id=other.page_id,
        label=other.topic.label,
        relation=relation,
        shared_entry_ids=shared_entries,
        shared_atom_ids=shared_atoms,
    )


def _hierarchy_relation(current: _PreparedTopic, other: _PreparedTopic) -> str | None:
    current_terms = current.terms
    other_terms = other.terms
    if not current_terms or not other_terms or current_terms == other_terms:
        return None
    if current_terms < other_terms:
        return "narrower topic"
    if other_terms < current_terms:
        return "broader topic"
    return None


def _append_bounded(bucket: list[RelatedTopicLink], link: RelatedTopicLink) -> None:
    bucket.append(link)
    bucket.sort(key=_link_sort_key)
    del bucket[_MAX_RELATED_LINKS_PER_TOPIC:]


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
