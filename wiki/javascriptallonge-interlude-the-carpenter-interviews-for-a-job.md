---
page_id: javascriptallonge-interlude-the-carpenter-interviews-for-a-job
page_kind: source
summary: Interlude: The Carpenter Interviews for a Job from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.261-272
updated: 2026-06-25
source_id: javascriptallonge.pdf
---

## Source record

The Carpenter solves a checkerboard game problem involving cycle detection (unknown).

## Key supported claims

- The Carpenter solves a checkerboard game problem involving cycle detection (raw/javascriptallonge.pdf p.261-272).
- The solution uses iterables and a statefulMapWith function to transform directions into positions (raw/javascriptallonge.pdf p.261-272).
- The Carpenter uses the Tortoise and Hare algorithm to detect cycles in the game (raw/javascriptallonge.pdf p.261-272).
- An alternative solution using a Set for cycle detection is presented (raw/javascriptallonge.pdf p.261-272).
- The interview question is presented as a whiteboard problem with a focus on technical conversation (raw/javascriptallonge.pdf p.261-272).

## Technical details

### `technical-atom-07a8bdc872cc7e0f` code

Citation: (raw/javascriptallonge.pdf p.261-272)

```javascript
const Game = (size = 8) => {
```

### `technical-atom-89c2a855c1048b32` code

Citation: (raw/javascriptallonge.pdf p.261-272)

```javascript
// initialize the board const board = []; for ( let i = 0; i < size; ++i) { board[i] = []; for ( let j = 0; j < size; ++j) { board[i][j] = '￿￿￿￿'[Math.floor(Math.random() * 4)]; } } // initialize the position let initialPosition = [ 2 + Math.floor(Math.random() * (size - 4)), 2 + Math.floor(Math.random() * (size - 4))]; // ??? let [x, y] = initialPosition; const MOVE = { "￿": ([x, y]) => [x - 1, y], "￿": ([x, y]) => [x + 1, y], "￿": ([x, y]) => [x, y - 1], "￿": ([x, y]) => [x, y + 1] }; while (x >= 0 && y >=0 && x < size && y < size) { const arrow = board[x][y]; // ??? [x, y] = MOVE[arrow]([x, y]); } // ??? }; 95http://babeljs.io 96http://www.es6fiddle.net
```

### `technical-atom-246a3172d533c6e9` code

Citation: (raw/javascriptallonge.pdf p.261-272)

```javascript
const MOVE = { "￿": ([x, y]) => [x - 1, y], "￿": ([x, y]) => [x + 1, y], "￿": ([x, y]) => [x, y + 1], "￿": ([x, y]) => [x, y - 1] };
```

### `technical-atom-e431a95e17a7d6c4` code

Citation: (raw/javascriptallonge.pdf p.261-272)

```javascript
const Board = (size = 8) => {
```

### `technical-atom-a65fef78efa5a8f9` code

Citation: (raw/javascriptallonge.pdf p.261-272)

```javascript
// initialize the board const board = []; for ( let i = 0; i < size; ++i) { board[i] = []; for ( let j = 0; j < size; ++j) { board[i][j] = '￿￿￿￿'[Math.floor(Math.random() * 4)]; } } // initialize the position const position = [
```

### `technical-atom-ed163592b7eb45a1` code

Citation: (raw/javascriptallonge.pdf p.261-272)

```
Math.floor(Math.random() * size), Math.floor(Math.random() * size)]; return {board, position}; };
```

### `technical-atom-db72a72e5a5f140f` code

Citation: (raw/javascriptallonge.pdf p.261-272)

```javascript
const Game = ({board, position}) => {
```

### `technical-atom-70469382ed227148` code

Citation: (raw/javascriptallonge.pdf p.261-272)

```javascript
const size = board[0].length; return ({ *[Symbol.iterator] () { let [x, y] = position; while (x >= 0 && y >=0 && x < size && y < size) { const direction = board[y][x]; yield direction; [x, y] = MOVE[direction]([x, y]); } } }); };
```

## Related technical details

### From [[javascriptallonge-iteration-and-iterables]]: `technical-atom-be126e6eb38ca51a` code

Relation: nearby source page; matched terms `code`, `function`, `iterables`, `javascript`, `uses`

Citation: (raw/javascriptallonge.pdf p.206-223)

```javascript
The .iterator() method is defined with shorthand equivalent to iterator: function iterator() { ... }. Note that it uses the function keyword, so when we invoke it with stack.iterator(), JavaScript sets this to the value of stack. But what about the function .iterator() returns? It is defined with a fat arrow () => { ... }. What is the value of this within that function?
```

### From [[javascriptallonge-basic-operations-on-iterables]]: `technical-atom-06f854f6dd0c3ede` code

Relation: nearby source page; matched terms `code`, `function`, `iterable`, `iterables`

Citation: (raw/javascriptallonge.pdf p.284-287)

```javascript
function * mapWith(fn, iterable) { for ( const element of iterable) { yield fn(element); } } function * mapAllWith (fn, iterable) { for ( const element of iterable) { yield * fn(element); } } function * filterWith (fn, iterable) { for ( const element of iterable) { if (!!fn(element)) yield element; } } function * compact (iterable) { for ( const element of iterable) { if (element != null) yield element; } } function * untilWith (fn, iterable) { for ( const element of iterable) { if (fn(element)) break; yield fn(element); } } function * rest (iterable) { const iterator = iterable[Symbol.iterator](); iterator.next();
```

### From [[javascriptallonge-basic-operations-on-iterables]]: `technical-atom-63329da7d920a7fa` code

Relation: nearby source page; matched terms `code`, `function`, `iterable`, `iterables`

Citation: (raw/javascriptallonge.pdf p.284-287)

```javascript
function * take (numberToTake, iterable) { const iterator = iterable[Symbol.iterator]();
```

### From [[javascriptallonge-lazy-and-eager-collections]]: `technical-atom-a52c46f037bbeeb7` code

Relation: nearby source page; matched terms `code`, `function`, `key`

Citation: (raw/javascriptallonge.pdf p.246-260)

```javascript
const extend = function (consumer, ...providers) { for ( let i = 0; i < providers.length; ++i) { const provider = providers[i]; for ( let key in provider) { if (provider.hasOwnProperty(key)) { consumer[key] = provider[key] } } } return consumer }; const LazyCollection = { map(fn) { return Object.assign({ [Symbol.iterator]: () => { const iterator = this [Symbol.iterator](); return { next: () => { const { done, value } = iterator.next(); return ({ done, value: done ? undefined: fn(value) }); } } } }, LazyCollection); }, reduce(fn, seed) { const iterator = this [Symbol.iterator](); let iterationResult, accumulator = seed; while ((iterationResult = iterator.next(), !iterationResult.done)) { accumulator = fn(accumulator, iterationResult.value); } return accumulator;
```
