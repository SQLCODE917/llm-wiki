from llmwiki.domain.bounded_text import sentence_fragments
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
        "Roll dice before combat. Add final modifier to result. "
        + "long procedure text " * 2000
    )

    assert claims[:2] == ("Roll dice before combat.", "Add final modifier to result.")
    assert len(claims) <= 120
    assert all(len(claim) <= 1800 for claim in claims)
