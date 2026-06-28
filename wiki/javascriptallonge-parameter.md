---
page_id: javascriptallonge-parameter
page_kind: concept
summary: Parameter: 4 statement(s) and 2 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-parameter@9c0b2973d525bfb1513457ec3def65e7
---

# Parameter

What [[javascriptallonge]] covers about parameter:

## Statements

- Parameters are declared when we create functions, so it makes sense that parameters are bound to environments created when we invoke functions. _(javascriptallonge.pdf (source-range-83ecb080-00486))_
- Binding values to names with const works just like binding values to names with parameter invocations, it uses lexical scope. _(javascriptallonge.pdf (source-range-83ecb080-00484))_
- Parameters are only bound when we invoke a function. _(javascriptallonge.pdf (source-range-83ecb080-00502))_
- In both cases, we take two parameters, and return the form of the data. _(javascriptallonge.pdf (source-range-83ecb080-01363))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00489))_

> Let’s start, as above, by doing this with parameters. We’ll start with:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00490))_

> ((PI) => (diameter) => diameter * PI )(3.14159265) And gratuitously wrap it in another IIFE so that we can bind PI to something else:

### Technical atom 2

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01364))_

> For “data” we access with K and K(I), our “structure” is the function (selector) => selector("primus")("secundus"). Let’s extract those into parameters: (first, second) => (selector) => selector(first)(second) For consistency with the way combinators are written as functions taking just one parameter, we’ll curry[78] the function: (first) => (second) => (selector) => selector(first)(second) Let’s try it, we’ll use the word pair for the function that makes data (When we need to refer to a specifi

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01365))_

> If we change the names to x, y, and z, we get: (x) => (y) => (z) => z(x)(y).


## Related pages

- [[javascriptallonge-function]] - shared technical atoms (1 shared atom(s))
- [[javascriptallonge-second]] - shared technical atoms (1 shared atom(s))
- [[javascriptallonge-bind]] - shared statements (1 shared statement(s))
- [[javascriptallonge-binding]] - shared statements (1 shared statement(s))
- [[javascriptallonge-const]] - shared statements (1 shared statement(s))
- [[javascriptallonge-lexical-scope]] - shared statements (1 shared statement(s))
- [[javascriptallonge-return]] - shared statements (1 shared statement(s))
- [[javascriptallonge-value]] - shared statements (1 shared statement(s))

## Source

- [[javascriptallonge]]
