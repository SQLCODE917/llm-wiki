---
page_id: javascriptallonge-section-folding-5df7a07c
page_kind: source
summary: **folding**: 15 source-backed entries and 9 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-folding-5df7a07c@485fd134addd742981d9f9a527c808ab
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

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01369))_

> With the exception of the length example at the beginning, our examples so far all involve rebuilding a solution using spreads. But they needn’t. A function to compute the sum of the squares of a list of numbers might look like this:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01372))_

> **const** sumSquares = ([first, ...rest]) => first === **undefined**

### Technical atom 2

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01375))_

> There are two differences between sumSquares and our maps above:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01374))_

> sumSquares([1, 2, 3, 4, 5]) _//=> 55_

### Technical atom 3

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01378))_

> Let’s rewrite mapWith so that we can use it to sum squares.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01379))_

> **const** foldWith = (fn, terminalValue, [first, ...rest]) => first === **undefined** ? terminalValue : fn(first, foldWith(fn, terminalValue, rest));

### Technical atom 4

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01380))_

> And now we supply a function that does slightly more than our mapping functions:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01381))_

> foldWith((number, rest) => number * number + rest, 0, [1, 2, 3, 4, 5]) _//=> 55_

### Technical atom 5

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01382))_

> Our foldWith function is a generalization of our mapWith function. We can represent a map as a fold, we just need to supply the array rebuilding code:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01383))_

> **const** squareAll = (array) => foldWith((first, rest) => [first * first, ...rest],\ [], array); squareAll([1, 2, 3, 4, 5]) _//=> [1,4,9,16,25]_

### Technical atom 6

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01384))_

> And if we like, we can write mapWith using foldWith:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01387))_

> **const** mapWith = (fn, array) => foldWith((first, rest) => [fn(first), ...rest], [\ ], array), squareAll = (array) => mapWith((x) => x * x, array);

### Technical atom 7

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01388))_

> squareAll([1, 2, 3, 4, 5]) _//=> [1,4,9,16,25]_

### Technical atom 8

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01389))_

> And to return to our first example, our version of length can be written as a fold:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01390))_

> **const** length = (array) => foldWith((first, rest) => 1 + rest, 0, array);

### Technical atom 9

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01389))_

> And to return to our first example, our version of length can be written as a fold:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01391))_

> length([1, 2, 3, 4, 5]) _//=> 5_
