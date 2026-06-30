"""Deterministic provenance audit for generated source pages."""

from __future__ import annotations

import argparse
import json
import re
from bisect import bisect_right
from collections import Counter, defaultdict
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, cast

from llmwiki.domain.ledger.projection_policy import PAGE_FAMILY_SOURCE_MANIFEST
from llmwiki.domain.pages import PageError, parse_page

_SOURCE_RANGE = re.compile(r"source-range-[a-f0-9]+-\d+")
_WORD = re.compile(r"[A-Za-z0-9]+")
_AUDIT_STOPWORDS = frozenset(
    {
        "about",
        "after",
        "also",
        "and",
        "any",
        "are",
        "because",
        "but",
        "can",
        "for",
        "from",
        "has",
        "have",
        "into",
        "its",
        "may",
        "not",
        "one",
        "only",
        "section",
        "source",
        "that",
        "the",
        "their",
        "them",
        "there",
        "these",
        "this",
        "those",
        "when",
        "which",
        "with",
        "you",
    }
)
_ROOT_CAUSES = {
    "missing-ledger-range": (
        "projection references a source range absent from source coverage and the ledger"
    ),
    "structure-only-range": (
        "projection references a source segment that did not become a claim or technical atom"
    ),
    "context-pointer-projected": "projection included an unresolved deictic/context pointer",
    "fragmentary-statement": "source segmentation split prose across source ranges",
    "topic-support-gap": "topic planning attached evidence without local lexical support",
    "technical-atom-topic-gap": "technical atom matching attached an atom without topic support",
    "range-order-outlier": "projection mixed distant source-order ranges on one page",
}


@dataclass(frozen=True)
class ProvenanceFinding:
    page_id: str
    line_no: int
    source_range_id: str
    finding_type: str
    severity: str
    root_cause: str
    title: str
    section_path: str
    excerpt: str


@dataclass(frozen=True)
class PageAuditSummary:
    page_id: str
    title: str
    cited_item_count: int
    finding_count: int


@dataclass(frozen=True)
class ProvenanceAuditReport:
    source_page_id: str
    page_count: int
    cited_item_count: int
    finding_count: int
    finding_counts: dict[str, int]
    source_manifest_finding_count: int
    source_manifest_finding_counts: dict[str, int]
    non_manifest_finding_count: int
    non_manifest_finding_counts: dict[str, int]
    page_summaries: tuple[PageAuditSummary, ...]
    findings: tuple[ProvenanceFinding, ...]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--source-page-id", required=True)
    parser.add_argument("--ledger-dir", type=Path, required=True)
    parser.add_argument("--json-out", type=Path, required=True)
    parser.add_argument("--markdown-out", type=Path, required=True)
    args = parser.parse_args()

    report = audit_source_pages(args.root, args.source_page_id, args.ledger_dir)
    args.json_out.parent.mkdir(parents=True, exist_ok=True)
    args.markdown_out.parent.mkdir(parents=True, exist_ok=True)
    args.json_out.write_text(json.dumps(asdict(report), indent=2), encoding="utf-8")
    args.markdown_out.write_text(render_markdown(report, args.json_out), encoding="utf-8")
    print(
        f"Audited {report.page_count} page(s), {report.cited_item_count} cited item(s), "
        f"{report.finding_count} finding(s)."
    )


def audit_source_pages(root: Path, source_page_id: str, ledger_dir: Path) -> ProvenanceAuditReport:
    ledger = _artifact_json(ledger_dir / "claim-ledger.json", "ledger")
    structure = _artifact_json(ledger_dir / "document-structure.json", "document_structure")
    source_coverage = _artifact_json(ledger_dir / "source-coverage.json", "source_coverage")
    projection_context = _artifact_json(
        ledger_dir / "projection-context.json", "projection_context"
    )
    index = _LedgerIndex(ledger, structure, source_coverage, projection_context)
    findings: list[ProvenanceFinding] = []
    source_manifest_findings: list[ProvenanceFinding] = []
    non_manifest_findings: list[ProvenanceFinding] = []
    summaries: list[PageAuditSummary] = []
    cited_total = 0
    for path in sorted((root / "wiki").glob(f"{source_page_id}*.md")):
        try:
            page = parse_page(path.read_text(encoding="utf-8"))
        except PageError:
            continue
        if not page.page_id.startswith(source_page_id):
            continue
        title = _page_title(page.page_body) or page.page_id
        page_findings, cited_count = _audit_page(page.page_id, title, page.page_body, index)
        cited_total += cited_count
        findings.extend(page_findings)
        if page.page_metadata.page_family == PAGE_FAMILY_SOURCE_MANIFEST:
            source_manifest_findings.extend(page_findings)
        else:
            non_manifest_findings.extend(page_findings)
        summaries.append(PageAuditSummary(page.page_id, title, cited_count, len(page_findings)))
    counts = Counter(f.finding_type for f in findings)
    source_manifest_counts = Counter(f.finding_type for f in source_manifest_findings)
    non_manifest_counts = Counter(f.finding_type for f in non_manifest_findings)
    return ProvenanceAuditReport(
        source_page_id=source_page_id,
        page_count=len(summaries),
        cited_item_count=cited_total,
        finding_count=len(findings),
        finding_counts=dict(sorted(counts.items())),
        source_manifest_finding_count=len(source_manifest_findings),
        source_manifest_finding_counts=dict(sorted(source_manifest_counts.items())),
        non_manifest_finding_count=len(non_manifest_findings),
        non_manifest_finding_counts=dict(sorted(non_manifest_counts.items())),
        page_summaries=tuple(summaries),
        findings=tuple(findings),
    )


def render_markdown(report: ProvenanceAuditReport, json_path: Path) -> str:
    lines = [
        "# Sword World Provenance Audit",
        "",
        "## Scope",
        "",
        f"- Source page id: `{report.source_page_id}`",
        f"- Pages audited: {report.page_count}",
        f"- Cited source-range items audited: {report.cited_item_count}",
        f"- Findings: {report.finding_count}",
        f"- Exhaustive JSON: `{json_path}`",
        "",
        "## Finding Counts",
        "",
    ]
    for finding_type, count in report.finding_counts.items():
        lines.append(f"- {finding_type}: {count}")
    lines.extend(["", "## Non-Manifest Finding Counts", ""])
    lines.append(f"- total: {report.non_manifest_finding_count}")
    for finding_type, count in report.non_manifest_finding_counts.items():
        lines.append(f"- {finding_type}: {count}")
    lines.extend(["", "## Source Manifest Finding Counts", ""])
    lines.append(f"- total: {report.source_manifest_finding_count}")
    for finding_type, count in report.source_manifest_finding_counts.items():
        lines.append(f"- {finding_type}: {count}")
    lines.extend(["", "## Root-Cause Classes", ""])
    for finding_type in report.finding_counts:
        lines.append(f"- {finding_type}: {_ROOT_CAUSES.get(finding_type, 'unclassified')}")
    lines.extend(["", "## Highest-Risk Pages", ""])
    for summary in sorted(report.page_summaries, key=lambda item: -item.finding_count)[:25]:
        if summary.finding_count == 0:
            continue
        lines.append(
            f"- [[{summary.page_id}]]: {summary.finding_count} finding(s), "
            f"{summary.cited_item_count} cited item(s) - {summary.title}"
        )
    lines.extend(["", "## Representative Findings", ""])
    for finding in report.findings[:200]:
        lines.append(
            f"- {finding.finding_type} on [[{finding.page_id}]] line {finding.line_no}: "
            f"{finding.source_range_id}; {finding.root_cause}; "
            f"section `{finding.section_path}`; excerpt `{finding.excerpt}`"
        )
    return "\n".join(lines).strip() + "\n"


def _audit_page(
    page_id: str, title: str, body: str, index: _LedgerIndex
) -> tuple[list[ProvenanceFinding], int]:
    findings: list[ProvenanceFinding] = []
    page_terms = _topic_terms(f"{title} {page_id}")
    seen: Counter[str] = Counter()
    cited_ranges: list[str] = []
    lines = body.splitlines()
    for line_no, line in enumerate(lines, start=1):
        line_ranges = tuple(_SOURCE_RANGE.findall(line))
        for source_range_id in line_ranges:
            seen[source_range_id] += 1
            cited_ranges.append(source_range_id)
            evidence = index.evidence(source_range_id)
            if evidence is None:
                findings.append(
                    _finding(page_id, title, line_no, source_range_id, "missing-ledger-range", line)
                )
                continue
            findings.extend(
                _evidence_findings(
                    page_id, title, line_no, line, page_terms, evidence, len(line_ranges)
                )
            )
    orders = [index.source_order(source_range_id) for source_range_id in cited_ranges]
    orders = [order for order in orders if order > 0]
    if orders:
        midpoint = sorted(orders)[len(orders) // 2]
        for source_range_id in sorted(set(cited_ranges)):
            order = index.source_order(source_range_id)
            if order > 0 and abs(order - midpoint) > 1_200:
                evidence = index.evidence(source_range_id)
                findings.append(
                    _finding(
                        page_id,
                        title,
                        _first_line(lines, source_range_id),
                        source_range_id,
                        "range-order-outlier",
                        evidence.excerpt if evidence is not None else source_range_id,
                        evidence.section_path if evidence is not None else "",
                    )
                )
    return findings, len(cited_ranges)


def _evidence_findings(
    page_id: str,
    title: str,
    line_no: int,
    line: str,
    page_terms: frozenset[str],
    evidence: _Evidence,
    line_range_count: int,
) -> list[ProvenanceFinding]:
    findings: list[ProvenanceFinding] = []
    if evidence.context_pointer:
        findings.append(
            _finding(
                page_id,
                title,
                line_no,
                evidence.source_range_id,
                "context-pointer-projected",
                line,
                evidence.section_path,
            )
        )
    if evidence.fragmentary and not (line_range_count > 1 and not _fragmentary(line)):
        findings.append(
            _finding(
                page_id,
                title,
                line_no,
                evidence.source_range_id,
                "fragmentary-statement",
                line,
                evidence.section_path,
            )
        )
    evidence_terms = _topic_terms(f"{evidence.section_path} {evidence.excerpt}")
    if evidence.structure_only:
        findings.append(
            _finding(
                page_id,
                title,
                line_no,
                evidence.source_range_id,
                "structure-only-range",
                line,
                evidence.section_path,
            )
        )
        return findings
    if page_terms and evidence_terms and not page_terms.intersection(evidence_terms):
        finding_type = (
            "technical-atom-topic-gap" if evidence.has_technical_atom else "topic-support-gap"
        )
        findings.append(
            _finding(
                page_id,
                title,
                line_no,
                evidence.source_range_id,
                finding_type,
                line,
                evidence.section_path,
            )
        )
    return findings


@dataclass(frozen=True)
class _Evidence:
    source_range_id: str
    section_path: str
    excerpt: str
    has_technical_atom: bool
    context_pointer: bool
    fragmentary: bool
    structure_only: bool


class _LedgerIndex:
    def __init__(
        self,
        ledger: dict[str, Any],
        structure: dict[str, Any],
        source_coverage: dict[str, Any],
        projection_context: dict[str, Any],
    ) -> None:
        self._nodes = {node["structure_node_id"]: node for node in structure["structure_nodes"]}
        self._nodes_by_range = {
            node.get("source_range_id", ""): node
            for node in structure["structure_nodes"]
            if node.get("source_range_id")
        }
        nodes_by_order = sorted(
            (
                int(node.get("source_order", 0) or 0),
                node["structure_node_id"],
            )
            for node in structure["structure_nodes"]
            if int(node.get("source_order", 0) or 0) > 0
        )
        self._node_orders = [item[0] for item in nodes_by_order]
        self._node_ids_by_order = [item[1] for item in nodes_by_order]
        self._entries_by_range: dict[str, list[dict[str, Any]]] = defaultdict(list)
        self._atoms_by_range: dict[str, list[dict[str, Any]]] = defaultdict(list)
        self._source_records_by_range: dict[str, list[dict[str, Any]]] = defaultdict(list)
        self._context_blocks_by_range: dict[str, list[dict[str, Any]]] = defaultdict(list)
        self._atom_frames_by_range: dict[str, list[dict[str, Any]]] = defaultdict(list)
        self._entries_by_id = {
            entry["ledger_entry_id"]: entry
            for entry in ledger["entries"]
            if entry.get("ledger_entry_id")
        }
        self._atoms_by_id = {
            atom["technical_atom_id"]: atom
            for atom in ledger["technical_atoms"]
            if atom.get("technical_atom_id")
        }
        for entry in ledger["entries"]:
            self._entries_by_range[entry["source_range_id"]].append(entry)
        for atom in ledger["technical_atoms"]:
            self._atoms_by_range[atom["source_range_id"]].append(atom)
        for record in source_coverage.get("records", ()):
            for source_range_id in record.get("source_range_ids", ()):
                self._source_records_by_range[source_range_id].append(record)
        for block in projection_context.get("evidence_blocks", ()):
            range_ids = block.get("source_range_ids") or (block.get("source_range_id", ""),)
            for source_range_id in range_ids:
                if source_range_id:
                    self._context_blocks_by_range[source_range_id].append(block)
        for frame in projection_context.get("atom_frames", ()):
            for source_range_id in frame.get("source_range_ids", ()):
                if source_range_id:
                    self._atom_frames_by_range[source_range_id].append(frame)
        self._order_by_range = {
            item["source_range_id"]: item.get("source_order", 0)
            for item in structure.get("dispositions", ())
        }
        self._disposition_by_range = {
            item["source_range_id"]: item.get("disposition", "")
            for item in structure.get("dispositions", ())
        }

    def source_order(self, source_range_id: str) -> int:
        return int(self._order_by_range.get(source_range_id, 0) or 0)

    def evidence(self, source_range_id: str) -> _Evidence | None:
        entries = self._entries_by_range.get(source_range_id, [])
        atoms = self._atoms_by_range.get(source_range_id, [])
        records = self._source_records_by_range.get(source_range_id, [])
        context_blocks = self._context_blocks_by_range.get(source_range_id, [])
        atom_frames = self._atom_frames_by_range.get(source_range_id, [])
        entries = _dedupe_records(
            entries
            + [
                self._entries_by_id[item]
                for item in _record_ids(records, "ledger_entry_ids")
                if item in self._entries_by_id
            ]
        )
        atoms = _dedupe_records(
            atoms
            + [
                self._atoms_by_id[item]
                for item in _record_ids(records, "technical_atom_ids")
                if item in self._atoms_by_id
            ]
        )
        if (
            not entries
            and not atoms
            and not records
            and not context_blocks
            and not atom_frames
            and source_range_id not in self._order_by_range
        ):
            return None
        node_ids = [node_id for entry in entries for node_id in entry.get("structure_node_ids", ())]
        section_path = _context_section_path(context_blocks) or self._section_path(
            node_ids[0] if node_ids else self._structure_node_for_range(source_range_id)
        )
        excerpt = (
            _excerpt(entries, atoms)
            or _context_excerpt(context_blocks, atom_frames)
            or _record_excerpt(records, source_range_id)
        )
        return _Evidence(
            source_range_id=source_range_id,
            section_path=section_path,
            excerpt=excerpt,
            has_technical_atom=bool(
                atoms or atom_frames or any(e.get("technical_atom_id") for e in entries)
            ),
            context_pointer=any(_context_pointer(entry) for entry in entries),
            fragmentary=any(
                _fragmentary(entry.get("normalized_text") or entry.get("source_text", ""))
                for entry in entries
            )
            or (
                not entries
                and any(_fragmentary(block.get("source_text", "")) for block in context_blocks)
            ),
            structure_only=not entries and not atoms and not context_blocks and not atom_frames,
        )

    def _section_path(self, node_id: str) -> str:
        labels: list[str] = []
        seen: set[str] = set()
        current = self._nodes.get(node_id)
        while current is not None and current["structure_node_id"] not in seen:
            seen.add(current["structure_node_id"])
            if current.get("structure_node_kind") != "root":
                labels.append(current.get("heading_text", ""))
            current = self._nodes.get(current.get("parent_structure_node_id", ""))
        return " / ".join(reversed([label for label in labels if label.strip()]))

    def _structure_node_for_range(self, source_range_id: str) -> str:
        exact = self._nodes_by_range.get(source_range_id)
        if exact is not None:
            return str(exact["structure_node_id"])
        order = self.source_order(source_range_id)
        if order <= 0:
            return ""
        index = bisect_right(self._node_orders, order) - 1
        if index < 0:
            return ""
        return str(self._node_ids_by_order[index])


def _artifact_json(path: Path, key: str) -> dict[str, Any]:
    if not path.exists():
        return {}
    data = cast(dict[str, Any], json.loads(path.read_text(encoding="utf-8")))
    value = data.get(key, data)
    return cast(dict[str, Any], value)


def _page_title(body: str) -> str:
    for line in body.splitlines():
        if line.startswith("# "):
            return line.removeprefix("# ").strip()
    return ""


def _excerpt(entries: list[dict[str, Any]], atoms: list[dict[str, Any]]) -> str:
    texts = [entry.get("normalized_text") or entry.get("source_text", "") for entry in entries]
    if not texts:
        texts = [json.dumps(atom.get("payload", {}), sort_keys=True) for atom in atoms]
    return " ".join(text.strip() for text in texts if text.strip())[:320]


def _record_excerpt(records: list[dict[str, Any]], source_range_id: str) -> str:
    if not records:
        return source_range_id
    pieces: list[str] = []
    for record in records[:3]:
        pieces.append(
            " ".join(
                text
                for text in (
                    record.get("coverage_kind", ""),
                    record.get("coverage_status", ""),
                    record.get("element_kind", ""),
                    record.get("heading_path", ""),
                    record.get("extracted_unit_disposition", ""),
                    record.get("excluded_reason", ""),
                )
                if text
            )
        )
    return " | ".join(piece for piece in pieces if piece)[:320]


def _context_section_path(blocks: list[dict[str, Any]]) -> str:
    for block in blocks:
        section = str(block.get("section_label", "")).strip()
        if section:
            return section
    return ""


def _context_excerpt(blocks: list[dict[str, Any]], frames: list[dict[str, Any]]) -> str:
    texts = [str(block.get("source_text", "")).strip() for block in blocks]
    if not texts:
        texts = [
            " ".join(
                text
                for text in (
                    str(frame.get("label", "")),
                    str(frame.get("technical_atom_kind", "")),
                )
                if text
            )
            for frame in frames
        ]
    return " ".join(text for text in texts if text)[:320]


def _record_ids(records: list[dict[str, Any]], key: str) -> list[str]:
    ids: list[str] = []
    for record in records:
        ids.extend(str(item) for item in record.get(key, ()) if item)
    return ids


def _dedupe_records(records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    seen: set[int] = set()
    deduped: list[dict[str, Any]] = []
    for record in records:
        record_id = id(record)
        if record_id in seen:
            continue
        seen.add(record_id)
        deduped.append(record)
    return deduped


def _topic_terms(text: str) -> frozenset[str]:
    terms: list[str] = []
    for raw in _WORD.findall(str(text).lower()[:4_000]):
        if len(raw) < 3 or raw.isdigit():
            continue
        term = _audit_singular(raw)
        if term in _AUDIT_STOPWORDS:
            continue
        terms.append(term)
    return frozenset(terms)


def _audit_singular(token: str) -> str:
    if token.endswith("ies") and len(token) > 4:
        return token[:-3] + "y"
    if token.endswith(("ches", "shes")) and len(token) > 5:
        return token[:-2]
    if token.endswith("s") and not token.endswith("ss") and len(token) > 4:
        return token[:-1]
    return token


def _context_pointer(entry: dict[str, Any]) -> bool:
    scope = entry.get("spatial_scope") or {}
    return bool(
        entry.get("ledger_entry_kind") in {"claim", "event"}
        and scope.get("spatial_kind") == "relative-location"
        and not scope.get("normalized_spatial_value")
        and "identity" in entry.get("claim_role_tags", ())
    )


def _fragmentary(text: str) -> bool:
    stripped = " ".join(text.split())
    if not stripped:
        return False
    first = stripped[0]
    lowered = stripped.lower()
    return bool(
        first.islower()
        or lowered.startswith(("and ", "or ", "but ", "because ", "believe in "))
        or lowered.endswith((",", " and", " or", " but"))
    )


def _finding(
    page_id: str,
    title: str,
    line_no: int,
    source_range_id: str,
    finding_type: str,
    line: str,
    section_path: str = "",
) -> ProvenanceFinding:
    return ProvenanceFinding(
        page_id=page_id,
        line_no=line_no,
        source_range_id=source_range_id,
        finding_type=finding_type,
        severity="warning",
        root_cause=_ROOT_CAUSES.get(finding_type, "unclassified"),
        title=title,
        section_path=section_path,
        excerpt=_clean_excerpt(line),
    )


def _first_line(lines: list[str], source_range_id: str) -> int:
    for line_no, line in enumerate(lines, start=1):
        if source_range_id in line:
            return line_no
    return 0


def _clean_excerpt(text: str) -> str:
    return " ".join(_WORD.findall(text))[:220]


if __name__ == "__main__":
    main()
