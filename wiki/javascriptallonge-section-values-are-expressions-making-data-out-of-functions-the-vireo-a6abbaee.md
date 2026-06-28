---
page_id: javascriptallonge-section-values-are-expressions-making-data-out-of-functions-the-vireo-a6abbaee
page_kind: source
summary: values are expressions / Making Data Out Of Functions / the vireo: 6 source-backed entries and 1 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-values-are-expressions-making-data-out-of-functions-the-vireo-a6abbaee@df4110112fb3f7861491c2a28fd313b4
---

# values are expressions / Making Data Out Of Functions / the vireo

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-values-are-expressions-making-data-out-of-functions-8e373317]] - broader source section

## Statements

- In both cases, we take two parameters, and return the form of the data. _(javascriptallonge.pdf (source-range-83ecb080-01363))_
- Let’s extract those into parameters: (first, second) => (selector) => selector(first)(second) For consistency with the way combinators are written as functions taking just one parameter, we’ll curry[78] the function: (first) => (second) => (selector) => selector(first)(second) Let’s try it, we’ll use the word pair for the function that makes data (When we need to refer to a specific pair, we’ll use the name aPair by default): **const** first = K, second = K(I), pair = (first) => (second) => (selector) => selector(first)(second); **const** latin = pair("primus")("secundus"); latin(first) _//=> "primus"_ latin(second) _//=> "secundus"_ _(javascriptallonge.pdf (source-range-83ecb080-01364))_
- It says, “take these two values and apply them to this function.” There are other, similar combinators that apply values to functions. _(javascriptallonge.pdf (source-range-83ecb080-01368))_
- One notable example is the “thrush” or T combinator: It takes one value and applies it to a function. _(javascriptallonge.pdf (source-range-83ecb080-01368))_
- It is known to most programmers as .tap. _(javascriptallonge.pdf (source-range-83ecb080-01368))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01364))_

> For “data” we access with K and K(I), our “structure” is the function (selector) => selector("primus")("secundus"). Let’s extract those into parameters: (first, second) => (selector) => selector(first)(second) For consistency with the way combinators are written as functions taking just one parameter, we’ll curry[78] the function: (first) => (second) => (selector) => selector(first)(second) Let’s try it, we’ll use the word pair for the function that makes data (When we need to refer to a specifi

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01365))_

> If we change the names to x, y, and z, we get: (x) => (y) => (z) => z(x)(y).
