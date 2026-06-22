"""Tools used only by the claim-support audit workflow."""

from __future__ import annotations

from collections.abc import Sequence

from forge.core.workflow import ToolDef, ToolSpec
from pydantic import BaseModel, Field

from llmwiki.domain.claim_support import (
    ClaimSupportCandidate,
    ClaimSupportFinding,
    ClaimSupportVerdict,
    ClaimSupportVerdictLabel,
)
from llmwiki.store import WikiStore, WikiStoreError


class RecordClaimSupportVerdictParams(BaseModel):
    candidate_id: str = Field(description="ClaimSupportCandidate id being judged.")
    verdict: ClaimSupportVerdictLabel = Field(
        description="One of: supported, too_broad, not_supported, unclear."
    )
    rationale: str = Field(description="Why the evidence does or does not support the claim.")
    recommended_action: str = Field(description="Curator-facing next action.")


def record_claim_support_verdict_tool(
    store: WikiStore,
    verdicts: list[ClaimSupportVerdict],
    candidates: Sequence[ClaimSupportCandidate],
    deterministic_findings: Sequence[ClaimSupportFinding] = (),
) -> ToolDef:
    """Record one structured claim-support verdict; never edits wiki pages."""

    candidate_map = {candidate.candidate_id: candidate for candidate in candidates}
    blocked = {
        finding.candidate_id
        for finding in deterministic_findings
        if finding.severity == "blocker"
    }

    def _record_claim_support_verdict(**kwargs: object) -> str:
        params = RecordClaimSupportVerdictParams(**kwargs)  # type: ignore[arg-type]
        candidate = candidate_map.get(params.candidate_id)
        if candidate is None:
            raise WikiStoreError(
                "Claim-support verdicts must reference one selected ClaimSupportCandidate."
            )
        if candidate.page_id not in store.list_pages():
            raise WikiStoreError(
                f"ClaimSupportCandidate page is missing: {candidate.page_id}."
            )
        if params.verdict == "supported" and (
            params.candidate_id in blocked or not candidate.evidence_ids
        ):
            raise WikiStoreError(
                "A claim with deterministic findings or no EvidenceRecord cannot be "
                "recorded as supported."
            )
        verdicts.append(
            ClaimSupportVerdict(
                candidate_id=params.candidate_id,
                verdict=params.verdict,
                rationale=params.rationale,
                recommended_action=params.recommended_action,
            )
        )
        return f"Recorded claim-support verdict for {params.candidate_id}: {params.verdict}."

    return ToolDef(
        spec=ToolSpec(
            name="record_claim_support_verdict",
            description="Record a structured support verdict for one selected claim.",
            parameters=RecordClaimSupportVerdictParams,
        ),
        callable=_record_claim_support_verdict,
    )
