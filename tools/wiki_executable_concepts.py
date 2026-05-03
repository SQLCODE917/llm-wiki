#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import sys
from collections import Counter
from dataclasses import dataclass
from datetime import date
from pathlib import Path

from wiki_common import iter_content_pages, parse_frontmatter, section


REPORT_PATH = Path("wiki/_executable-report.md")


@dataclass(frozen=True)
class Issue:
    level: str
    path: str
    message: str


def main() -> int:
    parser = argparse.ArgumentParser(description="Check executable concept links and formula/procedure implementation backlog.")
    parser.add_argument("--check", action="store_true", help="do not write wiki/_executable-report.md")
    args = parser.parse_args()

    issues = run_checks()
    report = render_report(issues)
    if not args.check:
        REPORT_PATH.write_text(report)
    print(report)
    return 1 if any(issue.level == "FAIL" for issue in issues) else 0


def run_checks() -> list[Issue]:
    issues: list[Issue] = []
    for page in iter_content_pages():
        fm = parse_frontmatter(page)
        page_type = fm.data.get("type")
        if page_type not in {"concept", "procedure", "reference"}:
            continue
        body = fm.body
        executable = section(body, "## Executable implementation")
        formula_like = implies_executable(body)
        if executable:
            issues.extend(check_executable_links(page, executable))
        elif formula_like:
            issues.append(
                Issue(
                    "WARN",
                    page.as_posix(),
                    "page appears to contain a formula or deterministic procedure but has no ## Executable implementation section",
                )
            )
    return issues


def check_executable_links(page: Path, executable: str) -> list[Issue]:
    issues: list[Issue] = []
    links = executable_links(page, executable_start_line(page))
    src_links = [link for link in links if "packages/concepts/src/" in link.as_posix()]
    test_links = [link for link in links if "packages/concepts/tests/" in link.as_posix()]
    if not src_links:
        issues.append(Issue("FAIL", page.as_posix(), "## Executable implementation must link to packages/concepts/src/*.ts"))
    if not test_links:
        issues.append(Issue("FAIL", page.as_posix(), "## Executable implementation must link to packages/concepts/tests/*.ts"))
    for link in src_links + test_links:
        if not link.exists():
            issues.append(Issue("FAIL", page.as_posix(), f"executable link target does not exist: {link.as_posix()}"))
    return issues


def executable_links(page: Path, start_line: int) -> list[Path]:
    links: list[Path] = []
    cwd = Path.cwd().resolve()
    for line_number, line in enumerate(page.read_text().splitlines(), start=1):
        if line_number < start_line:
            continue
        if line_number > start_line and line.startswith("## "):
            break
        for match in re.finditer(r"\[[^\]]+\]\(([^)]+)\)", line):
            target = match.group(1).split("#", 1)[0].strip()
            if not target or re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", target):
                continue
            resolved = (page.parent / target).resolve()
            try:
                links.append(resolved.relative_to(cwd))
            except ValueError:
                continue
    return links


def executable_start_line(page: Path) -> int:
    for line_number, line in enumerate(page.read_text().splitlines(), start=1):
        if line.strip() == "## Executable implementation":
            return line_number
    return 0


def implies_executable(body: str) -> bool:
    text = body.lower()
    if "not covered in sources" in text:
        return False
    formula_patterns = [
        r"\bformula\b",
        r"\bcalculate\b",
        r"\bcalculator\b",
        r"\bfunction\b",
        r"\b[a-z]\s*=\s*[^\\n|]{3,}",
        r"\b\d+(?:\.\d+)?\s*[*/^]\s*\d+",
    ]
    deterministic_procedure_patterns = [
        r"\binput\b.*\boutput\b",
        r"\bstep\s+\d+\b",
    ]
    return any(re.search(pattern, text) for pattern in formula_patterns + deterministic_procedure_patterns)


def render_report(issues: list[Issue]) -> str:
    counts = Counter(issue.level for issue in issues)
    lines = [
        "# Executable Concepts Report",
        "",
        f"Generated: {date.today().isoformat()}",
        "",
        "## Summary",
        "",
        f"- WARN: {counts.get('WARN', 0)}",
        f"- FAIL: {counts.get('FAIL', 0)}",
        "",
    ]
    for level in ("FAIL", "WARN"):
        selected = [issue for issue in issues if issue.level == level]
        lines.extend([f"## {level}", ""])
        if selected:
            lines.extend(f"- `{issue.path}` - {issue.message}" for issue in selected)
        else:
            lines.append("None.")
        lines.append("")
    return "\n".join(lines)


if __name__ == "__main__":
    sys.exit(main())
