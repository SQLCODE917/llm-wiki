# Stable Evidence Locators

## Context & Problem

Glossary:

| Term | Meaning |
|---|---|
| `EvidenceLocator` | Normalized source address for one evidence span. |
| `EvidenceIdentity` | Stable identity material for one `EvidenceRecord`. |
| `EvidenceLocatorIndex` | Generated index of `EvidenceLocator` records for one source. |
| `EvidenceLocatorFinding` | Deterministic issue found while checking an `EvidenceLocatorIndex`. |
| `EvidenceLocatorBuilder` | Domain service that creates an `EvidenceLocatorIndex`. |
| `LocatorArtifactFingerprint` | Fingerprint that decides whether a locator artifact is current. |
| `LocatorStabilityGate` | Confidence gate that compares old and new `EvidenceLocatorIndex` records. |
| `EvidenceRegistry` | Rebuildable collection of source evidence records. |
| `EvidenceRecord` | Stable audit record for one source excerpt. |
| `SourceText` | Line-addressable text derived from one `RawSource`. |
| `SourceRange` | Valid source span for one planned wiki page. |
| `IngestConfidenceReport` | Harness-owned report that summarizes post-ingest validation. |

The current `EvidenceRegistry` stores source text, source ranges, and evidence records.
The current `EvidenceRecord` identity can depend on `SourceRange`, which depends on `PageId`.
The current locator check resolves citation text but does not persist locator identity.
This TDD makes evidence identity independent of page placement and stores locator resolution as generated cache state.

## Goals

- Promote `EvidenceLocator` to a first-class domain object.
- Add `EvidenceIdentity` for `EvidenceRecord` identity.
- Add `EvidenceLocatorIndex` beside the `EvidenceRegistry` cache.
- Keep `EvidenceRecord` ids stable when source text and locator evidence stay stable.
- Report locator drift in `IngestConfidenceReport`.
- Reuse valid locator artifacts during repeated test ingests.
- Test Antikythera first, then JavaScript Allonge.

## Non-Goals & Forbidden Approaches

Non-goals:

- This TDD does not auto-repair citations.
- This TDD does not require evidence ids in wiki prose.
- This TDD does not change `WikiStructure`.
- This TDD does not reingest Sword World.
- This TDD does not add a web UI.

Forbidden approaches:

- Do not include `PageId` in `EvidenceIdentity`.
- Do not include `SourceRange.source_range_id` in `EvidenceIdentity`.
- Do not write locator artifacts under `raw/`.
- Do not accept model-authored locators without deterministic validation.
- Do not import backup code into active code.
- Do not migrate obsolete cache shapes.

## Requirements

- `EvidenceLocatorBuilder` must create one `EvidenceLocator` for each `EvidenceRecord`.
- `EvidenceLocatorBuilder` must create one `EvidenceLocator` for each resolved citation with evidence text.
- `EvidenceLocator` must record source locator, source hash, locator text, locator kind, range, and excerpt digest.
- `EvidenceLocator` must record a canonical excerpt digest.
- `EvidenceIdentity` must use source locator, source hash, locator text, and canonical excerpt digest.
- `EvidenceIdentity` must exclude `PageId`, `PagePath`, and `SourceRange`.
- `EvidenceRecord` must store `evidence_identity_id`.
- `EvidenceRecord.evidence_id` must derive from `EvidenceIdentity`.
- `EvidenceLocatorIndex` must store source locator, source hash, `LocatorArtifactFingerprint`, and locator records.
- `EvidenceLocatorIndex` must validate each locator against `SourceText`.
- `EvidenceLocatorIndex` must preserve invalid locator findings.
- The ingest cache must store `evidence-locators.json` beside `evidence-registry.json`.
- `ArtifactReuseDecision` must compare `LocatorArtifactFingerprint`.
- `IngestConfidenceReport` must include `LocatorStabilityGate`.
- `LocatorStabilityGate` must compare old and new locator artifacts when both exist.
- `LocatorStabilityGate` must report stable count, drift count, and invalid count.
- `lint --strict-evidence warn` must report invalid locator warnings.
- `lint --strict-evidence fail` must block invalid locators.

## Invariants

- `raw/` remains immutable.
- Generated cache state remains disposable.
- `EvidenceLocatorIndex` remains rebuildable from `SourceText`, `EvidenceRegistry`, and generated wiki pages.
- `SourceRange` controls page scope but not evidence identity.
- `Citation` parsing remains the authority for source path syntax.
- A passing locator gate does not prove that every wiki claim is correct.

## Proposed Architecture

```
+-----------+     +------------+     +-----------------+
| RawSource |---->| SourceText |---->| EvidenceLocator |
+-----------+     +-----+------+     +--------+--------+
                         |                     |
                         v                     v
                  +--------------+     +----------------+
                  | Evidence     |---->| Evidence       |
                  | Registry     |     | Identity       |
                  +------+-------+     +--------+-------+
                         |                      |
                         v                      v
                  +----------------------+  +----------------+
                  | EvidenceLocatorIndex |->| EvidencePolicy |
                  +----------+-----------+  +--------+-------+
                             |                       |
                             v                       v
                  +----------------------+  +----------------+
                  | IngestConfidence     |  | lint strict    |
                  | Report               |  | evidence       |
                  +----------------------+  +----------------+
```

`RawSource` remains the immutable source file.
`SourceText` gives valid line addresses.
`EvidenceLocator` records one normalized source address.
`EvidenceIdentity` gives one evidence record a page-independent id.
`EvidenceLocatorIndex` stores generated locator state.
`EvidencePolicy` checks citations against the locator index.
`IngestConfidenceReport` exposes locator stability for one source.

## Key Interactions

Evidence registry build:

```
SourceText -> EvidenceLocator
EvidenceLocator -> EvidenceIdentity
EvidenceIdentity -> EvidenceRecord
EvidenceRecord -> EvidenceRegistry
```

Citation check:

```
wiki page -> Citation
Citation -> EvidenceLocator
EvidenceLocatorIndex -> EvidenceLocatorFinding
EvidencePolicy -> lint finding
```

Artifact reuse:

```
raw source -> source hash
evidence-locators.json -> LocatorArtifactFingerprint
matching fingerprint -> reuse
stale fingerprint -> rebuild
```

Locator stability gate:

```
old EvidenceLocatorIndex -> locator ids
new EvidenceLocatorIndex -> locator ids
comparison -> IngestConfidenceReport
```

## Data Model

| Object | Required fields |
|---|---|
| `EvidenceLocator` | `locator_id`, `source_locator`, `source_hash`, `locator_text`, `locator_kind`, `range_start`, `range_end`, `excerpt_digest`, `canonical_excerpt_digest` |
| `EvidenceIdentity` | `evidence_identity_id`, `source_locator`, `source_hash`, `locator_text`, `canonical_excerpt_digest` |
| `EvidenceLocatorIndex` | `index_id`, `source_locator`, `source_hash`, `locator_artifact_fingerprint`, `locators`, `findings` |
| `EvidenceLocatorFinding` | `finding_id`, `severity`, `category`, `source_locator`, `page_id`, `locator_id`, `message` |

`locator_kind` values are `normalized-line` and `page-range`.
`severity` values are `blocker`, `warning`, and `info`.
`category` values are `invalid-range`, `missing-source-text`, `locator-drift`, and `stale-artifact`.

## APIs / Interfaces

- `EvidenceRegistry` exposes an `EvidenceLocatorIndex`.
- `EvidenceRecord` exposes `evidence_identity_id`.
- `EvidencePolicy` accepts an `EvidenceLocatorIndex`.
- `llmwiki ingest-confidence raw/<path>` runs `LocatorStabilityGate`.
- `llmwiki lint --strict-evidence warn` reports invalid locator warnings.
- `llmwiki lint --strict-evidence fail` treats blocker `EvidenceLocatorFinding` records as fatal.
- Curator status summarizes the latest `LocatorStabilityGate`.

## Behavior & Domain Rules

Rule: evidence identity ignores page placement.

Example: input evidence keeps the same source hash, locator text, and canonical excerpt digest.
Expected outcome: `EvidenceRecord.evidence_id` stays the same after `PageId` changes.

Example: input evidence keeps the same page target but changes canonical excerpt digest.
Expected outcome: `EvidenceRecord.evidence_id` changes.

Rule: locator records validate source addresses.

Example: input locator references `normalized:L2-L3` in a five-line source.
Expected outcome: `EvidenceLocatorIndex` records no finding.

Example: input locator references `normalized:L6` in a five-line source.
Expected outcome: `EvidenceLocatorIndex` records `invalid-range`.

Rule: locator stability reports drift.

Example: input old and new locator indexes contain the same locator ids.
Expected outcome: `LocatorStabilityGate` passes.

Example: input old and new locator indexes differ only because `PageId` changed.
Expected outcome: `LocatorStabilityGate` passes.

Ugliest edge case: input PDF cache changes line layout while raw source hash stays the same.
Expected outcome: `LocatorStabilityGate` records `locator-drift`.

## Acceptance Criteria

Milestone 1: domain tests.

- `docs/domain-vocabulary.md` records `EvidenceLocator`, `EvidenceIdentity`, `EvidenceLocatorIndex`, and `EvidenceLocatorFinding`.
- Tests prove `EvidenceRecord.evidence_id` survives `PageId` changes.
- Tests prove `EvidenceRecord.evidence_id` survives `SourceRange.source_range_id` changes.
- Tests prove `EvidenceRecord.evidence_id` changes when canonical excerpt digest changes.
- Tests prove `EvidenceLocatorIndex` validates normalized line ranges.
- Tests prove `EvidenceLocatorIndex` validates page ranges.
- Tests prove `evidence-locators.json` round-trips through JSON.

Milestone 2: policy and confidence tests.

- Tests prove `ArtifactReuseDecision` reuses matching locator artifacts.
- Tests prove stale locator artifacts rebuild.
- Tests prove `EvidencePolicy` reads `EvidenceLocatorIndex` in strict evidence modes.
- Tests prove `lint --strict-evidence warn` reports invalid locators.
- Tests prove `lint --strict-evidence fail` blocks invalid locators.
- Tests prove `IngestConfidenceReport` renders `LocatorStabilityGate`.
- Tests prove curator status summarizes `LocatorStabilityGate`.

Milestone 3: Antikythera ingest gate.

- Run `uv run llmwiki ingest-confidence raw/antikythera-mechanism.md --fresh`.
- Run `uv run llmwiki ingest-confidence raw/antikythera-mechanism.md`.
- The second run reuses valid locator artifacts.
- The second run reports stable evidence ids.
- The implementation fixes each Antikythera blocker and reruns the command.

Milestone 4: JavaScript Allonge ingest gate.

- Run `uv run llmwiki ingest-confidence raw/javascriptallonge.pdf --fresh`.
- Run `uv run llmwiki ingest-confidence raw/javascriptallonge.pdf`.
- The second run reuses valid PDF locator artifacts.
- The second run reports stable evidence ids or explicit locator drift.
- The implementation fixes each JavaScript Allonge blocker and reruns the command.

Milestone 5: standard verification.

- `uv run pytest harness/tests/test_evidence_locator_index.py harness/tests/test_evidence_registry.py` passes.
- `uv run pytest harness/tests/test_ingest_confidence_report.py harness/tests/test_maintenance.py` passes.
- `uv run ruff check harness/src harness/tests` passes.
- `uv run mypy harness/src` passes.
- No active code imports backup paths.

## Cross-Cutting Concerns

Observability: reports must show locator counts, stable counts, drift counts, and invalid counts.

Error handling: corrupt locator artifacts must produce `stale-artifact` findings and trigger rebuild.

Performance: `EvidenceLocatorBuilder` must not enumerate all possible source spans.

## Reference Implementations

- Current evidence registry: `harness/src/llmwiki/domain/evidence_registry.py`.
- Current locator matching: `harness/src/llmwiki/domain/evidence_locators.py`.
- Current registry JSON mapping: `harness/src/llmwiki/domain/evidence_registry_io.py`.
- Current confidence artifacts: `harness/src/llmwiki/runtime/ingest_confidence_artifacts.py`.
- Backup locator type idea: `backup/reference/llm-wiki-pre-m5-migration-2026-06-14/packages/wiki_core/src/wiki_core/types/locator.py`.
- Backup resolver idea: `backup/reference/llm-wiki-pre-m5-migration-2026-06-14/packages/wiki_io/src/wiki_io/evidence/resolver.py`.
- Backup validator idea: `backup/reference/llm-wiki-pre-m5-migration-2026-06-14/packages/wiki_io/src/wiki_io/evidence/validator.py`.
- Backup locator backfill idea: `backup/reference/llm-wiki-pre-m5-migration-2026-06-14/tools/wiki_add_evidence_locators.py`.

## Alternatives Considered

- Chosen: generated `EvidenceLocatorIndex`, because audits need durable locator state.
- Rejected: evidence ids derived from `PageId`, because page placement changes during ingest.
- Rejected: evidence ids in wiki prose, because generated prose is not the identity authority.
- Rejected: whole-source locator enumeration, because large PDFs would create unused records.
- Rejected: backup restore, because current domain objects must own the design.

## Halt Conditions

- If `EvidenceRecord.evidence_id` changes after only `PageId` changes, stop and fix identity first.
- If PDF locator drift cannot name the changed cache artifact, stop and write a PDF cache contract TDD.
- If implementation needs a new wiki folder structure, stop and keep `WikiStructure` unchanged.
