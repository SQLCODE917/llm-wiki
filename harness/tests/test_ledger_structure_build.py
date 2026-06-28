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


def test_build_structure_keeps_equal_number_marker_under_parent() -> None:
    plan = build_structure(
        "sourcehash",
        "source.md",
        (
            _segment("parent", "heading", "# 5.3 Spellsongs", 1),
            _segment("marker", "heading", "## **5.3**", 2),
            _segment("child", "heading", "## **Filling out the Character Sheet**", 3),
            _segment("body", "paragraph", "Write spellsongs on the sheet.", 4),
        ),
    )

    nodes = {node.heading_text: node for node in plan.nodes}
    assert "**5.3**" not in nodes
    assert (
        nodes["**Filling out the Character Sheet**"].parent_structure_node_id
        == nodes["5.3 Spellsongs"].structure_node_id
    )
    assert (
        plan.node_for_segment["body"]
        == nodes["**Filling out the Character Sheet**"].structure_node_id
    )


def test_build_structure_collapses_numbered_title_alias() -> None:
    plan = build_structure(
        "sourcehash",
        "source.md",
        (
            _segment("parent", "heading", "# 1.4 Character Creation", 1),
            _segment("marker", "heading", "## **1.4**", 2),
            _segment("alias", "heading", "## **Character Creation**", 3),
            _segment("body", "paragraph", "Create a player character.", 4),
        ),
    )

    assert [node.heading_text for node in plan.nodes] == ["source.md", "1.4 Character Creation"]
    assert plan.node_for_segment["marker"] == plan.node_for_segment["parent"]
    assert plan.node_for_segment["alias"] == plan.node_for_segment["parent"]
    assert plan.node_for_segment["body"] == plan.node_for_segment["parent"]


def test_build_structure_uses_numbered_path_when_markdown_depth_is_flat() -> None:
    plan = build_structure(
        "sourcehash",
        "source.md",
        (
            _segment("parent", "heading", "## **5.1 Basic Rules of Magic**", 1),
            _segment("child-number", "heading", "## **5.1.2**", 2),
            _segment("child-title", "heading", "## **Rune Masters and Rune Master Skills**", 3),
            _segment("body", "paragraph", "Rune master rule.", 4),
            _segment("sibling", "heading", "## **5.1.3 Casting Magic**", 5),
            _segment("sibling-body", "paragraph", "Casting rule.", 6),
        ),
    )

    nodes = {node.heading_text: node for node in plan.nodes}
    assert (
        nodes["**5.1.2**"].parent_structure_node_id
        == nodes["**5.1 Basic Rules of Magic**"].structure_node_id
    )
    assert (
        nodes["**Rune Masters and Rune Master Skills**"].parent_structure_node_id
        == nodes["**5.1.2**"].structure_node_id
    )
    assert (
        nodes["**5.1.3 Casting Magic**"].parent_structure_node_id
        == nodes["**5.1 Basic Rules of Magic**"].structure_node_id
    )
    assert (
        plan.node_for_segment["body"]
        == nodes["**Rune Masters and Rune Master Skills**"].structure_node_id
    )
    assert (
        plan.node_for_segment["sibling-body"] == nodes["**5.1.3 Casting Magic**"].structure_node_id
    )


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
