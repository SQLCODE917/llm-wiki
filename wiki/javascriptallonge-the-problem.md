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

### `technical-atom-11b62cbf365786b9` worked-example

Citation: (raw/javascriptallonge.pdf p.261-264)

Consider a finite checkerboard of unknown size.

### `technical-atom-57b7e0f27976b463` requirement

Citation: (raw/javascriptallonge.pdf p.261-264)

If the arrow should cause the chequer to move off the edge of the board, the game halts.

### `technical-atom-f00105e5cc810ebe` exception

Citation: (raw/javascriptallonge.pdf p.261-264)

Your code should not presume anything about the game-board's size or contents, only that it is given an arrow every time though the while loop.

### `technical-atom-e1703c9d18f73547` code

Citation: (raw/javascriptallonge.pdf p.261-264)

```
let [x, y] = initialPosition; const MOVE = { "￿": ([x, y]) => [x - 1, y], "￿": ([x, y]) => [x + 1, y], "￿": ([x, y]) => [x, y - 1], "￿": ([x, y]) => [x, y + 1] }; while (x >= 0 && y >=0 && x < size && y < size) { const arrow = board[x][y]; // ???
```
