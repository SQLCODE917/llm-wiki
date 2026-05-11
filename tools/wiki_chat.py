#!/usr/bin/env python3
"""Interactive chat REPL for llm-wiki using cloud model backends.

Usage:
    pnpm wiki:chat
    pnpm wiki:chat --backend bedrock
    
Commands:
    /query <question>  - Search wiki and answer from pages
    /ingest <path>     - Start guided PDF ingestion
    /lint              - Run wiki linter
    /status            - Show wiki health summary
    /help              - Show this help
    /quit              - Exit chat
    
Regular messages are sent directly to the model with AGENTS.md context.
"""
from __future__ import annotations

import argparse
import os
import readline  # noqa: F401 - enables line editing in input()
import sys
from pathlib import Path

from wiki_model_backend import get_backend, ModelConfig, ModelResponse


WELCOME = """
╭─────────────────────────────────────────────────────────────╮
│  llm-wiki interactive chat                                  │
│                                                             │
│  Commands:                                                  │
│    /query <question>  - Answer from wiki pages              │
│    /ingest <path>     - Guided PDF ingestion                │
│    /lint              - Run wiki linter                     │
│    /status            - Wiki health summary                 │
│    /help              - Show commands                       │
│    /quit              - Exit                                │
│                                                             │
│  Or just type naturally to chat with the wiki agent.        │
╰─────────────────────────────────────────────────────────────╯
"""

HELP_TEXT = """
Commands:
  /query <question>   Search the wiki and answer from relevant pages
  /ingest <path>      Start guided ingestion of a PDF or markdown file
  /lint               Run wiki linter and show results
  /status             Show wiki health summary (index, graph, grounding)
  /clear              Clear conversation history
  /help               Show this help message
  /quit or /exit      Exit the chat

Tips:
  - Regular messages go directly to the model with AGENTS.md context
  - Use /query for wiki-grounded answers with page citations
  - The model can run terminal commands and edit files when needed
"""


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Interactive chat REPL for llm-wiki")
    parser.add_argument(
        "--backend",
        default=os.environ.get("WIKI_MODEL_BACKEND", "bedrock"),
        help="Model backend: bedrock, openai, anthropic (default: from WIKI_MODEL_BACKEND or bedrock)",
    )
    parser.add_argument("--timeout", type=int, default=120,
                        help="Response timeout in seconds")
    args = parser.parse_args()

    # Initialize backend
    try:
        backend = get_backend(args.backend)
    except Exception as e:
        print(
            f"Failed to initialize {args.backend} backend: {e}", file=sys.stderr)
        return 1

    print(WELCOME)
    print(f"Backend: {backend.__class__.__name__}")
    print()

    # Load system context
    system_context = load_system_context()
    conversation: list[dict[str, str]] = []

    while True:
        try:
            user_input = input("llm-wiki> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            return 0

        if not user_input:
            continue

        # Handle commands
        if user_input.startswith("/"):
            result = handle_command(user_input, backend, args.timeout)
            if result == "quit":
                print("Goodbye!")
                return 0
            if result == "clear":
                conversation = []
                print("Conversation cleared.")
                continue
            if result:
                print(result)
            continue

        # Regular chat message
        conversation.append({"role": "user", "content": user_input})

        # Build prompt with conversation history
        prompt = build_chat_prompt(system_context, conversation)

        print("Thinking...", end="", flush=True)
        config = ModelConfig(
            worktree=Path.cwd(),
            prefix="chat",
            timeout=args.timeout,
        )

        try:
            response = backend.run(prompt, config)
            print("\r" + " " * 12 + "\r", end="")  # Clear "Thinking..."

            if response.success:
                print(response.output)
                conversation.append(
                    {"role": "assistant", "content": response.output})
            else:
                print(f"Error: {response.error}")
        except Exception as e:
            print(f"\rError: {e}")

    return 0


def load_system_context() -> str:
    """Load AGENTS.md and wiki index for system context."""
    parts = []

    agents_path = Path("AGENTS.md")
    if agents_path.exists():
        parts.append(f"# Operating Rules\n\n{agents_path.read_text()}")

    index_path = Path("wiki/index.md")
    if index_path.exists():
        parts.append(f"# Wiki Index\n\n{index_path.read_text()}")

    return "\n\n---\n\n".join(parts)


def build_chat_prompt(system_context: str, conversation: list[dict[str, str]]) -> str:
    """Build a prompt from system context and conversation history."""
    # Format conversation history
    history_parts = []
    for msg in conversation[-10:]:  # Keep last 10 messages for context
        role = msg["role"].upper()
        history_parts.append(f"{role}: {msg['content']}")

    history = "\n\n".join(history_parts)

    return f"""You are an interactive wiki maintenance assistant. Help the user query, maintain, and update the llm-wiki.

{system_context}

---

# Conversation

{history}

---

Respond helpfully and concisely. When answering questions about the wiki, cite specific pages.
If you need to run commands or edit files, describe what you would do (you cannot execute commands in this mode).
For actual file operations, suggest the user run specific pnpm commands."""


def handle_command(cmd: str, backend, timeout: int) -> str | None:
    """Handle slash commands. Returns output string, 'quit', 'clear', or None."""
    parts = cmd.split(None, 1)
    command = parts[0].lower()
    arg = parts[1] if len(parts) > 1 else ""

    if command in ("/quit", "/exit", "/q"):
        return "quit"

    if command == "/clear":
        return "clear"

    if command == "/help":
        return HELP_TEXT

    if command == "/query":
        if not arg:
            return "Usage: /query <your question>"
        return run_query(arg, backend, timeout)

    if command == "/ingest":
        if not arg:
            return "Usage: /ingest <path to PDF or markdown>"
        return run_ingest_guide(arg)

    if command == "/lint":
        return run_lint()

    if command == "/status":
        return run_status()

    return f"Unknown command: {command}. Type /help for available commands."


def run_query(question: str, backend, timeout: int) -> str:
    """Run a wiki query using the query tool's page selection."""
    try:
        from wiki_query import select_pages, render_prompt

        hits = select_pages(question, max_pages=6)
        if not hits:
            return "No relevant wiki pages found for that question."

        prompt = render_prompt(question, hits)
        config = ModelConfig(
            worktree=Path.cwd(),
            prefix="query",
            timeout=timeout,
        )

        response = backend.run(prompt, config)
        if response.success:
            # Add page citations
            pages_used = "\n".join(
                f"  - {hit.path.as_posix()}" for hit in hits)
            return f"{response.output}\n\n📚 Pages consulted:\n{pages_used}"
        else:
            return f"Query failed: {response.error}"
    except Exception as e:
        return f"Query error: {e}"


def run_ingest_guide(path: str) -> str:
    """Run cloud ingestion or provide guidance."""
    p = Path(path)
    if not p.exists():
        return f"File not found: {path}"

    # Derive slug from filename
    slug = p.stem.lower().replace(" ", "-").replace("_", "-")

    # Ask if user wants to run automated ingest
    return f"""📥 Ready to ingest: {path}
Slug: {slug}

To run automated cloud ingestion:
```bash
AWS_PROFILE=sdai-dev pnpm wiki:ingest:cloud {path} --slug {slug}
```

Or run phases manually:
1. Phase 0: `pnpm wiki:phase0 {path} {slug}`
2. Phase 1: Create wiki/sources/{slug}.md
3. Phase 2: Synthesize concept pages
4. Phase 3: `pnpm wiki:phase3 {slug}`

Type `/run-ingest {slug}` to start automated ingestion now."""


def run_lint() -> str:
    """Run the wiki linter and return summary."""
    import subprocess

    try:
        result = subprocess.run(
            ["python3", "tools/wiki_lint.py"],
            capture_output=True,
            text=True,
            timeout=60,
        )

        # Read the report
        report_path = Path("wiki/_linter-report.md")
        if report_path.exists():
            report = report_path.read_text()
            # Extract summary (first ~30 lines)
            lines = report.splitlines()[:30]
            return "🔍 Linter Results:\n\n" + "\n".join(lines)
        else:
            return result.stdout or result.stderr or "Lint completed (no report generated)"
    except subprocess.TimeoutExpired:
        return "Lint timed out after 60 seconds"
    except Exception as e:
        return f"Lint error: {e}"


def run_status() -> str:
    """Show wiki health status summary."""
    status_parts = []

    # Check index
    index_path = Path("wiki/index.md")
    if index_path.exists():
        lines = index_path.read_text().splitlines()
        page_count = sum(1 for line in lines if line.strip().startswith("- ["))
        status_parts.append(f"📑 Index: {page_count} pages listed")
    else:
        status_parts.append("❌ Index: missing")

    # Check graph
    graph_path = Path("wiki/_graph.json")
    if graph_path.exists():
        import json
        try:
            graph = json.loads(graph_path.read_text())
            node_count = len(graph.get("nodes", {}))
            status_parts.append(f"🔗 Graph: {node_count} nodes")
        except Exception:
            status_parts.append("⚠️ Graph: exists but unreadable")
    else:
        status_parts.append("❌ Graph: missing")

    # Check linter report
    linter_path = Path("wiki/_linter-report.md")
    if linter_path.exists():
        content = linter_path.read_text()
        fails = content.count("FAIL")
        warns = content.count("WARN")
        status_parts.append(f"🔍 Last lint: {fails} FAILs, {warns} WARNs")
    else:
        status_parts.append("⚠️ Linter: no report (run /lint)")

    # Check grounding report
    grounding_path = Path("wiki/_grounding-report.md")
    if grounding_path.exists():
        status_parts.append("✅ Grounding: report exists")
    else:
        status_parts.append("⚠️ Grounding: no report")

    # Count wiki pages by type
    page_counts: dict[str, int] = {}
    for subdir in ["sources", "concepts", "entities", "procedures", "references", "analyses"]:
        dir_path = Path("wiki") / subdir
        if dir_path.exists():
            count = len(list(dir_path.glob("*.md")))
            if count > 0:
                page_counts[subdir] = count

    if page_counts:
        counts_str = ", ".join(f"{k}: {v}" for k, v in page_counts.items())
        status_parts.append(f"📄 Pages: {counts_str}")

    return "📊 Wiki Status\n\n" + "\n".join(status_parts)


if __name__ == "__main__":
    sys.exit(main())
