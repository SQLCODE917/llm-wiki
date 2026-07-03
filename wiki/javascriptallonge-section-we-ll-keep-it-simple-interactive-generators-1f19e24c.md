---
page_id: javascriptallonge-section-we-ll-keep-it-simple-interactive-generators-1f19e24c
page_kind: source
page_family: section-reference
summary: We'll keep it simple: / Interactive Generators: 18 source-backed entries and 0 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-we-ll-keep-it-simple-interactive-generators-1f19e24c@b3ee3834d15fc3dbc3674eb3a074ea30
---

# We'll keep it simple: / Interactive Generators

From [[javascriptallonge]].

## Related pages

### Source structure

- [[javascriptallonge-section-we-ll-keep-it-simple-1104ef0d]] - broader source section: We'll keep it simple:
- [[javascriptallonge-section-we-ll-keep-it-simple-interactive-generators-representing-naughts-and-crosses-as-a-stateless-func-df9810de]] - narrower source section: We'll keep it simple: / Interactive Generators / representing naughts and crosses as a stateless function

### Other

- [[javascriptallonge-section-we-get-interactive-generators-6808178d]] - same source heading: another source section with the same heading, We get: / interactive generators

## Statements

- We used generators to build iterators that maintain implicit state. We saw how to use them for recursive unfolds and state machines. But there are other times we want to build functions that maintain implicit state. Let's start by looking at a very simple example of a function that can be written statefully. _(javascriptallonge.pdf (source-range-7239e085-01873))_
- Consider, for example, the moves in a game. The moves a player makes are a stream of values, just like the contents of an array can be consider a stream of values. But of course, iterating over a stream of moves requires us to wait for the game to be over so we know what moves were made. _(javascriptallonge.pdf (source-range-7239e085-01876))_
- The first player will always be o , and they will always place their chequer in the top-left corner, coincidentally numbered o : _(javascriptallonge.pdf (source-range-7239e085-01878))_

## Statements by subsection

### We'll keep it simple: / Interactive Generators / representing naughts and crosses as a stateless function

- We could plays naughts and crosses as a stateless function. We encode each position of the board in some fashion, and then we build a dictionary from positions to moves. For example, the entry for: _(javascriptallonge.pdf (source-range-7239e085-01895))_
