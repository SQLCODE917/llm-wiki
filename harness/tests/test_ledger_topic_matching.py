from llmwiki.domain.ledger.atom_context import TechnicalAtomContext, atom_context_matches
from llmwiki.domain.ledger.common import ConfidenceBasis
from llmwiki.domain.ledger.topic_terms import matching_topic_terms, topic_matcher


def test_atom_context_matching_requires_compound_topic_coverage() -> None:
    matcher = topic_matcher(("skeleton", "warrior"))
    assert matcher is not None

    assert atom_context_matches(
        (
            _context(
                "A skeleton warrior is a golem created from a dragon's tooth.",
                ("skeleton", "warrior", "golem"),
            ),
        ),
        matcher,
        ("skeleton", "warrior"),
    )
    assert not atom_context_matches(
        (_context("If the caster sacrifices their own life, apply a curse.", ("caster", "curse")),),
        matcher,
        ("skeleton", "warrior"),
    )


def test_matching_topic_terms_is_bounded_and_lexical() -> None:
    terms = tuple(f"topic{i}x" for i in range(100))

    matches = matching_topic_terms("topic1x topic2x topic99x", terms)

    assert matches == ("topic1x", "topic2x")


def _context(text: str, terms: tuple[str, ...]) -> TechnicalAtomContext:
    return TechnicalAtomContext(
        technical_atom_context_id="context",
        technical_atom_id="atom",
        context_role="explained-by-source-prose",
        context_text=text,
        context_entry_ids=(),
        context_source_range_ids=("range",),
        demonstrated_concept_keys=terms,
        evidence_ids=("range",),
        confidence_basis=ConfidenceBasis("test"),
    )
