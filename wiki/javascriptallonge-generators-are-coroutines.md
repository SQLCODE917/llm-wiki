---
page_id: javascriptallonge-generators-are-coroutines
page_kind: source
summary: generators are coroutines from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.231-234
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

Generators in JavaScript behave as coroutines, with a distinct execution model compared to ordinary functions. They suspend and resume execution at yield points, enabling a producer-consumer model.

## Key supported claims

- This is where generators behave very, very differently from ordinary functions (raw/javascriptallonge.pdf p.231-234).
- The body of our generator runs until it returns, ends, or encounters a yield statement, which is yield 1; (raw/javascriptallonge.pdf p.231-234).
- When we call interator.next() , the body of our generator begins to be evaluated (raw/javascriptallonge.pdf p.231-234).

## Technical details

### `technical-atom-ab4e6b5cacd7f603` code

Citation: (raw/javascriptallonge.pdf p.231-234)

```javascript
const oneTwoThree = function * () { yield 1; yield 2; yield 3; }; oneTwoThree().next() //=> {"done": false , value: 1} oneTwoThree().next() //=> {"done": false , value: 1} oneTwoThree().next() //=> {"done": false , value: 1} const iterator = oneTwoThree(); iterator.next() //=> {"done": false , value: 1} iterator.next() //=> {"done": false , value: 2} iterator.next() //=> {"done": false , value: 3} iterator.next() //=> {"done": true }
```

### `technical-atom-420ad61fb2f38318` code

Citation: (raw/javascriptallonge.pdf p.231-234)

```javascript
const oneTwoThree = function () { let state = 'newborn'; return { next () { switch (state) { case 'newborn': state = 1; return {value: 1}; case 1: state = 2; return {value: 2} case 2: state = 3; return {value: 3} case 3: return {done: true }; } } } };
```

### `technical-atom-1316593e83fedbe2` code

Citation: (raw/javascriptallonge.pdf p.231-234)

```
- The iterator wraps 1 in {done: false, value: 1} and returns that from the call to .next() .
```

### `technical-atom-a4bd2e289d21345e` code

Citation: (raw/javascriptallonge.pdf p.231-234)

```
- The iterator wraps 2 in {done: false, value: 2} and returns that from the call to .next() .
```

### `technical-atom-e1013b40c3bcd26c` procedure

Citation: (raw/javascriptallonge.pdf p.231-234)

- When we call interator.next() , the body of our generator begins to be evaluated.

### `technical-atom-8108f47f578c9f69` procedure

Citation: (raw/javascriptallonge.pdf p.231-234)

- The rest of the program continues along its way until it makes another call to iterator.next() .

### `technical-atom-d1a307d6e07de4e9` procedure

Citation: (raw/javascriptallonge.pdf p.231-234)

- The body of our generator runs until it returns, ends, or encounters the next yield statement, which is yield 2; .

### `technical-atom-66ba4e7ea1a0df88` procedure

Citation: (raw/javascriptallonge.pdf p.231-234)

- The body of our generator runs until it returns, ends, or encounters the next yield statement, which is yield 3; .

## Related technical details

### From [[javascriptallonge-generators-and-iterables]]: `technical-atom-1384299a1f559507` procedure

Relation: nearby source page; matched terms `call`, `function`, `generators`, `javascript`, `next`, `procedure`

Citation: (raw/javascriptallonge.pdf p.234-236)

We write the function to yield values instead of return a single value, and JavaScript takes care of turning this into an object with a .next() function we can call.

### From [[javascriptallonge-javascript-s-generators]]: `technical-atom-00fab8fb6887a7bc` procedure

Relation: nearby source page; matched terms `generator`, `generators`, `javascript`, `next`, `procedure`, `very`

Citation: (raw/javascriptallonge.pdf p.230-231)

It would be very nice if we could sometimes write iterators as a .next() method that gets called, and sometimes write out a generator.

### From [[javascriptallonge-javascript-s-generators]]: `technical-atom-0bb7018c27793c3c` code

Relation: nearby source page; matched terms `function`, `generators`, `javascript`, `next`, `yield`

Citation: (raw/javascriptallonge.pdf p.230-231)

```javascript
function * only (something) { yield something; }; only("you").next() //=> {"done": false , value: "you"}
```

### From [[javascriptallonge-javascript-s-generators]]: `technical-atom-595c724b56877ae5` procedure

Relation: nearby source page; matched terms `call`, `generators`, `javascript`, `next`, `procedure`

Citation: (raw/javascriptallonge.pdf p.230-231)

We call its .next() method, but it's done immediately.
