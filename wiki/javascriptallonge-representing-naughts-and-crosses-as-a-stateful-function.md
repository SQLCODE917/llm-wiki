---
page_id: javascriptallonge-representing-naughts-and-crosses-as-a-stateful-function
page_kind: source
summary: representing naughts and crosses as a stateful function from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.279-280
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

This section discusses how to represent naughts and crosses (tic-tac-toe) as a stateful function in JavaScript, showing how to create a game function that maintains its own state.

## Key supported claims

- Stateful function needed when exchanging moves with function. (raw/javascriptallonge.pdf p.279-280)
- Game API works by calling function to get new game, then calling game function repeatedly with moves. (raw/javascriptallonge.pdf p.279-280)
- Stateless function pushes state tracking work to player. (raw/javascriptallonge.pdf p.279-280)

## Technical details

### `technical-atom-37fcc5b39da4d3d0` code

Citation: (raw/javascriptallonge.pdf p.279-280)

```javascript
const aNaughtsAndCrossesGame = statefulNaughtsAndCrosses(); // our opponent makes the first move aNaughtsAndCrossesGame() //=> 0 // then we move, and get its next move back aNaughtsAndCrossesGame(1) //=> 6 // then we move, and get its next move back aNaughtsAndCrossesGame(4) //=> 3
```

### `technical-atom-07a24be90ab6d893` code

Citation: (raw/javascriptallonge.pdf p.279-280)

```javascript
const statefulNaughtsAndCrosses = () => { const state = [ ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ' ]; return (x = false ) => { if (x) {
```

### `technical-atom-c33ecf682ee5c6e8` code

Citation: (raw/javascriptallonge.pdf p.279-280)

```javascript
if (state[x] === ' ') { state[x] = 'x'; } else throw "occupied!" } let o = moveLookupTable[state]; state[o] = 'o'; return o; } }; const aNaughtsAndCrossesGame = statefulNaughtsAndCrosses(); // our opponent makes the first move aNaughtsAndCrossesGame() //=> 0 // then we move, and get its next move back aNaughtsAndCrossesGame(1) //=> 6 // then we move, and get its next move back aNaughtsAndCrossesGame(4) //=> 3
```
