from llmwiki.pdf.document import (
    DocumentElement,
    DocumentModel,
    build_source_chunks,
    build_source_sections,
    document_model_from_json,
    document_model_to_json,
    source_sections_from_json,
    source_sections_to_json,
)


def _element(
    element_id: str,
    element_kind: str,
    heading_path: str,
    text: str,
    page: int,
    *,
    body_state: str = "body",
) -> DocumentElement:
    markdown = f"# {text}" if element_kind == "heading" else text
    return DocumentElement(
        element_id=element_id,
        element_kind=element_kind,
        body_state=body_state,
        heading_path=heading_path,
        page_start=page,
        page_end=page,
        text=text,
        markdown=markdown,
    )


def _model(elements: tuple[DocumentElement, ...]) -> DocumentModel:
    return DocumentModel(
        source_locator="javascriptallonge.pdf",
        source_hash="ab" * 32,
        extractor_name="docling",
        extractor_version="test",
        elements=elements,
    )


class TestSourceSections:
    def test_separates_object_assign_why_and_warm_cup(self) -> None:
        model = _model(
            (
                _element("e1", "heading", "Object.assign", "Object.assign", 198),
                _element(
                    "e2",
                    "paragraph",
                    "Object.assign",
                    "Object.assign copies own properties.",
                    198,
                ),
                _element("e3", "code_block", "Object.assign", "Object.assign(target, source)", 199),
                _element("e4", "heading", "Why?", "Why?", 201),
                _element(
                    "e5",
                    "paragraph",
                    "Why?",
                    "Why? evaluates a Y Combinator example.",
                    201,
                ),
                _element(
                    "e6",
                    "heading",
                    "A Warm Cup: Basic Strings and Quasi-Literals",
                    "A Warm Cup: Basic Strings and Quasi-Literals",
                    202,
                ),
                _element(
                    "e7",
                    "paragraph",
                    "A Warm Cup: Basic Strings and Quasi-Literals",
                    "Strings begin here.",
                    202,
                ),
            )
        )

        sections = build_source_sections(model)

        assert [section.heading_path for section in sections] == [
            "Object.assign",
            "Why?",
            "A Warm Cup: Basic Strings and Quasi-Literals",
        ]
        assert "Y Combinator" not in sections[0].text
        assert "Object.assign(target, source)" not in sections[1].text

    def test_excludes_table_of_contents_and_furniture(self) -> None:
        model = _model(
            (
                _element(
                    "e1",
                    "heading",
                    "Contents",
                    "Contents",
                    1,
                    body_state="table_of_contents",
                ),
                _element(
                    "e2",
                    "paragraph",
                    "Contents",
                    "Object.assign ........ 198",
                    1,
                    body_state="table_of_contents",
                ),
                _element("e3", "paragraph", "Document", "Page footer", 1, body_state="furniture"),
                _element("e4", "heading", "Object.assign", "Object.assign", 198),
                _element("e5", "paragraph", "Object.assign", "Real body text.", 198),
            )
        )

        sections = build_source_sections(model)

        assert len(sections) == 1
        assert sections[0].heading_path == "Object.assign"
        assert "Real body text" in sections[0].text
        assert "footer" not in sections[0].text
        assert "198" not in sections[0].text

    def test_sections_roundtrip(self) -> None:
        model = _model(
            (
                _element("e1", "heading", "Object.assign", "Object.assign", 198),
                _element("e2", "paragraph", "Object.assign", "Body.", 198),
            )
        )
        sections = build_source_sections(model)

        assert source_sections_from_json(source_sections_to_json(sections)) == sections
        assert document_model_from_json(document_model_to_json(model)) == model


class TestSourceChunks:
    def test_does_not_merge_adjacent_sections(self) -> None:
        model = _model(
            (
                _element("e1", "heading", "Object.assign", "Object.assign", 198),
                _element("e2", "paragraph", "Object.assign", "Small section.", 198),
                _element("e3", "heading", "Why?", "Why?", 201),
                _element("e4", "paragraph", "Why?", "Another small section.", 201),
            )
        )
        sections = build_source_sections(model)

        chunks = build_source_chunks(model, sections, budget_tokens=6000)

        assert len(chunks) == 2
        assert chunks[0].heading_path == "Object.assign"
        assert chunks[1].heading_path == "Why?"

    def test_splits_oversized_section_at_element_boundaries(self) -> None:
        model = _model(
            (
                _element("e1", "heading", "Chapter", "Chapter", 1),
                _element("e2", "paragraph", "Chapter", "alpha " * 80, 1),
                _element("e3", "paragraph", "Chapter", "beta " * 80, 2),
                _element("e4", "code_block", "Chapter", "const answer = 42;\n" * 30, 3),
            )
        )
        sections = build_source_sections(model)

        chunks = build_source_chunks(model, sections, budget_tokens=40)

        assert len(chunks) > 1
        assert all(chunk.heading_path == "Chapter" for chunk in chunks)
        assert "const answer = 42;" in chunks[-1].text
