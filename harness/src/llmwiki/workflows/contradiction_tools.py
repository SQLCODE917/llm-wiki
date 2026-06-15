"""Tools used only by the contradiction-audit workflow."""

from __future__ import annotations

from forge.core.workflow import ToolDef, ToolSpec
from pydantic import BaseModel, Field

from llmwiki.domain.contradictions import ContradictionFinding, ContradictionSeverity
from llmwiki.store import WikiStore, WikiStoreError


class RecordContradictionParams(BaseModel):
    page_a: str = Field(description="First existing wiki page name.")
    claim_a: str = Field(description="Concise claim summary from page_a.")
    page_b: str = Field(description="Second existing wiki page name.")
    claim_b: str = Field(description="Concise claim summary from page_b.")
    severity: ContradictionSeverity = Field(description="Severity: low, medium, or high.")
    rationale: str = Field(description="Why the two claims cannot both be true as written.")
    recommended_action: str = Field(description="Curator-facing next action.")


def record_contradiction_tool(store: WikiStore, findings: list[ContradictionFinding]) -> ToolDef:
    """Record one structured contradiction finding; never edits wiki pages."""

    def _record_contradiction(**kwargs: object) -> str:
        params = RecordContradictionParams(**kwargs)  # type: ignore[arg-type]
        if params.page_a == params.page_b:
            raise WikiStoreError("page_a and page_b must be different pages.")
        existing = set(store.list_pages())
        missing = sorted({params.page_a, params.page_b} - existing)
        if missing:
            raise WikiStoreError(
                "Contradiction findings must reference existing pages. "
                f"Missing: {', '.join(missing)}."
            )
        finding = ContradictionFinding(
            page_a=params.page_a,
            claim_a=params.claim_a,
            page_b=params.page_b,
            claim_b=params.claim_b,
            severity=params.severity,
            rationale=params.rationale,
            recommended_action=params.recommended_action,
        )
        findings.append(finding)
        return f"Recorded contradiction candidate: {params.page_a} vs {params.page_b}."

    return ToolDef(
        spec=ToolSpec(
            name="record_contradiction",
            description="Record a structured contradiction candidate after reading "
            "the relevant pages. Use only when the claims cannot both be true as written.",
            parameters=RecordContradictionParams,
        ),
        callable=_record_contradiction,
    )
