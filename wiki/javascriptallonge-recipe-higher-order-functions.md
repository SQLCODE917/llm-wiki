---
page_id: javascriptallonge-recipe-higher-order-functions
page_kind: recipe
page_family: recipe-pattern
summary: higher-order functions: reusable source-backed pattern with 2 statement(s) and 1 technical atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: higher-order-functions
projection_coverage: recipe-javascriptallonge-recipe-higher-order-functions@fbed3b148207ca9bcd12d3e1eaaa3203
---

# higher-order functions

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-and-also-combinators-and-function-decorators-higher-order-functions-21afd32c]].
- Evidence roles: decision, constraint, example.

## Applicability And Rationale

- JavaScript functions are values, so JavaScript functions can take functions as arguments, return functions, or both. _(javascriptallonge.pdf (source-range-7239e085-00557))_
- Generally speaking, a function that either takes functions as arguments, or returns a function, or both, is referred to as a 'higher-order' function. _(javascriptallonge.pdf (source-range-7239e085-00557))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00559)_

```
const repeat = (num, fn) =>
(num > 0)
? (repeat(num - 1, fn), fn(num))
: undefined
repeat(3, function (n) {
console.log(`Hello ${n}`)
})
//=>
'Hello 1'
'Hello 2'
'Hello 3'
undefined
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-and-also-combinators-and-function-decorators-higher-order-functions-21afd32c]]
