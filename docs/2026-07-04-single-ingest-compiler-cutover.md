# TDD: Single Ingest Compiler Cutover

## Context & Problem

The current ingest orchestrator mixes extraction, ledger work, page projection,
lint, and publication.
The new source map pipeline must replace that flow.
The repository must not maintain two ingestion flows.

Glossary:

- `IngestCompiler`: the only orchestrator for source ingest.
- `IngestArtifactSet`: the ordered artifacts from one ingest run.
- `CompilerStage`: one named stage in the ingest compiler.
- `CompilerFinding`: one blocking or warning issue from a compiler stage.
- `NormalizedSourceMap`: the durable source model for one `RawSource`.
- `SourceProfile`: the source purpose and evidence vocabulary for one source.
- `EvidenceRecordSet`: all typed evidence records for one source.
- `PagePlan`: the accepted public page plan for one source.
- `EvidencePack`: the selected source support for one planned page.
- `HumanArticle`: structured article content for one public wiki page.
- `ArticleLintRun`: one lint run for generated public articles.
- `DiagnosticQuestionSet`: all diagnostic questions for one ingest run.

## Goals

- Replace the old ledger projection flow with one ingest compiler.
- Run compiler stages in the new source-to-article order.
- Delete or demote public outputs from old section and claim projection.
- Publish only pages accepted by article lint.
- Improve authority by making every public article traceable to source blocks.

## Non-Goals & Forbidden Approaches

Non-goals:

- This design does not preserve old artifact compatibility.
- This design does not add a runtime flag for the old flow.
- This design does not migrate existing generated wiki pages.
- This design does not implement new model providers.

Forbidden approaches:

- Do not add `legacy`, `v1`, `v2`, or dual-ingest flags.
- Do not run the old chunk-to-claim-to-page flow beside the compiler.
- Do not read old generated artifacts as required input.
- Do not publish section reference pages outside the page plan.

## Requirements

- `uv run llmwiki ingest <file>` calls `IngestCompiler`.
- `IngestCompiler` runs source map, source profile, evidence records, page plan,
  evidence pack, human article, article lint, diagnostics, and publication.
- `IngestCompiler` writes one `IngestArtifactSet`.
- The compiler stops publication when article lint blocks a page.
- The compiler writes index and log updates through harness-owned paths.
- The compiler records compiler findings for rejected pages.
- The old public projection path is removed or made unreachable.
- Tests prove one ingest entry point exists for source ingest.

## Invariants

- Raw sources stay immutable.
- The wiki layer remains generated state.
- `index.md` and `log.md` stay harness-owned.
- Generated artifacts remain disposable.
- Runtime profile selection remains separate from wiki schema behavior.

## Proposed Architecture

```text
CLI ingest
    |
    v
IngestCompiler
    |
    +--> NormalizedSourceMap
    +--> SourceProfile
    +--> EvidenceRecordSet
    +--> PagePlan
    +--> EvidencePack
    +--> HumanArticle
    +--> ArticleLintRun
    +--> DiagnosticQuestionSet
    v
Publisher
```

`CLI ingest` receives the source path.
`IngestCompiler` runs the ordered compiler stages.
`IngestArtifactSet` stores durable ingest artifacts.
`Publisher` writes accepted wiki pages, index, and log.

## Key Interactions

Run ingest:

```text
cli -> session: ingest source
session -> ingest compiler: compile source
ingest compiler -> artifact set: write stages
publisher -> wiki: write accepted pages
```

Reject page:

```text
article linter -> lint run: write blocking finding
publication gate -> ingest compiler: reject page
ingest compiler -> artifact set: record compiler finding
publisher -> wiki: omit rejected page
```

Update navigation:

```text
publisher -> page plan: read accepted pages
publisher -> index: write entries
publisher -> log: append ingest entry
```

## Data Model

`IngestCompiler` stores no durable state.
It arranges compiler stages and writes artifacts through stores.

`IngestArtifactSet` stores source id, run id, artifact paths, compiler findings,
accepted page ids, and rejected page ids.

`CompilerStage` stores stage name, input artifact ids, output artifact ids, and
status.

`CompilerFinding` stores finding id, stage name, severity, page id, source
anchor, and message.

## APIs / Interfaces

The session ingest path calls `IngestCompiler`.

The publisher accepts only page outputs with accepted publication gates.

The CLI exposes no compatibility flag for the old ingest path.

## Behavior & Domain Rules

The compiler runs stages in order.
Example: it builds evidence packs only after it writes a page plan.

The compiler rejects blocked pages.
Example: a Shade article with clipped prose does not publish.

The compiler publishes accepted pages.
Example: a JavaScript Allonge recipe page publishes after article lint accepts
it.

The compiler records rejected pages.
Example: a rejected candidate appears in the ingest artifact set and log entry.

## Acceptance Criteria

- A unit test proves `Session.ingest` calls `IngestCompiler`.
- A unit test proves the CLI exposes no legacy ingest flag.
- A unit test proves old chunk records are not required inputs.
- An integration test runs the compiler with fake model boundaries.
- The integration test writes source map, source profile, evidence record, page
  plan, evidence pack, article, lint, and diagnostic artifacts.
- The integration test publishes only pages with accepted publication gates.
- The integration test does not publish section reference pages by default.
- A Sword World fake ingest omits the incoherent Shade page when lint fails.
- A JavaScript Allonge fake ingest publishes an accepted recipe page.
- `uv run pytest --cov=llmwiki` passes.
- `uv run ruff check` passes.
- `uv run mypy harness/src/llmwiki` passes.

## Cross-Cutting Concerns

The compiler records stage timing and finding counts.
The log records the compiler run id and accepted page count.

Runtime profiles continue to use Forge and Ollama through existing config.

## Reference Implementations

- Current ledger pipeline: `harness/src/llmwiki/runtime/ledger_pipeline.py`
- Runtime session: `harness/src/llmwiki/runtime/session.py`
- Staged flow: `harness/src/llmwiki/domain/ledger/staged_flow.py`

## Alternatives Considered

- Add a second ingest command: rejected because the repository is pre-release.
- Keep old projection for fallback pages: rejected because fallback pages caused
  incoherent wiki output.
- Migrate old artifacts: rejected because generated data is disposable.

## Halt Conditions

- Stop if a production ingest path still calls the old ledger projection flow.
- Stop if a required test depends on old generated wiki data.
