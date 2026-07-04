from llmwiki.domain.source_profile_io import (
    evidence_extraction_plan_from_json,
    evidence_extraction_plan_to_json,
    source_profile_artifact_from_json,
    source_profile_artifact_to_json,
)
from llmwiki.domain.source_profile_selector import select_source_profile
from llmwiki.domain.source_profiles import (
    build_evidence_extraction_plan,
    default_evidence_vocabularies,
    validate_evidence_record_types,
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
) -> DocumentElement:
    rendered = markdown or (f"# {text}" if element_kind == "heading" else text)
    return DocumentElement(
        element_id=element_id,
        element_kind=element_kind,
        body_state="body",
        heading_path=heading_path,
        page_start=page,
        page_end=page,
        text=text,
        markdown=rendered,
    )


def _source_map(source_locator: str, elements: tuple[DocumentElement, ...]):
    return build_normalized_source_map(
        DocumentModel(
            source_locator=source_locator,
            source_hash="ab" * 32,
            extractor_name="docling",
            extractor_version="test",
            elements=elements,
        )
    )


def test_sword_world_source_selects_rpg_rules_vocabulary() -> None:
    source_map = _source_map(
        "Sword World RPG - Complete Edition.pdf",
        (
            _element("e1", "heading", "Character Creation", "Character Creation", 12),
            _element(
                "e2",
                "paragraph",
                "Character Creation",
                "A player must choose a character race, skills, magic, damage values, and dice.",
                12,
            ),
            _element("e3", "table", "Character Creation", "Skill | Bonus\nFighter | +1", 13),
        ),
    )

    artifact = select_source_profile(source_map)

    assert artifact.source_profile.profile_id == "rpg-rules"
    assert artifact.source_profile.confidence >= 0.8
    assert "normalized source map signals" in artifact.source_profile.selection_reason
    assert "rpg rules terms" in artifact.source_profile.matched_signals
    assert {"rule", "procedure_step"}.issubset(artifact.evidence_vocabulary.allowed_record_types)


def test_javascript_allonge_source_selects_programming_vocabulary() -> None:
    source_map = _source_map(
        "javascriptallonge.pdf",
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
            _element("e3", "paragraph", "Closures", "A function closes over an object.", 43),
        ),
    )

    artifact = select_source_profile(source_map)

    assert artifact.source_profile.profile_id == "programming-prose"
    assert {"code_example", "argument"}.issubset(artifact.evidence_vocabulary.allowed_record_types)
    assert any("code block count" in signal for signal in artifact.source_profile.matched_signals)


def test_reference_table_source_selects_reference_vocabulary() -> None:
    source_map = _source_map(
        "reference.pdf",
        (
            _element("e1", "heading", "Equipment Tables", "Equipment Tables", 4),
            _element("e2", "table", "Equipment Tables", "Name | Cost\nLantern | 5", 4),
        ),
    )

    artifact = select_source_profile(source_map)

    assert artifact.source_profile.profile_id == "reference"
    assert "table_fact" in artifact.evidence_vocabulary.allowed_record_types


def test_ambiguous_prose_source_uses_low_confidence_general_profile() -> None:
    source_map = _source_map(
        "essay.pdf",
        (
            _element("e1", "heading", "Notes", "Notes", 1),
            _element("e2", "paragraph", "Notes", "This passage reflects on ordinary reading.", 1),
        ),
    )

    artifact = select_source_profile(source_map)

    assert artifact.source_profile.profile_id == "general-prose"
    assert artifact.source_profile.confidence < 0.5
    assert artifact.findings[0].finding_code == "low-confidence-source-profile"


def test_vocabularies_do_not_publish_generic_claim_type() -> None:
    for vocabulary in default_evidence_vocabularies().values():
        assert "claim" not in vocabulary.allowed_record_types
        assert len(vocabulary.allowed_record_types) > 1


def test_evidence_extraction_plan_and_json_roundtrip() -> None:
    source_map = _source_map(
        "javascriptallonge.pdf",
        (
            _element("e1", "heading", "Functions", "Functions", 10),
            _element("e2", "code_block", "Functions", "function id(x) { return x; }", 10),
        ),
    )
    artifact = select_source_profile(source_map)
    plan = build_evidence_extraction_plan(
        source_map,
        artifact.source_profile,
        artifact.evidence_vocabulary,
    )

    assert plan.source_block_ids == tuple(
        block.source_block_id for block in source_map.source_blocks
    )
    assert plan.allowed_record_types == artifact.evidence_vocabulary.allowed_record_types
    assert evidence_extraction_plan_from_json(evidence_extraction_plan_to_json(plan)) == plan
    assert source_profile_artifact_from_json(source_profile_artifact_to_json(artifact)) == artifact


def test_unknown_or_disallowed_record_types_are_blocking_findings() -> None:
    source_map = _source_map(
        "Sword World RPG - Complete Edition.pdf",
        (
            _element("e1", "heading", "Spells", "Spells", 20),
            _element(
                "e2",
                "paragraph",
                "Spells",
                "A spell must define magic range and damage.",
                20,
            ),
        ),
    )
    artifact = select_source_profile(source_map)
    plan = build_evidence_extraction_plan(
        source_map,
        artifact.source_profile,
        artifact.evidence_vocabulary,
    )

    findings = validate_evidence_record_types(plan, ("rule", "spell_flavor", "code_example"))

    assert [finding.severity for finding in findings] == ["blocker", "blocker"]
    assert [finding.finding_code for finding in findings] == [
        "unknown-evidence-record-type",
        "disallowed-evidence-record-type",
    ]
