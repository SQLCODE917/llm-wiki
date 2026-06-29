from llmwiki.domain.ledger.builder import build_claim_ledger, default_schema_bundle
from llmwiki.domain.objects import Schema
from llmwiki.pdf.document import DocumentElement, DocumentModel
from llmwiki.runtime.document_model_segmentation import segment_document_model
from llmwiki.runtime.ledger_segmentation import ChunkText, segment_chunks


def test_segment_chunks_bounds_analysis_without_truncating_segment_text() -> None:
    text = "This rule applies. " + ("very long extracted text " * 10_000)

    inputs, profiles = segment_chunks(
        (ChunkText("unit-1", "p.1", "Rules", text),),
        source_locator="rules.pdf",
        source_hash="source-hash",
        schema=Schema(),
    )

    assert len(inputs[0].segment.text) > 80_000
    assert inputs[0].segment.text.startswith("This rule applies.")
    assert inputs[0].claims
    assert set(profiles) == {inputs[0].segment.segment_id}


def test_segment_chunks_merges_layout_split_prose_before_source_ranges() -> None:
    text = (
        "A character remains alive.\n\n"
        "If left untreated, they must make another death check after 1 hour, and\n\n"
        "again, will only die on double ones. If successful, they awaken."
    )

    inputs, _profiles = segment_chunks(
        (ChunkText("unit-1", "p.1", "Mercy", text),),
        source_locator="rules.pdf",
        source_hash="source-hash",
        schema=Schema(),
    )

    segment_texts = tuple(item.segment.text for item in inputs)
    assert any(
        text
        == (
            "If left untreated, they must make another death check after 1 hour, and "
            "again, will only die on double ones. If successful, they awaken."
        )
        for text in segment_texts
    )
    assert "If left untreated, they must make another death check after 1 hour, and" not in (
        text.strip() for text in segment_texts
    )


def test_fragmentary_rule_atom_becomes_review_work_when_unmerged() -> None:
    inputs, profiles = segment_chunks(
        (
            ChunkText(
                "unit-1",
                "p.1",
                "Mercy",
                "If left untreated, they must make another death check after 1 hour, and",
            ),
        ),
        source_locator="rules.pdf",
        source_hash="source-hash",
        schema=Schema(),
    )

    result = build_claim_ledger(
        source_locator="rules.pdf",
        source_hash="source-hash",
        evidence_registry_hash="registry-hash",
        segments=inputs,
        profiles=profiles,
        schema=default_schema_bundle(),
    )

    assert not result.ledger.usable_entries
    assert result.ledger.needs_review_entries[0].review_reason is not None
    assert result.ledger.needs_review_entries[0].review_reason.reason_kind == "fragmentary"
    assert result.ledger.technical_atoms[0].review_reason is not None


def test_document_model_segmentation_preserves_table_section_heading_for_structure() -> None:
    model = _document_model(
        (
            _element("e1", "heading", "Character Traits", "Character Traits", heading_level=2),
            _element("e2", "paragraph", "Character Traits", "1 Angular face"),
            _element("e3", "list_item", "Character Traits", "2 Scarred face"),
            _element("e4", "heading", "Bonds", "Bonds", heading_level=2),
            _element("e5", "paragraph", "Bonds", "1 Inherited a worn map"),
            _element("e6", "list_item", "Bonds", "2 Owe a debt to a stranger"),
        )
    )

    inputs, profiles = segment_document_model(
        model, source_locator="generic.pdf", source_hash="g" * 64, schema=Schema()
    )
    result = build_claim_ledger(
        source_locator="generic.pdf",
        source_hash="g" * 64,
        evidence_registry_hash="registry",
        segments=inputs,
        profiles=profiles,
        schema=default_schema_bundle(),
    )

    table_entry = next(
        entry
        for entry in result.ledger.entries
        if entry.technical_atom_kind == "table" and "Inherited a worn map" in entry.source_text
    )
    nearest = result.document_structure.node(table_entry.structure_node_ids[0])

    assert nearest is not None
    assert nearest.heading_text == "Bonds"


def test_document_model_segmentation_keeps_wrapped_numbered_table_together() -> None:
    model = _document_model(
        (
            _element("e1", "heading", "Results", "Results", heading_level=2),
            _element("e2", "paragraph", "Results", "1 First result starts here"),
            _element("e3", "paragraph", "Results", "and continues without a marker"),
            _element("e4", "paragraph", "Results", "with one more wrapped line"),
            _element("e5", "paragraph", "Results", "with a third wrapped line"),
            _element("e6", "paragraph", "Results", "with a fourth wrapped line"),
            _element("e7", "list_item", "Results", "2 Second result starts here"),
            _element("e8", "paragraph", "Results", "Closing prose is outside the table."),
        )
    )

    inputs, _profiles = segment_document_model(
        model, source_locator="generic.pdf", source_hash="i" * 64, schema=Schema()
    )

    assert [item.segment.segment_kind for item in inputs] == [
        "heading",
        "table-block",
        "paragraph",
    ]
    assert "with one more wrapped line" in inputs[1].segment.text
    assert "with a fourth wrapped line" in inputs[1].segment.text
    assert "2 Second result starts here" in inputs[1].segment.text


def test_document_model_segmentation_keeps_table_caption_as_atom_text_only() -> None:
    model = _document_model(
        (
            _element("e1", "heading", "Table- Sample Matrix", "Table- Sample Matrix"),
            _element("e2", "paragraph", "Sample Matrix", "1 Alpha result"),
            _element("e3", "list_item", "Sample Matrix", "2 Beta result"),
        )
    )

    inputs, _profiles = segment_document_model(
        model, source_locator="generic.pdf", source_hash="h" * 64, schema=Schema()
    )

    assert [item.segment.segment_kind for item in inputs] == ["table-block"]
    assert inputs[0].segment.text.startswith("Table- Sample Matrix")


def _element(
    element_id: str,
    element_kind: str,
    heading_path: str,
    text: str,
    *,
    page: int = 1,
    heading_level: int = 0,
    body_state: str = "body",
) -> DocumentElement:
    markdown = f"{'#' * heading_level} {text}" if element_kind == "heading" else text
    return DocumentElement(
        element_id=element_id,
        element_kind=element_kind,
        body_state=body_state,
        heading_path=heading_path,
        page_start=page,
        page_end=page,
        text=text,
        markdown=markdown,
        heading_level=heading_level,
    )


def _document_model(elements: tuple[DocumentElement, ...]) -> DocumentModel:
    return DocumentModel(
        source_locator="generic.pdf",
        source_hash="a" * 64,
        extractor_name="test",
        extractor_version="test",
        elements=elements,
    )
