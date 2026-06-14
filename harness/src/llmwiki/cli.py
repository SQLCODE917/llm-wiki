"""llmwiki CLI: ingest, query, lint.

Thin entry point — parses arguments, boots the backend, delegates to a
Session, prints the result. All wiki logic lives in domain/store/workflows.
"""

from __future__ import annotations

import argparse
import asyncio
import sys
from datetime import datetime
from pathlib import Path

from llmwiki.config import (
    VALID_STRICT_EVIDENCE_MODES,
    ConfigError,
    WikiPaths,
    load_backend_config,
    resolve_strict_evidence_mode,
)
from llmwiki.pdf import PdfError
from llmwiki.pdf.pipeline import ExtractionResult, ensure_extracted
from llmwiki.pdf.vision import AppleVisionRecognizer
from llmwiki.runtime.backend import start_backend
from llmwiki.runtime.chat_repl import ChatRepl
from llmwiki.runtime.session import ExtractFn, OperationResult, Session
from llmwiki.store import WikiStore
from llmwiki.store.chat_store import ChatStore


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="llmwiki",
        description="LLM-maintained local wiki (Ollama via forge).",
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=Path.cwd(),
        help="Project root containing raw/, wiki/, SCHEMA.md (default: cwd).",
    )
    parser.add_argument(
        "--runtime",
        help="Runtime profile: ollama-default or local-4090 "
        "(default: LLMWIKI_RUNTIME or ollama-default).",
    )
    sub = parser.add_subparsers(dest="op", required=True)

    ingest = sub.add_parser("ingest", help="Integrate one raw source into the wiki.")
    _add_strict_evidence_arg(ingest)
    ingest.add_argument("source", help="Source path relative to raw/, e.g. article.md")
    ingest.add_argument(
        "--reextract",
        action="store_true",
        help="PDF only: discard the cached extraction/manifest and start over "
        "(default resumes a partial ingest).",
    )
    ingest.add_argument(
        "--reintegrate",
        action="store_true",
        help="PDF only: rerun just the integrate pass of a completed ingest "
        "(rebuilds the hub with current salience).",
    )

    query = sub.add_parser("query", help="Answer a question from the wiki.")
    _add_strict_evidence_arg(query)
    query.add_argument("question", help="The question to answer.")

    lint = sub.add_parser("lint", help="Health-check the wiki.")
    _add_strict_evidence_arg(lint)

    chat = sub.add_parser("chat", help="Converse with the wiki (model stays loaded).")
    _add_strict_evidence_arg(chat)
    chat.add_argument(
        "--resume",
        nargs="?",
        const="latest",
        default=None,
        metavar="SESSION_ID",
        help="Continue a conversation (default: the most recent one).",
    )
    return parser


def _add_strict_evidence_arg(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        "--strict-evidence",
        choices=VALID_STRICT_EVIDENCE_MODES,
        help="Citation evidence validation: off, warn, or fail "
        "(default: LLMWIKI_STRICT_EVIDENCE or off).",
    )


def _pdf_extractor(paths: WikiPaths) -> ExtractFn:
    def extract(pdf_path: Path, source_rel: str, reextract: bool) -> ExtractionResult:
        return ensure_extracted(
            pdf_path,
            source_rel,
            cache_root=paths.cache_dir,
            recognizer=AppleVisionRecognizer(),
            reextract=reextract,
        )

    return extract


async def _run(args: argparse.Namespace) -> OperationResult:
    paths = WikiPaths(root=args.root.resolve())
    paths.validate()
    backend_config = load_backend_config(args.runtime)
    strict_evidence = resolve_strict_evidence_mode(args.strict_evidence)

    now = datetime.now()
    backend = await start_backend(backend_config)
    try:
        print(f"[runtime: {backend.summary}]", file=sys.stderr)
        print(f"[strict-evidence: {strict_evidence}]", file=sys.stderr)
        session = Session(
            store=WikiStore(paths),
            client=backend.client,
            context_manager=backend.context_manager,
            today=now.date().isoformat(),
            runs_dir=paths.runs_dir,
            run_id=now.strftime("%Y-%m-%d-%H%M%S"),
            extract_pdf=_pdf_extractor(paths),
            on_chunk_note=lambda note: print(note, flush=True),
            strict_evidence=strict_evidence,
        )
        if args.op == "ingest":
            return await session.ingest(
                args.source, reextract=args.reextract, reintegrate=args.reintegrate
            )
        if args.op == "query":
            return await session.query(args.question)
        if args.op == "chat":
            return await _run_chat(session, paths, args.resume)
        return await session.lint()
    finally:
        await backend.aclose()


async def _run_chat(session: Session, paths: WikiPaths, resume: str | None) -> OperationResult:
    """The thin input loop; all REPL logic lives in ChatRepl (testable)."""
    chat_store = ChatStore(paths.root / "harness" / "chat.db")
    repl = ChatRepl(session=session, chat_store=chat_store)
    try:
        repl.start(resume)
        while True:
            try:
                line = await asyncio.to_thread(input, "llmwiki> ")
            except EOFError:  # Ctrl-D
                break
            if not await repl.handle(line):
                break
    except KeyboardInterrupt:  # Ctrl-C: same graceful path as /exit
        pass
    finally:
        repl.finish()
        chat_store.close()
    summary = (
        f"chat ended: {repl.turns} turns across {len(repl.conversations_touched)} conversation(s)"
    )
    return OperationResult("chat", "conversation", summary, None)


def main() -> None:
    args = _build_parser().parse_args()
    try:
        result = asyncio.run(_run(args))
    except (ConfigError, PdfError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        raise SystemExit(2) from exc
    print(result.output)
    if result.transcript_path is not None:
        print(f"\n[transcript: {result.transcript_path}]", file=sys.stderr)


if __name__ == "__main__":
    main()
