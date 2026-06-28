from llmwiki.domain.ledger.atom_context import TechnicalAtomContext, atom_context_matches
from llmwiki.domain.ledger.common import ConfidenceBasis
from llmwiki.domain.ledger.topic_terms import topic_matcher


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
