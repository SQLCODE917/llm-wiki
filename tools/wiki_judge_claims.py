#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Any

from wiki_common import iter_content_pages, one_line, parse_frontmatter, section
from wiki_check_synthesis import clean_evidence_excerpt, normalize_for_search, parse_locator, strip_markdown


VERDICTS = {"supported", "too_broad", "not_supported", "unclear"}
PAGE_VERDICTS = {"useful", "too_broad", "duplicate_or_overlap", "unclear"}


@dataclass(frozen=True)
class EvidenceRow:
    row: int
    claim: str
    evidence: str
    locator: str
    source: str
    context: str


@dataclass(frozen=True)
class DeterministicFlag:
    row: int
    severity: str
    message: str


def main() -> int:
    parser = argparse.ArgumentParser(description="Judge whether synthesized page claims follow from cited evidence.")
    parser.add_argument("page", help="wiki synthesized page to judge")
    parser.add_argument("--normalized-source", required=True, help="normalized source markdown file")
    parser.add_argument("--candidate", help="local Codex candidate, e.g. local-4090 or local-4090:model")
    parser.add_argument("--codex-bin", default="codex")
    parser.add_argument("--timeout", type=int, default=600)
    parser.add_argument("--context-lines", type=int, default=2)
    parser.add_argument("--output", default="wiki/_claim-judge-report.md")
    parser.add_argument("--fail-on-issues", action="store_true")
    parser.add_argument("--deterministic-only", action="store_true")
    parser.add_argument("--batch", action="store_true", help="judge all claims in one model call instead of one call per row")
    args = parser.parse_args()

    page = Path(args.page)
    normalized_source = Path(args.normalized_source)
    if not page.exists():
        print(f"FAIL: missing page {page}", file=sys.stderr)
        return 2
    if not normalized_source.exists():
        print(f"FAIL: missing normalized source {normalized_source}", file=sys.stderr)
        return 2

    source_lines = normalized_source.read_text(errors="ignore").splitlines()
    rows = evidence_rows(page, source_lines, context_lines=args.context_lines)
    flags = deterministic_flags(rows, source_lines)
    siblings = sibling_pages(page)
    judge_result: dict[str, Any] | None = None
    judge_error = ""

    if not args.deterministic_only:
        if not args.candidate:
            print("FAIL: pass --candidate or use --deterministic-only", file=sys.stderr)
            return 2
        if args.batch:
            prompt = render_prompt(page, rows, siblings)
            raw, returncode = run_local_judge(args.codex_bin, args.candidate, prompt, args.timeout)
            if returncode != 0:
                judge_error = f"local judge exited with status {returncode}"
                judge_result = {"raw_output": raw}
            else:
                try:
                    judge_result = parse_json_result(raw)
                except ValueError as error:
                    judge_error = str(error)
                    judge_result = {"raw_output": raw}
        else:
            judge_result, judge_error = run_row_judges(args.codex_bin, args.candidate, page, rows, args.timeout)

    report = render_report(page, normalized_source, rows, flags, siblings, judge_result, judge_error)
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(report)
    print(f"wrote {output}")

    if args.fail_on_issues and has_issues(flags, judge_result, judge_error):
        return 1
    return 0


def evidence_rows(page: Path, source_lines: list[str], *, context_lines: int) -> list[EvidenceRow]:
    fm = parse_frontmatter(page)
    details = section(fm.body, "## Source-backed details")
    rows: list[EvidenceRow] = []
    header_seen = False
    row_number = 0
    for line in details.splitlines():
        cells = split_table_row(line)
        if cells is None:
            continue
        normalized = [cell.strip().lower() for cell in cells]
        if normalized == ["claim", "evidence", "locator", "source"]:
            header_seen = True
            continue
        if not header_seen or is_separator_row(cells):
            continue
        if len(cells) != 4:
            continue
        row_number += 1
        claim, evidence, locator, source = (cell.strip() for cell in cells)
        rows.append(
            EvidenceRow(
                row=row_number,
                claim=strip_markdown(claim),
                evidence=clean_evidence_excerpt(evidence),
                locator=strip_markdown(locator).strip(),
                source=source,
                context=context_for_locator(source_lines, locator, context_lines=context_lines),
            )
        )
    return rows


def deterministic_flags(rows: list[EvidenceRow], source_lines: list[str]) -> list[DeterministicFlag]:
    flags: list[DeterministicFlag] = []
    for row in rows:
        parsed = parse_locator(row.locator)
        if parsed is None:
            flags.append(DeterministicFlag(row.row, "fail", "locator is not parseable"))
            continue
        start, end = parsed
        if start < 1 or end > len(source_lines) or end < start:
            flags.append(DeterministicFlag(row.row, "fail", "locator is outside normalized source"))
            continue
        located_text = "\n".join(source_lines[start - 1 : end])
        if normalize_for_search(row.evidence) not in normalize_for_search(located_text):
            flags.append(DeterministicFlag(row.row, "fail", "evidence is not found in locator range"))
        if len(re.findall(r"[A-Za-z0-9']+", row.claim)) < 5:
            flags.append(DeterministicFlag(row.row, "warn", "claim is short"))
        if normalize_for_search(row.claim) == normalize_for_search(row.evidence):
            flags.append(DeterministicFlag(row.row, "warn", "claim repeats evidence exactly"))
    if not rows:
        flags.append(DeterministicFlag(0, "fail", "no evidence rows found"))
    return flags


def context_for_locator(source_lines: list[str], locator: str, *, context_lines: int) -> str:
    parsed = parse_locator(strip_markdown(locator).strip())
    if parsed is None:
        return "locator not parseable"
    start, end = parsed
    start_index = max(0, start - 1 - context_lines)
    end_index = min(len(source_lines), end + context_lines)
    out: list[str] = []
    for line_number in range(start_index + 1, end_index + 1):
        out.append(f"L{line_number}: {source_lines[line_number - 1]}")
    return "\n".join(out)


def sibling_pages(page: Path) -> list[str]:
    fm = parse_frontmatter(page)
    sources = fm.data.get("sources")
    if not isinstance(sources, list):
        return []
    resolved_sources = {
        (page.parent / source).resolve()
        for source in sources
        if isinstance(source, str)
    }
    siblings: list[str] = []
    for candidate in iter_content_pages():
        if candidate == page or candidate.parts[1] == "sources":
            continue
        candidate_fm = parse_frontmatter(candidate)
        candidate_sources = candidate_fm.data.get("sources")
        if not isinstance(candidate_sources, list):
            continue
        candidate_resolved_sources = {
            (candidate.parent / source).resolve()
            for source in candidate_sources
            if isinstance(source, str)
        }
        if not resolved_sources & candidate_resolved_sources:
            continue
        title = str(candidate_fm.data.get("title") or candidate.stem)
        summary = one_line(first_paragraph_after_h1(candidate_fm.body), 140)
        siblings.append(f"- {candidate.as_posix()} ({title}): {summary}")
    return siblings[:20]


def render_prompt(page: Path, rows: list[EvidenceRow], siblings: list[str]) -> str:
    fm = parse_frontmatter(page)
    title = str(fm.data.get("title") or page.stem)
    page_type = str(fm.data.get("type") or "unknown")
    summary = first_paragraph_after_h1(fm.body)
    row_blocks = []
    for row in rows:
        row_blocks.append(
            "\n".join(
                [
                    f"ROW {row.row}",
                    f"claim: {row.claim}",
                    f"evidence: {row.evidence}",
                    f"locator: {row.locator}",
                    "source_context:",
                    row.context,
                ]
            )
        )

    return f"""You are judging an LLM-Wiki synthesized page. Do not edit files. Return JSON only.

Page path: {page.as_posix()}
Page title: {title}
Page type: {page_type}
Page summary: {summary}

Sibling pages from the same source:
{chr(10).join(siblings) if siblings else "- none"}

Judge whether the page is useful and whether each claim is supported by its evidence and source context.

Use exactly these page verdicts: useful, too_broad, duplicate_or_overlap, unclear.
Use exactly these claim verdicts: supported, too_broad, not_supported, unclear.

Rules:
- supported: the claim follows directly from the evidence and context.
- too_broad: the evidence supports a narrower claim, but not the claim as written.
- not_supported: the evidence does not support the claim.
- unclear: the relationship cannot be judged from the provided context.
- Prefer a narrow suggested_claim when the claim is too broad.
- Do not reward generic wording if a more exact claim is available.

Claims:

{chr(10).join(row_blocks)}

Return this JSON object and nothing else:
{{
  "page_verdict": "useful",
  "page_issue": "",
  "claim_results": [
    {{
      "row": 1,
      "verdict": "supported",
      "issue": "",
      "suggested_claim": ""
    }}
  ]
}}
"""


def run_row_judges(
    codex_bin: str,
    candidate: str,
    page: Path,
    rows: list[EvidenceRow],
    timeout: int,
) -> tuple[dict[str, Any], str]:
    results: list[dict[str, Any]] = []
    raw_outputs: list[str] = []
    errors: list[str] = []
    for row in rows:
        prompt = render_row_prompt(page, row)
        raw, returncode = run_local_judge(codex_bin, candidate, prompt, timeout)
        raw_outputs.append(f"ROW {row.row}\n{raw}")
        if returncode != 0:
            errors.append(f"row {row.row}: local judge exited with status {returncode}")
            continue
        try:
            parsed = parse_row_json_result(raw, allow_text_recovery=False)
        except ValueError as error:
            retry_prompt = render_row_retry_prompt(row, raw, str(error))
            retry_raw, retry_returncode = run_local_judge(codex_bin, candidate, retry_prompt, timeout)
            raw_outputs.append(f"ROW {row.row} RETRY\n{retry_raw}")
            if retry_returncode == 0:
                try:
                    parsed = parse_row_json_result(retry_raw, allow_text_recovery=False)
                except ValueError as retry_error:
                    recovered = row_verdict_from_text("\n".join([raw, retry_raw]))
                    if recovered is None:
                        errors.append(f"row {row.row}: {retry_error}")
                        continue
                    parsed = recovered
                else:
                    parsed.setdefault("issue", "judge needed JSON-only retry")
            else:
                recovered = row_verdict_from_text(raw)
                if recovered is None:
                    errors.append(f"row {row.row}: retry exited with status {retry_returncode} after {error}")
                    continue
                parsed = recovered
        parsed["row"] = row.row
        results.append(parsed)
    page_verdict = "useful"
    page_issue = ""
    if not results:
        page_verdict = "unclear"
        page_issue = "no claim judgments could be parsed"
    elif errors:
        page_verdict = "unclear"
        page_issue = "one or more claim judgments could not be parsed"
    elif any(result.get("verdict") in {"not_supported", "unclear"} for result in results):
        page_verdict = "unclear"
        page_issue = "one or more claim judgments require repair or curator review"
    return {
        "page_verdict": page_verdict,
        "page_issue": page_issue,
        "claim_results": results,
        "raw_output": "\n\n".join(raw_outputs),
    }, "; ".join(errors)


def render_row_prompt(page: Path, row: EvidenceRow) -> str:
    return f"""You are judging exactly one LLM-Wiki claim. Do not edit files. Return JSON only.

Task:
Decide whether the claim follows from the evidence and source context below.

Important constraints:
- The evidence is an exact quote from the source.
- The locator points to the source line range for that quote.
- Judge only whether the claim is supported by the provided evidence and context.
- Do not claim that the source lacks the evidence if the quote is shown below.
- If the claim is mostly right but too broad, use `too_broad` and provide a narrower suggested_claim.

Page path: {page.as_posix()}
Row: {row.row}
Claim: {row.claim}
Evidence quote: {row.evidence}
Locator: {row.locator}

Source context:
{row.context}

Use exactly these verdicts:
- supported
- too_broad
- not_supported
- unclear

Return this JSON object and nothing else:
{{
  "verdict": "supported",
  "issue": "",
  "suggested_claim": ""
}}
"""


def render_row_retry_prompt(row: EvidenceRow, previous_output: str, parse_error: str) -> str:
    return f"""Your previous answer could not be parsed as JSON.

Parse error:
{parse_error}

Previous answer:
{previous_output}

Return exactly one JSON object and no prose. Do not use Markdown fences.

Claim: {row.claim}
Evidence quote: {row.evidence}
Source context:
{row.context}

Allowed verdicts:
- supported
- too_broad
- not_supported
- unclear

JSON shape:
{{
  "verdict": "supported",
  "issue": "",
  "suggested_claim": ""
}}
"""


def run_local_judge(codex_bin: str, candidate: str, prompt: str, timeout: int) -> tuple[str, int]:
    profile, model = parse_candidate(candidate)
    with tempfile.TemporaryDirectory(prefix="llm-wiki-judge.") as tmp:
        tmp_path = Path(tmp)
        last_message = tmp_path / "last-message.md"
        command = [
            codex_bin,
            "exec",
            "--profile",
            profile,
            "--cd",
            str(tmp_path),
            "--dangerously-bypass-approvals-and-sandbox",
            "--skip-git-repo-check",
            "--ephemeral",
            "--output-last-message",
            str(last_message),
        ]
        if model:
            command.extend(["--model", model])
        command.append("-")
        completed = subprocess.run(
            command,
            input=prompt,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            timeout=timeout,
            check=False,
        )
        output = last_message.read_text() if last_message.exists() else completed.stdout
        return output, completed.returncode


def parse_candidate(raw: str) -> tuple[str, str | None]:
    if ":" not in raw:
        return raw, None
    profile, model = raw.split(":", 1)
    if not profile or not model:
        raise SystemExit(f"invalid candidate {raw!r}; use PROFILE or PROFILE:MODEL")
    return profile, model


def parse_json_result(raw: str) -> dict[str, Any]:
    text = strip_code_fence(raw.strip())
    json_text = extract_json_object(text)
    if json_text is None:
        raise ValueError("local judge did not return a JSON object")
    parsed = json.loads(json_text)
    if not isinstance(parsed, dict):
        raise ValueError("local judge JSON was not an object")
    page_verdict = parsed.get("page_verdict")
    if page_verdict not in PAGE_VERDICTS:
        raise ValueError(f"local judge returned invalid page_verdict {page_verdict!r}")
    claim_results = parsed.get("claim_results")
    if not isinstance(claim_results, list):
        raise ValueError("local judge JSON missing claim_results list")
    for item in claim_results:
        if not isinstance(item, dict):
            raise ValueError("claim_results item is not an object")
        verdict = item.get("verdict")
        if verdict not in VERDICTS:
            raise ValueError(f"local judge returned invalid claim verdict {verdict!r}")
    return parsed


def row_verdict_from_text(text: str) -> dict[str, str] | None:
    lowered = text.lower()
    if "not supported" in lowered or "does not support" in lowered:
        verdict = "not_supported"
    elif "too broad" in lowered:
        verdict = "too_broad"
    elif "unclear" in lowered or "cannot be judged" in lowered:
        verdict = "unclear"
    elif "supported" in lowered or "supports the claim" in lowered or "directly supports" in lowered or "support" in lowered:
        verdict = "supported"
    else:
        return None
    return {
        "verdict": verdict,
        "issue": "verdict recovered from non-JSON local judge output",
        "suggested_claim": "",
    }


def parse_row_json_result(raw: str, *, allow_text_recovery: bool = True) -> dict[str, Any]:
    text = strip_code_fence(raw.strip())
    json_text = extract_json_object(text)
    if json_text is None:
        if allow_text_recovery:
            recovered = row_verdict_from_text(text)
            if recovered is not None:
                return recovered
        raise ValueError("local judge did not return a JSON object")
    parsed = json.loads(json_text)
    if not isinstance(parsed, dict):
        raise ValueError("local judge JSON was not an object")
    verdict = parsed.get("verdict")
    if verdict not in VERDICTS:
        raise ValueError(f"local judge returned invalid verdict {verdict!r}")
    return parsed


def strip_code_fence(text: str) -> str:
    if text.startswith("```"):
        text = re.sub(r"^```(?:json|text)?", "", text).strip()
        text = re.sub(r"```$", "", text).strip()
    return text


def extract_json_object(text: str) -> str | None:
    start = text.find("{")
    if start == -1:
        return None
    depth = 0
    in_string = False
    escaped = False
    for index in range(start, len(text)):
        char = text[index]
        if escaped:
            escaped = False
            continue
        if char == "\\":
            escaped = True
            continue
        if char == '"':
            in_string = not in_string
            continue
        if in_string:
            continue
        if char == "{":
            depth += 1
        elif char == "}":
            depth -= 1
            if depth == 0:
                return text[start : index + 1]
    return None


def render_report(
    page: Path,
    normalized_source: Path,
    rows: list[EvidenceRow],
    flags: list[DeterministicFlag],
    siblings: list[str],
    judge_result: dict[str, Any] | None,
    judge_error: str,
) -> str:
    lines: list[str] = [
        "# Claim Judge Report",
        "",
        f"Generated: {date.today().isoformat()}",
        f"Page: `{page.as_posix()}`",
        f"Normalized source: `{normalized_source.as_posix()}`",
        "",
        "## Summary",
        "",
        f"- Evidence rows: {len(rows)}",
        f"- Deterministic flags: {len(flags)}",
    ]
    if judge_error:
        lines.append(f"- Judge error: {judge_error}")
    if judge_result and "page_verdict" in judge_result:
        lines.append(f"- Page verdict: {judge_result.get('page_verdict')}")
        issue = str(judge_result.get("page_issue") or "")
        if issue:
            lines.append(f"- Page issue: {issue}")
    lines.extend(["", "## Deterministic Flags", ""])
    if flags:
        for flag in flags:
            row = "page" if flag.row == 0 else f"row {flag.row}"
            lines.append(f"- {flag.severity.upper()} {row}: {flag.message}")
    else:
        lines.append("None.")

    lines.extend(["", "## Sibling Pages", ""])
    lines.extend(siblings or ["None."])

    lines.extend(["", "## Claim Results", ""])
    lines.append("| Row | Verdict | Issue | Suggested claim |")
    lines.append("|---|---|---|---|")
    results_by_row = judge_results_by_row(judge_result)
    for row in rows:
        result = results_by_row.get(row.row, {})
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row.row),
                    escape_cell(str(result.get("verdict") or "not judged")),
                    escape_cell(str(result.get("issue") or "")),
                    escape_cell(str(result.get("suggested_claim") or "")),
                ]
            )
            + " |"
        )

    if judge_result and "raw_output" in judge_result:
        lines.extend(["", "## Raw Judge Output", "", "```text", str(judge_result["raw_output"]).strip(), "```"])

    return "\n".join(lines) + "\n"


def judge_results_by_row(judge_result: dict[str, Any] | None) -> dict[int, dict[str, Any]]:
    if not judge_result:
        return {}
    claim_results = judge_result.get("claim_results")
    if not isinstance(claim_results, list):
        return {}
    out: dict[int, dict[str, Any]] = {}
    for item in claim_results:
        if not isinstance(item, dict):
            continue
        row = item.get("row")
        if isinstance(row, int):
            out[row] = item
    return out


def has_issues(flags: list[DeterministicFlag], judge_result: dict[str, Any] | None, judge_error: str) -> bool:
    if judge_error:
        return True
    if any(flag.severity == "fail" for flag in flags):
        return True
    if not judge_result:
        return False
    if judge_result.get("page_verdict") != "useful":
        return True
    for item in judge_result.get("claim_results") or []:
        if isinstance(item, dict) and item.get("verdict") != "supported":
            return True
    return False


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


def escape_cell(text: str) -> str:
    return text.replace("|", "/").replace("\n", " ").strip()


if __name__ == "__main__":
    sys.exit(main())
