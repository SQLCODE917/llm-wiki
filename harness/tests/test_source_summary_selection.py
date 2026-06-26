"""Regression tests for source-summary claim selection edge cases."""

from llmwiki.domain.objects import ExtractedUnit, RawSource, Schema, SourceClaim
from llmwiki.domain.page_body_contracts import contract_for_page_kind, resolve_page_body_contract
from llmwiki.domain.source_claim_quality import claim_eligibility, claim_role_tags
from llmwiki.domain.source_claims import source_claim_groups, source_claims
from llmwiki.domain.source_summary_planning import source_summary_plan


def test_created_by_domain_claim_is_not_source_furniture() -> None:
    statement = "Special procedures created by the engine host can update running tasks."
    roles = claim_role_tags(statement)

    assert claim_eligibility(statement, roles) == "eligible"


def test_source_summary_catalog_focus_expands_to_substantive_claims() -> None:
    raw_source = RawSource.from_locator("book.pdf")
    units = (
        ExtractedUnit(
            "unit-0001",
            raw_source,
            "p.1",
            "Special widgets",
            (
                "Here is a list of special widgets created by each workshop.\n\n"
                "Users of special widgets can use basic tools and special widgets created "
                "by their workshop.\n\n"
                "**[ Alpha ] (Widget Level=1)**\n\n"
                "Base Cost=3 Distance=touch\n\n"
                "Area=One Duration=instant\n\n"
                "Mode=single target\n\n"
                "Alpha closes the active resource when traversal completes.\n\n"
                "Alpha returns successive values through calls to next.\n\n"
                "Alpha must release the handle after completion."
            ),
            "ok",
        ),
    )
    claims = source_claims(units, Schema())
    contract = resolve_page_body_contract(contract_for_page_kind(Schema(), "source"))

    plan = source_summary_plan(
        page_id="book-special-widgets",
        contract=contract,
        claims=claims,
        groups=source_claim_groups(claims),
    )
    assert plan is not None

    selected = _selected_claims(claims, plan.selected_source_claims)
    assert all(claim.claim_eligibility == "eligible" for claim in selected)
    assert len(selected) >= 3
    assert any(claim.statement.startswith("Alpha ") for claim in selected)


def test_relevant_source_furniture_role_claim_still_filters_through_eligibility() -> None:
    raw_source = RawSource.from_locator("book.pdf")
    units = (
        ExtractedUnit(
            "unit-0001",
            raw_source,
            "p.1",
            "Resistance rolls",
            (
                "Resistance rolls avoid poison and magic effects.\n\n"
                "To the right of each of these is a field to write down the bonus, "
                "and further to the right of that should be a field labeled resistance.\n\n"
                "Mental resistance rolls compare mental power against magical effects."
            ),
            "ok",
        ),
    )
    claims = source_claims(units, Schema())
    contract = resolve_page_body_contract(contract_for_page_kind(Schema(), "source"))

    plan = source_summary_plan(
        page_id="book-resistance-rolls",
        contract=contract,
        claims=claims,
        groups=source_claim_groups(claims),
    )
    assert plan is not None

    selected = _selected_claims(claims, plan.selected_source_claims)
    assert selected
    assert all(claim.claim_eligibility == "eligible" for claim in selected)


def test_source_summary_focus_prefers_strong_title_overlap() -> None:
    raw_source = RawSource.from_locator("book.pdf")
    units = (
        ExtractedUnit(
            "unit-0001",
            raw_source,
            "p.10-12",
            "Surprise Attacks",
            (
                "A referee must announce enemy action fairly.\n\n"
                "The referee cannot change an attack after a character used a spell.\n\n"
                "A later section begins after this neighboring rule.\n\n"
                "Surprise Attacks\n\n"
                "A surprise attack occurs when one side notices another side first.\n\n"
                "The Surprise Attack Check compares monster and adventurer results.\n\n"
                "Surprise attack modifiers decide which side may act first.\n\n"
                "Surprised combatants cannot take assertive actions."
            ),
            "ok",
        ),
    )
    claims = source_claims(units, Schema())
    contract = resolve_page_body_contract(contract_for_page_kind(Schema(), "source"))

    plan = source_summary_plan(
        page_id="book-surprise-attacks",
        contract=contract,
        claims=claims,
        groups=source_claim_groups(claims),
    )
    assert plan is not None

    selected = _selected_claims(claims, plan.selected_source_claims)
    selected_text = " ".join(claim.statement for claim in selected)
    assert "character used a spell" not in selected_text
    assert "Surprise Attack Check" in selected_text


def test_source_summary_focus_ignores_very_late_strong_overlap() -> None:
    raw_source = RawSource.from_locator("book.pdf")
    filler = "\n\n".join(f"Catalog entry {index} has ordinary details." for index in range(25))
    units = (
        ExtractedUnit(
            "unit-0001",
            raw_source,
            "p.20-30",
            "Mythical Beasts and Magical Beasts",
            (
                "A ceiling hanger is a magical beast with unusual arms.\n\n"
                "The catalog gives habitat and combat notes for many entries.\n\n"
                f"{filler}\n\n"
                "Androscorpio is a mythical beast with a scorpion body.\n\n"
                "In combat, an androscorpio uses a sword and tail together."
            ),
            "ok",
        ),
    )
    claims = source_claims(units, Schema())
    contract = resolve_page_body_contract(contract_for_page_kind(Schema(), "source"))

    plan = source_summary_plan(
        page_id="book-mythical-beasts-and-magical-beasts-part-1",
        contract=contract,
        claims=claims,
        groups=source_claim_groups(claims),
    )
    assert plan is not None

    selected = _selected_claims(claims, plan.selected_source_claims)
    selected_text = " ".join(claim.statement for claim in selected)
    assert "ceiling hanger" in selected_text
    assert not all("Androscorpio" in claim.statement for claim in selected)


def test_source_summary_broad_catalog_spreads_selected_claims() -> None:
    raw_source = RawSource.from_locator("book.pdf")
    units = (
        ExtractedUnit(
            "unit-0001",
            raw_source,
            "p.76-79",
            "Ancient Magic List",
            (
                "Vision improves sight over long distances.\n\n"
                "Flight lets the caster fly at travel speed.\n\n"
                "Blizzard creates an ice storm that deals cold damage.\n\n"
                "Acid Cloud creates acidic gas in an area.\n\n"
                "Geas imposes a magical prohibition on a target.\n\n"
                "Create Undead animates a corpse as an undead servant.\n\n"
                "Teleport moves targets to a visible or familiar place.\n\n"
                "Full Potential raises several physical scores.\n\n"
                "Blade Net catches a target in cutting strands.\n\n"
                "Bend Bar warps a bar-shaped object.\n\n"
                "Polymorph changes a target into an animal form.\n\n"
                "Magic Reflection reflects magic cast on the caster.\n\n"
                "Analyze Enchantment identifies power placed on an object.\n\n"
                "Geas pain punishes a target who violates a command.\n\n"
                "Create Undead requires a corpse for the servant.\n\n"
                "See-Through lets the caster inspect a blocked area.\n\n"
                "Seal Enchantment hides power on an object.\n\n"
                "Steal Mind transfers mental power from a target.\n\n"
                "Slow halves a target's agility for its duration.\n\n"
                "Haste doubles a target's agility for its duration.\n\n"
                "Rune Rope binds a target with invisible force.\n\n"
                "Dispel Order removes command effects from a target.\n\n"
                "Telekinesis moves an object by concentration.\n\n"
                "Magic Staff creates a mage staff for ancient spell work.\n\n"
                "A wooden staff can become a mage staff with this spell.\n\n"
                "The spell can create another magical catalyst instead of a staff."
            ),
            "ok",
        ),
    )
    claims = source_claims(units, Schema())
    contract = resolve_page_body_contract(contract_for_page_kind(Schema(), "source"))

    plan = source_summary_plan(
        page_id="book-ancient-magic-list-3",
        contract=contract,
        claims=claims,
        groups=source_claim_groups(claims),
    )
    assert plan is not None

    selected = _selected_claims(claims, plan.selected_source_claims)
    selected_text = " ".join(claim.statement for claim in selected)
    assert len(selected) == 5
    assert "Vision" in selected_text or "Flight" in selected_text
    assert "Magic Staff" in selected_text
    assert sum("staff" in claim.statement.lower() for claim in selected) < 3


def test_source_summary_selection_skips_low_centrality_worked_examples() -> None:
    raw_source = RawSource.from_locator("book.pdf")
    units = (
        ExtractedUnit(
            "unit-0001",
            raw_source,
            "p.40-44",
            "Undead",
            (
                "Undead resist poison and illness.\n\n"
                "Skeletons attack intruders without fear.\n\n"
                "Ghosts ignore ordinary weapons.\n\n"
                "Therefore, they will best be handled by experienced heroes."
            ),
            "ok",
        ),
    )
    claims = source_claims(units, Schema())
    contract = resolve_page_body_contract(contract_for_page_kind(Schema(), "source"))

    plan = source_summary_plan(
        page_id="book-undead-part-1",
        contract=contract,
        claims=claims,
        groups=source_claim_groups(claims),
    )
    assert plan is not None

    selected = _selected_claims(claims, plan.selected_source_claims)
    selected_text = " ".join(claim.statement for claim in selected)
    assert "best be handled" not in selected_text
    assert "Undead resist poison" in selected_text


def _selected_claims(
    claims: tuple[SourceClaim, ...], selected_ids: tuple[str, ...]
) -> tuple[SourceClaim, ...]:
    claims_by_id = {claim.source_claim_id: claim for claim in claims}
    return tuple(claims_by_id[claim_id] for claim_id in selected_ids)
