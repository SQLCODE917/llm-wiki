---
page_id: javascriptallonge-section-unary-e9640160
page_kind: source
summary: Unary: 16 source-backed entries and 7 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-unary-e9640160@81d7b9e4683737a686cc149f9ecc7866
---

# Unary

From [[javascriptallonge]].

## Statements

- “Unary” is a function decorator that modifies the number of arguments a function takes: Unary takes any function and turns it into a function taking exactly one argument. _(javascriptallonge.pdf (source-range-83ecb080-00955))_
- JavaScript has a .map method for arrays, and many libraries offer a map function with the same semantics. _(javascriptallonge.pdf (source-range-83ecb080-00956))_
- The most common use case is to fix a problem. _(javascriptallonge.pdf (source-range-83ecb080-00956))_
- But some functions have optional second or even third arguments. _(javascriptallonge.pdf (source-range-83ecb080-00961))_
- And when you call parseInt with map, the index is interpreted as a radix. _(javascriptallonge.pdf (source-range-83ecb080-00963))_
- What we want is to convert parseInt into a function taking only one argument. _(javascriptallonge.pdf (source-range-83ecb080-00963))_
- What we want is to convert parseInt into a function taking only one argument. _(javascriptallonge.pdf (source-range-83ecb080-00963))_
- This doesn’t work because parseInt is defined as parseInt(string[, radix]). _(javascriptallonge.pdf (source-range-83ecb080-00963))_
- This doesn’t work because parseInt is defined as parseInt(string[, radix]). _(javascriptallonge.pdf (source-range-83ecb080-00963))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00956))_

> The most common use case is to fix a problem. JavaScript has a .map method for arrays, and many libraries offer a map function with the same semantics. Here it is in action:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00957))_

> ['1', '2', '3'].map(parseFloat) _//=> [1, 2, 3]_

### Technical atom 2

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00959, source-range-83ecb080-00963))_

> Let’s try it: This doesn’t work because parseInt is defined as parseInt(string[, radix]). It takes an optional radix argument. And when you call parseInt with map, the index is interpreted as a radix. Not good! What we want is to convert parseInt into a function taking only one argument.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00961))_

> If you pass in a function taking only one argument, it simply ignores the additional arguments.

### Technical atom 3

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00961, source-range-83ecb080-00963))_

> If you pass in a function taking only one argument, it simply ignores the additional arguments. But some functions have optional second or even third arguments. For example: This doesn’t work because parseInt is defined as parseInt(string[, radix]). It takes an optional radix argument. And when you call parseInt with map, the index is interpreted as a radix. Not good! What we want is to convert parseInt into a function taking only one argument.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00962))_

> ['1', '2', '3'].map(parseInt) _//=> [1, NaN, NaN]_

### Technical atom 4

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00963))_

> This doesn’t work because parseInt is defined as parseInt(string[, radix]). It takes an optional radix argument. And when you call parseInt with map, the index is interpreted as a radix. Not good! What we want is to convert parseInt into a function taking only one argument.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00964))_

> We could write ['1', '2', '3'].map((s) => parseInt(s)), or we could come up with a decorator to do the job for us:

### Technical atom 5

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00964))_

> We could write ['1', '2', '3'].map((s) => parseInt(s)), or we could come up with a decorator to do the job for us:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00967))_

> **const** unary = (fn) =>

### Technical atom 6

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00968))_

> fn.length === 1

### Technical atom 7

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00970))_

> And now we can write:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00971))_

> ['1', '2', '3'].map(unary(parseInt)) _//=> [1, 2, 3]_
