from llmwiki.domain.ledger.segments import SourceSegment
from llmwiki.domain.ledger.structure_build import build_structure


def test_build_structure_collapses_nested_markdown_duplicate_heading() -> None:
    plan = build_structure(
        "sourcehash",
        "source.md",
        (
            _segment("chapter", "heading", "# Garbage, Garbage Everywhere", 1),
            _segment("page-header", "paragraph", "Composing and Decomposing Data\n103", 2),
            _segment("duplicate", "heading", "## **Garbage, Garbage Everywhere**", 3),
            _segment("body", "paragraph", "The source section begins here.", 4),
        ),
    )

    assert len(plan.nodes) == 2
    assert plan.nodes[1].heading_text == "Garbage, Garbage Everywhere"
    assert plan.node_for_segment["duplicate"] == plan.node_for_segment["chapter"]
    assert plan.node_for_segment["body"] == plan.node_for_segment["chapter"]


def test_build_structure_keeps_same_label_when_parent_is_different() -> None:
    plan = build_structure(
        "sourcehash",
        "source.md",
        (
            _segment("chapter", "heading", "# Alpha", 1),
            _segment("details", "heading", "## Details", 2),
            _segment("nested-alpha", "heading", "### Alpha", 3),
            _segment("body", "paragraph", "Nested Alpha has its own content.", 4),
        ),
    )

    assert [node.heading_text for node in plan.nodes] == [
        "source.md",
        "Alpha",
        "Details",
        "Alpha",
    ]
    assert plan.node_for_segment["nested-alpha"] != plan.node_for_segment["chapter"]
    assert plan.node_for_segment["body"] == plan.node_for_segment["nested-alpha"]


def _segment(segment_id: str, kind: str, text: str, order: int) -> SourceSegment:
    return SourceSegment(
        segment_id=segment_id,
        source_range_id=f"range-{segment_id}",
        source_locator="source.md",
        source_hash="sourcehash",
        heading_path="",
        structure_node_id="",
        source_order=order,
        text=text,
        segment_kind=kind,
    )
