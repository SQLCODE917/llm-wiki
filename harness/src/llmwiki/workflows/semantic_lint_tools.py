"""Tools used only by the semantic-lint workflow."""

from __future__ import annotations

from forge.core.workflow import ToolDef, ToolSpec
from pydantic import BaseModel, Field

from llmwiki.domain.semantic_lint import SemanticFinding, SemanticFindingKind
from llmwiki.store import WikiStore, WikiStoreError


class RecordSemanticFindingParams(BaseModel):
    kind: SemanticFindingKind = Field(
        description="One of: stale_claim, possible_supersession, data_gap."
    )
    affected_pages: list[str] = Field(description="Existing wiki pages the finding concerns.")
    rationale: str = Field(description="Why this is a semantic maintenance lead.")
    evidence_consulted: str = Field(description="Pages/claims/evidence consulted.")
    recommended_action: str = Field(description="Curator-facing next action.")


def record_semantic_finding_tool(
    store: WikiStore, findings: list[SemanticFinding]
) -> ToolDef:
    """Record one structured semantic lint finding; never edits wiki pages."""

    def _record_semantic_finding(**kwargs: object) -> str:
        params = RecordSemanticFindingParams(**kwargs)  # type: ignore[arg-type]
        if not params.affected_pages:
            raise WikiStoreError("Semantic findings must reference at least one existing page.")
        existing = set(store.list_pages())
        missing = sorted(set(params.affected_pages) - existing)
        if missing:
            raise WikiStoreError(
                "Semantic findings must reference existing pages. "
                f"Missing: {', '.join(missing)}."
            )
        finding = SemanticFinding(
            kind=params.kind,
            affected_pages=tuple(dict.fromkeys(params.affected_pages)),
            rationale=params.rationale,
            evidence_consulted=params.evidence_consulted,
            recommended_action=params.recommended_action,
        )
        findings.append(finding)
        return f"Recorded semantic lint finding: {params.kind}."

    return ToolDef(
        spec=ToolSpec(
            name="record_semantic_finding",
            description="Record a structured stale-claim, supersession, or data-gap finding.",
            parameters=RecordSemanticFindingParams,
        ),
        callable=_record_semantic_finding,
    )
