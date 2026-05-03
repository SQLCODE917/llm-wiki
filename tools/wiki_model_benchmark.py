#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
import sys
import tempfile
import time
from dataclasses import dataclass
from datetime import date
from pathlib import Path


DEFAULTS_PATH = Path("tools/wiki_model_defaults.json")
REPORT_PATH = Path("wiki/_model-benchmark-report.md")
PHASES = ("phase1", "phase2", "query")


@dataclass(frozen=True)
class BenchResult:
    phase: str
    candidate: str
    returncode: int
    duration_s: float
    command: list[str]
    report: Path | None = None


def main() -> int:
    parser = argparse.ArgumentParser(description="Benchmark local-model candidates and update phase defaults.")
    parser.add_argument("--candidate", action="append", default=[], help="PROFILE or PROFILE:MODEL; repeatable")
    parser.add_argument("--slug", default="aoe2-basics")
    parser.add_argument("--normalized-source", help="explicit normalized markdown source")
    parser.add_argument("--phase", action="append", choices=PHASES, help="phase(s) to run; default: phase1/query, plus phase2 if a candidate path is supplied")
    parser.add_argument("--phase2-candidate", help="uncreated Related-pages path for Phase 2, e.g. ../concepts/example.md")
    parser.add_argument("--query", default="How should this source be used?")
    parser.add_argument("--timeout", type=int, default=900)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--update-defaults", action="store_true", help="write fastest passing candidates to tools/wiki_model_defaults.json")
    parser.add_argument("--report", default=REPORT_PATH.as_posix())
    args = parser.parse_args()

    candidates = args.candidate or [load_defaults().get("default_candidate", "local-4090")]
    phases = args.phase or ["phase1", "query"]
    if args.phase2_candidate and "phase2" not in phases:
        phases.append("phase2")

    commands = planned_commands(
        candidates=candidates,
        phases=phases,
        slug=args.slug,
        normalized_source=args.normalized_source,
        phase2_candidate=args.phase2_candidate,
        query=args.query,
        timeout=args.timeout,
    )
    if args.dry_run:
        for command in commands:
            print("$ " + " ".join(command))
        return 0

    results = [run_command(command) for command in commands]
    report_path = Path(args.report)
    report_path.write_text(render_report(results))
    print(f"wrote {report_path}")

    if args.update_defaults:
        update_defaults(results)

    return 0 if all(result.returncode == 0 for result in results) else 1


def planned_commands(
    *,
    candidates: list[str],
    phases: list[str],
    slug: str,
    normalized_source: str | None,
    phase2_candidate: str | None,
    query: str,
    timeout: int,
) -> list[list[str]]:
    commands: list[list[str]] = []
    for phase in phases:
        for candidate in candidates:
            if phase == "phase1":
                command = ["python3", "tools/wiki_phase1_benchmark.py", slug, "--candidate", candidate, "--timeout", str(timeout), "--repair-attempts", "1"]
                if normalized_source:
                    command.extend(["--normalized-source", normalized_source])
                commands.append(command)
            elif phase == "phase2":
                if not phase2_candidate:
                    continue
                report = Path(tempfile.gettempdir()) / f"wiki-model-benchmark-{slug}-{safe(candidate)}-phase2.md"
                command = [
                    "python3",
                    "tools/wiki_phase2_single.py",
                    slug,
                    phase2_candidate,
                    "--candidate",
                    candidate,
                    "--timeout",
                    str(timeout),
                    "--judge-timeout",
                    str(timeout),
                    "--repair-attempts",
                    "1",
                    "--judge-repair-attempts",
                    "1",
                    "--judge-batch",
                    "--report",
                    report.as_posix(),
                ]
                if normalized_source:
                    command.extend(["--normalized-source", normalized_source])
                commands.append(command)
            elif phase == "query":
                output = Path(tempfile.gettempdir()) / f"wiki-model-benchmark-{safe(candidate)}-query.md"
                commands.append(
                    [
                        "python3",
                        "tools/wiki_query.py",
                        query,
                        "--candidate",
                        candidate,
                        "--timeout",
                        str(timeout),
                        "--output",
                        output.as_posix(),
                    ]
                )
    return commands


def run_command(command: list[str]) -> BenchResult:
    phase = command_phase(command)
    candidate = command_candidate(command)
    start = time.monotonic()
    completed = subprocess.run(command, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, check=False)
    duration = time.monotonic() - start
    log_path = Path(tempfile.gettempdir()) / f"wiki-model-benchmark-{phase}-{safe(candidate)}.log"
    log_path.write_text("$ " + " ".join(command) + "\n" + completed.stdout)
    print(f"{phase} {candidate}: {'PASS' if completed.returncode == 0 else 'FAIL'} in {duration:.1f}s (log {log_path})")
    return BenchResult(phase=phase, candidate=candidate, returncode=completed.returncode, duration_s=duration, command=command, report=log_path)


def command_phase(command: list[str]) -> str:
    joined = " ".join(command)
    if "wiki_phase1_benchmark.py" in joined:
        return "phase1"
    if "wiki_phase2_single.py" in joined:
        return "phase2"
    if "wiki_query.py" in joined:
        return "query"
    return "unknown"


def command_candidate(command: list[str]) -> str:
    for index, part in enumerate(command):
        if part == "--candidate" and index + 1 < len(command):
            return command[index + 1]
    return "unknown"


def render_report(results: list[BenchResult]) -> str:
    lines = [
        "# Model Benchmark Report",
        "",
        f"Generated: {date.today().isoformat()}",
        "",
        "| Phase | Candidate | Status | Duration | Log |",
        "|---|---|---:|---:|---|",
    ]
    for result in results:
        status = "PASS" if result.returncode == 0 else f"FAIL:{result.returncode}"
        log = result.report.as_posix() if result.report else ""
        lines.append(f"| {result.phase} | `{result.candidate}` | {status} | {result.duration_s:.1f}s | `{log}` |")
    lines.extend(["", "## Recommended Defaults", ""])
    recommendations = recommended_defaults(results)
    if recommendations:
        for phase, candidate in recommendations.items():
            lines.append(f"- {phase}: `{candidate}`")
    else:
        lines.append("None. No passing benchmark results.")
    return "\n".join(lines) + "\n"


def recommended_defaults(results: list[BenchResult]) -> dict[str, str]:
    winners: dict[str, str] = {}
    for phase in sorted({result.phase for result in results}):
        passing = [result for result in results if result.phase == phase and result.returncode == 0]
        if passing:
            winners[phase] = sorted(passing, key=lambda result: result.duration_s)[0].candidate
    return winners


def update_defaults(results: list[BenchResult]) -> None:
    current = load_defaults()
    phases = dict(current.get("phases") or {})
    for phase, candidate in recommended_defaults(results).items():
        if phase == "phase1":
            phases["phase1"] = candidate
        elif phase == "phase2":
            phases["phase2"] = candidate
            phases["claim_judge"] = candidate
        elif phase == "query":
            phases["query"] = candidate
            phases["analysis_judge"] = candidate
    updated = {
        "updated": date.today().isoformat(),
        "default_candidate": phases.get("phase2") or current.get("default_candidate", "local-4090"),
        "phases": phases,
        "notes": ["Updated from tools/wiki_model_benchmark.py."],
    }
    DEFAULTS_PATH.write_text(json.dumps(updated, indent=2) + "\n")
    print(f"wrote {DEFAULTS_PATH}")


def load_defaults() -> dict[str, object]:
    if not DEFAULTS_PATH.exists():
        return {"default_candidate": "local-4090", "phases": {}}
    try:
        parsed = json.loads(DEFAULTS_PATH.read_text())
    except json.JSONDecodeError:
        return {"default_candidate": "local-4090", "phases": {}}
    return parsed if isinstance(parsed, dict) else {"default_candidate": "local-4090", "phases": {}}


def safe(value: str) -> str:
    return "".join(char if char.isalnum() or char in "._-" else "_" for char in value)


if __name__ == "__main__":
    sys.exit(main())
