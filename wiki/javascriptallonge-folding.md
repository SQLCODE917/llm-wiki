---
page_id: javascriptallonge-folding
page_kind: source
summary: folding from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.114-116
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

This chapter discusses the concept of folding in JavaScript, showing how to implement functions like sumSquares, map, and length using fold operations.

## Key supported claims

- With the exception of the length example at the beginning, our examples so far all involve rebuilding a solution using spreads (raw/javascriptallonge.pdf p.114-116).
- We can represent a map as a fold, we just need to supply the array rebuilding code (raw/javascriptallonge.pdf p.114-116).
- And to return to our first example, our version of length can be written as a fold (raw/javascriptallonge.pdf p.114-116).

## Technical details

### `technical-atom-94a8db2caee75654` code

Citation: (raw/javascriptallonge.pdf p.114-116)

```javascript
const sumSquares = ([first, ...rest]) => first === undefined ? 0 : first * first + sumSquares(rest); sumSquares([1, 2, 3, 4, 5]) //=> 55
```

### `technical-atom-b27f3cddbf310b14` code

Citation: (raw/javascriptallonge.pdf p.114-116)

```javascript
const foldWith = (fn, terminalValue, [first, ...rest]) => first === undefined ? terminalValue : fn(first, foldWith(fn, terminalValue, rest));
```

### `technical-atom-78c1e74ef23a23a8` code

Citation: (raw/javascriptallonge.pdf p.114-116)

```javascript
foldWith((number, rest) => number * number + rest, 0, [1, 2, 3, 4, 5]) //=> 55
```

### `technical-atom-c305b302eeee5afb` code

Citation: (raw/javascriptallonge.pdf p.114-116)

```javascript
const squareAll = (array) => foldWith((first, rest) => [first * first, ...rest],\ [], array); squareAll([1, 2, 3, 4, 5]) //=> [1,4,9,16,25]
```

### `technical-atom-629c21e9ad75fc76` code

Citation: (raw/javascriptallonge.pdf p.114-116)

```javascript
const mapWith = (fn, array) => foldWith((first, rest) => [fn(first), ...rest], [\ ], array), squareAll = (array) => mapWith((x) => x * x, array); squareAll([1, 2, 3, 4, 5]) //=> [1,4,9,16,25]
```

### `technical-atom-f8baa94a1544e5b8` code

Citation: (raw/javascriptallonge.pdf p.114-116)

```javascript
const length = (array) => foldWith((first, rest) => 1 + rest, 0, array); length([1, 2, 3, 4, 5]) //=> 5
```

### `technical-atom-f3ee4de0231c05c2` worked-example

Citation: (raw/javascriptallonge.pdf p.114-116)

With the exception of the length example at the beginning, our examples so far all involve rebuilding a solution using spreads.

### `technical-atom-d696b45dc218ef5e` worked-example

Citation: (raw/javascriptallonge.pdf p.114-116)

And to return to our first example, our version of length can be written as a fold:

## Related technical details

### From [[javascriptallonge-linear-recursion]]: `technical-atom-0f5d51c0613f0645` code

Relation: nearby source page; matched terms `array`, `code`, `first`, `return`

Citation: (raw/javascriptallonge.pdf p.111-113)

```javascript
const flatten = ([first, ...rest]) => { if (first === undefined ) { return []; } else if (!Array.isArray(first)) { return [first, ...flatten(rest)]; } else { return [...flatten(first), ...flatten(rest)]; } } flatten(["foo", [3, 4, []]]) //=> ["foo",3,4]
```

### From [[javascriptallonge-self-similarity]]: `technical-atom-5d9fe5bf28074a51` exception

Relation: nearby source page; matched terms `examples`, `exception`, `our`

Citation: (raw/javascriptallonge.pdf p.109-111)

61 Well, actually, this does not work for arrays that contain undefined as a value, but we are not going to see that in our examples.

### From [[javascriptallonge-tail-calls-and-default-arguments]]: `technical-atom-14898c90c9499167` code

Relation: nearby source page; matched terms `code`, `first`, `function`, `return`

Citation: (raw/javascriptallonge.pdf p.117-118)

```javascript
const mapWith = function (fn, [first, ...rest]) { if (first === undefined ) { return []; } else { const _temp1 = fn(first), _temp2 = mapWith(fn, rest), _temp3 = [_temp1, ..._temp2]; return _temp3; } }
```

### From [[javascriptallonge-tail-call-optimization]]: `technical-atom-d96c8d42a851c268` code

Relation: nearby source page; matched terms `code`, `function`, `length`, `return`

Citation: (raw/javascriptallonge.pdf p.119)

```javascript
const maybe = (fn) => function (...args) { if (args.length === 0) { return ; } else { for ( let arg of args) { if (arg == null ) return ; } return fn.apply( this , args); } }
```
