"""Select a source-purpose profile from normalized source-map signals."""

from __future__ import annotations

from dataclasses import dataclass

from llmwiki.domain.ledger.features import profile_unit
from llmwiki.domain.source_map import NormalizedSourceMap, SourceBlock
from llmwiki.domain.source_profiles import (
    PROFILE_KINDS,
    SourceProfileArtifact,
    SourceProfileKind,
    default_evidence_vocabularies,
    low_confidence_profile_finding,
    make_source_profile,
)


def select_source_profile(source_map: NormalizedSourceMap) -> SourceProfileArtifact:
    vocabularies = default_evidence_vocabularies()
    signals = _selection_signals(source_map)
    profile_id, score = _select_profile_id(signals)
    confidence = _confidence(profile_id, score)
    vocabulary = vocabularies[profile_id]
    profile = make_source_profile(
        source_map,
        profile_id,
        vocabulary,
        confidence=confidence,
        matched_signals=signals.matched_signals_for(profile_id),
    )
    findings = (low_confidence_profile_finding(profile),) if profile_id == "general-prose" else ()
    return SourceProfileArtifact(profile, vocabulary, findings)


@dataclass(frozen=True)
class _SelectionSignals:
    scores: dict[SourceProfileKind, float]
    matched: dict[SourceProfileKind, tuple[str, ...]]

    def matched_signals_for(self, profile_id: SourceProfileKind) -> tuple[str, ...]:
        return self.matched.get(profile_id, ())


def _selection_signals(source_map: NormalizedSourceMap) -> _SelectionSignals:
    blocks = tuple(block for block in source_map.source_blocks if block.source_text.strip())
    features = _feature_means(blocks)
    block_counts = _block_counts(blocks)
    text = _source_text_sample(source_map, blocks)
    locator = source_map.source_locator.lower()
    scores: dict[SourceProfileKind, float] = {kind: 0.0 for kind in PROFILE_KINDS}
    matched: dict[SourceProfileKind, list[str]] = {kind: [] for kind in PROFILE_KINDS}
    _score_programming(locator, text, features, block_counts, scores, matched)
    _score_rpg(locator, text, features, block_counts, scores, matched)
    _score_reference(features, block_counts, scores, matched)
    return _SelectionSignals(scores, {key: tuple(value) for key, value in matched.items()})


def _select_profile_id(signals: _SelectionSignals) -> tuple[SourceProfileKind, float]:
    candidates: tuple[SourceProfileKind, ...] = ("programming-prose", "rpg-rules", "reference")
    profile_id = max(candidates, key=lambda item: signals.scores[item])
    score = signals.scores[profile_id]
    if score < 2.0:
        return "general-prose", signals.scores["general-prose"]
    return profile_id, score


def _score_programming(
    locator: str,
    text: str,
    features: dict[str, float],
    block_counts: dict[str, int],
    scores: dict[SourceProfileKind, float],
    matched: dict[SourceProfileKind, list[str]],
) -> None:
    content_signal = False
    if block_counts.get("code", 0):
        _add_signal(
            scores,
            matched,
            "programming-prose",
            2.0,
            f"code block count={block_counts['code']}",
        )
        content_signal = True
    if features.get("code-density", 0) >= 0.04:
        _add_signal(
            scores,
            matched,
            "programming-prose",
            1.0,
            f"code-density={features['code-density']:.2f}",
        )
        content_signal = True
    if _contains_any(
        text,
        ("function", "javascript", "prototype", "closure", "const ", "=>", "object"),
    ):
        _add_signal(scores, matched, "programming-prose", 1.0, "programming language terms")
        content_signal = True
    if content_signal and _contains_any(locator, ("javascript", "allonge", ".js")):
        _add_signal(scores, matched, "programming-prose", 0.5, "source locator programming hint")


def _score_rpg(
    locator: str,
    text: str,
    features: dict[str, float],
    block_counts: dict[str, int],
    scores: dict[SourceProfileKind, float],
    matched: dict[SourceProfileKind, list[str]],
) -> None:
    content_signal = False
    if features.get("rule-language-density", 0) >= 0.04:
        _add_signal(
            scores,
            matched,
            "rpg-rules",
            0.8,
            f"rule-language-density={features['rule-language-density']:.2f}",
        )
        content_signal = True
    if features.get("procedure-density", 0) >= 0.03:
        _add_signal(
            scores,
            matched,
            "rpg-rules",
            0.8,
            f"procedure-density={features['procedure-density']:.2f}",
        )
        content_signal = True
    if block_counts.get("table", 0) or features.get("table-density", 0) >= 0.08:
        _add_signal(scores, matched, "rpg-rules", 0.6, "source-map table/rule structure")
        content_signal = True
    if _contains_any(
        text,
        ("rpg", "character", "spell", "magic", "damage", "skill", "dice", "monster"),
    ):
        _add_signal(scores, matched, "rpg-rules", 1.2, "rpg rules terms")
        content_signal = True
    if content_signal and _contains_any(locator, ("rpg", "sword-world", "sword world", "rulebook")):
        _add_signal(scores, matched, "rpg-rules", 0.5, "source locator rpg hint")


def _score_reference(
    features: dict[str, float],
    block_counts: dict[str, int],
    scores: dict[SourceProfileKind, float],
    matched: dict[SourceProfileKind, list[str]],
) -> None:
    if block_counts.get("table", 0):
        _add_signal(scores, matched, "reference", 2.0, f"table block count={block_counts['table']}")
    if features.get("formula-density", 0) >= 0.04:
        _add_signal(
            scores,
            matched,
            "reference",
            1.0,
            f"formula-density={features['formula-density']:.2f}",
        )
    if features.get("definition-density", 0) >= 0.08:
        _add_signal(
            scores,
            matched,
            "reference",
            0.8,
            f"definition-density={features['definition-density']:.2f}",
        )


def _add_signal(
    scores: dict[SourceProfileKind, float],
    matched: dict[SourceProfileKind, list[str]],
    profile_id: SourceProfileKind,
    value: float,
    label: str,
) -> None:
    scores[profile_id] += value
    matched[profile_id].append(label)


def _feature_means(blocks: tuple[SourceBlock, ...]) -> dict[str, float]:
    totals: dict[str, float] = {}
    counts: dict[str, int] = {}
    for block in blocks:
        profile = profile_unit(
            extracted_unit_id=block.source_block_id,
            source_range_id=block.source_block_id,
            text=block.source_text,
            evidence_ids=(block.source_block_id,),
        )
        for signal in profile.feature_signals:
            kind = signal.feature_signal_kind
            totals[kind] = totals.get(kind, 0.0) + signal.feature_signal_value
            counts[kind] = counts.get(kind, 0) + 1
    return {kind: round(value / counts[kind], 4) for kind, value in totals.items() if counts[kind]}


def _block_counts(blocks: tuple[SourceBlock, ...]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for block in blocks:
        counts[block.block_type] = counts.get(block.block_type, 0) + 1
    return counts


def _source_text_sample(source_map: NormalizedSourceMap, blocks: tuple[SourceBlock, ...]) -> str:
    joined = " ".join(
        (
            source_map.source_locator,
            *(block.section_path for block in blocks),
            *(block.source_text for block in blocks),
        )
    )
    return joined[:200_000].lower()


def _contains_any(text: str, needles: tuple[str, ...]) -> bool:
    return any(needle in text for needle in needles)


def _confidence(profile_id: SourceProfileKind, score: float) -> float:
    if profile_id == "general-prose":
        return 0.35
    if score >= 3.0:
        return 0.85
    return 0.7
