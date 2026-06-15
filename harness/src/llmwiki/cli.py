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

from forge.context import ContextManager, NoCompact

from llmwiki.config import (
    VALID_STRICT_EVIDENCE_MODES,
    ConfigError,
    StrictEvidenceMode,
    WikiPaths,
    load_backend_config,
    resolve_strict_evidence_mode,
)
from llmwiki.domain.contradictions import DEFAULT_MAX_PAIRS, select_contradiction_candidates
from llmwiki.domain.evidence import EvidencePolicy
from llmwiki.domain.index import index_page_names
from llmwiki.domain.maintenance import build_curator_status, recent_log_entries
from llmwiki.domain.pages import WikiPage
from llmwiki.domain.salience import compute_salience
from llmwiki.domain.system_pages import CURATOR_STATUS_PAGE
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

    curator_status = sub.add_parser(
        "curator-status",
        help="Print deterministic wiki maintenance status without starting a model.",
    )
    _add_strict_evidence_arg(curator_status)

    maintenance = sub.add_parser(
        "maintenance",
        help="File deterministic curator status and append a maintenance log entry.",
    )
    _add_strict_evidence_arg(maintenance)

    contradictions = sub.add_parser(
        "contradictions",
        help="Audit bounded candidate page pairs for semantic contradictions.",
    )
    contradictions.add_argument(
        "--max-pairs",
        type=int,
        default=DEFAULT_MAX_PAIRS,
        help=f"Maximum candidate pairs to audit (default: {DEFAULT_MAX_PAIRS}).",
    )

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
    strict_evidence = resolve_strict_evidence_mode(getattr(args, "strict_evidence", None))

    now = datetime.now()
    if args.op in {"curator-status", "maintenance"}:
        paths.validate_status()
        return _run_curator_operation(args.op, paths, strict_evidence, now.date().isoformat())

    if args.op == "contradictions":
        return await _run_contradictions(args, paths, now)

    paths.validate()
    backend_config = load_backend_config(args.runtime)
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


async def _run_contradictions(
    args: argparse.Namespace, paths: WikiPaths, now: datetime
) -> OperationResult:
    if args.max_pairs < 1:
        raise ConfigError("--max-pairs must be at least 1.")
    paths.validate()
    store = WikiStore(paths)
    selection = select_contradiction_candidates(store.page_texts(), max_pairs=args.max_pairs)
    if not selection.candidates:
        session = Session(
            store=store,
            client=None,
            context_manager=ContextManager(strategy=NoCompact(), budget_tokens=1),
            today=now.date().isoformat(),
        )
        return await session.contradictions(selection)

    backend_config = load_backend_config(args.runtime)
    backend = await start_backend(backend_config)
    try:
        print(f"[runtime: {backend.summary}]", file=sys.stderr)
        session = Session(
            store=store,
            client=backend.client,
            context_manager=backend.context_manager,
            today=now.date().isoformat(),
            runs_dir=paths.runs_dir,
            run_id=now.strftime("%Y-%m-%d-%H%M%S"),
        )
        return await session.contradictions(selection)
    finally:
        await backend.aclose()


def _run_curator_operation(
    op: str, paths: WikiPaths, strict_evidence: StrictEvidenceMode, today: str
) -> OperationResult:
    store = WikiStore(paths)
    report = _curator_report(store, paths, strict_evidence)
    if op == "maintenance":
        store.ensure_navigation_files()
        store.write_page(
            WikiPage(
                name=CURATOR_STATUS_PAGE,
                category="synthesis",
                summary=f"Deterministic curator status from {today}.",
                body=report,
                updated=today,
            )
        )
        store.append_log(today, "maintenance", "curator status", report)
    return OperationResult(op, "curator status", report, None)


def _curator_report(store: WikiStore, paths: WikiPaths, strict_evidence: StrictEvidenceMode) -> str:
    page_texts = store.page_texts()
    index_exists = paths.index_path.is_file()
    log_exists = paths.log_path.is_file()
    index_text = paths.index_path.read_text(encoding="utf-8") if index_exists else ""
    log_text = paths.log_path.read_text(encoding="utf-8") if log_exists else ""
    evidence_policy = EvidencePolicy(mode=strict_evidence)
    inventory = store.source_inventory() if evidence_policy.enabled else None
    status = build_curator_status(
        page_texts=page_texts,
        index_names=index_page_names(index_text),
        raw_source_count=len(store.list_sources()),
        index_exists=index_exists,
        log_exists=log_exists,
        recent_log_entries=recent_log_entries(log_text),
        evidence_report=evidence_policy.lint_pages(page_texts, inventory),
        salience_report=compute_salience(page_texts),
        strict_evidence=strict_evidence,
    )
    return status.render()


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
