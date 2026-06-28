---
page_id: javascriptallonge-section-values-are-expressions-flip-552b12dc
page_kind: source
summary: values are expressions / Flip: 9 source-backed entries and 3 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-values-are-expressions-flip-552b12dc@16558e84539e1e6953e590212415420a
---

# values are expressions / Flip

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-values-are-expressions-4763e204]] - broader source section
- [[javascriptallonge-section-values-are-expressions-flip-self-currying-flip-2c65590b]] - narrower source section
- [[javascriptallonge-section-values-are-expressions-flip-flipping-methods-8649199c]] - narrower source section

## Statements

- Let’s consider the case whether we have a map function of our own, perhaps from the allong.es[84] library, perhaps from Underscore[85] . _(javascriptallonge.pdf (source-range-83ecb080-01448))_
- What we have now is a function that takes a function and “flips” the order of arguments around, then curries it. _(javascriptallonge.pdf (source-range-83ecb080-01453))_
- What we have now is a function that takes a function and “flips” the order of arguments around, then curries it. _(javascriptallonge.pdf (source-range-83ecb080-01453))_
- Consider how we define mapWith now: **var** mapWith = flipAndCurry(map); _(javascriptallonge.pdf (source-range-83ecb080-01459))_

## Statements by subsection

### values are expressions / Flip / self-currying flip

- Sometimes we’ll want to flip a function, but retain the flexibility to call it in its curried form (pass one parameter) or non-curried form (pass both). _(javascriptallonge.pdf (source-range-83ecb080-01462))_

### values are expressions / Flip / flipping methods

- When we learn about context and methods, we’ll see that flip throws the current context away, so it can’t be used to flip methods. _(javascriptallonge.pdf (source-range-83ecb080-01465))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01448))_

> Let’s consider the case whether we have a map function of our own, perhaps from the allong.es[84] library, perhaps from Underscore[85] . We could write our function something like this: **const** mapWith = (fn) => (list) => map(list, fn);

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01449))_

> You can see that if we simplify it: **const** mapWith = (fn, list) => map(list, fn);

### Technical atom 2

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01457))_

> 173 **const** flipAndCurry = (fn) => (first) => (second) => fn(second, first);

### Technical atom 3

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01463))_

> Now if we write mapWith = flip(map), we can call mapWith(fn, list) or mapWith(fn)(list), our choice.
