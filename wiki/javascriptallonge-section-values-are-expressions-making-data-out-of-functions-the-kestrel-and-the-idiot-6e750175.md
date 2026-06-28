---
page_id: javascriptallonge-section-values-are-expressions-making-data-out-of-functions-the-kestrel-and-the-idiot-6e750175
page_kind: source
summary: values are expressions / Making Data Out Of Functions / the kestrel and the idiot: 14 source-backed entries and 8 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-values-are-expressions-making-data-out-of-functions-the-kestrel-and-the-idiot-6e750175@9c4f989a2755ba90594659350e6b62a4
---

# values are expressions / Making Data Out Of Functions / the kestrel and the idiot

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-values-are-expressions-making-data-out-of-functions-8e373317]] - broader source section

## Statements

- The kestrel, or K, is a function that makes constant functions. _(javascriptallonge.pdf (source-range-83ecb080-01334))_
- You give it a value, and it returns a constant function that gives that value. _(javascriptallonge.pdf (source-range-83ecb080-01334))_
- A _constant function_ is a function that always returns the same thing, no matter what you give it. _(javascriptallonge.pdf (source-range-83ecb080-01334))_
- The _identity function_ is a function that evaluates to whatever parameter you pass it. _(javascriptallonge.pdf (source-range-83ecb080-01336))_
- Given two values, we can say that K always returns the _first_ value: K(x)(y) => x (that’s not valid JavaScript, but it’s essentially how it works). _(javascriptallonge.pdf (source-range-83ecb080-01340))_
- Given two values, we can say that K always returns the _first_ value, and given two values, K(I) always returns the _second_ value. _(javascriptallonge.pdf (source-range-83ecb080-01351))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01334))_

> A _constant function_ is a function that always returns the same thing, no matter what you give it. For example, (x) => 42 is a constant function that always evaluates to 42. The kestrel, or K, is a function that makes constant functions. You give it a value, and it returns a constant function that gives that value.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01335))_

> For example: **const** K = (x) => (y) => x; **const** fortyTwo = K(42); fortyTwo(6) _//=> 42_ fortyTwo("Hello") _//=> 42_

### Technical atom 2

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01338))_

> K(6)(7) _//=> 6_

### Technical atom 3

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01339))_

> K(12)(24) _//=> 12_

### Technical atom 4

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01341))_

> Now, an interesting thing happens when we pass functions to each other. Consider K(I). From what we just wrote, K(x)(y) => x So K(I)(x) => I. Makes sense. Now let’s tack one more invocation on: What is K(I)(x)(y)? If K(I)(x) => I, then K(I)(x)(y) === I(y) which is y.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01342))_

> Therefore, K(I)(x)(y) => y:

### Technical atom 5

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01345))_

> K(I)(6)(7) _//=> 7_

### Technical atom 6

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01346))_

> K(I)(12)(24) _//=> 24_

### Technical atom 7

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01348))_

> K("primus")("secundus") _//=> "primus"_

### Technical atom 8

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01349))_

> K(I)("primus")("secundus") _//=> "secundus"_
