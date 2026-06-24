---
page_id: javascriptallonge-this-seems-familiar
page_kind: source
summary: this seems familiar from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.280-282
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

Chapter on implicit state encoding in JavaScript control flow, particularly with generators and naughts and crosses game.

## Key supported claims

- Generators can represent stateful iterators implicitly through control flow rather than explicit data structures, as seen in the naughts and crosses game (raw/javascriptallonge.pdf p.280-282).
- The naughts and crosses game is a state machine that can be encoded implicitly in JavaScript control flow (raw/javascriptallonge.pdf p.280-282).
- A decision tree approach could encode game play implicitly in JavaScript control flow, showing that control flow can represent state (raw/javascriptallonge.pdf p.280-282).
- The control flow inversion in the current solution means the generator is called by the game rather than the game calling the generator, making it difficult to pass moves to the generator (raw/javascriptallonge.pdf p.280-282).

## Technical details

### `technical-atom-8252c71d11b6fdf7` code

Citation: (raw/javascriptallonge.pdf p.280-282)

```javascript
function browserNaughtsAndCrosses () { const x1 = parseInt(prompt('o plays 0, where does x play?')); switch (x1) { case 1: const x2 = parseInt(prompt('o plays 6, where does x play?')); switch (x2) { case 2: case 4: case 5: case 7: case 8: alert('o plays 3'); break ; case 3: const x3 = parseInt(prompt('o plays 8, where does x play?')); switch (x3) { case 2: case 5: case 7: alert('o plays 4'); break ; case 4: alert('o plays 7'); break ; } } break ; // ... } }
```

### `technical-atom-45ad4257e07d061d` procedure

Citation: (raw/javascriptallonge.pdf p.280-282)

With iterators, we wrote a generator function using function * , and then used yield to yield values while maintaining the implicit state of the generator's control flow.

### `technical-atom-2b5b4d3b6053b250` exception

Citation: (raw/javascriptallonge.pdf p.280-282)

But the first glance is deceptive, because we only see what we've seen so far.

### `technical-atom-054368b800c668ce` worked-example

Citation: (raw/javascriptallonge.pdf p.280-282)

For example, we could do this in a browser:

## Related technical details

### From [[javascriptallonge-interactive-generators]]: `technical-atom-dd7f6cd83f5fa7e4` worked-example

Relation: nearby source page; matched terms `crosses`, `generators`, `naughts`, `simple`

Citation: (raw/javascriptallonge.pdf p.273-275)

Let's take a look at a very simple example, naughts and crosses 99 (We really ought to do something like Chess, but that might be a little out of scope for this chapter).

### From [[javascriptallonge-representing-naughts-and-crosses-as-a-stateful-function]]: `technical-atom-c33ecf682ee5c6e8` code

Relation: nearby source page; matched terms `crosses`, `first`, `function`, `naughts`, `state`, `stateful`

Citation: (raw/javascriptallonge.pdf p.279-280)

```javascript
if (state[x] === ' ') { state[x] = 'x'; } else throw "occupied!" } let o = moveLookupTable[state]; state[o] = 'o'; return o; } }; const aNaughtsAndCrossesGame = statefulNaughtsAndCrosses(); // our opponent makes the first move aNaughtsAndCrossesGame() //=> 0 // then we move, and get its next move back aNaughtsAndCrossesGame(1) //=> 6 // then we move, and get its next move back aNaughtsAndCrossesGame(4) //=> 3
```

### From [[javascriptallonge-representing-naughts-and-crosses-as-a-stateful-function]]: `technical-atom-37fcc5b39da4d3d0` code

Relation: nearby source page; matched terms `crosses`, `first`, `function`, `naughts`, `stateful`

Citation: (raw/javascriptallonge.pdf p.279-280)

```javascript
const aNaughtsAndCrossesGame = statefulNaughtsAndCrosses(); // our opponent makes the first move aNaughtsAndCrossesGame() //=> 0 // then we move, and get its next move back aNaughtsAndCrossesGame(1) //=> 6 // then we move, and get its next move back aNaughtsAndCrossesGame(4) //=> 3
```

### From [[javascriptallonge-representing-naughts-and-crosses-as-a-stateful-function]]: `technical-atom-07a24be90ab6d893` code

Relation: nearby source page; matched terms `crosses`, `function`, `naughts`, `state`, `stateful`

Citation: (raw/javascriptallonge.pdf p.279-280)

```javascript
const statefulNaughtsAndCrosses = () => { const state = [ ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ' ]; return (x = false ) => { if (x) {
```
