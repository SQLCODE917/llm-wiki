---
page_id: javascriptallonge-section-interactive-generators-a0af33e2
page_kind: source
summary: **Interactive Generators**: 10 source-backed entries and 0 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-interactive-generators-a0af33e2@2c0db2436c4f2898022abd4fbaa05902
---

# **Interactive Generators**

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
