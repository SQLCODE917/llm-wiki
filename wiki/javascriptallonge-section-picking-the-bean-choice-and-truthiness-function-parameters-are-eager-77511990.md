---
page_id: javascriptallonge-section-picking-the-bean-choice-and-truthiness-function-parameters-are-eager-77511990
page_kind: source
page_family: section-reference
summary: Picking the Bean: Choice and Truthiness / function parameters are eager: 6 source-backed entries and 1 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-picking-the-bean-choice-and-truthiness-function-parameters-are-eager-77511990@cbdbf6d97057e6d4358b60d4cc94bad3
---

# Picking the Bean: Choice and Truthiness / function parameters are eager

From [[javascriptallonge]].

## Related pages

### Source structure

- [[javascriptallonge-section-picking-the-bean-choice-and-truthiness-d45c6f89]] - broader source section: Picking the Bean: Choice and Truthiness

## Statements

- In contrast to the behaviour of the ternary operator, || , and && , function parameters are always eagerly evaluated : _(javascriptallonge.pdf (source-range-7239e085-00801))_
- If we need to have functions with control-flow semantics, we can pass anonymous functions. We obviously don't need anything like this for or and and , but to demonstrate the technique: _(javascriptallonge.pdf (source-range-7239e085-00804))_
- Here we've passed functions that contain the expressions we want to evaluate, and now we can write our own functions that can delay evaluation. _(javascriptallonge.pdf (source-range-7239e085-00806))_
- In contrast to the behaviour of the ternary operator, || , and && , function parameters are always eagerly evaluated : _(javascriptallonge.pdf (source-range-7239e085-00801))_

## Technical atoms

### Technical frame 1: Picking the Bean: Choice and Truthiness / function parameters are eager

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00804))_

> If we need to have functions with control-flow semantics, we can pass anonymous functions. We obviously don't need anything like this for or and and , but to demonstrate the technique:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00802))_

<a id="atom-technical-atom-f6692ca904d56bf1"></a>

```
const or = (a, b) => a || b
const and = (a, b) => a && b
const even = (n) =>
or(n === 0, and(n !== 1, even(n - 2)))
even(42)
//=> Maximum call stack size exceeded.
```
