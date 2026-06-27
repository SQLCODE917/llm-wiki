from llmwiki.domain.evidence_registry import (
    EvidenceRecord,
    EvidenceRegistry,
    build_evidence_registry,
    source_text_from_text,
)
from llmwiki.domain.objects import (
    Evidence,
    ExtractedUnit,
    PagePlan,
    PlannedPageWrite,
    RawSource,
    SourceBundle,
    SourceClaim,
    SourceSummaryPlan,
)
from llmwiki.domain.pages import PageMetadata
from llmwiki.domain.technical_atom_builder import build_technical_atom_catalog
from llmwiki.domain.technical_atom_detection import best_evidence_ids


def test_best_evidence_ids_prefers_exact_table_row_evidence() -> None:
    records = (
        _record("evidence-intro", "A combat example introduces attack checks."),
        _record("evidence-hit", "A hit check uses 2D before damage is calculated."),
        _record("evidence-table", "| 2D | 2 | ** | ** |\n| 3 | 3 | ** | 0 |"),
    )

    evidence_ids = best_evidence_ids(records, "| 2D | 2 | ** | ** |")

    assert evidence_ids == ("evidence-table",)


def test_best_evidence_ids_tolerates_non_text_payloads() -> None:
    record = EvidenceRecord(
        evidence_id="evidence-weird",
        source_locator="rules.md",
        source_hash="source-hash",
        source_range_id="source-range-rules",
        line_range=(1, 4),
        excerpt=object(),  # type: ignore[arg-type]
        excerpt_digest="evidence-weird",
        evidence_kind="source-claim",
        source_claim_id="claim-weird",
    )

    assert best_evidence_ids((record,), {"table": "not normalized yet"}) == ("evidence-weird",)


def test_best_evidence_ids_bounds_pathological_excerpts() -> None:
    records = (
        _record("evidence-long", "noise " * 50_000),
        _record("evidence-hit", "A hit check uses 2D before damage is calculated."),
    )

    assert best_evidence_ids(records, "hit check 2D") == ("evidence-hit",)


def test_table_atoms_use_matching_table_evidence_and_claim() -> None:
    plan, registry = _table_plan()
    table_record = next(
        record for record in registry.evidence_records if record.source_claim_id == "claim-table"
    )

    catalog = build_technical_atom_catalog(
        source_locator="rules.md",
        page_plan=plan,
        evidence_registry=registry,
        artifact_fingerprint="fp",
    )

    table_atom = next(atom for atom in catalog.technical_atoms if atom.atom_kind == "table")
    assert table_atom.evidence_ids == (table_record.evidence_id,)
    assert table_atom.source_claim_ids == ("claim-table",)
    assert catalog.technical_tables[0].blocks[0].markdown == (
        "| 2D | 2 | ** | ** |\n| 3 | 3 | ** | 0 |"
    )


def _table_plan() -> tuple[PagePlan, EvidenceRegistry]:
    text = "\n".join(
        (
            "# Attack Table",
            "Use the attack table after the hit check.",
            "| 2D | 2 | ** | ** |",
            "| 3 | 3 | ** | 0 |",
        )
    )
    raw = RawSource("rules.md", "markdown")
    evidence = Evidence(raw, "L1-L4", "Attack Table", "Attack table source.")
    unit = ExtractedUnit("unit-1", raw, "L1-L4", "Attack Table", text, "extracted")
    write = PlannedPageWrite(
        write_id="write-rules",
        action="create",
        page_metadata=PageMetadata("rules", "source", "Rules.", sources=("rules.md",)),
        extracted_units=("unit-1",),
        evidence=(evidence,),
        source_summary_plan=SourceSummaryPlan("source-summary-plan-rules", "rules", ()),
    )
    plan = PagePlan(
        plan_id="plan-rules",
        source_bundle=SourceBundle.one(raw),
        extracted_units=(unit,),
        source_claims=(
            _claim(raw, "claim-intro", "Use the attack table after the hit check."),
            _claim(raw, "claim-table", "| 2D | 2 | ** | ** |\n| 3 | 3 | ** | 0 |"),
        ),
        source_claim_groups=(),
        candidate_claims=(),
        candidate_topics=(),
        candidate_entities=(),
        topic_clusters=(),
        wiki_matches=(),
        claim_comparisons=(),
        planned_writes=(write,),
    )
    registry = build_evidence_registry(plan, (source_text_from_text("rules.md", text),))
    return plan, registry


def _claim(raw: RawSource, source_claim_id: str, statement: str) -> SourceClaim:
    return SourceClaim(
        source_claim_id=source_claim_id,
        statement=statement,
        evidence=Evidence(raw, "L1-L4", "Attack Table", statement),
        extracted_unit_id="unit-1",
        source_span="L1-L4",
        claim_role_tags=("table",),
        claim_salience=1.0,
    )


def _record(evidence_id: str, excerpt: str) -> EvidenceRecord:
    return EvidenceRecord(
        evidence_id=evidence_id,
        source_locator="rules.md",
        source_hash="source-hash",
        source_range_id="source-range-rules",
        line_range=(1, 4),
        excerpt=excerpt,
        excerpt_digest=evidence_id,
        evidence_kind="source-claim",
        source_claim_id=evidence_id.replace("evidence", "claim"),
    )
