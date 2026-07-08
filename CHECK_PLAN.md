# LLM-Wiki Contract Check Plan

This file is the agent-runnable contract for LLM-Wiki harness changes.
Update it before changing compiler contracts, CLI surfaces, artifact names,
page families, or generated wiki workflows.

`CHECK_PLAN.md` is operator guidance. It is not source evidence, wiki content,
or a TDD.

## Source-Of-Truth Map

| Surface | Source Of Truth | Check |
|---|---|---|
| Page kinds | `llmwiki.domain.schema.PAGE_KINDS` | Static tests compare this file to the constant. |
| Page families | `llmwiki.domain.schema.PAGE_FAMILIES` | Static tests compare this file to the constant. |
| Metadata fields | `llmwiki.domain.schema.PAGE_METADATA_FIELDS` | Static tests compare this file to the constant. |
| Compiler stages | `llmwiki.runtime.ingest_compiler_artifacts._STAGE_ORDER` | Static tests compare this file to the tuple. |
| Compiler artifacts | `llmwiki.runtime.ingest_compiler_artifacts._STAGE_ORDER` | Static tests compare this file to stage outputs. |
| Deterministic artifacts | Strict domain parsers such as `normalized_source_map_from_json` | Parser tests reject wrong shape. |
| Model output | Forge tool DTOs and `ArticleWriter` contracts | Writer tests accept aliases and reject bad model shape. |
| CLI shape | `llmwiki.cli._build_parser` | CLI tests reject removed ingest flags. |
| Public wiki behavior | `SCHEMA.md` | Workflow tests and generated page tests enforce behavior. |

## Page Contract Table

Page kinds:

| PageKind |
|---|
| source |
| entity |
| concept |
| procedure |
| recipe |
| synthesis |

Page families:

| PageFamily |
|---|
| source-manifest |
| source-summary |
| section-reference |
| topic-concept |
| procedure-guide |
| recipe-pattern |
| collection-page |
| broad-topic |
| entity-profile |
| cross-source-synthesis |

Metadata fields:

| MetadataField |
|---|
| PageId |
| PageKind |
| PageFamily |
| Summary |
| Sources |
| Updated |

## Compiler Artifact Table

| Stage | Inputs | Outputs |
|---|---|---|
| source-map | none | normalized-source-map.json |
| source-structure | normalized-source-map | source-structure-integrity.json, source-record-plan.json |
| source-profile | normalized-source-map | source-profile.json, evidence-extraction-plan.json |
| evidence-records | evidence-extraction-plan | evidence-record-set.json |
| page-plan | source-structure-integrity, source-record-plan, evidence-record-set | candidate-admission-report.json, article-viability-report.json, page-publication-plan.json |
| evidence-packs | page-publication-plan | evidence-pack-set.json |
| article-write-queue | evidence-pack-set | article-write-queue-run.json |
| human-articles | article-write-queue-run | human-article-initial.json, human-article-findings-initial.json |
| article-lint | human-article-initial | article-lint-runs-initial.json |
| diagnostics | evidence-pack-set, article-lint-runs-initial | diagnostic-question-set.json, diagnostic-answer-set.json, diagnostic-finding-set.json, diagnostics-report.md |
| repair | diagnostic-finding-set | repair-task-set.json, repair-run.json, human-article.json, human-article-findings.json, article-lint-runs.json |
| staged-publish | article-lint-runs | staged-pages.json, lint-run.json, publish-run.json |

`ingest-artifact-set.json` is the ordered manifest for every compiler run.

## Forbidden Patterns

Active production code must not use these patterns:

| ForbiddenPattern | Reason |
|---|---|
| chunk-derived source authority | `NormalizedSourceMap` is the source-text authority. |
| claim-ledger projection as production ingest | `IngestCompiler` is the ordinary ingest path. |
| page-synthesis public prose | `HumanArticle` is the generated article contract. |
| model-authored markdown or frontmatter | The harness renders markdown and frontmatter. |
| summary-as-evidence | `EvidencePack` carries full source text and payload text. |
| deterministic artifact coercion | Deterministic boundaries fail fast through strict parsers. |
| support IDs without readable evidence context | Public pages must show human-readable source or payload context. |

Deprecated code may remain while the compiler paradigm is validated.
Active compiler, session, and source-resolution code must not point to it.

## Agent Workflow Catalog

| AgentWorkflow | When To Use | Primary Command | Artifacts | Acceptance Signal |
|---|---|---|---|---|
| inspect compiler artifacts | A reingest result needs explanation. | `jq` over `harness/cache/ingest-compiler/<source>/ingest-artifact-set.json` | `ingest-artifact-set.json`, stage outputs | Stage order and findings explain the result. |
| diagnose bad generated page | A wiki page is incoherent or unsupported. | `rg <page_id> harness/cache/ingest-compiler` | evidence pack, human article, article lint | The blocking or accepted support path is visible. |
| debug article writer failures | Generated pages fail before publication. | `uv run pytest harness/tests/test_human_article_renderer.py` | `human-article*.json`, writer findings | Failures are page-scoped writer or validation findings. |
| review source-map quality | Source extraction looks clipped or noisy. | `jq` over `normalized-source-map.json` | source map, source-map findings | Source blocks contain coherent source text and anchors. |
| compare reingests | A change may alter page count or quality. | `uv run llmwiki ingest <source>` | source manifest, log, compiler artifacts | Accepted/rejected counts and top findings are understood. |
| review generated wiki walkability | Navigation or coverage seems weak. | `uv run llmwiki graph --check` | source manifests, index, graph | Accepted pages link from source manifests and index. |

## Update Order

1. Update `docs/domain-vocabulary.md` when a change adds or renames a domain term.
2. Update this file when a change alters a contract surface listed above.
3. Update `SCHEMA.md` when public wiki behavior changes.
4. Update code and tests.
5. Regenerate disposable wiki state when generated page shape changes.

## Three-Pass Validation

1. Contract/static checks: run the relevant contract tests.
2. Unit/integration checks: run `uv --cache-dir /tmp/uv-cache run pytest`.
3. Live reingest comparison: reingest affected sources when ingest output changes.

Always finish implementation work with:

- `uv --cache-dir /tmp/uv-cache run pytest`
- `uv --cache-dir /tmp/uv-cache run ruff check`
- `uv --cache-dir /tmp/uv-cache run mypy harness/src/llmwiki`
