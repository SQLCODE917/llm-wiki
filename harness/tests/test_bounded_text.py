from llmwiki.domain.bounded_text import sentence_fragments
from llmwiki.domain.prose_flow import should_merge_prose
from llmwiki.domain.source_claim_sentences import claim_sentences


def test_sentence_fragments_handles_terminal_punctuation() -> None:
    assert tuple(sentence_fragments("Roll 2D. Add the modifier. Compare the target")) == (
        "Roll 2D.",
        " Add the modifier.",
        " Compare the target",
    )


def test_sentence_fragments_handles_one_character_sentence() -> None:
    assert tuple(sentence_fragments("A. B")) == ("A.", " B")


def test_claim_sentences_materializes_bounded_fragments() -> None:
    claims = claim_sentences(
        "Roll dice before combat. Add final modifier to result. " + "long procedure text " * 2000
    )

    assert claims[:2] == ("Roll dice before combat.", "Add final modifier to result.")
    assert len(claims) <= 120
    assert all(len(claim) <= 1800 for claim in claims)


def test_claim_sentences_repairs_layout_split_continuations() -> None:
    claims = claim_sentences(
        "If left untreated, they must make another death check after 1 hour, and\n\n"
        "again, will only die on double ones. If successful, they awaken."
    )

    first = " ".join(
        (
            "If left untreated, they must make another death check after 1 hour, and",
            "again, will only die on double ones.",
        )
    )
    assert claims[:2] == (
        first,
        "If successful, they awaken.",
    )


def test_prose_merge_delimiter_scan_is_bounded_for_large_fragments() -> None:
    left = "(" + ("very long extracted table prose " * 10_000) + ","

    assert should_merge_prose(left, "continued text", max_chars=None)
