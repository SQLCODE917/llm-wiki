---
page_id: javascriptallonge-the-carpenter-s-solution
page_kind: source
summary: the carpenter's solution from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.264-269
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

The carpenter's solution to the loop detection problem in linked lists and chequerboard games, as presented in 'javascriptallonge'.

## Key supported claims

- The Carpenter was not surprised at the problem, as Bob Plissken, a crafty recruiter, often prepared candidates with information about interview questions, including loop detection problems (raw/javascriptallonge.pdf p.264-269).
- To save time, The Carpenter had prepared the same answer for both questions about loop detection in linked lists and chequerboard games (raw/javascriptallonge.pdf p.264-269).
- Bob had, in fact, warned The Carpenter that 'Thing' liked to ask either or both of two questions: Determine how to detect a loop in a linked list, and determine whether the chequerboard game would halt (raw/javascriptallonge.pdf p.264-269).
- The Carpenter coughed softly, then began, introducing the solution using iterables and a statefulMapWith utility function (raw/javascriptallonge.pdf p.264-269).

## Technical details

### `technical-atom-b82829c9e5e93de3` code

Citation: (raw/javascriptallonge.pdf p.264-269)

```javascript
const MOVE = { "￿": ([x, y]) => [x - 1, y], "￿": ([x, y]) => [x + 1, y], "￿": ([x, y]) => [x, y + 1], "￿": ([x, y]) => [x, y - 1] }; const Board = (size = 8) => { // initialize the board const board = []; for ( let i = 0; i < size; ++i) { board[i] = []; for ( let j = 0; j < size; ++j) { board[i][j] = '￿￿￿￿'[Math.floor(Math.random() * 4)]; } } // initialize the position const position = [
```

### `technical-atom-4447f89fa1fdcec5` code

Citation: (raw/javascriptallonge.pdf p.264-269)

```javascript
Math.floor(Math.random() * size), Math.floor(Math.random() * size) ]; return {board, position}; }; const Game = ({board, position}) => { const size = board[0].length; return ({ *[Symbol.iterator] () { let [x, y] = position; while (x >= 0 && y >=0 && x < size && y < size) { const direction = board[y][x]; yield direction; [x, y] = MOVE[direction]([x, y]); } } }); };
```

### `technical-atom-63c6324c59ccb97e` code

Citation: (raw/javascriptallonge.pdf p.264-269)

```javascript
const statefulMapWith = (fn, seed, iterable) => ({ *[Symbol.iterator] () { let value, state = seed; for ( let element of iterable) { [state, value] = fn(state, element); yield value;
```

### `technical-atom-f3bbd64b055df046` code

Citation: (raw/javascriptallonge.pdf p.264-269)

```
} } });
```

### `technical-atom-cfc70520e219f389` code

Citation: (raw/javascriptallonge.pdf p.264-269)

```javascript
const positionsOf = (game) => statefulMapWith( (position, direction) => { const [x, y] = MOVE[direction](position); position = [x, y]; return [position, `x: ${ x } , y: ${ y } `]; }, [0, 0], game);
```

### `technical-atom-397da5d6445954ea` code

Citation: (raw/javascriptallonge.pdf p.264-269)

```javascript
const tortoiseAndHare = (iterable) => { const hare = iterable[Symbol.iterator](); let hareResult = (hare.next(), hare.next()); for ( let tortoiseValue of iterable) { hareResult = hare.next(); if (hareResult.done) { return false ; } if (tortoiseValue === hareResult.value) { return true ; } hareResult = hare.next(); if (hareResult.done) { return false ; } if (tortoiseValue === hareResult.value) { return true ; } } return false ; };
```

### `technical-atom-38c104b7ffd476a8` code

Citation: (raw/javascriptallonge.pdf p.264-269)

```javascript
const terminates = (game) => tortoiseAndHare(positionsOf(game)) const test = [ ["￿","￿","￿","￿"], ["￿","￿","￿","￿"], ["￿","￿","￿","￿"], ["￿","￿","￿","￿"] ]; terminates(Game({board: test, position: [0, 0]})) //=> false terminates(Game({board: test, position: [3, 0]})) //=> true terminates(Game({board: test, position: [0, 3]})) //=> false terminates(Game({board: test, position: [3, 3]})) //=> false
```

### `technical-atom-b2ed369ffed015a8` procedure

Citation: (raw/javascriptallonge.pdf p.264-269)

He then coached subsequent candidates to give polished answers to the company's pet technical questions.

## Related technical details

### From [[javascriptallonge-the-problem]]: `technical-atom-f00105e5cc810ebe` exception

Relation: nearby source page; matched terms `about`, `loop`, `not`, `problem`, `time`

Citation: (raw/javascriptallonge.pdf p.261-264)

Your code should not presume anything about the game-board's size or contents, only that it is given an arrow every time though the while loop.

### From [[javascriptallonge-implementing-methods-with-iteration]]: `technical-atom-c66bcf65c2866661` code

Relation: nearby source page; matched terms `linked`, `lists`

Citation: (raw/javascriptallonge.pdf p.246-253)

```javascript
const Numbers = Object.assign({ [Symbol.iterator]: () => { let n = 0; return { next: () => ({done: false , value: n++}) } } }, LazyCollection); // Pair, a/k/a linked lists const EMPTY = { isEmpty: () => true
```

### From [[javascriptallonge-lazy-collection-operations]]: `technical-atom-744115e2e3a310d4` procedure

Relation: nearby source page; matched terms `answer`, `procedure`, `two`

Citation: (raw/javascriptallonge.pdf p.253-256)

Finally, we take the first element of that filtered, squared iterable and now JavaScript actually iterates over the stack's elements, and it only needs to square two of those elements, 29 and 28 , to return the answer.
