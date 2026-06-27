---
page_id: javascriptallonge-section-function-decorators-a17cb157
page_kind: source
summary: **function decorators**: 11 source-backed entries and 4 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-function-decorators-a17cb157@7947fdfd721e3f7fa4ccbd5c8b63d1be
---

# **function decorators**

From [[javascriptallonge]].

## Statements

- A _function decorator_ is a higher-order function that takes one function as an argument, returns another function, and the returned function is a variation of the argument function. _(javascriptallonge.pdf (source-range-83ecb080-00807))_
- > 37As we’ll discuss later, this implementation of the B Combinator is correct in languages like Scheme, but for truly general-purpose use in JavaScript, it needs to correctly manage the function context. _(javascriptallonge.pdf (source-range-83ecb080-00808))_
- > 38 We’ll see later why an even more useful version would be written (fn) => (...args) => !fn(...args) _(javascriptallonge.pdf (source-range-83ecb080-00809))_
- So instead of writing !someFunction(42), we can write not(someFunction)(42). _(javascriptallonge.pdf (source-range-83ecb080-00813))_
- Function decorators aren’t strict about being pure functions, so there’s more latitude for making decorators than combinators. _(javascriptallonge.pdf (source-range-83ecb080-00819))_
- not is a function decorator because it modifies a function while remaining strongly related to the original function’s semantics. _(javascriptallonge.pdf (source-range-83ecb080-00819))_
- not is a function decorator because it modifies a function while remaining strongly related to the original function’s semantics. _(javascriptallonge.pdf (source-range-83ecb080-00819))_

## Technical atoms

### Technical atom 1

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00812))_

> **const** not = (fn) => (x) => !fn(x)

### Technical atom 2

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00813))_

> So instead of writing !someFunction(42), we can write not(someFunction)(42). Hardly progress. But like compose, we could write either:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00814))_

> **const** something = (x) => x != **null** ;

### Technical atom 3

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00815))_

> And elsewhere, write:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00816))_

> **const** nothing = (x) => !something(x);

### Technical atom 4

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00817, source-range-83ecb080-00819))_

> Or we could write: not is a function decorator because it modifies a function while remaining strongly related to the original function’s semantics. You’ll see other function decorators in the recipes, like once and maybe. Function decorators aren’t strict about being pure functions, so there’s more latitude for making decorators than combinators.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00818))_

> **const** nothing = not(something);
