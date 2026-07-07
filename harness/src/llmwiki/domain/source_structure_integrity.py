"""Source-map structure integrity gates for page-driving sections."""

from __future__ import annotations

import re
from collections import Counter
from dataclasses import dataclass

from llmwiki.domain.source_map import NormalizedSourceMap, SourceBlock

PAGE_DRIVER_DISPOSITIONS = frozenset({"trusted", "container"})
_FIELD_ASSIGNMENT = re.compile(r"\b[\w][\w /()-]{0,36}\s*=")
_ROW_SEPARATOR = re.compile(r"\s(?:=|:|/)\s")
_MARKDOWN_HEADING = re.compile(r"^\s{0,3}#{1,6}\s*")


@dataclass(frozen=True)
class SourceSectionDisposition:
    section_path: str
    disposition: str
    reason_codes: tuple[str, ...]

    @property
    def may_drive_pages(self) -> bool:
        return self.disposition in PAGE_DRIVER_DISPOSITIONS


@dataclass(frozen=True)
class SourceStructureFinding:
    severity: str
    finding_code: str
    section_path: str
    message: str


@dataclass(frozen=True)
class SourceStructureIntegrityReport:
    source_id: str
    source_hash: str
    dispositions: tuple[SourceSectionDisposition, ...]
    findings: tuple[SourceStructureFinding, ...]

    def disposition_for(self, section_path: str) -> SourceSectionDisposition | None:
        return next((item for item in self.dispositions if item.section_path == section_path), None)

    def section_can_drive_pages(self, section_path: str) -> bool:
        disposition = self.disposition_for(section_path)
        return disposition is None or disposition.may_drive_pages


def build_source_structure_integrity_report(
    source_map: NormalizedSourceMap,
) -> SourceStructureIntegrityReport:
    sections = tuple(
        dict.fromkeys(block.section_path or "Overview" for block in source_map.source_blocks)
    )
    dispositions = tuple(_section_disposition(section, source_map) for section in sections)
    findings = tuple(
        SourceStructureFinding(
            "warning",
            "source-section-cannot-drive-pages",
            item.section_path,
            f"Section cannot drive generated pages: {', '.join(item.reason_codes)}.",
        )
        for item in dispositions
        if not item.may_drive_pages and item.reason_codes
    )
    return SourceStructureIntegrityReport(
        source_map.source_id,
        source_map.source_hash,
        dispositions,
        findings,
    )


def _section_disposition(
    section_path: str, source_map: NormalizedSourceMap
) -> SourceSectionDisposition:
    label = _section_label(section_path)
    reasons = _bad_label_reasons(label)
    if reasons:
        return SourceSectionDisposition(section_path, "evidence-only", reasons)
    depth = max(0, section_path.count(">"))
    disposition = "container" if depth <= 0 and _short_label(label) else "trusted"
    return SourceSectionDisposition(section_path, disposition, ())


def source_block_can_drive_pages(block: SourceBlock) -> bool:
    return not _bad_label_reasons(_section_label(block.section_path or block.source_text))


def _bad_label_reasons(text: str) -> tuple[str, ...]:
    label = _plain(text)
    reasons: list[str] = []
    if not label:
        reasons.append("empty")
    if _has_unbalanced_delimiters(label):
        reasons.append("unbalanced-delimiters")
    if _is_bracket_wrapped_label(label):
        reasons.append("bracket-wrapped-label")
    if _field_density(label) >= 2:
        reasons.append("field-dense")
    if _looks_like_table_row(label):
        reasons.append("row-shaped")
    if _too_long_for_label(label):
        reasons.append("label-too-long")
    return tuple(reasons)


def _section_label(section_path: str) -> str:
    return section_path.rsplit(">", 1)[-1].strip() or "Overview"


def _plain(text: str) -> str:
    return re.sub(r"\s+", " ", _MARKDOWN_HEADING.sub("", text)).strip()


def _short_label(text: str) -> bool:
    return 0 < len(text.split()) <= 12 and len(text) <= 96


def _too_long_for_label(text: str) -> bool:
    return len(text.split()) > 18 or len(text) > 160


def _field_density(text: str) -> int:
    return len(_FIELD_ASSIGNMENT.findall(text))


def _looks_like_table_row(text: str) -> bool:
    if "|" in text and text.count("|") >= 2:
        return True
    if _field_density(text) >= 1 and len(_ROW_SEPARATOR.findall(text)) >= 3:
        return True
    separators = Counter(char for char in text if char in "=:/;")
    return sum(separators.values()) >= 5 and len(text.split()) >= 8


def _has_unbalanced_delimiters(text: str) -> bool:
    pairs = (("[", "]"), ("(", ")"), ("{", "}"), ("【", "】"), ("《", "》"))
    return any(text.count(left) != text.count(right) for left, right in pairs)


def _is_bracket_wrapped_label(text: str) -> bool:
    stripped = text.strip()
    return (
        len(stripped) <= 96
        and (
            (stripped.startswith("[") and stripped.endswith("]"))
            or (stripped.startswith("【") and stripped.endswith("】"))
            or (stripped.startswith("《") and stripped.endswith("》"))
        )
    )
