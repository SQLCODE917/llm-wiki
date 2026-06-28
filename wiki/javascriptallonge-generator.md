---
page_id: javascriptallonge-generator
page_kind: concept
summary: Generator: 5 statement(s) and 3 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-generator@79a0b3dd994382e364f69aeaeeec5188
---

# Generator

What [[javascriptallonge]] covers about generator:

## Statements

### generators and iterables

- Our generator function oneTwoThree is not an iterator. It's a function that returns an iterator when we invoke it. We write the function to yield values instead of return a single value, and JavaScript takes care of turning this into an object with a .next() function we can call. _(javascriptallonge.pdf (source-range-31a4cf47-01709))_

- If we call our generator function more than once, we get new iterators. As we saw above, we called oneTwoThree three times, and each time we got an iterator that begins at 1 and counts to 3 . Recalling the way we wrote ordered collections, we could make a collection that uses a generator function: _(javascriptallonge.pdf (source-range-31a4cf47-01710))_

- This pattern is encouraged, so much so that JavaScript provides a concise syntax for writing generator methods for objects: _(javascriptallonge.pdf (source-range-31a4cf47-01713))_

- This object declares a [Symbol.iterator] function that makes it iterable. Because it's declared *[Symbol.iterator] , it's a generator instead of an iterator. _(javascriptallonge.pdf (source-range-31a4cf47-01715))_

- So to summarize, ThreeNumbers is an object that we've made iterable, by way of writing a generator method for [Symbol.iterator] . _(javascriptallonge.pdf (source-range-31a4cf47-01716))_


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


## Related pages

- [[javascriptallonge-function]] - shared statements and technical atoms: Function shares source evidence from generators and iterables: Our generator function oneTwoThree is not an iterator. It's a function that returns an iterator when we invoke it. We write the function to yield values instead of r ... [truncated]; Function shares technical record from generators and iterables: If we call our generator function more than once, we get new iterators. (1 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-iterable]] - shared statements and technical atoms: Iterable shares source evidence from generators and iterables: So to summarize, ThreeNumbers is an object that we've made iterable, by way of writing a generator method for [Symbol.iterator] .; Iterable shares technical record from generators and iterables: If we call our generator function more than once, we get new iterators. (1 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-pattern]] - shared statements and technical atoms: Pattern shares source evidence from generators and iterables: This pattern is encouraged, so much so that JavaScript provides a concise syntax for writing generator methods for objects:; Pattern shares technical record from generators and iterables: const ThreeNumbers = { *[Symbol.iterator] () { yield 1; yield 2; yield 3 } } (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-recall]] - shared statements and technical atoms: Recall shares source evidence from generators and iterables: If we call our generator function more than once, we get new iterators. As we saw above, we called oneTwoThree three times, and each time we got an iterator that beg ... [truncated]; Recall shares technical record from generators and iterables: const ThreeNumbers = { [Symbol.iterator]: function * () { yield 1; yield 2; yield 3 } } for ( const i of ThreeNumbers) { console.log(i); } //=> 1 2 3 [...ThreeNumber ... [truncated] (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-iterator]] - shared technical atoms: Iterator shares technical record from generators and iterables: If we call our generator function more than once, we get new iterators. (3 shared atom(s))
- [[javascriptallonge-symbol]] - shared technical atoms: Symbol shares technical record from generators and iterables: If we call our generator function more than once, we get new iterators. (3 shared atom(s))
- [[javascriptallonge-object]] - shared technical atoms: Object shares technical record from generators and iterables: If we call our generator function more than once, we get new iterators. (2 shared atom(s))
- [[javascriptallonge-section-more-generators-59ed9e0a]] - source section: more generators shares source evidence from more generators: Our OneTwoThree example used implicit state to output the numbers in sequence. Recall that we wrote Fibonacci using explicit state:; more generators shares technical record from more generators: const Numbers = { *[Symbol.iterator] () { let i = 0; while ( true ) { yield i++; } } }; for ( const i of Numbers) { console.log(i); } //=> 0 1 2 3 4 5 6 7 (3 shared statement(s), 6 shared atom(s))

## Source

- [[javascriptallonge]]
