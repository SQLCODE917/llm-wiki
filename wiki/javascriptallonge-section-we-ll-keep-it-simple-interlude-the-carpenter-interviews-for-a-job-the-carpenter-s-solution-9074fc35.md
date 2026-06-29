---
page_id: javascriptallonge-section-we-ll-keep-it-simple-interlude-the-carpenter-interviews-for-a-job-the-carpenter-s-solution-9074fc35
page_kind: source
summary: We'll keep it simple: / Interlude: The Carpenter Interviews for a Job / the carpenter's solution: 24 source-backed entries and 8 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-29
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-we-ll-keep-it-simple-interlude-the-carpenter-interviews-for-a-job-the-carpenter-s-solution-9074fc35@42b1723ad1811e6dddeb1b1599d7c3cd
---

# We'll keep it simple: / Interlude: The Carpenter Interviews for a Job / the carpenter's solution

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-we-ll-keep-it-simple-interlude-the-carpenter-interviews-for-a-job-196a6679]] - broader source section: We'll keep it simple: / Interlude: The Carpenter Interviews for a Job

## Statements

- The Carpenter was not surprised at the problem. Bob Plissken was a crafty, almost reptilian recruiter that traded in information and secrets. Whenever Bob sent a candidate to a job interview, he debriefed them afterwards and got them to disclose what questions were asked in the interview. He then coached subsequent candidates to give polished answers to the company's pet technical questions. _(javascriptallonge.pdf (source-range-7239e085-01828))_
- Bob had, in fact, warned The Carpenter that 'Thing' liked to ask either or both of two questions: Determine how to detect a loop in a linked list, and determine whether the chequerboard game would halt. To save time, The Carpenter had prepared the same answer for both questions. _(javascriptallonge.pdf (source-range-7239e085-01830))_
- The Carpenter coughed softly, then began. 'To begin with, I'll transform a game into an iterable that generates arrows, using the 'Starman' notation for generators. I'll refactor a touch to make things clearer, for example I'll extract the board to make it easier to test:' _(javascriptallonge.pdf (source-range-7239e085-01831))_
- 'Now that we have an iterable, we can transform the iterable of arrows into an iterable of positions.' The Carpenter sketched quickly. 'We want to take the arrows and convert them to positions. For that, we'll map the Game iterable to positions. A statefulMap is a lazy map that preserves state from iteration to iteration. That's what we need, because we need to know the current position to map each move to the next position.' _(javascriptallonge.pdf (source-range-7239e085-01834))_
- 'We could draw positions as nodes in a graph, connected by arcs representing the arrows. Detecting whether the game terminates is equivalent to detecting whether the graph contains a cycle.' _(javascriptallonge.pdf (source-range-7239e085-01841))_
- 'There's an old joke that a mathematician is someone who will take a five-minute problem, then spend an hour proving it is equivalent to another problem they have already solved. I approached this question in that spirit. Now that we have created an iterable of values that can be compared with === , I can show you this function:' _(javascriptallonge.pdf (source-range-7239e085-01844))_
- 'A long time ago,' The Carpenter explained, 'Someone asked me a question in an interview. I have never forgotten the question, or the general form of the solution. The question was, Given a linked list, detect whether it contains a cycle. Use constant space. ' _(javascriptallonge.pdf (source-range-7239e085-01846))_
- He then coached subsequent candidates to give polished answers to the company's pet technical questions. _(javascriptallonge.pdf (source-range-7239e085-01828))_
- The Carpenter coughed softly, then began. _(javascriptallonge.pdf (source-range-7239e085-01831))_
- I'll refactor a touch to make things clearer, for example I'll extract the board to make it easier to test:' _(javascriptallonge.pdf (source-range-7239e085-01831))_
- That's what we need, because we need to know the current position to map each move to the next position.' _(javascriptallonge.pdf (source-range-7239e085-01834))_

## Technical atoms

### Technical frame 1: We'll keep it simple: / Interlude: The Carpenter Interviews for a Job / the carpenter's solution

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01834))_

> 'Now that we have an iterable, we can transform the iterable of arrows into an iterable of positions.' The Carpenter sketched quickly. 'We want to take the arrows and convert them to positions. For that, we'll map the Game iterable to positions. A statefulMap is a lazy map that preserves state from iteration to iteration. That's what we need, because we need to know the current position to map each move to the next position.'

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01832))_

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

### Technical frame 2: We'll keep it simple: / Interlude: The Carpenter Interviews for a Job / the carpenter's solution

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01834))_

> 'Now that we have an iterable, we can transform the iterable of arrows into an iterable of positions.' The Carpenter sketched quickly. 'We want to take the arrows and convert them to positions. For that, we'll map the Game iterable to positions. A statefulMap is a lazy map that preserves state from iteration to iteration. That's what we need, because we need to know the current position to map each move to the next position.'

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01833))_

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

### Technical frame 3: We'll keep it simple: / Interlude: The Carpenter Interviews for a Job / the carpenter's solution

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01841))_

> 'We could draw positions as nodes in a graph, connected by arcs representing the arrows. Detecting whether the game terminates is equivalent to detecting whether the graph contains a cycle.'

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01836))_

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

### Technical frame 4: We'll keep it simple: / Interlude: The Carpenter Interviews for a Job / the carpenter's solution

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01841))_

> 'We could draw positions as nodes in a graph, connected by arcs representing the arrows. Detecting whether the game terminates is equivalent to detecting whether the graph contains a cycle.'

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01837))_

```
}
}
});
```

### Technical frame 5: We'll keep it simple: / Interlude: The Carpenter Interviews for a Job / the carpenter's solution

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01841))_

> 'We could draw positions as nodes in a graph, connected by arcs representing the arrows. Detecting whether the game terminates is equivalent to detecting whether the graph contains a cycle.'

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01839))_

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

### Technical frame 6: We'll keep it simple: / Interlude: The Carpenter Interviews for a Job / the carpenter's solution

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01844))_

> 'There's an old joke that a mathematician is someone who will take a five-minute problem, then spend an hour proving it is equivalent to another problem they have already solved. I approached this question in that spirit. Now that we have created an iterable of values that can be compared with === , I can show you this function:'

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01842))_

> [Figure] (p.267)

### Technical frame 7: We'll keep it simple: / Interlude: The Carpenter Interviews for a Job / the carpenter's solution

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01846))_

> 'A long time ago,' The Carpenter explained, 'Someone asked me a question in an interview. I have never forgotten the question, or the general form of the solution. The question was, Given a linked list, detect whether it contains a cycle. Use constant space. '

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01845))_

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

### Technical frame 8: We'll keep it simple: / Interlude: The Carpenter Interviews for a Job / the carpenter's solution

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01846))_

> 'A long time ago,' The Carpenter explained, 'Someone asked me a question in an interview. I have never forgotten the question, or the general form of the solution. The question was, Given a linked list, detect whether it contains a cycle. Use constant space. '

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01850))_

```
const terminates = (game) =>
tortoiseAndHare(positionsOf(game))
const test = [
["￿","￿","￿","￿"],
["￿","￿","￿","￿"],
["￿","￿","￿","￿"],
["￿","￿","￿","￿"]
];
terminates(Game({board: test, position: [0, 0]}))
//=> false
terminates(Game({board: test, position: [3, 0]}))
//=> true
terminates(Game({board: test, position: [0, 3]}))
//=> false
terminates(Game({board: test, position: [3, 3]}))
//=> false
```
