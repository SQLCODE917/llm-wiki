"""Workflow tool for validated procedure execution."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from forge.core.workflow import ToolDef, ToolSpec
from pydantic import BaseModel, Field

from llmwiki.domain.procedure_execution import (
    ProcedureExecution,
    ProcedureOutput,
    ProcedureStepResult,
    validate_procedure_execution,
)
from llmwiki.domain.task_evidence import TaskEvidencePack
from llmwiki.store import WikiStore, WikiStoreError


class ProcedureOutputParams(BaseModel):
    name: str = Field(description="Output field name, e.g. race, ability scores, equipment.")
    value: str = Field(default="", description="Concrete value, if resolved.")
    support: Literal["evidence", "derived", "assumption", "unresolved"] = Field(
        description="How this output is supported."
    )
    evidence_page_ids: list[str] = Field(
        default_factory=list,
        description="Wiki page_ids that support this output.",
    )
    derivation: str = Field(
        default="",
        description="Calculation or rule application for derived outputs.",
    )
    note: str = Field(default="", description="Short caveat or unresolved reason.")


class ProcedureStepResultParams(BaseModel):
    sequence: int = Field(description="Required procedure step number.")
    title: str = Field(description="Required procedure step title.")
    status: Literal["completed", "partial", "unresolved"] = Field(
        description="Whether this step produced a result."
    )
    outputs: list[ProcedureOutputParams] = Field(
        default_factory=list,
        description="Recorded outputs for this step.",
    )
    note: str = Field(default="", description="Step-level caveat or unresolved reason.")


class ProcedureExecutionParams(BaseModel):
    procedure_id: str = Field(description="Procedure page_id from the task evidence pack.")
    assumptions: list[str] = Field(
        default_factory=list,
        description="User-independent choices made to execute the procedure.",
    )
    step_results: list[ProcedureStepResultParams] = Field(
        description="One result for every required procedure step.",
    )


@dataclass
class ProcedureExecutionState:
    execution: ProcedureExecution | None = None

    @property
    def has_valid_execution(self) -> bool:
        return self.execution is not None


def submit_procedure_execution_tool(
    store: WikiStore,
    pack: TaskEvidencePack,
    *,
    read_tracker: set[str],
    state: ProcedureExecutionState,
) -> ToolDef:
    """Record a validated procedure execution before the model responds."""

    def _submit_procedure_execution(**kwargs: object) -> str:
        params = ProcedureExecutionParams(**kwargs)  # type: ignore[arg-type]
        execution = _execution_from_params(params)
        evidence_texts = dict(pack.evidence_texts)
        for page_id in sorted(read_tracker - {"index.md"} - set(evidence_texts)):
            evidence_texts[page_id] = store.read_page(page_id)
        decision = validate_procedure_execution(execution, pack, evidence_texts)
        if not decision.allowed:
            raise WikiStoreError(decision.message)
        state.execution = execution
        return execution.render()

    return ToolDef(
        spec=ToolSpec(
            name="submit_procedure_execution",
            description=(
                "Submit a typed ProcedureExecution before answering a request "
                "to execute a procedure. Include one step_result for every "
                "required step in the deterministic task evidence pack. Label "
                "each output as evidence, derived, assumption, or unresolved."
            ),
            parameters=ProcedureExecutionParams,
        ),
        callable=_submit_procedure_execution,
    )


def _execution_from_params(params: ProcedureExecutionParams) -> ProcedureExecution:
    return ProcedureExecution(
        procedure_id=params.procedure_id,
        assumptions=tuple(params.assumptions),
        step_results=tuple(
            ProcedureStepResult(
                sequence=step.sequence,
                title=step.title,
                status=step.status,
                note=step.note,
                outputs=tuple(
                    ProcedureOutput(
                        name=output.name,
                        value=output.value,
                        support=output.support,
                        evidence_page_ids=tuple(output.evidence_page_ids),
                        derivation=output.derivation,
                        note=output.note,
                    )
                    for output in step.outputs
                ),
            )
            for step in params.step_results
        ),
    )
