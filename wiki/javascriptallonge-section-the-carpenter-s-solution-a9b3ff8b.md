---
page_id: javascriptallonge-section-the-carpenter-s-solution-a9b3ff8b
page_kind: source
summary: **the carpenter’s solution**: 31 source-backed entries and 5 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-the-carpenter-s-solution-a9b3ff8b@3debee7149a160d5895e908ebd5dd681
---

# **the carpenter’s solution**

From [[javascriptallonge]].

## Statements

- He then coached subsequent candidates to give polished answers to the company’s pet technical questions. _(javascriptallonge.pdf (source-range-83ecb080-02850))_
- The Carpenter was not surprised at the problem. _(javascriptallonge.pdf (source-range-83ecb080-02850))_
- He then coached subsequent candidates to give polished answers to the company’s pet technical questions. _(javascriptallonge.pdf (source-range-83ecb080-02850))_
- To save time, The Carpenter had prepared the same answer for both questions. _(javascriptallonge.pdf (source-range-83ecb080-02852))_
- Bob had, in fact, warned The Carpenter that “Thing” liked to ask either or both of two questions: Determine how to detect a loop in a linked list, and determine whether the chequerboard game would halt. _(javascriptallonge.pdf (source-range-83ecb080-02852))_
- The Carpenter coughed softly, then began. _(javascriptallonge.pdf (source-range-83ecb080-02853))_
- I’ll refactor a touch to make things clearer, for example I’ll extract the board to make it easier to test:” _(javascriptallonge.pdf (source-range-83ecb080-02853))_
- “To begin with, I’ll transform a game into an iterable that generates arrows, using the ‘Starman’ notation for generators. _(javascriptallonge.pdf (source-range-83ecb080-02853))_
- The Carpenter coughed softly, then began. _(javascriptallonge.pdf (source-range-83ecb080-02853))_
- I’ll refactor a touch to make things clearer, for example I’ll extract the board to make it easier to test:” _(javascriptallonge.pdf (source-range-83ecb080-02853))_
- A statefulMap is a lazy map that preserves state from iteration to iteration. _(javascriptallonge.pdf (source-range-83ecb080-02862))_
- “Now that we have an iterable, we can transform the iterable of arrows into an iterable of positions.” The Carpenter sketched quickly. _(javascriptallonge.pdf (source-range-83ecb080-02862))_
- That’s what we need, because we need to know the current position to map each move to the next position.” _(javascriptallonge.pdf (source-range-83ecb080-02862))_
- That’s what we need, because we need to know the current position to map each move to the next position.” _(javascriptallonge.pdf (source-range-83ecb080-02862))_
- “This is a standard idiom we can obtain from libraries, we don’t reinvent the wheel. _(javascriptallonge.pdf (source-range-83ecb080-02863))_
- “Armed with this, it’s straightforward to map an iterable of directions to an iterable of strings representing positions:” _(javascriptallonge.pdf (source-range-83ecb080-02868))_
- “Having turned our game loop into an iterable, we can now see that our problem of whether the game terminates is isomorphic to the problem of detecting whether the positions given ever repeat themselves: If the chequer ever returns to a position it has previously visited, it will cycle endlessly.” _(javascriptallonge.pdf (source-range-83ecb080-02870))_
- Detecting whether the game terminates is equivalent to detecting whether the graph contains a cycle.” _(javascriptallonge.pdf (source-range-83ecb080-02871))_
- “We could draw positions as nodes in a graph, connected by arcs representing the arrows. _(javascriptallonge.pdf (source-range-83ecb080-02871))_
- “There’s an old joke that a mathematician is someone who will take a five-minute problem, then spend an hour proving it is equivalent to another problem they have already solved. _(javascriptallonge.pdf (source-range-83ecb080-02876))_
- I approached this question in that spirit. _(javascriptallonge.pdf (source-range-83ecb080-02876))_
- “There’s an old joke that a mathematician is someone who will take a five-minute problem, then spend an hour proving it is equivalent to another problem they have already solved. _(javascriptallonge.pdf (source-range-83ecb080-02876))_
- The question was, _Given a linked list, detect whether it contains a cycle. _(javascriptallonge.pdf (source-range-83ecb080-02884))_
- I have never forgotten the question, or the general form of the solution. _(javascriptallonge.pdf (source-range-83ecb080-02884))_
- “This is, of course, the most common solution, it is Floyd’s cycle-finding algorithm[97] , although there is some academic dispute as to whether Robert Floyd actually discovered it or was misattributed by Knuth.” _(javascriptallonge.pdf (source-range-83ecb080-02885))_
- “This solution makes use of iterables and a single utility function, statefulMapWith. _(javascriptallonge.pdf (source-range-83ecb080-02892))_

## Technical atoms

> Context: The Carpenter coughed softly, then began. “To begin with, I’ll transform a game into an iterable that generates arrows, using the ‘Starman’ notation for generators. I’ll refactor a touch to make things clearer, for example I’ll extract the board to make it easier to test:”
_(context: javascriptallonge.pdf (source-range-83ecb080-02853))_

> **const** Board = (size = 8) => {
_(source: javascriptallonge.pdf (source-range-83ecb080-02855))_

> Context: “Now that we have an iterable, we can transform the iterable of arrows into an iterable of positions.” The Carpenter sketched quickly. “We want to take the arrows and convert them to positions. For that, we’ll map the Game iterable to positions. A statefulMap is a lazy map that preserves state from iteration to iteration. That’s what we need, because we need to know the current position to map each move to the next position.”
_(context: javascriptallonge.pdf (source-range-83ecb080-02862))_

> **const** Game = ({board, position}) => {
_(source: javascriptallonge.pdf (source-range-83ecb080-02860))_

> Context: “There’s an old joke that a mathematician is someone who will take a five-minute problem, then spend an hour proving it is equivalent to another problem they have already solved. I approached this question in that spirit. Now that we have created an iterable of values that can be compared with ===, I can show you this function:”
_(context: javascriptallonge.pdf (source-range-83ecb080-02876))_

> **const** tortoiseAndHare = (iterable) => { **const** hare = iterable[Symbol.iterator](); **let** hareResult = (hare.next(), hare.next());
_(source: javascriptallonge.pdf (source-range-83ecb080-02879))_

> hareResult = hare.next();
_(source: javascriptallonge.pdf (source-range-83ecb080-02881))_

> **const** terminates = (game) => tortoiseAndHare(positionsOf(game)) **const** test = [ ["￿","￿","￿","￿"], ["￿","￿","￿","￿"], ["￿","￿","￿","￿"], ["￿","￿","￿","￿"] ];
_(source: javascriptallonge.pdf (source-range-83ecb080-02890))_
