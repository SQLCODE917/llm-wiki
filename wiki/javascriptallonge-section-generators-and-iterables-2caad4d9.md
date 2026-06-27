---
page_id: javascriptallonge-section-generators-and-iterables-2caad4d9
page_kind: source
summary: **generators and iterables**: 11 source-backed entries and 3 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-generators-and-iterables-2caad4d9@1ef9a2116110015a09e75652787b7dce
---

# **generators and iterables**

From [[javascriptallonge]].

## Statements

- Our generator function oneTwoThree is not an iterator. _(javascriptallonge.pdf (source-range-83ecb080-02651))_
- As we saw above, we called oneTwoThree three times, and each time we got an iterator that begins at 1 and counts to 3. _(javascriptallonge.pdf (source-range-83ecb080-02652))_
- Recalling the way we wrote ordered collections, we could make a collection that uses a generator function: _(javascriptallonge.pdf (source-range-83ecb080-02652))_
- This pattern is encouraged, so much so that JavaScript provides a concise syntax for writing _(javascriptallonge.pdf (source-range-83ecb080-02659))_
- This object declares a [Symbol.iterator] function that makes it iterable. _(javascriptallonge.pdf (source-range-83ecb080-02664))_
- Because it’s declared *[Symbol.iterator], it’s a generator instead of an iterator. _(javascriptallonge.pdf (source-range-83ecb080-02664))_
- Because it’s declared *[Symbol.iterator], it’s a generator instead of an iterator. _(javascriptallonge.pdf (source-range-83ecb080-02664))_
- So to summarize, ThreeNumbers is an object that we’ve made iterable, by way of writing a _generator_ method for [Symbol.iterator]. _(javascriptallonge.pdf (source-range-83ecb080-02665))_

## Technical atoms

> Context: Our generator function oneTwoThree is not an iterator. It’s a function that returns an iterator when we invoke it. We write the function to yield values instead of return a single value, and JavaScript takes care of turning this into an object with a .next() function we can call.
_(context: javascriptallonge.pdf (source-range-83ecb080-02651))_

> If we call our generator function more than once, we get new iterators.
_(source: javascriptallonge.pdf (source-range-83ecb080-02652))_

> Context: Now we can use it in a for...of loop, spread it into an array literal, or spread it into a function invocation, because we have written an iterable that uses a generator to return an iterator from its [Symbol.iterator] method.
_(context: javascriptallonge.pdf (source-range-83ecb080-02658))_

> **const** iterator = ThreeNumbers[Symbol.iterator]();
_(source: javascriptallonge.pdf (source-range-83ecb080-02656))_

> Context: generator methods for objects: This object declares a [Symbol.iterator] function that makes it iterable. Because it’s declared *[Symbol.iterator], it’s a generator instead of an iterator.
_(context: javascriptallonge.pdf (source-range-83ecb080-02662, source-range-83ecb080-02664))_

> **const** ThreeNumbers = { *[Symbol.iterator] () { **yield** 1; **yield** 2; **yield** 3 } }
_(source: javascriptallonge.pdf (source-range-83ecb080-02663))_
