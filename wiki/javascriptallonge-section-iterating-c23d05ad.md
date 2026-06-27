---
page_id: javascriptallonge-section-iterating-c23d05ad
page_kind: source
summary: **iterating**: 16 source-backed entries and 4 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-iterating-c23d05ad@18d5d01df011690eea761c80eeb337ff
---

# **iterating**

From [[javascriptallonge]].

## Statements

- Nevertheless, there is some value in being able to express some algorithms as iteration. _(javascriptallonge.pdf (source-range-83ecb080-01960))_
- Folding is a universal operation, and with care we can accomplish any task with folds that could be accomplished with that stalwart of structured programming, the for loop. _(javascriptallonge.pdf (source-range-83ecb080-01960))_
- JavaScript has a particularly low-level version of for loop that mimics the semantics of the C language. _(javascriptallonge.pdf (source-range-83ecb080-01961))_
- And worst of all, we’re getting really low-level with details like knowing that the elements of an array are indexed with consecutive integers that begin with 0. _(javascriptallonge.pdf (source-range-83ecb080-01963))_
- Notice that buried inside our loop, we have bound the names done and value. _(javascriptallonge.pdf (source-range-83ecb080-01966))_
- We can put those into a POJO (a Plain Old JavaScript Object). _(javascriptallonge.pdf (source-range-83ecb080-01966))_
- Notice that buried inside our loop, we have bound the names done and value. _(javascriptallonge.pdf (source-range-83ecb080-01966))_
- All the summing code needs to know is to add eachIteration.value. _(javascriptallonge.pdf (source-range-83ecb080-01970))_
- With this code, we make a POJO that has done and value keys. _(javascriptallonge.pdf (source-range-83ecb080-01970))_
- Now this is something else. _(javascriptallonge.pdf (source-range-83ecb080-01976))_
- The arrayIterator function takes an array and returns a function we can call repeatedly to obtain the elements of the array. _(javascriptallonge.pdf (source-range-83ecb080-01976))_
- We can write a different iterator for a different data structure. _(javascriptallonge.pdf (source-range-83ecb080-01977))_

## Technical atoms

> sum += eachIteration.value; } **return** sum; }
_(source: javascriptallonge.pdf (source-range-83ecb080-01974))_

> iteratorSum(arrayIterator([1, 4, 9, 16, 25])) _//=> 55_
_(source: javascriptallonge.pdf (source-range-83ecb080-01975))_

> **while** ((eachIteration = iterator(), !eachIteration.done)) { sum += eachIteration.value; } **return** sum }
_(source: javascriptallonge.pdf (source-range-83ecb080-01982))_

> **const** aListIterator = listIterator(list(1, 4, 9, 16, 25));
_(source: javascriptallonge.pdf (source-range-83ecb080-01983))_
