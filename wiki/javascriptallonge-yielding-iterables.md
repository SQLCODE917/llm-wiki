---
page_id: javascriptallonge-yielding-iterables
page_kind: source
summary: yielding iterables from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.239-243
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

Chapter on yielding iterables from JavaScript Allongé, covering tree iteration and the use of yield*.

## Key supported claims

- We take advantage of the for...of loop in a plain and direct way: For each element e, if it is iterable, treat it as a tree and iterate over it, yielding each of its elements. This approach works well and is simpler than maintaining our own stack (raw/javascriptallonge.pdf p.239-243).
- Tucked inside of it is the same three-line idiom for yielding each element of an iterable, which can be abbreviated using yield* (raw/javascriptallonge.pdf p.239-243).
- A function that returns an iterable can often be written much more simply as a generator, rather than a function that returns an iterable object (raw/javascriptallonge.pdf p.239-243).
- append iterates over a collection of iterables, one element at a time (raw/javascriptallonge.pdf p.239-243).
- yield* is handy when writing generator functions that operate on or create iterables (raw/javascriptallonge.pdf p.239-243).

## Technical details

### `technical-atom-bf1e9608a096d6b8` code

Citation: (raw/javascriptallonge.pdf p.239-243)

```javascript
const isIterable = (something) => !!something[Symbol.iterator]; const TreeIterable = (iterable) => ({ [Symbol.iterator]: function * () { for ( const e of iterable) { if (isIterable(e)) { for ( const ee of TreeIterable(e)) { yield ee; } } else { yield e; } } } }) for ( const i of TreeIterable([1, [2, [3, 4], 5]])) { console.log(i); } //=> 1 2 3 4 5
```

### `technical-atom-d1aa9123c297089a` code

Citation: (raw/javascriptallonge.pdf p.239-243)

```javascript
function * tree (iterable) { for ( const e of iterable) { if (isIterable(e)) { for ( const ee of tree(e)) { yield ee; } } else { yield e; } } }; for ( const i of tree([1, [2, [3, 4], 5]])) { console.log(i); } //=> 1 2 3 4 5
```

### `technical-atom-875532cb48273d2f` code

Citation: (raw/javascriptallonge.pdf p.239-243)

```javascript
for ( const ee of tree(e)) { yield ee; }
```

### `technical-atom-4142e18769c82ac5` code

Citation: (raw/javascriptallonge.pdf p.239-243)

```javascript
function * append (...iterables) { for ( const iterable of iterables) { for ( const element of iterable) { yield element; } } } const lyrics = append(["a", "b", "c"], ["one", "two", "three"], ["do", "re", "me\ "]); for ( const word of lyrics) { console.log(word); } //=> a b c one two three do re me
```

### `technical-atom-e0a54f75af41d7b2` code

Citation: (raw/javascriptallonge.pdf p.239-243)

```javascript
function * append (...iterables) { for ( const iterable of iterables) { yield * iterable; } } const lyrics = append(["a", "b", "c"], ["one", "two", "three"], ["do", "re", "me\ "]); for ( const word of lyrics) { console.log(word); }
```

### `technical-atom-98324c7d9ef2bf54` code

Citation: (raw/javascriptallonge.pdf p.239-243)

```javascript
//=> a b c one two do re
```

### `technical-atom-a5b4a3116b590bc6` code

Citation: (raw/javascriptallonge.pdf p.239-243)

```javascript
const isIterable = (something) => !!something[Symbol.iterator]; function * tree (iterable) { for ( const e of iterable) { if (isIterable(e)) { yield * tree(e); } else { yield e; } } }; for ( const i of console.log(i); } //=> 1 2 3 4 5
```

### `technical-atom-b1c05692e4772b6e` code

Citation: (raw/javascriptallonge.pdf p.239-243)

```
three me yield * yields all of the elements of an iterable, in order. We can use it in tree , too: tree([1, [2, [3, 4], 5]])) {
```
