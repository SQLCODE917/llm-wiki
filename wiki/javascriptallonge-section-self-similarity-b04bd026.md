---
page_id: javascriptallonge-section-self-similarity-b04bd026
page_kind: source
page_family: section-reference
summary: Self-Similarity: 5 source-backed entries and 0 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-03
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-self-similarity-b04bd026@f99c2a5b0e30dbbd34598a0978866c8e
---

# Self-Similarity

From [[javascriptallonge]].

## Statements

- 93 

Composing and Decomposing Data 

**const** mapWith = (fn, array) => foldWith((first, rest) => [fn(first), ...rest], [\ ], array), squareAll = (array) => mapWith((x) => x * x, array); 

squareAll([1, 2, 3, 4, 5]) _//=> [1,4,9,16,25]_ 

And to return to our first example, our version of length can be written as a fold: 

**const** length = (array) => foldWith((first, rest) => 1 + rest, 0, array); 

length([1, 2, 3, 4, 5]) _//=> 5_ 

## **summary** 

Linear recursion is a basic building block of algorithms. Its basic form parallels the way linear data structures like lists are constructed: This helps make it understandable. Its specialized cases of mapping and folding are especially useful and can be used to build other functions. And finally, while folding is a special case of linear recursion, mapping is a special case of folding. _(javascriptallonge.pdf (source-range-af806fb1-00131))_
