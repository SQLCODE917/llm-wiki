---
page_id: javascriptallonge-section-function-parameters-are-eager-28366a07
page_kind: source
summary: **function parameters are eager**: 9 source-backed entries and 4 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-function-parameters-are-eager-28366a07@90b5c9af7df9d0aa012d8fd4686533e2
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

> **const** or = (a, b) => a || b
_(source: javascriptallonge.pdf (source-range-83ecb080-01162))_

> **const** and = (a, b) => a && b
_(source: javascriptallonge.pdf (source-range-83ecb080-01163))_

> **const** even = (n) => or(n === 0, and(n !== 1, even(n - 2)))
_(source: javascriptallonge.pdf (source-range-83ecb080-01164))_

> even(42) _//=> Maximum call stack size exceeded._
_(source: javascriptallonge.pdf (source-range-83ecb080-01165))_
