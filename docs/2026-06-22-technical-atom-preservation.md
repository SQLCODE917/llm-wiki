# Technical Atom Preservation

## Context & Problem

Glossary:

| Term | Meaning |
|---|---|
| `TechnicalAtom` | One preserved technical fact from a source. |
| `TechnicalAtomKind` | Category for one `TechnicalAtom`. |
| `TechnicalAtomBuilder` | Domain service that creates `TechnicalAtom` records. |
| `TechnicalAtomCatalog` | Rebuildable catalog of `TechnicalAtom` records for one source. |
| `TechnicalDetailsSection` | Source page section that renders `TechnicalAtom` records. |
| `SourcePageRenderer` | Domain service that renders one source `WikiPage`. |
| `AnswerEvaluationCase` | Test fixture that runs one regular `query` question. |
| `AnswerEvaluationReport` | Result of checking one regular query answer against required `TechnicalAtom` records. |
| `SourceClaim` | Atomic statement extracted from one `ExtractedUnit`. |
| `SourceText` | Line-addressable text derived from one raw source. |
| `EvidenceRecord` | Stable audit record for one source excerpt. |
| `EvidenceRegistry` | Rebuildable collection of source evidence records. |
| `SourceSummaryPlan` | Plan for one harness-rendered source summary page. |
| `ClaimSupportAuditReport` | Harness-owned report for one claim support audit. |
| `IngestConfidenceReport` | Harness-owned report that summarizes source validation. |
| `WikiPage` | One generated markdown page in `wiki/`. |
| `GeneratedWikiState` | `wiki/`, `index.md`, `log.md`, and disposable ingest cache. |

Source pages now summarize technical sources.
They do not preserve enough formulas, procedures, code, table rows, and exceptions.
This design adds preserved `TechnicalAtom` records to the generated wiki layer.
It keeps raw sources immutable and uses the wiki as a persistent compiled layer.

## Goals

- Preserve exact or structured technical details during ingest.
- Render preserved details on source pages.
- Support source-agnostic rules, code, formulas, tables, and procedures.
- Audit preserved details against `EvidenceRecord` records.
- Test normal query answers against required preserved details.
- Keep summary prose separate from preserved details.

## Non-Goals & Forbidden Approaches

Non-goals:

- This design does not add Sword World rules as hardcoded knowledge.
- This design does not add JavaScript Allonge code as hardcoded knowledge.
- This design does not replace source summary pages.
- This design does not require a new `PageKind`.
- This design does not add a second question mode.

Forbidden approaches:

- Do not use source-specific selectors or source-specific prompts.
- Do not treat summary bullets as preserved technical details.
- Do not store generated guesses as `TechnicalAtom` payloads.
- Do not render a `TechnicalAtom` without source citations.
- Do not use planning artifacts as source evidence.
- Do not write technical artifacts under `raw/`.

## Requirements

- The ingest confidence path must build a `TechnicalAtomCatalog` for one source.
- The `TechnicalAtomBuilder` must use `SourceClaim`, `EvidenceRecord`, and `SourceText` inputs.
- The `TechnicalAtomBuilder` must select candidates by structure and role tags.
- The `TechnicalAtomBuilder` must recognize code blocks, formulas, procedures, table rows, requirements, exceptions, and worked examples.
- The `TechnicalAtomBuilder` must not inspect the source file name to choose a candidate.
- Each `TechnicalAtom` must include one `TechnicalAtomKind`.
- Each `TechnicalAtom` must include a source locator.
- Each `TechnicalAtom` must include one page id.
- Each `TechnicalAtom` must include one or more evidence ids.
- Each `TechnicalAtom` must include a bounded technical payload.
- Each `TechnicalAtom` must include normalized fields when the kind has fields.
- The `SourcePageRenderer` must add a `TechnicalDetailsSection` to source pages that have atoms.
- The `SourcePageRenderer` must show the atom id, kind, payload, and citation.
- The claim support audit must include `TechnicalAtom` claims when atoms exist.
- The ingest confidence report must include atom counts by kind.
- The query workflow must read `TechnicalDetailsSection` as ordinary page content.
- The evaluation harness must run answer cases through normal `query` answers.

## Invariants

- `raw/` remains immutable.
- `GeneratedWikiState` remains disposable.
- `EvidenceRecord` remains the evidence source for preserved details.
- `TechnicalAtomCatalog` remains rebuildable from generated ingest artifacts.
- Source summaries remain useful for orientation.
- Preserved details remain separate from summary bullets.
- Every rendered `TechnicalAtom` remains citeable to a raw source.
- A passing evaluation case proves only that one question passed.

## Proposed Architecture

```
+-------------+      +------------------+      +-------------------+
| SourceClaim |----->| TechnicalAtom    |----->| TechnicalAtom     |
| Evidence    |      | Builder          |      | Catalog           |
+-------------+      +---------+--------+      +---------+---------+
                               |                         |
                               v                         v
                     +-------------------+      +-------------------+
                     | SourcePage        |      | claim support     |
                     | Renderer          |      | audit             |
                     +---------+---------+      +---------+---------+
                               |                         |
                               v                         v
                     +-------------------+      +-------------------+
                     | query workflow    |----->| Answer            |
                     |                   |      | Evaluation        |
                     +-------------------+      +-------------------+
```

The `TechnicalAtomBuilder` creates preserved details from source artifacts.
The `TechnicalAtomCatalog` stores rebuildable atom records.
The `SourcePageRenderer` writes atom records into source pages.
The claim support audit judges atom claims against evidence.
The query workflow reads source pages before it answers.
The `AnswerEvaluationReport` checks normal query answers against required atoms.

## Key Interactions

Atom build:

```
SourceClaim + EvidenceRecord + SourceText
-> TechnicalAtomBuilder
-> TechnicalAtomCatalog
```

Source page render:

```
SourceSummaryPlan + TechnicalAtomCatalog
-> SourcePageRenderer
-> WikiPage with TechnicalDetailsSection
```

Regular answer:

```
Question -> query workflow
query workflow -> source page with TechnicalDetailsSection
query workflow -> answer with citations
answer -> AnswerEvaluationReport
```

Confidence report:

```
TechnicalAtomCatalog -> atom count gate
ClaimSupportAuditReport -> atom support findings
IngestConfidenceReport -> wiki-ingest-confidence
```

## Data Model

| Object | Required fields |
|---|---|
| `TechnicalAtom` | `technical_atom_id`, `source_locator`, `page_id`, `atom_kind`, `title`, `technical_payload`, `normalized_fields`, `source_claim_ids`, `evidence_ids`, `source_range_id`, `support_status` |
| `TechnicalAtomCatalog` | `catalog_id`, `source_locator`, `artifact_fingerprint`, `technical_atoms` |
| `AnswerEvaluationCase` | `case_id`, `source_locator`, `question`, `required_atom_ids`, `required_fragments`, `required_citations` |
| `AnswerEvaluationReport` | `case_id`, `verdict`, `findings`, `required_atom_ids`, `covered_atom_ids`, `missing_fragments` |

`TechnicalAtomKind` values are `code`, `formula`, `procedure`, `table-row`, `requirement`, `exception`, and `worked-example`.
`support_status` values are `supported`, `too_broad`, `not_supported`, and `unclear`.
`verdict` values are `pass` and `fail`.
`technical_payload` stores one bounded item only.
`code` fields are `language` and `code`.
`formula` fields are `expression` and `variables`.
`procedure` fields are `ordered_steps`.
`table-row` fields are `table_title`, `columns`, and `cells`.
`requirement` and `exception` fields are `statement` and `scope`.
`worked-example` fields are `inputs`, `steps`, and `outcome`.

## APIs / Interfaces

- The page-plan cache stores `technical-atoms.json`.
- `ingest-confidence` reads `technical-atoms.json` when the fingerprint matches.
- `ingest-confidence --fresh` rebuilds `technical-atoms.json`.
- Source page rendering accepts a `TechnicalAtomCatalog`.
- `claim-support` includes `TechnicalAtom` records as candidate kind `technical-atom`.
- `query` remains the only user-facing question workflow.
- `answer-eval` runs one or more `AnswerEvaluationCase` records through `query`.
- `curator-status` reports the latest atom counts and evaluation failures.

The `technical-atoms.json` persistence model must contain only `TechnicalAtomCatalog`.
The `AnswerEvaluationCase` fixture format must use the fields listed in the data model.
The `AnswerEvaluationReport` must list missing required atoms.
The `AnswerEvaluationReport` must use deterministic checks.
The evaluator covers an atom only when the answer contains its required fragments and citation.

## Behavior & Domain Rules

Rule: the `TechnicalAtomBuilder` preserves structure before prose.

Example: input source text contains a fenced JavaScript block.
Expected outcome: the `TechnicalAtomBuilder` creates one `code` atom with the exact code block.

Example: input source claim contains `2D + baseline score >= target score`.
Expected outcome: the `TechnicalAtomBuilder` creates one `formula` atom with that formula.

Rule: the `TechnicalAtomBuilder` keeps procedure order.

Example: input claims describe roll, add modifier, compare target.
Expected outcome: the `TechnicalAtomBuilder` creates one `procedure` atom with three ordered steps.

Example: input claims describe a rule and a later exception.
Expected outcome: the `TechnicalAtomBuilder` creates one `requirement` atom and one `exception` atom.

Rule: the `SourcePageRenderer` separates summaries from atoms.

Example: input source page has summary bullets and one formula atom.
Expected outcome: the page keeps `Key supported claims` and adds `TechnicalDetailsSection`.

Ugliest edge case: input source text has a table row with OCR spacing errors.
Expected outcome: the `TechnicalAtomBuilder` creates a `table-row` atom only when cell boundaries are recoverable.

## Acceptance Criteria

Milestone 1: domain model.

- `docs/domain-vocabulary.md` records `TechnicalAtom`, `TechnicalAtomCatalog`, `AnswerEvaluationCase`, and `AnswerEvaluationReport`.
- Tests cover `TechnicalAtom`, `TechnicalAtomCatalog`, `AnswerEvaluationCase`, and `AnswerEvaluationReport`.
- Tests prove every atom has at least one evidence id.
- Tests prove atom ids stay stable when evidence ids and payload stay stable.
- Tests prove the `TechnicalAtomBuilder` never branches on a source file name.

Milestone 2: atom build.

- Tests prove fenced code becomes a `code` atom.
- Tests prove formula-like text becomes a `formula` atom.
- Tests prove ordered steps become a `procedure` atom.
- Tests prove table rows become `table-row` atoms.
- Tests prove `requirement`, `limitation`, and `negative-evidence` role tags can produce technical atoms.
- Tests prove unsupported or evidence-free candidates do not render as supported atoms.

Milestone 3: rendering and confidence.

- Tests prove source pages render `TechnicalDetailsSection` when atoms exist.
- Tests prove source pages omit `TechnicalDetailsSection` when no atoms exist.
- Tests prove rendered atoms include atom id, kind, payload, and citation.
- Tests prove `claim-support` samples `technical-atom` candidates.
- Tests prove `ingest-confidence` reports atom counts by kind.
- Tests prove stale `technical-atoms.json` rebuilds.

Milestone 4: answer evaluation.

- Tests prove `answer-eval` fails when an answer omits a required atom.
- Tests prove `answer-eval` fails when an answer omits a required citation.
- Tests prove `answer-eval` passes when an answer covers all required atoms.
- A Sword World case asks for the character-versus-monster attack procedure.
- A Sword World case requires hit check and damage calculation atoms.
- A JavaScript Allonge case asks for one exact code atom.
- A JavaScript Allonge case requires the exact code payload and citation.

Milestone 5: smoke tests.

- Run Antikythera ingest confidence first.
- Run JavaScript Allonge ingest confidence after Antikythera passes.
- Run Sword World ingest confidence after JavaScript Allonge passes.
- Run answer evaluation for JavaScript Allonge and Sword World.
- Fix each smoke-test failure and rerun the failing command.

Milestone 6: standard verification.
- Technical atom tests, ingest confidence tests, claim support tests, and session tests pass.
- `uv run ruff check harness/src harness/tests` passes.
- `uv run mypy harness/src` passes.

## Cross-Cutting Concerns

Observability: confidence reports must show atom counts by kind.

Error handling: invalid atom payloads must produce validation findings.

Copyright: rendered exact payloads must stay bounded to the single technical item.

Performance: artifact fingerprints must prevent needless atom rebuilds.

## Reference Implementations

- Evidence records: `harness/src/llmwiki/domain/evidence_registry.py`.
- Claim support: `harness/src/llmwiki/domain/claim_support.py`.
- Source summary rendering: `harness/src/llmwiki/domain/source_summary.py`.
- Ingest confidence: `harness/src/llmwiki/runtime/ingest_confidence.py`.
- Query workflow: `harness/src/llmwiki/workflows/definitions.py`.

## Alternatives Considered

- Chosen: render atoms into source pages, because the query workflow already reads pages.
- Rejected: store atoms only in cache, because query answers would miss them.
- Rejected: create a new `PageKind`, because source pages can carry source-scoped details.
- Rejected: source-specific profiles, because the mechanism must work for any technical source.
- Rejected: larger summaries, because summaries still lose exact technical structure.

## Halt Conditions

- If implementation needs a new `PageKind`, stop and ask.
- If implementation needs source-specific selectors, stop and ask.
- If implementation cannot bound exact payload rendering, stop and ask.
- If implementation needs to edit `raw/`, stop and ask.
