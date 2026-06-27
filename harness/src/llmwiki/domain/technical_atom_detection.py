"""Source-agnostic technical atom candidate detection."""

from __future__ import annotations

import re
from typing import Literal

from llmwiki.domain.evidence_registry import EvidenceRecord
from llmwiki.domain.source_claim_heuristics import code_fragment_payload, is_code_fragment
from llmwiki.domain.source_summary import SourceClaim

TechnicalAtomKind = Literal[
    "code",
    "formula",
    "procedure",
    "table",
    "table-row",
    "requirement",
    "exception",
    "worked-example",
]
SupportStatus = Literal["supported", "too_broad", "not_supported", "unclear"]

TECHNICAL_ATOM_KINDS = frozenset(
    (
        "code",
        "formula",
        "procedure",
        "table",
        "table-row",
        "requirement",
        "exception",
        "worked-example",
    )
)
SUPPORT_STATUSES = frozenset(("supported", "too_broad", "not_supported", "unclear"))
MAX_TECHNICAL_PAYLOAD_CHARS = 1200
MAX_RENDERED_ATOMS_PER_PAGE = 8
MAX_EVIDENCE_SCORER_TEXT_CHARS = 20_000

_FORMULA_RE = re.compile(r"(?=.*[=+\-*/x×÷])(?:[A-Za-z][A-Za-z0-9 _-]{2,}|\*\*.+?\*\*)\s*=")
_PROGRAMMING_DECLARATION_RE = re.compile(r"\b(?:const|let|var)\s+[A-Za-z_$][\w$]*\s*=")
_ORDERED_RE = re.compile(r"^\s*(?:\d+[.)]|[-*])\s+(?P<step>\S.+)")
_TERM_RE = re.compile(r"[a-z][a-z0-9-]{2,}", re.IGNORECASE)
_STRUCTURAL_TOKEN_RE = re.compile(r"[a-z0-9*]+", re.IGNORECASE)
_INLINE_FENCE_RE = re.compile(r"```(?P<body>.*?)```", re.DOTALL)
_EXACT_TABLE_MATCH_SCORE = 1000
_KNOWN_FENCE_LANGUAGES = frozenset(
    (
        "bash",
        "c",
        "c++",
        "cpp",
        "cs",
        "csharp",
        "css",
        "go",
        "html",
        "java",
        "javascript",
        "js",
        "json",
        "markdown",
        "md",
        "py",
        "python",
        "rb",
        "ruby",
        "rs",
        "rust",
        "sh",
        "shell",
        "sql",
        "ts",
        "typescript",
        "xml",
        "yaml",
        "yml",
    )
)


def claim_kind(claim: SourceClaim) -> TechnicalAtomKind | None:
    roles = set(claim.claim_role_tags)
    statement = claim.statement
    lowered = statement.lower()
    if is_code_fragment(statement):
        return "code"
    if "worked-example" in roles:
        return "worked-example"
    if is_formula(statement):
        return "formula"
    if "procedure" in roles or _looks_procedural(lowered):
        return "procedure"
    if roles & {"limitation", "negative-evidence"} or _looks_exceptional(lowered):
        return "exception"
    if "requirement" in roles or _looks_required(lowered):
        return "requirement"
    return None


def fields_for_claim(kind: TechnicalAtomKind, statement: str) -> tuple[tuple[str, str], ...]:
    if kind == "code":
        return (("language", _language("", code_fragment_payload(statement))),)
    if kind == "formula":
        return (("expression", statement),)
    if kind == "procedure":
        return (("ordered_steps", statement),)
    if kind in {"requirement", "exception"}:
        return (("statement", statement),)
    return ()


def fenced_code_blocks(text: str) -> tuple[tuple[str, str], ...]:
    blocks: list[tuple[str, str]] = []
    in_block = False
    language = ""
    lines: list[str] = []
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("```"):
            if in_block:
                code = "\n".join(lines).strip()
                if code:
                    blocks.append((_language(language, code), code))
                in_block = False
                lines = []
            else:
                in_block = True
                language = stripped.removeprefix("```").strip()
            continue
        if in_block:
            lines.append(line)
    return tuple(blocks)


def inline_fenced_code_blocks(text: str) -> tuple[tuple[str, str], ...]:
    blocks: list[tuple[str, str]] = []
    for match in _INLINE_FENCE_RE.finditer(text):
        language, code = _split_inline_fence_body(match.group("body"))
        if code:
            blocks.append((language, code))
    return tuple(blocks)


def text_without_fenced_code(text: str) -> str:
    lines: list[str] = []
    in_block = False
    for line in text.splitlines():
        if line.strip().startswith("```"):
            in_block = not in_block
            continue
        if not in_block:
            lines.append(line)
    return "\n".join(lines)


def table_row(line: object) -> tuple[str, ...] | None:
    if not isinstance(line, str):
        return None
    stripped = line.strip()
    if (
        not stripped.startswith("|")
        or not stripped.endswith("|")
        or set(stripped) <= {"|", "-", " "}
    ):
        return None
    cells = tuple(cell.strip() for cell in stripped.strip("|").split("|"))
    return cells if len(cells) >= 2 and any(cells) else None


def ordered_step_groups(text: str) -> tuple[tuple[str, ...], ...]:
    groups: list[tuple[str, ...]] = []
    current: list[str] = []
    for line in text.splitlines():
        match = _ORDERED_RE.match(line)
        if match is None:
            if len(current) >= 2:
                groups.append(tuple(current))
            current = []
            continue
        current.append(match.group("step").strip())
    if len(current) >= 2:
        groups.append(tuple(current))
    return tuple(groups)


def is_formula(text: str) -> bool:
    stripped = text.strip()
    if any(marker in stripped for marker in ("=>", "===", "!==", "==")):
        return False
    if _PROGRAMMING_DECLARATION_RE.search(code_fragment_payload(stripped)):
        return False
    left_side = stripped.split("=", 1)[0].lower()
    if any(term in left_side for term in ("example", " rolls ", " gets ", " means ")):
        return False
    return 12 <= len(stripped) <= 220 and bool(_FORMULA_RE.search(stripped))


def best_evidence_ids(records: tuple[EvidenceRecord, ...], payload: object) -> tuple[str, ...]:
    scored_payload = _score_text(payload)
    ranked: list[tuple[int, int, EvidenceRecord]] = []
    for index, record in enumerate(records):
        ranked.append((_evidence_match_score(record.excerpt, scored_payload), index, record))
    ranked.sort(key=lambda item: (-item[0], item[1]))
    if _has_table_payload(scored_payload):
        table_matches = [
            record.evidence_id
            for score, _index, record in ranked
            if score >= _EXACT_TABLE_MATCH_SCORE
        ][:3]
        if table_matches:
            return tuple(table_matches)
    selected = [record.evidence_id for score, _index, record in ranked if score > 0][:3]
    return tuple(selected or [record.evidence_id for record in records[:3]])


def bounded_payload(payload: str) -> str | None:
    normalized = payload.strip()
    if not normalized or len(normalized) > MAX_TECHNICAL_PAYLOAD_CHARS:
        return None
    return normalized


def normalize_payload(payload: str) -> str:
    return re.sub(r"\s+", " ", payload).strip().lower()


def title_for_payload(kind: str, payload: str) -> str:
    words = _TERM_RE.findall(payload)[:6]
    return f"{kind}: {' '.join(words)}" if words else kind


def _evidence_match_score(excerpt: object, payload: object) -> int:
    excerpt = _score_text(excerpt)
    payload = _score_text(payload)
    score = 0
    payload_terms = set(_TERM_RE.findall(payload.lower()))
    excerpt_terms = set(_TERM_RE.findall(excerpt.lower()))
    score += len(payload_terms & excerpt_terms) * 10
    score += _structural_token_overlap_score(excerpt, payload)
    score += _table_row_match_score(excerpt, payload)
    return score


def _structural_token_overlap_score(excerpt: str, payload: str) -> int:
    payload_tokens = set(_STRUCTURAL_TOKEN_RE.findall(payload.lower()))
    if not payload_tokens:
        return 0
    excerpt_tokens = set(_STRUCTURAL_TOKEN_RE.findall(excerpt.lower()))
    return len(payload_tokens & excerpt_tokens)


def _table_row_match_score(excerpt: str, payload: str) -> int:
    if not _has_table_payload(payload):
        return 0
    payload_text = _canonical_structural_text(payload)
    excerpt_text = _canonical_structural_text(excerpt)
    if payload_text and payload_text in excerpt_text:
        return 1000 + len(payload_text)
    return 0


def _canonical_structural_text(text: str) -> str:
    return re.sub(r"\s+", "", text).lower()


def _has_table_payload(payload: object) -> bool:
    if not isinstance(payload, str):
        return False
    return any(table_row(line) is not None for line in payload.splitlines())


def _score_text(value: object) -> str:
    text = value if isinstance(value, str) else str(value)
    return text[:MAX_EVIDENCE_SCORER_TEXT_CHARS]


def _looks_procedural(lowered: str) -> bool:
    return bool(
        re.search(r"\bfirst,", lowered)
        or re.search(r"\bthen\b", lowered)
        or re.search(r"\bnext\b", lowered)
        or re.search(r"\bfinally\b", lowered)
        or re.search(r"\bstep\s+\d+\b", lowered)
    )


def _looks_exceptional(lowered: str) -> bool:
    return any(term in lowered for term in ("except", "unless", "cannot", "not affected"))


def _looks_required(lowered: str) -> bool:
    return any(term in lowered for term in (" must ", " required ", " requires ", "always "))


def _language(language: str, code: str) -> str:
    if language:
        return language
    lowered = code.lower()
    if any(token in lowered for token in ("const ", "let ", "=>", "function", "symbol.iterator")):
        return "javascript"
    return ""


def _split_inline_fence_body(body: str) -> tuple[str, str]:
    stripped = body.strip()
    if not stripped:
        return "", ""
    first, separator, rest = stripped.partition(" ")
    if separator and first.lower() in _KNOWN_FENCE_LANGUAGES:
        return _language(first, rest.strip()), rest.strip()
    return _language("", stripped), stripped
