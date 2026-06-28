---
page_id: javascriptallonge-section-values-are-expressions-once-6fc90212
page_kind: source
summary: values are expressions / Once: 4 source-backed entries and 1 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-values-are-expressions-once-6fc90212@42f9d407a9843fe70f9c4af999b6d4c3
---

# values are expressions / Once

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-values-are-expressions-4763e204]] - broader source section

## Statements

- once is an extremely helpful combinator. _(javascriptallonge.pdf (source-range-83ecb080-00723))_
- It ensures that a function can only be called, well, _once_ . _(javascriptallonge.pdf (source-range-83ecb080-00723))_
- It ensures that a function can only be called, well, _once_ . _(javascriptallonge.pdf (source-range-83ecb080-00723))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00723))_

> once is an extremely helpful combinator. It ensures that a function can only be called, well, _once_ . Here’s the recipe: **const** once = (fn) => { **let** done = **false** ; **return function** () { **return** done ? **void** 0 : ((done = **true** ), fn.apply( **this** , arguments)) } } Very simple! You pass it a function, and you get a function back. That function will call your function once, and thereafter will return undefined whenever it is called. Let’s try it: **const** askedOnBlindDate

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00724))_

> askedOnBlindDate() _//=> undefined_ askedOnBlindDate() _//=> undefined_
