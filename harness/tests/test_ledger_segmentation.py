from llmwiki.domain.objects import Schema
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
