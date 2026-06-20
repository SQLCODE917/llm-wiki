"""Tests for Source Summary Coverage planning and write contracts."""

import pytest

from llmwiki.config import WikiPaths
from llmwiki.domain.objects import (
    ClaimRoleTag,
    Evidence,
    RawSource,
    Schema,
    SourceBundle,
    SourceClaim,
    SourceSummaryBullet,
    SourceSummaryDraft,
    SourceSummaryPlan,
)
from llmwiki.domain.page_body_contracts import (
    contract_for_page_kind,
    render_source_summary_draft,
    resolve_page_body_contract,
    validate_source_summary_draft,
)
from llmwiki.domain.pages import LOCAL_FLAT_STRUCTURE
from llmwiki.domain.planning import build_markdown_page_plan
from llmwiki.domain.planning_analysis import build_extracted_unit
from llmwiki.domain.source_claims import (
    source_claim_groups,
    source_claims,
    source_summary_plan,
)
from llmwiki.store import WikiStore, WikiStoreError
from llmwiki.workflows.planned_write_tools import (
    PlannedWriteSourceSummaryParams,
    planned_write_page_tool,
)

TODAY = "2026-06-19"


def test_claim_role_tags_default_to_shared_vocabulary_and_can_be_replaced() -> None:
    raw_source = RawSource.from_locator("antikythera-mechanism.md")
    unit = build_extracted_unit(
        unit_id="unit-0001",
        raw_source=raw_source,
        locator="document",
        heading_path="Antikythera Mechanism",
        text="The mechanism may predict eclipses. No full instruction manual was found.",
    )

    default_claims = source_claims((unit,), Schema())
    uncertainty_only_claims = source_claims(
        (unit,),
        Schema(claim_role_tags=(ClaimRoleTag("uncertainty"),)),
    )
    role_free_claims = source_claims((unit,), Schema(claim_role_tags=()))

    assert {"function", "uncertainty"} <= set(default_claims[0].claim_role_tags)
    assert uncertainty_only_claims[0].claim_role_tags == ("uncertainty",)
    assert all(claim.claim_role_tags == () for claim in role_free_claims)
    assert (
        SourceClaim(
            source_claim_id="source-claim-unit-0001-9999",
            statement="Role-free statement.",
            evidence=Evidence(raw_source, "document"),
            extracted_unit_id="unit-0001",
            source_span="document",
        ).claim_role_tags
        == ()
    )


def test_source_summary_plan_selects_limits_uncertainty_and_groups() -> None:
    raw_source = RawSource.from_locator("antikythera-mechanism.md")
    unit = build_extracted_unit(
        unit_id="unit-0001",
        raw_source=raw_source,
        locator="document",
        heading_path="Antikythera Mechanism",
        text=(
            "The Antikythera mechanism is a bronze device. "
            "It could predict eclipses. "
            "Only fragments survive. "
            "No complete manual was found. "
            "Scholars may not know every display."
        ),
    )
    claims = source_claims((unit,), Schema())
    groups = source_claim_groups(claims)
    contract = resolve_page_body_contract(
        contract_for_page_kind(Schema(), "source"),
        required_source_citations=("raw/antikythera-mechanism.md",),
    )

    plan = source_summary_plan(
        page_id="antikythera-mechanism",
        contract=contract,
        claims=claims,
        groups=groups,
    )

    assert plan is not None
    selected_roles = {
        role
        for claim in claims
        if claim.source_claim_id in plan.selected_source_claims
        for role in claim.claim_role_tags
    }
    assert {"limitation", "negative-evidence", "uncertainty"} <= selected_roles
    assert plan.required_source_claim_groups
    assert plan.required_source_citations == ("raw/antikythera-mechanism.md",)


def test_source_summary_draft_validation_requires_selected_claim_coverage() -> None:
    plan = _source_summary_plan(
        selected_source_claims=("source-claim-unit-0001-0001", "source-claim-unit-0001-0002")
    )
    missing = SourceSummaryDraft(
        source_record_text="Source record for [[alpha]]. (raw/alpha.md)",
        claim_bullets=(
            SourceSummaryBullet(
                "Alpha is summarized in new words. (raw/alpha.md)",
                ("source-claim-unit-0001-0001",),
            ),
        ),
    )
    leaking = SourceSummaryDraft(
        source_record_text="Source record for source-claim-unit-0001-0001. (raw/alpha.md)",
        claim_bullets=(
            SourceSummaryBullet(
                "Alpha is summarized in new words. (raw/alpha.md)",
                ("source-claim-unit-0001-0001",),
            ),
            SourceSummaryBullet(
                "Beta is summarized in new words. (raw/alpha.md)",
                ("source-claim-unit-0001-0002",),
            ),
        ),
    )
    copied = SourceSummaryDraft(
        source_record_text="Source record for [[alpha]]. (raw/alpha.md)",
        claim_bullets=(
            SourceSummaryBullet(
                "Alpha beta gamma delta epsilon zeta eta theta. (raw/alpha.md)",
                ("source-claim-unit-0001-0001",),
            ),
            SourceSummaryBullet(
                "Beta is summarized in new words. (raw/alpha.md)",
                ("source-claim-unit-0001-0002",),
            ),
        ),
    )
    valid = SourceSummaryDraft(
        source_record_text="Source record for [[alpha]]. (raw/alpha.md)",
        claim_bullets=(
            SourceSummaryBullet(
                "Alpha is summarized in new words. (raw/alpha.md)",
                ("source-claim-unit-0001-0001",),
            ),
            SourceSummaryBullet(
                "Beta is summarized in new words. (raw/alpha.md)",
                ("source-claim-unit-0001-0002",),
            ),
        ),
    )

    assert [finding.finding_type for finding in validate_source_summary_draft(missing, plan)] == [
        "SelectedSourceClaims"
    ]
    assert [finding.finding_type for finding in validate_source_summary_draft(leaking, plan)] == [
        "SourceClaimIdLeak"
    ]
    assert [
        finding.finding_type
        for finding in validate_source_summary_draft(
            copied,
            plan,
            source_text="Alpha beta gamma delta epsilon zeta eta theta iota.",
        )
    ] == ["CopiedSourcePhrase"]
    assert validate_source_summary_draft(valid, plan) == ()
    assert "source-claim-unit" not in render_source_summary_draft(valid)


def test_planned_source_summary_tool_accepts_draft_and_retains_artifact(
    paths: WikiPaths,
) -> None:
    source_text = (
        "# Alpha\n\n"
        "Alpha is a test source. "
        "It may predict beta behavior. "
        "No complete secondary record was found."
    )
    (paths.raw_dir / "alpha.md").write_text(source_text, encoding="utf-8")
    store = WikiStore(paths)
    raw_source = RawSource.from_locator("alpha.md")
    page_plan = build_markdown_page_plan(
        plan_id="test-plan",
        source_bundle=SourceBundle.one(raw_source),
        raw_source=raw_source,
        source_text=source_text,
        existing_pages={},
        wiki_structure=LOCAL_FLAT_STRUCTURE,
        today=TODAY,
    )
    planned_write = page_plan.planned_writes[0]
    assert planned_write.source_summary_plan is not None
    selected_claims = planned_write.source_summary_plan.selected_source_claims
    claim_bullets = [
        {
            "bullet_text": f"Claim {index} is paraphrased for alpha. (raw/alpha.md)",
            "covered_source_claims": [claim_id],
        }
        for index, claim_id in enumerate(selected_claims, start=1)
    ]
    while len(claim_bullets) < 3:
        claim_bullets.append(
            {
                "bullet_text": "A supporting alpha claim is restated briefly. (raw/alpha.md)",
                "covered_source_claims": [selected_claims[0]],
            }
        )
    tool = planned_write_page_tool(store, TODAY, planned_write)

    result = tool.callable(
        source_record_text=(
            "Source record for [[alpha]]; the source may remain limited. (raw/alpha.md)"
        ),
        claim_bullets=claim_bullets,
    )

    body = store.read_page("alpha")
    artifact = (
        store.page_plan_artifact_dir("alpha.md")
        / "accepted-source-summaries"
        / f"{planned_write.write_id}.json"
    )
    assert tool.spec.parameters is PlannedWriteSourceSummaryParams
    assert "Wrote wiki/alpha.md" in result
    assert "## Key supported claims" in body
    assert "source-claim-unit" not in body
    assert artifact.exists()


def test_planned_source_summary_tool_rejects_uncovered_selected_claim(
    paths: WikiPaths,
) -> None:
    source_text = (
        "Alpha is a test source. "
        "Alpha may predict beta behavior. "
        "No complete secondary record was found."
    )
    (paths.raw_dir / "alpha.md").write_text(source_text, encoding="utf-8")
    store = WikiStore(paths)
    raw_source = RawSource.from_locator("alpha.md")
    page_plan = build_markdown_page_plan(
        plan_id="test-plan",
        source_bundle=SourceBundle.one(raw_source),
        raw_source=raw_source,
        source_text=source_text,
        existing_pages={},
        wiki_structure=LOCAL_FLAT_STRUCTURE,
        today=TODAY,
    )
    tool = planned_write_page_tool(store, TODAY, page_plan.planned_writes[0])
    selected_claims = page_plan.planned_writes[0].source_summary_plan.selected_source_claims
    covered_claim = selected_claims[0]

    with pytest.raises(WikiStoreError, match="missing coverage"):
        tool.callable(
            source_record_text="Source record for [[alpha]] that may be limited. (raw/alpha.md)",
            claim_bullets=[
                {
                    "bullet_text": "Only one claim is covered and may be limited. (raw/alpha.md)",
                    "covered_source_claims": [covered_claim],
                },
                {
                    "bullet_text": "The same claim is paraphrased again. (raw/alpha.md)",
                    "covered_source_claims": [covered_claim],
                },
                {
                    "bullet_text": "The draft still omits another selected claim. (raw/alpha.md)",
                    "covered_source_claims": [covered_claim],
                },
            ],
        )

    assert store.list_pages() == []


def _source_summary_plan(selected_source_claims: tuple[str, ...]) -> SourceSummaryPlan:
    return SourceSummaryPlan(
        source_summary_plan_id="source-summary-plan-alpha",
        page_id="alpha",
        selected_source_claims=selected_source_claims,
        required_source_citations=("raw/alpha.md",),
    )
