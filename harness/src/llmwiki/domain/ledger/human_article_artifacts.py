"""Portable artifacts for human article writing."""

from __future__ import annotations

from dataclasses import dataclass, replace

from llmwiki.domain.ledger.canonical import artifact_fingerprint, deterministic_id
from llmwiki.domain.ledger.human_article import ArticleFinding, HumanArticleRecord
from llmwiki.domain.ledger.vocab import ARTIFACT_FORMAT


@dataclass(frozen=True)
class HumanArticleArtifact:
    human_article_artifact_id: str
    human_article_fingerprint: str
    artifact_format: str
    records: tuple[HumanArticleRecord, ...]


@dataclass(frozen=True)
class HumanArticleFindingsArtifact:
    human_article_findings_artifact_id: str
    human_article_findings_fingerprint: str
    artifact_format: str
    findings: tuple[ArticleFinding, ...]


def build_human_article_artifact(
    *, source_hash: str, records: tuple[HumanArticleRecord, ...]
) -> HumanArticleArtifact:
    draft = HumanArticleArtifact(
        human_article_artifact_id=deterministic_id("human-article", source_hash),
        human_article_fingerprint="",
        artifact_format=ARTIFACT_FORMAT,
        records=records,
    )
    fingerprint = artifact_fingerprint(
        draft, exclude=("human_article_artifact_id", "human_article_fingerprint")
    )
    return replace(
        draft,
        human_article_artifact_id=deterministic_id("human-article", source_hash, fingerprint),
        human_article_fingerprint=fingerprint,
    )


def build_human_article_findings_artifact(
    *, source_hash: str, findings: tuple[ArticleFinding, ...]
) -> HumanArticleFindingsArtifact:
    draft = HumanArticleFindingsArtifact(
        human_article_findings_artifact_id=deterministic_id(
            "human-article-findings", source_hash
        ),
        human_article_findings_fingerprint="",
        artifact_format=ARTIFACT_FORMAT,
        findings=findings,
    )
    fingerprint = artifact_fingerprint(
        draft,
        exclude=(
            "human_article_findings_artifact_id",
            "human_article_findings_fingerprint",
        ),
    )
    return replace(
        draft,
        human_article_findings_artifact_id=deterministic_id(
            "human-article-findings", source_hash, fingerprint
        ),
        human_article_findings_fingerprint=fingerprint,
    )
