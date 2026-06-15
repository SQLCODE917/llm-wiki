# Grounding Claim Audit

## Context & Problem

Strict citation checks can prove that cited source paths and locators are valid,
but they do not prove a synthesized claim follows from the evidence. The backup
had grounding and claim-judge scripts that separated deterministic evidence
failures from model-assisted support judgments. M5 needs a smaller version that
fits the flat wiki and Forge workflows.

Pattern excerpts addressed from `docs/llm-wiki.md`:

- "Raw sources ... are immutable"
- "The wiki ... keeps everything consistent"
- "synthesizes an answer with citations"
- "Look for ... stale claims that newer sources have superseded"

## Goals

- Audit whether important wiki claims are supported by cited evidence.
- Separate deterministic grounding failures from model judgment.
- File a report without rewriting content pages.
- Feed actionable findings into curator status and lint.

## Non-Goals & Forbidden Approaches

Non-goals:

- No automatic claim repair.
- No requirement that all prose become claim tables.
- No web search or freshness checking.
- No cloud-model dependency.

Forbidden approaches:

- Do not trust model support verdicts when deterministic citation evidence
  already fails.
- Do not judge unsupported claims by reading raw sources ad hoc outside the
  harness.
- Do not copy backup report formats that depend on type directories.

## Requirements

- The audit selects a bounded set of claim-bearing pages.
- Deterministic evidence failures are reported before model judging.
- The model sees the claim, cited page context, and resolved evidence excerpt.
- Verdicts are limited to `supported`, `too_broad`, `not_supported`, and
  `unclear`.
- The command writes a harness-owned synthesis report and appends `log.md`.

## Invariants

- Raw sources remain immutable.
- The audit is report-only.
- A clean audit over a bounded set is not proof that every wiki claim is
  grounded.
- Fatal deterministic evidence findings outrank model opinions.

## Proposed Architecture

```
+----------+      +----------------+      +--------------+      +---------+
| selector |----->| evidence layer |----->| judge workflow|----->| report  |
+----------+      +----------------+      +--------------+      +---------+
```

The selector chooses pages/claims. Evidence layer resolves citations. The model
judges only supportedness where deterministic evidence is available. The report
records scope and findings.

## Key Interactions

Deterministic failure:

```
Selector -> evidence: claim citation
Evidence -> report: locator invalid
Judge    -> skipped
```

Model-supported claim:

```
Selector -> evidence: resolved excerpt
Model    -> judge_claim: supported
Report   -> finding list
```

Too-broad claim:

```
Model -> judge_claim: too_broad with rationale
Report -> curator action: narrow claim or add evidence
```

## Data Model

- `ClaimCandidate`: page name, claim text, local context, citations.
- `GroundingVerdict`: candidate, verdict, severity, rationale, recommended
  action.
- Report page: `wiki-grounding` or another harness-owned synthesis page chosen
  consistently with existing system pages.

## APIs / Interfaces

- New CLI command: `llmwiki grounding`.
- Option: `--max-claims N`, with a small default.
- Model tool: `record_grounding_verdict`.
- Terminal tool: `finish_grounding`.

## Behavior & Domain Rules

- Claims without citations are findings, not model-judge prompts. This first
  implementation intentionally audits citation-bearing claims only; broad
  uncited-prose detection is deferred because a noisy claim detector would
  violate the selector halt condition.
- Model judges claim support, not writing quality.
- `unclear` is a warning unless deterministic evidence failed.

Examples:

- Claim says arrays copy on destructuring; evidence excerpt says same -> supported.
- Claim adds performance claims absent from excerpt -> too_broad.
- Claim contradicts excerpt -> not_supported.

## Acceptance Criteria

- Tests prove deterministic failures skip model judgment.
- Tests prove verdict enum validation rejects unexpected labels.
- Tests prove bounded claim selection and skipped counts are reported.
- Tests prove the command writes a report and appends log.
- Live smoke test over current wiki completes without max-iteration failure.

## Cross-Cutting Concerns

Observability: every model verdict must be visible in the transcript and final
report so a curator can inspect the page and evidence.

## Reference Implementations

- Current contradiction audit pattern: `harness/src/llmwiki/domain/contradictions.py`.
- Current evidence policy: `harness/src/llmwiki/domain/evidence.py`.
- Backup grounding idea: `backup/reference/llm-wiki-pre-m5-migration-2026-06-14/tools/wiki_grounding.py`.
- Backup judge idea: `backup/reference/llm-wiki-pre-m5-migration-2026-06-14/tools/wiki_judge_claims.py`.

## Alternatives Considered

- Fold into every lint run - rejected because model judging is expensive.
- Require claim tables first - rejected because the current wiki is prose-heavy.
- Auto-fix unsupported claims - rejected because source interpretation needs a
  curator decision.

## Halt Conditions

- If the selector cannot identify claim candidates without excessive false
  positives, stop and write a smaller claim-selection TDD first.

## Implementation Notes

- Implemented `llmwiki grounding` as a report-only command.
- Added deterministic claim selection in `llmwiki.domain.grounding`.
- Added `record_grounding_verdict` with the fixed verdict enum:
  `supported`, `too_broad`, `not_supported`, `unclear`.
- Added `wiki-grounding` as a harness-owned synthesis page exempt from orphan
  checks.
- Fatal deterministic evidence findings skip model judgment and are rendered
  before model verdicts.
- Non-`unclear` verdicts are rejected when the harness could not provide a
  normalized evidence excerpt for the selected claim.
- Current selector is deliberately narrow: it selects citation-bearing lines
  with valid deterministic evidence context. It does not attempt general
  uncited-claim detection yet.

## Verification Plan

- Run focused domain/session tests for grounding selection, verdict validation,
  short-circuiting, report filing, and log appends.
- Run the full test suite, formatter/linter/typecheck, and diff check.
- Run `uv run llmwiki grounding --max-claims 2` over the current wiki and
  inspect `wiki/wiki-grounding.md` for a coherent bounded report.

## Verification Results

- Focused domain/session tests pass.
- Live `uv run llmwiki grounding --max-claims 2` completed without a
  max-iteration failure.
- Initial live runs exposed citation-list/navigation line false positives and
  overconfident support verdicts without evidence excerpts. Fixed with
  selector filters and a `record_grounding_verdict` boundary check.
- Final live report selected actual prose claims and recorded `unclear` when
  PDF citations lacked normalized evidence excerpts.
