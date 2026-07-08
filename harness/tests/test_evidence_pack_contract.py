from llmwiki.domain.ledger.canonical import canonical_json
from llmwiki.domain.ledger.evidence_pack import (
    SupportRef,
    build_evidence_pack_set,
    validate_support_refs,
)
from llmwiki.domain.ledger.evidence_pack_synthesis_adapter import (
    apply_evidence_pack_to_synthesis_plan,
)
from llmwiki.domain.ledger.page_publication import PageCandidate, PagePublicationPlan
from llmwiki.domain.ledger.page_synthesis import (
    PageEvidenceSet,
    PageOutlineSection,
    PageSynthesisPlan,
)
from llmwiki.domain.source_map import NormalizedSourceMap, SourceAnchor, SourceBlock
from llmwiki.domain.typed_evidence import (
    EvidenceRecordSet,
    StructuredEvidencePayload,
    TypedEvidenceRecord,
)

_HASH = "c" * 64


def test_builds_evidence_pack_for_accepted_page_candidate() -> None:
    pack_set = build_evidence_pack_set(
        publication_plan=_plan(_candidate("shade", ("record-shade",))),
        evidence_record_set=_record_set(_record("record-shade", "rule", "Shade creates darkness.")),
        source_map=_source_map(_block("block-shade", "Shade creates a region of darkness.")),
    )

    assert pack_set.valid_page_ids == ("shade",)
    pack = pack_set.packs[0]
    assert pack.items[0].support_ref.code == "typed-evidence-record:record-shade"
    assert pack.items[0].source_text == "Shade creates a region of darkness."
    assert pack.coverage[0].page_family == "topic-concept"
    assert pack.coverage[0].coverage_status == "covered"


def test_rejects_pack_item_without_source_text_or_payload_text() -> None:
    pack_set = build_evidence_pack_set(
        publication_plan=_plan(_candidate("shade", ("record-shade",))),
        evidence_record_set=_record_set(
            _record("record-shade", "rule", "Shade creates darkness.", block_ids=("missing",))
        ),
        source_map=_source_map(),
    )

    assert pack_set.packs == ()
    assert {finding.finding_code for finding in pack_set.findings} == {
        "missing-support-text",
        "no-valid-evidence-pack-items",
    }


def test_evidence_pack_json_contains_no_summary_field() -> None:
    pack_set = build_evidence_pack_set(
        publication_plan=_plan(_candidate("shade", ("record-shade",))),
        evidence_record_set=_record_set(_record("record-shade", "rule", "Shade creates darkness.")),
        source_map=_source_map(_block("block-shade", "Shade creates a region of darkness.")),
    )

    assert '"summary"' not in canonical_json(pack_set, indent=2)


def test_rejects_article_support_refs_outside_evidence_pack() -> None:
    pack_set = build_evidence_pack_set(
        publication_plan=_plan(_candidate("shade", ("record-shade",))),
        evidence_record_set=_record_set(_record("record-shade", "rule", "Shade creates darkness.")),
        source_map=_source_map(_block("block-shade", "Shade creates a region of darkness.")),
    )

    findings = validate_support_refs(
        pack_set.packs[0],
        (SupportRef("typed-evidence-record", "record-other"),),
    )

    assert findings[0].finding_code == "unknown-support-ref"


def test_rejected_or_needs_review_records_do_not_become_pack_support() -> None:
    pack_set = build_evidence_pack_set(
        publication_plan=_plan(_candidate("shade", ("fragment", "rejected", "review"))),
        evidence_record_set=_record_set(
            _record("fragment", "rule", "Shade is fragile.", status="fragmentary"),
            _record("rejected", "rule", "Shade creates darkness.", status="rejected"),
            _record("review", "rule", "Shade has weak support.", status="needs_review"),
        ),
        source_map=_source_map(_block("block-shade", "Shade creates a region of darkness.")),
    )

    assert pack_set.packs == ()
    assert "typed-evidence-not-accepted" in {
        finding.finding_code for finding in pack_set.findings
    }


def test_accepted_candidate_without_source_map_has_no_valid_pack_page_id() -> None:
    pack_set = build_evidence_pack_set(
        publication_plan=_plan(_candidate("shade", ("record-shade",))),
        evidence_record_set=_record_set(_record("record-shade", "rule", "Shade creates darkness.")),
        source_map=None,
    )

    assert pack_set.valid_page_ids == ()
    assert pack_set.missing_pack_count == 1
    assert pack_set.findings[0].finding_code == "source-map-missing"


def test_sword_world_shade_pack_uses_full_source_block() -> None:
    full_text = (
        "Shade is a dark spirit. Its magic creates darkness in an area, and the "
        "darkness changes how will-o-wisp light interacts with the spell."
    )
    pack_set = build_evidence_pack_set(
        publication_plan=_plan(_candidate("shade", ("record-shade",))),
        evidence_record_set=_record_set(_record("record-shade", "rule", "Shade creates darkness.")),
        source_map=_source_map(_block("block-shade", full_text)),
    )

    assert full_text in pack_set.packs[0].items[0].source_text


def test_javascript_pack_preserves_full_code_example_payload() -> None:
    code = "const twice = (x) => x * 2;\n[1, 2, 3].map(twice);"
    pack_set = build_evidence_pack_set(
        publication_plan=_plan(_candidate("map", ("record-code",))),
        evidence_record_set=_record_set(
            _record("record-code", "code_example", "Map code example.", payload=code)
        ),
        source_map=_source_map(_block("block-shade", f"```js\n{code}\n```")),
    )

    assert pack_set.packs[0].items[0].payload_text == code
    assert code in pack_set.packs[0].items[0].source_text


def test_structured_payload_text_is_available_for_diagnostics() -> None:
    pack_set = build_evidence_pack_set(
        publication_plan=_plan(_candidate("shade", ("record-spell",))),
        evidence_record_set=_record_set(
            _record("record-spell", "formula", "Shade distance.", payload="Distance=20 meters")
        ),
        source_map=_source_map(_block("block-shade", "The spell distance is 20 meters.")),
    )

    assert pack_set.packs[0].items[0].payload_text == "Distance=20 meters"


def test_oversized_pack_is_shaped_and_records_trim_finding() -> None:
    records = tuple(
        _record(
            f"record-{index}",
            "definition",
            f"Definition {index}.",
            block_ids=(f"block-{index}",),
        )
        for index in range(20)
    )
    pack_set = build_evidence_pack_set(
        publication_plan=_plan(
            _candidate(
                "topic", tuple(record.typed_evidence_record_id for record in records)
            )
        ),
        evidence_record_set=_record_set(*records),
        source_map=_source_map(
            *(
                _block(f"block-{index}", f"Definition {index}.")
                for index in range(20)
            )
        ),
    )

    assert len(pack_set.packs[0].items) == 3
    assert "evidence-pack-trimmed" in {
        finding.finding_code for finding in pack_set.findings
    }


def test_recipe_pack_contains_code_and_explanatory_context() -> None:
    pack_set = build_evidence_pack_set(
        publication_plan=_plan(
            _candidate("map", ("code", "argument", "definition"), family="recipe-pattern")
        ),
        evidence_record_set=_record_set(
            _record(
                "code",
                "code_example",
                "Code example.",
                payload="values.map(fn)",
                block_ids=("block-code",),
            ),
            _record(
                "argument",
                "argument",
                "Map transforms each value.",
                block_ids=("block-argument",),
            ),
            _record(
                "definition",
                "definition",
                "Map returns a new collection.",
                block_ids=("block-definition",),
            ),
        ),
        source_map=_source_map(
            _block("block-code", "values.map(fn)"),
            _block("block-argument", "Map transforms each value."),
            _block("block-definition", "Map returns a new collection."),
        ),
    )

    assert [item.evidence_record_type for item in pack_set.packs[0].items] == [
        "code_example",
        "argument",
        "definition",
    ]
    assert pack_set.packs[0].items[0].support_ref.code == "typed-evidence-record:code"


def test_procedure_pack_contains_steps_and_rule_closure() -> None:
    pack_set = build_evidence_pack_set(
        publication_plan=_plan(
            _candidate("grapple", ("step-1", "step-2", "rule"), family="procedure-guide")
        ),
        evidence_record_set=_record_set(
            _record(
                "step-1", "procedure_step", "Choose a target.", block_ids=("block-step-1",)
            ),
            _record(
                "step-2",
                "procedure_step",
                "Make an attack check.",
                block_ids=("block-step-2",),
            ),
            _record("rule", "rule", "You must have an empty hand.", block_ids=("block-rule",)),
        ),
        source_map=_source_map(
            _block("block-step-1", "Choose a target."),
            _block("block-step-2", "Make an attack check."),
            _block("block-rule", "You must have an empty hand."),
        ),
    )

    assert [item.evidence_record_type for item in pack_set.packs[0].items] == [
        "procedure_step",
        "procedure_step",
        "rule",
    ]


def test_topic_pack_prefers_definitions_and_rules_over_repetitive_arguments() -> None:
    pack_set = build_evidence_pack_set(
        publication_plan=_plan(
            _candidate("shade", ("argument", "definition", "rule"), family="topic-concept")
        ),
        evidence_record_set=_record_set(
            _record(
                "argument",
                "argument",
                "Shade appears in the spell list.",
                block_ids=("block-argument",),
            ),
            _record(
                "definition",
                "definition",
                "Shade is a dark spirit.",
                block_ids=("block-definition",),
            ),
            _record("rule", "rule", "Shade creates darkness.", block_ids=("block-rule",)),
        ),
        source_map=_source_map(
            _block("block-argument", "Shade appears in the spell list."),
            _block("block-definition", "Shade is a dark spirit."),
            _block("block-rule", "Shade creates darkness."),
        ),
    )

    assert [item.evidence_record_type for item in pack_set.packs[0].items] == [
        "definition",
        "rule",
        "argument",
    ]


def test_evidence_packs_are_ordered_by_article_viability_rank() -> None:
    lower = _candidate("procedure", ("record-procedure",), family="procedure-guide", rank=10)
    higher = _candidate("topic", ("record-topic",), family="topic-concept", rank=30)
    pack_set = build_evidence_pack_set(
        publication_plan=PagePublicationPlan(
            page_publication_plan_id="publication-plan",
            page_publication_plan_fingerprint="fingerprint",
            source_id="source",
            source_hash=_HASH,
            source_profile_kind="rpg-rules",
            publication_budget_id="budget",
            accepted_candidates=(lower, higher),
            rejected_candidates=(),
            public_counts=(("procedure-guide", 1), ("topic-concept", 1)),
        ),
        evidence_record_set=_record_set(
            _record("record-procedure", "rule", "Procedure evidence."),
            _record("record-topic", "definition", "Topic evidence."),
        ),
        source_map=_source_map(_block("block-shade", "Shared source evidence.")),
    )

    assert [pack.page_id for pack in pack_set.packs] == ["topic", "procedure"]


def test_pack_adapter_keeps_support_refs_for_current_synthesis_plan() -> None:
    pack_set = build_evidence_pack_set(
        publication_plan=_plan(_candidate("shade", ("record-shade",))),
        evidence_record_set=_record_set(_record("record-shade", "rule", "Shade creates darkness.")),
        source_map=_source_map(_block("block-shade", "Shade creates a region of darkness.")),
    )
    plan = PageSynthesisPlan(
        page_id="shade",
        page_kind="concept",
        page_family="topic-concept",
        title="Shade",
        source_page_id="source",
        source_locator="source.pdf",
        source_section_page_ids=(),
        outline=(PageOutlineSection("Source-Backed View", "Explain.", (), "paragraph"),),
        evidence_set=PageEvidenceSet("shade", ()),
    )

    adapted = apply_evidence_pack_to_synthesis_plan(plan, pack_set.packs[0])

    assert adapted.selected_support_codes == frozenset({"typed-evidence-record:record-shade"})
    assert adapted.outline[0].support_refs[0].code == "typed-evidence-record:record-shade"


def _plan(candidate: PageCandidate) -> PagePublicationPlan:
    return PagePublicationPlan(
        page_publication_plan_id="publication-plan",
        page_publication_plan_fingerprint="fingerprint",
        source_id="source",
        source_hash=_HASH,
        source_profile_kind="rpg-rules",
        publication_budget_id="budget",
        accepted_candidates=(candidate,),
        rejected_candidates=(),
        public_counts=((candidate.page_family, 1),),
    )


def _candidate(
    page_id: str,
    support: tuple[str, ...],
    *,
    family: str = "topic-concept",
    rank: float = 1,
) -> PageCandidate:
    return PageCandidate(
        page_candidate_id=f"candidate-{page_id}",
        source_id="source",
        source_hash=_HASH,
        source_profile_kind="rpg-rules",
        page_id=page_id,
        title=page_id.title(),
        page_kind="concept",
        page_family=family,
        origin="test",
        rank_score=rank,
        source_order=1,
        supporting_evidence_record_ids=support,
    )


def _record_set(*records: TypedEvidenceRecord) -> EvidenceRecordSet:
    return EvidenceRecordSet(
        evidence_record_set_id="record-set",
        source_id="source",
        source_locator="source.pdf",
        source_hash=_HASH,
        source_profile_id="rpg-rules",
        evidence_extraction_plan_id="plan",
        records=records,
    )


def _record(
    record_id: str,
    record_type: str,
    text: str,
    *,
    status: str = "accepted",
    block_ids: tuple[str, ...] = ("block-shade",),
    payload: str = "",
) -> TypedEvidenceRecord:
    return TypedEvidenceRecord(
        typed_evidence_record_id=record_id,
        source_id="source",
        source_locator="source.pdf",
        source_hash=_HASH,
        evidence_record_type=record_type,
        status=status,  # type: ignore[arg-type]
        canonical_text=text,
        structured_payload=(
            StructuredEvidencePayload("test", payload) if payload else None
        ),
        source_anchors=(_anchor(),),
        source_block_ids=block_ids,
        confidence=0.9,
    )


def _source_map(*blocks: SourceBlock) -> NormalizedSourceMap:
    return NormalizedSourceMap(
        source_id="source",
        source_locator="source.pdf",
        source_hash=_HASH,
        extractor_name="test",
        extractor_version="test",
        source_blocks=blocks,
    )


def _block(block_id: str, text: str) -> SourceBlock:
    return SourceBlock(
        source_block_id=block_id,
        source_anchor=_anchor(),
        block_type="paragraph",
        source_text=text,
        page_span=(59, 59),
        section_path="Spirit Magic List / Shade",
        parent_block_id="",
        child_block_ids=(),
        confidence=1.0,
        source_order=1,
    )


def _anchor() -> SourceAnchor:
    return SourceAnchor(
        source_locator="source.pdf",
        source_hash=_HASH,
        page_span=(59, 59),
        element_path=("source", "shade"),
        text_fingerprint="shade",
    )
