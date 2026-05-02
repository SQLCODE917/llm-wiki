#!/usr/bin/env python3
from __future__ import annotations

import argparse
import sys
from datetime import date
from pathlib import Path


OPERATIONS = {
    "scaffold",
    "ingest",
    "query",
    "lint",
    "cleanup",
    "proposal",
    "contradiction",
    "schema-change",
    "todo",
}


def main() -> int:
    parser = argparse.ArgumentParser(description="Append a formatted entry to wiki/log.md.")
    parser.add_argument("operation", choices=sorted(OPERATIONS))
    parser.add_argument("summary")
    parser.add_argument("-d", "--detail", action="append", default=[], help="detail bullet; repeatable")
    parser.add_argument("--date", default=date.today().isoformat(), help="entry date in YYYY-MM-DD format")
    parser.add_argument("--dry-run", action="store_true", help="print the entry without writing")
    args = parser.parse_args()

    entry = render_entry(args.date, args.operation, args.summary, args.detail)
    if args.dry_run:
        print(entry, end="")
        return 0

    log_path = Path("wiki/log.md")
    current = log_path.read_text() if log_path.exists() else "# Log\n"
    separator = "" if current.endswith("\n") else "\n"
    log_path.write_text(current + separator + entry)
    print(f"appended {args.operation} entry to {log_path}")
    return 0


def render_entry(entry_date: str, operation: str, summary: str, details: list[str]) -> str:
    bullets = details or ["No additional details."]
    lines = [
        "",
        f"## [{entry_date}] {operation} | {summary}",
        "",
        *(f"- {detail}" for detail in bullets),
        "",
        "---",
        "",
    ]
    return "\n".join(lines)


if __name__ == "__main__":
    sys.exit(main())
