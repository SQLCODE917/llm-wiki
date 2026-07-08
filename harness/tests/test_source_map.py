import json

import pytest

from llmwiki.domain.source_map import (
    build_prompt_windows,
    normalized_source_map_from_json,
    normalized_source_map_to_json,
)
from llmwiki.pdf.document import DocumentElement, DocumentModel
from llmwiki.pdf.source_map_builder import build_normalized_source_map


def _element(
    element_id: str,
    element_kind: str,
    heading_path: str,
    text: str,
    page: int,
    *,
    markdown: str = "",
    body_state: str = "body",
    layout_y0: float = 0.0,
) -> DocumentElement:
    rendered = markdown or (f"# {text}" if element_kind == "heading" else text)
    return DocumentElement(
        element_id=element_id,
        element_kind=element_kind,
        body_state=body_state,
        heading_path=heading_path,
        page_start=page,
        page_end=page,
        text=text,
        markdown=rendered,
        layout_y0=layout_y0,
    )


def _model(elements: tuple[DocumentElement, ...]) -> DocumentModel:
    return DocumentModel(
        source_locator="book.pdf",
        source_hash="ab" * 32,
        extractor_name="docling",
        extractor_version="test",
        elements=elements,
    )


def _estimate_tokens(text: str) -> int:
    return len(text.split())


def test_source_map_builds_blocks_findings_and_roundtrips() -> None:
    model = _model(
        (
            _element("e1", "heading", "Shade", "Shade", 10),
            _element("e2", "paragraph", "Shade", "Shade creates magical darkness.", 10),
            _element("e3", "code_block", "Shade", "const shade = spell();", 10),
            _element("e4", "table", "Shade", "Name | Distance\nShade | 20 meters", 11),
            _element("e5", "paragraph", "Document", "Page footer", 11, body_state="furniture"),
            _element(
                "e6",
                "paragraph",
                "Contents",
                "Shade ........ 10",
                1,
                body_state="table_of_contents",
            ),
        )
    )

    source_map = build_normalized_source_map(model)
    roundtripped = normalized_source_map_from_json(normalized_source_map_to_json(source_map))

    assert roundtripped == source_map
    assert [block.block_type for block in source_map.source_blocks] == [
        "heading",
        "paragraph",
        "code",
        "table",
    ]
    assert all(block.source_anchor for block in source_map.source_blocks)
    assert all(block.page_span[0] > 0 for block in source_map.source_blocks)
    assert all(block.section_path == "Shade" for block in source_map.source_blocks)
    assert all(block.source_text for block in source_map.source_blocks)
    assert all(block.confidence > 0 for block in source_map.source_blocks)
    assert [block.source_order for block in source_map.source_blocks] == [1, 2, 3, 4]
    expected_findings = {
        "furniture-candidate",
        "table-of-contents",
        "code-block-candidate",
        "table-block-candidate",
    }
    assert expected_findings.issubset({finding.finding_code for finding in source_map.findings})


def test_source_map_json_rejects_numeric_strings_and_unknown_block_types() -> None:
    source_map = build_normalized_source_map(
        _model((_element("e1", "paragraph", "Shade", "Shade creates darkness.", 10),))
    )
    payload = json.loads(normalized_source_map_to_json(source_map))
    payload["source_blocks"][0]["page_span"][0] = "10"

    with pytest.raises(ValueError, match="page_span"):
        normalized_source_map_from_json(json.dumps(payload))

    payload = json.loads(normalized_source_map_to_json(source_map))
    payload["source_blocks"][0]["block_type"] = "mystery"

    with pytest.raises(ValueError, match="block_type"):
        normalized_source_map_from_json(json.dumps(payload))


def test_source_map_json_rejects_malformed_anchors() -> None:
    source_map = build_normalized_source_map(
        _model((_element("e1", "paragraph", "Shade", "Shade creates darkness.", 10),))
    )
    payload = json.loads(normalized_source_map_to_json(source_map))
    payload["source_blocks"][0]["source_anchor"] = "not-an-object"

    with pytest.raises(ValueError, match="source anchor"):
        normalized_source_map_from_json(json.dumps(payload))


def test_source_map_json_accepts_numeric_bounding_boxes() -> None:
    source_map = build_normalized_source_map(
        _model((_element("e1", "paragraph", "Shade", "Shade creates darkness.", 10),))
    )
    payload = json.loads(normalized_source_map_to_json(source_map))
    payload["source_blocks"][0]["source_anchor"]["bounding_boxes"] = [
        [1, 2.5, 3, 4.25]
    ]

    parsed = normalized_source_map_from_json(json.dumps(payload))

    assert parsed.source_blocks[0].source_anchor.bounding_boxes == (
        (1.0, 2.5, 3.0, 4.25),
    )


def test_source_block_ids_are_stable() -> None:
    model = _model(
        (
            _element("e1", "heading", "Object.assign", "Object.assign", 198),
            _element("e2", "paragraph", "Object.assign", "Objects copy properties.", 198),
        )
    )

    first = build_normalized_source_map(model)
    second = build_normalized_source_map(model)

    assert [block.source_block_id for block in first.source_blocks] == [
        block.source_block_id for block in second.source_blocks
    ]


def test_prompt_windows_use_only_listed_source_blocks_and_repeat_heading_context() -> None:
    source_map = build_normalized_source_map(
        _model(
            (
                _element("e1", "heading", "Functions", "Functions", 1),
                _element("e2", "paragraph", "Functions", "alpha beta gamma delta epsilon", 1),
                _element("e3", "paragraph", "Functions", "zeta eta theta iota kappa", 2),
            )
        )
    )

    windows = build_prompt_windows(source_map, budget_tokens=7, estimate_tokens=_estimate_tokens)
    blocks_by_id = source_map.source_blocks_by_id

    assert len(windows) == 2
    heading_id = source_map.source_blocks[0].source_block_id
    assert all(window.source_block_ids[0] == heading_id for window in windows)
    for window in windows:
        expected = "\n\n".join(
            blocks_by_id[block_id].source_text for block_id in window.source_block_ids
        )
        assert window.text == expected


def test_shade_source_block_has_stable_anchor_and_low_confidence_count() -> None:
    source_map = build_normalized_source_map(
        _model(
            (
                _element("e1", "heading", "Shade", "Shade", 58),
                _element(
                    "e2",
                    "paragraph",
                    "Shade",
                    "If a shade itself comes into contact with a will -o-wisp body.",
                    59,
                ),
            )
        )
    )

    shade_blocks = [
        block for block in source_map.source_blocks if "will -o-wisp" in block.source_text
    ]

    assert len(shade_blocks) == 1
    assert shade_blocks[0].source_anchor.source_locator == "book.pdf"
    assert shade_blocks[0].source_anchor.page_span == (59, 59)
    assert shade_blocks[0].source_anchor.text_fingerprint
    assert source_map.low_confidence_block_count == 1


def test_javascript_code_example_stays_code_block() -> None:
    source_map = build_normalized_source_map(
        _model(
            (
                _element("e1", "heading", "Closures", "Closures", 42),
                _element(
                    "e2",
                    "code_block",
                    "Closures",
                    "const counter = () => value;",
                    42,
                    markdown="```\nconst counter = () => value;\n```",
                ),
            )
        )
    )

    assert source_map.source_blocks[1].block_type == "code"
    assert "const counter" in source_map.source_blocks[1].source_text


def test_javascript_embedded_paragraph_code_is_recovered_as_code_block() -> None:
    source_map = build_normalized_source_map(
        _model(
            (
                _element("e1", "heading", "Map", "Map", 42),
                _element(
                    "e2",
                    "paragraph",
                    "Map",
                    (
                        "Use map when transforming values.\n\n"
                        "const doubled = values.map((value) => value * 2);\n"
                        "return doubled;\n\n"
                        "The result keeps the same order."
                    ),
                    42,
                ),
            )
        )
    )

    assert [block.block_type for block in source_map.source_blocks] == [
        "heading",
        "paragraph",
        "code",
        "paragraph",
    ]
    assert "values.map" in source_map.source_blocks[2].source_text
    assert source_map.source_blocks[2].source_anchor.element_path[-1] == "split-2"
