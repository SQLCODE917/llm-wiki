# TDD: Typed Evidence Records

## Context & Problem

The current ledger can promote clipped claims and atom labels into page input.
That makes public pages read like broken extraction output.
Typed evidence records must become the only factual input to page planning.

Glossary:

- `TypedEvidenceRecord`: one source-backed fact, rule, step, example, or table
  item.
- `EvidenceRecordSet`: all typed evidence records for one source.
- `EvidenceRecordStatus`: the publication status for one evidence record.
- `EvidenceRecordFinding`: one validation issue for an evidence record.
- `FragmentaryEvidenceRecord`: a typed evidence record that cannot support
  public prose.
- `NormalizedSourceMap`: the durable source model for one `RawSource`.
- `SourceProfile`: the source purpose and evidence vocabulary for one source.

## Goals

- Replace generic claim authority with typed evidence record authority.
- Attach every typed evidence record to source anchors.
- Mark fragmentary records before page planning.
- Keep technical atom payloads inside evidence records or source support.
- Improve wiki authority by blocking unsupported and malformed facts.

## Non-Goals & Forbidden Approaches

Non-goals:

- This design does not create public wiki pages.
- This design does not render article prose.
- This design does not implement the repair loop.
- This design does not preserve old ledger schema compatibility.

Forbidden approaches:

- Do not publish technical atom ids as human evidence.
- Do not send fragmentary evidence records to page planning.
- Do not accept evidence records without source anchors.
- Do not keep the old claim ledger as a parallel authority.

## Requirements

- The evidence extractor reads `EvidenceExtractionPlan` records.
- The evidence extractor writes one `EvidenceRecordSet` per source.
- Each typed evidence record has one allowed evidence record type.
- Each typed evidence record has at least one source anchor.
- Each typed evidence record has one evidence record status.
- Accepted records use complete source-backed statements or structured payloads.
- Fragmentary records record the missing context reason.
- Rejected records never enter page planning.
- Technical atom data maps into typed evidence records or structured payloads.

## Invariants

- `NormalizedSourceMap` remains the source text authority.
- `SourceProfile` owns the valid evidence record types.
- Raw sources stay immutable.
- Generated evidence artifacts remain disposable.
- Public wiki pages cite source evidence, not extraction confidence.

## Proposed Architecture

```text
EvidenceExtractionPlan
        |
        v
TypedEvidenceExtractor
        |
        v
EvidenceRecordSet
        |
        +--> EvidenceRecordFinding
        |
        v
PagePlanBuilder
```

`EvidenceExtractionPlan` defines source profile and source block scope.
`TypedEvidenceExtractor` creates typed records from source blocks.
`EvidenceRecordSet` stores accepted, fragmentary, and rejected records.
`EvidenceRecordFinding` stores evidence validation issues.
`PagePlanBuilder` reads only accepted evidence records.

## Key Interactions

Extract evidence records:

```text
extractor -> extraction plan: read profile vocabulary
extractor -> source map: read source blocks
model -> extractor: return typed records
extractor -> record validator: validate records
record validator -> evidence record set: store statuses
```

Block fragmentary evidence:

```text
model -> typed evidence record: emits clipped statement
record validator -> evidence record finding: record fragment
record validator -> evidence record set: mark fragmentary
page planner -> evidence record set: skip fragmentary record
```

Map technical payload:

```text
technical parser -> typed evidence record: attach payload
record validator -> source anchor: verify support
evidence pack builder -> typed evidence record: preserve payload text
```

## Data Model

`TypedEvidenceRecord` stores record id, source id, record type, status,
canonical text, structured payload, source anchors, confidence, and findings.

`EvidenceRecordStatus` values are `accepted`, `fragmentary`, `rejected`, and
`needs_review`.

`EvidenceRecordFinding` stores finding id, record id, severity, finding code,
source anchor, and message.

`EvidenceRecordSet` stores source id, source fingerprint, source profile id,
typed evidence records, and evidence record findings.

## APIs / Interfaces

The page planner accepts only `EvidenceRecordSet`.

The page planner reads only typed evidence records with status `accepted`.

The evidence record validator returns `EvidenceRecordFinding` records for all
non-accepted records.

## Behavior & Domain Rules

The validator accepts complete records.
Example: `Shade creates magical darkness in its area` can be accepted when the
source block supports the full statement.

The validator marks clipped records as fragmentary.
Example: `The shade is also very fragile and will easily.` is fragmentary.

The validator rejects malformed record text.
Example: `Furthermore if an opponent destroys a will also suffer the same
damage.` is rejected.

The validator preserves structured payloads.
Example: a spell record stores `Distance=20 meters` as payload text.

## Acceptance Criteria

- A unit test creates accepted, fragmentary, rejected, and needs-review records.
- A unit test rejects a typed evidence record without a source anchor.
- A unit test marks the Shade clipped sentence as fragmentary.
- A unit test rejects the jammed Shade sentence as malformed.
- A unit test proves a fragmentary record cannot enter a page plan.
- A unit test maps a technical atom payload into a typed evidence record.
- A Sword World fixture creates rule and procedure records.
- A JavaScript Allonge fixture creates code example and argument records.
- No public page writer reads the old claim ledger as authority.
- `uv run pytest --cov=llmwiki` passes.
- `uv run ruff check` passes.
- `uv run mypy harness/src/llmwiki` passes.

## Cross-Cutting Concerns

The evidence record artifact is auditable state.
It is not reader-facing wiki markdown.

Rejected and fragmentary counts appear in the ingest log.

## Reference Implementations

- Evidence registry: `harness/src/llmwiki/domain/evidence_registry.py`
- Technical atoms: `harness/src/llmwiki/domain/technical_atoms.py`
- Source claim gates: `docs/2026-06-20-source-claim-quality-gates.md`

## Alternatives Considered

- Keep generic claims with stricter text checks: rejected because evidence type
  still stays ambiguous.
- Keep technical atoms beside evidence records: rejected because page support
  needs one authority.
- Auto-repair clipped records: rejected because repair belongs after diagnostics.

## Halt Conditions

- Stop if page planning needs rejected or fragmentary records.
- Stop if a required source fact cannot cite a source anchor.
