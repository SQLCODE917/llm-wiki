from llmwiki.domain.source_records import build_source_record_plan
from llmwiki.domain.source_structure_integrity import (
    build_source_structure_integrity_report,
)
from llmwiki.pdf.document import DocumentElement, DocumentModel
from llmwiki.pdf.source_map_builder import build_normalized_source_map


def test_source_structure_demotes_record_shaped_section_labels() -> None:
    source_map = build_normalized_source_map(
        _model(
            (
                _element(
                    "h1",
                    "heading",
                    "[ Luma ] Rate=2 Cost=4 Range=near",
                    "[ Luma ] Rate=2 Cost=4 Range=near",
                    10,
                ),
                _element(
                    "p1",
                    "paragraph",
                    "[ Luma ] Rate=2 Cost=4 Range=near",
                    "Effect text.",
                    10,
                ),
            )
        )
    )

    report = build_source_structure_integrity_report(source_map)

    assert not report.section_can_drive_pages("[ Luma ] Rate=2 Cost=4 Range=near")
    assert report.findings[0].finding_code == "source-section-cannot-drive-pages"
    assert "field-dense" in report.findings[0].message


def test_source_record_plan_detects_repeated_field_dense_records() -> None:
    source_map = build_normalized_source_map(
        _model(
            (
                _element("h1", "heading", "Poisons", "Poisons", 12),
                _element(
                    "p1",
                    "paragraph",
                    "Poisons",
                    "Ale Dose=drink Damage=2d6 Type=poison",
                    12,
                ),
                _element(
                    "p2",
                    "paragraph",
                    "Poisons",
                    "Bad Joke Dose=inhaled Damage=1d6 Type=poison",
                    12,
                ),
            )
        )
    )

    plan = build_source_record_plan(source_map)

    assert plan.record_count == 2
    assert [record.label for record in plan.records] == ["Ale Dose", "Bad Joke Dose"]
    assert all(record.field_names for record in plan.records)
    assert set(plan.source_record_block_ids).issubset(source_map.source_blocks_by_id)


def _element(
    element_id: str,
    element_kind: str,
    heading_path: str,
    text: str,
    page: int,
) -> DocumentElement:
    return DocumentElement(
        element_id=element_id,
        element_kind=element_kind,
        body_state="body",
        heading_path=heading_path,
        page_start=page,
        page_end=page,
        text=text,
        markdown=f"# {text}" if element_kind == "heading" else text,
    )


def _model(elements: tuple[DocumentElement, ...]) -> DocumentModel:
    return DocumentModel(
        source_locator="book.pdf",
        source_hash="ab" * 32,
        extractor_name="docling",
        extractor_version="test",
        elements=elements,
    )
