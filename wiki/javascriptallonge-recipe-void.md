---
page_id: javascriptallonge-recipe-void
page_kind: recipe
page_family: recipe-pattern
summary: void: reusable source-backed pattern with 4 statement(s) and 1 technical atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: void
projection_coverage: recipe-javascriptallonge-recipe-void@ff78e2a3e25b599ac8b8b2e58730b2c6
---

# void

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-or-even-void-8a19170f]].
- Evidence roles: decision, example.

## Applicability And Rationale

- We've seen that JavaScript represents an undefined value by typing undefined , and we've generated undefined values in two ways: _(javascriptallonge.pdf (source-range-7239e085-00226))_
- - By writing undefined ourselves. _(javascriptallonge.pdf (source-range-7239e085-00228))_
- The first form works but it's cumbersome. _(javascriptallonge.pdf (source-range-7239e085-00232))_
- The second form works most of the time, but it is possible to break it by reassigning undefined to a different value, something we'll discuss in Reassignment and Mutation. _(javascriptallonge.pdf (source-range-7239e085-00232))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00230)_

```
void 0
//=> undefined
void 1
//=> undefined
void (2 + 2)
//=> undefined
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-or-even-void-8a19170f]]
