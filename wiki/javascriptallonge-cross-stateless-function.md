---
page_id: javascriptallonge-cross-stateless-function
page_kind: concept
summary: Cross Stateless Function: 1 statement(s) and 1 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-cross-stateless-function@d251a86bda77a2efcfe0bf7083f4cc6e
---

# Cross Stateless Function

What [[javascriptallonge]] covers about cross stateless function:

## Statements

- We could plays naughts and crosses as a stateless function. _(javascriptallonge.pdf (source-range-83ecb080-01888))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01902))_

> { "o,x, , , , , , , ":6, "o,x,x, , , ,o, , ":3, "o,x, ,x, , ,o, , ":8, "o,x, , ,x, ,o, , ":3, "o,x, , , ,x,o, , ":3, "o,x, , , , ,o,x, ":3, "o,x, , , , ,o, ,x":3 } And if we want to look up what move to make, we can write: moveLookupTable[[ 'o', 'x', ' ', ' ' ' ' ' ' , , , 'o', 'x', ' ' _//=> 3_ ]] And from there, a stateless function to play naughts-and-crosses is trivial:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01904))_

> 256 statelessNaughtsAndCrosses([ 'o', 'x', ' ', ' ' ' ' ' ' , , , 'o', 'x', ' ' ]) _//=> 3_


## Related pages

- [[javascriptallonge-function]] - broader topic (1 shared atom(s))
- [[javascriptallonge-representing-naught]] - shared statements and technical atoms (1 shared statement(s), 1 shared atom(s))

## Source

- [[javascriptallonge]]
