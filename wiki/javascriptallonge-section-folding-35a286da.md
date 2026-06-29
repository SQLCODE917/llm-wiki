---
page_id: javascriptallonge-section-folding-35a286da
page_kind: source
summary: folding: 11 source-backed entries and 6 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-folding-35a286da@f14ec341331714170f984d263d167b00
---

# folding

From [[javascriptallonge]].

## Statements

- With the exception of the length example at the beginning, our examples so far all involve rebuilding a solution using spreads. But they needn't. A function to compute the sum of the squares of a list of numbers might look like this: _(javascriptallonge.pdf (source-range-8eb13d6b-00936))_
- And now we supply a function that does slightly more than our mapping functions: _(javascriptallonge.pdf (source-range-8eb13d6b-00943))_
- Our foldWith function is a generalization of our mapWith function. We can represent a map as a fold, we just need to supply the array rebuilding code: _(javascriptallonge.pdf (source-range-8eb13d6b-00945))_
- And to return to our first example, our version of length can be written as a fold: _(javascriptallonge.pdf (source-range-8eb13d6b-00949))_

## Technical atoms

### Technical frame 1: folding

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00943))_

> And now we supply a function that does slightly more than our mapping functions:

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00937))_

```
const sumSquares = ([first, ...rest]) => first === undefined ? 0 : first * first + sumSquares(rest); sumSquares([1, 2, 3, 4, 5]) //=> 55
```

### Technical frame 2: folding

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00943))_

> And now we supply a function that does slightly more than our mapping functions:

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00942))_

```
const foldWith = (fn, terminalValue, [first, ...rest]) => first === undefined ? terminalValue : fn(first, foldWith(fn, terminalValue, rest));
```

### Technical frame 3: folding

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00945))_

> Our foldWith function is a generalization of our mapWith function. We can represent a map as a fold, we just need to supply the array rebuilding code:

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00944))_

```
foldWith((number, rest) => number * number + rest, 0, [1, 2, 3, 4, 5]) //=> 55
```

### Technical frame 4: folding

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00949))_

> And to return to our first example, our version of length can be written as a fold:

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00946))_

```
const squareAll = (array) => foldWith((first, rest) => [first * first, ...rest],\ [], array); squareAll([1, 2, 3, 4, 5]) //=> [1,4,9,16,25]
```

### Technical frame 5: folding

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00949))_

> And to return to our first example, our version of length can be written as a fold:

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00948))_

```
const mapWith = (fn, array) => foldWith((first, rest) => [fn(first), ...rest], [\ ], array), squareAll = (array) => mapWith((x) => x * x, array); squareAll([1, 2, 3, 4, 5]) //=> [1,4,9,16,25]
```

### Technical frame 6: folding

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00949))_

> And to return to our first example, our version of length can be written as a fold:

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00950))_

```
const length = (array) => foldWith((first, rest) => 1 + rest, 0, array); length([1, 2, 3, 4, 5]) //=> 5
```
