---
page_id: javascriptallonge-section-values-are-expressions-self-similarity-folding-aad20ac1
page_kind: source
summary: values are expressions / Self-Similarity / folding: 5 source-backed entries and 2 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-values-are-expressions-self-similarity-folding-aad20ac1@28487bdaf244ef156871267f321b829d
---

# values are expressions / Self-Similarity / folding

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-values-are-expressions-self-similarity-441bad10]] - broader source section

## Statements

- A function to compute the sum of the squares of a list of numbers might look like this: _(javascriptallonge.pdf (source-range-83ecb080-00934))_
- Let’s rewrite mapWith so that we can use it to sum squares. _(javascriptallonge.pdf (source-range-83ecb080-00941))_
- Our foldWith function is a generalization of our mapWith function. _(javascriptallonge.pdf (source-range-83ecb080-00943))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00934, source-range-83ecb080-00938))_

> With the exception of the length example at the beginning, our examples so far all involve rebuilding a solution using spreads. But they needn’t. A function to compute the sum of the squares of a list of numbers might look like this: There are two differences between sumSquares and our maps above:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00936))_

> 92 **const** sumSquares = ([first, ...rest]) => first === **undefined**

### Technical atom 2

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00934, source-range-83ecb080-00938))_

> With the exception of the length example at the beginning, our examples so far all involve rebuilding a solution using spreads. But they needn’t. A function to compute the sum of the squares of a list of numbers might look like this: There are two differences between sumSquares and our maps above:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00937))_

> ? 0 : first * first + sumSquares(rest); sumSquares([1, 2, 3, 4, 5]) _//=> 55_
