from llmwiki.domain.ledger.builder import build_claim_ledger, default_schema_bundle
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
