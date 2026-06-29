from llmwiki.domain.ledger.extraction import ExtractedUnitProfile, FeatureSignal
from llmwiki.domain.ledger.extractors import _decision_signal_ids


def test_decision_signal_ids_are_bounded() -> None:
    profile = ExtractedUnitProfile(
        extracted_unit_id="segment-1",
        source_range_id="range-1",
        feature_signals=tuple(_signal(index) for index in range(100)),
    )

    signal_ids = _decision_signal_ids(profile)

    assert len(signal_ids) == 32
    assert signal_ids[0] == "signal-0"
    assert signal_ids[-1] == "signal-31"


def _signal(index: int) -> FeatureSignal:
    return FeatureSignal(
        feature_signal_id=f"signal-{index}",
        feature_signal_kind="kind",
        feature_signal_value=0.0,
        feature_signal_confidence="low",
        source_range_id="range-1",
    )
