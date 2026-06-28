---
page_id: javascriptallonge-section-values-are-expressions-interactive-generators-representing-naughts-and-crosses-as-a-stateless-fu-a61e15d9
page_kind: source
summary: values are expressions / Interactive Generators / representing naughts and crosses as a stateless function: 5 source-backed entries and 1 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-values-are-expressions-interactive-generators-representing-naughts-and-crosses-as-a-stateless-fu-a61e15d9@77184db4ae5c20cb3f3054264274ce0a
---

# values are expressions / Interactive Generators / representing naughts and crosses as a stateless function

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-values-are-expressions-interactive-generators-90df6a1c]] - broader source section

## Statements

- We could plays naughts and crosses as a stateless function. _(javascriptallonge.pdf (source-range-83ecb080-01888))_
- We can encode the board in several different ways. _(javascriptallonge.pdf (source-range-83ecb080-01893))_
- [ 'o', 'x', ' ', 'x', ' ', ' ', 'o', ' ', ' ' ] We can use a POJO to make a map from positions to moves. _(javascriptallonge.pdf (source-range-83ecb080-01900))_
- We’ll use the [] notation for keys, it allows us to use any expression as a key, and JavaScript will convert it to a string. _(javascriptallonge.pdf (source-range-83ecb080-01900))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01902))_

> { "o,x, , , , , , , ":6, "o,x,x, , , ,o, , ":3, "o,x, ,x, , ,o, , ":8, "o,x, , ,x, ,o, , ":3, "o,x, , , ,x,o, , ":3, "o,x, , , , ,o,x, ":3, "o,x, , , , ,o, ,x":3 } And if we want to look up what move to make, we can write: moveLookupTable[[ 'o', 'x', ' ', ' ' ' ' ' ' , , , 'o', 'x', ' ' _//=> 3_ ]] And from there, a stateless function to play naughts-and-crosses is trivial:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01904))_

> 256 statelessNaughtsAndCrosses([ 'o', 'x', ' ', ' ' ' ' ' ' , , , 'o', 'x', ' ' ]) _//=> 3_
