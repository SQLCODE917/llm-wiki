"""ConfidencePolicy: maps source-neutral extraction signals to confidence.

Confidence is the confidence that a ledger entry faithfully represents source
text. It does not score whether the source is true. Claim-like entries with
low confidence become needs-review. Exact-preservation atoms can be usable at
medium confidence when their exact source payload is preserved.
"""

from __future__ import annotations

from dataclasses import dataclass

from llmwiki.domain.ledger.common import ConfidenceBasis


@dataclass(frozen=True)
class ConfidenceSignals:
    evidence_resolved: bool
    required_fields_complete: bool
    validation_passed: bool
    ambiguity_present: bool = False
    anchors_resolved: bool = True
    competing_candidates: bool = False
    ranker_in_range: bool = True
    exact_payload_preserved: bool = False


@dataclass(frozen=True)
class ConfidencePolicy:
    """Deterministic policy mapping extraction signals to confidence + status."""

    def assess(self, signals: ConfidenceSignals) -> tuple[str, ConfidenceBasis]:
        base_complete = (
            signals.evidence_resolved
            and signals.required_fields_complete
            and signals.validation_passed
            and signals.ranker_in_range
        )
        fully_clean = (
            base_complete
            and not signals.ambiguity_present
            and signals.anchors_resolved
            and not signals.competing_candidates
        )
        if fully_clean:
            return "high", ConfidenceBasis(
                "evidence-resolved-required-complete-validated", _signals(signals)
            )
        if base_complete and not signals.ambiguity_present:
            return "medium", ConfidenceBasis("optional-interpretation-partial", _signals(signals))
        if signals.exact_payload_preserved and base_complete:
            return "medium", ConfidenceBasis("exact-payload-preserved", _signals(signals))
        return "low", ConfidenceBasis("interpretation-unsafe", _signals(signals))

    def status_for(self, confidence: str) -> str:
        return "needs-review" if confidence == "low" else "usable"


def _signals(signals: ConfidenceSignals) -> tuple[str, ...]:
    flags = (
        ("evidence-resolved", signals.evidence_resolved),
        ("required-fields-complete", signals.required_fields_complete),
        ("validation-passed", signals.validation_passed),
        ("ambiguity-present", signals.ambiguity_present),
        ("anchors-resolved", signals.anchors_resolved),
        ("competing-candidates", signals.competing_candidates),
        ("ranker-in-range", signals.ranker_in_range),
        ("exact-payload-preserved", signals.exact_payload_preserved),
    )
    return tuple(name for name, present in flags if present)
