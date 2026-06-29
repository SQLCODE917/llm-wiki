---
page_id: javascriptallonge-generator
page_kind: concept
summary: Generator: 5 statement(s) and 3 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-29
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-generator@3a1014d70ebd370e1f0d4c9998bb2fb4
---

# Generator

What [[javascriptallonge]] covers about generator:

## Statements

### We'll keep it simple: / generators and iterables

- Our generator function oneTwoThree is not an iterator. It's a function that returns an iterator when we invoke it. We write the function to yield values instead of return a single value, and JavaScript takes care of turning this into an object with a .next() function we can call. _(javascriptallonge.pdf (source-range-7239e085-01708))_

- If we call our generator function more than once, we get new iterators. As we saw above, we called oneTwoThree three times, and each time we got an iterator that begins at 1 and counts to 3 . Recalling the way we wrote ordered collections, we could make a collection that uses a generator function: _(javascriptallonge.pdf (source-range-7239e085-01709))_

- This pattern is encouraged, so much so that JavaScript provides a concise syntax for writing generator methods for objects: _(javascriptallonge.pdf (source-range-7239e085-01712))_

- This object declares a [Symbol.iterator] function that makes it iterable. Because it's declared *[Symbol.iterator] , it's a generator instead of an iterator. _(javascriptallonge.pdf (source-range-7239e085-01714))_

- So to summarize, ThreeNumbers is an object that we've made iterable, by way of writing a generator method for [Symbol.iterator] . _(javascriptallonge.pdf (source-range-7239e085-01715))_


## Technical atoms

### Technical frame 1: We'll keep it simple: / generators and iterables

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01712))_

> This pattern is encouraged, so much so that JavaScript provides a concise syntax for writing generator methods for objects:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01709))_

> If we call our generator function more than once, we get new iterators.

### Technical frame 2: We'll keep it simple: / generators and iterables

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01712))_

> This pattern is encouraged, so much so that JavaScript provides a concise syntax for writing generator methods for objects:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01710))_

```
const ThreeNumbers = {
[Symbol.iterator]: function * () {
yield 1;
yield 2;
yield 3
}
}
for (const i of ThreeNumbers) {
console.log(i);
}
//=>
1
2
3
[...ThreeNumbers]
//=>
[1,2,3]
const iterator = ThreeNumbers[Symbol.iterator]();
iterator.next()
//=>
{"done":false, value: 1}
iterator.next()
//=>
{"done":false, value: 2}
iterator.next()
//=>
{"done":false, value: 3}
iterator.next()
//=>
{"done":true}
```

### Technical frame 3: We'll keep it simple: / generators and iterables

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01714))_

> This object declares a [Symbol.iterator] function that makes it iterable. Because it's declared *[Symbol.iterator] , it's a generator instead of an iterator.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01713))_

```
const ThreeNumbers = {
*[Symbol.iterator] () {
yield 1;
yield 2;
yield 3
}
}
```


## Related pages

- [[javascriptallonge-function]] - shared statements and technical atoms: Function shares source evidence from We'll keep it simple: / generators and iterables: Our generator function oneTwoThree is not an iterator. It's a function that returns an iterator when we invoke it. We write the function to yield values instead of r ... [truncated]; Function shares technical record from We'll keep it simple: / generators and iterables: If we call our generator function more than once, we get new iterators. (1 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-iterable]] - shared statements and technical atoms: Iterable shares source evidence from We'll keep it simple: / generators and iterables: So to summarize, ThreeNumbers is an object that we've made iterable, by way of writing a generator method for [Symbol.iterator] .; Iterable shares technical record from We'll keep it simple: / generators and iterables: If we call our generator function more than once, we get new iterators. (1 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-pattern]] - shared statements and technical atoms: Pattern shares source evidence from We'll keep it simple: / generators and iterables: This pattern is encouraged, so much so that JavaScript provides a concise syntax for writing generator methods for objects:; Pattern shares technical record from We'll keep it simple: / generators and iterables: const ThreeNumbers = { *[Symbol.iterator] () { yield 1; yield 2; yield 3 } } (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-iterator]] - shared technical atoms: Iterator shares technical record from We'll keep it simple: / generators and iterables: If we call our generator function more than once, we get new iterators. (3 shared atom(s))
- [[javascriptallonge-symbol]] - shared technical atoms: Symbol shares technical record from We'll keep it simple: / generators and iterables: If we call our generator function more than once, we get new iterators. (3 shared atom(s))
- [[javascriptallonge-object]] - shared technical atoms: Object shares technical record from We'll keep it simple: / generators and iterables: If we call our generator function more than once, we get new iterators. (2 shared atom(s))
- [[javascriptallonge-write]] - shared technical atoms: Write shares technical record from We'll keep it simple: / generators and iterables: If we call our generator function more than once, we get new iterators. (1 shared atom(s))
- [[javascriptallonge-section-we-ll-keep-it-simple-more-generators-6ce23867]] - source section: We'll keep it simple: / more generators shares source evidence from We'll keep it simple: / more generators: Our OneTwoThree example used implicit state to output the numbers in sequence. Recall that we wrote Fibonacci using explicit state:; We'll keep it simple: / more generators shares technical record from We'll keep it simple: / more generators: const Numbers = { *[Symbol.iterator] () { let i = 0; while (true) { yield i++; } } }; for (const i of Numbers) { console.log(i); } //=> 0 1 2 3 4 5 6 7 (3 shared statement(s), 6 shared atom(s))

## Source

- [[javascriptallonge]]
