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

### `technical-atom-f552e8bca51f04a8` worked-example

Citation: (raw/javascriptallonge.pdf p.230-231)

Let's start with the degenerate example, the empty iterator : 91

### `technical-atom-595c724b56877ae5` procedure

Citation: (raw/javascriptallonge.pdf p.230-231)

We call its .next() method, but it's done immediately.
