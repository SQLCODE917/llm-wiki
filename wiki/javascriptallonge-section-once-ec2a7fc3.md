---
page_id: javascriptallonge-section-once-ec2a7fc3
page_kind: source
summary: Once: 5 source-backed entries and 2 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-once-ec2a7fc3@024613528c2bcd64bfe80ed9a6c7744e
---

# Once

From [[javascriptallonge]].

## Statements

- once is an extremely helpful combinator. It ensures that a function can only be called, well, once . Here's the recipe: _(javascriptallonge.pdf (source-range-8eb13d6b-00710))_
- It ensures that a function can only be called, well, once . _(javascriptallonge.pdf (source-range-8eb13d6b-00710))_

## Technical atoms

### Technical frame 1: Once

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00710))_

> once is an extremely helpful combinator. It ensures that a function can only be called, well, once . Here's the recipe:

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00711))_

```
const once = (fn) => { let done = false ; return function () { return done ? void 0 : ((done = true ), fn.apply( this , arguments)) } }
```

### Technical frame 2: Once

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00710))_

> once is an extremely helpful combinator. It ensures that a function can only be called, well, once . Here's the recipe:

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00713))_

```
const askedOnBlindDate = once( () => "sure, why not?" ); askedOnBlindDate() //=> 'sure, why not?' askedOnBlindDate() //=> undefined askedOnBlindDate() //=> undefined
```
