---
page_id: javascriptallonge-iterable
page_kind: concept
summary: Iterable: 2 statement(s) and 3 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-iterable@898f04301724ff475fd2511542e91b88
---

# Iterable

What [[javascriptallonge]] covers about iterable:

## Statements

### generators and iterables

- This object declares a [Symbol.iterator] function that makes it iterable. Because it's declared *[Symbol.iterator] , it's a generator instead of an iterator. _(javascriptallonge.pdf (source-range-8eb13d6b-01713))_

- So to summarize, ThreeNumbers is an object that we've made iterable, by way of writing a generator method for [Symbol.iterator] . _(javascriptallonge.pdf (source-range-8eb13d6b-01714))_


## Technical atoms

### Technical frame 1: generators and iterables

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01711))_

> This pattern is encouraged, so much so that JavaScript provides a concise syntax for writing generator methods for objects:

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01708))_

> If we call our generator function more than once, we get new iterators.

### Technical frame 2: generators and iterables

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01711))_

> This pattern is encouraged, so much so that JavaScript provides a concise syntax for writing generator methods for objects:

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01709))_

```
const ThreeNumbers = { [Symbol.iterator]: function * () { yield 1; yield 2; yield 3 } } for ( const i of ThreeNumbers) { console.log(i); } //=> 1 2 3 [...ThreeNumbers] //=> [1,2,3] const iterator = ThreeNumbers[Symbol.iterator](); iterator.next() //=> {"done": false , value: 1} iterator.next() //=> {"done": false , value: 2} iterator.next() //=> {"done": false , value: 3} iterator.next() //=> {"done": true }
```

### Technical frame 3: generators and iterables

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01713))_

> This object declares a [Symbol.iterator] function that makes it iterable. Because it's declared *[Symbol.iterator] , it's a generator instead of an iterator.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01712))_

```
const ThreeNumbers = { *[Symbol.iterator] () { yield 1; yield 2; yield 3 } }
```


## Related pages

- [[javascriptallonge-function]] - shared statements and technical atoms: Function shares source evidence from generators and iterables: This object declares a [Symbol.iterator] function that makes it iterable. Because it's declared *[Symbol.iterator] , it's a generator instead of an iterator.; Function shares technical record from generators and iterables: If we call our generator function more than once, we get new iterators. (1 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-generator]] - shared statements and technical atoms: Generator shares source evidence from generators and iterables: So to summarize, ThreeNumbers is an object that we've made iterable, by way of writing a generator method for [Symbol.iterator] .; Generator shares technical record from generators and iterables: If we call our generator function more than once, we get new iterators. (1 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-iterator]] - shared statements and technical atoms: Iterator shares source evidence from generators and iterables: This object declares a [Symbol.iterator] function that makes it iterable. Because it's declared *[Symbol.iterator] , it's a generator instead of an iterator.; Iterator shares technical record from generators and iterables: If we call our generator function more than once, we get new iterators. (1 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-symbol]] - shared statements and technical atoms: Symbol shares source evidence from generators and iterables: This object declares a [Symbol.iterator] function that makes it iterable. Because it's declared *[Symbol.iterator] , it's a generator instead of an iterator.; Symbol shares technical record from generators and iterables: If we call our generator function more than once, we get new iterators. (1 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-object]] - shared statements and technical atoms: Object shares source evidence from generators and iterables: This object declares a [Symbol.iterator] function that makes it iterable. Because it's declared *[Symbol.iterator] , it's a generator instead of an iterator.; Object shares technical record from generators and iterables: If we call our generator function more than once, we get new iterators. (1 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-pattern]] - shared technical atoms: Pattern shares technical record from generators and iterables: const ThreeNumbers = { *[Symbol.iterator] () { yield 1; yield 2; yield 3 } } (1 shared atom(s))
- [[javascriptallonge-recall]] - shared technical atoms: Recall shares technical record from generators and iterables: const ThreeNumbers = { [Symbol.iterator]: function * () { yield 1; yield 2; yield 3 } } for ( const i of ThreeNumbers) { console.log(i); } //=> 1 2 3 [...ThreeNumber ... [truncated] (1 shared atom(s))
- [[javascriptallonge-section-iterables-5d93ec42]] - source section: iterables shares source evidence from iterables: People have been writing iterators since JavaScript was first released in the late 1990s. Since there was no particular standard way to do it, people used all sorts ... [truncated]; iterables shares technical record from iterables: const Stack3 = () => ({ array: [], index: -1, push (value) { return this .array[ this .index += 1] = value; }, pop () { const value = this .array[ this .index]; this ... [truncated] (16 shared statement(s), 5 shared atom(s))

## Source

- [[javascriptallonge]]
