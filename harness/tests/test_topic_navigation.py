import json

from llmwiki.domain.topic_navigation import reconcile_topic_links, topic_index_prompt_block


def test_topic_index_prompt_and_reconcile_filter_to_existing_pages() -> None:
    topic_index = json.dumps(
        {
            "topics": [
                {"topic_key": "alpha", "entry_count": 3, "atom_count": 1},
                {"topic_key": "missing", "entry_count": 9, "atom_count": 0},
                {"topic_key": "beta", "entry_count": 2, "atom_count": 0},
            ]
        }
    )
    existing = frozenset({"alpha", "beta"})

    prompt = topic_index_prompt_block(topic_index, existing)
    body = reconcile_topic_links(
        "Intro\n\n**Key topics:** [[old-topic]]",
        topic_index,
        existing,
    )

    assert prompt == "Source topic index: [[alpha]] (4), [[beta]] (2)"
    assert body == "Intro\n\n**Key topics:** [[alpha]], [[beta]]"
