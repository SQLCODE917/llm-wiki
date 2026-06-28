---
page_id: javascriptallonge-section-values-are-expressions-unary-b96fc1ec
page_kind: source
summary: values are expressions / Unary: 12 source-backed entries and 3 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-values-are-expressions-unary-b96fc1ec@3793760b55c16cc8710b069046fcbe7c
---

# values are expressions / Unary

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-values-are-expressions-4763e204]] - broader source section

## Statements

- “Unary” is a function decorator that modifies the number of arguments a function takes: Unary takes any function and turns it into a function taking exactly one argument. _(javascriptallonge.pdf (source-range-83ecb080-00687))_
- The most common use case is to fix a problem. _(javascriptallonge.pdf (source-range-83ecb080-00688))_
- JavaScript has a .map method for arrays, and many libraries offer a map function with the same semantics. _(javascriptallonge.pdf (source-range-83ecb080-00688))_
- But some functions have optional second or even third arguments. _(javascriptallonge.pdf (source-range-83ecb080-00691))_
- What we want is to convert parseInt into a function taking only one argument. _(javascriptallonge.pdf (source-range-83ecb080-00692))_
- And when you call parseInt with map, the index is interpreted as a radix. _(javascriptallonge.pdf (source-range-83ecb080-00692))_
- ['1', '2', '3'].map(parseInt) _//=> [1, NaN, NaN]_ This doesn’t work because parseInt is defined as parseInt(string[, radix]). _(javascriptallonge.pdf (source-range-83ecb080-00692))_
- ['1', '2', '3'].map(parseInt) _//=> [1, NaN, NaN]_ This doesn’t work because parseInt is defined as parseInt(string[, radix]). _(javascriptallonge.pdf (source-range-83ecb080-00692))_
- What we want is to convert parseInt into a function taking only one argument. _(javascriptallonge.pdf (source-range-83ecb080-00692))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00692))_

> ['1', '2', '3'].map(parseInt) _//=> [1, NaN, NaN]_ This doesn’t work because parseInt is defined as parseInt(string[, radix]). It takes an optional radix argument. And when you call parseInt with map, the index is interpreted as a radix. Not good! What we want is to convert parseInt into a function taking only one argument.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00693))_

> We could write ['1', '2', '3'].map((s) => parseInt(s)), or we could come up with a decorator to do the job for us:

### Technical atom 2

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00693))_

> We could write ['1', '2', '3'].map((s) => parseInt(s)), or we could come up with a decorator to do the job for us:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00695))_

> 60 **const** unary = (fn) => fn.length === 1

### Technical atom 3

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00696))_

> ? fn : **function** (something) { **return** fn.call( **this** , something) } And now we can write:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00697))_

> ['1', '2', '3'].map(unary(parseInt)) _//=> [1, 2, 3]_ Presto!
