---
page_id: javascriptallonge-section-folding-5df7a07c
page_kind: source
summary: **folding**: 15 source-backed entries and 9 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-folding-5df7a07c@fc6f74ae9bd75f94999dde486b5d7459
---

# **folding**

From [[javascriptallonge]].

## Statements

- A function to compute the sum of the squares of a list of numbers might look like this: _(javascriptallonge.pdf (source-range-83ecb080-01369))_
- Let’s rewrite mapWith so that we can use it to sum squares. _(javascriptallonge.pdf (source-range-83ecb080-01378))_
- And now we supply a function that does slightly more than our mapping functions: _(javascriptallonge.pdf (source-range-83ecb080-01380))_
- We can represent a map as a fold, we just need to supply the array rebuilding code: _(javascriptallonge.pdf (source-range-83ecb080-01382))_
- Our foldWith function is a generalization of our mapWith function. _(javascriptallonge.pdf (source-range-83ecb080-01382))_
- And to return to our first example, our version of length can be written as a fold: _(javascriptallonge.pdf (source-range-83ecb080-01389))_

## Technical atoms

> Context: With the exception of the length example at the beginning, our examples so far all involve rebuilding a solution using spreads. But they needn’t. A function to compute the sum of the squares of a list of numbers might look like this:
_(context: javascriptallonge.pdf (source-range-83ecb080-01369))_

> **const** sumSquares = ([first, ...rest]) => first === **undefined**
_(source: javascriptallonge.pdf (source-range-83ecb080-01372))_

> Context: There are two differences between sumSquares and our maps above:
_(context: javascriptallonge.pdf (source-range-83ecb080-01375))_

> sumSquares([1, 2, 3, 4, 5]) _//=> 55_
_(source: javascriptallonge.pdf (source-range-83ecb080-01374))_

> Context: Let’s rewrite mapWith so that we can use it to sum squares.
_(context: javascriptallonge.pdf (source-range-83ecb080-01378))_

> **const** foldWith = (fn, terminalValue, [first, ...rest]) => first === **undefined** ? terminalValue : fn(first, foldWith(fn, terminalValue, rest));
_(source: javascriptallonge.pdf (source-range-83ecb080-01379))_

> Context: And now we supply a function that does slightly more than our mapping functions:
_(context: javascriptallonge.pdf (source-range-83ecb080-01380))_

> foldWith((number, rest) => number * number + rest, 0, [1, 2, 3, 4, 5]) _//=> 55_
_(source: javascriptallonge.pdf (source-range-83ecb080-01381))_

> Context: Our foldWith function is a generalization of our mapWith function. We can represent a map as a fold, we just need to supply the array rebuilding code:
_(context: javascriptallonge.pdf (source-range-83ecb080-01382))_

> **const** squareAll = (array) => foldWith((first, rest) => [first * first, ...rest],\ [], array); squareAll([1, 2, 3, 4, 5]) _//=> [1,4,9,16,25]_
_(source: javascriptallonge.pdf (source-range-83ecb080-01383))_

> Context: And if we like, we can write mapWith using foldWith:
_(context: javascriptallonge.pdf (source-range-83ecb080-01384))_

> **const** mapWith = (fn, array) => foldWith((first, rest) => [fn(first), ...rest], [\ ], array), squareAll = (array) => mapWith((x) => x * x, array);
_(source: javascriptallonge.pdf (source-range-83ecb080-01387))_

> squareAll([1, 2, 3, 4, 5]) _//=> [1,4,9,16,25]_
_(source: javascriptallonge.pdf (source-range-83ecb080-01388))_

> Context: And to return to our first example, our version of length can be written as a fold:
_(context: javascriptallonge.pdf (source-range-83ecb080-01389))_

> **const** length = (array) => foldWith((first, rest) => 1 + rest, 0, array);
_(source: javascriptallonge.pdf (source-range-83ecb080-01390))_

> Context: And to return to our first example, our version of length can be written as a fold:
_(context: javascriptallonge.pdf (source-range-83ecb080-01389))_

> length([1, 2, 3, 4, 5]) _//=> 5_
_(source: javascriptallonge.pdf (source-range-83ecb080-01391))_
