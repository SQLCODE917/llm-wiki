---
page_id: javascriptallonge-from
page_kind: source
summary: from from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.221-222
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

This section discusses how to create .from functions to gather iterables into particular collection types, using JavaScript's built-in Array.from and custom implementations for other collections like Stack3 and Pair1.

## Key supported claims

- One useful thing is to write a .from function that gathers an iterable into a particular collection type. (raw/javascriptallonge.pdf p.221-222)
- As you recall, functions are mutable objects. (raw/javascriptallonge.pdf p.221-222)
- No, of course not, we can do anything we like with them. (raw/javascriptallonge.pdf p.221-222)

## Technical details

### `technical-atom-dac42232b1dd6899` code

Citation: (raw/javascriptallonge.pdf p.221-222)

```javascript
Array.from(UpTo1000) //=> [1,81,121,361,441,841,961]
```

### `technical-atom-096e3d7cf4be2948` code

Citation: (raw/javascriptallonge.pdf p.221-222)

```javascript
Stack3.from = function (iterable) { const stack = this (); for ( let element of iterable) { stack.push(element); } return stack; } Pair1.from = (iterable) => ( function iterationToList (iteration) { const {done, value} = iteration.next(); return done ? EMPTY : Pair1(value, iterationToList(iteration)); })(iterable[Symbol.iterator]())
```

### `technical-atom-bb3f798ec6996bf9` code

Citation: (raw/javascriptallonge.pdf p.221-222)

```javascript
const numberList = Pair1.from(untilWith((x) => x > 10, Numbers)); Pair1.from(Squares) //=> {"first":0, "rest":{"first":1, "rest":{"first":4, "rest":{ ...
```

### `technical-atom-dd469f1aaeba06ba` exception

Citation: (raw/javascriptallonge.pdf p.221-222)

Having iterated over a collection, are we limited to for..do and/or gathering the elements in an array literal and/or gathering the elements into the parameters of a function?
