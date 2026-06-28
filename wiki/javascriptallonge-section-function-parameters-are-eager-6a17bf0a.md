---
page_id: javascriptallonge-section-function-parameters-are-eager-6a17bf0a
page_kind: source
summary: function parameters are eager: 6 source-backed entries and 2 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-function-parameters-are-eager-6a17bf0a@7298232a0218f540d126898e881357da
---

# function parameters are eager

From [[javascriptallonge]].

## Statements

- In contrast to the behaviour of the ternary operator, || , and && , function parameters are always eagerly evaluated : _(javascriptallonge.pdf (source-range-31a4cf47-00801))_
- If we need to have functions with control-flow semantics, we can pass anonymous functions. We obviously don't need anything like this for or and and , but to demonstrate the technique: _(javascriptallonge.pdf (source-range-31a4cf47-00804))_
- Here we've passed functions that contain the expressions we want to evaluate, and now we can write our own functions that can delay evaluation. _(javascriptallonge.pdf (source-range-31a4cf47-00806))_
- In contrast to the behaviour of the ternary operator, || , and && , function parameters are always eagerly evaluated : _(javascriptallonge.pdf (source-range-31a4cf47-00801))_

## Technical atoms

### Technical frame 1: function parameters are eager

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00804))_

> If we need to have functions with control-flow semantics, we can pass anonymous functions. We obviously don't need anything like this for or and and , but to demonstrate the technique:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00802))_

```
const or = (a, b) => a || b const and = (a, b) => a && b const even = (n) => or(n === 0, and(n !== 1, even(n - 2))) even(42) //=> Maximum call stack size exceeded.
```

### Technical frame 2: function parameters are eager

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00806))_

> Here we've passed functions that contain the expressions we want to evaluate, and now we can write our own functions that can delay evaluation.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00805))_

```
const or = (a, b) => a() || b() const and = (a, b) => a() && b() const even = (n) => or(() => n === 0, () => and(() => n !== 1, () => even(n - 2))) even(7) //=> false
```
