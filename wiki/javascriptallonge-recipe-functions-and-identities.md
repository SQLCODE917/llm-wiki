---
page_id: javascriptallonge-recipe-functions-and-identities
page_kind: recipe
page_family: recipe-pattern
summary: functions and identities: reusable source-backed pattern with 3 statement(s) and 1 technical atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: functions-and-identities
projection_coverage: recipe-javascriptallonge-recipe-functions-and-identities@40fbd04b86a24d03037a0643d9ef268a
---

# functions and identities

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-the-first-sip-basic-functions-as-little-as-possible-about-functions-but-no-less-functions-and-id-04ebbc48]].
- Evidence roles: decision, example.

## Applicability And Rationale

- Value types share the same identity if they have the same contents. _(javascriptallonge.pdf (source-range-7239e085-00176))_
- Reference types do not. _(javascriptallonge.pdf (source-range-7239e085-00176))_
- You recall that we have two types of values with respect to identity: Value types and reference types. _(javascriptallonge.pdf (source-range-7239e085-00176))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00178)_

```
(() => 0) === (() => 0)
//=> false
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-the-first-sip-basic-functions-as-little-as-possible-about-functions-but-no-less-functions-and-id-04ebbc48]]
