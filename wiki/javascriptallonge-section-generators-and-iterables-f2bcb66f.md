---
page_id: javascriptallonge-section-generators-and-iterables-f2bcb66f
page_kind: source
summary: generators and iterables: 11 source-backed entries and 3 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-generators-and-iterables-f2bcb66f@324e061d94022fec79e4e75d4795459c
---

# generators and iterables

From [[javascriptallonge]].

## Statements

- Our generator function oneTwoThree is not an iterator. It's a function that returns an iterator when we invoke it. We write the function to yield values instead of return a single value, and JavaScript takes care of turning this into an object with a .next() function we can call. _(javascriptallonge.pdf (source-range-31a4cf47-01709))_
- If we call our generator function more than once, we get new iterators. As we saw above, we called oneTwoThree three times, and each time we got an iterator that begins at 1 and counts to 3 . Recalling the way we wrote ordered collections, we could make a collection that uses a generator function: _(javascriptallonge.pdf (source-range-31a4cf47-01710))_
- This pattern is encouraged, so much so that JavaScript provides a concise syntax for writing generator methods for objects: _(javascriptallonge.pdf (source-range-31a4cf47-01713))_
- This object declares a [Symbol.iterator] function that makes it iterable. Because it's declared *[Symbol.iterator] , it's a generator instead of an iterator. _(javascriptallonge.pdf (source-range-31a4cf47-01715))_
- So to summarize, ThreeNumbers is an object that we've made iterable, by way of writing a generator method for [Symbol.iterator] . _(javascriptallonge.pdf (source-range-31a4cf47-01716))_
- Because it's declared *[Symbol.iterator] , it's a generator instead of an iterator. _(javascriptallonge.pdf (source-range-31a4cf47-01715))_

## Technical atoms

### Technical frame 1: generators and iterables

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01713))_

> This pattern is encouraged, so much so that JavaScript provides a concise syntax for writing generator methods for objects:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01710))_

> If we call our generator function more than once, we get new iterators.

### Technical frame 2: generators and iterables

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01713))_

> This pattern is encouraged, so much so that JavaScript provides a concise syntax for writing generator methods for objects:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01711))_

```
const ThreeNumbers = { [Symbol.iterator]: function * () { yield 1; yield 2; yield 3 } } for ( const i of ThreeNumbers) { console.log(i); } //=> 1 2 3 [...ThreeNumbers] //=> [1,2,3] const iterator = ThreeNumbers[Symbol.iterator](); iterator.next() //=> {"done": false , value: 1} iterator.next() //=> {"done": false , value: 2} iterator.next() //=> {"done": false , value: 3} iterator.next() //=> {"done": true }
```

### Technical frame 3: generators and iterables

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01715))_

> This object declares a [Symbol.iterator] function that makes it iterable. Because it's declared *[Symbol.iterator] , it's a generator instead of an iterator.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01714))_

```
const ThreeNumbers = { *[Symbol.iterator] () { yield 1; yield 2; yield 3 } }
```
