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

### `technical-atom-211166ddde5ca25f` worked-example

Citation: (raw/javascriptallonge.pdf p.229-230)

Again, this is not particularly horrendous, but like the recursive example, we're explicitly greenspunning the natural linear state.

### `technical-atom-1c71905df1a926c6` procedure

Citation: (raw/javascriptallonge.pdf p.229-230)

In a generator, we write 'do this, then this, then this.' In an iterator, we have to wrap that up and explicitly keep track of what step we're on.

### `technical-atom-01efb8331f065136` requirement

Citation: (raw/javascriptallonge.pdf p.229-230)

Whereas the iteration version must make that state explicit.
