#!/usr/bin/env python3
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


SERVICE_NAME = "llm-wiki-maintenance.service"
TIMER_NAME = "llm-wiki-maintenance.timer"


def main() -> int:
    parser = argparse.ArgumentParser(description="Install or print a user-level systemd timer for wiki maintenance.")
    parser.add_argument("--repo", default=Path.cwd().as_posix(), help="repo directory to run maintenance in")
    parser.add_argument("--on-calendar", default="daily", help="systemd OnCalendar value")
    parser.add_argument("--install", action="store_true", help="write files under ~/.config/systemd/user and enable the timer")
    parser.add_argument("--dry-run", action="store_true", help="print unit files without writing")
    parser.add_argument("--no-enable", action="store_true", help="write units but do not enable/start the timer")
    args = parser.parse_args()

    repo = Path(args.repo).resolve()
    service = render_service(repo)
    timer = render_timer(args.on_calendar)
    if args.dry_run or not args.install:
        print(f"# {SERVICE_NAME}\n{service}")
        print(f"# {TIMER_NAME}\n{timer}")
        if not args.install:
            print("# Pass --install to write these as user systemd units.")
        return 0

    user_dir = Path.home() / ".config/systemd/user"
    user_dir.mkdir(parents=True, exist_ok=True)
    (user_dir / SERVICE_NAME).write_text(service)
    (user_dir / TIMER_NAME).write_text(timer)
    print(f"wrote {user_dir / SERVICE_NAME}")
    print(f"wrote {user_dir / TIMER_NAME}")

    if not args.no_enable:
        run(["systemctl", "--user", "daemon-reload"])
        run(["systemctl", "--user", "enable", "--now", TIMER_NAME])
    return 0


def render_service(repo: Path) -> str:
    return f"""[Unit]
Description=Run LLM-Wiki maintenance checks

[Service]
Type=oneshot
WorkingDirectory={repo.as_posix()}
ExecStart=/usr/bin/env pnpm wiki:maintenance --append-log
"""


def render_timer(on_calendar: str) -> str:
    return f"""[Unit]
Description=Scheduled LLM-Wiki maintenance

[Timer]
OnCalendar={on_calendar}
Persistent=true

[Install]
WantedBy=timers.target
"""


def run(command: list[str]) -> None:
    subprocess.run(command, check=True)


if __name__ == "__main__":
    sys.exit(main())
