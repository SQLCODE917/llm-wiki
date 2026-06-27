---
page_id: javascriptallonge-section-function-parameters-are-eager-28366a07
page_kind: source
summary: **function parameters are eager**: 9 source-backed entries and 4 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-function-parameters-are-eager-28366a07@9ce016b360c1dd7d438b7c6f2602237f
---

# **function parameters are eager**

From [[javascriptallonge]].

## Statements

- In contrast to the behaviour of the ternary operator, ||, and &&, function parameters are always : _eagerly evaluated_ _(javascriptallonge.pdf (source-range-83ecb080-01161))_
- In contrast to the behaviour of the ternary operator, ||, and &&, function parameters are always : _eagerly evaluated_ _(javascriptallonge.pdf (source-range-83ecb080-01161))_
- This leads to the infinite recursion we fear. _(javascriptallonge.pdf (source-range-83ecb080-01166))_
- If we need to have functions with control-flow semantics, we can pass anonymous functions. _(javascriptallonge.pdf (source-range-83ecb080-01167))_
- Here we’ve passed functions that contain the expressions we want to evaluate, and now we can write our own functions that can delay evaluation. _(javascriptallonge.pdf (source-range-83ecb080-01171))_

## Technical atoms

### Technical atom 1

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01162))_

> **const** or = (a, b) => a || b

### Technical atom 2

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01163))_

> **const** and = (a, b) => a && b

### Technical atom 3

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01164))_

> **const** even = (n) => or(n === 0, and(n !== 1, even(n - 2)))

### Technical atom 4

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01165))_

> even(42) _//=> Maximum call stack size exceeded._
