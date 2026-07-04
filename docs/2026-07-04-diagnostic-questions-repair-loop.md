# TDD: Diagnostic Questions Repair Loop

## Context & Problem

The current pipeline can publish pages that pass local checks but fail reader
tasks.
The wiki needs diagnostics that ask source-grounded questions and inspect
whether the generated wiki can answer them.
Repair tasks must feed back into page planning and article writing.

Glossary:

- `DiagnosticQuestion`: one source-grounded question for wiki evaluation.
- `DiagnosticAnswer`: the wiki-only answer to one diagnostic question.
- `DiagnosticFinding`: one evaluation issue for a diagnostic answer.
- `RepairTask`: one planned repair from a diagnostic finding.
- `RepairRun`: one bounded repair attempt.
- `IngestArtifactSet`: the ordered artifacts from one ingest run.
- `EvidencePack`: the selected source support for one planned page.
- `PagePlan`: the accepted public page plan for one source.
- `ArticleLintRun`: one lint run for generated public articles.

## Goals

- Generate diagnostic questions from source evidence and page plans.
- Answer diagnostic questions from the wiki layer only.
- Judge diagnostic answers against evidence packs and source blocks.
- Create repair tasks for missing, unsupported, or incoherent answers.
- Improve wiki coherence with a measurable reader-task loop.

## Non-Goals & Forbidden Approaches

Non-goals:

- This design does not replace article lint.
- This design does not run live network searches.
- This design does not require human review for every diagnostic question.
- This design does not preserve old evaluation artifact formats.

Forbidden approaches:

- Do not answer diagnostic questions from raw sources.
- Do not let repair tasks bypass article lint.
- Do not publish repaired pages without accepted publication gates.
- Do not use diagnostics as source evidence.

## Requirements

- The diagnostic builder reads source map, evidence records, page plan, and
  evidence packs.
- Each diagnostic question cites the source anchors that justify the question.
- The diagnostic answerer reads only published wiki pages.
- The diagnostic judge compares answers with evidence packs and source blocks.
- The diagnostic judge writes diagnostic findings.
- The repair planner creates repair tasks from blocking diagnostic findings.
- A repair run updates page plans or human articles.
- Repaired pages pass article lint before publication.

## Invariants

- Raw sources remain immutable.
- Diagnostics evaluate the wiki layer.
- Evidence packs remain the support authority.
- Article lint remains the publication gate.
- Generated artifacts remain disposable.

## Proposed Architecture

```text
IngestArtifactSet
       |
       v
DiagnosticBuilder
       |
       v
DiagnosticQuestion
       |
       v
DiagnosticAnswerer
       |
       v
DiagnosticJudge
       |
       v
RepairTask
       |
       v
RepairRun
```

`IngestArtifactSet` stores source and article artifacts.
`DiagnosticBuilder` creates source-grounded questions.
`DiagnosticQuestion` stores one evaluation prompt.
`DiagnosticAnswerer` answers from the wiki.
`DiagnosticJudge` evaluates the answer against support.
`RepairTask` stores one repair target.
`RepairRun` executes bounded repair and returns to article lint.

## Key Interactions

Build diagnostics:

```text
diagnostic builder -> evidence pack: read support
diagnostic builder -> page plan: read public pages
diagnostic builder -> diagnostic question: write question
```

Judge answer:

```text
answerer -> wiki: read pages
answerer -> diagnostic answer: write answer
judge -> evidence pack: compare support
judge -> diagnostic finding: write finding
```

Repair page:

```text
repair planner -> diagnostic finding: read issue
repair planner -> repair task: write task
repair run -> article writer: revise article
article linter -> revised article: gate publication
```

## Data Model

`DiagnosticQuestion` stores question id, source id, page ids, source anchors,
expected support refs, question text, and purpose.

`DiagnosticAnswer` stores question id, answer text, cited page ids, and cited
support refs.

`DiagnosticFinding` stores finding id, question id, severity, finding code,
support ref, page id, and message.

`RepairTask` stores task id, finding ids, repair kind, target page id, required
support refs, and status.

`RepairRun` stores run id, repair task ids, changed page ids, lint run ids, and
status.

## APIs / Interfaces

The diagnostic answerer reads only wiki pages and index data.

The repair planner reads diagnostic findings.

The repair run sends changed pages through article lint.

## Behavior & Domain Rules

The diagnostic builder asks reader-task questions.
Example: `How does Shade interact with will-o-wisp?` cites Shade support refs.

The answerer cannot read raw sources.
Example: a missing answer records a wiki coverage finding.

The judge checks authority.
Example: an answer that invents a Shade effect records an unsupported answer
finding.

The repair run respects lint.
Example: a repaired Shade page with a clipped sentence still does not publish.

## Acceptance Criteria

- A unit test creates diagnostic questions from an evidence pack.
- A unit test proves diagnostic answers read wiki pages, not raw sources.
- A unit test records a missing-answer diagnostic finding.
- A unit test records an unsupported-answer diagnostic finding.
- A unit test creates a repair task from a blocking diagnostic finding.
- A repair run test sends changed pages through article lint.
- A Sword World fixture asks and evaluates a Shade interaction question.
- A Sword World fixture asks and evaluates a character creation question.
- A JavaScript Allonge fixture asks and evaluates a recipe question.
- A diagnostics report records answered count, missing count, unsupported count,
  and repaired count.
- `uv run pytest --cov=llmwiki` passes.
- `uv run ruff check` passes.
- `uv run mypy harness/src/llmwiki` passes.

## Cross-Cutting Concerns

Diagnostics use fake model boundaries in tests.
They do not run live network calls.

The ingest log records diagnostic finding counts and repair run status.

## Reference Implementations

- Answer evaluation: `harness/src/llmwiki/domain/answer_evaluation.py`
- Query runtime: `harness/src/llmwiki/runtime/session.py`
- Claim support audit: `harness/src/llmwiki/domain/claim_support.py`

## Alternatives Considered

- Rely only on lint: rejected because lint does not test reader tasks.
- Answer diagnostics from raw sources: rejected because the wiki layer is the
  product under test.
- Let repair bypass page planning: rejected because repairs must preserve public
  wiki shape.

## Halt Conditions

- Stop if diagnostic answers require raw source access.
- Stop if repair publishes pages without article lint.
