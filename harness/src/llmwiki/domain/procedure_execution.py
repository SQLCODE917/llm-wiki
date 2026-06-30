"""Typed procedure execution results and validation."""

from __future__ import annotations

import re
from collections.abc import Mapping
from dataclasses import dataclass
from typing import Literal

from llmwiki.domain.task_evidence import TaskEvidencePack

ProcedureStepStatus = Literal["completed", "partial", "unresolved"]
ProcedureOutputSupport = Literal["evidence", "derived", "assumption", "unresolved"]

_WORD_RE = re.compile(r"[a-z0-9]+")
_GENERIC_DERIVED_TERMS = frozenset(
    {
        "ability",
        "abilities",
        "character",
        "completed",
        "details",
        "equipment",
        "score",
        "scores",
        "sheet",
        "skill",
        "skills",
        "standard",
        "starting",
        "value",
        "values",
    }
)


@dataclass(frozen=True)
class ProcedureOutput:
    name: str
    value: str
    support: ProcedureOutputSupport
    evidence_page_ids: tuple[str, ...] = ()
    derivation: str = ""
    note: str = ""


@dataclass(frozen=True)
class ProcedureStepResult:
    sequence: int
    title: str
    status: ProcedureStepStatus
    outputs: tuple[ProcedureOutput, ...] = ()
    note: str = ""


@dataclass(frozen=True)
class ProcedureExecution:
    procedure_id: str
    step_results: tuple[ProcedureStepResult, ...]
    assumptions: tuple[str, ...] = ()

    def render(self) -> str:
        lines = [f"ProcedureExecution accepted for [[{self.procedure_id}]]."]
        if self.assumptions:
            lines.append("")
            lines.append("Assumptions:")
            for assumption in self.assumptions:
                lines.append(f"- {assumption}")
        lines.append("")
        lines.append("Step results:")
        for step in sorted(self.step_results, key=lambda item: item.sequence):
            lines.append(f"{step.sequence}. {step.title} [{step.status}]")
            if step.note:
                lines.append(f"   - Note: {step.note}")
            for output in step.outputs:
                evidence = _render_evidence(output.evidence_page_ids)
                suffix = f" {evidence}" if evidence else ""
                value = output.value or output.note or "unresolved"
                lines.append(f"   - {output.name}: {value} ({output.support}{suffix})")
                if output.derivation:
                    lines.append(f"     Derivation: {output.derivation}")
        return "\n".join(lines)


@dataclass(frozen=True)
class ProcedureExecutionValidation:
    allowed: bool
    message: str = ""


def validate_procedure_execution(
    execution: ProcedureExecution,
    pack: TaskEvidencePack,
    evidence_texts: Mapping[str, str],
) -> ProcedureExecutionValidation:
    if execution.procedure_id != pack.procedure_id:
        return _reject(
            f"procedure_id must be {pack.procedure_id!r}; got {execution.procedure_id!r}."
        )
    required = {step.sequence: step for step in pack.steps}
    actual = {step.sequence: step for step in execution.step_results}
    missing = sorted(set(required) - set(actual))
    if missing:
        return _reject(f"Missing ProcedureExecution step result(s): {missing}.")
    extra = sorted(set(actual) - set(required))
    if extra:
        return _reject(f"ProcedureExecution includes unknown step(s): {extra}.")
    for sequence, requirement in required.items():
        step = actual[sequence]
        if not step.title:
            return _reject(f"Step {sequence} must include a title.")
        if step.status not in {"completed", "partial", "unresolved"}:
            return _reject(f"Step {sequence} has invalid status {step.status!r}.")
        if step.status == "unresolved" and not (step.note or step.outputs):
            return _reject(f"Step {sequence} is unresolved but has no note.")
        if step.status != "unresolved" and not step.outputs:
            return _reject(f"Step {sequence} must record at least one output.")
        decision = _validate_outputs(
            step.outputs,
            sequence=sequence,
            step_title=step.title,
            expected_page_id=requirement.evidence_page_id,
            evidence_texts=evidence_texts,
            assumptions=execution.assumptions,
        )
        if not decision.allowed:
            return decision
    return ProcedureExecutionValidation(allowed=True)


def _validate_outputs(
    outputs: tuple[ProcedureOutput, ...],
    *,
    sequence: int,
    step_title: str,
    expected_page_id: str,
    evidence_texts: Mapping[str, str],
    assumptions: tuple[str, ...],
) -> ProcedureExecutionValidation:
    for output in outputs:
        if not output.name.strip():
            return _reject(f"Step {sequence} has an output without a name.")
        if output.support not in {"evidence", "derived", "assumption", "unresolved"}:
            return _reject(
                f"Step {sequence} output {output.name!r} has invalid support {output.support!r}."
            )
        unknown = sorted(set(output.evidence_page_ids) - set(evidence_texts))
        if unknown:
            return _reject(
                f"Step {sequence} output {output.name!r} cites pages outside "
                f"the evidence pack or pages read this turn: {unknown}."
            )
        if output.support in {"evidence", "derived"} and not output.evidence_page_ids:
            return _reject(
                f"Step {sequence} output {output.name!r} needs evidence_page_ids. "
                "If no evidence page supports this concrete value, change support "
                "to unresolved, clear the value, and explain the missing evidence "
                "in note."
            )
        if (
            output.support == "evidence"
            and output.value
            and not _value_is_supported(output.value, output.evidence_page_ids, evidence_texts)
        ):
            return _reject(
                f"Step {sequence} output {output.name!r} says {output.value!r} "
                "is direct evidence, but that value does not appear in its cited "
                "evidence text. Mark it as an assumption, derived value, or unresolved."
            )
        if output.support == "derived" and not output.derivation.strip():
            return _reject(
                f"Step {sequence} output {output.name!r} is derived but has no derivation."
            )
        if output.support == "derived" and output.value:
            unsupported = _unsupported_derived_terms(
                output.value, output.evidence_page_ids, evidence_texts
            )
            if unsupported:
                return _reject(
                    f"Step {sequence} output {output.name!r} derives terms absent "
                    f"from its cited evidence text: {unsupported}. Use source "
                    "vocabulary, mark the field unresolved, or cite evidence that "
                    "contains those terms."
                )
        if output.support == "assumption" and not _assumption_is_declared(
            output.value or output.note, assumptions
        ):
            return _reject(
                f"Step {sequence} output {output.name!r} is an assumption but is "
                "not listed in the top-level assumptions."
            )
        if output.support == "assumption" and output.value:
            evidence_ids = output.evidence_page_ids or (
                (expected_page_id,) if expected_page_id in evidence_texts else ()
            )
            unsupported = _unsupported_derived_terms(output.value, evidence_ids, evidence_texts)
            if unsupported and not _free_choice_output(output.name, step_title):
                return _reject(
                    f"Step {sequence} output {output.name!r} assumes terms absent "
                    f"from the relevant evidence text: {unsupported}. Use terms "
                    "from the evidence, reserve arbitrary assumptions for free-form "
                    "identity fields, or mark the field unresolved."
                )
        if output.support == "unresolved" and not (output.note or output.value):
            return _reject(f"Step {sequence} output {output.name!r} is unresolved but has no note.")
        if expected_page_id in evidence_texts and output.support in {"evidence", "derived"}:
            continue
    return ProcedureExecutionValidation(allowed=True)


def _value_is_supported(
    value: str, page_ids: tuple[str, ...], evidence_texts: Mapping[str, str]
) -> bool:
    normalized_value = _normalize(value)
    if not normalized_value:
        return True
    combined = _normalize(" ".join(evidence_texts[page_id] for page_id in page_ids))
    if normalized_value in combined:
        return True
    value_tokens = set(_WORD_RE.findall(normalized_value))
    if len(value_tokens) <= 1:
        return value_tokens <= set(_WORD_RE.findall(combined))
    return False


def _unsupported_derived_terms(
    value: str, page_ids: tuple[str, ...], evidence_texts: Mapping[str, str]
) -> tuple[str, ...]:
    evidence_tokens = set(
        _WORD_RE.findall(_normalize(" ".join(evidence_texts[page_id] for page_id in page_ids)))
    )
    unsupported: list[str] = []
    for token in _WORD_RE.findall(value.lower()):
        if len(token) <= 3 or token.isdigit() or token in _GENERIC_DERIVED_TERMS:
            continue
        if _token_in_evidence(token, evidence_tokens):
            continue
        unsupported.append(token)
    return tuple(dict.fromkeys(unsupported))


def _token_in_evidence(token: str, evidence_tokens: set[str]) -> bool:
    return (
        token in evidence_tokens
        or f"{token}s" in evidence_tokens
        or (token.endswith("s") and token[:-1] in evidence_tokens)
    )


def _free_choice_output(output_name: str, step_title: str) -> bool:
    text = f"{output_name} {step_title}".lower()
    return any(term in text for term in ("name", "gender", "sex", "label", "title"))


def _assumption_is_declared(value: str, assumptions: tuple[str, ...]) -> bool:
    if assumptions:
        return True
    if not value.strip():
        return False
    normalized_value = _normalize(value)
    return any(
        normalized_value in _normalize(assumption) or _normalize(assumption) in normalized_value
        for assumption in assumptions
    )


def _normalize(text: str) -> str:
    return " ".join(_WORD_RE.findall(text.lower()))


def _render_evidence(page_ids: tuple[str, ...]) -> str:
    if not page_ids:
        return ""
    return "evidence " + ", ".join(f"[[{page_id}]]" for page_id in page_ids)


def _reject(message: str) -> ProcedureExecutionValidation:
    return ProcedureExecutionValidation(allowed=False, message=message)
