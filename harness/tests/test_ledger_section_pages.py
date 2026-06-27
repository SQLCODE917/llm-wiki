from llmwiki.domain.ledger.section_pages import _page_id
from llmwiki.domain.ledger.structure import StructureNode


def test_section_page_id_falls_back_for_unsluggable_heading() -> None:
    node = StructureNode(
        structure_node_id="structure-node-code-heading",
        structure_node_kind="section",
        heading_text="() => {}",
        source_range_id="source-range-heading",
        source_locator="javascriptallonge.pdf",
        source_order=12,
    )

    assert _page_id("javascriptallonge", node).startswith("javascriptallonge-section-section-")
