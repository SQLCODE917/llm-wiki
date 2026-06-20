"""Tests for planned PageBody contracts and planned write tools."""

import pytest

from llmwiki.config import WikiPaths
from llmwiki.domain.evidence import EvidencePolicy
from llmwiki.domain.objects import (
    Evidence,
    PageBodyContract,
    PageBodyFinding,
    PlannedPageWrite,
    RawSource,
    Schema,
    SourceBundle,
    SourcePlan,
    SourcePlanContractSelection,
)
from llmwiki.domain.page_body_contracts import (
    contract_for_page_kind,
    resolve_page_body_contract,
    validate_page_body,
)
from llmwiki.domain.pages import LOCAL_FLAT_STRUCTURE, PageMetadata, WikiPage
from llmwiki.domain.planning import build_page_plan, observation_report
from llmwiki.domain.planning_analysis import build_extracted_unit
from llmwiki.store import WikiStore, WikiStoreError
from llmwiki.workflows.tools import planned_write_page_tool

TODAY = "2026-06-19"


class SpyStore(WikiStore):
    def __init__(self, paths: WikiPaths) -> None:
        super().__init__(paths)
        self.write_count = 0

    def write_page(self, page: WikiPage) -> None:
        self.write_count += 1
        super().write_page(page)


def test_schema_owns_default_page_body_contracts_and_raw_source_has_none() -> None:
    schema = Schema()
    contract_ids = {contract.contract_id for contract in schema.page_body_contracts}

    assert {"source-summary", "entity-page", "concept-page", "synthesis-page"} <= contract_ids
    assert contract_for_page_kind(schema, "source").contract_id == "source-summary"
    assert PageBodyFinding("RequiredSections", "missing Source record").finding_type
    assert not hasattr(RawSource.from_locator("article.md"), "page_body_contract_selections")


def test_source_plan_selects_contract_and_page_plan_resolves_it() -> None:
    raw_source = RawSource.from_locator("article.md")
    contract = PageBodyContract(
        contract_id="brief-source",
        match_page_kinds=("source",),
        max_words=90,
    )
    schema = Schema(page_body_contracts=Schema().page_body_contracts + (contract,))
    source_plan = SourcePlan(
        raw_source=raw_source,
        source_classification="markdown",
        ingest_disposition="plan-pages",
        page_body_contract_selections=(
            SourcePlanContractSelection(
                contract_id="brief-source",
                page_ids=("alpha",),
                max_words_override=72,
            ),
        ),
    )
    unit = build_extracted_unit(
        unit_id="unit-0001",
        raw_source=raw_source,
        locator="document",
        heading_path="Alpha",
        text="Alpha may suggest a possible observation.",
    )

    plan = build_page_plan(
        plan_id="test-plan",
        source_bundle=SourceBundle.one(raw_source),
        raw_source=raw_source,
        extracted_units=(unit,),
        existing_pages={},
        wiki_structure=LOCAL_FLAT_STRUCTURE,
        today=TODAY,
        schema=schema,
        source_plan=source_plan,
    )

    alpha = next(write for write in plan.planned_writes if write.page_metadata.page_id == "alpha")
    hub = next(write for write in plan.planned_writes if write.page_metadata.page_id == "article")
    assert alpha.resolved_page_body_contract.contract_id == "brief-source"
    assert alpha.resolved_page_body_contract.max_words == 72
    assert alpha.resolved_page_body_contract.required_uncertainty_terms == (
        "may",
        "possible",
        "suggest",
    )
    assert hub.resolved_page_body_contract.contract_id == "source-summary"
    assert "ResolvedPageBodyContract `brief-source`" in observation_report(plan)


def test_source_summary_rejects_copy_and_accepts_compact_claims() -> None:
    source_text = (
        "The Antikythera mechanism may have tracked astronomical cycles. "
        "The device was recovered from a shipwreck and its inscriptions "
        "suggest possible calendrical and eclipse functions."
    )
    contract = resolve_page_body_contract(
        contract_for_page_kind(Schema(), "source"),
        required_link_page_ids=("antikythera-mechanism",),
        required_source_citations=("raw/antikythera-mechanism.md",),
        required_uncertainty_terms=("may", "suggest", "possible"),
    )
    copied = (
        "The Antikythera mechanism may have tracked astronomical cycles. "
        "The device was recovered from a shipwreck and its inscriptions "
        "suggest possible calendrical and eclipse functions. "
        "See [[antikythera-mechanism]]. (raw/antikythera-mechanism.md)"
    )
    compact = (
        "## Source record\n\n"
        "Source record for [[antikythera-mechanism]]. The evidence may remain uncertain. "
        "(raw/antikythera-mechanism.md)\n\n"
        "## Key supported claims\n\n"
        "- The source supports an astronomical interpretation. (raw/antikythera-mechanism.md)\n"
        "- The source preserves possible functions without resolving them. "
        "(raw/antikythera-mechanism.md)\n"
        "- The source points to unresolved origin evidence. (raw/antikythera-mechanism.md)"
    )

    copied_findings = validate_page_body(copied, contract, source_text=source_text)

    assert {finding.finding_type for finding in copied_findings} >= {
        "RequiredSections",
        "RequiredMarkdownShape",
        "MaxCopiedNGramRatio",
    }
    assert validate_page_body(compact, contract, source_text=source_text) == ()


def test_user_defined_contract_controls_page_shape() -> None:
    contract = PageBodyContract(
        contract_id="product-page",
        match_page_kinds=("entity",),
        required_sections=("Applications", "Limitations"),
    )
    resolved = resolve_page_body_contract(contract)

    assert [
        f.finding_type for f in validate_page_body("## Applications\n\nDoor closer.", resolved)
    ] == ["RequiredSections"]
    assert (
        validate_page_body(
            "## Applications\n\nDoor closer.\n\n## Limitations\n\nOpen items.",
            resolved,
        )
        == ()
    )


def test_planned_write_rejects_invalid_page_body_before_store_write(
    paths: WikiPaths,
) -> None:
    (paths.raw_dir / "alpha.md").write_text(
        "Alpha may suggest possible evidence.", encoding="utf-8"
    )
    store = SpyStore(paths)
    tool = planned_write_page_tool(store, TODAY, _source_summary_write("alpha.md"))

    with pytest.raises(WikiStoreError, match="PageBody violates ResolvedPageBodyContract"):
        tool.callable(page_body="Copied prose without required structure. (raw/alpha.md)")

    assert store.write_count == 0
    assert store.list_pages() == []


def test_planned_write_retry_succeeds_after_corrected_page_body(paths: WikiPaths) -> None:
    (paths.raw_dir / "alpha.md").write_text(
        "Alpha may suggest possible evidence.", encoding="utf-8"
    )
    store = SpyStore(paths)
    write_log: list[str] = []
    tool = planned_write_page_tool(
        store,
        TODAY,
        _source_summary_write("alpha.md"),
        write_log=write_log,
    )

    with pytest.raises(WikiStoreError):
        tool.callable(page_body="too short")
    result = tool.callable(page_body=_valid_source_summary_body())

    assert "Wrote wiki/alpha.md" in result
    assert "Key supported claims" in store.read_page("alpha")
    assert store.write_count == 1
    assert write_log == ["alpha"]


def test_planned_write_runs_evidence_policy_after_body_validation(paths: WikiPaths) -> None:
    (paths.raw_dir / "article.md").write_text("Real source text.", encoding="utf-8")
    store = SpyStore(paths)
    raw_source = RawSource.from_locator("article.md")
    contract = resolve_page_body_contract(
        contract_for_page_kind(Schema(), "concept"),
        required_source_citations=("raw/article.md normalized:L1",),
    )
    planned_write = PlannedPageWrite(
        write_id="write-alpha",
        action="create-new",
        page_metadata=PageMetadata(
            page_id="alpha",
            page_kind="concept",
            summary="Alpha.",
            sources=("raw/article.md normalized:L1",),
        ),
        evidence=(Evidence(raw_source, "document"),),
        resolved_page_body_contract=contract,
    )
    tool = planned_write_page_tool(
        store,
        TODAY,
        planned_write,
        evidence_policy=EvidencePolicy(mode="fail"),
    )

    with pytest.raises(WikiStoreError, match="evidence-not-found"):
        tool.callable(page_body='"Fabricated quote." (raw/article.md normalized:L1)')

    assert store.write_count == 0


def _source_summary_write(source_locator: str) -> PlannedPageWrite:
    raw_source = RawSource.from_locator(source_locator)
    return PlannedPageWrite(
        write_id="write-alpha",
        action="create-new",
        page_metadata=PageMetadata(
            page_id="alpha",
            page_kind="source",
            summary="Alpha source.",
            sources=(f"raw/{source_locator}",),
        ),
        evidence=(Evidence(raw_source, "document"),),
        resolved_page_body_contract=resolve_page_body_contract(
            contract_for_page_kind(Schema(), "source"),
            required_source_citations=(f"raw/{source_locator}",),
            required_uncertainty_terms=("may", "possible", "suggest"),
        ),
    )


def _valid_source_summary_body() -> str:
    return (
        "## Source record\n\n"
        "Source record for [[alpha]]. The source may preserve uncertainty. (raw/alpha.md)\n\n"
        "## Key supported claims\n\n"
        "- The source supports an alpha observation. (raw/alpha.md)\n"
        "- The source keeps possible limits visible. (raw/alpha.md)\n"
        "- The source suggests a compact claim set. (raw/alpha.md)"
    )
