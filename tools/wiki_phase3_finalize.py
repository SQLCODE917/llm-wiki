#!/usr/bin/env python3
from __future__ import annotations

import argparse
import subprocess
import sys


def main() -> int:
    parser = argparse.ArgumentParser(description="Finalize an ingest after source and synthesis phases.")
    parser.add_argument("slug", help="source slug, e.g. aoe2-basics")
    parser.add_argument("--summary", help="custom log summary")
    args = parser.parse_args()

    commands = [
        ["python3", "tools/wiki_index.py"],
        ["python3", "tools/wiki_graph.py"],
        ["python3", "tools/wiki_lint.py"],
        [
            "python3",
            "tools/wiki_log.py",
            "ingest",
            args.summary or f"finalized ingest for {args.slug}",
            "-d",
            f"Finalized source `{args.slug}` after phased ingest.",
            "-d",
            "Updated wiki/index.md and wiki/_graph.json.",
            "-d",
            "Generated wiki/_linter-report.md.",
        ],
    ]

    for command in commands:
        completed = subprocess.run(command, text=True)
        if completed.returncode != 0:
            print(f"FAIL: {' '.join(command)}", file=sys.stderr)
            return completed.returncode

    return 0


if __name__ == "__main__":
    sys.exit(main())
