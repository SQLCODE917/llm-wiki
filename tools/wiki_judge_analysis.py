#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from datetime import date
from pathlib import Path
from typing import Any

from wiki_common import markdown_links, parse_frontmatter, section
from wiki_judge_claims import extract_json_object, run_local_judge, strip_code_fence


VERDICTS = {"supported", "too_broad", "not_supported", "unclear"}


def main() -> int:
    parser = argparse.ArgumentParser(description="Judge whether an analysis page is supported by its cited wiki pages.")
    parser.add_argument("page", help="wiki/analyses/*.md page")
    parser.add_argument("--candidate", help="local Codex candidate, e.g. local-4090")
    parser.add_argument("--codex-bin", default="codex")
    parser.add_argument("--timeout", type=int, default=600)
    parser.add_argument("--output", default="wiki/_analysis-judge-report.md")
    parser.add_argument("--deterministic-only", action="store_true")
    parser.add_argument("--fail-on-issues", action="store_true")
    args = parser.parse_args()

    page = Path(args.page)
    failures = deterministic_failures(page)
    judge_result: dict[str, Any] | None = None
    judge_error = ""
    if not args.deterministic_only and not failures:
        if not args.candidate:
            print("FAIL: pass --candidate or use --deterministic-only", file=sys.stderr)
            return 2
        prompt = render_prompt(page)
        raw, returncode = run_local_judge(args.codex_bin, args.candidate, prompt, args.timeout)
        if returncode != 0:
            judge_error = f"local analysis judge exited with status {returncode}"
            judge_result = {"raw_output": raw}
        else:
            try:
                judge_result = parse_result(raw)
            except ValueError as error:
                judge_error = str(error)
                judge_result = {"raw_output": raw}

    report = render_report(page, failures, judge_result, judge_error)
    output = Path(args.output)
    output.write_text(report)
    print(f"wrote {output}")
    if args.fail_on_issues and has_issues(failures, judge_result, judge_error):
        return 1
    return 0


def deterministic_failures(page: Path) -> list[str]:
    failures: list[str] = []
    if not page.exists():
        return [f"missing analysis page {page}"]
    fm = parse_frontmatter(page)
    if fm.data.get("type") != "analysis":
        failures.append("page type must be analysis")
    sources = fm.data.get("sources")
    if not isinstance(sources, list) or not sources:
        failures.append("analysis must have frontmatter sources")
        return failures
    for source in sources:
        if not isinstance(source, str):
            failures.append("source values must be strings")
            continue
        if not (page.parent / source).resolve().exists():
            failures.append(f"source does not exist: {source}")
    if not answer_body(page).strip():
        failures.append("analysis answer body is empty")
    return failures


def render_prompt(page: Path) -> str:
    source_blocks: list[str] = []
    for source_path in cited_wiki_pages(page):
        source_blocks.append(
            "\n".join(
                [
                    f"PAGE: {source_path.relative_to(Path.cwd()).as_posix()}",
                    "CONTENT:",
                    source_path.read_text(errors="ignore")[:9000],
                ]
            )
        )
    return f"""You are judging whether a filed LLM-Wiki analysis is supported by its cited wiki pages.
Do not edit files. Return JSON only.

Analysis page: {page.as_posix()}

Analysis answer:
{answer_body(page)}

Cited wiki pages:
{chr(10).join(source_blocks)}

Use exactly these verdicts:
- supported: the answer is supported by the cited wiki pages.
- too_broad: the cited pages support a narrower answer.
- not_supported: one or more important claims are not supported.
- unclear: support cannot be judged from the supplied pages.

Return this JSON object and nothing else:
{{
  "verdict": "supported",
  "issue": "",
  "unsupported_claims": []
}}
"""


def cited_wiki_pages(page: Path) -> list[Path]:
    fm = parse_frontmatter(page)
    paths: set[Path] = set()
    cwd = Path.cwd().resolve()
    for source in fm.data.get("sources") or []:
        if not isinstance(source, str):
            continue
        resolved = (page.parent / source).resolve()
        if resolved.exists():
            paths.add(resolved)
    for link in markdown_links(page):
        if not link.resolved or not link.resolved.exists() or link.resolved.suffix != ".md":
            continue
        try:
            rel = link.resolved.relative_to(cwd)
        except ValueError:
            continue
        if len(rel.parts) >= 3 and rel.parts[0] == "wiki":
            paths.add(link.resolved)
    return sorted(paths, key=lambda candidate: candidate.as_posix())


def answer_body(page: Path) -> str:
    fm = parse_frontmatter(page)
    body = fm.body
    source_pages = section(body, "## Source pages")
    if source_pages:
        body = body.split("## Source pages", 1)[0]
    lines = [line for line in body.splitlines() if not line.startswith("# ")]
    return "\n".join(lines).strip()


def parse_result(raw: str) -> dict[str, Any]:
    text = strip_code_fence(raw.strip())
    json_text = extract_json_object(text)
    if json_text is None:
        raise ValueError("local analysis judge did not return a JSON object")
    parsed = json.loads(json_text)
    if not isinstance(parsed, dict):
        raise ValueError("local analysis judge JSON was not an object")
    verdict = parsed.get("verdict")
    if verdict not in VERDICTS:
        raise ValueError(f"invalid verdict {verdict!r}")
    claims = parsed.get("unsupported_claims")
    if claims is not None and not isinstance(claims, list):
        raise ValueError("unsupported_claims must be a list")
    return parsed


def render_report(page: Path, failures: list[str], judge_result: dict[str, Any] | None, judge_error: str) -> str:
    lines = [
        "# Analysis Judge Report",
        "",
        f"Generated: {date.today().isoformat()}",
        f"Page: `{page.as_posix()}`",
        "",
        "## Summary",
        "",
        f"- Deterministic failures: {len(failures)}",
    ]
    if judge_error:
        lines.append(f"- Judge error: {judge_error}")
    if judge_result and "verdict" in judge_result:
        lines.append(f"- Verdict: {judge_result.get('verdict')}")
        issue = str(judge_result.get("issue") or "")
        if issue:
            lines.append(f"- Issue: {issue}")
    lines.extend(["", "## Deterministic Failures", ""])
    lines.extend(f"- {failure}" for failure in failures) if failures else lines.append("None.")
    lines.extend(["", "## Unsupported Claims", ""])
    unsupported = judge_result.get("unsupported_claims") if judge_result else None
    if isinstance(unsupported, list) and unsupported:
        lines.extend(f"- {claim}" for claim in unsupported)
    else:
        lines.append("None.")
    if judge_result and "raw_output" in judge_result:
        lines.extend(["", "## Raw Judge Output", "", "```text", str(judge_result["raw_output"]).strip(), "```"])
    return "\n".join(lines) + "\n"


def has_issues(failures: list[str], judge_result: dict[str, Any] | None, judge_error: str) -> bool:
    if failures or judge_error:
        return True
    if not judge_result:
        return False
    return judge_result.get("verdict") != "supported"


if __name__ == "__main__":
    sys.exit(main())
