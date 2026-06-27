---
page_id: javascriptallonge-functional-iterator
page_kind: concept
summary: Functional Iterators: 33 statement(s) and 25 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-functional-iterator@49fa45523c6eb6ecbd7e9f396b000f2e
---

# Functional Iterators

What [[javascriptallonge]] covers about functional iterators:

## Statements

- For all intents and purposes, once you pass an iterator to a function, you can expect that you no longer “own” that iterator, and that its state either has changed or will change. _(javascriptallonge.pdf (source-range-83ecb080-02025))_
- Mapping and filtering iterators allows us to compose the parts we already have, rather than writing a tricky bit of code with ifs and whiles and boundary conditions. _(javascriptallonge.pdf (source-range-83ecb080-02013))_
- We can write a different iterator for a different data structure. _(javascriptallonge.pdf (source-range-83ecb080-01977))_
- It’s possible to write a generic unfold mechanism, but let’s pass on to what we can do with unfolded iterators. _(javascriptallonge.pdf (source-range-83ecb080-01995))_
- We can start with take, an easy function that returns an iterator that only returns a fixed number of elements: _(javascriptallonge.pdf (source-range-83ecb080-02001))_
- We’ll need an iterator that produces odd numbers. _(javascriptallonge.pdf (source-range-83ecb080-02003))_
- We could also write a filter for iterators to accompany our mapping function: _(javascriptallonge.pdf (source-range-83ecb080-02009))_
- One is that while functions like take(...) appear to create an entirely new iterator, in reality they return a decorated reference to the original iterator. _(javascriptallonge.pdf (source-range-83ecb080-02024))_
- But it still relies on foldArrayWith, so it can only sum arrays. _(javascriptallonge.pdf (source-range-83ecb080-01939))_
- The nice thing about this is that the definition for arraySum mostly concerns itself with summing, and not with traversing over a collection of data. _(javascriptallonge.pdf (source-range-83ecb080-01939))_
- Well, we call arraySum with an array, and it has baked into it a method for traversing the array. _(javascriptallonge.pdf (source-range-83ecb080-01941))_
- Perhaps we could extract both of those things. _(javascriptallonge.pdf (source-range-83ecb080-01941))_
- The sumFoldable function doesn’t care what kind of data structure we have, as long as it’s foldable. _(javascriptallonge.pdf (source-range-83ecb080-01949))_
- Nevertheless, there is some value in being able to express some algorithms as iteration. _(javascriptallonge.pdf (source-range-83ecb080-01960))_

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


## Source

- [[javascriptallonge]]
