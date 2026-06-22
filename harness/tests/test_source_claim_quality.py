"""Tests for deterministic source-claim quality planning."""

from dataclasses import replace

from source_claim_quality_fixtures import fixtures as _fixtures

from llmwiki.domain.objects import (
    ExtractedUnit,
    RawSource,
    Schema,
    SourceBundle,
)
from llmwiki.domain.page_body_contracts import contract_for_page_kind, resolve_page_body_contract
from llmwiki.domain.pages import LOCAL_FLAT_STRUCTURE
from llmwiki.domain.planning import (
    build_page_plan,
    source_summary_quality_report,
)
from llmwiki.domain.source_claim_quality import (
    claim_eligibility as _claim_eligibility,
)
from llmwiki.domain.source_claim_quality import (
    claim_role_tags as _claim_role_tags,
)
from llmwiki.domain.source_claims import source_claim_groups, source_claims
from llmwiki.domain.source_summary_planning import source_summary_plan


def test_source_claim_quality_fixture_accuracy() -> None:
    fixtures = _fixtures()
    assert sum(1 for item in fixtures if item.source_locator == "javascriptallonge.pdf") >= 80
    assert sum(1 for item in fixtures if item.source_locator == "antikythera-mechanism.md") >= 20
    assert sum(1 for item in fixtures if item.source_locator == "sword-world.pdf") >= 20

    correct = 0
    possible = 0
    for fixture in fixtures:
        roles = _claim_role_tags(fixture.statement)
        eligibility = _claim_eligibility(fixture.statement, roles)
        possible += 1
        if eligibility == fixture.expected_claim_eligibility:
            correct += 1
        for expected_role in fixture.expected_claim_role_tags:
            possible += 1
            if expected_role in roles:
                correct += 1

    assert correct / possible >= 0.90


def test_claim_role_tags_handles_long_source_sentences() -> None:
    statement = "Functions return values. " + ("unpunctuated source text " * 2000)

    roles = _claim_role_tags(statement)

    assert "function" in roles


def test_layout_field_claims_are_source_furniture() -> None:
    statement = "To the right of each of these is a field labeled resistance."
    roles = _claim_role_tags(statement)

    assert _claim_eligibility(statement, roles) == "source-furniture"


def test_source_claims_bounds_long_unpunctuated_units() -> None:
    long_text = "Functions return values. " + ("unpunctuated source text " * 5000)

    claims = source_claims((_unit("unit-0001", "Long text", long_text),), Schema())

    assert claims
    assert all(len(claim.statement) <= 1800 for claim in claims)
    assert len(claims) <= 120


def test_source_summary_plan_selects_eligible_claim_over_analogy() -> None:
    plan = _plan_for_units(
        (
            _unit(
                "unit-0001",
                "Object.assign",
                (
                    "Closures are similar to backpacks that carry bindings for a function. "
                    "Object.assign copies enumerable properties into a target object."
                ),
            ),
        )
    )
    source_write = next(
        write for write in plan.planned_writes if write.page_metadata.page_id != "book"
    )
    selected = _selected_claims(plan, source_write.source_summary_plan.selected_source_claims)

    assert selected[0].claim_eligibility == "eligible"
    assert selected[0].statement.startswith("Object.assign")


def test_source_summary_plan_selects_eligible_claim_over_code_fragment() -> None:
    plan = _plan_for_units(
        (
            _unit(
                "unit-0001",
                "Map",
                (
                    "const result = values.map(value => value * value);\n\n"
                    "Map transforms each element with a callback function."
                ),
            ),
        )
    )
    source_write = next(
        write for write in plan.planned_writes if write.page_metadata.page_id != "book"
    )
    selected = _selected_claims(plan, source_write.source_summary_plan.selected_source_claims)

    assert selected[0].claim_eligibility == "eligible"
    assert selected[0].statement.startswith("Map transforms")


def test_source_summary_plan_skips_source_furniture_when_unit_has_eligible_claim() -> None:
    plan = _plan_for_units(
        (
            _unit(
                "unit-0001",
                "Iterator close",
                (
                    "Copyright 2016 by the author. "
                    "The iterator closes the resource when traversal completes."
                ),
            ),
        )
    )
    source_write = next(
        write for write in plan.planned_writes if write.page_metadata.page_id != "book"
    )
    selected = _selected_claims(plan, source_write.source_summary_plan.selected_source_claims)

    assert selected
    assert all(claim.claim_eligibility == "eligible" for claim in selected)


def test_source_summary_plan_skips_transition_frame_when_unit_has_eligible_claims() -> None:
    plan = _plan_for_units(
        (
            _unit(
                "unit-0001",
                "truthiness and the ternary operator",
                (
                    "Truthiness controls how logical operators evaluate JavaScript values. "
                    "We'll look at them in a moment, but first, we'll look at one more operator. "
                    "The ternary operator takes three arguments."
                ),
            ),
        )
    )
    source_write = next(
        write for write in plan.planned_writes if write.page_metadata.page_id != "book"
    )
    selected = _selected_claims(plan, source_write.source_summary_plan.selected_source_claims)

    assert selected
    assert all(claim.claim_eligibility != "narrative-frame" for claim in selected)
    assert any("ternary operator" in claim.statement for claim in selected)


def test_source_summary_plan_covers_one_eligible_claim_per_unit_for_small_pages() -> None:
    raw_source = RawSource.from_locator("book.pdf")
    units = (
        ExtractedUnit(
            "unit-0001",
            raw_source,
            "p.1",
            "Closures",
            "Closures remember bindings from an outer lexical scope.",
            "ok",
        ),
        ExtractedUnit(
            "unit-0002",
            raw_source,
            "p.2",
            "Iterators",
            "Iterators return successive values through calls to next.",
            "ok",
        ),
    )
    schema = Schema()
    claims = source_claims(units, schema)
    contract = resolve_page_body_contract(contract_for_page_kind(schema, "source"))
    plan = source_summary_plan(
        page_id="book-closures-to-iterators",
        contract=contract,
        claims=claims,
        groups=source_claim_groups(claims),
    )
    selected = _selected_claims_from_claims(claims, plan.selected_source_claims)

    assert {claim.extracted_unit_id for claim in selected} == {"unit-0001", "unit-0002"}
    assert all(claim.claim_eligibility == "eligible" for claim in selected)


def test_source_summary_plan_separates_ordinary_modality_from_source_uncertainty() -> None:
    ordinary_plan = _plan_for_units(
        (
            _unit(
                "unit-0001",
                "Map",
                "A caller may pass a function to map in order to transform each element.",
            ),
        )
    )
    ordinary_write = next(
        write for write in ordinary_plan.planned_writes if write.page_metadata.page_id != "book"
    )
    assert ordinary_write.source_summary_plan is not None
    assert "ordinary-modality" in ordinary_write.source_summary_plan.required_claim_role_tags
    assert "source-uncertainty" not in ordinary_write.source_summary_plan.required_claim_role_tags
    assert ordinary_write.resolved_page_body_contract.required_uncertainty_terms == ()

    uncertainty_plan = _plan_for_units(
        (
            _unit(
                "unit-0001",
                "Iterator close",
                "The source does not specify whether the iterator closes the resource.",
            ),
        )
    )
    uncertainty_write = next(
        write for write in uncertainty_plan.planned_writes if write.page_metadata.page_id != "book"
    )
    assert uncertainty_write.source_summary_plan is not None
    assert "source-uncertainty" in uncertainty_write.source_summary_plan.required_claim_role_tags
    assert uncertainty_write.resolved_page_body_contract.required_uncertainty_terms


def test_source_summary_quality_report_counts_deterministic_failures() -> None:
    plan = _plan_for_units(
        (
            _unit("unit-0001", "Functions", "Functions are values."),
            _unit("unit-0002", "Closures", "Closures remember lexical bindings."),
        )
    )
    clean_report = source_summary_quality_report(plan, {})
    assert clean_report.selected_ineligible_claims == 0
    assert clean_report.false_source_uncertainty_claims == 0
    assert clean_report.missing_unit_coverage == 0

    dirty_report = source_summary_quality_report(
        plan,
        {
            "book-functions": (
                "## Key supported claims\n\n"
                "- The source discusses functions and closures. (raw/book.pdf)"
            )
        },
    )
    assert dirty_report.source_framing_bullets == 1

    bad_claim = replace(plan.source_claims[0], claim_certainty="uncertain")
    bad_plan = replace(plan, source_claims=(bad_claim,) + plan.source_claims[1:])
    false_uncertainty_report = source_summary_quality_report(bad_plan, {})
    assert false_uncertainty_report.false_source_uncertainty_claims == 1


def _plan_for_units(units: tuple[ExtractedUnit, ...]):
    raw_source = units[0].raw_source
    return build_page_plan(
        plan_id="test-plan",
        source_bundle=SourceBundle.one(raw_source),
        raw_source=raw_source,
        extracted_units=units,
        existing_pages={},
        wiki_structure=LOCAL_FLAT_STRUCTURE,
        today="2026-06-20",
    )


def _unit(unit_id: str, heading_path: str, text: str) -> ExtractedUnit:
    raw_source = RawSource.from_locator("book.pdf")
    return ExtractedUnit(unit_id, raw_source, unit_id, heading_path, text, "ok")


def _selected_claims(plan, selected_ids: tuple[str, ...]):
    return _selected_claims_from_claims(plan.source_claims, selected_ids)


def _selected_claims_from_claims(claims, selected_ids: tuple[str, ...]):
    claims_by_id = {claim.source_claim_id: claim for claim in claims}
    return tuple(claims_by_id[claim_id] for claim_id in selected_ids)
