# Claim Support Audit

## Context & Problem

Glossary:

| Term | Meaning |
|---|---|
| `ClaimSupportCandidate` | One wiki claim selected for support judgment. |
| `ClaimSupportVerdict` | Model-assisted judgment for one `ClaimSupportCandidate`. |
| `ClaimSupportAuditReport` | Harness-owned report for one claim support audit. |
| `ClaimSupportFinding` | Structured finding from deterministic checks or model judgment. |
| `EvidenceRecord` | Stable audit record for one source excerpt. |
| `EvidenceRegistry` | Rebuildable collection of source evidence records. |
| `SourceClaim` | Atomic statement extracted from one `ExtractedUnit`. |
| `SourceSummaryBullet` | One source summary bullet with covered source claims. |
| `PageBody` | Markdown body of one `WikiPage`. |
| `GeneratedWikiState` | `wiki/`, `index.md`, `log.md`, and disposable ingest cache. |

Current grounding audit samples citation-bearing prose.
It cannot judge source-summary bullets against selected `SourceClaim` records.
The backup row judge separated deterministic evidence failures from support verdicts.
This TDD adds that stronger audit as a report-only workflow.

## Goals

- Select structured `ClaimSupportCandidate` records from generated wiki pages.
- Prefer candidates with `SourceClaim` and `EvidenceRecord` links.
- Separate deterministic findings from model support judgment.
- Limit model verdicts to a fixed support enum.
- File a `ClaimSupportAuditReport` without editing content pages.
- Feed report summaries into curator status.

## Non-Goals & Forbidden Approaches

Non-goals:

- This TDD does not auto-repair wiki content.
- This TDD does not replace the existing grounding audit.
- This TDD does not require all wiki prose to become claim tables.
- This TDD does not add web search or freshness checks.
- This TDD does not judge claims without source evidence.

Forbidden approaches:

- Do not let the model mark a candidate supported without evidence excerpts.
- Do not send raw whole-source text to the model.
- Do not use planning artifacts as source evidence.
- Do not rewrite content pages from the audit workflow.
- Do not import backup tools into active code.

## Requirements

- The selector must build `ClaimSupportCandidate` records from `SourceSummaryBullet` records first.
- The selector must build lower-priority candidates from citation-bearing `PageBody` lines.
- Each candidate must include page id, claim text, local page context, and citation text.
- Each candidate must include `SourceClaim.source_claim_id` values when they exist.
- Each candidate must include `EvidenceRecord.evidence_id` values when they exist.
- Deterministic checks must run before the model sees a candidate.
- Deterministic checks must record missing evidence, locator mismatch, source-range violation, and copied evidence mismatch.
- The model must see claim text, local context, and bounded evidence excerpts.
- The model must return one verdict per judged candidate.
- Verdict labels must be `supported`, `too_broad`, `not_supported`, or `unclear`.
- The workflow must reject unsupported verdict labels.
- The workflow must reject `supported` when deterministic findings exist.
- The workflow must file `wiki-claim-support`.
- The workflow must append one `log.md` entry.

## Invariants

- `raw/` remains immutable.
- The audit is report-only.
- A bounded audit is not proof that every wiki claim is supported.
- Fatal deterministic findings outrank model verdicts.
- `GeneratedWikiState` remains disposable.
- `EvidenceRegistry` remains the source of audit excerpts.

## Proposed Architecture

```
+----------------+     +-----------------------+     +----------------+
| wiki pages     |---->| ClaimSupportCandidate |---->| deterministic  |
+----------------+     +-----------+-----------+     | checks         |
                                   |                 +-------+--------+
                                   v                         |
                         +--------------------+              v
                         | judge workflow     |------>| ClaimSupport  |
                         +---------+----------+       | AuditReport   |
                                   |                  +---------------+
                                   v
                         +--------------------+
                         | claim-support page |
                         +--------------------+
```

The selector chooses bounded candidates.
Deterministic checks protect the judge from bad evidence.
The judge workflow records fixed verdicts.
The report writer files a harness-owned report page.

## Key Interactions

Candidate selection:

```
SourceSummaryDraft cache -> SourceSummaryBullet
SourceSummaryBullet -> ClaimSupportCandidate
PageBody -> citation-bearing line
citation-bearing line -> ClaimSupportCandidate
```

Deterministic failure:

```
ClaimSupportCandidate -> EvidenceRegistry
EvidenceRegistry -> ClaimSupportFinding
judge workflow -> skipped
```

Model judgment:

```
ClaimSupportCandidate -> bounded evidence excerpts
model -> record_claim_support_verdict
verdict -> ClaimSupportAuditReport
```

Report filing:

```
ClaimSupportAuditReport -> wiki-claim-support
ClaimSupportAuditReport -> log.md
```

## Data Model

| Object | Required fields |
|---|---|
| `ClaimSupportCandidate` | `candidate_id`, `page_id`, `claim_text`, `page_context`, `citation_texts`, `source_claim_ids`, `evidence_ids` |
| `ClaimSupportVerdict` | `candidate_id`, `verdict`, `rationale`, `recommended_action` |
| `ClaimSupportFinding` | `finding_id`, `candidate_id`, `page_id`, `severity`, `category`, `message`, `evidence_id` |
| `ClaimSupportAuditReport` | `run_id`, `selected_count`, `skipped_count`, `findings`, `verdicts`, `model_report` |

`severity` values are `blocker`, `warning`, and `info`.
`category` values are `missing-evidence`, `locator-mismatch`, `source-range`, `copied-evidence`, and `support-verdict`.
`verdict` values are `supported`, `too_broad`, `not_supported`, and `unclear`.

## APIs / Interfaces

- New CLI command: `llmwiki claim-support`.
- Option: `--max-claims N`, with default `5`.
- Option: `--source raw/<path>`, which limits candidates to pages sourced from one raw source.
- Model tool: `record_claim_support_verdict`.
- Terminal tool: `finish_claim_support`.
- Report page: `wiki-claim-support`.
- Curator status reads the latest `ClaimSupportAuditReport` summary.

## Behavior & Domain Rules

Rule: deterministic findings skip model judgment.

Example: input candidate has no `EvidenceRecord`.
Expected outcome: audit records `missing-evidence` and skips the model.

Example: input candidate cites a locator outside its `SourceRange`.
Expected outcome: audit records `source-range` and skips the model.

Rule: model verdicts judge support, not prose quality.

Example: input claim states exactly what the evidence excerpt states.
Expected outcome: verdict is `supported`.

Example: input claim adds a rule exception absent from the evidence excerpt.
Expected outcome: verdict is `too_broad`.

Example: input claim contradicts the evidence excerpt.
Expected outcome: verdict is `not_supported`.

Ugliest edge case: input claim combines two supported clauses and one unsupported clause.
Expected outcome: verdict is `too_broad`.

## Acceptance Criteria

Milestone 1: selector tests.

- `docs/domain-vocabulary.md` records `ClaimSupportCandidate`, `ClaimSupportVerdict`, `ClaimSupportFinding`, and `ClaimSupportAuditReport`.
- Tests prove source-summary bullets outrank prose lines.
- Tests prove citation-bearing prose lines become candidates.
- Tests prove candidates include `SourceClaim` ids when cached drafts include them.
- Tests prove candidates include `EvidenceRecord` ids when the registry contains them.
- Tests prove `--source` filters candidates by raw source.

Milestone 2: deterministic check tests.

- Tests prove missing evidence skips model judgment.
- Tests prove locator mismatch skips model judgment.
- Tests prove source-range violation skips model judgment.
- Tests prove copied evidence mismatch skips model judgment.
- Tests prove deterministic findings render in the report.

Milestone 3: workflow tests.

- Tests prove verdict enum validation rejects unknown labels.
- Tests prove `supported` fails when deterministic findings exist.
- Tests prove `wiki-claim-support` is filed.
- Tests prove `log.md` receives one claim-support entry.
- Tests prove curator status summarizes the latest report.
- `uv run pytest harness/tests/test_claim_support_audit.py harness/tests/test_session_e2e.py` passes.

Milestone 4: ingest audit smoke tests.

- Antikythera claim-support audit runs after Antikythera ingest.
- JavaScript Allonge claim-support audit runs after JavaScript Allonge ingest.
- The implementation fixes each smoke-test issue and reruns the failing audit.

## Cross-Cutting Concerns

Observability: every candidate must show selected evidence ids and deterministic findings in the report.

Error handling: model tool errors must state why the verdict was rejected.

Cost control: `--max-claims` bounds model work and defaults to five candidates.

## Reference Implementations

- Current grounding audit: `harness/src/llmwiki/domain/grounding.py`.
- Current grounding tools: `harness/src/llmwiki/workflows/grounding_tools.py`.
- Current source summary drafts: `harness/src/llmwiki/workflows/source_summary_write.py`.
- Backup row judge idea: `backup/reference/llm-wiki-pre-m5-migration-2026-06-14/tools/wiki_judge_claims.py`.
- Backup repair hints idea: `backup/reference/llm-wiki-pre-m5-migration-2026-06-14/tools/wiki_claim_repair_hints.py`.

## Alternatives Considered

- Chosen: report-only claim support audit, because source interpretation needs curator review.
- Rejected: automatic claim repair, because the model can over-correct rules.
- Rejected: whole-page model judgment, because row-level verdicts give actionable findings.
- Rejected: lexical overlap scoring, because technical claims can share words and differ in meaning.

## Halt Conditions

- If candidates cannot include evidence excerpts, stop and implement the source evidence registry first.
- If verdicts need source text outside bounded excerpts, stop and redesign the candidate contract.
- If the workflow must edit content pages, stop and split a repair TDD.
