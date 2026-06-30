"""Deterministic evidence packs for task-shaped chat turns."""

from __future__ import annotations

import re
from collections.abc import Iterable, Mapping, Sequence
from dataclasses import dataclass

from llmwiki.domain.chat_grounding import ChatTaskMode
from llmwiki.domain.links import extract_links
from llmwiki.domain.pages import PageError, parse_page
from llmwiki.domain.search import SearchHit
from llmwiki.domain.structured_evidence import (
    StructuredEvidenceArtifact,
    select_structured_evidence_artifacts,
)

_STEP_RE = re.compile(
    r"^\s*(?P<sequence>\d+)\.\s+\*\*(?P<title>[^*]+)\*\*.*?\[\[(?P<page_id>[a-z0-9-]+)\]\]",
    re.MULTILINE,
)
_MAX_PROCEDURE_CHARS = 5_000
_MAX_PAGE_CHARS = 350
_MAX_TOTAL_CHARS = 8_000


@dataclass(frozen=True)
class ProcedureStepRequirement:
    sequence: int
    title: str
    evidence_page_id: str


@dataclass(frozen=True)
class TaskEvidencePage:
    page_id: str
    page_kind: str
    page_family: str
    summary: str
    excerpt: str


@dataclass(frozen=True)
class TaskEvidencePack:
    """Bounded, deterministic evidence selected before a task is executed."""

    procedure_id: str
    procedure_title: str
    steps: tuple[ProcedureStepRequirement, ...]
    pages: tuple[TaskEvidencePage, ...]
    structured_artifacts: tuple[StructuredEvidenceArtifact, ...] = ()

    @property
    def page_ids(self) -> frozenset[str]:
        return frozenset(page.page_id for page in self.pages) | frozenset(
            artifact.page_id for artifact in self.structured_artifacts
        )

    @property
    def evidence_texts(self) -> dict[str, str]:
        texts = {page.page_id: page.excerpt for page in self.pages}
        for artifact in self.structured_artifacts:
            existing = texts.get(artifact.page_id, "")
            texts[artifact.page_id] = f"{existing}\n\n{artifact.excerpt}".strip()
        return texts

    def render(self, *, require_procedure_execution: bool = True) -> str:
        lines = [
            "Deterministic task evidence pack:",
            f"- Procedure: [[{self.procedure_id}]] {self.procedure_title}",
            "- Required procedure steps:",
        ]
        for step in self.steps:
            lines.append(f"  {step.sequence}. {step.title} - evidence [[{step.evidence_page_id}]]")
        lines.append("")
        if require_procedure_execution:
            lines.extend(
                (
                    "ProcedureExecution submission checklist:",
                    "- Call submit_procedure_execution before respond.",
                    f"- procedure_id must be {self.procedure_id}.",
                    "- step_results must include every sequence/title listed above.",
                    "- For each output, set support to evidence, derived, "
                    "assumption, or unresolved.",
                    "- For broad steps, a status=partial step_result with a concise "
                    "note is acceptable when many nested outputs would be too large.",
                    "- Put user-independent choices in assumptions; mark missing rule "
                    "details unresolved.",
                    "",
                )
            )
        else:
            lines.extend(
                (
                    "Procedure explanation checklist:",
                    "- Walk through every required step listed above.",
                    "- Name relevant table, formula, and worked-example artifacts "
                    "using their exact source titles.",
                    "- Treat the table-index artifact as the authoritative list "
                    "of table titles; do not replace those titles with generic names.",
                    "- Say plainly when a detail is a free choice or unresolved.",
                    "",
                )
            )
        if self.structured_artifacts:
            lines.append("Deterministic structured evidence artifacts:")
            for artifact in self.structured_artifacts:
                lines.extend(
                    (
                        f"### [[{artifact.page_id}]] {artifact.category}: {artifact.heading}",
                        artifact.excerpt.strip(),
                        "",
                    )
                )
        lines.append("Evidence pages:")
        for page in self.pages:
            family = f"/{page.page_family}" if page.page_family else ""
            lines.extend(
                (
                    f"### [[{page.page_id}]] ({page.page_kind}{family})",
                    page.summary,
                    "",
                    page.excerpt.strip(),
                    "",
                )
            )
        if require_procedure_execution:
            lines.extend(
                (
                    "ProcedureExecution tool reminder:",
                    "- For an execution request, the next tool call must be "
                    "submit_procedure_execution, not respond.",
                    "- Include every required step result. Use unresolved outputs for "
                    "missing details instead of answering directly.",
                )
            )
        else:
            lines.extend(
                (
                    "Procedure explanation reminder:",
                    "- Answer by explaining the required steps and the structured "
                    "table/formula/example evidence above, preserving exact table titles.",
                    "- Include exact table titles from the table-index artifact "
                    "whenever you summarize tables and formulas.",
                    "- Do not answer with a meta-summary that the steps were provided.",
                )
            )
        return "\n".join(lines).strip()


def build_task_evidence_pack(
    pages: Mapping[str, str],
    hits: Sequence[SearchHit],
    *,
    task_mode: ChatTaskMode,
) -> TaskEvidencePack | None:
    """Build a task evidence pack from search hits and procedure-page links."""

    if task_mode not in {
        ChatTaskMode.EXPLAIN_PROCEDURE,
        ChatTaskMode.EXECUTE_PROCEDURE,
        ChatTaskMode.SOURCE_AUDIT,
    }:
        return None
    procedure_id = _best_procedure_page(pages, hits)
    if procedure_id is None:
        return None
    procedure_text = pages[procedure_id]
    procedure_page = parse_page(procedure_text)
    steps = _procedure_steps(procedure_page.page_body)
    if not steps:
        return None
    page_ids = _candidate_page_ids(procedure_id, procedure_page.page_body, steps, hits, pages)
    structured_artifacts = select_structured_evidence_artifacts(
        pages,
        page_ids,
        (procedure_page.page_body, *(step.title for step in steps)),
    )
    evidence_pages = _pack_pages(pages, page_ids)
    if not evidence_pages:
        return None
    return TaskEvidencePack(
        procedure_id=procedure_id,
        procedure_title=_title(procedure_page.page_body) or procedure_page.summary,
        steps=steps,
        pages=evidence_pages,
        structured_artifacts=structured_artifacts,
    )


def _best_procedure_page(pages: Mapping[str, str], hits: Sequence[SearchHit]) -> str | None:
    for hit in hits:
        text = pages.get(hit.name)
        if text is None:
            continue
        try:
            page = parse_page(text)
        except PageError:
            continue
        metadata = page.page_metadata
        if metadata.page_kind == "procedure" or metadata.page_family == "procedure-guide":
            return metadata.page_id
    return None


def _procedure_steps(body: str) -> tuple[ProcedureStepRequirement, ...]:
    steps: list[ProcedureStepRequirement] = []
    for match in _STEP_RE.finditer(body):
        steps.append(
            ProcedureStepRequirement(
                sequence=int(match.group("sequence")),
                title=" ".join(match.group("title").split()),
                evidence_page_id=match.group("page_id"),
            )
        )
    return tuple(steps)


def _candidate_page_ids(
    procedure_id: str,
    procedure_body: str,
    steps: tuple[ProcedureStepRequirement, ...],
    hits: Sequence[SearchHit],
    pages: Mapping[str, str],
) -> tuple[str, ...]:
    ordered: list[str] = [procedure_id]
    ordered.extend(step.evidence_page_id for step in steps)
    ordered.extend(_prioritized_page_links(extract_links(procedure_body), pages))
    ordered.extend(hit.name for hit in hits)
    return tuple(dict.fromkeys(page_id for page_id in ordered if page_id in pages))


def _prioritized_page_links(page_ids: Iterable[str], pages: Mapping[str, str]) -> tuple[str, ...]:
    existing = tuple(dict.fromkeys(page_id for page_id in page_ids if page_id in pages))
    return tuple(sorted(existing, key=lambda page_id: _page_link_priority(page_id, pages)))


def _page_link_priority(page_id: str, pages: Mapping[str, str]) -> tuple[int, str]:
    try:
        page = parse_page(pages[page_id])
    except PageError:
        return (2, page_id)
    if page.page_metadata.page_family == "source-manifest":
        return (2, page_id)
    if page.page_kind == "source":
        return (0, page_id)
    return (1, page_id)


def _pack_pages(
    pages: Mapping[str, str], page_ids: tuple[str, ...]
) -> tuple[TaskEvidencePage, ...]:
    packed: list[TaskEvidencePage] = []
    total = 0
    for page_id in page_ids:
        text = pages[page_id]
        try:
            page = parse_page(text)
        except PageError:
            continue
        if page_id != page_ids[0] and page.page_metadata.page_family == "source-manifest":
            continue
        cap = _MAX_PROCEDURE_CHARS if page_id == page_ids[0] else _MAX_PAGE_CHARS
        remaining = _MAX_TOTAL_CHARS - total
        if remaining <= 0:
            break
        excerpt = _clip(page.page_body, min(cap, remaining))
        total += len(excerpt)
        packed.append(
            TaskEvidencePage(
                page_id=page.page_id,
                page_kind=page.page_kind,
                page_family=page.page_metadata.page_family,
                summary=page.summary,
                excerpt=excerpt,
            )
        )
    return tuple(packed)


def _clip(text: str, max_chars: int) -> str:
    if len(text) <= max_chars:
        return text
    clipped = text[:max_chars].rstrip()
    return f"{clipped}\n\n[TRUNCATED: task evidence pack excerpt]"


def _title(body: str) -> str:
    for line in body.splitlines():
        if line.startswith("# "):
            return line.removeprefix("# ").strip()
    return ""
