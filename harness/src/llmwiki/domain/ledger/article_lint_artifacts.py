"""Source-scoped article lint artifact contracts."""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass, replace

from llmwiki.domain.ledger.article_lint_contracts import ArticleLintRun
from llmwiki.domain.ledger.canonical import artifact_fingerprint, deterministic_id
from llmwiki.domain.ledger.vocab import ARTIFACT_FORMAT


@dataclass(frozen=True)
class ArticleLintArtifact:
    article_lint_artifact_id: str
    article_lint_fingerprint: str
    artifact_format: str
    runs: tuple[ArticleLintRun, ...]

    @property
    def accepted_count(self) -> int:
        return sum(1 for run in self.runs if run.publication_gate.decision == "accepted")

    @property
    def blocked_count(self) -> int:
        return sum(1 for run in self.runs if run.publication_gate.decision == "blocked")

    @property
    def top_blocking_codes(self) -> tuple[tuple[str, int], ...]:
        counter: Counter[str] = Counter()
        for run in self.runs:
            if run.publication_gate.decision != "blocked":
                continue
            counter.update(
                finding.finding_code
                for finding in run.findings
                if finding.severity == "blocking"
            )
        return tuple(counter.most_common(5))


def build_article_lint_artifact(
    *, source_hash: str, runs: tuple[ArticleLintRun, ...]
) -> ArticleLintArtifact:
    draft = ArticleLintArtifact(
        article_lint_artifact_id=deterministic_id("article-lint", source_hash),
        article_lint_fingerprint="",
        artifact_format=ARTIFACT_FORMAT,
        runs=runs,
    )
    fingerprint = artifact_fingerprint(
        draft, exclude=("article_lint_artifact_id", "article_lint_fingerprint")
    )
    return replace(
        draft,
        article_lint_artifact_id=deterministic_id("article-lint", source_hash, fingerprint),
        article_lint_fingerprint=fingerprint,
    )
