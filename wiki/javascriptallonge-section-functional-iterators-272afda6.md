---
page_id: javascriptallonge-section-functional-iterators-272afda6
page_kind: source
summary: **Functional Iterators**: 19 source-backed entries and 12 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-functional-iterators-272afda6@653a64989b134988f032db9ed3e0ee1b
---

# **Functional Iterators**

From [[javascriptallonge]].

## Statements

- But it still relies on foldArrayWith, so it can only sum arrays. _(javascriptallonge.pdf (source-range-83ecb080-01939))_
- The nice thing about this is that the definition for arraySum mostly concerns itself with summing, and not with traversing over a collection of data. _(javascriptallonge.pdf (source-range-83ecb080-01939))_
- But it still relies on foldArrayWith, so it can only sum arrays. _(javascriptallonge.pdf (source-range-83ecb080-01939))_
- Well, we call arraySum with an array, and it has baked into it a method for traversing the array. _(javascriptallonge.pdf (source-range-83ecb080-01941))_
- Perhaps we could extract both of those things. _(javascriptallonge.pdf (source-range-83ecb080-01941))_
- The sumFoldable function doesn’t care what kind of data structure we have, as long as it’s foldable. _(javascriptallonge.pdf (source-range-83ecb080-01949))_
- We’ve found another way to express the principle of separating traversing a data structure from the operation we want to perform on that data structure, we’ve completely separated the knowledge of how to sum from the knowledge of how to fold an array or tree (or anything else, really). _(javascriptallonge.pdf (source-range-83ecb080-01956))_

## Technical atoms

> Context: Let’s consider a remarkably simple problem: Finding the sum of the elements of an array. In tailrecursive style, it looks like this:
_(context: javascriptallonge.pdf (source-range-83ecb080-01933))_

> **const** arraySum = ([first, ...rest], accumulator = 0) => first === **undefined** ? accumulator : arraySum(rest, first + accumulator)
_(source: javascriptallonge.pdf (source-range-83ecb080-01934))_

> Context: Let’s consider a remarkably simple problem: Finding the sum of the elements of an array. In tailrecursive style, it looks like this:
_(context: javascriptallonge.pdf (source-range-83ecb080-01933))_

> arraySum([1, 4, 9, 16, 25]) _//=> 55_
_(source: javascriptallonge.pdf (source-range-83ecb080-01935))_

> Context: As we saw earlier, this entangles the mechanism of traversing the array with the business of summing the bits. So we can separate them using fold:
_(context: javascriptallonge.pdf (source-range-83ecb080-01936))_

> **const** arraySum = callLeft(foldArrayWith, (a, b) => a + b, 0); arraySum([1, 4, 9, 16, 25]) _//=> 55_
_(source: javascriptallonge.pdf (source-range-83ecb080-01938))_

> Context: Well, we call arraySum with an array, and it has baked into it a method for traversing the array. Perhaps we could extract both of those things. Let’s rearrange our code a bit:
_(context: javascriptallonge.pdf (source-range-83ecb080-01941))_

> **const** callRight = (fn, ...args) => (...remainingArgs) => fn(...remainingArgs, ...args);
_(source: javascriptallonge.pdf (source-range-83ecb080-01944))_

> **const** foldArrayWith = (fn, terminalValue, [first, ...rest]) => first === **undefined** ? terminalValue : fn(first, foldArrayWith(fn, terminalValue, rest));
_(source: javascriptallonge.pdf (source-range-83ecb080-01945))_

> **const** foldArray = (array) => callRight(foldArrayWith, array);
_(source: javascriptallonge.pdf (source-range-83ecb080-01946))_

> **const** sumFoldable = (folder) => folder((a, b) => a + b, 0);
_(source: javascriptallonge.pdf (source-range-83ecb080-01947))_

> sumFoldable(foldArray([1, 4, 9, 16, 25])) _//=> 55_
_(source: javascriptallonge.pdf (source-range-83ecb080-01948))_

> Context: Here it is summing a tree of numbers:
_(context: javascriptallonge.pdf (source-range-83ecb080-01950))_

> **const** callRight = (fn, ...args) => (...remainingArgs) => fn(...remainingArgs, ...args);
_(source: javascriptallonge.pdf (source-range-83ecb080-01951))_

> Context: Here it is summing a tree of numbers:
_(context: javascriptallonge.pdf (source-range-83ecb080-01950))_

> **const** foldTree = (tree) => callRight(foldTreeWith, tree);
_(source: javascriptallonge.pdf (source-range-83ecb080-01953))_

> **const** sumFoldable = (folder) => folder((a, b) => a + b, 0);
_(source: javascriptallonge.pdf (source-range-83ecb080-01954))_

> sumFoldable(foldTree([1, [4, [9, 16]], 25])) _//=> 55_
_(source: javascriptallonge.pdf (source-range-83ecb080-01955))_
