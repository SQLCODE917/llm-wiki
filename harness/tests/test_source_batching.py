from llmwiki.domain.model_profile import BASELINE_CONTEXT_TOKENS, ModelProfile
from llmwiki.domain.source_batching import source_block_batches
from llmwiki.pdf.document import DocumentElement, DocumentModel
from llmwiki.pdf.source_map_builder import build_normalized_source_map


def test_model_profile_scales_source_budget_by_context_window() -> None:
    small = ModelProfile("small", BASELINE_CONTEXT_TOKENS // 2)
    baseline = ModelProfile("baseline", BASELINE_CONTEXT_TOKENS)

    assert small.source_chunk_tokens < baseline.source_chunk_tokens
    assert small.source_chunk_tokens >= 512
    assert baseline.estimate_tokens("x" * 400) == 100


def test_source_block_batches_preserve_source_block_coverage() -> None:
    source_map = build_normalized_source_map(
        _model(
            (
                _element("h1", "heading", "Functions", "Functions", 1),
                _element("p1", "paragraph", "Functions", "alpha beta gamma delta", 1),
                _element("p2", "paragraph", "Functions", "epsilon zeta eta theta", 1),
                _element("c1", "code_block", "Functions", "const f = () => 1;", 2),
            )
        )
    )

    batches = source_block_batches(
        source_map,
        budget_tokens=4,
        model_profile=ModelProfile("test", BASELINE_CONTEXT_TOKENS, chars_per_token_estimate=6),
    )

    batched_ids = tuple(block_id for batch in batches for block_id in batch.source_block_ids)
    assert batched_ids == tuple(block.source_block_id for block in source_map.source_blocks)
    for batch in batches:
        assert batch.text == "\n\n".join(
            source_map.source_blocks_by_id[block_id].source_text
            for block_id in batch.source_block_ids
        )


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
