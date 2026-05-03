#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import subprocess
import sys
from collections import Counter
from datetime import date
from pathlib import Path

from wiki_common import iter_content_pages, parse_frontmatter


VALID_STATUSES = {"draft", "reviewed", "stable"}
TRANSITIONS = {
    "draft": {"draft", "reviewed"},
    "reviewed": {"reviewed", "stable", "draft"},
    "stable": {"stable", "reviewed", "draft"},
}


def main() -> int:
    parser = argparse.ArgumentParser(description="Inspect or update curator review status for wiki pages.")
    parser.add_argument("page", nargs="*", help="page(s) to update; omit with --check/--list")
    parser.add_argument("--set", choices=sorted(VALID_STATUSES), dest="new_status")
    parser.add_argument("--reason", help="required when changing status")
    parser.add_argument("--reviewer", default="curator")
    parser.add_argument("--check", action="store_true", help="validate statuses without changing pages")
    parser.add_argument("--list", action="store_true", help="print status counts and page list")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    if args.check:
        failures = status_failures()
        for failure in failures:
            print(f"FAIL: {failure}")
        if failures:
            return 1
        print("PASS: curator statuses are valid")
        return 0
    if args.list or not args.new_status:
        print(render_status_list())
        return 0
    if not args.page:
        print("FAIL: pass at least one page when using --set", file=sys.stderr)
        return 2
    if not args.reason:
        print("FAIL: --reason is required when changing status", file=sys.stderr)
        return 2

    changed: list[Path] = []
    for raw in args.page:
        page = Path(raw)
        if not page.exists():
            print(f"FAIL: missing page {page}", file=sys.stderr)
            return 1
        old_status = str(parse_frontmatter(page).data.get("status") or "")
        if args.new_status not in TRANSITIONS.get(old_status, set()):
            print(f"FAIL: cannot move {page} from {old_status!r} to {args.new_status!r}", file=sys.stderr)
            return 1
        if args.dry_run:
            print(f"would set {page} from {old_status} to {args.new_status}")
        else:
            update_status(page, args.new_status, args.reviewer)
            changed.append(page)
            print(f"updated {page}: {old_status} -> {args.new_status}")

    if changed and not args.dry_run:
        details = [f"{page.as_posix()} -> {args.new_status}" for page in changed]
        details.append(f"Reviewer: {args.reviewer}")
        details.append(f"Reason: {args.reason}")
        command = ["python3", "tools/wiki_log.py", "cleanup", f"curator marked {len(changed)} page(s) {args.new_status}"]
        for detail in details:
            command.extend(["--detail", detail])
        subprocess.run(command, check=True)
    return 0


def status_failures() -> list[str]:
    failures: list[str] = []
    for page in iter_content_pages():
        fm = parse_frontmatter(page)
        status = fm.data.get("status")
        if status not in VALID_STATUSES:
            failures.append(f"{page.as_posix()}: invalid status {status!r}")
    return failures


def render_status_list() -> str:
    rows: list[tuple[str, str, str]] = []
    for page in iter_content_pages():
        fm = parse_frontmatter(page)
        rows.append((str(fm.data.get("status") or "missing"), str(fm.data.get("title") or page.stem), page.as_posix()))
    counts = Counter(status for status, _title, _page in rows)
    lines = ["# Curator Status", "", "## Summary", ""]
    for status in sorted(VALID_STATUSES | set(counts)):
        lines.append(f"- {status}: {counts.get(status, 0)}")
    lines.extend(["", "## Pages", "", "| Status | Page |", "|---|---|"])
    for status, title, page in sorted(rows):
        lines.append(f"| {status} | [{title}]({page}) |")
    return "\n".join(lines) + "\n"


def update_status(page: Path, new_status: str, reviewer: str) -> None:
    text = page.read_text()
    if not text.startswith("---\n"):
        raise SystemExit(f"FAIL: {page} has no frontmatter")
    end = text.find("\n---\n", 4)
    if end == -1:
        raise SystemExit(f"FAIL: {page} has unterminated frontmatter")
    raw = text[4:end]
    body = text[end + 5 :]
    raw = replace_or_add_key(raw, "status", new_status)
    raw = replace_or_add_key(raw, "last_updated", date.today().isoformat())
    raw = replace_or_add_key(raw, "reviewed_by", reviewer if new_status in {"reviewed", "stable"} else "")
    if new_status == "stable":
        raw = replace_or_add_key(raw, "stabilized_on", date.today().isoformat())
    else:
        raw = remove_key(raw, "stabilized_on")
    page.write_text("---\n" + raw.strip() + "\n---\n" + body)


def replace_or_add_key(frontmatter: str, key: str, value: str) -> str:
    if not value:
        return remove_key(frontmatter, key)
    line = f"{key}: {value}"
    pattern = re.compile(rf"^{re.escape(key)}:.*$", re.MULTILINE)
    if pattern.search(frontmatter):
        return pattern.sub(line, frontmatter)
    return frontmatter.rstrip() + "\n" + line + "\n"


def remove_key(frontmatter: str, key: str) -> str:
    return re.sub(rf"^{re.escape(key)}:.*\n?", "", frontmatter, flags=re.MULTILINE)


if __name__ == "__main__":
    sys.exit(main())
