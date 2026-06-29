---
page_id: javascriptallonge-section-we-ll-keep-it-simple-interlude-the-carpenter-interviews-for-a-job-the-problem-69f83674
page_kind: source
summary: We'll keep it simple: / Interlude: The Carpenter Interviews for a Job / the problem: 13 source-backed entries and 5 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-29
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-we-ll-keep-it-simple-interlude-the-carpenter-interviews-for-a-job-the-problem-69f83674@dfc6110ce564b68eed978322bf7752dc
---

# We'll keep it simple: / Interlude: The Carpenter Interviews for a Job / the problem

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-we-ll-keep-it-simple-interlude-the-carpenter-interviews-for-a-job-196a6679]] - broader source section: We'll keep it simple: / Interlude: The Carpenter Interviews for a Job
- [[javascriptallonge-problem]] - topic hub: opens the topic page for Problem

## Statements

- After some small talk, Christine explained that they liked to ask candidates to whiteboard some code. Despite his experience and industry longevity, the Carpenter did not mind being asked to demonstrate that he was, in fact, the person described on the resumé. _(javascriptallonge.pdf (source-range-7239e085-01813))_
- Many companies use white-boarding code as an excuse to have a technical conversation with a candidate, and The Carpenter felt that being asked to whiteboard code was an excuse to have a technical conversation with a future colleague. 'Win, win' he thought to himself. _(javascriptallonge.pdf (source-range-7239e085-01814))_
- Consider a finite checkerboard of unknown size. On each square, we randomly place an arrow pointing to one of its four sides. A chequer is placed randomly on the checkerboard. Each move consists of moving the chequer one square in the direction of the arrow in the square it occupies. If the arrow should cause the chequer to move off the edge of the board, the game halts. _(javascriptallonge.pdf (source-range-7239e085-01818))_
- The problem is this: The game board is hidden from us. A player moves the chequer, following the rules. As the player moves the chequer, they calls out the direction of movement, e.g. '↑, →, ↑, ↓, ↑, →…' Write an algorithm that will determine whether the game halts, strictly from the called out directions, in finite time and space. _(javascriptallonge.pdf (source-range-7239e085-01819))_
- Christine interrupted. 'To save time, we have written a template of the solution for you in ECMASCript 2015 notation. Fill in the blanks. Your code should not presume anything about the game-board's size or contents, only that it is given an arrow every time though the while loop. You may use babeljs.io 95 , or ES6Fiddle 96 to check your work. ' _(javascriptallonge.pdf (source-range-7239e085-01821))_
- After some small talk, Christine explained that they liked to ask candidates to whiteboard some code. _(javascriptallonge.pdf (source-range-7239e085-01813))_
- Your code should not presume anything about the game-board's size or contents, only that it is given an arrow every time though the while loop. _(javascriptallonge.pdf (source-range-7239e085-01821))_

## Technical atoms

### Technical frame 1: We'll keep it simple: / Interlude: The Carpenter Interviews for a Job / the problem

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01818))_

> Consider a finite checkerboard of unknown size. On each square, we randomly place an arrow pointing to one of its four sides. A chequer is placed randomly on the checkerboard. Each move consists of moving the chequer one square in the direction of the arrow in the square it occupies. If the arrow should cause the chequer to move off the edge of the board, the game halts.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01816))_

> [Figure] (p.262)

### Technical frame 2: We'll keep it simple: / Interlude: The Carpenter Interviews for a Job / the problem

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01819))_

> The problem is this: The game board is hidden from us. A player moves the chequer, following the rules. As the player moves the chequer, they calls out the direction of movement, e.g. '↑, →, ↑, ↓, ↑, →…' Write an algorithm that will determine whether the game halts, strictly from the called out directions, in finite time and space.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01818))_

> If the arrow should cause the chequer to move off the edge of the board, the game halts.

### Technical frame 3: We'll keep it simple: / Interlude: The Carpenter Interviews for a Job / the problem

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01819))_

> The problem is this: The game board is hidden from us. A player moves the chequer, following the rules. As the player moves the chequer, they calls out the direction of movement, e.g. '↑, →, ↑, ↓, ↑, →…' Write an algorithm that will determine whether the game halts, strictly from the called out directions, in finite time and space.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01821))_

> You may use babeljs.io 95 , or ES6Fiddle 96 to check your work.

### Technical frame 4: We'll keep it simple: / Interlude: The Carpenter Interviews for a Job / the problem

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01821))_

> Christine interrupted. 'To save time, we have written a template of the solution for you in ECMASCript 2015 notation. Fill in the blanks. Your code should not presume anything about the game-board's size or contents, only that it is given an arrow every time though the while loop. You may use babeljs.io 95 , or ES6Fiddle 96 to check your work. '

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01824))_

```
const Game = (size = 8) => {
// initialize the board
const board = [];
for (let i = 0; i < size; ++i) {
board[i] = [];
for (let j = 0; j < size; ++j) {
board[i][j] = '￿￿￿￿'[Math.floor(Math.random() * 4)];
}
}
// initialize the position
let initialPosition = [
2 + Math.floor(Math.random() * (size - 4)),
2 + Math.floor(Math.random() * (size - 4))
];
// ???
let [x, y] = initialPosition;
const MOVE = {
"￿": ([x, y]) => [x - 1, y],
"￿": ([x, y]) => [x + 1, y],
"￿": ([x, y]) => [x, y - 1],
"￿": ([x, y]) => [x, y + 1]
};
while (x >= 0 && y >=0 && x < size && y < size) {
const arrow = board[x][y];
// ???
[x, y] = MOVE[arrow]([x, y]);
}
// ???
};
```

### Technical atom 5

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01823))_

> Christine quickly scribbled on the whiteboard:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01825))_

| entry | content |
| --- | --- |
| 95 | http://babeljs.io |
| 96 | http://www.es6fiddle.net |

<details>
<summary>Raw table text</summary>

```
95 http://babeljs.io
96 http://www.es6fiddle.net
```

</details>
