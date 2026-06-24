---
page_id: javascriptallonge-we-get
page_kind: source
summary: We get: from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.278-279
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

Chapter on stateless functions and naughts-and-crosses game implementation in JavaScript.

## Key supported claims

- And from there, a stateless function to play naughts-and-crosses is trivial: (raw/javascriptallonge.pdf p.278-279).
- And if we want to look up what move to make, we can write: (raw/javascriptallonge.pdf p.278-279).

## Technical details

### `technical-atom-cb2eff94e55c00d0` code

Citation: (raw/javascriptallonge.pdf p.278-279)

```
{ "o,x, , , , , , , ":6, "o,x,x, , , ,o, , ":3, "o,x, ,x, , ,o, , ":8, "o,x, , ,x, ,o, , ":3, "o,x, , , ,x,o, , ":3, "o,x, , , , ,o,x, ":3, "o,x, , , , ,o, ,x":3 }
```

### `technical-atom-64bc3261890a798c` code

Citation: (raw/javascriptallonge.pdf p.278-279)

```javascript
moveLookupTable[[ 'o', 'x', ' ', ' ', ' ', ' ', 'o', 'x', ' ' ]] //=> 3
```

### `technical-atom-bf68af0b793b420a` code

Citation: (raw/javascriptallonge.pdf p.278-279)

```javascript
statelessNaughtsAndCrosses([ 'o', 'x', ' ', ' ', ' ', ' ', 'o', 'x', ' ' ]) //=> 3
```

## Related technical details

### From [[javascriptallonge-representing-naughts-and-crosses-as-a-stateful-function]]: `technical-atom-37fcc5b39da4d3d0` code

Relation: nearby source page; matched terms `function`, `get`, `move`

Citation: (raw/javascriptallonge.pdf p.279-280)

```javascript
const aNaughtsAndCrossesGame = statefulNaughtsAndCrosses(); // our opponent makes the first move aNaughtsAndCrossesGame() //=> 0 // then we move, and get its next move back aNaughtsAndCrossesGame(1) //=> 6 // then we move, and get its next move back aNaughtsAndCrossesGame(4) //=> 3
```

### From [[javascriptallonge-representing-naughts-and-crosses-as-a-stateful-function]]: `technical-atom-c33ecf682ee5c6e8` code

Relation: nearby source page; matched terms `function`, `get`, `move`

Citation: (raw/javascriptallonge.pdf p.279-280)

```javascript
if (state[x] === ' ') { state[x] = 'x'; } else throw "occupied!" } let o = moveLookupTable[state]; state[o] = 'o'; return o; } }; const aNaughtsAndCrossesGame = statefulNaughtsAndCrosses(); // our opponent makes the first move aNaughtsAndCrossesGame() //=> 0 // then we move, and get its next move back aNaughtsAndCrossesGame(1) //=> 6 // then we move, and get its next move back aNaughtsAndCrossesGame(4) //=> 3
```
