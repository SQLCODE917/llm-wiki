"""Deterministic parsing and validation for lightweight raw-source citations."""

from __future__ import annotations

import re
from collections.abc import Iterable
from dataclasses import dataclass, field
from pathlib import PurePosixPath
from typing import Literal

from llmwiki.domain.citation_context import (
    citation_caveats,
    evidence_text_near_citation,
    ocr_caveat_texts,
)

FindingSeverity = Literal["info", "warn", "fail"]
FindingCode = Literal[
    "evidence-canonicalized",
    "evidence-not-found",
    "evidence-outside-locator",
    "invalid-locator",
    "locator-out-of-range",
    "missing-source",
    "malformed-page-range",
    "malformed-line-range",
    "path-outside-raw",
    "ocr-verbatim-risk",
]

_RAW_CITATION_RE = re.compile(r"raw/(?P<body>[^\n)\]]+)")
_PAGE_RANGE_RE = re.compile(r"^p\.(?P<start>[0-9]+)(?:-(?P<end>[0-9]+))?$")
_LINE_RANGE_RE = re.compile(r"^normalized:L(?P<start>[0-9]+)(?:-L?(?P<end>[0-9]+))?$")
_NORMALIZED_TOKEN_RE = re.compile(r"normalized:[^\s)\],;]+")
_LOCATOR_TRANSLATION = str.maketrans(
    {
        "\u2010": "-",
        "\u2011": "-",
        "\u2012": "-",
        "\u2013": "-",
        "\u2014": "-",
        "\u2212": "-",
    }
)


@dataclass(frozen=True)
class Citation:
    """A syntactic raw-source citation extracted from one wiki page."""

    page_name: str
    source_path: str
    raw_text: str
    page_range: tuple[int, int] | None = None
    line_range: tuple[int, int] | None = None
    evidence_text: str | None = None
    caveat_flags: tuple[str, ...] = ()


@dataclass(frozen=True)
class CitationFinding:
    """A deterministic citation issue for a later policy gate to interpret."""

    page_name: str
    severity: FindingSeverity
    citation_text: str
    code: FindingCode
    message: str


@dataclass(frozen=True)
class CitationReport:
    citations: tuple[Citation, ...] = ()
    findings: tuple[CitationFinding, ...] = ()

    @property
    def is_clean(self) -> bool:
        return not self.findings


@dataclass(frozen=True)
class SourceInventory:
    """Known raw-source paths, normalized to the citation form ``raw/<path>``."""

    source_paths: frozenset[str] = field(default_factory=frozenset)

    @classmethod
    def from_raw_relative_paths(cls, paths: Iterable[str]) -> SourceInventory:
        return cls(frozenset(_inventory_path(path) for path in paths))

    def has_source(self, source_path: str) -> bool:
        return source_path in self.source_paths


@dataclass(frozen=True)
class _ParsedRange:
    value: tuple[int, int] | None
    finding: CitationFinding | None = None


@dataclass(frozen=True)
class _CitationSpan:
    citation: Citation
    start: int
    end: int


def parse_citations(page_name: str, body: str) -> CitationReport:
    """Parse citation syntax from *body* without reading the filesystem."""

    spans: list[_CitationSpan] = []
    findings: list[CitationFinding] = []
    for match in _RAW_CITATION_RE.finditer(body):
        source_path, raw_text, locators = _citation_parts(match.group("body"))
        page_range: tuple[int, int] | None = None
        line_range: tuple[int, int] | None = None
        for locator in locators:
            if locator.startswith("p."):
                parsed = _parse_page_range(page_name, locator)
                page_range = parsed.value
                if parsed.finding is not None:
                    findings.append(parsed.finding)
            elif locator.startswith("normalized:"):
                parsed = _parse_line_range(page_name, locator)
                line_range = parsed.value
                if parsed.finding is not None:
                    findings.append(parsed.finding)
        citation = Citation(
            page_name=page_name,
            source_path=source_path,
            raw_text=raw_text,
            page_range=page_range,
            line_range=line_range,
            evidence_text=evidence_text_near_citation(body, match.start(), match.end()),
            caveat_flags=citation_caveats(body, match.start(), match.end()),
        )
        spans.append(_CitationSpan(citation=citation, start=match.start(), end=match.end()))

    findings.extend(_standalone_line_locator_findings(page_name, body, spans))
    findings.extend(_ocr_caveat_findings(page_name, body))
    return CitationReport(
        citations=tuple(span.citation for span in spans),
        findings=tuple(findings),
    )


def _citation_parts(body: str) -> tuple[str, str, tuple[str, ...]]:
    path_tokens: list[str] = []
    locators: list[str] = []
    found_locator = False
    for token in body.strip().split():
        normalized = token.translate(_LOCATOR_TRANSLATION).rstrip(".,;")
        if normalized.startswith("p.") or normalized.startswith("normalized:"):
            found_locator = True
            locators.append(normalized)
        elif found_locator:
            break
        else:
            path_tokens.append(token)
    path = " ".join(path_tokens).rstrip(".,;")
    source_path = f"raw/{path}"
    raw_text = source_path
    if locators:
        raw_text += " " + " ".join(locators)
    return source_path, raw_text, tuple(locators)


def validate_citations(report: CitationReport, inventory: SourceInventory) -> CitationReport:
    """Add source-existence and raw-path confinement findings to a parsed report."""

    findings = list(report.findings)
    for citation in report.citations:
        if not _is_confined_to_raw(citation.source_path):
            findings.append(
                CitationFinding(
                    page_name=citation.page_name,
                    severity="fail",
                    citation_text=citation.raw_text,
                    code="path-outside-raw",
                    message=f"Citation path {citation.source_path!r} escapes raw/.",
                )
            )
            continue
        if not inventory.has_source(citation.source_path):
            findings.append(
                CitationFinding(
                    page_name=citation.page_name,
                    severity="fail",
                    citation_text=citation.raw_text,
                    code="missing-source",
                    message=f"Citation source {citation.source_path!r} is not present in raw/.",
                )
            )
    return CitationReport(citations=report.citations, findings=tuple(findings))


def inspect_citations(page_name: str, body: str, inventory: SourceInventory) -> CitationReport:
    """Parse and validate one page body against a known source inventory."""

    return validate_citations(parse_citations(page_name, body), inventory)


def _parse_page_range(page_name: str, token: str) -> _ParsedRange:
    match = _PAGE_RANGE_RE.match(token)
    if match is None:
        return _ParsedRange(
            value=None,
            finding=_finding(
                page_name,
                "fail",
                token,
                "malformed-page-range",
                "PDF page ranges must look like p.28 or p.28-41.",
            ),
        )
    return _positive_range(
        page_name,
        token,
        match.group("start"),
        match.group("end"),
        "malformed-page-range",
        "PDF page ranges must be positive and ordered.",
    )


def _parse_line_range(page_name: str, token: str) -> _ParsedRange:
    match = _LINE_RANGE_RE.match(token)
    if match is None:
        return _ParsedRange(
            value=None,
            finding=_finding(
                page_name,
                "fail",
                token,
                "malformed-line-range",
                "Normalized line ranges must look like normalized:L12 or normalized:L12-L20.",
            ),
        )
    return _positive_range(
        page_name,
        token,
        match.group("start"),
        match.group("end"),
        "malformed-line-range",
        "Normalized line ranges must be positive and ordered.",
    )


def _positive_range(
    page_name: str,
    token: str,
    start_text: str,
    end_text: str | None,
    code: FindingCode,
    message: str,
) -> _ParsedRange:
    start = int(start_text)
    end = int(end_text) if end_text is not None else start
    if start < 1 or end < 1 or end < start:
        return _ParsedRange(value=None, finding=_finding(page_name, "fail", token, code, message))
    return _ParsedRange(value=(start, end))


def _standalone_line_locator_findings(
    page_name: str, body: str, spans: list[_CitationSpan]
) -> tuple[CitationFinding, ...]:
    findings: list[CitationFinding] = []
    for match in _NORMALIZED_TOKEN_RE.finditer(body):
        if any(span.start <= match.start() < span.end for span in spans):
            continue
        token = match.group(0)
        parsed = _parse_line_range(page_name, token)
        findings.append(
            parsed.finding
            or _finding(
                page_name,
                "fail",
                token,
                "malformed-line-range",
                "Normalized line locators must be attached to a raw source citation.",
            )
        )
    return tuple(findings)


def _ocr_caveat_findings(page_name: str, body: str) -> tuple[CitationFinding, ...]:
    return tuple(
        _finding(
            page_name,
            "warn",
            text,
            "ocr-verbatim-risk",
            "OCR caveat text may be used only as caveated evidence, not a verbatim quote.",
        )
        for text in ocr_caveat_texts(body)
    )


def _finding(
    page_name: str,
    severity: FindingSeverity,
    citation_text: str,
    code: FindingCode,
    message: str,
) -> CitationFinding:
    return CitationFinding(
        page_name=page_name,
        severity=severity,
        citation_text=citation_text,
        code=code,
        message=message,
    )


def _inventory_path(path: str) -> str:
    cleaned = path.strip()
    return cleaned if cleaned.startswith("raw/") else f"raw/{cleaned}"


def _is_confined_to_raw(source_path: str) -> bool:
    path = PurePosixPath(source_path)
    parts = path.parts
    return bool(parts) and parts[0] == "raw" and all(part not in {"", ".", ".."} for part in parts)
