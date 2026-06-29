---
page_id: javascriptallonge-section-composing-and-decomposing-data-self-similarity-folding-6afcd1fe
page_kind: source
summary: Composing and Decomposing Data / Self-Similarity / folding: 11 source-backed entries and 6 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-29
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-composing-and-decomposing-data-self-similarity-folding-6afcd1fe@14cdc7fe8c5e51fcd7aebd70e9221390
---

# Composing and Decomposing Data / Self-Similarity / folding

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-composing-and-decomposing-data-self-similarity-f4d3bc3f]] - broader source section: Composing and Decomposing Data / Self-Similarity

## Statements

- With the exception of the length example at the beginning, our examples so far all involve rebuilding a solution using spreads. But they needn't. A function to compute the sum of the squares of a list of numbers might look like this: _(javascriptallonge.pdf (source-range-7239e085-00936))_
- And now we supply a function that does slightly more than our mapping functions: _(javascriptallonge.pdf (source-range-7239e085-00943))_
- Our foldWith function is a generalization of our mapWith function. We can represent a map as a fold, we just need to supply the array rebuilding code: _(javascriptallonge.pdf (source-range-7239e085-00945))_
- And to return to our first example, our version of length can be written as a fold: _(javascriptallonge.pdf (source-range-7239e085-00949))_

## Technical atoms

### Technical frame 1: Composing and Decomposing Data / Self-Similarity / folding

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00943))_

> And now we supply a function that does slightly more than our mapping functions:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00937))_

```
const sumSquares = ([first, ...rest]) => first === undefined
? 0
: first * first + sumSquares(rest);
sumSquares([1, 2, 3, 4, 5])
//=> 55
```

### Technical frame 2: Composing and Decomposing Data / Self-Similarity / folding

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00943))_

> And now we supply a function that does slightly more than our mapping functions:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00942))_

```
const foldWith = (fn, terminalValue, [first, ...rest]) =>
first === undefined
? terminalValue
: fn(first, foldWith(fn, terminalValue, rest));
```

### Technical frame 3: Composing and Decomposing Data / Self-Similarity / folding

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00945))_

> Our foldWith function is a generalization of our mapWith function. We can represent a map as a fold, we just need to supply the array rebuilding code:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00944))_

```
foldWith((number, rest) => number * number + rest, 0, [1, 2, 3, 4, 5])
//=> 55
```

### Technical frame 4: Composing and Decomposing Data / Self-Similarity / folding

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00949))_

> And to return to our first example, our version of length can be written as a fold:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00946))_

```
const squareAll = (array) => foldWith((first, rest) => [first * first, ...rest],\
[], array);
squareAll([1, 2, 3, 4, 5])
//=> [1,4,9,16,25]
```

### Technical frame 5: Composing and Decomposing Data / Self-Similarity / folding

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00949))_

> And to return to our first example, our version of length can be written as a fold:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00948))_

```
const mapWith = (fn, array) => foldWith((first, rest) => [fn(first), ...rest], [\
], array),
squareAll = (array) => mapWith((x) => x * x, array);
squareAll([1, 2, 3, 4, 5])
//=> [1,4,9,16,25]
```

### Technical frame 6: Composing and Decomposing Data / Self-Similarity / folding

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00949))_

> And to return to our first example, our version of length can be written as a fold:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00950))_

```
const length = (array) => foldWith((first, rest) => 1 + rest, 0, array);
length([1, 2, 3, 4, 5])
//=> 5
```
