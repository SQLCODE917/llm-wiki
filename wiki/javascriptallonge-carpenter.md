---
page_id: javascriptallonge-carpenter
page_kind: concept
summary: Carpenter: 8 statement(s) and 2 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-carpenter@fb3a3e9e735ab99028ad969e8cf053d7
---

# Carpenter

What [[javascriptallonge]] covers about carpenter:

## Statements

### the problem

- After some small talk, Christine explained that they liked to ask candidates to whiteboard some code. Despite his experience and industry longevity, the Carpenter did not mind being asked to demonstrate that he was, in fact, the person described on the resumé. _(javascriptallonge.pdf (source-range-31a4cf47-01814))_

### the carpenter's solution

- The Carpenter was not surprised at the problem. Bob Plissken was a crafty, almost reptilian recruiter that traded in information and secrets. Whenever Bob sent a candidate to a job interview, he debriefed them afterwards and got them to disclose what questions were asked in the interview. He then coached subsequent candidates to give polished answers to the company's pet technical questions. _(javascriptallonge.pdf (source-range-31a4cf47-01829))_

- Bob had, in fact, warned The Carpenter that 'Thing' liked to ask either or both of two questions: Determine how to detect a loop in a linked list, and determine whether the chequerboard game would halt. To save time, The Carpenter had prepared the same answer for both questions. _(javascriptallonge.pdf (source-range-31a4cf47-01831))_

- The Carpenter coughed softly, then began. 'To begin with, I'll transform a game into an iterable that generates arrows, using the 'Starman' notation for generators. I'll refactor a touch to make things clearer, for example I'll extract the board to make it easier to test:' _(javascriptallonge.pdf (source-range-31a4cf47-01832))_

### the aftermath

- The Carpenter sat down and waited. This type of solution provided an excellent opportunity to explore lazy versus eager evaluation, the performance of iterators versus native iteration, single responsibility design, and many other rich topics. _(javascriptallonge.pdf (source-range-31a4cf47-01854))_

- The Carpenter was confident that although nobody would write this exact code in production, prospective employers would also recognize that nobody would try to detect whether a chequer game terminates in production, either. It's all just a pretext for kicking off an interesting conversation, right? _(javascriptallonge.pdf (source-range-31a4cf47-01855))_

### after another drink

- A few drinks later, The Carpenter was telling his Thing story and an engineer named Kidu introduced themself. _(javascriptallonge.pdf (source-range-31a4cf47-01864))_

- The Carpenter stared at Kidu's solution. 'I guess,' he allowed, 'It isn't always necessary to make a solution so awesome it would please the Ghosts of Mars.' _(javascriptallonge.pdf (source-range-31a4cf47-01872))_


## Technical atoms

### Technical frame 1: the carpenter's solution

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01835))_

> 'Now that we have an iterable, we can transform the iterable of arrows into an iterable of positions.' The Carpenter sketched quickly. 'We want to take the arrows and convert them to positions. For that, we'll map the Game iterable to positions. A statefulMap is a lazy map that preserves state from iteration to iteration. That's what we need, because we need to know the current position to map each move to the next position.'

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01833))_

```
const MOVE = { "￿": ([x, y]) => [x - 1, y], "￿": ([x, y]) => [x + 1, y], "￿": ([x, y]) => [x, y + 1], "￿": ([x, y]) => [x, y - 1] }; const Board = (size = 8) => { // initialize the board const board = []; for ( let i = 0; i < size; ++i) { board[i] = []; for ( let j = 0; j < size; ++j) { board[i][j] = '￿￿￿￿'[Math.floor(Math.random() * 4)]; } } // initialize the position const position = [
```

### Technical frame 2: the carpenter's solution

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01835))_

> 'Now that we have an iterable, we can transform the iterable of arrows into an iterable of positions.' The Carpenter sketched quickly. 'We want to take the arrows and convert them to positions. For that, we'll map the Game iterable to positions. A statefulMap is a lazy map that preserves state from iteration to iteration. That's what we need, because we need to know the current position to map each move to the next position.'

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01834))_

```
Math.floor(Math.random() * size), Math.floor(Math.random() * size) ]; return {board, position}; }; const Game = ({board, position}) => { const size = board[0].length; return ({ *[Symbol.iterator] () { let [x, y] = position; while (x >= 0 && y >=0 && x < size && y < size) { const direction = board[y][x]; yield direction; [x, y] = MOVE[direction]([x, y]); } } }); };
```


## Source

- [[javascriptallonge]]
