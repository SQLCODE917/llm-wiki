---
page_id: javascriptallonge-section-mapping-c254bfef
page_kind: source
summary: **mapping**: 12 source-backed entries and 5 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-mapping-c254bfef@e8b7eabba77aff568555948885c4d672
---

# **mapping**

From [[javascriptallonge]].

## Statements

- JavaScript has a built-in function for this, but let’s write our own using linear recursion. _(javascriptallonge.pdf (source-range-83ecb080-01353))_
- Another common problem is applying a function to every element of an array. _(javascriptallonge.pdf (source-range-83ecb080-01353))_
- Functions can take functions as arguments, so let’s “extract” the thing to do to each element and separate it from the business of taking an array apart, doing the thing, and putting the array back together. _(javascriptallonge.pdf (source-range-83ecb080-01362))_
- This specific case of linear recursion is called “mapping,” and it is not necessary to constantly write out the same pattern again and again. _(javascriptallonge.pdf (source-range-83ecb080-01362))_
- This specific case of linear recursion is called “mapping,” and it is not necessary to constantly write out the same pattern again and again. _(javascriptallonge.pdf (source-range-83ecb080-01362))_
- We can write it out using a ternary operator. _(javascriptallonge.pdf (source-range-83ecb080-01365))_
- Even in this small function, we can identify the terminal condition, the piece being broken off, and recomposing the solution. _(javascriptallonge.pdf (source-range-83ecb080-01365))_

## Technical atoms

> Context: If we want to square each number in a list, we could write:
_(context: javascriptallonge.pdf (source-range-83ecb080-01354))_

> **const** squareAll = ([first, ...rest]) => first === **undefined** ? [] : [first * first, ...squareAll(rest)\ ]; squareAll([1, 2, 3, 4, 5]) _//=> [1,4,9,16,25]_
_(source: javascriptallonge.pdf (source-range-83ecb080-01355))_

> Context: And if we wanted to “truthify” each element in a list, we could write:
_(context: javascriptallonge.pdf (source-range-83ecb080-01356))_

> **const** truthyAll = ([first, ...rest]) => first === **undefined**
_(source: javascriptallonge.pdf (source-range-83ecb080-01359))_

> truthyAll([ **null** , **true** , 25, **false** , "foo"]) _//=> [false,true,true,false,true]_
_(source: javascriptallonge.pdf (source-range-83ecb080-01361))_

> Context: Given the signature:
_(context: javascriptallonge.pdf (source-range-83ecb080-01363))_

> **const** mapWith = (fn, array) => _// ..._
_(source: javascriptallonge.pdf (source-range-83ecb080-01364))_

> Context: We can write it out using a ternary operator. Even in this small function, we can identify the terminal condition, the piece being broken off, and recomposing the solution.
_(context: javascriptallonge.pdf (source-range-83ecb080-01365))_

> mapWith((x) => !!x, [ **null** , **true** , 25, **false** , "foo"]) _//=> [false,true,true,false,true]_
_(source: javascriptallonge.pdf (source-range-83ecb080-01367))_
