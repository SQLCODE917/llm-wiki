---
page_id: javascriptallonge-section-values-are-expressions-interactive-generators-90df6a1c
page_kind: source
summary: values are expressions / Interactive Generators: 36 source-backed entries and 2 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-values-are-expressions-interactive-generators-90df6a1c@65458bd3d76c196fd28c5061cffd521a
---

# values are expressions / Interactive Generators

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-values-are-expressions-4763e204]] - broader source section
- [[javascriptallonge-section-values-are-expressions-interactive-generators-representing-naughts-and-crosses-as-a-stateless-fu-a61e15d9]] - narrower source section
- [[javascriptallonge-section-values-are-expressions-interactive-generators-representing-naughts-and-crosses-as-a-stateful-fun-e2cd0114]] - narrower source section
- [[javascriptallonge-section-values-are-expressions-interactive-generators-this-seems-familiar-6b49e18a]] - narrower source section
- [[javascriptallonge-section-values-are-expressions-interactive-generators-summary-b170d9be]] - narrower source section

## Statements

- We used generators to build iterators that maintain implicit state. _(javascriptallonge.pdf (source-range-83ecb080-01871))_
- We saw how to use them for recursive unfolds and state machines. _(javascriptallonge.pdf (source-range-83ecb080-01871))_
- Let’s start by looking at a very simple example of a function that can be written statefully. _(javascriptallonge.pdf (source-range-83ecb080-01871))_
- But there are other times we want to build functions that maintain implicit state. _(javascriptallonge.pdf (source-range-83ecb080-01871))_
- The moves a player makes are a stream of values, just like the contents of an array can be consider a stream of values. _(javascriptallonge.pdf (source-range-83ecb080-01874))_
- But of course, iterating over a stream of moves requires us to wait for the game to be over so we know what moves were made. _(javascriptallonge.pdf (source-range-83ecb080-01874))_
- Let’s take a look at a very simple example, naughts and crosses[99] (We really ought to do something like Chess, but that might be a little out of scope for this chapter). _(javascriptallonge.pdf (source-range-83ecb080-01875))_
- The first player will always be o, and they will always place their chequer in the top-left corner, coincidentally numbered o: _(javascriptallonge.pdf (source-range-83ecb080-01876))_
- If we could do that, a generator function that played naughts and crosses would look like this: _(javascriptallonge.pdf (source-range-83ecb080-01926))_
- So far, we have called iterators (and generators) with .next(). _(javascriptallonge.pdf (source-range-83ecb080-01926))_
- If we wanted to pass some state to the generator before it begins, we’d do that with parameters.): aNaughtsAndCrossesGame.next().value _(javascriptallonge.pdf (source-range-83ecb080-01929))_
- We can then get the first move by calling .next(). _(javascriptallonge.pdf (source-range-83ecb080-01929))_
- We can then get the first move by calling .next(). _(javascriptallonge.pdf (source-range-83ecb080-01929))_
- If we wanted to pass some state to the generator before it begins, we’d do that with parameters.): aNaughtsAndCrossesGame.next().value _(javascriptallonge.pdf (source-range-83ecb080-01929))_
- It isn’t a collection, it has no meaning if we try to spread it into parameters or as the subject of a for...of block. _(javascriptallonge.pdf (source-range-83ecb080-01934))_
- And sometimes, we want to use implicit state instead of explicitly storing state in our data. _(javascriptallonge.pdf (source-range-83ecb080-01935))_
- But the generator function allows us to maintain state implicitly. _(javascriptallonge.pdf (source-range-83ecb080-01935))_

## Statements by subsection

### values are expressions / Interactive Generators / representing naughts and crosses as a stateless function

- We could plays naughts and crosses as a stateless function. _(javascriptallonge.pdf (source-range-83ecb080-01888))_
- We can encode the board in several different ways. _(javascriptallonge.pdf (source-range-83ecb080-01893))_
- [ 'o', 'x', ' ', 'x', ' ', ' ', 'o', ' ', ' ' ] We can use a POJO to make a map from positions to moves. _(javascriptallonge.pdf (source-range-83ecb080-01900))_
- We’ll use the [] notation for keys, it allows us to use any expression as a key, and JavaScript will convert it to a string. _(javascriptallonge.pdf (source-range-83ecb080-01900))_

### values are expressions / Interactive Generators / representing naughts and crosses as a stateful function

- In that case, we need a stateful function. _(javascriptallonge.pdf (source-range-83ecb080-01906))_
- Let’s recap what we have: We have a stateful function, but we built it by wrapping a stateless function in a function that updates state based on the moves we provide. _(javascriptallonge.pdf (source-range-83ecb080-01914))_
- The state is encoded entirely in data. _(javascriptallonge.pdf (source-range-83ecb080-01914))_

### values are expressions / Interactive Generators / this seems familiar

- When we looked at generators, we saw that some iterators are inherently stateful, but sometimes it is awkward to represent them in a fully stateless fashion. _(javascriptallonge.pdf (source-range-83ecb080-01916))_
- Sometimes there is a state machine that is naturally represented implicitly in JavaScript’s control flow rather than explicitly in data. _(javascriptallonge.pdf (source-range-83ecb080-01916))_
- A game like this is absolutely a state machine, and we’ve explicitly coded those states into the lookup table. _(javascriptallonge.pdf (source-range-83ecb080-01917))_
- If we were in full control of the interaction, it would be easy to encode the game play as a decision tree instead of as a lookup table. _(javascriptallonge.pdf (source-range-83ecb080-01918))_
- But we can clearly see that if we wanted to, we could represent the state of the program implicitly in a decision tree. _(javascriptallonge.pdf (source-range-83ecb080-01920))_
- But the first glance is deceptive, because we only see what we’ve seen so far. _(javascriptallonge.pdf (source-range-83ecb080-01924))_
- Let’s see how it would actually work. _(javascriptallonge.pdf (source-range-83ecb080-01924))_
- But the first glance is deceptive, because we only see what we’ve seen so far. _(javascriptallonge.pdf (source-range-83ecb080-01924))_

### values are expressions / Interactive Generators / summary

- We have looked at generators as ways of making iterators over static collections, where state is modelled implicitly in control flow. _(javascriptallonge.pdf (source-range-83ecb080-01937))_
- Again, the salient difference is that an “interactive” generator is stateful, and it embodies its state in its control flow. _(javascriptallonge.pdf (source-range-83ecb080-01938))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01902))_

> { "o,x, , , , , , , ":6, "o,x,x, , , ,o, , ":3, "o,x, ,x, , ,o, , ":8, "o,x, , ,x, ,o, , ":3, "o,x, , , ,x,o, , ":3, "o,x, , , , ,o,x, ":3, "o,x, , , , ,o, ,x":3 } And if we want to look up what move to make, we can write: moveLookupTable[[ 'o', 'x', ' ', ' ' ' ' ' ' , , , 'o', 'x', ' ' _//=> 3_ ]] And from there, a stateless function to play naughts-and-crosses is trivial:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01904))_

> 256 statelessNaughtsAndCrosses([ 'o', 'x', ' ', ' ' ' ' ' ' , , , 'o', 'x', ' ' ]) _//=> 3_

### Technical atom 2

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01907))_

> Something like this: **const** aNaughtsAndCrossesGame = statefulNaughtsAndCrosses();
