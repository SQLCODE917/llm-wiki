---
page_id: javascriptallonge-javascript-s-generators
page_kind: source
summary: javascript's generators from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.230-231
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

This chapter covers JavaScript generators, including how to declare them using the function * syntax and how to use the yield keyword to produce values.

## Key supported claims

- Given the title of this chapter, it is not a surprise that JavaScript makes this possible (raw/javascriptallonge.pdf p.230-231).
- An iterator written in a generation style is called a generator (raw/javascriptallonge.pdf p.230-231).
- It would be very nice if we could sometimes write iterators as a .next() method that gets called, and sometimes write out a generator (raw/javascriptallonge.pdf p.230-231).

## Technical details

### `technical-atom-86d8be716add0911` code

Citation: (raw/javascriptallonge.pdf p.230-231)

```javascript
function * empty () {}; empty().next() //=> {"done": true }
```

### `technical-atom-0bb7018c27793c3c` code

Citation: (raw/javascriptallonge.pdf p.230-231)

```javascript
function * only (something) { yield something; }; only("you").next() //=> {"done": false , value: "you"}
```

### `technical-atom-dbb94b02c909e641` code

Citation: (raw/javascriptallonge.pdf p.230-231)

```javascript
only("you").next() //=> {"done": false , value: "you"} only("the lonely").next() //=> {"done": false , value: "the lonely"}
```

### `technical-atom-00dfdad6f11c662f` code

Citation: (raw/javascriptallonge.pdf p.230-231)

```javascript
const sixteen = only("sixteen"); sixteen.next() //=> {"done": false , value: "sixteen"} sixteen.next() //=> {"done": true }
```

### `technical-atom-bd725d9058677fd9` formula

Citation: (raw/javascriptallonge.pdf p.230-231)

91 Wewrote a generator declaration . We can also write const empty = function * () {} to bind an anonymous generator to the empty keyword, but we don't need to do that here.

### `technical-atom-00fab8fb6887a7bc` procedure

Citation: (raw/javascriptallonge.pdf p.230-231)

It would be very nice if we could sometimes write iterators as a .next() method that gets called, and sometimes write out a generator.

### `technical-atom-595c724b56877ae5` procedure

Citation: (raw/javascriptallonge.pdf p.230-231)

We call its .next() method, but it's done immediately.

### `technical-atom-f552e8bca51f04a8` worked-example

Citation: (raw/javascriptallonge.pdf p.230-231)

Let's start with the degenerate example, the empty iterator : 91

## Related technical details

### From [[javascriptallonge-generators-and-iterables]]: `technical-atom-1384299a1f559507` procedure

Relation: nearby source page; matched terms `function`, `generators`, `javascript`, `next`, `procedure`, `values`

Citation: (raw/javascriptallonge.pdf p.234-236)

We write the function to yield values instead of return a single value, and JavaScript takes care of turning this into an object with a .next() function we can call.

### From [[javascriptallonge-iteration]]: `technical-atom-e4b37a182a0d29ef` code

Relation: nearby source page; matched terms `iterator`, `iterators`, `next`

Citation: (raw/javascriptallonge.pdf p.227-228)

```javascript
const isIterable = (something) => !!something[Symbol.iterator]; const treeIterator = (iterable) => { const iterators = [ iterable[Symbol.iterator]() ]; return () => { while (!!iterators[0]) { const iterationResult = iterators[0].next(); if (iterationResult.done) { iterators.shift(); } else if (isIterable(iterationResult.value)) { iterators.unshift(iterationResult.value[Symbol.iterator]()); } else { return iterationResult.value; } } return ; } } const i = treeIterator([1, [2, [3, 4], 5]]); let n; while (n = i()) { console.log(n) } //=> 1 2 3 4 5
```

### From [[javascriptallonge-generators-are-coroutines]]: `technical-atom-ab4e6b5cacd7f603` code

Relation: nearby source page; matched terms `function`, `generators`, `iterator`, `next`, `yield`

Citation: (raw/javascriptallonge.pdf p.231-234)

```javascript
const oneTwoThree = function * () { yield 1; yield 2; yield 3; }; oneTwoThree().next() //=> {"done": false , value: 1} oneTwoThree().next() //=> {"done": false , value: 1} oneTwoThree().next() //=> {"done": false , value: 1} const iterator = oneTwoThree(); iterator.next() //=> {"done": false , value: 1} iterator.next() //=> {"done": false , value: 2} iterator.next() //=> {"done": false , value: 3} iterator.next() //=> {"done": true }
```

### From [[javascriptallonge-generators-are-coroutines]]: `technical-atom-8108f47f578c9f69` procedure

Relation: nearby source page; matched terms `generators`, `iterator`, `makes`, `next`, `procedure`

Citation: (raw/javascriptallonge.pdf p.231-234)

- The rest of the program continues along its way until it makes another call to iterator.next() .
