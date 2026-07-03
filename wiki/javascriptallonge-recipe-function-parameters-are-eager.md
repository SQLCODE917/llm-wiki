---
page_id: javascriptallonge-recipe-function-parameters-are-eager
page_kind: recipe
page_family: recipe-pattern
summary: function parameters are eager: reusable source-backed pattern with 3 statement(s) and 2 technical atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: function-parameters-are-eager
projection_coverage: recipe-javascriptallonge-recipe-function-parameters-are-eager@08eebe06474e914163b97a797c5811a1
---

# function parameters are eager

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-picking-the-bean-choice-and-truthiness-function-parameters-are-eager-77511990]].
- Evidence roles: decision, explanation, constraint, example.

## Applicability And Rationale

- In contrast to the behaviour of the ternary operator, || , and && , function parameters are always eagerly evaluated : _(javascriptallonge.pdf (source-range-7239e085-00801))_
- If we need to have functions with control-flow semantics, we can pass anonymous functions. _(javascriptallonge.pdf (source-range-7239e085-00804))_
- Here we've passed functions that contain the expressions we want to evaluate, and now we can write our own functions that can delay evaluation. _(javascriptallonge.pdf (source-range-7239e085-00806))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00802)_

```
const or = (a, b) => a || b
const and = (a, b) => a && b
const even = (n) =>
or(n === 0, and(n !== 1, even(n - 2)))
even(42)
//=> Maximum call stack size exceeded.
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00805)_

```
const or = (a, b) => a() || b()
const and = (a, b) => a() && b()
const even = (n) =>
or(() => n === 0, () => and(() => n !== 1, () => even(n - 2)))
even(7)
//=> false
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-picking-the-bean-choice-and-truthiness-function-parameters-are-eager-77511990]]
