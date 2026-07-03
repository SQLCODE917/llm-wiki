"""Tests for source-neutral source-scope boundary detection."""

from pathlib import Path

from llmwiki.domain.source_scope import is_source_scope_transition


def test_source_scope_transition_detection_is_source_neutral() -> None:
    assert is_source_scope_transition("We have not introduced the archival mode yet.")
    assert is_source_scope_transition(
        "Readers will examine the secondary clause in the following section."
    )


def test_source_scope_transition_ignores_subject_matter_not_yet() -> None:
    assert not is_source_scope_transition(
        "The detector has not yet encountered a thermal limit during testing."
    )


def test_scope_logic_avoids_regression_source_particulars() -> None:
    root = Path(__file__).resolve().parents[1] / "src" / "llmwiki" / "domain"
    production_text = "\n".join(
        (root / filename).read_text()
        for filename in (
            "source_scope.py",
            "planning.py",
            "claim_support_selection.py",
        )
    ).lower()

    for forbidden in (
        "fourth possibility",
        "serial number",
        "same kind of cup",
        "value cups",
        "javascriptallonge",
    ):
        assert forbidden not in production_text
