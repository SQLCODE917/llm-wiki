"""Tools used only by the grounding-audit workflow."""

from __future__ import annotations

from collections.abc import Sequence

from forge.core.workflow import ToolDef, ToolSpec
from pydantic import BaseModel, Field

from llmwiki.domain.grounding import ClaimCandidate, GroundingVerdict, GroundingVerdictLabel
from llmwiki.store import WikiStore, WikiStoreError


class RecordGroundingVerdictParams(BaseModel):
    page_name: str = Field(description="Existing wiki page containing the claim.")
    claim_text: str = Field(description="The claim being judged.")
    verdict: GroundingVerdictLabel = Field(
        description="One of: supported, too_broad, not_supported, unclear."
    )
    rationale: str = Field(description="Why the evidence does or does not support the claim.")
    recommended_action: str = Field(description="Curator-facing next action.")


def record_grounding_verdict_tool(
    store: WikiStore,
    verdicts: list[GroundingVerdict],
    candidates: Sequence[ClaimCandidate] = (),
) -> ToolDef:
    """Record one structured grounding verdict; never edits wiki pages."""

    candidate_map = {
        (candidate.page_name, candidate.claim_text): candidate for candidate in candidates
    }

    def _record_grounding_verdict(**kwargs: object) -> str:
        params = RecordGroundingVerdictParams(**kwargs)  # type: ignore[arg-type]
        if params.page_name not in store.list_pages():
            raise WikiStoreError(
                "Grounding verdicts must reference existing pages. "
                f"Missing: {params.page_name}."
            )
        candidate = candidate_map.get((params.page_name, params.claim_text))
        if candidate_map and candidate is None:
            raise WikiStoreError(
                "Grounding verdicts must reference one of the selected claim candidates."
            )
        if (
            candidate is not None
            and candidate.evidence_excerpt.startswith("No normalized evidence excerpt")
            and params.verdict != "unclear"
        ):
            raise WikiStoreError(
                "Claims without a resolved evidence excerpt must be recorded as unclear."
            )
        verdicts.append(
            GroundingVerdict(
                page_name=params.page_name,
                claim_text=params.claim_text,
                verdict=params.verdict,
                rationale=params.rationale,
                recommended_action=params.recommended_action,
            )
        )
        return f"Recorded grounding verdict for {params.page_name}: {params.verdict}."

    return ToolDef(
        spec=ToolSpec(
            name="record_grounding_verdict",
            description="Record a structured support verdict for one selected claim.",
            parameters=RecordGroundingVerdictParams,
        ),
        callable=_record_grounding_verdict,
    )
