# Page Body Contracts

`PageBodyContract` values define the deterministic shape checks for model-written
`PageBody` text. `Schema` owns reusable contracts. `SourcePlan` may select or
override a contract for one source run. `PagePlan` resolves those choices into a
`ResolvedPageBodyContract` on each `PlannedPageWrite`.

`RawSource` never stores contract choices; it remains immutable evidence.

## Local Defaults

| Contract | Default PageKind | Purpose |
|---|---|---|
| `source-summary` | `source` | Compact, claim-oriented source page. |
| `entity-page` | `entity` | Concise page for a named object, person, place, system, or organization. |
| `concept-page` | `concept` | Concise page for one idea, rule, theme, or pattern. |
| `synthesis-page` | `synthesis` | Cross-source answer, comparison, or analysis. |

`source-summary` requires `Source record` and `Key supported claims` sections,
at least three claim bullets, source citations, planned related links when any
exist, source uncertainty terms when present, and compact paraphrase limits.

Example source body:

```markdown
## Source record

Source record for [[antikythera-mechanism]]. The source may remain uncertain.
(raw/antikythera-mechanism.md)

## Key supported claims

- The source supports an astronomical interpretation. (raw/antikythera-mechanism.md)
- The source preserves possible functions without resolving them. (raw/antikythera-mechanism.md)
- The source records open provenance limits. (raw/antikythera-mechanism.md)
```

## Custom Contracts

Custom contracts are domain data, not pipeline branches. Add them to `Schema`
and select them through `SourcePlanContractSelection`. Config-file loading can
be layered on later without changing the validator or planned write tool.

Architecture example:

```python
from llmwiki.domain.objects import RawSource, Schema, SourcePlan
from llmwiki.domain.page_body_contracts import (
    PageBodyContract,
    SourcePlanContractSelection,
)

raw_source = RawSource.from_locator("lcn-4040xp.md")
architecture_contract = PageBodyContract(
    contract_id="architecture-product-page",
    match_page_kinds=("entity",),
    required_sections=("Applications", "Limitations", "Open items"),
    max_words=260,
    required_citation_policy="all-raw-sources",
)

schema = Schema(page_body_contracts=Schema().page_body_contracts + (architecture_contract,))
source_plan = SourcePlan(
    raw_source=raw_source,
    source_classification="product literature",
    ingest_disposition="plan-pages",
    page_body_contract_selections=(
        SourcePlanContractSelection(
            contract_id="architecture-product-page",
            page_ids=("lcn-4040xp",),
            max_words_override=220,
        ),
    ),
)
```

Physics example:

```python
from llmwiki.domain.objects import RawSource, SourcePlan
from llmwiki.domain.page_body_contracts import (
    PageBodyContract,
    SourcePlanContractSelection,
)

raw_source = RawSource.from_locator("lagrangian-notes.md")
theorem_contract = PageBodyContract(
    contract_id="physics-theorem-page",
    match_page_kinds=("concept",),
    required_sections=("Statement", "Assumptions", "Evidence", "Limits"),
    max_words=360,
    required_uncertainty_policy="preserve-source-uncertainty",
)

source_plan = SourcePlan(
    raw_source=raw_source,
    source_classification="physics notes",
    ingest_disposition="plan-pages",
    page_body_contract_selections=(
        SourcePlanContractSelection(
            contract_id="physics-theorem-page",
            match_page_kinds=("concept",),
        ),
    ),
)
```
