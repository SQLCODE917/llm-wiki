from llmwiki.config import WikiPaths
from llmwiki.domain.answer_evaluation import AnswerEvaluationCase, evaluate_answer
from llmwiki.domain.claim_support_selection import select_claim_support_candidates
from llmwiki.domain.evidence_registry import (
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
from llmwiki.domain.pages import PageMetadata, WikiPage
from llmwiki.domain.technical_atom_builder import build_technical_atom_catalog
from llmwiki.domain.technical_atom_io import (
    technical_atom_catalog_from_json,
    technical_atom_catalog_to_json,
)
from llmwiki.store import WikiStore
from llmwiki.workflows.source_summary_write import (
    SourceSummaryBulletParams,
    source_summary_page_body,
)

TODAY = "2026-06-22"


def test_technical_atom_builder_preserves_structured_details() -> None:
    plan, registry = _plan(_technical_source())

    catalog = build_technical_atom_catalog(
        source_locator="rules.md",
        page_plan=plan,
        evidence_registry=registry,
        artifact_fingerprint="fp",
    )

    atoms_by_kind = {atom.atom_kind: atom for atom in catalog.technical_atoms}
    assert {
        "code",
        "formula",
        "procedure",
        "table-row",
        "requirement",
        "exception",
        "worked-example",
    } <= set(atoms_by_kind)
    assert atoms_by_kind["code"].technical_payload == "const add = (a, b) => a + b;"
    assert atoms_by_kind["formula"].technical_payload == (
        "**Falling damage** = fall height x 3 - defense reduction"
    )
    assert all(atom.evidence_ids for atom in catalog.technical_atoms)


def test_technical_atom_ids_are_stable_for_same_payload_and_evidence() -> None:
    plan, registry = _plan(_technical_source())

    first = build_technical_atom_catalog(
        source_locator="rules.md",
        page_plan=plan,
        evidence_registry=registry,
        artifact_fingerprint="fp",
    )
    second = build_technical_atom_catalog(
        source_locator="rules.md",
        page_plan=plan,
        evidence_registry=registry,
        artifact_fingerprint="fp",
    )

    assert [atom.technical_atom_id for atom in first.technical_atoms] == [
        atom.technical_atom_id for atom in second.technical_atoms
    ]


def test_builder_does_not_branch_on_source_file_name() -> None:
    markdown_plan, markdown_registry = _plan(_technical_source(), source_locator="rules.md")
    pdf_plan, pdf_registry = _plan(_technical_source(), source_locator="manual.pdf")

    markdown_catalog = build_technical_atom_catalog(
        source_locator="rules.md",
        page_plan=markdown_plan,
        evidence_registry=markdown_registry,
        artifact_fingerprint="fp",
    )
    pdf_catalog = build_technical_atom_catalog(
        source_locator="manual.pdf",
        page_plan=pdf_plan,
        evidence_registry=pdf_registry,
        artifact_fingerprint="fp",
    )

    markdown_shapes = tuple(
        (atom.atom_kind, atom.technical_payload) for atom in markdown_catalog.technical_atoms
    )
    pdf_shapes = tuple(
        (atom.atom_kind, atom.technical_payload) for atom in pdf_catalog.technical_atoms
    )
    assert markdown_shapes == pdf_shapes


def test_technical_atom_catalog_round_trips_json() -> None:
    plan, registry = _plan(_technical_source())
    catalog = build_technical_atom_catalog(
        source_locator="rules.md",
        page_plan=plan,
        evidence_registry=registry,
        artifact_fingerprint="fp",
    )

    restored = technical_atom_catalog_from_json(technical_atom_catalog_to_json(catalog))

    assert restored == catalog


def test_source_summary_page_body_appends_technical_details(
    store: WikiStore, paths: WikiPaths
) -> None:
    (paths.raw_dir / "rules.md").write_text(_technical_source(), encoding="utf-8")
    plan, registry = _plan(_technical_source())
    catalog = build_technical_atom_catalog(
        source_locator="rules.md",
        page_plan=plan,
        evidence_registry=registry,
        artifact_fingerprint="fp",
    )
    store.write_technical_atom_catalog_artifact("rules.md", technical_atom_catalog_to_json(catalog))

    body, _draft = source_summary_page_body(
        store,
        plan.planned_writes[0],
        "Rules source.",
        [
            SourceSummaryBulletParams(
                bullet_text="Characters roll dice. (raw/rules.md)",
                covered_source_claims=["claim-requirement"],
            )
        ],
    )

    assert "## Technical details" in body
    assert "const add = (a, b) => a + b;" in body
    assert "Citation: (raw/rules.md normalized:L1-L12)" in body


def test_claim_support_selection_samples_technical_atom_candidates(
    store: WikiStore, paths: WikiPaths
) -> None:
    (paths.raw_dir / "rules.md").write_text(_technical_source(), encoding="utf-8")
    plan, registry = _plan(_technical_source())
    catalog = build_technical_atom_catalog(
        source_locator="rules.md",
        page_plan=plan,
        evidence_registry=registry,
        artifact_fingerprint="fp",
    )
    store.write_page(
        WikiPage.from_metadata(
            PageMetadata("rules", "source", "Rules.", sources=("rules.md",), updated=TODAY),
            "## Technical details\n\nFormula. (raw/rules.md)",
        )
    )

    selection = select_claim_support_candidates(
        store.page_texts(),
        store.source_inventory(),
        (registry,),
        (),
        (catalog,),
        max_claims=10,
        source="raw/rules.md",
    )

    assert any(candidate.candidate_kind == "technical-atom" for candidate in selection.candidates)


def test_answer_evaluation_checks_normal_query_answer() -> None:
    case = AnswerEvaluationCase(
        case_id="case-1",
        source_locator="rules.md",
        question="How do checks work?",
        required_atom_ids=("technical-atom-1",),
        required_fragments=("roll 2D",),
        required_citations=("raw/rules.md",),
    )

    report = evaluate_answer("You roll 2D, then compare. (raw/rules.md)", case)

    assert report.verdict == "pass"
    assert report.covered_atom_ids == ("technical-atom-1",)


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
            "Except when double ones occur, the check fails.",
            "A worked example rolls 8 + 4 = 12.",
        )
    )


def _plan(text: str, source_locator: str = "rules.md") -> tuple[PagePlan, EvidenceRegistry]:
    raw = RawSource(source_locator, "markdown")
    evidence = Evidence(raw, "L1-L13", "rules", "Rules source.")
    unit = ExtractedUnit("unit-1", raw, "L1-L13", "Rules", text, "extracted")
    write = PlannedPageWrite(
        write_id="write-rules",
        action="create",
        page_metadata=PageMetadata("rules", "source", "Rules.", sources=(source_locator,)),
        extracted_units=("unit-1",),
        evidence=(evidence,),
        source_summary_plan=SourceSummaryPlan(
            "source-summary-plan-rules",
            "rules",
            ("claim-requirement",),
        ),
    )
    claims = (
        _claim(
            raw,
            "claim-requirement",
            "Characters must roll 2D before comparing target.",
            "requirement",
        ),
        _claim(
            raw,
            "claim-exception",
            "Except when double ones occur, the check fails.",
            "limitation",
        ),
        _claim(raw, "claim-example", "A worked example rolls 8 + 4 = 12.", "worked-example"),
    )
    plan = PagePlan(
        plan_id="plan-rules",
        source_bundle=SourceBundle.one(raw),
        extracted_units=(unit,),
        source_claims=claims,
        source_claim_groups=(),
        candidate_claims=(),
        candidate_topics=(),
        candidate_entities=(),
        topic_clusters=(),
        wiki_matches=(),
        claim_comparisons=(),
        planned_writes=(write,),
    )
    return plan, build_evidence_registry(plan, (source_text_from_text(source_locator, text),))


def _claim(raw: RawSource, claim_id: str, statement: str, role: str) -> SourceClaim:
    return SourceClaim(
        source_claim_id=claim_id,
        statement=statement,
        evidence=Evidence(raw, "L1-L13", "rules", statement),
        extracted_unit_id="unit-1",
        source_span="L1-L13",
        claim_role_tags=(role,),
        claim_salience=1.0,
    )
