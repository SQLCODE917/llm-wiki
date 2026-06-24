---
page_id: javascriptallonge-the-problem
page_kind: source
summary: the problem from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.261-264
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

The problem involves a finite checkerboard of unknown size, where arrows point to one of four sides. A chequer is placed randomly on the board, and each move consists of moving the chequer one square in the direction of the arrow in the square it occupies. If the arrow should cause the chequer to move off the edge of the board, the game halts.

## Key supported claims

- The game board is hidden. (raw/javascriptallonge.pdf p.261-264)
- Player calls out directions as the chequer moves. (raw/javascriptallonge.pdf p.261-264)

## Technical details

### `technical-atom-304463e70ab0d5ba` code

Citation: (raw/javascriptallonge.pdf p.261-264)

```javascript
const Game = (size = 8) => { // initialize the board const board = []; for ( let i = 0; i < size; ++i) { board[i] = []; for ( let j = 0; j < size; ++j) { board[i][j] = '￿￿￿￿'[Math.floor(Math.random() * 4)]; } } // initialize the position let initialPosition = [ 2 + Math.floor(Math.random() * (size - 4)), 2 + Math.floor(Math.random() * (size - 4)) ]; // ??? let [x, y] = initialPosition; const MOVE = { "￿": ([x, y]) => [x - 1, y], "￿": ([x, y]) => [x + 1, y], "￿": ([x, y]) => [x, y - 1], "￿": ([x, y]) => [x, y + 1] }; while (x >= 0 && y >=0 && x < size && y < size) { const arrow = board[x][y]; // ??? [x, y] = MOVE[arrow]([x, y]); } // ??? };
```

### `technical-atom-e1703c9d18f73547` code

Citation: (raw/javascriptallonge.pdf p.261-264)

```
let [x, y] = initialPosition; const MOVE = { "￿": ([x, y]) => [x - 1, y], "￿": ([x, y]) => [x + 1, y], "￿": ([x, y]) => [x, y - 1], "￿": ([x, y]) => [x, y + 1] }; while (x >= 0 && y >=0 && x < size && y < size) { const arrow = board[x][y]; // ???
```

### `technical-atom-57b7e0f27976b463` requirement

Citation: (raw/javascriptallonge.pdf p.261-264)

If the arrow should cause the chequer to move off the edge of the board, the game halts.

### `technical-atom-f00105e5cc810ebe` exception

Citation: (raw/javascriptallonge.pdf p.261-264)

Your code should not presume anything about the game-board's size or contents, only that it is given an arrow every time though the while loop.

### `technical-atom-11b62cbf365786b9` worked-example

Citation: (raw/javascriptallonge.pdf p.261-264)

Consider a finite checkerboard of unknown size.

## Related technical details

### From [[javascriptallonge-the-carpenter-s-solution]]: `technical-atom-4447f89fa1fdcec5` code

Relation: nearby source page; matched terms `board`, `direction`, `game`, `move`, `size`

Citation: (raw/javascriptallonge.pdf p.264-269)

```javascript
Math.floor(Math.random() * size), Math.floor(Math.random() * size) ]; return {board, position}; }; const Game = ({board, position}) => { const size = board[0].length; return ({ *[Symbol.iterator] () { let [x, y] = position; while (x >= 0 && y >=0 && x < size && y < size) { const direction = board[y][x]; yield direction; [x, y] = MOVE[direction]([x, y]); } } }); };
```

### From [[javascriptallonge-the-carpenter-s-solution]]: `technical-atom-38c104b7ffd476a8` code

Relation: nearby source page; matched terms `board`, `game`

Citation: (raw/javascriptallonge.pdf p.264-269)

```javascript
const terminates = (game) => tortoiseAndHare(positionsOf(game)) const test = [ ["￿","￿","￿","￿"], ["￿","￿","￿","￿"], ["￿","￿","￿","￿"], ["￿","￿","￿","￿"] ]; terminates(Game({board: test, position: [0, 0]})) //=> false terminates(Game({board: test, position: [3, 0]})) //=> true terminates(Game({board: test, position: [0, 3]})) //=> false terminates(Game({board: test, position: [3, 3]})) //=> false
```

### From [[javascriptallonge-the-carpenter-s-solution]]: `technical-atom-b82829c9e5e93de3` code

Relation: nearby source page; matched terms `board`, `move`, `size`

Citation: (raw/javascriptallonge.pdf p.264-269)

```javascript
const MOVE = { "￿": ([x, y]) => [x - 1, y], "￿": ([x, y]) => [x + 1, y], "￿": ([x, y]) => [x, y + 1], "￿": ([x, y]) => [x, y - 1] }; const Board = (size = 8) => { // initialize the board const board = []; for ( let i = 0; i < size; ++i) { board[i] = []; for ( let j = 0; j < size; ++j) { board[i][j] = '￿￿￿￿'[Math.floor(Math.random() * 4)]; } } // initialize the position const position = [
```

### From [[javascriptallonge-the-carpenter-s-solution]]: `technical-atom-cfc70520e219f389` code

Relation: nearby source page; matched terms `direction`, `game`, `move`

Citation: (raw/javascriptallonge.pdf p.264-269)

```javascript
const positionsOf = (game) => statefulMapWith( (position, direction) => { const [x, y] = MOVE[direction](position); position = [x, y]; return [position, `x: ${ x } , y: ${ y } `]; }, [0, 0], game);
```
