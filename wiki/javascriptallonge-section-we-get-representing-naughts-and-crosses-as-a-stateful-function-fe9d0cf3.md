---
page_id: javascriptallonge-section-we-get-representing-naughts-and-crosses-as-a-stateful-function-fe9d0cf3
page_kind: source
page_family: section-reference
summary: We get: / representing naughts and crosses as a stateful function: 5 source-backed entries and 0 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-we-get-representing-naughts-and-crosses-as-a-stateful-function-fe9d0cf3@df773ab4ccc5206d4cc6a0b5335589ba
---

# We get: / representing naughts and crosses as a stateful function

From [[javascriptallonge]].

## Related pages

### Source structure

- [[javascriptallonge-section-we-get-2605e005]] - broader source section: We get:

## Statements

- Our statelessNaughtsAndCrosses function pushes the work of tracking the game's state onto us, the player. What if we want to exchange moves with the function? In that case, we need a stateful function. Our 'API' will work like this: When we want a new game, we'll call a function that will return a game function, We'll call the game function repeatedly, passing our moves, and get the opponent's moves from it. _(javascriptallonge.pdf (source-range-7239e085-01922))_
- Let's recap what we have: We have a stateful function, but we built it by wrapping a stateless function in a function that updates state based on the moves we provide. The state is encoded entirely in data. _(javascriptallonge.pdf (source-range-7239e085-01928))_
