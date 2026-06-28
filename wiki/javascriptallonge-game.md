---
page_id: javascriptallonge-game
page_kind: concept
summary: Game: 5 statement(s) and 0 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-game@3016f02b55aece3d09077097c8899de2
---

# Game

What [[javascriptallonge]] covers about game:

## Statements

### As Little As Possible About Functions, But No Less

- 13

The first sip: Basic Functions

## (() => {})()

_//=> undefined_

We said that the function returns the result of evaluating a _block_ , and we said that a block is a (possibly empty) list of JavaScript _statements_ separated by semicolons.[21] Something like: { statement[1] ; statement[2] ; statement[3] ; ... ; statement[n] } We haven’t discussed these _statements_ . What’s a statement?

There are many kinds of JavaScript statements, but the first kind is one we’ve already met. An expression is a JavaScript statement. Although they aren’t very practical, these are valid JavaScript functions, and they return undefined when applied: () => { 2 + 2 } () => { 1 + 1; 2 + 2 } As we saw with commas above, we can rearrange these functions onto multiple lines when we feel its more readable that way: () => { 1 + 1; 2 + 2 } But no matter how we arrange them, a block with one or more expressions still evaluates to undefined: (() => { 2 + 2 })() _//=> undefined_ (() => { 1 + 1; 2 + 2 })() _//=> undefined_ (() => { 1 + 1; 2 + 2 })() _//=> undefined_ As you can see, a block with one expression does not behave like an expression, and a block with more than one expression does not behave like an expression constructed with the comma operator:

> 21You can also separate statements with line breaks. Readers who follow internet flame-fests may be aware of something called automatic semicolon insertion. Basically, there’s a step where JavaScript looks at your code and follows some rules to guess where you meant to put semicolons in should you leave them out. This feature was originally created as a kind of helpful error-correction. Some programmers argue that since it’s part of the language’s definition, it’s fair game to write code that exploits it, so they deliberately omit any semicolon that JavaScript will insert for them. _(javascriptallonge.pdf (source-range-83ecb080-00050))_

### Interlude: The Carpenter Interviews for a Job

- Served by the Pot: Collections

241

“What,” Christine asked, “Do you write in place of the three // ??? placeholders to determine whether the game halts?”

## **the carpenter’s solution**

The Carpenter was not surprised at the problem. Bob Plissken was a crafty, almost reptilian recruiter that traded in information and secrets. Whenever Bob sent a candidate to a job interview, he debriefed them afterwards and got them to disclose what questions were asked in the interview. He then coached subsequent candidates to give polished answers to the company’s pet technical questions.

And just as companies often pick a problem that gives them broad latitude for discussing alternate approaches and determining that depth of a candidate’s experience, The Carpenter liked to sketch out solutions that provided an opportunity to judge the interviewer’s experience and provide an easy excuse to discuss the company’s approach to software design.

Bob had, in fact, warned The Carpenter that “Thing” liked to ask either or both of two questions: Determine how to detect a loop in a linked list, and determine whether the chequerboard game would halt. To save time, The Carpenter had prepared the same answer for both questions.

The Carpenter coughed softly, then began. “To begin with, I’ll transform a game into an iterable that generates arrows, using the ‘Starman’ notation for generators. I’ll refactor a touch to make things clearer, for example I’ll extract the board to make it easier to test:” **const** MOVE = { "￿": ([x, y]) => [x - 1, y], "￿": ([x, y]) => [x + 1, y], "￿": ([x, y]) => [x, y + 1], "￿": ([x, y]) => [x, y - 1] }; **const** Board = (size = 8) => { _// initialize the board_ **const** board = []; **for** ( **let** i = 0; i < size; ++i) { board[i] = []; **for** ( **let** j = 0; j < size; ++j) { board[i][j] = '￿￿￿￿'[Math.floor(Math.random() * 4)]; } } _// initialize the position_ **const** position = [ _(javascriptallonge.pdf (source-range-83ecb080-00306))_

- 243

Served by the Pot: Collections } } });

“Armed with this, it’s straightforward to map an iterable of directions to an iterable of strings representing positions:” **const** positionsOf = (game) => statefulMapWith( (position, direction) => { **const** [x, y] = MOVE[direction](position); position = [x, y]; **return** [position, `x: **${** x **}** , y: **${** y **}** `]; }, [0, 0], game);

The Carpenter reflected. “Having turned our game loop into an iterable, we can now see that our problem of whether the game terminates is isomorphic to the problem of detecting whether the positions given ever repeat themselves: If the chequer ever returns to a position it has previously visited, it will cycle endlessly.” “We could draw positions as nodes in a graph, connected by arcs representing the arrows. Detecting whether the game terminates is equivalent to detecting whether the graph contains a cycle.” _(javascriptallonge.pdf (source-range-83ecb080-00308))_

- 246

Served by the Pot: Collections **const** terminates = (game) => tortoiseAndHare(positionsOf(game)) **const** test = [ ["￿","￿","￿","￿"], ["￿","￿","￿","￿"], ["￿","￿","￿","￿"], ["￿","￿","￿","￿"] ]; terminates(Game({board: test, position: [0, 0]})) _//=> false_ terminates(Game({board: test, position: [3, 0]})) _//=> true_ terminates(Game({board: test, position: [0, 3]})) _//=> false_ terminates(Game({board: test, position: [3, 3]})) _//=> false_

“This solution makes use of iterables and a single utility function, statefulMapWith. It also cleanly separates the mechanics of the game from the algorithm for detecting cycles in a graph.”

## **the aftermath**

The Carpenter sat down and waited. This type of solution provided an excellent opportunity to explore lazy versus eager evaluation, the performance of iterators versus native iteration, single responsibility design, and many other rich topics.

The Carpenter was confident that although nobody would write this exact code in production, prospective employers would also recognize that nobody would try to detect whether a chequer game terminates in production, either. It’s all just a pretext for kicking off an interesting conversation, right?

Christine looked at the solution on the board, frowned, and glanced at the clock on the wall. “ _Well, where has the time gone?_ ” “We at the Thing Software company are very grateful you made some time to visit with us, but alas, that is all the time we have today. If we wish to talk to you further, we’ll be in touch.” The Carpenter never did hear back from them, but the next day there was an email containing a generous contract from Friends of Ghosts (“FOG”), a codename for a stealth startup doing interesting work, and the Thing interview was forgotten.

Some time later, The Carpenter ran into Bob Plissken at a local technology meet-up. “John! What happened at Thing?” Bob wanted to know, “I asked them what they thought of you, and all they _(javascriptallonge.pdf (source-range-83ecb080-00311))_

### Interactive Generators

- 257

Served by the Pot: Collections **if** (state[x] === ' ') { state[x] = 'x'; } **else throw** "occupied!" } **let** o = moveLookupTable[state]; state[o] = 'o'; **return** o; } }; **const** aNaughtsAndCrossesGame = statefulNaughtsAndCrosses();

_// our opponent makes the first move_ aNaughtsAndCrossesGame() _//=> 0_

_// then we move, and get its next move back_ aNaughtsAndCrossesGame(1) _//=> 6_

_// then we move, and get its next move back_ aNaughtsAndCrossesGame(4) _//=> 3_

Let’s recap what we have: We have a stateful function, but we built it by wrapping a stateless function in a function that updates state based on the moves we provide. The state is encoded entirely in data.

## **this seems familiar**

When we looked at generators, we saw that some iterators are inherently stateful, but sometimes it is awkward to represent them in a fully stateless fashion. Sometimes there is a state machine that is naturally represented implicitly in JavaScript’s control flow rather than explicitly in data.

We’ve done almost the exact same thing here with our naughts and crosses game. A game like this is absolutely a state machine, and we’ve explicitly coded those states into the lookup table. Which leads us to wonder: Is there a way to encode those states _implicitly_ , in JavaScript control flow?

If we were in full control of the interaction, it would be easy to encode the game play as a decision tree instead of as a lookup table. For example, we could do this in a browser: _(javascriptallonge.pdf (source-range-83ecb080-00323))_


## Related pages

- [[javascriptallonge-carpenter]] - shared statements: Carpenter shares source evidence from Interlude: The Carpenter Interviews for a Job: Served by the Pot: Collections  241  “What,” Christine asked, “Do you write in place of the three // ??? placeholders to determine whether the game halts?”  ## **the ... [truncated] (2 shared statement(s))
- [[javascriptallonge-algorithm]] - shared statements: Algorithm shares source evidence from Interlude: The Carpenter Interviews for a Job: 246  Served by the Pot: Collections **const** terminates = (game) => tortoiseAndHare(positionsOf(game)) **const** test = [ ["￿","￿","￿","￿"], ["￿","￿","￿","￿"], ["￿" ... [truncated] (1 shared statement(s))
- [[javascriptallonge-code]] - shared statements: Code shares source evidence from As Little As Possible About Functions, But No Less: 13  The first sip: Basic Functions  ## (() => {})()  _//=> undefined_  We said that the function returns the result of evaluating a _block_ , and we said that a bloc ... [truncated] (1 shared statement(s))
- [[javascriptallonge-javascript]] - shared statements: Javascript shares source evidence from As Little As Possible About Functions, But No Less: 13  The first sip: Basic Functions  ## (() => {})()  _//=> undefined_  We said that the function returns the result of evaluating a _block_ , and we said that a bloc ... [truncated] (1 shared statement(s))
- [[javascriptallonge-language]] - shared statements: Language shares source evidence from As Little As Possible About Functions, But No Less: 13  The first sip: Basic Functions  ## (() => {})()  _//=> undefined_  We said that the function returns the result of evaluating a _block_ , and we said that a bloc ... [truncated] (1 shared statement(s))
- [[javascriptallonge-programmer]] - shared statements: Programmer shares source evidence from As Little As Possible About Functions, But No Less: 13  The first sip: Basic Functions  ## (() => {})()  _//=> undefined_  We said that the function returns the result of evaluating a _block_ , and we said that a bloc ... [truncated] (1 shared statement(s))
- [[javascriptallonge-write]] - shared statements: Write shares source evidence from As Little As Possible About Functions, But No Less: 13  The first sip: Basic Functions  ## (() => {})()  _//=> undefined_  We said that the function returns the result of evaluating a _block_ , and we said that a bloc ... [truncated] (1 shared statement(s))

## Source

- [[javascriptallonge]]
