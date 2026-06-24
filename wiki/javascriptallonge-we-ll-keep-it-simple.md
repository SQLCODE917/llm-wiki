---
page_id: javascriptallonge-we-ll-keep-it-simple
page_kind: source
summary: We'll keep it simple: from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.229-230
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

This section contrasts the use of generators and iterators in JavaScript, focusing on how state is handled in each approach.

## Key supported claims

- In a generator, we write 'do this, then this, then this.' In an iterator, we have to wrap that up and explicitly keep track of what step we're on. (raw/javascriptallonge.pdf p.229-230)
- So we see the same thing: The generation version has state, but it's implicit in JavaScript's linear control flow. (raw/javascriptallonge.pdf p.229-230)
- Whereas the iteration version must make that state explicit. (raw/javascriptallonge.pdf p.229-230)

## Technical details

### `technical-atom-a586853268640bbd` code

Citation: (raw/javascriptallonge.pdf p.229-230)

```javascript
// Iteration let a, b, state = 0; const fibonacci = () => { switch (state) { case 0: state = 1; return a = 0; case 1: state = 2; return b = 1; case 2: [a, b] = [b, a + b]; return b } }; while ( true ) { console.log(fibonacci()); } //=> 0 1 1 2 3 5 8 13
```

### `technical-atom-875b229bac9f6fd0` code

Citation: (raw/javascriptallonge.pdf p.229-230)

```
21 34 55 89 144 ...
```

### `technical-atom-1c71905df1a926c6` procedure

Citation: (raw/javascriptallonge.pdf p.229-230)

In a generator, we write 'do this, then this, then this.' In an iterator, we have to wrap that up and explicitly keep track of what step we're on.

### `technical-atom-01efb8331f065136` requirement

Citation: (raw/javascriptallonge.pdf p.229-230)

Whereas the iteration version must make that state explicit.

### `technical-atom-211166ddde5ca25f` worked-example

Citation: (raw/javascriptallonge.pdf p.229-230)

Again, this is not particularly horrendous, but like the recursive example, we're explicitly greenspunning the natural linear state.

## Related technical details

### From [[javascriptallonge-iteration]]: `technical-atom-cae674bcd9bcea03` procedure

Relation: nearby source page; matched terms `function`, `iteration`, `procedure`, `simple`, `use`, `version`

Citation: (raw/javascriptallonge.pdf p.227-228)

A less kind way to put it is that the iteration version is greenspunning something built into our programming language: We're reinventing the use of a stack to manage recursion, because writing our code to respond to a function call makes us turn a simple recursive algorithm inside-out.

### From [[javascriptallonge-iteration]]: `technical-atom-b526abb079ec9050` procedure

Relation: nearby source page; matched terms `explicit`, `iteration`, `iterator`, `procedure`, `version`

Citation: (raw/javascriptallonge.pdf p.227-228)

If you peel off isIterable and ignore the way that the iteration version uses [Symbol.iterator] and .next , we're left with the fact that the generating version calls itself recursively, and the iteration version maintains an explicit stack.

### From [[javascriptallonge-javascript-s-generators]]: `technical-atom-bd725d9058677fd9` formula

Relation: nearby source page; matched terms `but`, `function`, `generator`, `generators`, `javascript`, `write`

Citation: (raw/javascriptallonge.pdf p.230-231)

91 Wewrote a generator declaration . We can also write const empty = function * () {} to bind an anonymous generator to the empty keyword, but we don't need to do that here.

### From [[javascriptallonge-javascript-s-generators]]: `technical-atom-00fab8fb6887a7bc` procedure

Relation: nearby source page; matched terms `generator`, `generators`, `iterators`, `javascript`, `procedure`, `write`

Citation: (raw/javascriptallonge.pdf p.230-231)

It would be very nice if we could sometimes write iterators as a .next() method that gets called, and sometimes write out a generator.
