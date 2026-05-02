#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from dataclasses import dataclass
from datetime import date
from pathlib import Path

from wiki_common import (
    CONTENT_DIRS,
    SOURCE_HEADINGS,
    code_paths,
    first_h1,
    h2_headings,
    is_content_page,
    iter_content_pages,
    markdown_links,
    page_node_id,
    parse_frontmatter,
    section,
)


@dataclass(frozen=True)
class Issue:
    level: str
    path: str
    message: str


REQUIRED_GENERAL_KEYS = ["title", "type", "tags", "status", "last_updated", "sources"]
REQUIRED_SOURCE_KEYS = [
    "title",
    "type",
    "source_id",
    "source_type",
    "raw_path",
    "normalized_path",
    "status",
    "last_updated",
    "tags",
    "sources",
]
VALID_TYPES = {"source", "entity", "concept", "procedure", "reference", "analysis"}
SPECIAL_WIKI_FILES = {
    Path("wiki/index.md"),
    Path("wiki/log.md"),
    Path("wiki/_linter-report.md"),
    Path("wiki/_grounding-report.md"),
}


def main() -> int:
    parser = argparse.ArgumentParser(description="Lint the LLM-Wiki markdown layer.")
    parser.add_argument("--append-log", action="store_true", help="append a lint entry to wiki/log.md")
    args = parser.parse_args()

    issues = run_lint()
    report = render_report(issues)
    report_path = Path("wiki/_linter-report.md")
    report_path.write_text(report)
    print(report)

    if args.append_log:
        append_log(issues)

    return 1 if any(issue.level == "FAIL" for issue in issues) else 0


def run_lint() -> list[Issue]:
    issues: list[Issue] = []
    content_pages = list(iter_content_pages())

    for path in sorted(Path("wiki").rglob("*.md")):
        if path in SPECIAL_WIKI_FILES:
            continue
        if not is_content_page(path):
            issues.append(Issue("WARN", path.as_posix(), "markdown file is outside a known content directory"))

    for path in content_pages:
        issues.extend(lint_page(path))

    issues.extend(lint_links(content_pages))
    issues.extend(lint_index(content_pages))
    issues.extend(lint_graph(content_pages))
    issues.extend(lint_log())
    return issues


def lint_page(path: Path) -> list[Issue]:
    issues: list[Issue] = []
    fm = parse_frontmatter(path)
    for error in fm.errors:
        issues.append(Issue("FAIL", path.as_posix(), error))

    required = REQUIRED_SOURCE_KEYS if path.parts[1] == "sources" else REQUIRED_GENERAL_KEYS
    for key in required:
        if key not in fm.data:
            issues.append(Issue("FAIL", path.as_posix(), f"missing frontmatter key {key!r}"))

    page_type = fm.data.get("type")
    if page_type not in VALID_TYPES:
        issues.append(Issue("FAIL", path.as_posix(), f"invalid type {page_type!r}"))

    if first_h1(fm.body) is None:
        issues.append(Issue("FAIL", path.as_posix(), "missing H1 title"))

    if path.parts[1] == "sources":
        issues.extend(lint_source_page(path, fm))
    return issues


def lint_source_page(path: Path, fm) -> list[Issue]:
    issues: list[Issue] = []
    if h2_headings(fm.body) != SOURCE_HEADINGS:
        issues.append(Issue("FAIL", path.as_posix(), "source page headings do not match required order"))

    slug = path.stem
    if fm.data.get("source_id") != slug:
        issues.append(Issue("FAIL", path.as_posix(), f"source_id must be {slug!r}"))
    if fm.data.get("raw_path") != f"../../raw/imported/{slug}/":
        issues.append(Issue("FAIL", path.as_posix(), "raw_path must point to imported source directory"))
    if fm.data.get("normalized_path") != f"../../raw/normalized/{slug}/":
        issues.append(Issue("FAIL", path.as_posix(), "normalized_path must point to normalized source directory"))

    key_claims = section(fm.body, "## Key claims")
    claim_count = len(
        [line for line in key_claims.splitlines() if re.match(r"^\s*(?:[-*]\s+|\d+[.]\s+)", line)]
    )
    if claim_count == 0:
        issues.append(Issue("FAIL", path.as_posix(), "source page has no key claims"))

    related = section(fm.body, "## Related pages")
    if not related or related.lower() in {"none.", "not covered in sources"}:
        issues.append(Issue("WARN", path.as_posix(), "source page has no related pages or candidate pages"))
    if code_paths(related):
        issues.append(Issue("WARN", path.as_posix(), "Related pages lists candidate paths not created yet"))

    if re.search(r"DE \(Dark Age\)", path.read_text(), flags=re.IGNORECASE):
        issues.append(Issue("FAIL", path.as_posix(), "contains unsupported expansion DE (Dark Age)"))
    return issues


def lint_links(paths: list[Path]) -> list[Issue]:
    issues: list[Issue] = []
    for path in paths + [Path("wiki/index.md")]:
        if not path.exists():
            continue
        for link in markdown_links(path):
            if link.resolved and not link.resolved.exists():
                issues.append(Issue("FAIL", f"{path.as_posix()}:{link.line}", f"broken Markdown link {link.target!r}"))
    return issues


def lint_index(content_pages: list[Path]) -> list[Issue]:
    issues: list[Issue] = []
    index = Path("wiki/index.md")
    if not index.exists():
        return [Issue("FAIL", index.as_posix(), "missing index")]

    linked = set()
    for link in markdown_links(index):
        if link.resolved and link.resolved.exists():
            try:
                linked.add(link.resolved.relative_to(Path.cwd()).as_posix())
            except ValueError:
                linked.add(link.resolved.as_posix())

    for page in content_pages:
        resolved = page.resolve()
        try:
            key = resolved.relative_to(Path.cwd()).as_posix()
        except ValueError:
            key = resolved.as_posix()
        if key not in linked:
            issues.append(Issue("WARN", page.as_posix(), "content page is missing from wiki/index.md"))
    return issues


def lint_graph(content_pages: list[Path]) -> list[Issue]:
    graph_path = Path("wiki/_graph.json")
    if not graph_path.exists():
        return [Issue("FAIL", graph_path.as_posix(), "missing graph")]

    try:
        graph = json.loads(graph_path.read_text())
    except json.JSONDecodeError as exc:
        return [Issue("FAIL", graph_path.as_posix(), f"invalid JSON: {exc}")]

    nodes = graph.get("nodes", {})
    if not isinstance(nodes, dict):
        return [Issue("FAIL", graph_path.as_posix(), "nodes must be an object")]

    issues: list[Issue] = []
    expected = {page_node_id(path): path.as_posix() for path in content_pages}
    for node_id, page_path in expected.items():
        if node_id not in nodes:
            issues_msg = f"content page missing from graph as {node_id}"
            issues.append(Issue("FAIL", page_path, issues_msg))

    for node_id, node in nodes.items():
        if not isinstance(node, dict):
            issues.append(Issue("FAIL", graph_path.as_posix(), f"{node_id} node must be an object"))
            continue
        node_path = node.get("path")
        if not isinstance(node_path, str) or not Path(node_path).exists():
            issues.append(Issue("FAIL", graph_path.as_posix(), f"{node_id} points to missing file {node_path!r}"))
    return issues


def lint_log() -> list[Issue]:
    log = Path("wiki/log.md")
    if not log.exists():
        return [Issue("FAIL", log.as_posix(), "missing log")]

    issues: list[Issue] = []
    for line_no, line in enumerate(log.read_text().splitlines(), start=1):
        if line.startswith("## ") and not re.match(r"^## \[\d{4}-\d{2}-\d{2}\] ", line):
            issues.append(Issue("WARN", f"{log.as_posix()}:{line_no}", "log heading is not grep-able"))
    if "contradiction |" in log.read_text() and "resolved" not in log.read_text().lower():
        issues.append(Issue("WARN", log.as_posix(), "possible unresolved contradiction entry"))
    return issues


def render_report(issues: list[Issue]) -> str:
    counts = Counter(issue.level for issue in issues)
    lines = [
        "# Wiki Linter Report",
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


def append_log(issues: list[Issue]) -> None:
    counts = Counter(issue.level for issue in issues)
    summary = f"{counts.get('FAIL', 0)} FAIL | {counts.get('WARN', 0)} WARN"
    entry = "\n".join(
        [
            "",
            f"## [{date.today().isoformat()}] lint | {summary}",
            "",
            f"- FAIL: {counts.get('FAIL', 0)}",
            f"- WARN: {counts.get('WARN', 0)}",
            "- Report: wiki/_linter-report.md",
            "",
            "---",
            "",
        ]
    )
    Path("wiki/log.md").write_text(Path("wiki/log.md").read_text().rstrip() + entry)


if __name__ == "__main__":
    sys.exit(main())
