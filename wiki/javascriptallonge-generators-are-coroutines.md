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

### `technical-atom-e1013b40c3bcd26c` procedure

Citation: (raw/javascriptallonge.pdf p.231-234)

- When we call interator.next() , the body of our generator begins to be evaluated.

### `technical-atom-1316593e83fedbe2` code

Citation: (raw/javascriptallonge.pdf p.231-234)

```
- The iterator wraps 1 in {done: false, value: 1} and returns that from the call to .next() .
```

### `technical-atom-8108f47f578c9f69` procedure

Citation: (raw/javascriptallonge.pdf p.231-234)

- The rest of the program continues along its way until it makes another call to iterator.next() .

### `technical-atom-d1a307d6e07de4e9` procedure

Citation: (raw/javascriptallonge.pdf p.231-234)

- The body of our generator runs until it returns, ends, or encounters the next yield statement, which is yield 2; .

### `technical-atom-a4bd2e289d21345e` code

Citation: (raw/javascriptallonge.pdf p.231-234)

```
- The iterator wraps 2 in {done: false, value: 2} and returns that from the call to .next() .
```

### `technical-atom-66ba4e7ea1a0df88` procedure

Citation: (raw/javascriptallonge.pdf p.231-234)

- The body of our generator runs until it returns, ends, or encounters the next yield statement, which is yield 3; .
