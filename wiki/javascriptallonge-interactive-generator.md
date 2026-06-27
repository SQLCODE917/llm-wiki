---
page_id: javascriptallonge-interactive-generator
page_kind: concept
summary: Interactive Generators: 33 statement(s) and 5 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-interactive-generator@5eb5cb3c5d062b4857b4410823f7cf62
---

# Interactive Generators

What [[javascriptallonge]] covers about interactive generators:

## Statements

_Showing 14 of 33 statements selected for this topic._

- But the generator function allows us to maintain state implicitly. _(javascriptallonge.pdf (source-range-83ecb080-03043))_
- We used generators to build iterators that maintain implicit state. _(javascriptallonge.pdf (source-range-83ecb080-02926))_
- When we looked at generators, we saw that some iterators are inherently stateful, but sometimes it is awkward to represent them in a fully stateless fashion. _(javascriptallonge.pdf (source-range-83ecb080-03013))_
- If we could do that, a generator function that played naughts and crosses would look like this: _(javascriptallonge.pdf (source-range-83ecb080-03026))_
- So far, we have called iterators (and generators) with .next(). _(javascriptallonge.pdf (source-range-83ecb080-03026))_
- Thereafter, we call .next(...) and pass in our moves (The very first call has to be .next() without any arguments, because the generator hasn’t started yet. _(javascriptallonge.pdf (source-range-83ecb080-03033))_
- We have looked at generators as ways of making iterators over static collections, where state is modelled implicitly in control flow. _(javascriptallonge.pdf (source-range-83ecb080-03045))_
- Again, the salient difference is that an “interactive” generator is stateful, and it embodies its state in its control flow. _(javascriptallonge.pdf (source-range-83ecb080-03046))_
- We saw how to use them for recursive unfolds and state machines. _(javascriptallonge.pdf (source-range-83ecb080-02926))_
- But there are other times we want to build functions that maintain implicit state. _(javascriptallonge.pdf (source-range-83ecb080-02926))_
- Let’s start by looking at a very simple example of a function that can be written statefully. _(javascriptallonge.pdf (source-range-83ecb080-02926))_
- The moves a player makes are a stream of values, just like the contents of an array can be consider a stream of values. _(javascriptallonge.pdf (source-range-83ecb080-02929))_
- But of course, iterating over a stream of moves requires us to wait for the game to be over so we know what moves were made. _(javascriptallonge.pdf (source-range-83ecb080-02929))_
- Let’s take a look at a very simple example, naughts and crosses[99] (We really ought to do something like Chess, but that might be a little out of scope for this chapter). _(javascriptallonge.pdf (source-range-83ecb080-02930))_

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


## Source

- [[javascriptallonge]]
