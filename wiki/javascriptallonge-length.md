---
page_id: javascriptallonge-length
page_kind: concept
summary: Length: 7 statement(s) and 12 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-length@7153a3f6173c00e01eee9f73794851ea
---

# Length

What [[javascriptallonge]] covers about length:

## Statements

### Self-Similarity

- We need something for when the array isn't empty. If an array is not empty, and we break it into two pieces, first and rest , the length of our array is going to be length(first) + length(rest) . Well, the length of first is 1 , there's just one element at the front. But we don't know the length of rest . If only there was a function we could call… Like length ! _(javascriptallonge.pdf (source-range-31a4cf47-00901))_

- Our length function is recursive , it calls itself. This makes sense because our definition of a list is recursive, and if a list is self-similar, it is natural to create an algorithm that is also self-similar. _(javascriptallonge.pdf (source-range-31a4cf47-00904))_

### folding

- And to return to our first example, our version of length can be written as a fold: _(javascriptallonge.pdf (source-range-31a4cf47-00949))_

### tail-call optimization

- The length function calls itself, but it is not a tail-call, because it returns 1 + length(rest) , not length(rest) . _(javascriptallonge.pdf (source-range-31a4cf47-00974))_

### converting non-tail-calls to tail-calls

- This version of length calls uses lengthDelaysWork , and JavaScript optimizes that not to take up memory proportional to the length of the string. We can use this technique with mapWith : _(javascriptallonge.pdf (source-range-31a4cf47-00983))_

### revisiting linked lists

- Mind you, this is still much, much faster than making partial copies of arrays. For a list of length n , wecreated n superfluous nodes and copied n superfluous values. Whereas our naïve array algorithm created 2 n superfluous arrays and copied n 2 superfluous values. _(javascriptallonge.pdf (source-range-31a4cf47-01117))_

### Making Data Out Of Functions

- In our code so far, we have used arrays and objects to represent the structure of data, and we have extensively used the ternary operator to write algorithms that terminate when we reach a base case. For example, this length function uses a functions to bind values to names, POJOs to structure nodes, and the ternary function to detect the base case, the empty list. _(javascriptallonge.pdf (source-range-31a4cf47-01328))_


## Technical atoms

### Technical frame 1: Self-Similarity

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00901))_

> We need something for when the array isn't empty. If an array is not empty, and we break it into two pieces, first and rest , the length of our array is going to be length(first) + length(rest) . Well, the length of first is 1 , there's just one element at the front. But we don't know the length of rest . If only there was a function we could call… Like length !

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00900))_

```
const length = ([first, ...rest]) => first === undefined ? 0 : // ???
```

### Technical frame 2: Self-Similarity

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00904))_

> Our length function is recursive , it calls itself. This makes sense because our definition of a list is recursive, and if a list is self-similar, it is natural to create an algorithm that is also self-similar.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00902))_

```
const length = ([first, ...rest]) => first === undefined ? 0 : 1 + length(rest); Let's try it! length([]) //=> 0 length(["foo"]) //=> 1 length(["foo", "bar", "baz"])
```

### Technical frame 3: Self-Similarity

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00904))_

> Our length function is recursive , it calls itself. This makes sense because our definition of a list is recursive, and if a list is self-similar, it is natural to create an algorithm that is also self-similar.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00903))_

```
//=> 3
```

### Technical frame 4: folding

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00943))_

> And now we supply a function that does slightly more than our mapping functions:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00937))_

```
const sumSquares = ([first, ...rest]) => first === undefined ? 0 : first * first + sumSquares(rest); sumSquares([1, 2, 3, 4, 5]) //=> 55
```

### Technical frame 5: folding

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00949))_

> And to return to our first example, our version of length can be written as a fold:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00950))_

```
const length = (array) => foldWith((first, rest) => 1 + rest, 0, array); length([1, 2, 3, 4, 5]) //=> 5
```

### Technical frame 6: tail-call optimization

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00974))_

> The length function calls itself, but it is not a tail-call, because it returns 1 + length(rest) , not length(rest) .

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00973))_

```
const length = ([first, ...rest]) => first === undefined ? 0 : 1 + length(rest);
```

### Technical frame 7: converting non-tail-calls to tail-calls

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00980))_

> This lengthDelaysWork function calls itself in tail position. The 1 + work is done before calling itself, and by the time it reaches the terminal position, it has the answer. Now that we've seen how it works, we can clean up the 0 + numberToBeAdded business. But while we're doing that, it's annoying to remember to call it with a zero. Let's fix that:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00979))_

```
const lengthDelaysWork = ([first, ...rest], numberToBeAdded) => first === undefined ? 0 + numberToBeAdded : lengthDelaysWork(rest, 1 + numberToBeAdded) lengthDelaysWork(["foo", "bar", "baz"], 0) //=> 3
```

### Technical frame 8: converting non-tail-calls to tail-calls

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00983))_

> This version of length calls uses lengthDelaysWork , and JavaScript optimizes that not to take up memory proportional to the length of the string. We can use this technique with mapWith :

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00981))_

```
const lengthDelaysWork = ([first, ...rest], numberToBeAdded) => first === undefined ? numberToBeAdded : lengthDelaysWork(rest, 1 + numberToBeAdded) const length = (n) => lengthDelaysWork(n, 0);
```

### Technical frame 9: converting non-tail-calls to tail-calls

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00983))_

> This version of length calls uses lengthDelaysWork , and JavaScript optimizes that not to take up memory proportional to the length of the string. We can use this technique with mapWith :

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00982))_

```
Or we could use partial application: const callLast = (fn, ...args) => (...remainingArgs) => fn(...remainingArgs, ...args); const length = callLast(lengthDelaysWork, 0); length(["foo", "bar", "baz"]) //=> 3
```

### Technical frame 10: converting non-tail-calls to tail-calls

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00986))_

> Brilliant! We can map over large arrays without incurring all the memory and performance overhead of non-tail-calls. And this basic transformation from a recursive function that does not make a tail call, into a recursive function that calls itself in tail position, is a bread-and-butter pattern for programmers using a language that incorporates tail-call optimization.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00984))_

```
const mapWithDelaysWork = (fn, [first, ...rest], prepend) => first === undefined ? prepend : mapWithDelaysWork(fn, rest, [...prepend, fn(first)]); const mapWith = callLast(mapWithDelaysWork, []); mapWith((x) => x * x, [1, 2, 3, 4, 5]) //=> [1,4,9,16,25] We can use it with ridiculously large arrays:
```

### Technical frame 11: converting non-tail-calls to tail-calls

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00986))_

> Brilliant! We can map over large arrays without incurring all the memory and performance overhead of non-tail-calls. And this basic transformation from a recursive function that does not make a tail call, into a recursive function that calls itself in tail position, is a bread-and-butter pattern for programmers using a language that incorporates tail-call optimization.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00985))_

```
mapWith((x) => x * x, [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, // ... 2980, 2981, 2982, 2983, 2984, 2985, 2986, 2987, 2988, 2989, 2990, 2991, 2992, 2993, 2994, 2995, 2996, 2997, 2998, 2999 ]) //=> [0,1,4,9,16,25,36,49,64,81,100,121,144,169,196, ...
```

### Technical frame 12: Making Data Out Of Functions

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01330))_

> A very long time ago, mathematicians like Alonzo Church, Moses Schönfinkel, Alan Turning, and Haskell Curry and asked themselves if we really needed all these features to perform computations. They searched for a radically simpler set of tools that could accomplish all of the same things.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01329))_

```
const EMPTY = {}; const OneTwoThree = { first: 1, rest: { first: 2, rest: { first: 3, rest: EMPTY \ } } }; OneTwoThree.first //=> 1 OneTwoThree.rest.first //=> 2 OneTwoThree.rest.rest.first //=> 3 const length = (node, delayed = 0) => node === EMPTY ? delayed : length(node.rest, delayed + 1); length(OneTwoThree) //=> 3
```


## Related pages

- [[javascriptallonge-function]] - shared statements and technical atoms: Function shares source evidence from Self-Similarity: Our length function is recursive , it calls itself. This makes sense because our definition of a list is recursive, and if a list is self-similar, it is natural to c ... [truncated]; Function shares technical record from Self-Similarity: const length = ([first, ...rest]) => first === undefined ? 0 : // ??? (3 shared statement(s), 9 shared atom(s))
- [[javascriptallonge-version]] - shared statements and technical atoms: Version shares source evidence from folding: And to return to our first example, our version of length can be written as a fold:; Version shares technical record from folding: const length = (array) => foldWith((first, rest) => 1 + rest, 0, array); length([1, 2, 3, 4, 5]) //=> 5 (2 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-list]] - shared statements and technical atoms: List shares source evidence from revisiting linked lists: Mind you, this is still much, much faster than making partial copies of arrays. For a list of length n , wecreated n superfluous nodes and copied n superfluous value ... [truncated]; List shares technical record from Self-Similarity: const length = ([first, ...rest]) => first === undefined ? 0 : 1 + length(rest); Let's try it! length([]) //=> 0 length(["foo"]) //=> 1 length(["foo", "bar", "baz"]) (1 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-return]] - shared statements and technical atoms: Return shares source evidence from folding: And to return to our first example, our version of length can be written as a fold:; Return shares technical record from folding: const length = (array) => foldWith((first, rest) => 1 + rest, 0, array); length([1, 2, 3, 4, 5]) //=> 5 (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-seen]] - shared technical atoms: Seen shares technical record from converting non-tail-calls to tail-calls: const lengthDelaysWork = ([first, ...rest], numberToBeAdded) => first === undefined ? 0 + numberToBeAdded : lengthDelaysWork(rest, 1 + numberToBeAdded) lengthDelaysW ... [truncated] (3 shared atom(s))
- [[javascriptallonge-array]] - shared technical atoms: Array shares technical record from Self-Similarity: const length = ([first, ...rest]) => first === undefined ? 0 : // ??? (2 shared atom(s))
- [[javascriptallonge-code]] - shared technical atoms: Code shares technical record from Making Data Out Of Functions: const EMPTY = {}; const OneTwoThree = { first: 1, rest: { first: 2, rest: { first: 3, rest: EMPTY \ } } }; OneTwoThree.first //=> 1 OneTwoThree.rest.first //=> 2 One ... [truncated] (1 shared atom(s))

## Source

- [[javascriptallonge]]
