#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Any

from wiki_common import content_tokens, iter_content_pages, one_line, parse_frontmatter, section
from wiki_check_synthesis import clean_evidence_excerpt, normalize_for_search, parse_locator, strip_markdown
from wiki_evidence_validator import (
    validate_evidence_location,
    is_evidence_too_short,
    should_fail_on_deterministic_flag,
)


VERDICTS = {"supported", "too_broad", "not_supported", "unclear"}
PAGE_VERDICTS = {"useful", "too_broad", "duplicate_or_overlap", "unclear"}
WEAK_CLAIM_WORDS = {"important", "crucial",
                    "fundamental", "essential", "success"}

# Flag types for the warning taxonomy
FLAG_TYPES = {
    "grounding_fail",      # evidence not found, locator invalid, quote mismatch
    "link_fail",           # broken link, page not found
    "schema_fail",         # missing frontmatter, malformed table, missing required section
    "coverage_warning",    # incomplete claim, missing context
    "structure_warning",   # optional section missing, unusual heading order
    "style_info",          # weak words, vague phrasing
    "unclassified_warning",  # unknown patterns
}

# Severity levels
SEVERITY_ERROR = "error"      # Blocks ingestion
SEVERITY_WARNING = "warning"  # Logged for review
SEVERITY_INFO = "info"        # Diagnostic only


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
    """A flag from deterministic validation.

    Fields:
        row: Row number in evidence table (0 for page-level issues)
        type: Flag type (grounding_fail, link_fail, schema_fail, etc.)
        severity: error | warning | info
        source: Origin of the flag (deterministic_validator, llm_judge, etc.)
        message: Human-readable description
    """
    row: int
    type: str
    severity: str
    source: str
    message: str

    def blocks_ingestion(self) -> bool:
        """Only error severity blocks. No message-text special cases."""
        return self.severity == SEVERITY_ERROR


def classify_flag(message: str) -> tuple[str, str]:
    """Classify a flag message into (type, severity).

    Returns (flag_type, severity) tuple.
    Defaults to unclassified_warning for unknown patterns.
    """
    message_lower = message.lower()

    # schema_fail (error) - includes missing required sections
    if any(term in message_lower for term in [
        "malformed",
        "render failure",
        "json error",
        "missing frontmatter",
        "missing required",
        "required section",
        "claim without evidence",
        "no evidence rows",
        "not parseable",
    ]):
        return ("schema_fail", SEVERITY_ERROR)

    # grounding_fail (error)
    if any(term in message_lower for term in [
        "evidence not found",
        "evidence not in source",
        "locator invalid",
        "quote mismatch",
        "not in source",
        "locator out of range",
        "outside normalized source",
        "outside source",
        "source_not_found",
        "fabricated",
        "contradicted",
    ]):
        return ("grounding_fail", SEVERITY_ERROR)

    # link_fail (error)
    if any(term in message_lower for term in [
        "broken link",
        "page not found",
        "invalid path",
        "link target missing",
    ]):
        return ("link_fail", SEVERITY_ERROR)

    # coverage_warning (warning)
    if any(term in message_lower for term in [
        "incomplete",
        "missing context",
        "partial coverage",
        "too short",
        "short (prose)",
        "claim is short",
    ]):
        return ("coverage_warning", SEVERITY_WARNING)

    # structure_warning (warning) - only optional structural issues
    if any(term in message_lower for term in [
        "optional section",
        "section order",
        "extra heading",
        "repeats evidence",
    ]):
        return ("structure_warning", SEVERITY_WARNING)

    # style_info (info)
    if any(term in message_lower for term in [
        "weak word",
        "weak generic",
        "vague",
        "promotional",
        "essential",
        "crucial",
        "important",
        "style",
    ]):
        return ("style_info", SEVERITY_INFO)

    # Default: unknown patterns are warnings, not structure issues
    return ("unclassified_warning", SEVERITY_WARNING)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Judge whether synthesized page claims follow from cited evidence.")
    parser.add_argument("page", help="wiki synthesized page to judge")
    parser.add_argument("--normalized-source", required=True,
                        help="normalized source markdown file")
    parser.add_argument(
        "--backend", help="model backend: codex, bedrock, openai, anthropic (default: WIKI_MODEL_BACKEND env or codex)")
    parser.add_argument(
        "--candidate", help="(codex backend only) profile, e.g. local-4090 or local-4090:model")
    parser.add_argument("--codex-bin", default="codex",
                        help="(deprecated, use --backend codex)")
    parser.add_argument("--timeout", type=int, default=600)
    parser.add_argument("--context-lines", type=int, default=2)
    parser.add_argument("--output", default="wiki/_claim-judge-report.md")
    parser.add_argument("--fail-on-issues", action="store_true")
    parser.add_argument("--soft-pass", action="store_true",
                        help="treat too_broad as warning, only fail on not_supported/unclear")
    parser.add_argument("--deterministic-only", action="store_true")
    parser.add_argument("--batch", action="store_true",
                        help="judge all claims in one model call instead of one call per row")
    args = parser.parse_args()

    page = Path(args.page)
    normalized_source = Path(args.normalized_source)
    if not page.exists():
        print(f"FAIL: missing page {page}", file=sys.stderr)
        return 2
    if not normalized_source.exists():
        print(
            f"FAIL: missing normalized source {normalized_source}", file=sys.stderr)
        return 2

    source_lines = normalized_source.read_text(errors="ignore").splitlines()
    rows = evidence_rows(page, source_lines, context_lines=args.context_lines)
    flags = deterministic_flags(rows, source_lines)
    siblings = sibling_pages(page)
    judge_result: dict[str, Any] | None = None
    judge_error = ""

    if not args.deterministic_only:
        # Determine backend
        backend_name = args.backend or os.environ.get(
            "WIKI_MODEL_BACKEND", "codex")

        # For codex backend, require --candidate for backward compatibility
        if backend_name == "codex" and not args.candidate:
            print(
                "FAIL: pass --candidate for codex backend, or use --backend <other>", file=sys.stderr)
            return 2

        if args.batch:
            prompt = render_prompt(page, rows, siblings)
            raw, returncode = run_judge_model(
                backend_name=backend_name,
                prompt=prompt,
                timeout=args.timeout,
                codex_bin=args.codex_bin,
                candidate=args.candidate,
            )
            if returncode != 0:
                judge_error = f"judge exited with status {returncode}"
                judge_result = {"raw_output": raw}
            else:
                try:
                    judge_result = parse_json_result(raw)
                except ValueError as error:
                    judge_error = str(error)
                    judge_result = {"raw_output": raw}
        else:
            judge_result, judge_error = run_row_judges_with_backend(
                backend_name=backend_name,
                page=page,
                rows=rows,
                timeout=args.timeout,
                codex_bin=args.codex_bin,
                candidate=args.candidate,
            )

    report = render_report(page, normalized_source, rows,
                           flags, siblings, judge_result, judge_error)
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(report)
    print(f"wrote {output}")

    if args.fail_on_issues and has_issues(flags, judge_result, judge_error, soft_pass=args.soft_pass):
        return 1
    return 0


def evidence_rows(page: Path, source_lines: list[str], *, context_lines: int) -> list[EvidenceRow]:
    fm = parse_frontmatter(page)
    page_type = fm.data.get("type")
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
                context=context_for_locator(
                    source_lines, locator, context_lines=context_lines),
            )
        )
    if page_type == "reference":
        rows.extend(reference_data_rows(fm.body, source_lines,
                    context_lines=context_lines, start_row=len(rows) + 1))
    return rows


def reference_data_rows(
    body: str,
    source_lines: list[str],
    *,
    context_lines: int,
    start_row: int,
) -> list[EvidenceRow]:
    reference_data = section(body, "## Reference data")
    table = table_rows(reference_data)
    if len(table) < 2:
        return []
    header_index: int | None = None
    for index, cells in enumerate(table):
        if not is_separator_row(cells):
            header_index = index
            break
    if header_index is None:
        return []
    header = [strip_markdown(cell).strip() for cell in table[header_index]]
    normalized_header = [cell.lower() for cell in header]
    if "evidence" not in normalized_header or "locator" not in normalized_header:
        return []
    evidence_index = normalized_header.index("evidence")
    locator_index = normalized_header.index("locator")

    rows: list[EvidenceRow] = []
    row_number = start_row
    for cells in table[header_index + 1:]:
        if is_separator_row(cells) or len(cells) != len(header):
            continue
        evidence = clean_evidence_excerpt(cells[evidence_index])
        locator = strip_markdown(cells[locator_index]).strip()
        claim_parts: list[str] = []
        for index, cell in enumerate(cells):
            header_name = normalized_header[index]
            if index in {evidence_index, locator_index} or header_name == "source":
                continue
            value = strip_markdown(cell).strip()
            if value:
                claim_parts.append(value)
        if not claim_parts:
            continue
        rows.append(
            EvidenceRow(
                row=row_number,
                claim="; ".join(claim_parts),
                evidence=evidence,
                locator=locator,
                source="Reference data",
                context=context_for_locator(
                    source_lines, locator, context_lines=context_lines),
            )
        )
        row_number += 1
    return rows


def deterministic_flags(rows: list[EvidenceRow], source_lines: list[str]) -> list[DeterministicFlag]:
    """Run deterministic checks on evidence rows.

    Uses shared validator to ensure consistency with wiki_check_synthesis.py.
    Distinguishes hard failures (fabricated evidence) from soft issues (locator precision).
    Uses the v3 flag taxonomy with type, severity, and source fields.
    """
    flags: list[DeterministicFlag] = []
    source_name = "deterministic_validator"

    for row in rows:
        parsed = parse_locator(row.locator)
        if parsed is None:
            flag_type, severity = classify_flag("locator is not parseable")
            flags.append(DeterministicFlag(
                row=row.row,
                type=flag_type,
                severity=severity,
                source=source_name,
                message="locator is not parseable",
            ))
            continue
        start, end = parsed

        # Use shared evidence validator for consistent behavior
        validation_result = validate_evidence_location(
            row.evidence, start, end, source_lines, window_size=2
        )

        if validation_result.is_hard_failure:
            # Hard failures (evidence fabricated, locator invalid)
            flag_type, severity = classify_flag(validation_result.reason)
            flags.append(DeterministicFlag(
                row=row.row,
                type=flag_type,
                severity=severity,
                source=source_name,
                message=validation_result.reason,
            ))
        elif validation_result.severity == "warn":
            # Soft issues (locator precision) - warn, don't fail
            reason = validation_result.reason
            if validation_result.suggested_locator:
                reason += f" (suggested: {validation_result.suggested_locator})"
            flag_type, severity = classify_flag(reason)
            flags.append(DeterministicFlag(
                row=row.row,
                type=flag_type,
                severity=severity,
                source=source_name,
                message=reason,
            ))
        # pass = no flag

        # Check evidence too short (allows code snippets)
        if is_evidence_too_short(row.evidence):
            flag_type, severity = classify_flag("evidence is short (prose)")
            flags.append(DeterministicFlag(
                row=row.row,
                type=flag_type,
                severity=severity,
                source=source_name,
                message="evidence is short (prose)",
            ))

        if len(re.findall(r"[A-Za-z0-9']+", row.claim)) < 5:
            flag_type, severity = classify_flag("claim is short")
            flags.append(DeterministicFlag(
                row=row.row,
                type=flag_type,
                severity=severity,
                source=source_name,
                message="claim is short",
            ))
        if normalize_for_search(row.claim) == normalize_for_search(row.evidence):
            flag_type, severity = classify_flag(
                "claim repeats evidence exactly")
            flags.append(DeterministicFlag(
                row=row.row,
                type=flag_type,
                severity=severity,
                source=source_name,
                message="claim repeats evidence exactly",
            ))
        weak_words = sorted(WEAK_CLAIM_WORDS & set(content_tokens(row.claim)))
        if weak_words:
            # Weak words are style guidance, not hard failures
            # The LLM-Wiki reference requires useful summaries, not word policing
            message = "claim uses weak generic words: " + ", ".join(weak_words)
            flag_type, severity = classify_flag(message)
            flags.append(DeterministicFlag(
                row=row.row,
                type=flag_type,
                severity=severity,
                source=source_name,
                message=message,
            ))
        # NOTE: Lexical unsupported-term check removed.
        # Synthesis naturally uses different vocabulary than evidence.
        # Semantic entailment should be checked by the LLM judge, not lexical overlap.
    if not rows:
        flag_type, severity = classify_flag("no evidence rows found")
        flags.append(DeterministicFlag(
            row=0,
            type=flag_type,
            severity=severity,
            source=source_name,
            message="no evidence rows found",
        ))
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

The page exists in the caller's repository. You are not expected to access the filesystem.
All content needed for judgment is included below. Do not return missing-file or inaccessible-file issues.

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
- supported: the claim's MEANING follows from the evidence, even if worded differently or via logical inference.
- too_broad: the claim makes factual assertions NOT entailed by the evidence even via inference.
- not_supported: the evidence contradicts the claim or is completely unrelated.
- unclear: the relationship cannot be judged from the provided context.
- Claims SHOULD use different vocabulary from the evidence. That is good synthesis.
- Accept claims that follow from logical inference (e.g., if A is B and B is C, then A is C).
- Accept claims that paraphrase or summarize the evidence in different words.
- Only flag too_broad or not_supported for genuinely unsupported FACTUAL ASSERTIONS, not vocabulary differences.
- Do NOT suggest replacement claim text. Leave suggested_claim empty.

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
        raw, returncode = run_local_judge(
            codex_bin, candidate, prompt, timeout)
        raw_outputs.append(f"ROW {row.row}\n{raw}")
        if returncode != 0:
            errors.append(
                f"row {row.row}: local judge exited with status {returncode}")
            continue
        try:
            parsed = parse_row_json_result(raw, allow_text_recovery=False)
        except ValueError as error:
            retry_prompt = render_row_retry_prompt(row, raw, str(error))
            retry_raw, retry_returncode = run_local_judge(
                codex_bin, candidate, retry_prompt, timeout)
            raw_outputs.append(f"ROW {row.row} RETRY\n{retry_raw}")
            if retry_returncode == 0:
                try:
                    parsed = parse_row_json_result(
                        retry_raw, allow_text_recovery=False)
                except ValueError as retry_error:
                    recovered = row_verdict_from_text(
                        "\n".join([raw, retry_raw]))
                    if recovered is None:
                        errors.append(f"row {row.row}: {retry_error}")
                        continue
                    parsed = recovered
                else:
                    parsed.setdefault("issue", "judge needed JSON-only retry")
            else:
                recovered = row_verdict_from_text(raw)
                if recovered is None:
                    errors.append(
                        f"row {row.row}: retry exited with status {retry_returncode} after {error}")
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
Decide whether the claim's MEANING follows from the evidence and source context below.

Important constraints:
- The evidence is an exact quote from the source.
- The locator points to the source line range for that quote.
- Judge whether the claim's factual assertions are entailed by the evidence.
- Claims SHOULD use different vocabulary than evidence. That is good synthesis.
- Only flag too_broad for genuinely unsupported FACTUAL ASSERTIONS, not word choices.
- Accept claims that follow from logical inference (e.g., if A is B and B is C, then A is C).
- Accept claims that paraphrase or summarize the evidence in different words.
- Do NOT suggest replacement claim text. Leave suggested_claim empty.
- Do not return missing-file or inaccessible-file issues; all needed content is shown below.

Page path: {page.as_posix()}
Row: {row.row}
Claim: {row.claim}
Evidence quote: {row.evidence}
Locator: {row.locator}

Source context:
{row.context}

Use exactly these verdicts:
- supported: claim meaning follows from evidence, even if words differ or via inference
- too_broad: claim makes factual assertions NOT entailed by evidence even via inference
- not_supported: evidence contradicts the claim or is completely unrelated
- unclear: cannot judge from provided context

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


def run_judge_model(
    *,
    backend_name: str,
    prompt: str,
    timeout: int,
    codex_bin: str = "codex",
    candidate: str | None = None,
) -> tuple[str, int]:
    """Run judge using the specified backend.

    For codex backend, uses run_local_judge for backward compatibility.
    For other backends, uses the model backend abstraction.

    Returns:
        Tuple of (output_text, returncode). returncode 0 means success.
    """
    if backend_name == "codex":
        if not candidate:
            return "ERROR: codex backend requires --candidate", 1
        return run_local_judge(codex_bin, candidate, prompt, timeout)

    # Use model backend abstraction for non-codex backends
    try:
        from wiki_model_backend import get_backend, ModelConfig
    except ImportError as e:
        return f"ERROR: failed to import model backend: {e}", 1

    try:
        backend = get_backend(backend_name)
    except ValueError as e:
        return f"ERROR: {e}", 1

    # Create a temporary directory for the model config
    with tempfile.TemporaryDirectory(prefix="llm-wiki-judge.") as tmp:
        tmp_path = Path(tmp)

        config = ModelConfig(
            worktree=tmp_path,
            prefix="judge",
            timeout=timeout,
            save_debug_files=True,
            system_prompt_style="judge",
        )

        response = backend.run(prompt, config)

        if not response.success:
            error_msg = response.error or "unknown error"
            return f"ERROR: {error_msg}", 1

        return response.output, 0


def run_row_judges_with_backend(
    *,
    backend_name: str,
    page: Path,
    rows: list[EvidenceRow],
    timeout: int,
    codex_bin: str = "codex",
    candidate: str | None = None,
) -> tuple[dict[str, Any], str]:
    """Run per-row judges using the specified backend."""
    results: list[dict[str, Any]] = []
    raw_outputs: list[str] = []
    errors: list[str] = []

    for row in rows:
        prompt = render_row_prompt(page, row)
        raw, returncode = run_judge_model(
            backend_name=backend_name,
            prompt=prompt,
            timeout=timeout,
            codex_bin=codex_bin,
            candidate=candidate,
        )
        raw_outputs.append(f"ROW {row.row}\n{raw}")

        if returncode != 0:
            errors.append(
                f"row {row.row}: judge exited with status {returncode}")
            continue

        try:
            parsed = parse_row_json_result(raw, allow_text_recovery=False)
        except ValueError as error:
            # Try recovery from text
            recovered = row_verdict_from_text(raw)
            if recovered is None:
                errors.append(f"row {row.row}: {error}")
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


def parse_candidate(raw: str) -> tuple[str, str | None]:
    if ":" not in raw:
        return raw, None
    profile, model = raw.split(":", 1)
    if not profile or not model:
        raise SystemExit(
            f"invalid candidate {raw!r}; use PROFILE or PROFILE:MODEL")
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
        raise ValueError(
            f"local judge returned invalid page_verdict {page_verdict!r}")
    claim_results = parsed.get("claim_results")
    if not isinstance(claim_results, list):
        raise ValueError("local judge JSON missing claim_results list")
    for item in claim_results:
        if not isinstance(item, dict):
            raise ValueError("claim_results item is not an object")
        verdict = item.get("verdict")
        if verdict not in VERDICTS:
            raise ValueError(
                f"local judge returned invalid claim verdict {verdict!r}")
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
                return text[start: index + 1]
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

    # Group flags by severity for better reporting
    error_flags = [f for f in flags if f.severity == SEVERITY_ERROR]
    warning_flags = [f for f in flags if f.severity == SEVERITY_WARNING]
    info_flags = [f for f in flags if f.severity == SEVERITY_INFO]

    lines.extend(["", "## Deterministic Flags", ""])

    if error_flags:
        lines.append("### Errors (blocking)")
        lines.append("")
        lines.append("| Type | Source | Row | Message |")
        lines.append("|---|---|---|---|")
        for flag in error_flags:
            row = "page" if flag.row == 0 else str(flag.row)
            lines.append(
                f"| {flag.type} | {flag.source} | {row} | {flag.message} |")
        lines.append("")

    if warning_flags:
        lines.append("### Warnings (review)")
        lines.append("")
        lines.append("| Type | Source | Row | Message |")
        lines.append("|---|---|---|---|")
        for flag in warning_flags:
            row = "page" if flag.row == 0 else str(flag.row)
            lines.append(
                f"| {flag.type} | {flag.source} | {row} | {flag.message} |")
        lines.append("")

    if info_flags:
        lines.append("### Info (diagnostic)")
        lines.append("")
        lines.append("| Type | Source | Row | Message |")
        lines.append("|---|---|---|---|")
        for flag in info_flags:
            row = "page" if flag.row == 0 else str(flag.row)
            lines.append(
                f"| {flag.type} | {flag.source} | {row} | {flag.message} |")
        lines.append("")

    if not flags:
        lines.append("None.")

    lines.append("")
    lines.append(
        f"Summary: {len(error_flags)} errors, {len(warning_flags)} warnings, {len(info_flags)} info")

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
        lines.extend(["", "## Raw Judge Output", "", "```text",
                     str(judge_result["raw_output"]).strip(), "```"])

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


def has_issues(
    flags: list[DeterministicFlag],
    judge_result: dict[str, Any] | None,
    judge_error: str,
    *,
    soft_pass: bool = False,
) -> bool:
    """Check if judge report has issues that should fail the build.

    Uses the v3 warning taxonomy:
    - Only error severity blocks ingestion
    - style_info and coverage_warning do not block
    - grounding_fail, link_fail, schema_fail block

    In soft_pass mode (aligned with REFERENCE_llm-wiki-pattern):
    - too_broad = stylistic choice, human can accept or refine
    - not_supported/unclear = substantive error, must fix

    The pattern says the human curates and guides; minor embellishments
    are synthesis choices, not contradictions.
    """
    if judge_error:
        return True

    # Use the new blocks_ingestion() method from v3 taxonomy
    # Only error severity blocks ingestion
    for flag in flags:
        if flag.blocks_ingestion():
            return True

    if not judge_result:
        return False
    if judge_result.get("page_verdict") not in ("useful", None):
        # In soft_pass, accept "too_broad" page verdict
        if soft_pass and judge_result.get("page_verdict") == "too_broad":
            pass
        else:
            return True
    for item in judge_result.get("claim_results") or []:
        if not isinstance(item, dict):
            continue
        verdict = item.get("verdict")
        if verdict == "supported":
            continue
        if soft_pass and verdict == "too_broad":
            # Stylistic choice - human can accept or refine
            continue
        # not_supported, unclear, or other = substantive issue
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


def table_rows(markdown: str) -> list[list[str]]:
    rows: list[list[str]] = []
    for line in markdown.splitlines():
        row = split_table_row(line)
        if row is not None:
            rows.append(row)
    return rows


def is_separator_row(cells: list[str]) -> bool:
    return all(cell and set(cell) <= {"-", ":", " "} for cell in cells)


def escape_cell(text: str) -> str:
    return text.replace("|", "/").replace("\n", " ").strip()


if __name__ == "__main__":
    sys.exit(main())
