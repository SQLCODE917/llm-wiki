#!/usr/bin/env python3
from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

from wiki_phase1_benchmark import copy_repo


def main() -> int:
    parser = argparse.ArgumentParser(description="Smoke-test saved query analysis filing in a temp wiki copy.")
    parser.add_argument("--keep", action="store_true", help="keep the temp repo copy after the smoke test")
    args = parser.parse_args()

    repo_root = Path.cwd()
    worktree = Path(tempfile.mkdtemp(prefix="llm-wiki-query-smoke.", dir="/tmp"))
    try:
        copy_repo(repo_root, worktree)
        script = """
from pathlib import Path
import sys

sys.path.insert(0, "tools")
from wiki_query import finalize_analysis, save_analysis, select_pages

question = "What should a player scout for in AoE2?"
hits = select_pages(question, 4)
if not hits:
    raise SystemExit("no pages selected for smoke query")

answer = \"\"\"AoE2 scouting should not rely on auto-scout when efficient results are needed. The scouting procedure says the player should look for their own resources, enemy activity, and extra resources on the map. Early scouting starts around the player's town center, while enemy scouting checks golds, woodlines, berries, hills, and similar map features. Later scouting looks for enemy buildings, unit tech choices, and upgrades. This answer is based on the filed wiki pages selected by the deterministic query planner.\"\"\"

path = save_analysis(question, "smoke-query-analysis", answer, hits)
finalize_analysis(path, question, hits)
print(path.as_posix())
"""
        run([sys.executable, "-c", script], cwd=worktree)
        analysis = next((worktree / "wiki/analyses").glob("*-smoke-query-analysis.md"), None)
        if analysis is None:
            print("FAIL: smoke analysis page was not created", file=sys.stderr)
            return 1
        run([sys.executable, "tools/wiki_check_analysis.py", analysis.as_posix()], cwd=worktree)
        run([sys.executable, "tools/wiki_judge_analysis.py", analysis.as_posix(), "--deterministic-only"], cwd=worktree)
        run([sys.executable, "tools/wiki_index.py", "--check"], cwd=worktree)
        run([sys.executable, "tools/wiki_graph.py", "--check"], cwd=worktree)
        print(f"PASS: query analysis smoke test in {worktree}")
        return 0
    finally:
        if not args.keep:
            shutil.rmtree(worktree, ignore_errors=True)


def run(command: list[str], *, cwd: Path) -> None:
    subprocess.run(command, cwd=cwd, check=True)


if __name__ == "__main__":
    sys.exit(main())
