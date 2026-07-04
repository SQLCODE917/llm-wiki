---
page_id: javascriptallonge-section-interactive-generators-dd4aba99
page_kind: source
page_family: section-reference
summary: Interactive Generators: 33 source-backed entries and 0 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-03
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-interactive-generators-dd4aba99@15cd0fb3e1dc5f876db1b580dc8f2939
---

# Interactive Generators

From [[javascriptallonge]].

## Statements

- Served by the Pot: Collections 

250 

## **Interactive Generators** 

We used generators to build iterators that maintain implicit state. We saw how to use them for recursive unfolds and state machines. But there are other times we want to build functions that maintain implicit state. Let’s start by looking at a very simple example of a function that can be written statefully. 

**==> picture [469 x 313] intentionally omitted <==**

**Coffee and Chess** 

Consider, for example, the moves in a game. The moves a player makes are a stream of values, just like the contents of an array can be consider a stream of values. But of course, iterating over a stream of moves requires us to wait for the game to be over so we know what moves were made. 

Let’s take a look at a very simple example, naughts and crosses[99] (We really ought to do something like Chess, but that might be a little out of scope for this chapter). To save space, we’ll ignore rotations and reflections, and we’ll model the first player’s moves as a stream. 

The first player will always be o, and they will always place their chequer in the top-left corner, coincidentally numbered o: 

> 99https://en.wikipedia.org/wiki/naughts-and-crosses _(javascriptallonge.pdf (source-range-af806fb1-00300))_
- Served by the Pot: Collections 

252 

o | x | ---+---+--x | | ---+---+--o | | o 

x now has three significant moves: 4, 7, and anything else: 

o | x | 2 ---+---+--x | 4 | 5 ---+---+--x | 7 | 8 

If x plays 4, we play 7 and win. If x plays anything else, including 7, we play 4 and win. 

## **representing naughts and crosses as a stateless function** 

We could plays naughts and crosses as a stateless function. We encode each position of the board in some fashion, and then we build a dictionary from positions to moves. For example, the entry for: 

o | x | ---+---+--x | | ---+---+--o | | 

Would be 8, producing: 

o | x | ---+---+--x | | ---+---+--o | | o 

And the entry for: _(javascriptallonge.pdf (source-range-af806fb1-00302))_
- Served by the Pot: Collections 

253 

o | x | ---+---+--| x | ---+---+--o | | 

Would be 3, producing: 

o | x | ---+---+--o | x | ---+---+--o | | 

We can encode the board in several different ways. We could use multiline strings with formatting just as we’ve written it here, but it is a design smell to couple presentation with modelling. Our function should be just as useful on a teletype as it would be backing a DOM game that uses a table, or a browser game that draws on Canvas. 

Let’s use an array. So this: 

o | x | ---+---+--| | ---+---+--| | 

Will be represented as: 

[ 'o', 'x', ' ', ' ' ' ' ' ' , , , ' ' ' ' ' ' , , ] 

And this: _(javascriptallonge.pdf (source-range-af806fb1-00303))_
- Served by the Pot: Collections 

254 

o | x | ---+---+--x | | ---+---+--o | | 

Will be represented as: 

[ 'o', 'x', ' ', 'x', ' ', ' ', 'o', ' ', ' ' ] 

We can use a POJO to make a map from positions to moves. We’ll use the [] notation for keys, it allows us to use any expression as a key, and JavaScript will convert it to a string. So if we write: 

**const** moveLookupTable = { [[ 

' ' ' ' ' ' , , , ' ' ' ' ' ' , , , ' ' ' ' ' ' , , ]]: 0, [[ 

'o', 'x', ' ', ' ' ' ' ' ' , , , ' ' ' ' ' ' , , ]]: 6, [[ 'o', 'x', 'x', ' ' ' ' ' ' , , , 'o', ' ', ' ' ]]: 3, [[ 'o', 'x', ' ', 'x', ' ', ' ', 'o', ' ', ' ' ]]: 8, [[ 'o', 'x', ' ', ' ', 'x', ' ', 'o', ' ', ' ' _(javascriptallonge.pdf (source-range-af806fb1-00304))_
- Served by the Pot: Collections 

256 

statelessNaughtsAndCrosses([ 

'o', 'x', ' ', ' ' ' ' ' ' , , , 'o', 'x', ' ' ]) _//=> 3_ 

## **representing naughts and crosses as a stateful function** 

Our statelessNaughtsAndCrosses function pushes the work of tracking the game’s state onto us, the player. What if we want to exchange moves with the function? In that case, we need a stateful function. Our “API” will work like this: When we want a new game, we’ll call a function that will return a game function, We’ll call the game function repeatedly, passing our moves, and get the opponent’s moves from it. 

Something like this: 

**const** aNaughtsAndCrossesGame = statefulNaughtsAndCrosses(); 

_// our opponent makes the first move_ aNaughtsAndCrossesGame() _//=> 0_ 

_// then we move, and get its next move back_ aNaughtsAndCrossesGame(1) 

_//=> 6 // then we move, and get its next move back_ aNaughtsAndCrossesGame(4) _//=> 3_ 

We can build this out of our statelessNaughtsAndCrosses function: 

**const** statefulNaughtsAndCrosses = () => { **const** state = [ ' ' ' ' ' ' , , , ' ' ' ' ' ' , , , ' ' ' ' ' ' , , ]; **return** (x = **false** ) => { **if** (x) { _(javascriptallonge.pdf (source-range-af806fb1-00306))_
- 257 

Served by the Pot: Collections 

**if** (state[x] === ' ') { state[x] = 'x'; } **else throw** "occupied!" } **let** o = moveLookupTable[state]; state[o] = 'o'; **return** o; } }; 

**const** aNaughtsAndCrossesGame = statefulNaughtsAndCrosses(); 

_// our opponent makes the first move_ aNaughtsAndCrossesGame() _//=> 0_ 

_// then we move, and get its next move back_ aNaughtsAndCrossesGame(1) 

_//=> 6_ 

_// then we move, and get its next move back_ aNaughtsAndCrossesGame(4) 

_//=> 3_ 

Let’s recap what we have: We have a stateful function, but we built it by wrapping a stateless function in a function that updates state based on the moves we provide. The state is encoded entirely in data. 

## **this seems familiar** 

When we looked at generators, we saw that some iterators are inherently stateful, but sometimes it is awkward to represent them in a fully stateless fashion. Sometimes there is a state machine that is naturally represented implicitly in JavaScript’s control flow rather than explicitly in data. 

We’ve done almost the exact same thing here with our naughts and crosses game. A game like this is absolutely a state machine, and we’ve explicitly coded those states into the lookup table. Which leads us to wonder: Is there a way to encode those states _implicitly_ , in JavaScript control flow? 

If we were in full control of the interaction, it would be easy to encode the game play as a decision tree instead of as a lookup table. For example, we could do this in a browser: _(javascriptallonge.pdf (source-range-af806fb1-00307))_
- 258 

Served by the Pot: Collections 

**function** browserNaughtsAndCrosses () { **const** x1 = parseInt(prompt('o plays 0, where does x play?')); **switch** (x1) { **case** 1: **const** x2 = parseInt(prompt('o plays 6, where does x play?')); **switch** (x2) { **case** 2: **case** 4: **case** 5: **case** 7: **case** 8: alert('o plays 3'); **break** ; **case** 3: **const** x3 = parseInt(prompt('o plays 8, where does x play?')); **switch** (x3) { **case** 2: **case** 5: **case** 7: alert('o plays 4'); **break** ; **case** 4: alert('o plays 7'); **break** ; } } **break** ; _// ..._ } } 

Naughts and crosses is simple enough that the lookup function seems substantially simpler, in part because linear code doesn’t represent trees particularly well. But we can clearly see that if we wanted to, we could represent the state of the program implicitly in a decision tree. 

However, our solution inverts the control. We aren’t calling our function with moves, it’s calling us. With iterators, we wrote a generator function using function *, and then used yield to yield _(javascriptallonge.pdf (source-range-af806fb1-00308))_
- Served by the Pot: Collections 

259 

values while maintaining the implicit state of the generator’s control flow. 

Can we do the same thing here? At first glance, no. How do we get the player’s moves to the generator function? But the first glance is deceptive, because we only see what we’ve seen so far. Let’s see how it would actually work. 

## **interactive generators** 

So far, we have called iterators (and generators) with .next(). But what if we pass a value to .next()? If we could do that, a generator function that played naughts and crosses would look like this: 

If it _was_ possible, how would it work? 

**function** * generatorNaughtsAndCrosses () { **const** x1 = **yield** 0; **switch** (x1) { **case** 1: **const** x2 = **yield** 6; **switch** (x2) { **case** 2: **case** 4: **case** 5: **case** 7: **case** 8: **yield** 3; **break** ; **case** 3: **const** x3 = **yield** 8; **switch** (x3) { **case** 2: **case** 5: **case** 7: **yield** 4; **break** ; **case** 4: **yield** 7; **break** ; _(javascriptallonge.pdf (source-range-af806fb1-00309))_
- Served by the Pot: Collections 

260 

} } **break** ; _// ..._ } } 

**const** aNaughtsAndCrossesGame = generatorNaughtsAndCrosses(); 

We can then get the first move by calling .next(). Thereafter, we call .next(...) and pass in our moves (The very first call has to be .next() without any arguments, because the generator hasn’t started yet. If we wanted to pass some state to the generator before it begins, we’d do that with parameters.): 

aNaughtsAndCrossesGame.next().value 

_//=> 0_ 

aNaughtsAndCrossesGame.next(1).value 

_//=> 6_ 

aNaughtsAndCrossesGame.next(3).value 

_//=> 8_ 

aNaughtsAndCrossesGame.next(7).value 

_//=> 4_ 

Our generator function maintains state implicitly in its control flow, but returns an iterator that we call, it doesn’t call us. It isn’t a collection, it has no meaning if we try to spread it into parameters or as the subject of a for...of block. 

But the generator function allows us to maintain state implicitly. And sometimes, we want to use implicit state instead of explicitly storing state in our data. 

## **summary** 

We have looked at generators as ways of making iterators over static collections, where state is modelled implicitly in control flow. But as we see here, it’s also possible to use a generator interactively, passing values in and receiving a value in return, just like an ordinary function. 

Again, the salient difference is that an “interactive” generator is stateful, and it embodies its state in its control flow. _(javascriptallonge.pdf (source-range-af806fb1-00310))_
- For example, we could do this in a browser: _(javascriptallonge.pdf (source-range-af806fb1-00307))_
- But the first glance is deceptive, because we only see what we’ve seen so far. _(javascriptallonge.pdf (source-range-af806fb1-00309))_
- We can then get the first move by calling .next(). _(javascriptallonge.pdf (source-range-af806fb1-00310))_
