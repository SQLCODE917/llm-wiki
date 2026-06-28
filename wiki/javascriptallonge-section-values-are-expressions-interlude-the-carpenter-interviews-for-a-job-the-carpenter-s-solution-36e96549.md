---
page_id: javascriptallonge-section-values-are-expressions-interlude-the-carpenter-interviews-for-a-job-the-carpenter-s-solution-36e96549
page_kind: source
summary: values are expressions / Interlude: The Carpenter Interviews for a Job / the carpenter’s solution: 14 source-backed entries and 1 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-values-are-expressions-interlude-the-carpenter-interviews-for-a-job-the-carpenter-s-solution-36e96549@ade92dbb749546e171ca40d4b0d36357
---

# values are expressions / Interlude: The Carpenter Interviews for a Job / the carpenter’s solution

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-values-are-expressions-interlude-the-carpenter-interviews-for-a-job-7514d3b1]] - broader source section

## Statements

- He then coached subsequent candidates to give polished answers to the company’s pet technical questions. _(javascriptallonge.pdf (source-range-83ecb080-01836))_
- The Carpenter was not surprised at the problem. _(javascriptallonge.pdf (source-range-83ecb080-01836))_
- He then coached subsequent candidates to give polished answers to the company’s pet technical questions. _(javascriptallonge.pdf (source-range-83ecb080-01836))_
- To save time, The Carpenter had prepared the same answer for both questions. _(javascriptallonge.pdf (source-range-83ecb080-01838))_
- Bob had, in fact, warned The Carpenter that “Thing” liked to ask either or both of two questions: Determine how to detect a loop in a linked list, and determine whether the chequerboard game would halt. _(javascriptallonge.pdf (source-range-83ecb080-01838))_
- A statefulMap is a lazy map that preserves state from iteration to iteration. _(javascriptallonge.pdf (source-range-83ecb080-01840))_
- “Now that we have an iterable, we can transform the iterable of arrows into an iterable of positions.” The Carpenter sketched quickly. _(javascriptallonge.pdf (source-range-83ecb080-01840))_
- Detecting whether the game terminates is equivalent to detecting whether the graph contains a cycle.” Served by the Pot: Collections _(javascriptallonge.pdf (source-range-83ecb080-01842))_
- Now that we have created an iterable of values that can be compared with ===, I can show you this function:” Served by the Pot: Collections _(javascriptallonge.pdf (source-range-83ecb080-01846))_
- I approached this question in that spirit. _(javascriptallonge.pdf (source-range-83ecb080-01846))_
- Now that we have created an iterable of values that can be compared with ===, I can show you this function:” Served by the Pot: Collections _(javascriptallonge.pdf (source-range-83ecb080-01846))_
- The question was, _Given a linked list, detect whether it contains a cycle. _(javascriptallonge.pdf (source-range-83ecb080-01848))_
- I have never forgotten the question, or the general form of the solution. _(javascriptallonge.pdf (source-range-83ecb080-01848))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01838, source-range-83ecb080-01840))_

> Bob had, in fact, warned The Carpenter that “Thing” liked to ask either or both of two questions: Determine how to detect a loop in a linked list, and determine whether the chequerboard game would halt. To save time, The Carpenter had prepared the same answer for both questions. “Now that we have an iterable, we can transform the iterable of arrows into an iterable of positions.” The Carpenter sketched quickly. “We want to take the arrows and convert them to positions. For that, we’ll map the Ga

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01839))_

> The Carpenter coughed softly, then began. “To begin with, I’ll transform a game into an iterable that generates arrows, using the ‘Starman’ notation for generators. I’ll refactor a touch to make things clearer, for example I’ll extract the board to make it easier to test:” **const** MOVE = { "￿": ([x, y]) => [x - 1, y], "￿": ([x, y]) => [x + 1, y], "￿": ([x, y]) => [x, y + 1], "￿": ([x, y]) => [x, y - 1] }; **const** Board = (size = 8) => { _// initialize the board_ **const** board = []; **for** ( **let** i = 0; i < size; ++i) { board[i] = []; **for** ( **let** j = 0; j < size; ++j) { board[i][j] = '￿￿￿￿'[Math.floor(Math.random() * 4)]; } } _// initialize the position_ **const** position = [ 242 Served by the Pot: Collections Math.floor(Math.random() * size), Math.floor(Math.random() * size) ]; **return** {board, position}; }; **const** Game = ({board, position}) => { **const** size = board[0].length; **return** ({ *[Symbol.iterator] () { **let** [x, y] = position; **while** (x >= 0 && y >=0 && x < size && y < size) { **const** direction = board[y][x]; **yield** direction; [x, y] = MOVE[direction]([x, y]); } } }); };
