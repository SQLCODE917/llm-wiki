---
page_id: javascriptallonge-generating-iterables
page_kind: source
summary: Generating Iterables from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.224-226
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

This chapter explains how iterables and generators work in JavaScript, covering iterator protocols, recursive iteration, state machines, and generator syntax.

## Key supported claims

- Iterables look cool, but then again, everything looks amazing when you're given cherry-picked examples. What is there they don't do well? (raw/javascriptallonge.pdf p.224-226)
- Whether it's a simple functional iterator, or an iterable object with a .next() method, an iterator is something we call repeatedly until it tells us that it's done. (raw/javascriptallonge.pdf p.224-226)
- Iterators have to arrange its own state such that when you call them, they compute and return the next item. (raw/javascriptallonge.pdf p.224-226)

## Technical details

### `technical-atom-25debf1bd5150c87` code

Citation: (raw/javascriptallonge.pdf p.224-226)

```javascript
const Numbers = { [Symbol.iterator]: () => { let n = 0; return { next: () => ({done: false , value: n++}) } } };
```

### `technical-atom-a98fa92391927baf` code

Citation: (raw/javascriptallonge.pdf p.224-226)

```javascript
let n = 0; while ( true ) { console.log(n++) }
```

### `technical-atom-331f02c2738cde63` code

Citation: (raw/javascriptallonge.pdf p.224-226)

```javascript
// Iteration let n = 0; () => ({done: false , value: n++}) // Generation let n = 0; while ( true ) { console.log(n++) }
```

### `technical-atom-4317039718eba4b5` procedure

Citation: (raw/javascriptallonge.pdf p.224-226)

Iterables look cool, but then again, everything looks amazing when you're given cherry-picked examples.

### `technical-atom-d5b243613b22833a` worked-example

Citation: (raw/javascriptallonge.pdf p.224-226)

Let's consider how they work.

### `technical-atom-efb7e60dcd1e8dce` procedure

Citation: (raw/javascriptallonge.pdf p.224-226)

Whether it's a simple functional iterator, or an iterable object with a .next() method, an iterator is something we call repeatedly until it tells us that it's done.

### `technical-atom-10b9ccb62f560bfc` procedure

Citation: (raw/javascriptallonge.pdf p.224-226)

Iterators have to arrange its own state such that when you call them, they compute and return the next item.

### `technical-atom-e82674fd1d436f3a` worked-example

Citation: (raw/javascriptallonge.pdf p.224-226)

If, for example, you want numbers, you write:
