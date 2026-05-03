#!/usr/bin/env python3
from __future__ import annotations

import argparse
import subprocess
import sys
from dataclasses import dataclass
from datetime import date
from pathlib import Path


@dataclass(frozen=True)
class Check:
    name: str
    command: list[str]
    required: bool = True


def main() -> int:
    parser = argparse.ArgumentParser(description="Run scheduled deterministic wiki maintenance checks.")
    parser.add_argument("--append-log", action="store_true", help="append one maintenance lint entry to wiki/log.md")
    parser.add_argument("--skip-smoke", action="store_true", help="skip temp-copy smoke tests")
    args = parser.parse_args()

    checks = [
        Check("index", ["python3", "tools/wiki_index.py", "--check"]),
        Check("graph", ["python3", "tools/wiki_graph.py", "--check"]),
        Check("analysis", ["python3", "tools/wiki_check_analysis.py"]),
        Check("grounding", ["python3", "tools/wiki_grounding.py", "--check"]),
        Check("lint", ["python3", "tools/wiki_lint.py"]),
        Check("semantic", ["python3", "tools/wiki_semantic_lint.py"]),
        Check("contradictions", ["python3", "tools/wiki_contradictions.py"]),
        Check("executables", ["python3", "tools/wiki_executable_concepts.py", "--check"]),
        Check("curator-status", ["python3", "tools/wiki_curator_status.py", "--check"]),
    ]
    if not args.skip_smoke:
        checks.extend(
            [
                Check("phase0-smoke", ["python3", "tools/wiki_phase0_smoke_test.py"]),
                Check("query-smoke", ["python3", "tools/wiki_query_smoke_test.py"]),
            ]
        )

    results: list[tuple[Check, int]] = []
    for check in checks:
        print(f"\n## {check.name}")
        completed = subprocess.run(check.command, text=True)
        results.append((check, completed.returncode))

    report = render_report(results)
    report_path = Path("wiki/_maintenance-report.md")
    report_path.write_text(report)
    print("\n" + report)

    if args.append_log:
        append_log(results, report_path)

    return 1 if any(code != 0 and check.required for check, code in results) else 0


def render_report(results: list[tuple[Check, int]]) -> str:
    failed = [(check, code) for check, code in results if code != 0]
    lines = [
        "# Maintenance Report",
        "",
        f"Generated: {date.today().isoformat()}",
        "",
        "## Summary",
        "",
        f"- Checks run: {len(results)}",
        f"- Failed: {len(failed)}",
        "",
        "## Checks",
        "",
        "| Check | Status | Command |",
        "|---|---|---|",
    ]
    for check, code in results:
        status = "PASS" if code == 0 else f"FAIL:{code}"
        lines.append(f"| {check.name} | {status} | `{' '.join(check.command)}` |")
    return "\n".join(lines) + "\n"


def append_log(results: list[tuple[Check, int]], report_path: Path) -> None:
    failed = [(check, code) for check, code in results if code != 0]
    details = [
        f"Report: {report_path.as_posix()}",
        f"Checks run: {len(results)}",
        f"Failed: {len(failed)}",
    ]
    command = ["python3", "tools/wiki_log.py", "lint", f"maintenance {len(failed)} failure(s)"]
    for detail in details:
        command.extend(["--detail", detail])
    subprocess.run(command, check=True)


if __name__ == "__main__":
    sys.exit(main())
