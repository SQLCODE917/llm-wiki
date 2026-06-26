---
page_id: javascriptallonge-interactive-generators
page_kind: source
summary: Interactive Generators from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.273-283
updated: 2026-06-25
source_id: javascriptallonge.pdf
---

## Source record

Chapter on interactive generators in JavaScript Allongé, covering stateful functions and generator-based state management.

## Key supported claims

- Generators can be used to build iterators that maintain implicit state (raw/javascriptallonge.pdf p.273-283).
- Interactive generators allow passing values in and receiving values out, functioning like stateful functions (raw/javascriptallonge.pdf p.273-283).
- The chapter demonstrates building a stateful naughts and crosses game using both stateless and stateful approaches (raw/javascriptallonge.pdf p.273-283).

## Technical details

### `technical-atom-1bf2f64b233003fc` code

Citation: (raw/javascriptallonge.pdf p.273-283)

```javascript
const moveLookupTable = { [[
```

### `technical-atom-ba2e2fde01ca8483` code

Citation: (raw/javascriptallonge.pdf p.273-283)

```
};
```

### `technical-atom-fb12246462a2a22b` code

Citation: (raw/javascriptallonge.pdf p.273-283)

```
{ "o,x,,,,,,, ":6, "o,x,x,,,,o,, ":3, "o,x,,x,,,o,, ":8, "o,x,,,x,,o,, ":3, "o,x,,,,x,o,, ":3, "o,x,,,,,o,x, ":3, "o,x,,,,,o,,x":3 }
```

### `technical-atom-f2826d58755cc716` code

Citation: (raw/javascriptallonge.pdf p.273-283)

```javascript
Our statelessNaughtsAndCrosses function pushes the work of tracking the game’s state onto us, the player. What if we want to exchange moves with the function? In that case, we need a stateful function. Our “API” will work like this: When we want a new game, we’ll call a function that will return a game function, We’ll call the game function repeatedly, passing our moves, and get the opponent’s moves from it.
```

### `technical-atom-51878d5c896ac9fe` code

Citation: (raw/javascriptallonge.pdf p.273-283)

```javascript
const aNaughtsAndCrossesGame = statefulNaughtsAndCrosses();
```

### `technical-atom-7bf9ccafcfec19cf` code

Citation: (raw/javascriptallonge.pdf p.273-283)

```javascript
const statefulNaughtsAndCrosses = () => { const state = [ ' ' ' ' ' ',,, ' ' ' ' ' ',,, ' ' ' ' ' ',,]; return (x = false) => { if (x) {
```

### `technical-atom-f26db54775106b2f` code

Citation: (raw/javascriptallonge.pdf p.273-283)

```javascript
if (state[x] === ' ') { state[x] = 'x'; } else throw "occupied!" } let o = moveLookupTable[state]; state[o] = 'o'; return o; } };
```

### `technical-atom-fea22f8d96e4b12f` code

Citation: (raw/javascriptallonge.pdf p.273-283)

```javascript
function browserNaughtsAndCrosses () { const x1 = parseInt(prompt('o plays 0, where does x play?')); switch (x1) { case 1: const x2 = parseInt(prompt('o plays 6, where does x play?')); switch (x2) { case 2: case 4: case 5: case 7: case 8: alert('o plays 3'); break; case 3: const x3 = parseInt(prompt('o plays 8, where does x play?')); switch (x3) { case 2: case 5: case 7: alert('o plays 4'); break; case 4: alert('o plays 7'); break; } } break; // ... } }
```

## Related technical details

### From [[javascriptallonge-iteration-and-iterables]]: `technical-atom-d3b675be6d62eed9` code

Relation: nearby source page; matched terms `javascript`, `method`, `other`

Citation: (raw/javascriptallonge.pdf p.206-223)

```javascript
Since JavaScript doesn’t bind this within a fat arrow function, we follow the same rules of variable scoping as any other variable name: We check in the environment enclosing the function. Although the .iterator() method has returned, its environment is the one that encloses our () => { ... } function, and that’s where this is bound to the value of stack.
```
