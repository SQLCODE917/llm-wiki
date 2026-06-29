---
page_id: javascriptallonge-section-we-ll-keep-it-simple-interlude-the-carpenter-interviews-for-a-job-196a6679
page_kind: source
summary: We'll keep it simple: / Interlude: The Carpenter Interviews for a Job: 51 source-backed entries and 16 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-29
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-we-ll-keep-it-simple-interlude-the-carpenter-interviews-for-a-job-196a6679@59f73e5c4c44c027438f0e2d808bf404
---

# We'll keep it simple: / Interlude: The Carpenter Interviews for a Job

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-we-ll-keep-it-simple-1104ef0d]] - broader source section: We'll keep it simple:
- [[javascriptallonge-section-we-ll-keep-it-simple-interlude-the-carpenter-interviews-for-a-job-the-problem-69f83674]] - narrower source section: We'll keep it simple: / Interlude: The Carpenter Interviews for a Job / the problem
- [[javascriptallonge-section-we-ll-keep-it-simple-interlude-the-carpenter-interviews-for-a-job-the-carpenter-s-solution-9074fc35]] - narrower source section: We'll keep it simple: / Interlude: The Carpenter Interviews for a Job / the carpenter's solution
- [[javascriptallonge-section-we-ll-keep-it-simple-interlude-the-carpenter-interviews-for-a-job-the-aftermath-0085c9b6]] - narrower source section: We'll keep it simple: / Interlude: The Carpenter Interviews for a Job / the aftermath
- [[javascriptallonge-section-we-ll-keep-it-simple-interlude-the-carpenter-interviews-for-a-job-after-another-drink-b1c5a752]] - narrower source section: We'll keep it simple: / Interlude: The Carpenter Interviews for a Job / after another drink

## Statements

- Plissken lined up a technical interview with a well-funded startup in San Francisco. The Carpenter arrived early for his meeting with 'Thing Software,' and was shown to conference room 13. A few minutes later, he was joined by one of the company's developers, Christine. _(javascriptallonge.pdf (source-range-7239e085-01811))_

## Statements by subsection

### We'll keep it simple: / Interlude: The Carpenter Interviews for a Job / the problem

- After some small talk, Christine explained that they liked to ask candidates to whiteboard some code. Despite his experience and industry longevity, the Carpenter did not mind being asked to demonstrate that he was, in fact, the person described on the resumé. _(javascriptallonge.pdf (source-range-7239e085-01813))_
- Many companies use white-boarding code as an excuse to have a technical conversation with a candidate, and The Carpenter felt that being asked to whiteboard code was an excuse to have a technical conversation with a future colleague. 'Win, win' he thought to himself. _(javascriptallonge.pdf (source-range-7239e085-01814))_
- Consider a finite checkerboard of unknown size. On each square, we randomly place an arrow pointing to one of its four sides. A chequer is placed randomly on the checkerboard. Each move consists of moving the chequer one square in the direction of the arrow in the square it occupies. If the arrow should cause the chequer to move off the edge of the board, the game halts. _(javascriptallonge.pdf (source-range-7239e085-01818))_
- The problem is this: The game board is hidden from us. A player moves the chequer, following the rules. As the player moves the chequer, they calls out the direction of movement, e.g. '↑, →, ↑, ↓, ↑, →…' Write an algorithm that will determine whether the game halts, strictly from the called out directions, in finite time and space. _(javascriptallonge.pdf (source-range-7239e085-01819))_
- Christine interrupted. 'To save time, we have written a template of the solution for you in ECMASCript 2015 notation. Fill in the blanks. Your code should not presume anything about the game-board's size or contents, only that it is given an arrow every time though the while loop. You may use babeljs.io 95 , or ES6Fiddle 96 to check your work. ' _(javascriptallonge.pdf (source-range-7239e085-01821))_
- After some small talk, Christine explained that they liked to ask candidates to whiteboard some code. _(javascriptallonge.pdf (source-range-7239e085-01813))_
- Your code should not presume anything about the game-board's size or contents, only that it is given an arrow every time though the while loop. _(javascriptallonge.pdf (source-range-7239e085-01821))_

### We'll keep it simple: / Interlude: The Carpenter Interviews for a Job / the carpenter's solution

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

### We'll keep it simple: / Interlude: The Carpenter Interviews for a Job / the aftermath

- The Carpenter sat down and waited. This type of solution provided an excellent opportunity to explore lazy versus eager evaluation, the performance of iterators versus native iteration, single responsibility design, and many other rich topics. _(javascriptallonge.pdf (source-range-7239e085-01853))_
- The Carpenter was confident that although nobody would write this exact code in production, prospective employers would also recognize that nobody would try to detect whether a chequer game terminates in production, either. It's all just a pretext for kicking off an interesting conversation, right? _(javascriptallonge.pdf (source-range-7239e085-01854))_
- Christine looked at the solution on the board, frowned, and glanced at the clock on the wall. ' Well, where has the time gone? ' _(javascriptallonge.pdf (source-range-7239e085-01855))_

### We'll keep it simple: / Interlude: The Carpenter Interviews for a Job / after another drink

- A few drinks later, The Carpenter was telling his Thing story and an engineer named Kidu introduced themself. _(javascriptallonge.pdf (source-range-7239e085-01863))_
- 'I worked at Thing, and Christine told us about your solution. I had a look at the code you left on the whiteboard. Of course, white-boarding in an interview situation is notoriously unreliable, so small defects are not important. But I couldn't help but notice that your solution doesn't actually meet the stated requirements for a different reason:' _(javascriptallonge.pdf (source-range-7239e085-01865))_
- 'The hasCycle function, a/k/a Tortoise and Hare, requires two separate iterators to do its job. Whereas the problem as stated involves a single stream of directions. You're essentially calling for the player to clone themselves and call out the directions in parallel.' _(javascriptallonge.pdf (source-range-7239e085-01866))_
- Kidu shrugged. 'You know, the requirement asked for a finite space algorithm, not a constant state algorithm. Doesn't it make sense to go with a faster finite space algorithm? There's no benefit to constant space if finite space is sufficient. ' _(javascriptallonge.pdf (source-range-7239e085-01869))_
- The Carpenter stared at Kidu's solution. 'I guess,' he allowed, 'It isn't always necessary to make a solution so awesome it would please the Ghosts of Mars.' _(javascriptallonge.pdf (source-range-7239e085-01871))_
- Whereas the problem as stated involves a single stream of directions. _(javascriptallonge.pdf (source-range-7239e085-01866))_

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

### Technical frame 5: We'll keep it simple: / Interlude: The Carpenter Interviews for a Job / the carpenter's solution

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

### Technical frame 6: We'll keep it simple: / Interlude: The Carpenter Interviews for a Job / the carpenter's solution

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

### Technical frame 7: We'll keep it simple: / Interlude: The Carpenter Interviews for a Job / the carpenter's solution

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

### Technical frame 8: We'll keep it simple: / Interlude: The Carpenter Interviews for a Job / the carpenter's solution

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01841))_

> 'We could draw positions as nodes in a graph, connected by arcs representing the arrows. Detecting whether the game terminates is equivalent to detecting whether the graph contains a cycle.'

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01837))_

```
}
}
});
```

### Technical frame 9: We'll keep it simple: / Interlude: The Carpenter Interviews for a Job / the carpenter's solution

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

### Technical frame 10: We'll keep it simple: / Interlude: The Carpenter Interviews for a Job / the carpenter's solution

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01844))_

> 'There's an old joke that a mathematician is someone who will take a five-minute problem, then spend an hour proving it is equivalent to another problem they have already solved. I approached this question in that spirit. Now that we have created an iterable of values that can be compared with === , I can show you this function:'

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01842))_

> [Figure] (p.267)

### Technical frame 11: We'll keep it simple: / Interlude: The Carpenter Interviews for a Job / the carpenter's solution

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

### Technical frame 12: We'll keep it simple: / Interlude: The Carpenter Interviews for a Job / the carpenter's solution

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

### Technical frame 13: We'll keep it simple: / Interlude: The Carpenter Interviews for a Job / the aftermath

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01855))_

> Christine looked at the solution on the board, frowned, and glanced at the clock on the wall. ' Well, where has the time gone? '

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01861))_

> [Figure] (p.270)

### Technical frame 14: We'll keep it simple: / Interlude: The Carpenter Interviews for a Job / after another drink

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01869))_

> Kidu shrugged. 'You know, the requirement asked for a finite space algorithm, not a constant state algorithm. Doesn't it make sense to go with a faster finite space algorithm? There's no benefit to constant space if finite space is sufficient. '

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01868))_

```
// implements Teleporting Tortoise
// cycle detection algorithm.
const hasCycle = (iterable) => {
let iterator = iterable[Symbol.iterator](),
teleportDistance = 1;
while (true) {
let {value, done} = iterator.next(),
tortoise = value;
if (done) return false;
for (let i = 0; i < teleportDistance; ++i) {
let {value, done} = iterator.next(),
hare = value;
if (done) return false;
if (tortoise === hare) return true;
}
teleportDistance *= 2;
}
return false;
};
```

### Technical frame 15: We'll keep it simple: / Interlude: The Carpenter Interviews for a Job / after another drink

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01871))_

> The Carpenter stared at Kidu's solution. 'I guess,' he allowed, 'It isn't always necessary to make a solution so awesome it would please the Ghosts of Mars.'

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01870))_

```
const hasCycle = (orderedCollection) => {
const visited = new Set();
for (let element of orderedCollection) {
if (visited.has(element)) {
return true;
}
visited.add(element);
}
return false;
};
```

### Technical atom 16

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
