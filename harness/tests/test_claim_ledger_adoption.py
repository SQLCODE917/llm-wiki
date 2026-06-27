import json

from llmwiki.config import WikiPaths
from llmwiki.domain.evidence_registry import build_evidence_registry, source_text_from_text
from llmwiki.domain.ingest_confidence import ArtifactFingerprint
from llmwiki.domain.ledger.current_artifacts import build_current_ledger_artifacts
from llmwiki.domain.objects import (
    Evidence,
    ExtractedUnit,
    PagePlan,
    PlannedPageWrite,
    RawSource,
    Schema,
    SourceBundle,
    SourceClaim,
    SourceSummaryPlan,
)
from llmwiki.domain.pages import PageMetadata
from llmwiki.domain.technical_atom_builder import build_technical_atom_catalog
from llmwiki.runtime.ingest_confidence_artifact_store import write_generated_artifacts
from llmwiki.store import WikiStore
from llmwiki.workflows.source_summary_write import (
    SourceSummaryBulletParams,
    source_summary_page_body,
)


def test_current_ledger_preserves_claims_and_technical_atoms() -> None:
    plan, registry, catalog = _artifacts()

    bundle = build_current_ledger_artifacts(
        source_locator="rules.md",
        page_plan=plan,
        evidence_registry=registry,
        technical_atom_catalog=catalog,
    )

    kinds = {entry.ledger_entry_kind for entry in bundle.ledger.entries}
    atom_kinds = {atom.technical_atom_kind for atom in bundle.ledger.technical_atoms}
    table = next(
        atom for atom in bundle.ledger.technical_atoms if atom.technical_atom_kind == "table"
    )
    coverage = bundle.projection_coverage_artifact.projection_coverage
    topics = bundle.topic_index.topics
    coverage_kinds = {entry.projection_coverage_unit_kind for entry in coverage.entries}
    assert {"claim", "technical-atom"} <= kinds
    assert {"code-block", "formula", "procedure", "rule", "table"} <= atom_kinds
    assert "| 2D | Result |" in table.payload.raw_table_text
    assert {"generated-page-claim", "rendered-technical-atom-block"} <= coverage_kinds
    assert topics[0].topic_key == "rules"
    assert not bundle.ledger_quality_report.has_severity("blocking")


def test_generated_artifacts_write_claim_ledger_without_replacing_page_synthesis(
    store: WikiStore, paths: WikiPaths
) -> None:
    source_text = _technical_source()
    (paths.raw_dir / "rules.md").write_text(source_text, encoding="utf-8")
    plan, registry, catalog = _artifacts()
    fingerprint = ArtifactFingerprint.from_schema(
        source_locator="rules.md",
        source_hash=registry.source_texts[0].source_hash,
        schema=Schema(),
    )

    write_generated_artifacts(
        store,
        "rules.md",
        store.page_plan_artifact_dir("rules.md"),
        fingerprint,
        plan,
        registry,
        None,
        catalog,
    )
    body, _draft = source_summary_page_body(
        store,
        plan.planned_writes[0],
        "Rules source.",
        [
            SourceSummaryBulletParams(
                bullet_text="Characters must roll dice. (raw/rules.md)",
                covered_source_claims=["claim-requirement"],
            )
        ],
    )

    ledger_text = store.read_claim_ledger_artifact("rules.md")
    topics_text = store.read_topic_index_artifact("rules.md")
    assert ledger_text is not None
    assert topics_text is not None
    assert json.loads(ledger_text)["ledger"]["technical_atoms"]
    assert json.loads(topics_text)["topics"][0]["topic_key"] == "rules"
    assert store.list_topic_index_artifacts() == [topics_text]
    assert "## Technical details" in body
    assert "const add = (a, b) => a + b;" in body
    assert "## Source review" not in body
    assert "Claim-ledger projection" not in body


def _artifacts():
    text = _technical_source()
    plan = _plan(text)
    registry = build_evidence_registry(plan, (source_text_from_text("rules.md", text),))
    catalog = build_technical_atom_catalog(
        source_locator="rules.md",
        page_plan=plan,
        evidence_registry=registry,
        artifact_fingerprint="fp",
    )
    return plan, registry, catalog


def _technical_source() -> str:
    return "\n".join(
        (
            "# Rules",
            "```js",
            "const add = (a, b) => a + b;",
            "```",
            "**Falling damage** = fall height x 3 - defense reduction",
            "| 2D | Result |",
            "| 2 | fumble |",
            "1. Roll 2D.",
            "2. Add modifier.",
            "Characters must roll 2D before comparing target.",
        )
    )


def _plan(text: str) -> PagePlan:
    raw = RawSource("rules.md", "markdown")
    unit = ExtractedUnit("unit-1", raw, "L1-L10", "Rules", text, "extracted")
    write = PlannedPageWrite(
        write_id="write-rules",
        action="create",
        page_metadata=PageMetadata("rules", "source", "Rules.", sources=("rules.md",)),
        extracted_units=("unit-1",),
        evidence=(Evidence(raw, "L1-L10", "rules", "Rules source."),),
        source_summary_plan=SourceSummaryPlan(
            "source-summary-plan-rules",
            "rules",
            ("claim-requirement",),
        ),
    )
    return PagePlan(
        plan_id="plan-rules",
        source_bundle=SourceBundle.one(raw),
        extracted_units=(unit,),
        source_claims=(_claim(raw),),
        source_claim_groups=(),
        candidate_claims=(),
        candidate_topics=(),
        candidate_entities=(),
        topic_clusters=(),
        wiki_matches=(),
        claim_comparisons=(),
        planned_writes=(write,),
    )


def _claim(raw: RawSource) -> SourceClaim:
    statement = "Characters must roll 2D before comparing target."
    return SourceClaim(
        source_claim_id="claim-requirement",
        statement=statement,
        evidence=Evidence(raw, "L1-L10", "rules", statement),
        extracted_unit_id="unit-1",
        source_span="L1-L10",
        claim_role_tags=("requirement",),
        claim_salience=1.0,
    )
