---
page_id: javascriptallonge-section-representing-naughts-and-crosses-as-a-stateful-function-42b09e48
page_kind: source
summary: representing naughts and crosses as a stateful function: 5 source-backed entries and 3 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-representing-naughts-and-crosses-as-a-stateful-function-42b09e48@1ca434a0355248dc5c0faa2d22c62595
---

# representing naughts and crosses as a stateful function

From [[javascriptallonge]].

## Statements

- Our statelessNaughtsAndCrosses function pushes the work of tracking the game's state onto us, the player. What if we want to exchange moves with the function? In that case, we need a stateful function. Our 'API' will work like this: When we want a new game, we'll call a function that will return a game function, We'll call the game function repeatedly, passing our moves, and get the opponent's moves from it. _(javascriptallonge.pdf (source-range-31a4cf47-01923))_
- Let's recap what we have: We have a stateful function, but we built it by wrapping a stateless function in a function that updates state based on the moves we provide. The state is encoded entirely in data. _(javascriptallonge.pdf (source-range-31a4cf47-01929))_

## Technical atoms

### Technical frame 1: representing naughts and crosses as a stateful function

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01929))_

> Let's recap what we have: We have a stateful function, but we built it by wrapping a stateless function in a function that updates state based on the moves we provide. The state is encoded entirely in data.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01925))_

```
const aNaughtsAndCrossesGame = statefulNaughtsAndCrosses(); // our opponent makes the first move aNaughtsAndCrossesGame() //=> 0 // then we move, and get its next move back aNaughtsAndCrossesGame(1) //=> 6 // then we move, and get its next move back aNaughtsAndCrossesGame(4) //=> 3
```

### Technical frame 2: representing naughts and crosses as a stateful function

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01929))_

> Let's recap what we have: We have a stateful function, but we built it by wrapping a stateless function in a function that updates state based on the moves we provide. The state is encoded entirely in data.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01927))_

```
const statefulNaughtsAndCrosses = () => { const state = [ ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ' ]; return (x = false ) => { if (x) {
```

### Technical frame 3: representing naughts and crosses as a stateful function

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01929))_

> Let's recap what we have: We have a stateful function, but we built it by wrapping a stateless function in a function that updates state based on the moves we provide. The state is encoded entirely in data.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01928))_

```
if (state[x] === ' ') { state[x] = 'x'; } else throw "occupied!" } let o = moveLookupTable[state]; state[o] = 'o'; return o; } }; const aNaughtsAndCrossesGame = statefulNaughtsAndCrosses(); // our opponent makes the first move aNaughtsAndCrossesGame() //=> 0 // then we move, and get its next move back aNaughtsAndCrossesGame(1) //=> 6 // then we move, and get its next move back aNaughtsAndCrossesGame(4) //=> 3
```
