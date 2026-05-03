#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import sys
from collections import Counter
from dataclasses import dataclass
from datetime import date
from pathlib import Path

from wiki_common import content_tokens, iter_content_pages, markdown_links, parse_frontmatter, section


@dataclass(frozen=True)
class Issue:
    level: str
    path: str
    message: str


def main() -> int:
    parser = argparse.ArgumentParser(description="Check wiki pages for source grounding.")
    parser.add_argument("--max-unsupported-claim-tokens", type=int, default=4)
    parser.add_argument("--check", action="store_true", help="print report but do not write wiki/_grounding-report.md")
    args = parser.parse_args()

    issues = run_grounding(args.max_unsupported_claim_tokens)
    report = render_report(issues)
    if not args.check:
        report_path = Path("wiki/_grounding-report.md")
        report_path.write_text(report)
    print(report)
    return 1 if any(issue.level == "FAIL" for issue in issues) else 0


def run_grounding(max_unsupported_claim_tokens: int) -> list[Issue]:
    issues: list[Issue] = []
    for path in iter_content_pages():
        fm = parse_frontmatter(path)
        page_type = fm.data.get("type")
        if page_type == "source":
            issues.extend(check_source_claims(path, fm, max_unsupported_claim_tokens))
        else:
            issues.extend(check_synthesized_page(path, fm))
    return issues


def check_source_claims(path: Path, fm, max_unsupported_claim_tokens: int) -> list[Issue]:
    issues: list[Issue] = []
    normalized_source = find_normalized_markdown(fm.data.get("normalized_path"))
    if normalized_source is None:
        issues.append(Issue("WARN", path.as_posix(), "could not find exactly one normalized markdown source"))
        return issues

    source_tokens = set(content_tokens(normalized_source.read_text()))
    claims = [
        line
        for line in section(fm.body, "## Key claims").splitlines()
        if re.match(r"^\s*(?:[-*]\s+|\d+[.]\s+)", line)
    ]
    for i, claim in enumerate(claims, start=1):
        claim_text = re.sub(r"^\s*(?:[-*]\s+|\d+[.]\s+)", "", claim).strip()
        unsupported = sorted(set(content_tokens(claim_text)) - source_tokens)
        if len(unsupported) > max_unsupported_claim_tokens:
            sample = ", ".join(unsupported[:8])
            issues.append(
                Issue(
                    "FAIL",
                    path.as_posix(),
                    f"key claim {i} has {len(unsupported)} tokens not found in normalized source: {sample}",
                )
            )
    return issues


def check_synthesized_page(path: Path, fm) -> list[Issue]:
    issues: list[Issue] = []
    sources = fm.data.get("sources")
    if not isinstance(sources, list) or not sources:
        issues.append(Issue("FAIL", path.as_posix(), "synthesized page has no frontmatter sources"))
        sources = []

    existing_source_links = []
    for source in sources:
        if not isinstance(source, str) or "sources/" not in source or not source.endswith(".md"):
            issues.append(Issue("FAIL", path.as_posix(), f"frontmatter source is not a source page path: {source!r}"))
            continue
        resolved = (path.parent / source).resolve()
        if not resolved.exists():
            issues.append(Issue("FAIL", path.as_posix(), f"frontmatter source path does not exist: {source!r}"))
        else:
            existing_source_links.append(resolved)

    body_source_links = [
        link for link in markdown_links(path) if link.resolved and "wiki/sources/" in link.resolved.as_posix()
    ]
    if existing_source_links and not body_source_links:
        issues.append(Issue("FAIL", path.as_posix(), "synthesized page does not link to a source page in the body"))
    return issues


def find_normalized_markdown(normalized_path: object) -> Path | None:
    if not isinstance(normalized_path, str):
        return None
    root = (Path("wiki/sources") / normalized_path).resolve()
    if not root.exists():
        return None
    matches = sorted(path for path in root.rglob("*.md") if path.is_file())
    if len(matches) != 1:
        return None
    return matches[0]


def render_report(issues: list[Issue]) -> str:
    counts = Counter(issue.level for issue in issues)
    lines = [
        "# Wiki Grounding Report",
        "",
        f"Generated: {date.today().isoformat()}",
        "",
        "## Summary",
        "",
        f"- PASS: {counts.get('PASS', 0)}",
        f"- WARN: {counts.get('WARN', 0)}",
        f"- FAIL: {counts.get('FAIL', 0)}",
        "",
    ]
    for level in ("FAIL", "WARN"):
        selected = [issue for issue in issues if issue.level == level]
        lines.extend([f"## {level}", ""])
        if not selected:
            lines.append("None.")
        else:
            lines.extend(f"- `{issue.path}` — {issue.message}" for issue in selected)
        lines.append("")
    return "\n".join(lines)


if __name__ == "__main__":
    sys.exit(main())
