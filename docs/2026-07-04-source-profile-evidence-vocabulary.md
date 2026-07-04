# TDD: Source Profile Evidence Vocabulary

## Context & Problem

The current claim path treats many source types as generic claims.
Rulebooks, programming books, recipes, and reference manuals need different
evidence types.
A generic claim shape turns procedures, rules, code examples, and tables into
weak prose fragments.

Glossary:

- `SourceProfile`: the source purpose and evidence vocabulary for one source.
- `EvidenceRecordType`: the type label for one evidence record.
- `EvidenceVocabulary`: the allowed evidence record types for one source.
- `EvidenceExtractionPlan`: the typed extraction plan for one source.
- `NormalizedSourceMap`: the durable source model for one `RawSource`.

## Goals

- Select one `SourceProfile` before typed evidence records are extracted.
- Define the allowed `EvidenceRecordType` values for each source profile.
- Make typed extraction depend on `NormalizedSourceMap`, not chunks.
- Make source profile selection observable in ingest artifacts.
- Improve wiki authority by using source-appropriate evidence types.

## Non-Goals & Forbidden Approaches

Non-goals:

- This design does not build evidence records.
- This design does not plan public pages.
- This design does not choose an LLM model.
- This design does not migrate old source profiles.

Forbidden approaches:

- Do not infer evidence type from page title alone.
- Do not let the model invent evidence record types.
- Do not use one generic claim type for all source profiles.
- Do not store source profile data in rendered wiki pages as authority.

## Requirements

- The ingest compiler selects one `SourceProfile` for each source.
- The source profile selector reads source metadata and source map signals.
- The selected source profile owns one `EvidenceVocabulary`.
- Each `EvidenceVocabulary` lists allowed evidence record types.
- The evidence extractor receives an `EvidenceExtractionPlan`.
- The evidence extractor rejects model output with unknown record types.
- The ingest artifacts record the selected source profile.
- Tests cover at least RPG rules and programming prose profiles.

## Invariants

- Raw sources stay immutable.
- `NormalizedSourceMap` remains the source text authority.
- `SourceProfile` does not replace citations.
- Generated wiki data remains disposable.
- The harness owns source profile selection.

## Proposed Architecture

```text
NormalizedSourceMap
        |
        v
SourceProfileSelector
        |
        v
SourceProfile
        |
        v
EvidenceExtractionPlan
        |
        v
TypedEvidenceExtractor
```

`NormalizedSourceMap` stores source structure.
`SourceProfileSelector` chooses the source profile.
`SourceProfile` stores source purpose and vocabulary.
`EvidenceExtractionPlan` tells the extractor which record types are valid.
`TypedEvidenceExtractor` creates typed evidence records later.

## Key Interactions

Select source profile:

```text
ingest compiler -> source map: read structure
source profile selector -> source profile: choose profile
source profile selector -> ingest artifact: write decision
```

Build extraction plan:

```text
evidence planner -> source profile: read vocabulary
evidence planner -> source map: read source blocks
evidence planner -> extraction plan: choose block ranges
```

Validate type vocabulary:

```text
model -> evidence extractor: emits typed record
evidence extractor -> source profile: check record type
evidence extractor -> finding: reject unknown type
```

## Data Model

`SourceProfile` stores profile id, source id, purpose, evidence vocabulary id,
selection reason, and confidence.

`EvidenceVocabulary` stores profile id and allowed evidence record types.

Core `EvidenceRecordType` values are `rule`, `procedure_step`, `formula`,
`table_fact`, `code_example`, `argument`, `definition`, `entity_fact`, and
`navigation_note`.

`EvidenceExtractionPlan` stores source profile id, source block ids, allowed
record types, and extraction instructions.

## APIs / Interfaces

The source profile selector returns one `SourceProfile`.

The evidence extractor accepts one `EvidenceExtractionPlan`.

The evidence extractor returns findings for unknown evidence record types.

## Behavior & Domain Rules

The selector chooses an RPG profile for a rulebook.
Example: Sword World enables `rule`, `procedure_step`, `formula`, `table_fact`,
and `entity_fact`.

The selector chooses a programming profile for a programming book.
Example: JavaScript Allonge enables `code_example`, `argument`, `definition`,
and `procedure_step`.

The extractor rejects unknown record types.
Example: `spell_flavor` is rejected unless the selected vocabulary allows it.

The selector records uncertainty.
Example: a source with weak metadata records a warning and uses the default
reference profile.

## Acceptance Criteria

- A unit test selects the RPG profile for a Sword World fixture.
- A unit test selects the programming profile for a JavaScript Allonge fixture.
- The Sword World extraction plan allows `rule` and `procedure_step`.
- The JavaScript Allonge extraction plan allows `code_example` and `argument`.
- A model output with an unknown record type creates a blocking finding.
- A source profile artifact records selection reason and confidence.
- No test fixture uses a generic claim type as the only record type.
- A fixture proves source profile data does not create public wiki pages.
- `uv run pytest --cov=llmwiki` passes.
- `uv run ruff check` passes.
- `uv run mypy harness/src/llmwiki` passes.

## Cross-Cutting Concerns

The source profile artifact is diagnostic state.
It is not source evidence.

The ingest log records the selected source profile and blocking findings.

## Reference Implementations

- Ingest profiles: `docs/2026-06-16-ingest-profiles.md`
- Domain vocabulary: `docs/domain-vocabulary.md`
- Runtime profiles: `harness/src/llmwiki/config.py`

## Alternatives Considered

- Let each prompt define its own type names: rejected because type drift breaks
  validation.
- Use one universal claim type: rejected because source purpose affects evidence
  shape.
- Store profiles only in `SCHEMA.md`: rejected because the compiler needs a
  typed artifact.

## Halt Conditions

- Stop if a source needs more than one source profile in one ingest run.
- Stop if the selected vocabulary cannot represent tables or code examples.
