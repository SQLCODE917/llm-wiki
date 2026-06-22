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
    SourceSummaryClaimRequirement,
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
from llmwiki.domain.source_summary_coverage import infer_source_summary_coverage
from llmwiki.domain.source_summary_rescue import repair_source_summary_draft
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
    modality_only_claims = source_claims(
        (unit,),
        Schema(claim_role_tags=(ClaimRoleTag("ordinary-modality"),)),
    )
    role_free_claims = source_claims((unit,), Schema(claim_role_tags=()))

    assert {"function", "ordinary-modality"} <= set(default_claims[0].claim_role_tags)
    assert modality_only_claims[0].claim_role_tags == ("ordinary-modality",)
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
            "The source does not specify every display."
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
    assert {"limitation", "negative-evidence", "source-uncertainty"} <= selected_roles
    assert plan.required_source_claim_groups
    assert plan.required_source_citations == ("raw/antikythera-mechanism.md",)


def test_source_summary_plan_prefers_early_claims_in_mixed_chunks() -> None:
    raw_source = RawSource.from_locator("rulebook.pdf")
    filler = " ".join(f"Filler sentence {index} records ordinary context." for index in range(30))
    unit = build_extracted_unit(
        unit_id="unit-0010",
        raw_source=raw_source,
        locator="p.50-56",
        heading_path="Unconscious and Death Checks",
        text=(
            "Damage reduces life force. "
            "If life force becomes 0 or negative, the character falls unconscious. "
            "You must make a death check to determine survival. "
            "A character may die if left untreated. "
            "Only treatment to positive life force restores consciousness. "
            f"{filler} "
            "The Crimson breastplate is said to glow redder than enemy blood. "
            "Mithril silver can be processed into colors that never fade. "
            "If all colors mix together, the result is only black."
        ),
    )
    claims = source_claims((unit,), Schema())
    plan = source_summary_plan(
        page_id="rulebook-unconscious-and-death-checks",
        contract=resolve_page_body_contract(contract_for_page_kind(Schema(), "source")),
        claims=claims,
        groups=source_claim_groups(claims),
    )

    assert plan is not None
    selected_statements = [
        claim.statement for claim in claims if claim.source_claim_id in plan.selected_source_claims
    ]
    assert any("death check" in statement for statement in selected_statements)
    assert not any("Crimson breastplate" in statement for statement in selected_statements)
    assert not any("Mithril silver" in statement for statement in selected_statements)


def test_source_summary_plan_ignores_generic_page_terms_in_section_titles() -> None:
    raw_source = RawSource.from_locator("rulebook.pdf")
    unit = build_extracted_unit(
        unit_id="unit-0029",
        raw_source=raw_source,
        locator="p.125-129",
        heading_path="7.2 Merchant Skill",
        text=(
            "The hunter skill is very similar to the ranger skill. "
            "Being a hunter is a respectable profession, so you should never look down on it. "
            "Merchants are a class with a lot of freedom and often travel for trade. "
            "Merchants are usually issued a merchant pass as proof of status. "
            "Some merchants may sell arts and crafts while others sell fresh produce. "
            "You can only make a check for items that the merchant deals with. "
            "In this case, make a success roll using the captain's sailor skill level."
        ),
    )
    claims = source_claims((unit,), Schema())
    plan = source_summary_plan(
        page_id="sword-world-rpg-complete-edition-7-2-merchant-skill",
        contract=resolve_page_body_contract(contract_for_page_kind(Schema(), "source")),
        claims=claims,
        groups=source_claim_groups(claims),
    )

    assert plan is not None
    selected_statements = [
        claim.statement for claim in claims if claim.source_claim_id in plan.selected_source_claims
    ]
    assert any("Merchants are a class" in statement for statement in selected_statements)
    assert any("merchant deals" in statement for statement in selected_statements)
    assert not any("hunter" in statement.lower() for statement in selected_statements)
    assert not any("sailor skill" in statement for statement in selected_statements)


def test_source_summary_plan_uses_first_relevant_claim_as_mixed_chunk_boundary() -> None:
    raw_source = RawSource.from_locator("rulebook.pdf")
    unit = build_extracted_unit(
        unit_id="unit-0036",
        raw_source=raw_source,
        locator="p.154-158",
        heading_path="11.5 Asking NPCs to Use Magic",
        text=(
            "This is only possible if you're part of a group of people who believe in dragons. "
            "In some cases, adventurers may need to rely on NPCs to save them. "
            "A certain price is required in order to have the magic cast. "
            "You may want to have Remove Curse cast or a magical item appraised. "
            "Runes have magical power, and by chanting them a rune master can use magic."
        ),
    )
    claims = source_claims((unit,), Schema())
    plan = source_summary_plan(
        page_id="sword-world-rpg-complete-edition-11-5-asking-npcs-to-use-magic",
        contract=resolve_page_body_contract(contract_for_page_kind(Schema(), "source")),
        claims=claims,
        groups=source_claim_groups(claims),
    )

    assert plan is not None
    selected_statements = [
        claim.statement for claim in claims if claim.source_claim_id in plan.selected_source_claims
    ]
    assert any("NPCs" in statement for statement in selected_statements)
    assert any("price is required" in statement for statement in selected_statements)
    assert any("Remove Curse" in statement for statement in selected_statements)
    assert not any("believe in dragons" in statement for statement in selected_statements)
    assert not any("Runes have magical power" in statement for statement in selected_statements)


def test_source_summary_plan_does_not_fill_with_late_generic_service_claims() -> None:
    raw_source = RawSource.from_locator("rulebook.pdf")
    unit = build_extracted_unit(
        unit_id="unit-0038",
        raw_source=raw_source,
        locator="p.159-169",
        heading_path="12.2 Rules for Poison, Illness and Infection (part 2)",
        text=(
            "This score is used when making a check to see if you know the illness. "
            "However, this must be at each progression speed of the illness. "
            "Immediately after the illness progression check, only one success roll is allowed. "
            "Adventurer level may also be hero level, but even heroes cannot win against illness. "
            "For requests for such work, you'd usually give 10% to 30% as an advance payment."
        ),
    )
    claims = source_claims((unit,), Schema())
    plan = source_summary_plan(
        page_id="sword-world-rpg-complete-edition-12-2-rules-for-poison-illness-and-infection-part-2",
        contract=resolve_page_body_contract(contract_for_page_kind(Schema(), "source")),
        claims=claims,
        groups=source_claim_groups(claims),
    )

    assert plan is not None
    selected_statements = [
        claim.statement for claim in claims if claim.source_claim_id in plan.selected_source_claims
    ]
    assert any("know the illness" in statement for statement in selected_statements)
    assert any("progression speed" in statement for statement in selected_statements)
    assert not any("advance payment" in statement for statement in selected_statements)


def test_source_summary_plan_uses_local_topic_window_for_narrow_rule_titles() -> None:
    raw_source = RawSource.from_locator("rulebook.pdf")
    filler = " ".join(
        f"Filler sentence {index} records unrelated equipment context." for index in range(10)
    )
    unit = build_extracted_unit(
        unit_id="unit-0064",
        raw_source=raw_source,
        locator="p.268-273",
        heading_path="16.7 Throwing Multiple Darts or Daggers",
        text=(
            "In the basic rules, characters cannot hold separate weapons in each hand. "
            "It’s possible to throw multiple darts or daggers at once. "
            "However, the following restrictions occur in this case. "
            "All objects thrown at the same time must have the same weight. "
            "The total required strength must be up to the character's strength. "
            "The number thrown at the same time becomes a penalty to attack power. "
            "For example, if you throw three at the same time, that incurs a penalty. "
            "You cannot choose multiple targets. "
            "There must always be one target. "
            "Never forget that projectiles cannot be used while in an engagement. "
            f"{filler} "
            "For those with multiple attack methods, you must declare one each round. "
            "A main-gauche is a dagger held in the left hand for parrying. "
            "You gain a +1 bonus to evasion speed only if the opponent's weapon is a dagger. "
            "Of course, your opponent's weapons are limited to daggers, rapiers, and short swords. "
            "It is used in melee, but you can also use it by throwing it."
        ),
    )
    claims = source_claims((unit,), Schema())
    plan = source_summary_plan(
        page_id="sword-world-rpg-complete-edition-16-7-throwing-multiple-darts-or-daggers",
        contract=resolve_page_body_contract(contract_for_page_kind(Schema(), "source")),
        claims=claims,
        groups=source_claim_groups(claims),
    )

    assert plan is not None
    selected_statements = [
        claim.statement for claim in claims if claim.source_claim_id in plan.selected_source_claims
    ]
    assert any("throw multiple darts or daggers" in statement for statement in selected_statements)
    assert any("same weight" in statement for statement in selected_statements)
    assert any("multiple targets" in statement for statement in selected_statements)
    assert not any("multiple attack methods" in statement for statement in selected_statements)
    assert not any("evasion speed" in statement for statement in selected_statements)
    assert not any("opponent's weapons" in statement for statement in selected_statements)


def test_source_summary_plan_ignores_incidental_topic_mentions() -> None:
    raw_source = RawSource.from_locator("rulebook.pdf")
    unit = build_extracted_unit(
        unit_id="unit-0007",
        raw_source=raw_source,
        locator="p.33-36",
        heading_path="2.7 Resistance Rolls",
        text=(
            "A success roll made using adventurer level plus life force bonus is "
            "specifically referred to as a life force resistance roll. "
            "Similarly, a success roll made using adventurer level plus mental power "
            "bonus is called a mental power resistance roll. "
            "Life force resistance rolls avoid physical dangers such as poison, while "
            "mental power resistance rolls avoid magic or curses. "
            "The game master asks us to make a mental power resistance roll against "
            "target score 17. "
            "To the right of each of these is a field to write down the bonus, and "
            "further right is a field labeled resistance."
        ),
    )
    claims = source_claims((unit,), Schema())
    plan = source_summary_plan(
        page_id="sword-world-rpg-complete-edition-2-7-resistance-rolls",
        contract=resolve_page_body_contract(contract_for_page_kind(Schema(), "source")),
        claims=claims,
        groups=source_claim_groups(claims),
    )

    assert plan is not None
    selected_statements = [
        claim.statement for claim in claims if claim.source_claim_id in plan.selected_source_claims
    ]
    assert any("life force resistance roll" in statement for statement in selected_statements)
    assert any("mental power resistance roll" in statement for statement in selected_statements)
    assert any("avoid physical dangers" in statement for statement in selected_statements)
    assert not any("game master asks" in statement for statement in selected_statements)
    assert not any("field labeled resistance" in statement for statement in selected_statements)


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


def test_source_summary_coverage_infers_missing_claim_from_bullet_cues() -> None:
    plan = SourceSummaryPlan(
        source_summary_plan_id="source-summary-plan-alpha",
        page_id="alpha",
        selected_source_claims=(
            "source-claim-unit-0001-0001",
            "source-claim-unit-0001-0002",
        ),
        selected_claim_requirements=(
            SourceSummaryClaimRequirement(
                source_claim_id="source-claim-unit-0001-0001",
                cue_terms=("mental", "power", "roll"),
            ),
            SourceSummaryClaimRequirement(
                source_claim_id="source-claim-unit-0001-0002",
                cue_terms=("life", "force", "roll"),
            ),
        ),
        required_source_citations=("raw/alpha.md",),
    )
    draft = SourceSummaryDraft(
        source_record_text="Source record for [[alpha]]. (raw/alpha.md)",
        claim_bullets=(
            SourceSummaryBullet(
                "Life force resistance roll uses the life force bonus. (raw/alpha.md)",
                ("source-claim-unit-0001-0001",),
            ),
        ),
    )

    inferred = infer_source_summary_coverage(draft, plan)

    assert inferred.claim_bullets[0].covered_source_claims == (
        "source-claim-unit-0001-0001",
        "source-claim-unit-0001-0002",
    )


def test_source_summary_coverage_infers_singular_plural_cue_matches() -> None:
    plan = SourceSummaryPlan(
        source_summary_plan_id="source-summary-plan-alpha",
        page_id="alpha",
        selected_source_claims=("source-claim-unit-0001-0001",),
        selected_claim_requirements=(
            SourceSummaryClaimRequirement(
                source_claim_id="source-claim-unit-0001-0001",
                cue_terms=("character", "sheet", "write"),
            ),
        ),
        required_source_citations=("raw/alpha.md",),
    )
    draft = SourceSummaryDraft(
        source_record_text="Source record for [[alpha]]. (raw/alpha.md)",
        claim_bullets=(
            SourceSummaryBullet(
                "Sheets required for character creation. (raw/alpha.md)",
                (),
            ),
        ),
    )

    inferred = infer_source_summary_coverage(draft, plan)

    assert inferred.claim_bullets[0].covered_source_claims == (
        "source-claim-unit-0001-0001",
    )


def test_source_summary_rescue_repairs_catalog_style_bullets() -> None:
    plan = SourceSummaryPlan(
        source_summary_plan_id="source-summary-plan-catalog",
        page_id="catalog",
        selected_source_claims=(
            "source-claim-unit-0001-0001",
            "source-claim-unit-0001-0002",
            "source-claim-unit-0001-0003",
        ),
        required_source_citations=("raw/book.pdf p.199-211",),
    )
    draft = SourceSummaryDraft(
        source_record_text="Catalog source record.",
        claim_bullets=tuple(
            SourceSummaryBullet(
                f"Catalog item {index} has a page-only citation (p. {199 + index}).",
                (f"source-claim-{index}",),
            )
            for index in range(1, 8)
        ),
    )

    repaired = repair_source_summary_draft(draft, plan, max_claim_bullets=5)

    assert len(repaired.claim_bullets) == 5
    assert all(not bullet.covered_source_claims for bullet in repaired.claim_bullets)
    assert "raw/book.pdf p.199-211" in repaired.source_record_text
    assert "raw/book.pdf p.200" in repaired.claim_bullets[0].bullet_text
    assert "raw/book.pdf p.204" in repaired.claim_bullets[4].bullet_text


def test_missing_source_summary_coverage_reports_claim_requirements() -> None:
    plan = SourceSummaryPlan(
        source_summary_plan_id="source-summary-plan-alpha",
        page_id="alpha",
        selected_source_claims=("source-claim-unit-0001-0001",),
        selected_claim_requirements=(
            SourceSummaryClaimRequirement(
                source_claim_id="source-claim-unit-0001-0001",
                claim_role_tags=("method", "identity"),
                claim_eligibility="eligible",
                claim_centrality=0.5,
                cue_terms=("life", "force", "roll"),
            ),
        ),
        required_source_citations=("raw/alpha.md",),
    )
    draft = SourceSummaryDraft(
        source_record_text="Source record for [[alpha]]. (raw/alpha.md)",
        claim_bullets=(
            SourceSummaryBullet(
                "Alpha is summarized in new words. (raw/alpha.md)",
                (),
            ),
        ),
    )

    findings = validate_source_summary_draft(draft, plan)

    assert len(findings) == 1
    assert findings[0].finding_type == "SelectedSourceClaims"
    assert "claim_id `source-claim-unit-0001-0001`" in findings[0].detail
    assert "cue_terms `life, force, roll`" in findings[0].detail


def test_source_summary_draft_validation_rejects_source_framing_bullets() -> None:
    plan = _source_summary_plan(selected_source_claims=("source-claim-unit-0001-0001",))
    draft = SourceSummaryDraft(
        source_record_text="Source record for [[alpha]]. (raw/alpha.md)",
        claim_bullets=(
            SourceSummaryBullet(
                "The source discusses alpha behavior. (raw/alpha.md)",
                ("source-claim-unit-0001-0001",),
            ),
        ),
    )

    assert [finding.finding_type for finding in validate_source_summary_draft(draft, plan)] == [
        "SourceFramingBullet"
    ]


def test_source_summary_citation_matching_normalizes_unicode_dashes() -> None:
    plan = SourceSummaryPlan(
        source_summary_plan_id="source-summary-plan-book",
        page_id="book-front-matter",
        selected_source_claims=("source-claim-unit-0001-0001",),
        required_source_citations=("raw/book.pdf p.1-7",),
    )
    draft = SourceSummaryDraft(
        source_record_text="Source record for [[book-front-matter]].",
        claim_bullets=(
            SourceSummaryBullet(
                "The front matter is summarized with a nonbreaking page dash (raw/book.pdf p.1‑7).",
                ("source-claim-unit-0001-0001",),
            ),
        ),
    )

    assert validate_source_summary_draft(draft, plan) == ()


def test_source_summary_citation_matching_accepts_contained_page_locator() -> None:
    plan = SourceSummaryPlan(
        source_summary_plan_id="source-summary-plan-book",
        page_id="book-resistance-rolls",
        selected_source_claims=("source-claim-unit-0001-0001",),
        required_source_citations=("raw/book.pdf p.33-36",),
    )
    draft = SourceSummaryDraft(
        source_record_text="Source record for [[book-resistance-rolls]].",
        claim_bullets=(
            SourceSummaryBullet(
                "Resistance rolls use a baseline score. (raw/book.pdf p.36)",
                ("source-claim-unit-0001-0001",),
            ),
        ),
    )

    assert validate_source_summary_draft(draft, plan) == ()


@pytest.mark.parametrize(
    "bullet_text",
    (
        "The cited page falls outside the planned source span. (raw/book.pdf p.40)",
        "The cited source is not the planned source. (raw/other-book.pdf p.36)",
        "The cited span extends outside the planned source span. (raw/book.pdf p.35-37)",
    ),
)
def test_source_summary_citation_matching_rejects_outside_locators(bullet_text: str) -> None:
    plan = SourceSummaryPlan(
        source_summary_plan_id="source-summary-plan-book",
        page_id="book-resistance-rolls",
        selected_source_claims=("source-claim-unit-0001-0001",),
        required_source_citations=("raw/book.pdf p.33-36",),
    )
    draft = SourceSummaryDraft(
        source_record_text="Source record for [[book-resistance-rolls]].",
        claim_bullets=(
            SourceSummaryBullet(
                bullet_text,
                ("source-claim-unit-0001-0001",),
            ),
        ),
    )

    findings = validate_source_summary_draft(draft, plan)

    assert [finding.finding_type for finding in findings] == ["SourceSummaryBulletCitation"]


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


def test_planned_source_summary_tool_accepts_single_selected_claim(paths: WikiPaths) -> None:
    source_text = (
        "# Composing and Decomposing Data\n\n"
        "Recursion is foundational to computation because it trades description for time."
    )
    (paths.raw_dir / "recursion.md").write_text(source_text, encoding="utf-8")
    store = WikiStore(paths)
    raw_source = RawSource.from_locator("recursion.md")
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
    selected_claims = planned_write.source_summary_plan.selected_source_claims
    assert selected_claims == ("source-claim-unit-0001-0001",)
    tool = planned_write_page_tool(store, TODAY, planned_write)

    result = tool.callable(
        source_record_text="Chapter opener introduces recursion. (raw/recursion.md)",
        claim_bullets=[
            {
                "bullet_text": (
                    "Recursion can trade compact descriptions for computation time. "
                    "(raw/recursion.md)"
                ),
                "covered_source_claims": [selected_claims[0]],
            },
        ],
    )

    assert "Wrote wiki/recursion.md" in result
    assert store.read_page("recursion").count("\n- ") == 1


def test_planned_source_summary_tool_rejects_copy_only_drafts(paths: WikiPaths) -> None:
    source_text = (
        "# Alpha\n\n"
        "Alpha beta gamma delta epsilon zeta eta theta iota. "
        "The alpha record was recovered from a dated archive. "
        "Researchers used tomography to read hidden inscriptions."
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
    tool = planned_write_page_tool(store, TODAY, planned_write)

    with pytest.raises(WikiStoreError, match="CopiedSourcePhrase") as exc:
        tool.callable(
            source_record_text="Alpha beta gamma delta epsilon zeta eta theta iota.",
            claim_bullets=[
                {
                    "bullet_text": (
                        "Alpha beta gamma delta epsilon zeta eta theta iota. (raw/alpha.md)"
                    ),
                    "covered_source_claims": [selected_claims[0]],
                },
                {
                    "bullet_text": (
                        "The alpha record was recovered from a dated archive. (raw/alpha.md)"
                    ),
                    "covered_source_claims": [selected_claims[1]],
                },
                {
                    "bullet_text": (
                        "Researchers used tomography to read hidden inscriptions. (raw/alpha.md)"
                    ),
                    "covered_source_claims": [selected_claims[2]],
                },
            ],
        )

    assert "source_record_text copies source phrase" in str(exc.value)
    assert "avoid copied phrases" in str(exc.value)
    assert store.list_pages() == []


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


def test_planned_source_summary_tool_rejects_too_many_claim_bullets(
    paths: WikiPaths,
) -> None:
    source_text = (
        "Alpha measures orbital events. "
        "Beta records workshop evidence. "
        "Gamma preserves later research notes."
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
    selected_claims = page_plan.planned_writes[0].source_summary_plan.selected_source_claims
    tool = planned_write_page_tool(store, TODAY, page_plan.planned_writes[0])

    with pytest.raises(WikiStoreError, match="at most 5 markdown bullet claims"):
        tool.callable(
            source_record_text="Compact alpha source summary. (raw/alpha.md)",
            claim_bullets=[
                {
                    "bullet_text": f"Compact claim label {index}. (raw/alpha.md)",
                    "covered_source_claims": [selected_claims[index % len(selected_claims)]],
                }
                for index in range(6)
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
