---
page_id: javascriptallonge-section-interactive-generators-5d88ed7c
page_kind: source
summary: Interactive Generators: 44 source-backed entries and 5 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-interactive-generators-5d88ed7c@9beafe6c0f777b0da34e40f8c8f80f0d
---

# Interactive Generators

From [[javascriptallonge]].

## Statements

- We saw how to use them for recursive unfolds and state machines. _(javascriptallonge.pdf (source-range-83ecb080-02926))_
- But there are other times we want to build functions that maintain implicit state. _(javascriptallonge.pdf (source-range-83ecb080-02926))_
- Let’s start by looking at a very simple example of a function that can be written statefully. _(javascriptallonge.pdf (source-range-83ecb080-02926))_
- We used generators to build iterators that maintain implicit state. _(javascriptallonge.pdf (source-range-83ecb080-02926))_
- The moves a player makes are a stream of values, just like the contents of an array can be consider a stream of values. _(javascriptallonge.pdf (source-range-83ecb080-02929))_
- But of course, iterating over a stream of moves requires us to wait for the game to be over so we know what moves were made. _(javascriptallonge.pdf (source-range-83ecb080-02929))_
- Consider, for example, the moves in a game. _(javascriptallonge.pdf (source-range-83ecb080-02929))_
- Let’s take a look at a very simple example, naughts and crosses[99] (We really ought to do something like Chess, but that might be a little out of scope for this chapter). _(javascriptallonge.pdf (source-range-83ecb080-02930))_
- The first player will always be o, and they will always place their chequer in the top-left corner, coincidentally numbered o: _(javascriptallonge.pdf (source-range-83ecb080-02931))_
- x has six possible moves, but they are really just two choices: 3 and anything else: _(javascriptallonge.pdf (source-range-83ecb080-02942))_
- We could plays naughts and crosses as a stateless function. _(javascriptallonge.pdf (source-range-83ecb080-02952))_
- We encode each position of the board in some fashion, and then we build a dictionary from positions to moves. _(javascriptallonge.pdf (source-range-83ecb080-02952))_
- We can encode the board in several different ways. _(javascriptallonge.pdf (source-range-83ecb080-02962))_
- We’ll use the [] notation for keys, it allows us to use any expression as a key, and JavaScript will convert it to a string. _(javascriptallonge.pdf (source-range-83ecb080-02973))_
- We can use a POJO to make a map from positions to moves. _(javascriptallonge.pdf (source-range-83ecb080-02973))_
- In that case, we need a stateful function. _(javascriptallonge.pdf (source-range-83ecb080-02994))_
- The state is encoded entirely in data. _(javascriptallonge.pdf (source-range-83ecb080-03011))_
- Let’s recap what we have: We have a stateful function, but we built it by wrapping a stateless function in a function that updates state based on the moves we provide. _(javascriptallonge.pdf (source-range-83ecb080-03011))_
- When we looked at generators, we saw that some iterators are inherently stateful, but sometimes it is awkward to represent them in a fully stateless fashion. _(javascriptallonge.pdf (source-range-83ecb080-03013))_
- Sometimes there is a state machine that is naturally represented implicitly in JavaScript’s control flow rather than explicitly in data. _(javascriptallonge.pdf (source-range-83ecb080-03013))_
- A game like this is absolutely a state machine, and we’ve explicitly coded those states into the lookup table. _(javascriptallonge.pdf (source-range-83ecb080-03014))_
- If we were in full control of the interaction, it would be easy to encode the game play as a decision tree instead of as a lookup table. _(javascriptallonge.pdf (source-range-83ecb080-03015))_
- But we can clearly see that if we wanted to, we could represent the state of the program implicitly in a decision tree. _(javascriptallonge.pdf (source-range-83ecb080-03019))_
- Naughts and crosses is simple enough that the lookup function seems substantially simpler, in part because linear code doesn’t represent trees particularly well. _(javascriptallonge.pdf (source-range-83ecb080-03019))_
- Naughts and crosses is simple enough that the lookup function seems substantially simpler, in part because linear code doesn’t represent trees particularly well. _(javascriptallonge.pdf (source-range-83ecb080-03019))_
- Let’s see how it would actually work. _(javascriptallonge.pdf (source-range-83ecb080-03024))_
- But the first glance is deceptive, because we only see what we’ve seen so far. _(javascriptallonge.pdf (source-range-83ecb080-03024))_
- But the first glance is deceptive, because we only see what we’ve seen so far. _(javascriptallonge.pdf (source-range-83ecb080-03024))_
- If we could do that, a generator function that played naughts and crosses would look like this: _(javascriptallonge.pdf (source-range-83ecb080-03026))_
- So far, we have called iterators (and generators) with .next(). _(javascriptallonge.pdf (source-range-83ecb080-03026))_
- Thereafter, we call .next(...) and pass in our moves (The very first call has to be .next() without any arguments, because the generator hasn’t started yet. _(javascriptallonge.pdf (source-range-83ecb080-03033))_
- We can then get the first move by calling .next(). _(javascriptallonge.pdf (source-range-83ecb080-03033))_
- Thereafter, we call .next(...) and pass in our moves (The very first call has to be .next() without any arguments, because the generator hasn’t started yet. _(javascriptallonge.pdf (source-range-83ecb080-03033))_
- We can then get the first move by calling .next(). _(javascriptallonge.pdf (source-range-83ecb080-03033))_
- It isn’t a collection, it has no meaning if we try to spread it into parameters or as the subject of a for...of block. _(javascriptallonge.pdf (source-range-83ecb080-03042))_
- But the generator function allows us to maintain state implicitly. _(javascriptallonge.pdf (source-range-83ecb080-03043))_
- And sometimes, we want to use implicit state instead of explicitly storing state in our data. _(javascriptallonge.pdf (source-range-83ecb080-03043))_
- We have looked at generators as ways of making iterators over static collections, where state is modelled implicitly in control flow. _(javascriptallonge.pdf (source-range-83ecb080-03045))_
- Again, the salient difference is that an “interactive” generator is stateful, and it embodies its state in its control flow. _(javascriptallonge.pdf (source-range-83ecb080-03046))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02984))_

> And if we want to look up what move to make, we can write:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02986))_

> 'o', 'x', ' ', ' ' ' ' ' ' , , , 'o', 'x', ' ' _//=> 3_

### Technical atom 2

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02992))_

> 'o', 'x', ' ', ' ' ' ' ' ' , , , 'o', 'x', ' ' ]) _//=> 3_

### Technical atom 3

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02996))_

> **const** aNaughtsAndCrossesGame = statefulNaughtsAndCrosses();

### Technical atom 4

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-03005))_

> **const** aNaughtsAndCrossesGame = statefulNaughtsAndCrosses();

### Technical atom 5

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-03033))_

> We can then get the first move by calling .next(). Thereafter, we call .next(...) and pass in our moves (The very first call has to be .next() without any arguments, because the generator hasn’t started yet. If we wanted to pass some state to the generator before it begins, we’d do that with parameters.):

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-03032))_

> **const** aNaughtsAndCrossesGame = generatorNaughtsAndCrosses();
