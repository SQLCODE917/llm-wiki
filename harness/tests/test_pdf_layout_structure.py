from llmwiki.pdf.document import DocumentElement, DocumentModel
from llmwiki.pdf.layout_structure import compile_layout_structure


def _heading(element_id: str, text: str, size: float, y: float, page: int = 1) -> DocumentElement:
    return DocumentElement(
        element_id=element_id,
        element_kind="heading",
        body_state="body",
        heading_path=text,
        page_start=page,
        page_end=page,
        text=text,
        markdown=f"# {text}",
        heading_level=1,
        layout_font_size=size,
        layout_y0=y,
    )


def _paragraph(element_id: str, text: str, page: int = 1) -> DocumentElement:
    return DocumentElement(
        element_id=element_id,
        element_kind="paragraph",
        body_state="body",
        heading_path="Document",
        page_start=page,
        page_end=page,
        text=text,
        markdown=text,
        layout_font_size=9.0,
        layout_y0=200.0,
    )


def _model(*elements: DocumentElement) -> DocumentModel:
    return DocumentModel(
        source_locator="synthetic.pdf",
        source_hash="a" * 64,
        extractor_name="test",
        extractor_version="test",
        elements=elements,
    )


def test_layout_font_tiers_create_parent_child_paths_without_source_terms() -> None:
    model = _model(
        _heading("h1", "Primary Module", 18.0, 10.0),
        _paragraph("p1", "Primary body."),
        _heading("h2", "Secondary Operation", 14.0, 40.0),
        _paragraph("p2", "Secondary body."),
        _heading("h3", "Tertiary Case", 11.0, 70.0),
        _paragraph("p3", "Tertiary body."),
        _heading("h4", "Next Secondary Operation", 14.0, 100.0),
    )

    compiled = compile_layout_structure(model, body_font_size=9.0)
    headings = [element for element in compiled.elements if element.element_kind == "heading"]

    assert [(heading.text, heading.heading_level) for heading in headings] == [
        ("Primary Module", 1),
        ("Secondary Operation", 2),
        ("Tertiary Case", 3),
        ("Next Secondary Operation", 2),
    ]
    assert compiled.elements[3].heading_path == "Primary Module > Secondary Operation"
    assert headings[2].heading_path == ("Primary Module > Secondary Operation > Tertiary Case")
    assert headings[3].heading_path == "Primary Module > Next Secondary Operation"


def test_layout_structure_demotes_nearby_duplicate_heading_fragments() -> None:
    model = _model(
        _heading("h1", "Chapter 7 - Alpha Beta Gamma", 18.0, 50.0),
        _heading("h2", "Beta", 18.0, 70.0),
        _paragraph("p1", "Body remains under the full heading."),
    )

    compiled = compile_layout_structure(model, body_font_size=9.0)

    assert compiled.elements[0].element_kind == "heading"
    assert compiled.elements[1].element_kind == "paragraph"
    assert compiled.elements[1].heading_path == "Chapter 7 - Alpha Beta Gamma"
    assert compiled.elements[2].heading_path == "Chapter 7 - Alpha Beta Gamma"
