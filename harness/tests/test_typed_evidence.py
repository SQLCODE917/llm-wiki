import json

import pytest

from llmwiki.domain.objects import RawSource
from llmwiki.domain.source_profile_selector import select_source_profile
from llmwiki.domain.source_profiles import build_evidence_extraction_plan
from llmwiki.domain.typed_evidence import (
    StructuredEvidencePayload,
    TypedEvidenceRecord,
    stable_id,
    validate_typed_evidence_record,
)
from llmwiki.domain.typed_evidence_io import (
    evidence_record_set_from_json,
    evidence_record_set_to_json,
)
from llmwiki.domain.typed_evidence_producer import DeterministicTypedEvidenceProducer
from llmwiki.pdf.document import DocumentElement, DocumentModel
from llmwiki.pdf.source_map_builder import build_normalized_source_map
from llmwiki.runtime.typed_evidence_source_claims import source_claims_from_typed_evidence


def _element(
    element_id: str,
    element_kind: str,
    heading_path: str,
    text: str,
    page: int,
    *,
    markdown: str = "",
) -> DocumentElement:
    return DocumentElement(
        element_id=element_id,
        element_kind=element_kind,
        body_state="body",
        heading_path=heading_path,
        page_start=page,
        page_end=page,
        text=text,
        markdown=markdown or (f"# {text}" if element_kind == "heading" else text),
    )


def _source_map(source_locator: str, elements: tuple[DocumentElement, ...]):
    return build_normalized_source_map(
        DocumentModel(
            source_locator=source_locator,
            source_hash="cd" * 32,
            extractor_name="docling",
            extractor_version="test",
            elements=elements,
        )
    )


def _artifact_and_plan(source_map):
    artifact = select_source_profile(source_map)
    return artifact, build_evidence_extraction_plan(
        source_map,
        artifact.source_profile,
        artifact.evidence_vocabulary,
    )


def _record(source_map, record_type: str, text: str, *, confidence: float = 1.0):
    anchor = source_map.source_blocks[0].source_anchor
    return TypedEvidenceRecord(
        typed_evidence_record_id=stable_id("typed-evidence-record", text),
        source_id=source_map.source_id,
        source_locator=source_map.source_locator,
        source_hash=source_map.source_hash,
        evidence_record_type=record_type,
        status="accepted",
        canonical_text=text,
        structured_payload=StructuredEvidencePayload("text", text),
        source_anchors=(anchor,),
        source_block_ids=(source_map.source_blocks[0].source_block_id,),
        confidence=confidence,
    )


def test_validator_rejects_disallowed_and_missing_anchor_records() -> None:
    source_map = _source_map(
        "Sword World RPG - Complete Edition.pdf",
        (
            _element("e1", "paragraph", "Shade", "A shade must follow magic rules.", 68),
        ),
    )
    _, plan = _artifact_and_plan(source_map)
    missing_anchor = TypedEvidenceRecord(
        typed_evidence_record_id="typed-evidence-record-missing-anchor",
        source_id=source_map.source_id,
        source_locator=source_map.source_locator,
        source_hash=source_map.source_hash,
        evidence_record_type="rule",
        status="accepted",
        canonical_text="A shade must follow magic rules.",
        structured_payload=StructuredEvidencePayload("text", "A shade must follow magic rules."),
        source_anchors=(),
        source_block_ids=(source_map.source_blocks[0].source_block_id,),
        confidence=1.0,
    )
    disallowed = _record(source_map, "code_example", "Code example: const x = 1;")

    assert validate_typed_evidence_record(missing_anchor, plan).status == "rejected"
    rejected = validate_typed_evidence_record(disallowed, plan)
    assert rejected.status == "rejected"
    assert rejected.findings[0].finding_code == "disallowed-evidence-record-type"


def test_validator_classifies_fragmentary_rejected_and_needs_review_records() -> None:
    source_map = _source_map(
        "Sword World RPG - Complete Edition.pdf",
        (
            _element("e1", "paragraph", "Shade", "A shade must follow magic rules.", 68),
        ),
    )
    _, plan = _artifact_and_plan(source_map)

    fragment = validate_typed_evidence_record(
        _record(source_map, "rule", "The shade is also very fragile and will easily."),
        plan,
    )
    jammed = validate_typed_evidence_record(
        _record(
            source_map,
            "rule",
            "Furthermore if an opponent destroys a will also suffer the same damage.",
        ),
        plan,
    )
    clipped = validate_typed_evidence_record(
        _record(
            source_map,
            "rule",
            "If a shade itself comes into will -o-wisp's body or enters the area.",
        ),
        plan,
    )
    weak = validate_typed_evidence_record(
        _record(source_map, "rule", "A shade must follow magic rules.", confidence=0.4),
        plan,
    )

    assert fragment.status == "fragmentary"
    assert jammed.status == "rejected"
    assert clipped.status == "rejected"
    assert weak.status == "needs_review"


def test_sword_world_producer_emits_rules_and_procedure_steps() -> None:
    source_map = _source_map(
        "Sword World RPG - Complete Edition.pdf",
        (
            _element("e1", "heading", "Character Creation", "Character Creation", 12),
            _element(
                "e2",
                "paragraph",
                "Character Creation",
                "A player must choose race, skills, magic, damage values, and dice.",
                12,
            ),
            _element(
                "e3",
                "list_item",
                "Character Creation",
                "1. Choose a race.\n2. Choose a class.",
                12,
            ),
        ),
    )
    artifact, plan = _artifact_and_plan(source_map)

    record_set = DeterministicTypedEvidenceProducer().build_record_set(source_map, artifact, plan)

    accepted_types = {record.evidence_record_type for record in record_set.accepted_records}
    assert {"rule", "procedure_step"}.issubset(accepted_types)
    assert all(record.source_anchors for record in record_set.records)


def test_javascript_producer_emits_code_examples_and_arguments() -> None:
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
            _element(
                "e3",
                "paragraph",
                "Closures",
                "JavaScript can pass functions around to build closures.",
                43,
            ),
        ),
    )
    artifact, plan = _artifact_and_plan(source_map)

    record_set = DeterministicTypedEvidenceProducer().build_record_set(source_map, artifact, plan)

    accepted_types = {record.evidence_record_type for record in record_set.accepted_records}
    assert {"code_example", "argument"}.issubset(accepted_types)
    assert "const counter" in record_set.accepted_records[0].support_text


def test_javascript_producer_emits_code_example_from_recovered_paragraph_code() -> None:
    source_map = _source_map(
        "javascriptallonge.pdf",
        (
            _element("e1", "heading", "Mapping", "Mapping", 42),
            _element(
                "e2",
                "paragraph",
                "Mapping",
                (
                    "Map transforms values.\n\n"
                    "const doubled = values.map((value) => value * 2);\n"
                    "return doubled;"
                ),
                42,
            ),
        ),
    )
    artifact, plan = _artifact_and_plan(source_map)

    record_set = DeterministicTypedEvidenceProducer().build_record_set(source_map, artifact, plan)

    code_records = [
        record
        for record in record_set.accepted_records
        if record.evidence_record_type == "code_example"
    ]
    assert len(code_records) == 1
    assert "values.map" in code_records[0].payload_text


def test_structured_payload_round_trips_and_preserves_table_text() -> None:
    source_map = _source_map(
        "reference.pdf",
        (
            _element("e1", "heading", "Spell Table", "Spell Table", 59),
            _element("e2", "table", "Spell Table", "Name | Value\nDistance=20 meters | 5", 59),
        ),
    )
    artifact, plan = _artifact_and_plan(source_map)
    record_set = DeterministicTypedEvidenceProducer().build_record_set(source_map, artifact, plan)

    restored = evidence_record_set_from_json(evidence_record_set_to_json(record_set))

    assert restored == record_set
    assert "Distance=20 meters" in restored.accepted_records[0].payload_text


def test_evidence_record_set_json_rejects_unknown_status_and_wrong_types() -> None:
    source_map = _source_map(
        "reference.pdf",
        (
            _element("e1", "heading", "Spell Table", "Spell Table", 59),
            _element("e2", "table", "Spell Table", "Name | Value\nDistance=20 meters | 5", 59),
        ),
    )
    artifact, plan = _artifact_and_plan(source_map)
    record_set = DeterministicTypedEvidenceProducer().build_record_set(source_map, artifact, plan)
    payload = json.loads(evidence_record_set_to_json(record_set))
    payload["records"][0]["status"] = "maybe"

    with pytest.raises(ValueError, match="status"):
        evidence_record_set_from_json(json.dumps(payload))

    payload = json.loads(evidence_record_set_to_json(record_set))
    payload["records"][0]["confidence"] = "1.0"

    with pytest.raises(ValueError, match="confidence"):
        evidence_record_set_from_json(json.dumps(payload))


def test_evidence_record_set_json_rejects_wrong_nested_payload_shape() -> None:
    source_map = _source_map(
        "reference.pdf",
        (
            _element("e1", "heading", "Spell Table", "Spell Table", 59),
            _element("e2", "table", "Spell Table", "Name | Value\nDistance=20 meters | 5", 59),
        ),
    )
    artifact, plan = _artifact_and_plan(source_map)
    record_set = DeterministicTypedEvidenceProducer().build_record_set(source_map, artifact, plan)
    payload = json.loads(evidence_record_set_to_json(record_set))
    payload["records"][0]["structured_payload"]["normalized_fields"] = {"Distance": "20 meters"}

    with pytest.raises(ValueError, match="normalized_fields"):
        evidence_record_set_from_json(json.dumps(payload))


def test_modality_gate_emits_formula_from_formula_like_prose() -> None:
    source_map = _source_map(
        "reference.pdf",
        (
            _element("e1", "heading", "Damage", "Damage", 44),
            _element("e2", "paragraph", "Damage", "Final Damage = Power + Bonus", 44),
            _element("e3", "table", "Damage", "Name | Value\nDamage | 2d6", 44),
        ),
    )
    artifact, plan = _artifact_and_plan(source_map)

    record_set = DeterministicTypedEvidenceProducer().build_record_set(source_map, artifact, plan)

    assert any(record.evidence_record_type == "formula" for record in record_set.records)


def test_trust_gate_blocks_contaminated_code_payloads_from_accepted_support() -> None:
    source_map = _source_map(
        "javascriptallonge.pdf",
        (
            _element("e1", "heading", "Examples", "Examples", 44),
            _element(
                "e2",
                "code_block",
                "Examples",
                "const x = 1;\nThis sentence is prose inside code and should be reviewed.",
                44,
            ),
        ),
    )
    artifact, plan = _artifact_and_plan(source_map)

    record_set = DeterministicTypedEvidenceProducer().build_record_set(source_map, artifact, plan)

    assert record_set.records[0].status == "needs_review"
    assert record_set.records[0].findings[-1].finding_code == "typed-evidence-trust"
    assert not record_set.accepted_records


def test_page_planning_adapter_uses_only_accepted_typed_records() -> None:
    source_map = _source_map(
        "Sword World RPG - Complete Edition.pdf",
        (
            _element("e1", "heading", "Shade", "Shade", 68),
            _element("e2", "paragraph", "Shade", "A shade must follow magic rules.", 68),
            _element(
                "e3",
                "paragraph",
                "Shade",
                "The shade is also very fragile and will easily.",
                68,
            ),
        ),
    )
    artifact, plan = _artifact_and_plan(source_map)
    record_set = DeterministicTypedEvidenceProducer().build_record_set(source_map, artifact, plan)

    source_claims = source_claims_from_typed_evidence(
        raw_source=RawSource.from_locator(source_map.source_locator),
        source_map=source_map,
        record_set=record_set,
    )

    assert record_set.status_counts["fragmentary"] == 1
    assert [claim.statement for claim in source_claims] == ["A shade must follow magic rules."]
