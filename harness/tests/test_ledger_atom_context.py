from llmwiki.domain.ledger.atom_context import build_technical_atom_contexts
from llmwiki.domain.ledger.atoms import FormulaPayload, TechnicalAtom
from llmwiki.domain.ledger.segments import SourceSegment


def test_atom_context_uses_source_range_ids_instead_of_segment_equality() -> None:
    intro = SourceSegment(
        segment_id="segment-intro",
        source_range_id="range-intro",
        source_locator="rules.md",
        source_hash="source-hash",
        heading_path="Rules",
        structure_node_id="node-rules",
        source_order=1,
        text="For example, " + ("large context text " * 10_000),
        segment_kind="paragraph",
        evidence_ids=("evidence-intro",),
    )
    atom_segment = SourceSegment(
        segment_id="segment-formula",
        source_range_id="range-formula",
        source_locator="rules.md",
        source_hash="source-hash",
        heading_path="Rules",
        structure_node_id="node-rules",
        source_order=2,
        text="x = y + z",
        segment_kind="paragraph",
        evidence_ids=("evidence-formula",),
    )
    atom = TechnicalAtom(
        technical_atom_id="atom-formula",
        technical_atom_kind="formula",
        payload=FormulaPayload(
            raw_formula_text="x = y + z",
            formula_subtype="symbolic-formula",
            formula_surface_form="equation",
            source_locator="rules.md",
        ),
        source_locator="rules.md",
        source_range_id="range-formula",
        evidence_ids=("evidence-formula",),
    )

    contexts = build_technical_atom_contexts(
        source_hash="source-hash",
        segments=(intro, atom_segment),
        entries=(),
        atoms=(atom,),
    )

    assert contexts[0].technical_atom_id == "atom-formula"
    assert contexts[0].context_source_range_ids == ("range-intro",)
