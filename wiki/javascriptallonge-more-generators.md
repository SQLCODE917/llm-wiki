---
page_id: javascriptallonge-more-generators
page_kind: source
summary: more generators from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.236-239
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

Chapter on more generators in JavaScript Allongé, focusing on infinite streams and Fibonacci sequences using generators.

## Key supported claims

- Generators can produce infinite streams of values, such as a sequence of numbers (raw/javascriptallonge.pdf p.236-239).
- The Fibonacci sequence can be implemented using explicit state or generator methods (raw/javascriptallonge.pdf p.236-239).
- A generator function can be used to create a Fibonacci sequence, allowing natural state management in JavaScript (raw/javascriptallonge.pdf p.236-239).

## Technical details

### `technical-atom-9459db0d26b3472a` code

Citation: (raw/javascriptallonge.pdf p.236-239)

```javascript
const Numbers = { *[Symbol.iterator] () { let i = 0; while ( true ) { yield i++; } } }; for ( const i of Numbers) { console.log(i); } //=> 0 1 2 3 4 5 6 7
```

### `technical-atom-9d29261ca64c4a99` code

Citation: (raw/javascriptallonge.pdf p.236-239)

```
8 9 10 ...
```

### `technical-atom-4eb306a4de6660bf` code

Citation: (raw/javascriptallonge.pdf p.236-239)

```javascript
const Fibonacci = { [Symbol.iterator]: () => { let a = 0, b = 1, state = 0; return { next: () => { switch (state) { case 0: state = 1; return {value: a}; case 1: state = 2; return {value: b}; case 2: [a, b] = [b, a + b]; return {value: b}; } } } } }; for ( let n of Fibonacci) { console.log(n) } //=> 0 1 1 2 3 5 8 13
```

### `technical-atom-1547a708283ab40f` code

Citation: (raw/javascriptallonge.pdf p.236-239)

```
21 34 55 89 144 ...
```

### `technical-atom-8cf8e8761b405ccf` code

Citation: (raw/javascriptallonge.pdf p.236-239)

```javascript
const Fibonacci = { *[Symbol.iterator] () { let a, b; yield a = 0; yield b = 1; while ( true ) { [a, b] = [b, a + b] yield b; } } } for ( const i of Fibonacci) { console.log(i); } //=> 0 1 1 2 3 5 8 13 21 34 55 89 144 ...
```

### `technical-atom-2fad7774095f2a2f` code

Citation: (raw/javascriptallonge.pdf p.236-239)

```javascript
function * fibonacci () { let a, b; yield a = 0; yield b = 1; while ( true ) { [a, b] = [b, a + b] yield b; } } for ( const i of fibonacci()) { console.log(i); } //=> 0 1 1 2 3 5 8 13 21 34 55 89 144 ...
```

### `technical-atom-e1aa0d60f3c9e86a` worked-example

Citation: (raw/javascriptallonge.pdf p.236-239)

Our OneTwoThree example used implicit state to output the numbers in sequence.
