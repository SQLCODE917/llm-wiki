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


def test_build_structure_reparents_numbered_heading_that_precedes_parent() -> None:
    plan = build_structure(
        "sourcehash",
        "source.md",
        (
            _segment("synthetic", "heading", "# 4.10 Excellent Weapons and Armor", 1),
            _segment("mercy", "heading", "## **4.9.4 Mercy**", 2),
            _segment("mercy-body", "paragraph", "Mercy rule.", 3),
            _segment("number", "heading", "## **4.10**", 4),
            _segment("title", "heading", "## **Excellent Weapons and Armor**", 5),
            _segment("title-body", "paragraph", "Equipment rule.", 6),
        ),
    )

    nodes = {node.heading_text: node for node in plan.nodes}
    assert nodes["**4.9.4 Mercy**"].parent_structure_node_id == plan.root_node_id
    assert plan.node_for_segment["mercy-body"] == nodes["**4.9.4 Mercy**"].structure_node_id
    assert (
        plan.node_for_segment["title-body"]
        == nodes["**Excellent Weapons and Armor**"].structure_node_id
    )


def test_build_structure_keeps_numbered_child_under_matching_parent() -> None:
    plan = build_structure(
        "sourcehash",
        "source.md",
        (
            _segment("parent", "heading", "# 4.10 Excellent Weapons and Armor", 1),
            _segment("child", "heading", "## 4.10.1 High-Quality Weapons", 2),
            _segment("body", "paragraph", "High-quality weapon rule.", 3),
        ),
    )

    nodes = {node.heading_text: node for node in plan.nodes}
    assert (
        nodes["4.10.1 High-Quality Weapons"].parent_structure_node_id
        == nodes["4.10 Excellent Weapons and Armor"].structure_node_id
    )
    assert plan.node_for_segment["body"] == nodes["4.10.1 High-Quality Weapons"].structure_node_id


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
