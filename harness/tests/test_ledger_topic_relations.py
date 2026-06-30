from llmwiki.domain.ledger.topic_models import SourceTopic
from llmwiki.domain.ledger.topic_relations import related_topic_links


def test_related_topic_links_are_reciprocal_for_shared_evidence() -> None:
    topics = (
        _topic("skeleton-warrior", "Skeleton Warrior", ("entry-command",)),
        _topic("caster", "Caster", ("entry-command",)),
    )

    links = related_topic_links(topics, source_page_id="rules")

    assert links["skeleton-warrior"][0].page_id == "rules-caster"
    assert links["caster"][0].page_id == "rules-skeleton-warrior"
    assert links["skeleton-warrior"][0].shared_entry_ids == ("entry-command",)


def test_related_topic_links_keep_strongest_bounded_neighbors() -> None:
    hub = _topic("hub", "Hub", tuple(f"entry-{index:02d}" for index in range(30)))
    spokes = tuple(
        _topic(f"spoke-{index:02d}", f"Spoke {index:02d}", (f"entry-{index:02d}",))
        for index in range(30)
    )

    links = related_topic_links((hub, *spokes), source_page_id="rules")

    assert len(links["hub"]) == 24
    assert links["hub"][0].page_id == "rules-spoke-00"
    assert links["hub"][-1].page_id == "rules-spoke-23"


def _topic(topic_key: str, label: str, entry_ids: tuple[str, ...]) -> SourceTopic:
    return SourceTopic(
        topic_key=topic_key,
        label=label,
        page_kind="concept",
        match_terms=tuple(topic_key.split("-")),
        entry_ids=entry_ids,
        atom_ids=(),
        from_heading=True,
        salience=float(len(entry_ids)),
    )
