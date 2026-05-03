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


IGNORE_NAMES = {
    ".git",
    "node_modules",
    "__pycache__",
    ".pytest_cache",
    "coverage",
    "dist",
    "Example_AGENTS.md",
    "Handoff.md",
}


@dataclass(frozen=True)
class Candidate:
    raw: str
    profile: str
    model: str | None

    @property
    def label(self) -> str:
        return self.raw

    @property
    def safe_label(self) -> str:
        return re.sub(r"[^A-Za-z0-9_.-]+", "_", self.raw)


@dataclass
class Result:
    candidate: Candidate
    worktree: Path
    duration_s: float
    codex_returncodes: list[int | None]
    validation_returncode: int | None
    changed_files: list[str]
    log_paths: list[Path]


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Benchmark local Codex candidates on one Phase 1 source-page repair task."
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
    parser.add_argument("--normalized-source", help="explicit normalized markdown path")
    parser.add_argument("--prompt-template", default="tools/prompts/phase1-source-repair.md")
    parser.add_argument("--codex-bin", default="codex")
    parser.add_argument("--timeout", type=int, default=600)
    parser.add_argument("--min-claims", type=int, default=12)
    parser.add_argument("--max-claims", type=int, default=32)
    parser.add_argument("--min-claim-words", type=int, default=10)
    parser.add_argument("--min-related-candidates", type=int, default=8)
    parser.add_argument("--max-related-candidates", type=int, default=16)
    parser.add_argument("--min-natural-groups", type=int, default=2)
    parser.add_argument(
        "--allow-weak-claims",
        action="store_true",
        help="do not pass --reject-weak-claims to the source checker",
    )
    parser.add_argument(
        "--max-unsupported-claim-tokens",
        type=int,
        default=0,
        help="optional lexical source-grounding check; 0 disables",
    )
    parser.add_argument(
        "--repair-attempts",
        type=int,
        default=1,
        help="number of extra Codex repair prompts to run after failed validation",
    )
    parser.add_argument("--keep", action="store_true", help="keep temp worktrees after the run")
    args = parser.parse_args()

    repo_root = Path.cwd()
    normalized_source = Path(args.normalized_source) if args.normalized_source else find_normalized_source(args.slug)
    if not normalized_source.exists():
        print(f"FAIL: normalized source does not exist: {normalized_source}", file=sys.stderr)
        return 2

    prompt_template = Path(args.prompt_template)
    if not prompt_template.exists():
        print(f"FAIL: prompt template does not exist: {prompt_template}", file=sys.stderr)
        return 2

    candidates = [parse_candidate(raw) for raw in (args.candidate or ["local-4090"])]
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
            min_claims=args.min_claims,
            max_claims=args.max_claims,
            min_claim_words=args.min_claim_words,
            min_related_candidates=args.min_related_candidates,
            max_related_candidates=args.max_related_candidates,
            min_natural_groups=args.min_natural_groups,
            reject_weak_claims=not args.allow_weak_claims,
            max_unsupported_claim_tokens=args.max_unsupported_claim_tokens,
            repair_attempts=args.repair_attempts,
        )
        results.append(result)
        print_result(result)
        if not args.keep:
            shutil.rmtree(result.worktree, ignore_errors=True)

    return 0 if all(result.validation_returncode == 0 for result in results) else 1


def parse_candidate(raw: str) -> Candidate:
    if ":" not in raw:
        return Candidate(raw=raw, profile=raw, model=None)
    profile, model = raw.split(":", 1)
    if not profile or not model:
        raise SystemExit(f"invalid candidate {raw!r}; use PROFILE or PROFILE:MODEL")
    return Candidate(raw=raw, profile=profile, model=model)


def find_normalized_source(slug: str) -> Path:
    root = Path("raw/normalized") / slug
    matches = sorted(path for path in root.rglob("*.md") if path.is_file())
    if len(matches) == 1:
        return matches[0]
    if not matches:
        raise SystemExit(f"no normalized markdown files found under {root}")
    joined = "\n".join(str(path) for path in matches)
    raise SystemExit(f"multiple normalized markdown files found under {root}; pass --normalized-source\n{joined}")


def run_candidate(
    *,
    repo_root: Path,
    slug: str,
    normalized_source: Path,
    prompt_template: Path,
    candidate: Candidate,
    codex_bin: str,
    timeout: int,
    min_claims: int,
    max_claims: int,
    min_claim_words: int,
    min_related_candidates: int,
    max_related_candidates: int,
    min_natural_groups: int,
    reject_weak_claims: bool,
    max_unsupported_claim_tokens: int,
    repair_attempts: int,
) -> Result:
    worktree = Path(
        tempfile.mkdtemp(prefix=f"llm-wiki-phase1-{slug}-{candidate.safe_label}.", dir="/tmp")
    )
    copy_repo(repo_root, worktree)
    init_git(worktree)

    prompt = render_prompt(
        template=(worktree / prompt_template).read_text(),
        slug=slug,
        normalized_source=normalized_source.as_posix(),
        source_type=source_type_for_slug(slug),
        imported_original=imported_original_for_slug(slug),
        min_claims=min_claims,
        max_claims=max_claims,
        min_claim_words=min_claim_words,
        min_related_candidates=min_related_candidates,
        max_related_candidates=max_related_candidates,
        min_natural_groups=min_natural_groups,
        reject_weak_claims=reject_weak_claims,
        max_unsupported_claim_tokens=max_unsupported_claim_tokens,
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
        min_claims,
        max_claims,
        min_claim_words,
        min_related_candidates,
        max_related_candidates,
        min_natural_groups,
        reject_weak_claims,
        normalized_source,
        max_unsupported_claim_tokens,
    )

    for attempt in range(1, repair_attempts + 1):
        if validation_returncode == 0:
            break
        repair_prompt = render_repair_prompt(
            slug=slug,
            validation_output=(worktree / "phase1-validation.log").read_text(),
            min_claims=min_claims,
            max_claims=max_claims,
            min_claim_words=min_claim_words,
            min_related_candidates=min_related_candidates,
            max_related_candidates=max_related_candidates,
            min_natural_groups=min_natural_groups,
            reject_weak_claims=reject_weak_claims,
            normalized_source=normalized_source,
            max_unsupported_claim_tokens=max_unsupported_claim_tokens,
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
            min_claims,
            max_claims,
            min_claim_words,
            min_related_candidates,
            max_related_candidates,
            min_natural_groups,
            reject_weak_claims,
            normalized_source,
            max_unsupported_claim_tokens,
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


def run_codex(
    *,
    worktree: Path,
    candidate: Candidate,
    codex_bin: str,
    prompt: str,
    timeout: int,
    prefix: str,
) -> tuple[int | None, list[Path]]:
    stdout_path = worktree / f"{prefix}-stdout.log"
    stderr_path = worktree / f"{prefix}-stderr.log"
    last_message_path = worktree / f"{prefix}-last-message.md"
    command = [
        codex_bin,
        "exec",
        "--profile",
        candidate.profile,
        "--cd",
        str(worktree),
        "--dangerously-bypass-approvals-and-sandbox",
        "--skip-git-repo-check",
        "--ephemeral",
        "--output-last-message",
        str(last_message_path),
    ]
    if candidate.model:
        command.extend(["--model", candidate.model])
    command.append("-")

    with stdout_path.open("w") as stdout, stderr_path.open("w") as stderr:
        try:
            completed = subprocess.run(
                command,
                cwd=worktree,
                input=prompt,
                text=True,
                stdout=stdout,
                stderr=stderr,
                timeout=timeout,
            )
            return completed.returncode, [stdout_path, stderr_path, last_message_path]
        except subprocess.TimeoutExpired:
            stderr.write(f"\nTIMEOUT after {timeout} seconds\n")
            return None, [stdout_path, stderr_path, last_message_path]


def copy_repo(src: Path, dst: Path) -> None:
    def ignore(_directory: str, names: list[str]) -> set[str]:
        return {name for name in names if name in IGNORE_NAMES}

    for child in src.iterdir():
        if child.name in IGNORE_NAMES:
            continue
        target = dst / child.name
        if child.is_dir():
            shutil.copytree(child, target, ignore=ignore)
        else:
            shutil.copy2(child, target)


def init_git(worktree: Path) -> None:
    run(["git", "init", "-q"], worktree)
    exclude = worktree / ".git/info/exclude"
    with exclude.open("a") as f:
        f.write("\n# Generated by tools/wiki_phase1_benchmark.py\n")
        f.write("codex-*.log\n")
        f.write("codex-*.md\n")
        f.write("phase*-validation*.log\n")
    run(["git", "add", "-A"], worktree)
    run(
        [
            "git",
            "-c",
            "user.name=LLM Wiki Benchmark",
            "-c",
            "user.email=benchmark@example.invalid",
            "commit",
            "-qm",
            "baseline",
        ],
        worktree,
    )


def render_prompt(
    *,
    template: str,
    slug: str,
    normalized_source: str,
    source_type: str,
    imported_original: str,
    min_claims: int,
    max_claims: int,
    min_claim_words: int,
    min_related_candidates: int,
    max_related_candidates: int,
    min_natural_groups: int,
    reject_weak_claims: bool,
    max_unsupported_claim_tokens: int,
) -> str:
    replacements = {
        "{{current_date}}": date.today().isoformat(),
        "{{slug}}": slug,
        "{{normalized_source}}": normalized_source,
        "{{source_type}}": source_type,
        "{{imported_original}}": imported_original,
        "{{min_claims}}": str(min_claims),
        "{{max_claims}}": str(max_claims),
        "{{min_claim_words}}": str(min_claim_words),
        "{{min_related_candidates}}": str(min_related_candidates),
        "{{max_related_candidates}}": str(max_related_candidates),
        "{{min_natural_groups}}": str(min_natural_groups),
        "{{weak_claims_flag}}": "--reject-weak-claims" if reject_weak_claims else "",
        "{{grounding_flag}}": (
            f"--normalized-source {normalized_source}"
            + (
                f" --max-unsupported-claim-tokens {max_unsupported_claim_tokens}"
                if max_unsupported_claim_tokens
                else ""
            )
        ),
    }
    rendered = template
    for old, new in replacements.items():
        rendered = rendered.replace(old, new)
    return rendered


def source_type_for_slug(slug: str) -> str:
    imported = Path("raw/imported") / slug
    if (imported / "original.pdf").exists():
        return "pdf"
    if (imported / "original.md").exists():
        return "markdown"
    return "other"


def imported_original_for_slug(slug: str) -> str:
    source_type = source_type_for_slug(slug)
    if source_type == "pdf":
        return "original.pdf"
    if source_type == "markdown":
        return "original.md"
    return "original"


def render_repair_prompt(
    *,
    slug: str,
    validation_output: str,
    min_claims: int,
    max_claims: int,
    min_claim_words: int,
    min_related_candidates: int,
    max_related_candidates: int,
    min_natural_groups: int,
    reject_weak_claims: bool,
    normalized_source: Path,
    max_unsupported_claim_tokens: int,
) -> str:
    weak_claims_line = ""
    weak_claims_flag = ""
    if reject_weak_claims:
        weak_claims_line = (
            "- The words important, crucial, fundamental, essential, and success are validation "
            "failures in `## Key claims`.\n"
        )
        weak_claims_flag = " --reject-weak-claims"
    grounding_line = (
        f"- Evidence excerpts and locators must resolve inside `{normalized_source.as_posix()}`.\n"
    )
    grounding_flag = f" --normalized-source {normalized_source.as_posix()}"
    if max_unsupported_claim_tokens:
        grounding_line += (
            f"- Avoid introducing claim terms that are absent from `{normalized_source.as_posix()}`; "
            "reuse source vocabulary for specific units, timings, resources, and map mechanics.\n"
        )
        grounding_flag += f" --max-unsupported-claim-tokens {max_unsupported_claim_tokens}"
    return f"""Read `AGENTS.md` fully before acting.

Repair only `wiki/sources/{slug}.md`.

Forbidden writes:
- `raw/imported/**`
- `raw/normalized/**`
- `wiki/index.md`
- `wiki/log.md`
- `wiki/_graph.json`
- `wiki/_linter-report.md`
- `wiki/concepts/**`
- `wiki/entities/**`
- `wiki/procedures/**`
- `wiki/references/**`
- `wiki/analyses/**`
- `packages/**`
- `tools/**`

Validation failed with this exact output:

```text
{validation_output.strip()}
```

Fix the failures mechanically:
- If a key claim is flagged as document metadata, rewrite that claim as a direct gameplay fact.
- In `## Key claims`, do not use these validation-failure words: guide, document, author, coached, coaching, Twitch, Google Docs, published.
- Keep {min_claims} to {max_claims} key claims.
- Write `## Key claims` as a `| Claim | Evidence | Locator |` table, not a numbered list.
- Each evidence cell must contain a short exact excerpt from `{normalized_source.as_posix()}`.
- Each locator must use `normalized:L12` or `normalized:L12-L14`, and the excerpt must appear inside that locator range.
- Each key claim must be at least {min_claim_words} words.
{weak_claims_line.rstrip()}
{grounding_line.rstrip()}
- Keep `## Related pages` as a candidate table with code-formatted intended paths only.
- Keep {min_related_candidates} to {max_related_candidates} strong related-page candidates.
- Keep at least {min_natural_groups} source-native natural groups under `## Major concepts` in the required table shape.
- Every `## Related pages` row must include a Group cell copied from that natural group table.
- Do not create related pages.

After editing, run exactly:

```bash
python3 tools/wiki_check_source.py {slug} --min-claims {min_claims} --max-claims {max_claims} --min-claim-words {min_claim_words} --min-related-candidates {min_related_candidates} --max-related-candidates {max_related_candidates} --require-natural-groups --min-natural-groups {min_natural_groups} --require-claim-evidence{weak_claims_flag}{grounding_flag}
```

If validation still fails, repair only `wiki/sources/{slug}.md` and rerun the same command.
"""


def run_validation(
    worktree: Path,
    slug: str,
    min_claims: int,
    max_claims: int,
    min_claim_words: int,
    min_related_candidates: int,
    max_related_candidates: int,
    min_natural_groups: int,
    reject_weak_claims: bool,
    normalized_source: Path,
    max_unsupported_claim_tokens: int,
) -> int:
    command = [
        "python3",
        "tools/wiki_check_source.py",
        slug,
        "--min-claims",
        str(min_claims),
        "--max-claims",
        str(max_claims),
        "--min-claim-words",
        str(min_claim_words),
        "--min-related-candidates",
        str(min_related_candidates),
        "--max-related-candidates",
        str(max_related_candidates),
        "--require-natural-groups",
        "--min-natural-groups",
        str(min_natural_groups),
        "--require-claim-evidence",
        "--normalized-source",
        normalized_source.as_posix(),
    ]
    if reject_weak_claims:
        command.append("--reject-weak-claims")
    if max_unsupported_claim_tokens:
        command.extend(
            [
                "--max-unsupported-claim-tokens",
                str(max_unsupported_claim_tokens),
            ]
        )

    completed = subprocess.run(
        command,
        cwd=worktree,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    (worktree / "phase1-validation.log").write_text(completed.stdout)
    return completed.returncode


def git_changed_files(worktree: Path) -> list[str]:
    completed = subprocess.run(
        ["git", "status", "--short", "--untracked-files=all"],
        cwd=worktree,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
        check=False,
    )
    return [line.rstrip() for line in completed.stdout.splitlines() if line.strip()]


def run(command: list[str], cwd: Path) -> None:
    subprocess.run(command, cwd=cwd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def print_result(result: Result) -> None:
    codex_status = ", ".join("timeout" if code is None else str(code) for code in result.codex_returncodes)
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
    print(f"- logs: {log_list}, {result.worktree / 'phase1-validation.log'}")


if __name__ == "__main__":
    sys.exit(main())
