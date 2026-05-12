"""System prompt loading utilities.

Loads system prompts from tools/prompts/ directory.

Usage:
    from wiki_llm.prompts import load_system_prompt
    
    prompt = load_system_prompt("synthesis", worktree=Path("."))
"""
from __future__ import annotations

from pathlib import Path


# Map style names to prompt files
PROMPT_FILES = {
    "synthesis": "tools/prompts/system-synthesis.md",
    "synthesis-json": "tools/prompts/system-synthesis-json.md",
    "extract": "tools/prompts/system-extract.md",
    "query": "tools/prompts/system-query.md",
    "judge": "tools/prompts/system-judge.md",
    "base": "tools/prompts/system-base.md",
}


def load_system_prompt(style: str, worktree: Path | None = None) -> str:
    """Load a system prompt by style name.

    Supported styles:
    - "full": Complete AGENTS.md (~7K tokens)
    - "synthesis": Wiki page synthesis (~800 tokens)
    - "synthesis-json": JSON schema output for synthesis (~500 tokens)
    - "extract": Claim extraction (~500 tokens)
    - "query": Query answering (~400 tokens)
    - "judge": Claim judging (~400 tokens)
    - "base": Minimal base prompt

    Args:
        style: Prompt style name
        worktree: Working directory to resolve paths from

    Returns:
        Prompt content with working directory suffix
    """
    worktree = worktree or Path(".")

    if style in PROMPT_FILES:
        prompt_path = Path(PROMPT_FILES[style])
        alt_path = worktree / PROMPT_FILES[style]

        if alt_path.exists():
            prompt_content = alt_path.read_text()
        elif prompt_path.exists():
            prompt_content = prompt_path.read_text()
        else:
            # Fallback to full AGENTS.md if prompt not found
            prompt_content = _load_agents_md(worktree)
    else:
        # Default: use full AGENTS.md
        prompt_content = _load_agents_md(worktree)

    return f"""{prompt_content}

Working directory: {worktree}
"""


def _load_agents_md(worktree: Path) -> str:
    """Load AGENTS.md content."""
    agents_path = worktree / "AGENTS.md"
    if not agents_path.exists():
        agents_path = Path("AGENTS.md")

    if agents_path.exists():
        return agents_path.read_text()
    return "You are a wiki maintenance agent."


def load_prompt_template(name: str, worktree: Path | None = None) -> str | None:
    """Load a prompt template file by name.

    Args:
        name: Template name (e.g., "phase2-synthesis", "phase1-source-repair")
        worktree: Working directory to resolve paths from

    Returns:
        Template content or None if not found
    """
    worktree = worktree or Path(".")

    # Try with and without .md extension
    candidates = [
        worktree / "tools" / "prompts" / f"{name}.md",
        worktree / "tools" / "prompts" / name,
        Path("tools/prompts") / f"{name}.md",
        Path("tools/prompts") / name,
    ]

    for path in candidates:
        if path.exists():
            return path.read_text()

    return None


def get_available_prompts(worktree: Path | None = None) -> list[str]:
    """List available prompt templates.

    Returns:
        List of prompt template names (without .md extension)
    """
    worktree = worktree or Path(".")
    prompts_dir = worktree / "tools" / "prompts"

    if not prompts_dir.exists():
        prompts_dir = Path("tools/prompts")

    if not prompts_dir.exists():
        return []

    return sorted(
        p.stem for p in prompts_dir.glob("*.md")
    )
