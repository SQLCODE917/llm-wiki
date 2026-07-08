"""Artifact serialization for the single ingest compiler."""

from __future__ import annotations

from collections import Counter

from llmwiki.domain.ingest_compiler import (
    CompilerFinding,
    CompilerStage,
    IngestArtifactMember,
    IngestArtifactSet,
    build_ingest_artifact_set,
)
from llmwiki.domain.ledger.canonical import canonical_json, deterministic_id, short_digest
from llmwiki.domain.source_map import NormalizedSourceMap, normalized_source_map_to_json


def compiler_artifact_files(
    *,
    source_locator: str,
    source_page_id: str,
    source_hash: str,
    run_id: str,
    source_map: NormalizedSourceMap,
    payloads: dict[str, str],
    findings: tuple[CompilerFinding, ...],
    accepted_page_ids: tuple[str, ...],
    rejected_page_ids: tuple[str, ...],
) -> tuple[dict[str, str], IngestArtifactSet]:
    files = {"normalized-source-map.json": normalized_source_map_to_json(source_map), **payloads}
    members = tuple(_member(kind, name, text) for kind, name, text in _member_inputs(files))
    artifact_set = build_ingest_artifact_set(
        source_id=source_page_id,
        source_locator=source_locator,
        source_hash=source_hash,
        run_id=run_id,
        stages=_stages(members, findings),
        artifacts=members,
        findings=findings,
        accepted_page_ids=accepted_page_ids,
        rejected_page_ids=rejected_page_ids,
    )
    files["ingest-artifact-set.json"] = canonical_json(artifact_set, indent=2)
    return files, artifact_set


def _member_inputs(files: dict[str, str]) -> tuple[tuple[str, str, str], ...]:
    return tuple(
        (name.removesuffix(".json").removesuffix(".md"), name, text)
        for name, text in files.items()
    )


def _member(kind: str, path: str, text: str) -> IngestArtifactMember:
    fingerprint = short_digest(text, 32)
    return IngestArtifactMember(
        artifact_kind=kind,
        artifact_id=deterministic_id(kind, fingerprint),
        artifact_path=path,
        fingerprint=fingerprint,
    )


def _stages(
    members: tuple[IngestArtifactMember, ...], findings: tuple[CompilerFinding, ...]
) -> tuple[CompilerStage, ...]:
    member_by_kind = {member.artifact_kind: member.artifact_id for member in members}
    counts = Counter(finding.stage_name for finding in findings)
    return tuple(
        _stage(
            name,
            tuple(member_by_kind[kind] for kind in inputs if kind in member_by_kind),
            tuple(member_by_kind[kind] for kind in outputs if kind in member_by_kind),
            counts[name],
        )
        for name, inputs, outputs in _STAGE_ORDER
    )


def _stage(
    name: str,
    inputs: tuple[str, ...],
    outputs: tuple[str, ...],
    finding_count: int,
) -> CompilerStage:
    return CompilerStage(name, inputs, outputs, "completed", 0, finding_count)


_STAGE_ORDER = (
    ("source-map", (), ("normalized-source-map",)),
    (
        "source-structure",
        ("normalized-source-map",),
        ("source-structure-integrity", "source-record-plan"),
    ),
    ("source-profile", ("normalized-source-map",), ("source-profile", "evidence-extraction-plan")),
    ("evidence-records", ("evidence-extraction-plan",), ("evidence-record-set",)),
    (
        "page-plan",
        ("source-structure-integrity", "source-record-plan", "evidence-record-set"),
        ("candidate-admission-report", "article-viability-report", "page-publication-plan"),
    ),
    ("evidence-packs", ("page-publication-plan",), ("evidence-pack-set",)),
    ("article-write-queue", ("evidence-pack-set",), ("article-write-queue-run",)),
    (
        "human-articles",
        ("article-write-queue-run",),
        ("human-article-initial", "human-article-findings-initial"),
    ),
    ("article-lint", ("human-article-initial",), ("article-lint-runs-initial",)),
    (
        "diagnostics",
        ("evidence-pack-set", "article-lint-runs-initial"),
        (
            "diagnostic-question-set",
            "diagnostic-answer-set",
            "diagnostic-finding-set",
            "diagnostics-report",
        ),
    ),
    (
        "repair",
        ("diagnostic-finding-set",),
        (
            "repair-task-set",
            "repair-run",
            "human-article",
            "human-article-findings",
            "article-lint-runs",
        ),
    ),
    ("staged-publish", ("article-lint-runs",), ("staged-pages", "lint-run", "publish-run")),
)
