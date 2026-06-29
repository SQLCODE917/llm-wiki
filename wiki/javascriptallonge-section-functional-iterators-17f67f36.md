---
page_id: javascriptallonge-section-functional-iterators-17f67f36
page_kind: source
summary: Functional Iterators: 11 source-backed entries and 4 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-functional-iterators-17f67f36@a6b61f3f074567cdd4bb61c42fd4cedb
---

# Functional Iterators

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-functional-iterator]] - topic hub: opens the topic page for Functional Iterator
- [[javascriptallonge-section-a-look-back-at-functional-iterators-c95ba37c]] - same source heading: another source section with the same heading, a look back at functional iterators

## Statements

- The nice thing about this is that the definition for arraySum mostly concerns itself with summing, and not with traversing over a collection of data. But it still relies on foldArrayWith , so it can only sum arrays. _(javascriptallonge.pdf (source-range-8eb13d6b-01275))_
- Well, we call arraySum with an array, and it has baked into it a method for traversing the array. Perhaps we could extract both of those things. Let's rearrange our code a bit: _(javascriptallonge.pdf (source-range-8eb13d6b-01277))_
- What we've done is turn an array into a function that folds an array with const foldArray = (array) => callRight(foldArrayWith, array); . The sumFoldable function doesn't care what kind of data structure we have, as long as it's foldable. _(javascriptallonge.pdf (source-range-8eb13d6b-01279))_
- We've found another way to express the principle of separating traversing a data structure from the operation we want to perform on that data structure, we've completely separated the knowledge of how to sum from the knowledge of how to fold an array or tree (or anything else, really). _(javascriptallonge.pdf (source-range-8eb13d6b-01282))_
- But it still relies on foldArrayWith , so it can only sum arrays. _(javascriptallonge.pdf (source-range-8eb13d6b-01275))_

## Technical atoms

### Technical frame 1: Functional Iterators

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01275))_

> The nice thing about this is that the definition for arraySum mostly concerns itself with summing, and not with traversing over a collection of data. But it still relies on foldArrayWith , so it can only sum arrays.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01272))_

```
const arraySum = ([first, ...rest], accumulator = 0) => first === undefined ? accumulator : arraySum(rest, first + accumulator) arraySum([1, 4, 9, 16, 25]) //=> 55
```

### Technical frame 2: Functional Iterators

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01275))_

> The nice thing about this is that the definition for arraySum mostly concerns itself with summing, and not with traversing over a collection of data. But it still relies on foldArrayWith , so it can only sum arrays.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01274))_

```
const callLeft = (fn, ...args) => (...remainingArgs) => fn(...args, ...remainingArgs); const foldArrayWith = (fn, terminalValue, [first, ...rest]) => first === undefined ? terminalValue : fn(first, foldArrayWith(fn, terminalValue, rest)); const arraySum = callLeft(foldArrayWith, (a, b) => a + b, 0); arraySum([1, 4, 9, 16, 25]) //=> 55
```

### Technical frame 3: Functional Iterators

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01279))_

> What we've done is turn an array into a function that folds an array with const foldArray = (array) => callRight(foldArrayWith, array); . The sumFoldable function doesn't care what kind of data structure we have, as long as it's foldable.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01278))_

```
const callRight = (fn, ...args) => (...remainingArgs) => fn(...remainingArgs, ...args); const foldArrayWith = (fn, terminalValue, [first, ...rest]) => first === undefined ? terminalValue : fn(first, foldArrayWith(fn, terminalValue, rest)); const foldArray = (array) => callRight(foldArrayWith, array); const sumFoldable = (folder) => folder((a, b) => a + b, 0); sumFoldable(foldArray([1, 4, 9, 16, 25])) //=> 55
```

### Technical frame 4: Functional Iterators

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01282))_

> We've found another way to express the principle of separating traversing a data structure from the operation we want to perform on that data structure, we've completely separated the knowledge of how to sum from the knowledge of how to fold an array or tree (or anything else, really).

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01281))_

```
const callRight = (fn, ...args) => (...remainingArgs) => fn(...remainingArgs, ...args); const foldTreeWith = (fn, terminalValue, [first, ...rest]) => first === undefined ? terminalValue : Array.isArray(first) ? fn(foldTreeWith(fn, terminalValue, first), foldTreeWith(fn, terminalValu\ e, rest)) : fn(first, foldTreeWith(fn, terminalValue, rest)); const foldTree = (tree) => callRight(foldTreeWith, tree); const sumFoldable = (folder) => folder((a, b) => a + b, 0); sumFoldable(foldTree([1, [4, [9, 16]], 25])) //=> 55
```
