from llmwiki.domain.ledger.features import profile_unit


def test_profile_unit_bounds_pathological_lines() -> None:
    profile = profile_unit(
        extracted_unit_id="unit-long",
        source_range_id="source-range-long",
        text=("word  " * 50_000) + "\n| Roll | Result |\n| 2 | Miss |",
        evidence_ids=("evidence-long",),
    )

    signals = {signal.feature_signal_kind: signal for signal in profile.feature_signals}
    assert signals["table-density"].feature_signal_value > 0
    assert set(signals) == {
        "table-density",
        "code-density",
        "formula-density",
        "figure-density",
        "entity-date-density",
        "rule-language-density",
        "procedure-density",
        "definition-density",
        "relationship-density",
    }
