---
page_id: javascriptallonge-recipe-representing-naughts-and-crosses-as-a-stateful-function
page_kind: recipe
page_family: recipe-pattern
summary: representing naughts and crosses as a stateful function: reusable source-backed pattern with 2 statement(s) and 3 technical atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: representing-naughts-and-crosses-as-a-stateful-function
projection_coverage: recipe-javascriptallonge-recipe-representing-naughts-and-crosses-as-a-stateful-function@1172cd24a5b4ffce1f60950fa0b75b56
---

# representing naughts and crosses as a stateful function

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-we-get-representing-naughts-and-crosses-as-a-stateful-function-fe9d0cf3]].
- Evidence roles: decision, example.

## Applicability And Rationale

- In that case, we need a stateful function. _(javascriptallonge.pdf (source-range-7239e085-01922))_
- The state is encoded entirely in data. _(javascriptallonge.pdf (source-range-7239e085-01928))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01924)_

```
const aNaughtsAndCrossesGame = statefulNaughtsAndCrosses();
// our opponent makes the first move
aNaughtsAndCrossesGame()
//=> 0
// then we move, and get its next move back
aNaughtsAndCrossesGame(1)
//=> 6
// then we move, and get its next move back
aNaughtsAndCrossesGame(4)
//=> 3
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01926)_

```
const statefulNaughtsAndCrosses = () => {
const state = [
' ', ' ', ' ',
' ', ' ', ' ',
' ', ' ', ' '
];
return (x = false) => {
if (x) {
```

### Atom 3: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01927)_

```
if (state[x] === ' ') {
state[x] = 'x';
}
else throw "occupied!"
}
let o = moveLookupTable[state];
state[o] = 'o';
return o;
}
};
const aNaughtsAndCrossesGame = statefulNaughtsAndCrosses();
// our opponent makes the first move
aNaughtsAndCrossesGame()
//=> 0
// then we move, and get its next move back
aNaughtsAndCrossesGame(1)
//=> 6
// then we move, and get its next move back
aNaughtsAndCrossesGame(4)
//=> 3
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-we-get-representing-naughts-and-crosses-as-a-stateful-function-fe9d0cf3]]
