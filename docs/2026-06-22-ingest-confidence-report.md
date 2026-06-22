# Ingest Confidence Report

## Context & Problem

Glossary:

| Term | Meaning |
|---|---|
| `IngestConfidenceReport` | Harness-owned report that summarizes post-ingest validation. |
| `IngestConfidenceGate` | One validation check inside an `IngestConfidenceReport`. |
| `ValidationFinding` | Structured finding emitted by one confidence gate. |
| `FindingSeverity` | Severity label for one `ValidationFinding`. |
| `FindingCategory` | Category label for one `ValidationFinding`. |
| `ArtifactReuseDecision` | Decision to reuse or rebuild generated ingest artifacts. |
| `EvidenceRegistry` | Rebuildable collection of source evidence records. |
| `ClaimSupportAuditReport` | Harness-owned report for one claim support audit. |
| `SourceSummaryQualityReport` | Deterministic report for source-summary selection and generated pages. |
| `GeneratedWikiState` | `wiki/`, `index.md`, `log.md`, and disposable ingest cache. |

Current audits each answer one narrow question.
They do not produce one post-ingest confidence report for a source.
The backup had ingest verification and synthesis checks with structured failures.
This TDD adds a current-domain acceptance report for test ingests and curator review.

## Goals

- Add `IngestConfidenceReport` as the post-ingest validation summary.
- Add structured `ValidationFinding` records with stable categories.
- Reuse valid generated artifacts to save test time.
- Rebuild stale artifacts when the source or contract changed.
- Run deterministic gates before model-assisted gates.
- Test with Antikythera first, then JavaScript Allonge.
- File the report into the wiki and log.

## Non-Goals & Forbidden Approaches

Non-goals:

- This TDD does not auto-repair content pages.
- This TDD does not require Sword World reingest.
- This TDD does not replace `lint`, `grounding`, `semantic-lint`, or `claim-support`.
- This TDD does not add a web UI.
- This TDD does not preserve obsolete cache shapes.

Forbidden approaches:

- Do not treat a passing report as proof that the whole wiki is correct.
- Do not reuse artifacts when the artifact fingerprint differs.
- Do not hide model-assisted findings inside deterministic gates.
- Do not import backup scripts into active code.
- Do not adapt code to obsolete generated cache data.

## Requirements

- The report command must accept one raw source path.
- The report command must read the latest matching `PagePlan` cache when it is valid.
- `ArtifactReuseDecision` must record `reuse`, `rebuild`, or `missing`.
- `ArtifactReuseDecision` must compare source hash, schema id, page body contracts, and ingest profile.
- A stale artifact must trigger rebuild before the gate consumes it.
- The report must run deterministic gates before model-assisted gates.
- Deterministic gates must include graph, index, citation syntax, evidence registry, source range, and source summary quality.
- Model-assisted gates must include claim support when evidence excerpts exist.
- The report must keep skipped gates visible.
- `ValidationFinding` must include severity, category, source path, page id, and message.
- The report must write `wiki-ingest-confidence`.
- The report must append one `log.md` entry.
- Curator status must summarize the latest report.

## Invariants

- `raw/` remains immutable.
- `GeneratedWikiState` remains disposable.
- Ingest remains the operation that creates or updates wiki pages.
- Confidence reports are audit pages, not source evidence.
- Deterministic gates must not call the model.
- Model-assisted gates must state their bounded scope.

## Proposed Architecture

```
+------------+     +-----------------------+     +------------------+
| raw source |---->| ArtifactReuseDecision |---->| confidence gates |
+------------+     +-----------+-----------+     +--------+---------+
                                 |                          |
                                 v                          v
                         +---------------+         +----------------+
                         | ingest/cache  |-------->| Validation     |
                         | artifacts     |         | Finding        |
                         +---------------+         +--------+-------+
                                                            |
                                                            v
                                                   +----------------+
                                                   | IngestConfidence|
                                                   | Report         |
                                                   +----------------+
```

`ArtifactReuseDecision` protects test time and cache correctness.
Confidence gates convert existing audits into report sections.
`ValidationFinding` gives every issue a stable category and severity.
`IngestConfidenceReport` files the final source-level result.

## Key Interactions

Artifact reuse:

```
raw source -> artifact fingerprint
cache artifact -> artifact fingerprint
matching artifact -> reuse
stale artifact -> rebuild
```

Deterministic gates:

```
PagePlan cache -> source summary quality
EvidenceRegistry -> evidence gate
wiki pages -> graph and index gates
```

Model-assisted gate:

```
EvidenceRegistry -> claim support candidates
claim support workflow -> ClaimSupportAuditReport
ClaimSupportAuditReport -> IngestConfidenceReport
```

Report filing:

```
IngestConfidenceReport -> wiki-ingest-confidence
IngestConfidenceReport -> log.md
IngestConfidenceReport -> curator status
```

## Data Model

| Object | Required fields |
|---|---|
| `IngestConfidenceReport` | `run_id`, `source_locator`, `artifact_decisions`, `gates`, `findings`, `summary` |
| `IngestConfidenceGate` | `gate_id`, `gate_kind`, `scope`, `status`, `finding_ids` |
| `ValidationFinding` | `finding_id`, `severity`, `category`, `source_locator`, `page_id`, `message`, `fingerprint` |
| `ArtifactReuseDecision` | `artifact_kind`, `artifact_path`, `decision`, `reason`, `fingerprint` |

`FindingSeverity` values are `blocker`, `warning`, and `info`.
`FindingCategory` values are `planning`, `source-summary`, `citation`, `evidence`, `source-range`, `claim-support`, `graph`, `index`, and `runtime`.
`gate_kind` values are `deterministic` and `model-assisted`.
`status` values are `pass`, `fail`, and `skipped`.
`decision` values are `reuse`, `rebuild`, and `missing`.

## APIs / Interfaces

- New CLI command: `llmwiki ingest-confidence raw/<path>`.
- Option: `--fresh`, which rebuilds generated artifacts for the source.
- Option: `--max-claims N`, which bounds claim-support model work.
- Report page: `wiki-ingest-confidence`.
- Curator status reads the latest `IngestConfidenceReport` summary.
- The report command can call existing `lint`, evidence, source-summary quality, and claim-support domain services.

## Behavior & Domain Rules

Rule: artifact reuse requires a matching fingerprint.

Example: input cache has matching source hash and schema id.
Expected outcome: `ArtifactReuseDecision.decision` is `reuse`.

Example: input cache has a different source hash.
Expected outcome: `ArtifactReuseDecision.decision` is `rebuild`.

Rule: deterministic gates run first.

Example: input evidence registry has fatal source-range findings.
Expected outcome: claim support gate is `skipped`.

Example: input deterministic gates pass and evidence excerpts exist.
Expected outcome: claim support gate runs with `--max-claims`.

Rule: report status reflects findings.

Example: input has one blocker.
Expected outcome: report summary says confidence failed for the source.

Ugliest edge case: input has no claim-support candidates after deterministic gates pass.
Expected outcome: claim support gate is `skipped` with an info finding.

## Acceptance Criteria

Milestone 1: domain and report tests.

- `docs/domain-vocabulary.md` records `IngestConfidenceReport`, `IngestConfidenceGate`, `ValidationFinding`, and `ArtifactReuseDecision`.
- Tests cover `IngestConfidenceReport`, `IngestConfidenceGate`, `ValidationFinding`, and `ArtifactReuseDecision`.
- Tests prove matching fingerprints reuse artifacts.
- Tests prove stale fingerprints rebuild artifacts.
- Tests prove deterministic gate blockers skip model-assisted gates.
- Tests prove report rendering includes skipped gates.
- Tests prove curator status summarizes the latest report.

Milestone 2: Antikythera implementation gate.

- Run `uv run llmwiki ingest-confidence raw/antikythera-mechanism.md`.
- The command reuses valid Antikythera artifacts when fingerprints match.
- The command rebuilds stale Antikythera artifacts when fingerprints differ.
- The report includes source-summary quality, evidence, graph, index, and claim-support sections.
- The implementation fixes each Antikythera blocker and reruns the command.

Milestone 3: JavaScript Allonge scale gate.

- Run `uv run llmwiki ingest-confidence raw/javascriptallonge.pdf`.
- The command reuses valid PDF extraction artifacts when fingerprints match.
- The command rebuilds stale JavaScript Allonge artifacts when fingerprints differ.
- The report completes with bounded claim-support work.
- The implementation fixes each JavaScript Allonge blocker and reruns the command.

Milestone 4: standard verification.

- `uv run pytest harness/tests/test_ingest_confidence_report.py harness/tests/test_maintenance.py` passes.
- `uv run pytest harness/tests/test_claim_support_audit.py harness/tests/test_source_summary_coverage.py` passes.
- `uv run ruff check harness/src harness/tests` passes.
- `uv run mypy harness/src` passes.
- No active code imports backup paths.

## Cross-Cutting Concerns

Observability: each report section must state scope, artifact reuse, skipped gates, and finding counts.

Error handling: rebuild failures must produce `runtime` blocker findings.

Cost control: the report must run deterministic gates before model-assisted gates.

## Reference Implementations

- Current curator status: `harness/src/llmwiki/domain/maintenance.py`.
- Current lint session flow: `harness/src/llmwiki/runtime/session.py`.
- Current source summary quality: `harness/src/llmwiki/domain/source_summary_quality.py`.
- Current graph export: `harness/src/llmwiki/domain/graph.py`.
- Backup failure classifier idea: `backup/reference/llm-wiki-pre-m5-migration-2026-06-14/tools/wiki_failure_classifier.py`.
- Backup ingest verifier idea: `backup/reference/llm-wiki-pre-m5-migration-2026-06-14/tools/wiki_verify_ingest.py`.
- Backup synthesis checker idea: `backup/reference/llm-wiki-pre-m5-migration-2026-06-14/tools/wiki_check_synthesis.py`.

## Alternatives Considered

- Chosen: one source-level confidence report, because curators need a test-ingest result.
- Rejected: full wiki proof, because bounded audits cannot prove every claim.
- Rejected: always fresh ingest, because valid artifacts save time during repeated fixes.
- Rejected: silent cache reuse, because stale artifacts hide schema changes.

## Halt Conditions

- If artifact fingerprints cannot be computed for a cache type, stop and add that artifact contract first.
- If claim support needs whole-source prompts, stop and reduce candidate scope.
- If the report requires migration of old cache shapes, stop and regenerate instead.
