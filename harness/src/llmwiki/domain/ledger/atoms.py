"""Technical atom payloads and the materialized ``TechnicalAtom`` record.

Technical atoms preserve source-equivalent structured data: tables, code
blocks, formulas, procedures, rules, and worked examples. The exact source
payload is always preserved. Parsed/logical structure is convenience: when it
cannot be formed, the atom keeps its raw text and carries a ``ReviewReason``.
"""

from __future__ import annotations

from dataclasses import dataclass

from llmwiki.domain.ledger.canonical import content_fingerprint
from llmwiki.domain.ledger.common import ReviewReason

# -- table -----------------------------------------------------------------


@dataclass(frozen=True)
class TableColumn:
    column_index: int
    header_text: str


@dataclass(frozen=True)
class TableRow:
    row_index: int


@dataclass(frozen=True)
class TableCell:
    row_index: int
    column_index: int
    value: str
    source_locator: str = ""


@dataclass(frozen=True)
class TablePayload:
    raw_table_text: str
    parse_status: str
    source_locator: str
    columns: tuple[TableColumn, ...] = ()
    rows: tuple[TableRow, ...] = ()
    cells: tuple[TableCell, ...] = ()
    caption: str = ""
    notes: tuple[str, ...] = ()


# -- code block ------------------------------------------------------------


@dataclass(frozen=True)
class CodeBlockPayload:
    raw_code_text: str
    parse_status: str
    source_locator: str
    language_tag: str = ""
    language_detected: bool = False
    language_confidence: str = ""
    code_fence: str = ""
    line_count: int = 0
    surrounding_explanation_locator: str = ""
    code_ast: str = ""


# -- formula ---------------------------------------------------------------


@dataclass(frozen=True)
class FormulaPayload:
    raw_formula_text: str
    formula_subtype: str
    formula_surface_form: str
    source_locator: str
    parse_status: str = "unparsed"
    notation_context_locator: str = ""


# -- figure ----------------------------------------------------------------


@dataclass(frozen=True)
class FigurePayload:
    raw_figure_text: str
    parse_status: str
    source_locator: str
    figure_locator: str = ""
    page_locator: str = ""


# -- procedure -------------------------------------------------------------


@dataclass(frozen=True)
class ProcedurePayload:
    procedure_text: str
    source_locator: str
    goal: str = ""
    inputs: tuple[str, ...] = ()
    preconditions: tuple[str, ...] = ()
    steps: tuple[str, ...] = ()
    outputs: tuple[str, ...] = ()
    exceptions: tuple[str, ...] = ()


# -- rule ------------------------------------------------------------------


@dataclass(frozen=True)
class RulePayload:
    rule_text: str
    rule_force: str
    source_locator: str
    scope: str = ""
    trigger: str = ""
    effect: str = ""
    exception: str = ""


# -- worked example --------------------------------------------------------


@dataclass(frozen=True)
class WorkedExamplePayload:
    example_text: str
    source_locator: str
    setup: str = ""
    inputs: tuple[str, ...] = ()
    operations: tuple[str, ...] = ()
    outputs: tuple[str, ...] = ()
    explanation: str = ""
    referenced_atom_ids: tuple[str, ...] = ()


AtomPayload = (
    TablePayload
    | CodeBlockPayload
    | FormulaPayload
    | FigurePayload
    | ProcedurePayload
    | RulePayload
    | WorkedExamplePayload
)


@dataclass(frozen=True)
class TechnicalAtom:
    """One preserved structured item materialized into the ledger."""

    technical_atom_id: str
    technical_atom_kind: str
    payload: AtomPayload
    source_locator: str
    source_range_id: str
    evidence_ids: tuple[str, ...]
    parse_status: str = "parsed"
    review_reason: ReviewReason | None = None


@dataclass(frozen=True)
class AtomCandidate:
    """A materialized atom candidate with payload or structured review reason."""

    atom_candidate_id: str
    extractor_decision_id: str
    extractor_capability_id: str
    technical_atom_kind: str
    ranker_score: float
    calibration_bucket: str
    source_range_id: str
    feature_signal_ids: tuple[str, ...] = ()
    evidence_ids: tuple[str, ...] = ()
    payload: AtomPayload | None = None
    review_reason: ReviewReason | None = None
    validation_status: str = ""
    validation_detail: str = ""


def payload_fingerprint(payload: AtomPayload) -> str:
    """Hash of the domain-relevant contents of one technical atom payload."""
    return content_fingerprint(payload)


def atom_raw_text(payload: AtomPayload) -> str:
    """The exact source text preserved by a payload (used for fidelity checks)."""
    for attr in (
        "raw_table_text",
        "raw_code_text",
        "raw_formula_text",
        "raw_figure_text",
        "rule_text",
        "procedure_text",
        "example_text",
    ):
        value = getattr(payload, attr, None)
        if isinstance(value, str):
            return value
    return ""
