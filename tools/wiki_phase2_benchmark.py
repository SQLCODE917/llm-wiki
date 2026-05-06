#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
import tempfile
import time
from dataclasses import dataclass
from datetime import date
from pathlib import Path

from wiki_common import code_paths, parse_frontmatter, section
from wiki_evidence_bank import source_chunks, snippets_for_candidate
from wiki_evidence_ranges import (
    SourceRange,
    format_ranges,
    locator_within_ranges,
    normalize_locator,
    parse_locator_range,
    source_ranges_for_candidate,
)
from wiki_phase1_benchmark import (
    Candidate,
    copy_repo,
    find_normalized_source,
    git_changed_files,
    init_git,
    parse_candidate,
    run_codex,
)


PRIORITY_ORDER = {"must create": 0,
                  "should create": 1, "could create": 2, "defer": 3}


@dataclass
class Result:
    candidate: Candidate
    worktree: Path
    duration_s: float
    codex_returncodes: list[int | None]
    validation_returncode: int | None
    changed_files: list[str]
    log_paths: list[Path]


@dataclass(frozen=True)
class RelatedCandidate:
    path: str
    priority: str
    index: int
    group: str | None = None
    evidence_basis: str | None = None


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Benchmark local Codex candidates on one Phase 2 synthesis task."
    )
    parser.add_argument("slug", help="source slug, e.g. aoe2-basics")
    parser.add_argument(
        "--candidate",
        action="append",
        help=(
            "Candidate as PROFILE or PROFILE:MODEL. Repeat to compare models. "
            "Example: --candidate local-4090 --candidate local-4090:gpt-oss:20b"
        ),
    )
    parser.add_argument("--normalized-source",
                        help="explicit normalized markdown path")
    parser.add_argument("--prompt-template",
                        default="tools/prompts/phase2-synthesis.md")
    parser.add_argument("--codex-bin", default="codex")
    parser.add_argument("--timeout", type=int, default=900)
    parser.add_argument("--min-pages", type=int, default=5)
    parser.add_argument("--max-pages", type=int, default=8)
    parser.add_argument(
        "--repair-attempts",
        type=int,
        default=1,
        help="number of extra Codex repair prompts to run after failed validation",
    )
    parser.add_argument(
        "--report", help="write a Markdown benchmark report to this path")
    parser.add_argument("--keep", action="store_true",
                        help="keep temp worktrees after the run")
    args = parser.parse_args()

    repo_root = Path.cwd()
    normalized_source = Path(
        args.normalized_source) if args.normalized_source else find_normalized_source(args.slug)
    if not normalized_source.exists():
        print(
            f"FAIL: normalized source does not exist: {normalized_source}", file=sys.stderr)
        return 2

    prompt_template = Path(args.prompt_template)
    if not prompt_template.exists():
        print(
            f"FAIL: prompt template does not exist: {prompt_template}", file=sys.stderr)
        return 2

    candidates = [parse_candidate(raw)
                  for raw in (args.candidate or ["local-4090"])]
    results: list[Result] = []

    for candidate in candidates:
        result = run_candidate(
            repo_root=repo_root,
            slug=args.slug,
            normalized_source=normalized_source,
            prompt_template=prompt_template,
            candidate=candidate,
            codex_bin=args.codex_bin,
            timeout=args.timeout,
            min_pages=args.min_pages,
            max_pages=args.max_pages,
            repair_attempts=args.repair_attempts,
        )
        results.append(result)
        print_result(result)
        if not args.keep:
            shutil.rmtree(result.worktree, ignore_errors=True)

    if args.report:
        write_report(Path(args.report), args.slug, results)

    return 0 if all(result.validation_returncode == 0 for result in results) else 1


def run_candidate(
    *,
    repo_root: Path,
    slug: str,
    normalized_source: Path,
    prompt_template: Path,
    candidate: Candidate,
    codex_bin: str,
    timeout: int,
    min_pages: int,
    max_pages: int,
    repair_attempts: int,
) -> Result:
    worktree = Path(
        tempfile.mkdtemp(
            prefix=f"llm-wiki-phase2-{slug}-{candidate.safe_label}.", dir="/tmp")
    )
    copy_repo(repo_root, worktree)
    init_git(worktree)

    source_page = worktree / "wiki/sources" / f"{slug}.md"
    existing_paths = existing_created_paths(source_page)
    selected_candidates = selected_candidate_paths(source_page, max_pages)
    selected_paths = [candidate.path for candidate in selected_candidates]
    allowed_paths = sorted(set(existing_paths + selected_paths))
    expected_total_pages = len(allowed_paths)
    evidence_bank = build_evidence_bank(
        worktree, normalized_source, selected_candidates)
    prompt = render_prompt(
        template=(worktree / prompt_template).read_text(),
        slug=slug,
        normalized_source=normalized_source.as_posix(),
        min_pages=min_pages,
        max_pages=max_pages,
        existing_paths=existing_paths,
        selected_candidates=selected_candidates,
        expected_total_pages=expected_total_pages,
        evidence_bank=evidence_bank,
        range_page_args=range_page_args(selected_paths),
    )

    start = time.monotonic()
    codex_returncodes: list[int | None] = []
    log_paths: list[Path] = []

    returncode, paths = run_codex(
        worktree=worktree,
        candidate=candidate,
        codex_bin=codex_bin,
        prompt=prompt,
        timeout=timeout,
        prefix="codex-initial",
    )
    codex_returncodes.append(returncode)
    log_paths.extend(paths)
    validation_returncode = run_validation(
        worktree,
        slug,
        expected_total_pages,
        expected_total_pages,
        allowed_paths,
        normalized_source,
        range_paths=selected_paths,
    )

    for attempt in range(1, repair_attempts + 1):
        if validation_returncode == 0:
            break
        repair_prompt = render_repair_prompt(
            slug=slug,
            validation_output=(worktree / "phase2-validation.log").read_text(),
            min_pages=expected_total_pages,
            max_pages=expected_total_pages,
            selected_candidates=selected_candidates,
            existing_paths=existing_paths,
            normalized_source=normalized_source,
            evidence_bank=evidence_bank,
        )
        returncode, paths = run_codex(
            worktree=worktree,
            candidate=candidate,
            codex_bin=codex_bin,
            prompt=repair_prompt,
            timeout=timeout,
            prefix=f"codex-repair-{attempt}",
        )
        codex_returncodes.append(returncode)
        log_paths.extend(paths)
        validation_returncode = run_validation(
            worktree,
            slug,
            expected_total_pages,
            expected_total_pages,
            allowed_paths,
            normalized_source,
            range_paths=selected_paths,
        )

    duration_s = time.monotonic() - start
    changed_files = git_changed_files(worktree)

    return Result(
        candidate=candidate,
        worktree=worktree,
        duration_s=duration_s,
        codex_returncodes=codex_returncodes,
        validation_returncode=validation_returncode,
        changed_files=changed_files,
        log_paths=log_paths,
    )


def render_prompt(
    *,
    template: str,
    slug: str,
    normalized_source: str,
    min_pages: int,
    max_pages: int,
    existing_paths: list[str],
    selected_candidates: list[RelatedCandidate],
    expected_total_pages: int,
    evidence_bank: str,
    range_page_args: str = "",
) -> str:
    selected_paths = [candidate.path for candidate in selected_candidates]
    selected_text = render_selected_candidates(selected_candidates)
    replacements = {
        "{{current_date}}": date.today().isoformat(),
        "{{slug}}": slug,
        "{{normalized_source}}": normalized_source,
        "{{min_pages}}": str(min_pages),
        "{{max_pages}}": str(max_pages),
        "{{existing_pages}}": render_existing_pages(existing_paths),
        "{{selected_count}}": str(len(selected_paths)),
        "{{expected_total_pages}}": str(expected_total_pages),
        "{{selected_candidates}}": selected_text,
        "{{evidence_bank}}": evidence_bank,
        "{{allowed_page_args}}": allowed_page_args(sorted(set(existing_paths + selected_paths))),
        "{{range_page_args}}": range_page_args,
    }
    rendered = template
    for old, new in replacements.items():
        rendered = rendered.replace(old, new)
    return rendered


def run_validation(
    worktree: Path,
    slug: str,
    min_pages: int,
    max_pages: int,
    selected_paths: list[str],
    normalized_source: Path,
    *,
    range_paths: list[str] | None = None,
) -> int:
    synthesis_command = [
        "python3",
        "tools/wiki_check_synthesis.py",
        slug,
        "--min-pages",
        str(min_pages),
        "--max-pages",
        str(max_pages),
        "--normalized-source",
        normalized_source.as_posix(),
    ]
    for path in selected_paths:
        synthesis_command.extend(
            ["--allowed-page", source_relative_to_repo(path)])
    if selected_paths:
        synthesis_command.append("--require-allowed-pages")
    for path in range_paths or []:
        synthesis_command.extend(
            ["--range-page", source_relative_to_repo(path)])

    reference_repair_commands = [
        [
            "python3",
            "tools/wiki_repair_reference.py",
            source_relative_to_repo(path),
            "--normalized-source",
            normalized_source.as_posix(),
        ]
        for path in selected_paths
        if source_relative_to_repo(path).startswith("wiki/references/")
    ]

    commands = [
        ["python3", "tools/wiki_link_related.py", slug],
        ["python3", "tools/wiki_fix_broken_links.py", slug],
        ["python3", "tools/wiki_normalize_ascii.py", slug],
        ["python3", "tools/wiki_normalize_tables.py", slug],
        *reference_repair_commands,
        synthesis_command,
        ["pnpm", "wiki:grounding:check"],
    ]

    outputs: list[str] = []
    returncode = 0
    for command in commands:
        completed = subprocess.run(
            command,
            cwd=worktree,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
        )
        outputs.append("$ " + " ".join(command))
        outputs.append(completed.stdout)
        if completed.returncode != 0 and returncode == 0:
            returncode = completed.returncode

    scope_failures = changed_file_scope_failures(
        worktree, slug, selected_paths)
    cleanup_messages = cleanup_backup_artifacts(worktree, slug, selected_paths)
    if cleanup_messages:
        outputs.append("$ backup artifact cleanup")
        outputs.extend(cleanup_messages)
        scope_failures = changed_file_scope_failures(
            worktree, slug, selected_paths)
    if scope_failures:
        outputs.append("$ changed-file scope check")
        outputs.extend(f"FAIL: {failure}" for failure in scope_failures)
        if returncode == 0:
            returncode = 1

    (worktree / "phase2-validation.log").write_text("\n".join(outputs))
    return returncode


def changed_file_scope_failures(worktree: Path, slug: str, allowed_paths: list[str]) -> list[str]:
    allowed = {f"wiki/sources/{slug}.md"}
    allowed.update(source_relative_to_repo(path) for path in allowed_paths)
    failures: list[str] = []
    for changed in git_changed_files(worktree):
        path = changed_status_path(changed)
        if path and is_runner_artifact(path):
            continue
        if path and path not in allowed:
            failures.append(f"{path} changed outside Phase 2 allowed files")
    return failures


def cleanup_backup_artifacts(worktree: Path, slug: str, allowed_paths: list[str]) -> list[str]:
    allowed = {f"wiki/sources/{slug}.md"}
    allowed.update(source_relative_to_repo(path) for path in allowed_paths)
    suffixes = [".bak", ".orig", ".tmp", ".fixed", "~"]
    messages: list[str] = []
    for rel in sorted(allowed):
        base = worktree / rel
        for suffix in suffixes:
            artifact = Path(str(base) + suffix)
            if artifact.exists() and artifact.is_file():
                artifact.unlink()
                messages.append(
                    f"removed {artifact.relative_to(worktree).as_posix()}")
    for name in ("temp_file.md", "temp.md", "scratch.md"):
        artifact = worktree / name
        if artifact.exists() and artifact.is_file():
            artifact.unlink()
            messages.append(
                f"removed {artifact.relative_to(worktree).as_posix()}")
    return messages


def changed_status_path(line: str) -> str:
    value = line[3:].strip() if len(
        line) > 3 and line[2] == " " else line[2:].strip()
    if " -> " in value:
        value = value.split(" -> ", 1)[1].strip()
    return value


def is_runner_artifact(path: str) -> bool:
    name = Path(path).name
    if path == "wiki/_claim-judge-report.md":
        return True
    if name == "phase2-validation.log":
        return True
    if re.fullmatch(r"phase2-judge(?:-[A-Za-z0-9_.-]+)?\.(?:md|log)", name):
        return True
    # JSON output files from structured output mode
    if re.fullmatch(r"codex-(?:initial|repair-\d+|judge-repair-\d+)-output\.json", name):
        return True
    return False


def render_repair_prompt(
    *,
    slug: str,
    validation_output: str,
    min_pages: int,
    max_pages: int,
    selected_candidates: list[RelatedCandidate],
    existing_paths: list[str],
    normalized_source: Path,
    evidence_bank: str,
) -> str:
    selected_paths = [candidate.path for candidate in selected_candidates]
    allowed_paths = sorted(set(existing_paths + selected_paths))
    selected = render_selected_candidates(selected_candidates)
    existing = render_existing_pages(existing_paths)
    return f"""Read `AGENTS.md` fully before acting.

Repair only Phase 2 synthesis for `wiki/sources/{slug}.md`.

CRITICAL: Make minimal targeted edits only. DO NOT rewrite pages from scratch.
- If a page has the required sections (`## Source-backed details`, `## Source pages`), keep them.
- Fix only the specific FAIL items listed below.
- Preserve all existing structure and content that passes validation.

Allowed writes:
- `wiki/sources/{slug}.md`
- `wiki/concepts/**`
- `wiki/entities/**`
- `wiki/procedures/**`
- `wiki/references/**`

Forbidden writes:
- `raw/imported/**`
- `raw/normalized/**`
- `wiki/index.md`
- `wiki/log.md`
- `wiki/_graph.json`
- `wiki/_linter-report.md`
- `wiki/_claim-judge-report.md`
- `wiki/_grounding-report.md`
- `wiki/analyses/**`
- `packages/**`
- `tools/**`
- backup files such as `*.bak`, `*.orig`, `*.tmp`, or `*~`

Validation failed with this exact output:

```text
{validation_output.strip()}
```

Fix the failures mechanically:
- Existing synthesized pages for this source that should remain linked:
{existing}
- Create or update exactly these selected pages in this repair:
{selected}
- Evidence bank with exact normalized-source snippets:
{evidence_bank}
- After repair, `wiki/sources/{slug}.md` should link to exactly {min_pages} synthesized pages total: existing pages plus selected pages.
- If any other synthesized pages were created for this source, delete them and return their source-page `Related pages` rows to `not created yet`.
- Each synthesized page must have correct frontmatter, a body link to the source page, and a source page section.
- Each synthesized page must have exactly one `## Source-backed details` section and it must contain substantial source-backed content.
- Each synthesized page must include a `## Source-backed details` evidence table with header `| Claim | Evidence | Locator | Source |`.
- Each evidence cell must contain a short exact excerpt from the normalized source, not a paraphrase.
- Each locator cell must use `normalized:L12` or `normalized:L12-L14` from the evidence bank, and the evidence excerpt must appear inside that cited line range.
- Each selected page's evidence locators must stay inside the allowed source range shown in the evidence bank, unless the page declares a narrower/more exact `source_ranges` frontmatter value.
- Evidence table data rows must start with `|`, not `+`, `-`, or diff-marker text.
- Each claim cell must synthesize the evidence in the page's own words; do not copy the evidence sentence into the claim cell.
- SYNTHESIS means expressing the SAME MEANING as the evidence using DIFFERENT WORDS. Example:
  - Evidence: "Linear recursion is a basic building block of algorithms."
  - BAD claim (copies): "Linear recursion is a basic building block of algorithms."
  - BAD claim (adds facts): "Linear recursion is a pattern where functions repeatedly call themselves."
  - GOOD claim: "Linear recursion serves as a core component for constructing algorithms."
- CONSERVATIVE CLAIMS: Each claim must be fully entailed by the cited evidence. Do NOT add details, qualifications, or explanations not present in the evidence.
- Claim cells must not use weak generic words: important, crucial, fundamental, essential, success.
- Remove empty headings, duplicate headings, and empty `## Executable implementation` sections.
- Do not put YAML/frontmatter keys such as `tags:`, `sources:`, `status:`, or `last_updated:` in the Markdown body.
- Procedure pages must include `## Steps` with at least 3 concrete numbered or bulleted steps.
- Reference pages must include `## Reference data` with a Markdown lookup table containing at least 2 data rows.
- Reference data tables must include `Evidence` and `Locator` columns with exact normalized-source excerpts.
- Synthesized-page cross-links may point only to pages that already exist or pages created in this phase.
- Do not create extra pages to repair broken cross-links; remove the broken Markdown link or change it to plain text instead.
- Created pages and not-yet-created candidates must use this canonical `## Related pages` row shape:

```md
| Page title | [../concepts/example.md](../concepts/example.md) | Source-native group name | must create | concrete evidence basis | created |
| Page title | `../concepts/example.md` | Source-native group name | should create | concrete evidence basis | not created yet |
```

- Preserve any Group, Priority, and Evidence basis cells already present in `## Related pages`.
- Do not use placeholder text such as `Page title`; keep the real page titles in the first column.
- Use ASCII punctuation unless the source requires otherwise.
- Do not update index, graph, log, reports, raw files, code, or tools.
- Do not create backup files.
- Do not create scratch files such as `.fixed` files or `temp_file.md`.

After editing, run exactly:

```bash
python3 tools/wiki_link_related.py {slug}
python3 tools/wiki_fix_broken_links.py {slug}
python3 tools/wiki_normalize_ascii.py {slug}
python3 tools/wiki_normalize_tables.py {slug}
python3 tools/wiki_check_synthesis.py {slug} --min-pages {min_pages} --max-pages {max_pages}{allowed_page_args(allowed_paths)} --require-allowed-pages --normalized-source {normalized_source.as_posix()}{range_page_args(selected_paths)}
pnpm wiki:grounding:check
```

If validation still fails, repair only the allowed files and rerun the same commands.
"""


def print_result(result: Result) -> None:
    codex_status = ", ".join("timeout" if code is None else str(
        code) for code in result.codex_returncodes)
    validation_status = "pass" if result.validation_returncode == 0 else f"fail:{result.validation_returncode}"
    print(f"\n## {result.candidate.label}")
    print(f"- worktree: {result.worktree}")
    print(f"- duration_s: {result.duration_s:.1f}")
    print(f"- codex_returncodes: {codex_status}")
    print(f"- validation: {validation_status}")
    print("- changed_files:")
    if result.changed_files:
        for changed in result.changed_files:
            print(f"  - {changed}")
    else:
        print("  - None")
    log_list = ", ".join(str(path) for path in result.log_paths)
    print(f"- logs: {log_list}, {result.worktree / 'phase2-validation.log'}")


def write_report(path: Path, slug: str, results: list[Result]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Phase 2 Benchmark Report",
        "",
        f"- Source slug: `{slug}`",
        f"- Candidates: {len(results)}",
        "",
        "| Candidate | Duration | Codex | Validation | Worktree |",
        "|---|---:|---|---|---|",
    ]
    for result in results:
        codex_status = ", ".join("timeout" if code is None else str(
            code) for code in result.codex_returncodes)
        validation_status = "pass" if result.validation_returncode == 0 else f"fail:{result.validation_returncode}"
        lines.append(
            f"| {result.candidate.label} | {result.duration_s:.1f}s | {codex_status} | {validation_status} | `{result.worktree}` |"
        )
    lines.extend(["", "## Changed Files", ""])
    for result in results:
        lines.extend([f"### {result.candidate.label}", ""])
        if result.changed_files:
            lines.extend(f"- `{changed}`" for changed in result.changed_files)
        else:
            lines.append("- None.")
        lines.append("")
    path.write_text("\n".join(lines).rstrip() + "\n")
    print(f"wrote {path}")


def selected_candidate_paths(source_page: Path, max_pages: int) -> list[RelatedCandidate]:
    fm = parse_frontmatter(source_page)
    related = section(fm.body, "## Related pages")
    rows = related_candidate_rows(related)
    if rows:
        return sorted(rows, key=lambda row: (PRIORITY_ORDER.get(row.priority, 1), row.index))[:max_pages]
    return [
        RelatedCandidate(path=path, priority="should create", index=index)
        for index, path in enumerate(code_paths(related)[:max_pages])
    ]


def existing_created_paths(source_page: Path) -> list[str]:
    fm = parse_frontmatter(source_page)
    related = section(fm.body, "## Related pages")
    paths: list[str] = []
    for line in related.splitlines():
        cells = split_table_row(line)
        if cells is None or is_separator_row(cells) or cells[0].lower() in {"candidate page", "page"}:
            continue
        if len(cells) not in {3, 5, 6}:
            continue
        if cells[-1].strip().lower() != "created":
            continue
        target = markdown_target(cells[1])
        if target:
            paths.append(target)
    return sorted(set(paths))


def related_candidate_rows(markdown: str) -> list[RelatedCandidate]:
    rows: list[RelatedCandidate] = []
    for index, line in enumerate(markdown.splitlines()):
        cells = split_table_row(line)
        if cells is None or len(cells) not in {3, 5, 6}:
            continue
        if is_separator_row(cells) or cells[0].lower() in {"candidate page", "page"}:
            continue
        status = cells[-1].strip().lower()
        target = code_cell_target(cells[1])
        if status != "not created yet" or target is None:
            continue
        group = cells[2].strip() if len(cells) == 6 else None
        priority = cells[3].strip().lower() if len(cells) == 6 else cells[2].strip(
        ).lower() if len(cells) == 5 else "should create"
        evidence_basis = cells[4].strip() if len(
            cells) == 6 else cells[3].strip() if len(cells) == 5 else None
        rows.append(RelatedCandidate(path=target, group=group,
                    priority=priority, evidence_basis=evidence_basis, index=index))
    return rows


def render_selected_candidates(candidates: list[RelatedCandidate]) -> str:
    if not candidates:
        return "- No candidate paths found; stop and report this."
    lines: list[str] = []
    for candidate in candidates:
        group = candidate.group or "unclassified"
        evidence_basis = f"; evidence basis: {candidate.evidence_basis}" if candidate.evidence_basis else ""
        lines.append(
            f"- `{candidate.path}` - group: {group}; priority: {candidate.priority}{evidence_basis}")
    return "\n".join(lines)


def render_existing_pages(paths: list[str]) -> str:
    if not paths:
        return "- None."
    return "\n".join(f"- `{path}`" for path in paths)


@dataclass
class EvidenceItem:
    """A single evidence snippet with an ID."""
    id: str  # e.g., "E01", "E02"
    locator: str  # e.g., "normalized:L123"
    text: str  # The actual evidence text
    candidate: str  # Which candidate/topic this belongs to
    # Enriched context (optional)
    context_before: str = ""  # 3 lines before the evidence
    evidence_line: str = ""  # The actual line at the locator
    context_after: str = ""  # 3 lines after the evidence
    line_start: int = 0  # Starting line number (1-indexed)


@dataclass
class EvidenceBankResult:
    """Result of building an evidence bank."""
    prompt_text: str  # Rendered text for the prompt
    items: dict[str, EvidenceItem]  # ID -> EvidenceItem mapping
    by_locator: dict[str, EvidenceItem]  # locator -> EvidenceItem mapping


def build_evidence_bank(
    worktree: Path,
    normalized_source: Path,
    selected_candidates: list[str | RelatedCandidate],
    extraction_claims: list[dict] | None = None,
    use_ids: bool = True,
    slug: str = "",
) -> str | EvidenceBankResult:
    """Build evidence bank for synthesis prompt.

    If use_ids is True (default), returns an EvidenceBankResult with:
    - prompt_text: ID-based format for efficient model output
    - items: dict mapping IDs to EvidenceItem objects
    - by_locator: dict mapping locators to EvidenceItem objects

    If use_ids is False, returns the legacy string format.
    """
    source_path = normalized_source if normalized_source.is_absolute() else worktree / \
        normalized_source
    if not source_path.exists():
        if use_ids:
            return EvidenceBankResult(
                prompt_text="No evidence bank available; normalized source was not found.",
                items={},
                by_locator={},
            )
        return "No evidence bank available; normalized source was not found."

    source_text = source_path.read_text(errors="ignore")
    lines = source_text.splitlines()

    # Only need chunks if we're not using extraction claims
    chunks = None if extraction_claims else source_chunks(source_text)

    sections: list[str] = []
    items: dict[str, EvidenceItem] = {}
    by_locator: dict[str, EvidenceItem] = {}
    evidence_id = 1

    for candidate in selected_candidates:
        query = evidence_query(candidate)
        ranges = source_ranges_for_candidate(candidate_path(
            candidate), lines, candidate_title(candidate))

        # Try to get claims from extraction state by matching topic name
        matched_claims = None
        if extraction_claims:
            candidate_title_text = candidate_title(candidate) or ""
            # Match by topic name (case-insensitive comparison)
            matched_claims = [
                c for c in extraction_claims
                if c.get("topic", "").lower() == candidate_title_text.lower()
            ]

        sections.append(f"### {query}")
        if ranges and not use_ids:
            sections.append(
                f"Allowed source range: `{format_ranges(ranges)}` ({'; '.join(r.reason for r in ranges)})")

        evidence_items: list[tuple[str, str]] = []  # (locator, text)

        if matched_claims:
            # Use full evidence from extraction state (preferred)
            for claim in matched_claims[:10]:
                locator = claim.get("locator", "")
                evidence = claim.get("evidence", "")
                if evidence and locator:
                    # Truncate very long evidence for readability
                    if len(evidence) > 400:
                        evidence = evidence[:400] + "..."
                    # Normalize to always-range format
                    evidence_items.append((normalize_locator(locator), evidence))
        else:
            # Fall back to re-extracting snippets (less accurate)
            if chunks is None:
                chunks = source_chunks(source_text)
            candidate_chunks = chunks_in_ranges(
                chunks, ranges) if ranges else chunks
            snippets = snippets_for_candidate(
                query, candidate_chunks, limit=10)
            for snippet in snippets:
                # Normalize to always-range format (source_chunks already does this)
                evidence_items.append((normalize_locator(snippet.locator), snippet.text))

        if not evidence_items:
            sections.append("- not covered in sources")
        elif use_ids:
            # Format with IDs
            for locator, text in evidence_items:
                eid = f"E{evidence_id:02d}"
                evidence_id += 1

                # Extract line number from locator for context
                # Locators are 1-indexed (L1 = first line), arrays are 0-indexed
                line_start = 0
                match = re.search(r"L(\d+)", locator)
                if match:
                    line_start = int(match.group(1))  # 1-indexed

                # Get surrounding context (±3 lines)
                context_before = ""
                context_after = ""
                evidence_line = ""
                context_lines = 3

                if line_start > 0:
                    idx = line_start - 1  # Convert to 0-indexed

                    # Context before (3 lines)
                    before_start = max(0, idx - context_lines)
                    context_before = "\n".join(lines[before_start:idx])

                    # Evidence line itself
                    if idx < len(lines):
                        evidence_line = lines[idx]

                    # Find end line (from range or single line)
                    end_match = re.search(r"L\d+-L(\d+)", locator)
                    line_end_1indexed = int(end_match.group(
                        1)) if end_match else line_start
                    line_end_idx = line_end_1indexed - 1  # Convert to 0-indexed

                    # Context after (3 lines after the end)
                    after_end = min(
                        len(lines), line_end_idx + 1 + context_lines)
                    context_after = "\n".join(
                        lines[line_end_idx + 1:after_end])

                # Truncate for prompt display
                display_text = text[:150] + "..." if len(text) > 150 else text
                sections.append(f'[{eid}] {locator} "{display_text}"')

                item = EvidenceItem(
                    id=eid,
                    locator=locator,
                    text=text,
                    candidate=query,
                    context_before=context_before,
                    evidence_line=evidence_line,
                    context_after=context_after,
                    line_start=line_start,
                )
                items[eid] = item
                by_locator[locator] = item
        else:
            # Legacy format
            for locator, text in evidence_items:
                sections.append(f"- `{locator}` - {text}")

        sections.append("")

    prompt_text = "\n".join(sections).rstrip()

    if use_ids:
        return EvidenceBankResult(
            prompt_text=prompt_text,
            items=items,
            by_locator=by_locator,
        )
    return prompt_text


def evidence_query(candidate: str | RelatedCandidate) -> str:
    if isinstance(candidate, str):
        return candidate
    parts = [candidate.path]
    if candidate.group:
        parts.append(candidate.group)
    if candidate.evidence_basis:
        parts.append(candidate.evidence_basis)
    return " ".join(parts)


def candidate_path(candidate: str | RelatedCandidate) -> str:
    return candidate.path if isinstance(candidate, RelatedCandidate) else candidate


def candidate_title(candidate: str | RelatedCandidate) -> str | None:
    if not isinstance(candidate, RelatedCandidate):
        return None
    return Path(candidate.path).stem.replace("-", " ").title()


def chunks_in_ranges(chunks, ranges: list[SourceRange]):
    scoped = []
    for chunk in chunks:
        parsed = parse_locator_range(chunk.locator)
        if parsed is None:
            continue
        start, end = parsed
        if locator_within_ranges(start, end, ranges):
            scoped.append(chunk)
    return scoped


def split_table_row(line: str) -> list[str] | None:
    stripped = line.strip()
    if not stripped.startswith("|") or not stripped.endswith("|"):
        return None
    return [cell.strip() for cell in stripped[1:-1].split("|")]


def is_separator_row(cells: list[str]) -> bool:
    return all(cell and set(cell) <= {"-", ":", " "} for cell in cells)


def code_cell_target(cell: str) -> str | None:
    stripped = cell.strip()
    if stripped.startswith("`") and stripped.endswith("`") and stripped.count("`") == 2:
        value = stripped[1:-1].strip()
        if value.endswith(".md"):
            return value
    return None


def markdown_target(cell: str) -> str | None:
    match = re.fullmatch(r"\[[^\]]+\]\(([^)]+\.md)\)", cell.strip())
    return match.group(1) if match else None


def source_relative_to_repo(path: str) -> str:
    return (Path("wiki/sources") / path).resolve().relative_to(Path.cwd().resolve()).as_posix()


def allowed_page_args(paths: list[str]) -> str:
    if not paths:
        return ""
    return "".join(f" --allowed-page {source_relative_to_repo(path)}" for path in paths)


def range_page_args(paths: list[str]) -> str:
    if not paths:
        return ""
    return "".join(f" --range-page {source_relative_to_repo(path)}" for path in paths)


if __name__ == "__main__":
    sys.exit(main())
