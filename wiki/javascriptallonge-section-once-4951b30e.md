---
page_id: javascriptallonge-section-once-4951b30e
page_kind: source
summary: Once: 5 source-backed entries and 2 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-once-4951b30e@8c6c6e4a6c767d9c22ae334d6052d3ab
---

# Once

From [[javascriptallonge]].

## Statements

- once is an extremely helpful combinator. It ensures that a function can only be called, well, once . Here's the recipe: _(javascriptallonge.pdf (source-range-31a4cf47-00710))_
- It ensures that a function can only be called, well, once . _(javascriptallonge.pdf (source-range-31a4cf47-00710))_

## Technical atoms

### Technical frame 1: Once

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00710))_

> once is an extremely helpful combinator. It ensures that a function can only be called, well, once . Here's the recipe:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00711))_

```
const once = (fn) => { let done = false ; return function () { return done ? void 0 : ((done = true ), fn.apply( this , arguments)) } }
```

### Technical frame 2: Once

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00710))_

> once is an extremely helpful combinator. It ensures that a function can only be called, well, once . Here's the recipe:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00713))_

```
const askedOnBlindDate = once( () => "sure, why not?" ); askedOnBlindDate() //=> 'sure, why not?' askedOnBlindDate() //=> undefined askedOnBlindDate() //=> undefined
```
