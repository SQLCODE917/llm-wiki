"""State-flow evidence for source-grounded procedure candidates."""

from __future__ import annotations

from dataclasses import dataclass

from llmwiki.domain.ledger.topic_terms import content_terms

_STATEFUL_ACTION_TYPES = frozenset(
    {"choose", "generate", "calculate", "allocate", "acquire", "record", "validate", "finalize"}
)
_PROCEDURE_ROLE_TAGS = frozenset({"procedure"})
_OUTPUT_ATOM_KINDS = frozenset({"formula", "procedure", "table"})
_LOW_SIGNAL_TERMS = frozenset(
    {
        "ability",
        "basic",
        "chapter",
        "entry",
        "list",
        "normal",
        "other",
        "rule",
        "section",
        "special",
        "table",
        "type",
    }
)


@dataclass(frozen=True)
class ProcedureStepEvidence:
    sequence: int
    title: str
    action_type: str
    heading_action_type: str
    claim_texts: tuple[str, ...]
    claim_role_tags: tuple[str, ...]
    technical_atom_kinds: tuple[str, ...]
    technical_atom_texts: tuple[str, ...]


@dataclass(frozen=True)
class ProcedureStateFlow:
    stateful_action_step_count: int
    procedure_role_step_count: int
    technical_output_step_count: int
    prior_output_dependency_count: int

    @property
    def has_state_flow(self) -> bool:
        if self.prior_output_dependency_count >= 1:
            return True
        if self.procedure_role_step_count >= 2:
            return True
        return self.stateful_action_step_count >= 2 and self.technical_output_step_count >= 1


def build_procedure_state_flow(steps: tuple[ProcedureStepEvidence, ...]) -> ProcedureStateFlow:
    output_steps = tuple(step for step in steps if _step_produces_or_transforms_state(step))
    return ProcedureStateFlow(
        stateful_action_step_count=sum(1 for step in steps if _has_stateful_action(step)),
        procedure_role_step_count=sum(1 for step in steps if _has_procedure_role(step)),
        technical_output_step_count=sum(1 for step in steps if _has_output_atom(step)),
        prior_output_dependency_count=_prior_output_dependency_count(steps, output_steps),
    )


def _step_produces_or_transforms_state(step: ProcedureStepEvidence) -> bool:
    return (
        _has_stateful_action(step)
        or step.action_type in _STATEFUL_ACTION_TYPES
        or _has_procedure_role(step)
        or _has_output_atom(step)
    )


def _has_stateful_action(step: ProcedureStepEvidence) -> bool:
    return step.heading_action_type in _STATEFUL_ACTION_TYPES


def _has_procedure_role(step: ProcedureStepEvidence) -> bool:
    return any(tag in _PROCEDURE_ROLE_TAGS for tag in step.claim_role_tags)


def _has_output_atom(step: ProcedureStepEvidence) -> bool:
    return any(kind in _OUTPUT_ATOM_KINDS for kind in step.technical_atom_kinds)


def _prior_output_dependency_count(
    steps: tuple[ProcedureStepEvidence, ...],
    output_steps: tuple[ProcedureStepEvidence, ...],
) -> int:
    count = 0
    repeated_title_terms = _repeated_step_title_terms(steps)
    for step in steps:
        prior_terms = _prior_output_terms(output_steps, step.sequence, repeated_title_terms)
        if prior_terms and _step_mentions_any(step, prior_terms, repeated_title_terms):
            count += 1
    return count


def _prior_output_terms(
    output_steps: tuple[ProcedureStepEvidence, ...],
    sequence: int,
    ignored_terms: frozenset[str],
) -> frozenset[str]:
    terms: set[str] = set()
    for step in output_steps:
        if step.sequence >= sequence:
            continue
        terms.update(_meaningful_terms(step.title, ignored_terms))
    return frozenset(terms)


def _step_mentions_any(
    step: ProcedureStepEvidence, terms: frozenset[str], ignored_terms: frozenset[str]
) -> bool:
    if not terms:
        return False
    return bool(
        _meaningful_terms(" ".join((step.title, *_bounded_evidence_texts(step))), ignored_terms)
        & terms
    )


def _bounded_evidence_texts(step: ProcedureStepEvidence) -> tuple[str, ...]:
    return (*step.claim_texts[:6], *step.technical_atom_texts[:6])


def _repeated_step_title_terms(steps: tuple[ProcedureStepEvidence, ...]) -> frozenset[str]:
    seen_once: set[str] = set()
    repeated: set[str] = set()
    for step in steps:
        for term in _meaningful_terms(step.title, frozenset()):
            if term in seen_once:
                repeated.add(term)
            seen_once.add(term)
    return frozenset(repeated)


def _meaningful_terms(text: str, ignored_terms: frozenset[str]) -> frozenset[str]:
    return frozenset(
        term
        for term in (_normalize_term(raw) for raw in content_terms(text))
        if len(term) >= 3 and term not in _LOW_SIGNAL_TERMS and term not in ignored_terms
    )


def _normalize_term(term: str) -> str:
    if term.endswith("s") and len(term) > 3:
        return term[:-1]
    return term
