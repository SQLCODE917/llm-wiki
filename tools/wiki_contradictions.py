#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import subprocess
import sys
from dataclasses import dataclass
from datetime import date
from pathlib import Path

from wiki_common import content_tokens, iter_content_pages, parse_frontmatter, section
from wiki_check_synthesis import strip_markdown


@dataclass(frozen=True)
class SourceClaim:
    page: Path
    row: int
    claim: str
    evidence: str
    locator: str
    tokens: frozenset[str]
    numbers: frozenset[str]


@dataclass(frozen=True)
class CandidateContradiction:
    left: SourceClaim
    right: SourceClaim
    reason: str
    shared: tuple[str, ...]


def main() -> int:
    parser = argparse.ArgumentParser(description="Deterministically scan source-page claims for possible contradictions.")
    parser.add_argument("--output", default="wiki/_contradiction-report.md")
    parser.add_argument("--append-log", action="store_true")
    args = parser.parse_args()

    source_claims = claims_by_source()
    findings = find_candidates(source_claims)
    report = render_report(source_claims, findings)
    output = Path(args.output)
    output.write_text(report)
    print(report)
    if args.append_log:
        append_log(findings, output)
    return 0


def claims_by_source() -> dict[Path, list[SourceClaim]]:
    out: dict[Path, list[SourceClaim]] = {}
    for page in iter_content_pages():
        if page.parts[1] != "sources":
            continue
        claims = parse_source_claims(page)
        if claims:
            out[page] = claims
    return out


def parse_source_claims(page: Path) -> list[SourceClaim]:
    fm = parse_frontmatter(page)
    key_claims = section(fm.body, "## Key claims")
    rows = table_rows(key_claims)
    claims: list[SourceClaim] = []
    header_seen = False
    row_number = 0
    for cells in rows:
        normalized = [cell.strip().lower() for cell in cells]
        if normalized == ["claim", "evidence", "locator"]:
            header_seen = True
            continue
        if not header_seen or is_separator_row(cells) or len(cells) != 3:
            continue
        row_number += 1
        claim = strip_markdown(cells[0])
        evidence = strip_markdown(cells[1])
        locator = strip_markdown(cells[2])
        tokens = frozenset(content_tokens(claim))
        claims.append(
            SourceClaim(
                page=page,
                row=row_number,
                claim=claim,
                evidence=evidence,
                locator=locator,
                tokens=tokens,
                numbers=frozenset(re.findall(r"\b\d+(?:[.]\d+)?%?\b", claim + " " + evidence)),
            )
        )
    return claims


def find_candidates(claims_by_page: dict[Path, list[SourceClaim]]) -> list[CandidateContradiction]:
    substantial_pages = [page for page, claims in claims_by_page.items() if len(claims) >= 5]
    if len(substantial_pages) < 2:
        return []
    findings: list[CandidateContradiction] = []
    for index, left_page in enumerate(substantial_pages):
        for right_page in substantial_pages[index + 1 :]:
            for left in claims_by_page[left_page]:
                for right in claims_by_page[right_page]:
                    shared = left.tokens & right.tokens
                    if len(shared) < 4:
                        continue
                    reason = contradiction_reason(left, right)
                    if reason:
                        findings.append(CandidateContradiction(left, right, reason, tuple(sorted(shared)[:12])))
    return findings


def contradiction_reason(left: SourceClaim, right: SourceClaim) -> str:
    if left.numbers and right.numbers and left.numbers != right.numbers:
        return "overlapping claims cite different numeric values"
    left_text = left.claim.lower()
    right_text = right.claim.lower()
    opposing_pairs = [
        ("increase", "decrease"),
        ("improve", "hurt"),
        ("should", "should not"),
        ("can", "cannot"),
        ("always", "never"),
        ("faster", "slower"),
    ]
    for a, b in opposing_pairs:
        if (a in left_text and b in right_text) or (b in left_text and a in right_text):
            return f"overlapping claims contain opposing cues: {a!r}/{b!r}"
    return ""


def render_report(claims_by_page: dict[Path, list[SourceClaim]], findings: list[CandidateContradiction]) -> str:
    substantial = [page for page, claims in claims_by_page.items() if len(claims) >= 5]
    lines = [
        "# Contradiction Report",
        "",
        f"Generated: {date.today().isoformat()}",
        "",
        "## Summary",
        "",
        f"- Source pages with claims: {len(claims_by_page)}",
        f"- Substantial source pages: {len(substantial)}",
        f"- Candidate contradictions: {len(findings)}",
        "",
    ]
    if len(substantial) < 2:
        lines.extend(
            [
                "## Status",
                "",
                "TODO: fewer than two substantial source pages are available, so cross-source contradiction scanning is not meaningful yet.",
                "",
            ]
        )
    lines.extend(["## Candidate Contradictions", ""])
    if not findings:
        lines.append("None.")
    for finding in findings:
        lines.extend(
            [
                f"- {finding.reason}; shared: {', '.join(finding.shared)}",
                f"  - `{finding.left.page.as_posix()}` row {finding.left.row}: {finding.left.claim}",
                f"  - `{finding.right.page.as_posix()}` row {finding.right.row}: {finding.right.claim}",
            ]
        )
    return "\n".join(lines) + "\n"


def append_log(findings: list[CandidateContradiction], output: Path) -> None:
    command = [
        "python3",
        "tools/wiki_log.py",
        "lint",
        f"{len(findings)} candidate contradiction(s)",
        "--detail",
        f"Contradiction report: {output.as_posix()}",
    ]
    subprocess.run(command, check=True)


def table_rows(markdown: str) -> list[list[str]]:
    rows: list[list[str]] = []
    for line in markdown.splitlines():
        stripped = line.strip()
        if stripped.startswith("|") and stripped.endswith("|"):
            rows.append([cell.strip() for cell in stripped[1:-1].split("|")])
    return rows


def is_separator_row(cells: list[str]) -> bool:
    return all(cell and set(cell) <= {"-", ":", " "} for cell in cells)


if __name__ == "__main__":
    sys.exit(main())
