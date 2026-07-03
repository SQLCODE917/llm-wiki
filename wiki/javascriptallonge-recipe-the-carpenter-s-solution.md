---
page_id: javascriptallonge-recipe-the-carpenter-s-solution
page_kind: recipe
page_family: recipe-pattern
summary: the carpenter's solution: reusable source-backed pattern with 12 statement(s) and 7 technical atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: the-carpenter-s-solution
projection_coverage: recipe-javascriptallonge-recipe-the-carpenter-s-solution@ac566dd4492084b6490f135a09f4c581
---

# the carpenter's solution

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-we-ll-keep-it-simple-interlude-the-carpenter-interviews-for-a-job-the-carpenter-s-solution-9074fc35]].
- Evidence roles: decision, constraint, procedure, explanation, example, technical-atom.

## Applicability And Rationale

- He then coached subsequent candidates to give polished answers to the company's pet technical questions. _(javascriptallonge.pdf (source-range-7239e085-01828))_
- The Carpenter was not surprised at the problem. _(javascriptallonge.pdf (source-range-7239e085-01828))_
- Bob had, in fact, warned The Carpenter that 'Thing' liked to ask either or both of two questions: Determine how to detect a loop in a linked list, and determine whether the chequerboard game would halt. _(javascriptallonge.pdf (source-range-7239e085-01830))_
- To save time, The Carpenter had prepared the same answer for both questions. _(javascriptallonge.pdf (source-range-7239e085-01830))_
- I'll refactor a touch to make things clearer, for example I'll extract the board to make it easier to test:' _(javascriptallonge.pdf (source-range-7239e085-01831))_
- The Carpenter coughed softly, then began. _(javascriptallonge.pdf (source-range-7239e085-01831))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01832)_

```
const MOVE = {
"￿": ([x, y]) => [x - 1, y],
"￿": ([x, y]) => [x + 1, y],
"￿": ([x, y]) => [x, y + 1],
"￿": ([x, y]) => [x, y - 1]
};
const Board = (size = 8) => {
// initialize the board
const board = [];
for (let i = 0; i < size; ++i) {
board[i] = [];
for (let j = 0; j < size; ++j) {
board[i][j] = '￿￿￿￿'[Math.floor(Math.random() * 4)];
}
}
// initialize the position
const position = [
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01833)_

```
Math.floor(Math.random() * size),
Math.floor(Math.random() * size)
];
return {board, position};
};
const Game = ({board, position}) => {
const size = board[0].length;
return ({
*[Symbol.iterator] () {
let [x, y] = position;
while (x >= 0 && y >=0 && x < size && y < size) {
const direction = board[y][x];
yield direction;
[x, y] = MOVE[direction]([x, y]);
}
}
});
};
```

### Atom 3: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01836)_

```
const statefulMapWith = (fn, seed, iterable) =>
({
*[Symbol.iterator] () {
let value,
state = seed;
for (let element of iterable) {
[state, value] = fn(state, element);
yield value;
```

### Atom 4: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01837)_

```
}
}
});
```

### Atom 5: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01839)_

```
const positionsOf = (game) =>
statefulMapWith(
(position, direction) => {
const [x, y] =
MOVE[direction](position);
position = [x, y];
return [position, `x: ${x}, y: ${y}`];
},
[0, 0],
game);
```

### Atom 6: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01845)_

```
const tortoiseAndHare = (iterable) => {
const hare = iterable[Symbol.iterator]();
let hareResult = (hare.next(), hare.next());
for (let tortoiseValue of iterable) {
hareResult = hare.next();
if (hareResult.done) {
return false;
}
if (tortoiseValue === hareResult.value) {
return true;
}
hareResult = hare.next();
if (hareResult.done) {
return false;
}
if (tortoiseValue === hareResult.value) {
return true;
}
}
return false;
};
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-we-ll-keep-it-simple-interlude-the-carpenter-interviews-for-a-job-the-carpenter-s-solution-9074fc35]]
