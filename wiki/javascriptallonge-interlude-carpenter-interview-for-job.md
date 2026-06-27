---
page_id: javascriptallonge-interlude-carpenter-interview-for-job
page_kind: concept
summary: Interlude: The Carpenter Interviews for a Job: 46 statement(s) and 9 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-interlude-carpenter-interview-for-job@ac6e0b74d1988da9ee402d7e1e2e9d10
---

# Interlude: The Carpenter Interviews for a Job

What [[javascriptallonge]] covers about interlude: the carpenter interviews for a job:

## Statements

_Showing 14 of 46 statements selected for this topic._

- “The Carpenter” was a JavaScript programmer, well-known for a meticulous attention to detail and love for hand-crafted, exquisitely joined code. _(javascriptallonge.pdf (source-range-83ecb080-02825))_
- To save time, The Carpenter had prepared the same answer for both questions. _(javascriptallonge.pdf (source-range-83ecb080-02852))_
- Despite his experience and industry longevity, the Carpenter did not mind being asked to demonstrate that he was, in fact, the person described on the resumé. _(javascriptallonge.pdf (source-range-83ecb080-02828))_
- The Carpenter was not surprised at the problem. _(javascriptallonge.pdf (source-range-83ecb080-02850))_
- The Carpenter coughed softly, then began. _(javascriptallonge.pdf (source-range-83ecb080-02853))_
- The Carpenter sat down and waited. _(javascriptallonge.pdf (source-range-83ecb080-02894))_
- The Carpenter was confident that although nobody would write this exact code in production, prospective employers would also recognize that nobody would try to detect whether a chequer game terminates in production, either. _(javascriptallonge.pdf (source-range-83ecb080-02895))_
- “I forgot about them, it’s been a while. _(javascriptallonge.pdf (source-range-83ecb080-02903))_
- A few drinks later, The Carpenter was telling his Thing story and an engineer named Kidu introduced themself. _(javascriptallonge.pdf (source-range-83ecb080-02907))_
- The Carpenter stared at Kidu’s solution. _(javascriptallonge.pdf (source-range-83ecb080-02921))_
- Many companies use white-boarding code as an excuse to have a technical conversation with a candidate, and The Carpenter felt that being asked to whiteboard code was an excuse to have a technical conversation with a future colleague. _(javascriptallonge.pdf (source-range-83ecb080-02829))_
- “To save time, we have written a template of the solution for you in ECMASCript 2015 notation. _(javascriptallonge.pdf (source-range-83ecb080-02838))_
- Bob had, in fact, warned The Carpenter that “Thing” liked to ask either or both of two questions: Determine how to detect a loop in a linked list, and determine whether the chequerboard game would halt. _(javascriptallonge.pdf (source-range-83ecb080-02852))_
- I’ll refactor a touch to make things clearer, for example I’ll extract the board to make it easier to test:” _(javascriptallonge.pdf (source-range-83ecb080-02853))_

## Technical atoms

_Showing 6 of 9 technical atoms selected for this topic._

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02834))_

> Christine intoned the question, as if by rote:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02835))_

> If the arrow should cause the chequer to move off the edge of the board, the game halts.

### Technical atom 2

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02842))_

> You may use babeljs.io[95] , or ES6Fiddle[96] to check your work.

### Technical atom 3

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02843))_

> Christine quickly scribbled on the whiteboard:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02844))_

> **const** Game = (size = 8) => {

### Technical atom 4

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02853))_

> The Carpenter coughed softly, then began. “To begin with, I’ll transform a game into an iterable that generates arrows, using the ‘Starman’ notation for generators. I’ll refactor a touch to make things clearer, for example I’ll extract the board to make it easier to test:”

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02855))_

> **const** Board = (size = 8) => {

### Technical atom 5

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02862))_

> “Now that we have an iterable, we can transform the iterable of arrows into an iterable of positions.” The Carpenter sketched quickly. “We want to take the arrows and convert them to positions. For that, we’ll map the Game iterable to positions. A statefulMap is a lazy map that preserves state from iteration to iteration. That’s what we need, because we need to know the current position to map each move to the next position.”

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02860))_

> **const** Game = ({board, position}) => {

### Technical atom 6

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02876))_

> “There’s an old joke that a mathematician is someone who will take a five-minute problem, then spend an hour proving it is equivalent to another problem they have already solved. I approached this question in that spirit. Now that we have created an iterable of values that can be compared with ===, I can show you this function:”

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02879))_

> **const** tortoiseAndHare = (iterable) => { **const** hare = iterable[Symbol.iterator](); **let** hareResult = (hare.next(), hare.next());


## Source

- [[javascriptallonge]]
