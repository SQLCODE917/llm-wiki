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


def _selected_claims(
    claims: tuple[SourceClaim, ...], selected_ids: tuple[str, ...]
) -> tuple[SourceClaim, ...]:
    claims_by_id = {claim.source_claim_id: claim for claim in claims}
    return tuple(claims_by_id[claim_id] for claim_id in selected_ids)
