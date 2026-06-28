---
page_id: javascriptallonge-carpenter
page_kind: concept
summary: Carpenter: 10 statement(s) and 0 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-carpenter@5fb6b417d72038032c790d1a01aeec8f
---

# Carpenter

What [[javascriptallonge]] covers about carpenter:

## Statements

### Interlude: The Carpenter Interviews for a Job

- Served by the Pot: Collections

238

## **Interlude: The Carpenter Interviews for a Job**

“The Carpenter” was a JavaScript programmer, well-known for a meticulous attention to detail and love for hand-crafted, exquisitely joined code. The Carpenter normally worked through personal referrals, but from time to time a recruiter would slip through his screen. One such recruiter was Bob Plissken. Bob was well-known in the Python community, but his clients often needed experience with other languages.

Plissken lined up a technical interview with a well-funded startup in San Francisco. The Carpenter arrived early for his meeting with “Thing Software,” and was shown to conference room 13. A few minutes later, he was joined by one of the company’s developers, Christine.

## **the problem**

After some small talk, Christine explained that they liked to ask candidates to whiteboard some code. Despite his experience and industry longevity, the Carpenter did not mind being asked to demonstrate that he was, in fact, the person described on the resumé.

Many companies use white-boarding code as an excuse to have a technical conversation with a candidate, and The Carpenter felt that being asked to whiteboard code was an excuse to have a technical conversation with a future colleague. “Win, win” he thought to himself. _(javascriptallonge.pdf (source-range-83ecb080-00303))_

- Served by the Pot: Collections

239

**==> picture [476 x 314] intentionally omitted <==**

**----- Start of picture text -----**<br> 94<br>**----- End of picture text -----**<br>

Christine intoned the question, as if by rote:

Consider a finite checkerboard of unknown size. On each square, we randomly place an arrow pointing to one of its four sides. A chequer is placed randomly on the checkerboard. Each move consists of moving the chequer one square in the direction of the arrow in the square it occupies. If the arrow should cause the chequer to move off the edge of the board, the game halts.

The problem is this: The game board is hidden from us. A player moves the chequer, following the rules. As the player moves the chequer, they calls out the direction of movement, e.g. “↑, →, ↑, ↓, ↑, →…” Write an algorithm that will determine whether the game halts, strictly from the called out directions, in finite time and space.

“So,” The Carpenter asked, “I am to write an algorithm that takes a possibly infinite stream of…” Christine interrupted. “To save time, we have written a template of the solution for you in ECMASCript 2015 notation. Fill in the blanks. Your code should not presume anything about the > 94https://www.flickr.com/photos/stigrudeholm/6710684795 _(javascriptallonge.pdf (source-range-83ecb080-00304))_

- Served by the Pot: Collections

241

“What,” Christine asked, “Do you write in place of the three // ??? placeholders to determine whether the game halts?”

## **the carpenter’s solution**

The Carpenter was not surprised at the problem. Bob Plissken was a crafty, almost reptilian recruiter that traded in information and secrets. Whenever Bob sent a candidate to a job interview, he debriefed them afterwards and got them to disclose what questions were asked in the interview. He then coached subsequent candidates to give polished answers to the company’s pet technical questions.

And just as companies often pick a problem that gives them broad latitude for discussing alternate approaches and determining that depth of a candidate’s experience, The Carpenter liked to sketch out solutions that provided an opportunity to judge the interviewer’s experience and provide an easy excuse to discuss the company’s approach to software design.

Bob had, in fact, warned The Carpenter that “Thing” liked to ask either or both of two questions: Determine how to detect a loop in a linked list, and determine whether the chequerboard game would halt. To save time, The Carpenter had prepared the same answer for both questions.

The Carpenter coughed softly, then began. “To begin with, I’ll transform a game into an iterable that generates arrows, using the ‘Starman’ notation for generators. I’ll refactor a touch to make things clearer, for example I’ll extract the board to make it easier to test:” **const** MOVE = { "￿": ([x, y]) => [x - 1, y], "￿": ([x, y]) => [x + 1, y], "￿": ([x, y]) => [x, y + 1], "￿": ([x, y]) => [x, y - 1] }; **const** Board = (size = 8) => { _// initialize the board_ **const** board = []; **for** ( **let** i = 0; i < size; ++i) { board[i] = []; **for** ( **let** j = 0; j < size; ++j) { board[i][j] = '￿￿￿￿'[Math.floor(Math.random() * 4)]; } } _// initialize the position_ **const** position = [ _(javascriptallonge.pdf (source-range-83ecb080-00306))_

- 246

Served by the Pot: Collections **const** terminates = (game) => tortoiseAndHare(positionsOf(game)) **const** test = [ ["￿","￿","￿","￿"], ["￿","￿","￿","￿"], ["￿","￿","￿","￿"], ["￿","￿","￿","￿"] ]; terminates(Game({board: test, position: [0, 0]})) _//=> false_ terminates(Game({board: test, position: [3, 0]})) _//=> true_ terminates(Game({board: test, position: [0, 3]})) _//=> false_ terminates(Game({board: test, position: [3, 3]})) _//=> false_

“This solution makes use of iterables and a single utility function, statefulMapWith. It also cleanly separates the mechanics of the game from the algorithm for detecting cycles in a graph.”

## **the aftermath**

The Carpenter sat down and waited. This type of solution provided an excellent opportunity to explore lazy versus eager evaluation, the performance of iterators versus native iteration, single responsibility design, and many other rich topics.

The Carpenter was confident that although nobody would write this exact code in production, prospective employers would also recognize that nobody would try to detect whether a chequer game terminates in production, either. It’s all just a pretext for kicking off an interesting conversation, right?

Christine looked at the solution on the board, frowned, and glanced at the clock on the wall. “ _Well, where has the time gone?_ ” “We at the Thing Software company are very grateful you made some time to visit with us, but alas, that is all the time we have today. If we wish to talk to you further, we’ll be in touch.” The Carpenter never did hear back from them, but the next day there was an email containing a generous contract from Friends of Ghosts (“FOG”), a codename for a stealth startup doing interesting work, and the Thing interview was forgotten.

Some time later, The Carpenter ran into Bob Plissken at a local technology meet-up. “John! What happened at Thing?” Bob wanted to know, “I asked them what they thought of you, and all they _(javascriptallonge.pdf (source-range-83ecb080-00311))_

- Served by the Pot: Collections

247 would say was, _Writes unreadable code_ . I thought it was a lock! I thought you’d finally make your escape from New York.”

The Carpenter smiled. “I forgot about them, it’s been a while. So, do They Live?” **==> picture [476 x 465] intentionally omitted <==**

**----- Start of picture text -----**<br> 98<br>**----- End of picture text -----**<br>

## **after another drink**

A few drinks later, The Carpenter was telling his Thing story and an engineer named Kidu introduced themself.

> 98https://www.flickr.com/photos/jlhopgood/6795353385 _(javascriptallonge.pdf (source-range-83ecb080-00312))_

- 249

Served by the Pot: Collections **const** hasCycle = (orderedCollection) => { **const** visited = **new** Set(); **for** ( **let** element **of** orderedCollection) { **if** (visited.has(element)) { **return true** ; } visited.add(element); } **return false** ; };

The Carpenter stared at Kidu’s solution. “I guess,” he allowed, “It isn’t always necessary to make a solution so awesome it would please the Ghosts of Mars.” _(javascriptallonge.pdf (source-range-83ecb080-00314))_


## Related pages

- [[javascriptallonge-game]] - shared statements: Game shares source evidence from Interlude: The Carpenter Interviews for a Job: Served by the Pot: Collections  241  “What,” Christine asked, “Do you write in place of the three // ??? placeholders to determine whether the game halts?”  ## **the ... [truncated] (2 shared statement(s))
- [[javascriptallonge-algorithm]] - shared statements: Algorithm shares source evidence from Interlude: The Carpenter Interviews for a Job: 246  Served by the Pot: Collections **const** terminates = (game) => tortoiseAndHare(positionsOf(game)) **const** test = [ ["￿","￿","￿","￿"], ["￿","￿","￿","￿"], ["￿" ... [truncated] (1 shared statement(s))

## Source

- [[javascriptallonge]]
