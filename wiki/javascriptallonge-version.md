---
page_id: javascriptallonge-version
page_kind: concept
summary: Version: 5 statement(s) and 4 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-version@b7fedf0c6e66e7050f140bc8201e784a
---

# Version

What [[javascriptallonge]] covers about version:

## Statements

### Foreword to the 'Six' edition

- ECMAScript 6 (short name: ES6; official name: ECMAScript 2015) was ratified as a standard on June 17. Getting there took a while - in a way, the origins of ES6 date back to the year 2000: After ECMAScript 3 was finished, TC39 (the committee evolving JavaScript) started to work on ECMAScript 4. That version was planned to have numerous new features (interfaces, namespaces, packages, multimethods, etc.), which would have turned JavaScript into a completely new language. After internal conflict, a settlement was reached in July 2008 and a new plan was made - to abandon ECMAScript 4 and to replace it with two upgrades: _(javascriptallonge.pdf (source-range-31a4cf47-00069))_

### folding

- And to return to our first example, our version of length can be written as a fold: _(javascriptallonge.pdf (source-range-31a4cf47-00949))_

### converting non-tail-calls to tail-calls

- This version of length calls uses lengthDelaysWork , and JavaScript optimizes that not to take up memory proportional to the length of the string. We can use this technique with mapWith : _(javascriptallonge.pdf (source-range-31a4cf47-00983))_

### // Iteration

- If you peel off isIterable and ignore the way that the iteration version uses [Symbol.iterator] and .next , we're left with the fact that the generating version calls itself recursively, and the iteration version maintains an explicit stack. In essence, both the generation and iteration implementations have stacks, but the generation version's stack is implicit , while the iteration version's stack is explicit . _(javascriptallonge.pdf (source-range-31a4cf47-01643))_

### We'll keep it simple:

- So we see the same thing: The generation version has state, but it's implicit in JavaScript's linear control flow. Whereas the iteration version must make that state explicit. _(javascriptallonge.pdf (source-range-31a4cf47-01660))_


## Technical atoms

### Technical frame 1: folding

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00949))_

> And to return to our first example, our version of length can be written as a fold:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00950))_

```
const length = (array) => foldWith((first, rest) => 1 + rest, 0, array); length([1, 2, 3, 4, 5]) //=> 5
```

### Technical frame 2: converting non-tail-calls to tail-calls

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00986))_

> Brilliant! We can map over large arrays without incurring all the memory and performance overhead of non-tail-calls. And this basic transformation from a recursive function that does not make a tail call, into a recursive function that calls itself in tail position, is a bread-and-butter pattern for programmers using a language that incorporates tail-call optimization.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00984))_

```
const mapWithDelaysWork = (fn, [first, ...rest], prepend) => first === undefined ? prepend : mapWithDelaysWork(fn, rest, [...prepend, fn(first)]); const mapWith = callLast(mapWithDelaysWork, []); mapWith((x) => x * x, [1, 2, 3, 4, 5]) //=> [1,4,9,16,25] We can use it with ridiculously large arrays:
```

### Technical frame 3: converting non-tail-calls to tail-calls

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00986))_

> Brilliant! We can map over large arrays without incurring all the memory and performance overhead of non-tail-calls. And this basic transformation from a recursive function that does not make a tail call, into a recursive function that calls itself in tail position, is a bread-and-butter pattern for programmers using a language that incorporates tail-call optimization.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00985))_

```
mapWith((x) => x * x, [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, // ... 2980, 2981, 2982, 2983, 2984, 2985, 2986, 2987, 2988, 2989, 2990, 2991, 2992, 2993, 2994, 2995, 2996, 2997, 2998, 2999 ]) //=> [0,1,4,9,16,25,36,49,64,81,100,121,144,169,196, ...
```

### Technical frame 4: // Iteration

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01643))_

> If you peel off isIterable and ignore the way that the iteration version uses [Symbol.iterator] and .next , we're left with the fact that the generating version calls itself recursively, and the iteration version maintains an explicit stack. In essence, both the generation and iteration implementations have stacks, but the generation version's stack is implicit , while the iteration version's stack is explicit .

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01642))_

```
const isIterable = (something) => !!something[Symbol.iterator]; const treeIterator = (iterable) => { const iterators = [ iterable[Symbol.iterator]() ]; return () => { while (!!iterators[0]) { const iterationResult = iterators[0].next(); if (iterationResult.done) { iterators.shift(); } else if (isIterable(iterationResult.value)) { iterators.unshift(iterationResult.value[Symbol.iterator]()); } else { return iterationResult.value; } } return ; } } const i = treeIterator([1, [2, [3, 4], 5]]); let n; while (n = i()) { console.log(n) } //=> 1 2 3 4 5
```


## Related pages

- [[javascriptallonge-length]] - shared statements and technical atoms: Length shares source evidence from folding: And to return to our first example, our version of length can be written as a fold:; Length shares technical record from folding: const length = (array) => foldWith((first, rest) => 1 + rest, 0, array); length([1, 2, 3, 4, 5]) //=> 5 (2 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-return]] - shared statements and technical atoms: Return shares source evidence from folding: And to return to our first example, our version of length can be written as a fold:; Return shares technical record from folding: const length = (array) => foldWith((first, rest) => 1 + rest, 0, array); length([1, 2, 3, 4, 5]) //=> 5 (1 shared statement(s), 1 shared atom(s))

## Source

- [[javascriptallonge]]
