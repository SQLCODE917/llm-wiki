#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import subprocess
import sys
from collections import Counter
from dataclasses import dataclass
from datetime import date
from pathlib import Path

from wiki_common import content_tokens, iter_content_pages, one_line, parse_frontmatter, section
from wiki_check_synthesis import strip_markdown


@dataclass(frozen=True)
class PageProfile:
    path: Path
    title: str
    page_type: str
    sources: tuple[str, ...]
    tokens: frozenset[str]
    summary: str


@dataclass(frozen=True)
class Finding:
    level: str
    left: PageProfile
    right: PageProfile
    jaccard: float
    containment: float
    shared: tuple[str, ...]
    message: str


def main() -> int:
    parser = argparse.ArgumentParser(description="Lexical duplicate/overlap lint for synthesized wiki pages.")
    parser.add_argument("--jaccard", type=float, default=0.34)
    parser.add_argument("--containment", type=float, default=0.68)
    parser.add_argument("--output", default="wiki/_semantic-linter-report.md")
    parser.add_argument("--append-log", action="store_true")
    parser.add_argument("--fail-on-warn", action="store_true")
    args = parser.parse_args()

    profiles = [profile for profile in (page_profile(path) for path in iter_content_pages()) if profile is not None]
    findings = find_overlaps(profiles, jaccard_threshold=args.jaccard, containment_threshold=args.containment)
    report = render_report(findings, profiles)
    output = Path(args.output)
    output.write_text(report)
    print(report)
    if args.append_log:
        append_log(findings, output)
    return 1 if args.fail_on_warn and findings else 0


def page_profile(path: Path) -> PageProfile | None:
    if path.parts[1] in {"sources", "analyses"}:
        return None
    fm = parse_frontmatter(path)
    page_type = str(fm.data.get("type") or "")
    if page_type not in {"concept", "entity", "procedure", "reference"}:
        return None
    title = str(fm.data.get("title") or path.stem.replace("-", " ").title())
    sources = tuple(str(source) for source in fm.data.get("sources") or [] if isinstance(source, str))
    summary = first_paragraph_after_h1(fm.body)
    text = " ".join(
        [
            title,
            summary,
            claims_text(section(fm.body, "## Source-backed details")),
            claims_text(section(fm.body, "## Reference data")),
        ]
    )
    tokens = frozenset(set(content_tokens(text)) - {"aoe2", "source", "page", "pages"})
    if len(tokens) < 12:
        return None
    return PageProfile(path, title, page_type, sources, tokens, one_line(summary, 140))


def claims_text(markdown: str) -> str:
    out: list[str] = []
    for line in markdown.splitlines():
        cells = split_table_row(line)
        if cells is None:
            continue
        normalized = [cell.strip().lower() for cell in cells]
        if not normalized or is_separator_row(cells) or "evidence" in normalized:
            continue
        if len(cells) >= 2:
            out.append(strip_markdown(cells[0]))
            out.append(strip_markdown(cells[1]))
    return " ".join(out)


def find_overlaps(
    profiles: list[PageProfile],
    *,
    jaccard_threshold: float,
    containment_threshold: float,
) -> list[Finding]:
    findings: list[Finding] = []
    for left_index, left in enumerate(profiles):
        for right in profiles[left_index + 1 :]:
            if not comparable(left, right):
                continue
            shared = left.tokens & right.tokens
            if len(shared) < 8:
                continue
            union = left.tokens | right.tokens
            jaccard = len(shared) / len(union)
            containment = len(shared) / min(len(left.tokens), len(right.tokens))
            if jaccard < jaccard_threshold and containment < containment_threshold:
                continue
            message = "possible duplicate or heavy overlap; review whether one page should link to, narrow, or absorb the other"
            findings.append(
                Finding(
                    "WARN",
                    left,
                    right,
                    jaccard,
                    containment,
                    tuple(sorted(shared)[:18]),
                    message,
                )
            )
    return sorted(findings, key=lambda item: (-item.containment, -item.jaccard, item.left.path.as_posix()))


def comparable(left: PageProfile, right: PageProfile) -> bool:
    if left.page_type != right.page_type:
        return False
    if set(left.sources) and set(right.sources) and not (set(left.sources) & set(right.sources)):
        return False
    title_shared = set(content_tokens(left.title)) & set(content_tokens(right.title))
    return bool(title_shared) or left.sources == right.sources


def render_report(findings: list[Finding], profiles: list[PageProfile]) -> str:
    counts = Counter(finding.level for finding in findings)
    lines = [
        "# Semantic Linter Report",
        "",
        f"Generated: {date.today().isoformat()}",
        "",
        "## Summary",
        "",
        f"- Pages checked: {len(profiles)}",
        f"- WARN: {counts.get('WARN', 0)}",
        "",
        "## WARN",
        "",
    ]
    if not findings:
        lines.append("None.")
    for finding in findings:
        lines.extend(
            [
                f"- `{finding.left.path.as_posix()}` <-> `{finding.right.path.as_posix()}` - {finding.message}",
                f"  - jaccard: {finding.jaccard:.2f}; containment: {finding.containment:.2f}",
                f"  - shared: {', '.join(finding.shared)}",
                f"  - left: {finding.left.summary or finding.left.title}",
                f"  - right: {finding.right.summary or finding.right.title}",
            ]
        )
    return "\n".join(lines) + "\n"


def append_log(findings: list[Finding], output: Path) -> None:
    summary = f"{len(findings)} semantic overlap warning(s)"
    command = [
        "python3",
        "tools/wiki_log.py",
        "lint",
        summary,
        "--detail",
        f"Semantic report: {output.as_posix()}",
        "--detail",
        f"WARN: {len(findings)}",
    ]
    subprocess.run(command, check=True)


def first_paragraph_after_h1(body: str) -> str:
    seen_h1 = False
    lines: list[str] = []
    for line in body.splitlines():
        stripped = line.strip()
        if stripped.startswith("# "):
            seen_h1 = True
            continue
        if not seen_h1:
            continue
        if not stripped:
            if lines:
                break
            continue
        if stripped.startswith("## "):
            break
        lines.append(stripped)
    return " ".join(lines)


def split_table_row(line: str) -> list[str] | None:
    stripped = line.strip()
    if not stripped.startswith("|") or not stripped.endswith("|"):
        return None
    return [cell.strip() for cell in stripped[1:-1].split("|")]


def is_separator_row(cells: list[str]) -> bool:
    return all(cell and set(cell) <= {"-", ":", " "} for cell in cells)


if __name__ == "__main__":
    sys.exit(main())
