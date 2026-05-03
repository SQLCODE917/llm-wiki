#!/usr/bin/env python3
from __future__ import annotations

import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

from wiki_phase1_benchmark import copy_repo


def main() -> int:
    worktree = Path(tempfile.mkdtemp(prefix="llm-wiki-phase0-smoke.", dir="/tmp"))
    try:
        copy_repo(Path.cwd(), worktree)
        inbox = worktree / "raw/inbox"
        inbox.mkdir(parents=True, exist_ok=True)
        source = inbox / "phase0-smoke.md"
        source.write_text("# Phase 0 Smoke\n\nA small markdown source.\n")

        run(["python3", "tools/wiki_phase0_import.py", "raw/inbox/phase0-smoke.md", "phase0-smoke"], cwd=worktree)
        assert_file(worktree / "raw/imported/phase0-smoke/original.md")
        assert_file(worktree / "raw/normalized/phase0-smoke/source.md")

        duplicate = subprocess.run(
            ["python3", "tools/wiki_phase0_import.py", "raw/inbox/phase0-smoke.md", "phase0-smoke"],
            cwd=worktree,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            check=False,
        )
        if duplicate.returncode == 0:
            print("FAIL: duplicate import unexpectedly succeeded", file=sys.stderr)
            return 1

        run(
            [
                "python3",
                "tools/wiki_phase0_import.py",
                "raw/inbox/phase0-smoke.md",
                "phase0-smoke",
                "--reuse-imported",
                "--overwrite-normalized",
            ],
            cwd=worktree,
        )

        pdf = inbox / "phase0-smoke.pdf"
        pdf.write_bytes(b"%PDF-1.4\n% smoke only\n")
        dry_run = subprocess.run(
            ["python3", "tools/wiki_phase0_import.py", "raw/inbox/phase0-smoke.pdf", "phase0-smoke-pdf", "--dry-run"],
            cwd=worktree,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            check=False,
        )
        if dry_run.returncode != 0 or "marker_single" not in dry_run.stdout or "TORCH_DEVICE=cuda" not in dry_run.stdout:
            print(dry_run.stdout, file=sys.stderr)
            print("FAIL: pdf dry-run did not show marker command", file=sys.stderr)
            return 1

        print(f"PASS: phase0 smoke test in {worktree}")
        return 0
    finally:
        shutil.rmtree(worktree, ignore_errors=True)


def run(command: list[str], *, cwd: Path) -> None:
    subprocess.run(command, cwd=cwd, check=True)


def assert_file(path: Path) -> None:
    if not path.is_file():
        raise SystemExit(f"missing expected file {path}")


if __name__ == "__main__":
    sys.exit(main())
