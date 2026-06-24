---
page_id: javascriptallonge-interactive-generators
page_kind: source
summary: interactive generators from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.282-283
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

Interactive Generators chapter covering generators, stateful functions, and examples.

## Key supported claims

- So far, we have called iterators (and generators) with .next(). (raw/javascriptallonge.pdf p.282-283)
- Thereafter, we call .next(...) and pass in our moves (The very first call has to be .next() without any arguments, because the generator hasn't started yet.) (raw/javascriptallonge.pdf p.282-283)
- If we wanted to pass some state to the generator before it begins, we'd do that with parameters. (raw/javascriptallonge.pdf p.282-283)
- If we could do that, a generator function that played naughts and crosses would look like this: (raw/javascriptallonge.pdf p.282-283)
- Our generator function maintains state implicitly in its control flow, but returns an iterator that we call, it doesn't call us. (raw/javascriptallonge.pdf p.282-283)

## Technical details

### `technical-atom-6ddfd13c4643d485` code

Citation: (raw/javascriptallonge.pdf p.282-283)

```javascript
function * generatorNaughtsAndCrosses () { const x1 = yield 0; switch (x1) { case 1: const x2 = yield 6; switch (x2) { case 2: case 4: case 5: case 7: case 8: yield 3; break ; case 3: const x3 = yield 8; switch (x3) { case 2: case 5: case 7: yield 4; break ; case 4: yield 7; break ;
```

### `technical-atom-449c45b24ee18436` requirement

Citation: (raw/javascriptallonge.pdf p.273-275)

But of course, iterating over a stream of moves requires us to wait for the game to be over so we know what moves were made.

### `technical-atom-85e159978fa2e604` requirement

Citation: (raw/javascriptallonge.pdf p.273-275)

The first player will always be o , and they will always place their chequer in the top-left corner, coincidentally numbered o :

### `technical-atom-91386e0617ecea45` worked-example

Citation: (raw/javascriptallonge.pdf p.273-275)

Let's start by looking at a very simple example of a function that can be written statefully.

### `technical-atom-70bef72c720a597a` worked-example

Citation: (raw/javascriptallonge.pdf p.273-275)

Consider, for example, the moves in a game.

### `technical-atom-772d1b88d2ba5437` worked-example

Citation: (raw/javascriptallonge.pdf p.273-275)

The moves a player makes are a stream of values, just like the contents of an array can be consider a stream of values.

### `technical-atom-dd7f6cd83f5fa7e4` worked-example

Citation: (raw/javascriptallonge.pdf p.273-275)

Let's take a look at a very simple example, naughts and crosses 99 (We really ought to do something like Chess, but that might be a little out of scope for this chapter).

### `technical-atom-ecf1ff5da5d2e045` worked-example

Citation: (raw/javascriptallonge.pdf p.273-275)

Let's consider move 1 .

## Related technical details

### From [[javascriptallonge-this-seems-familiar]]: `technical-atom-45ad4257e07d061d` procedure

Relation: nearby source page; matched terms `control`, `flow`, `function`, `generator`, `iterators`, `procedure`

Citation: (raw/javascriptallonge.pdf p.280-282)

With iterators, we wrote a generator function using function * , and then used yield to yield values while maintaining the implicit state of the generator's control flow.

### From [[javascriptallonge-representing-naughts-and-crosses-as-a-stateful-function]]: `technical-atom-c33ecf682ee5c6e8` code

Relation: nearby source page; matched terms `anaughtsandcrossesgame`, `crosses`, `first`, `function`, `its`, `naughts`

Citation: (raw/javascriptallonge.pdf p.279-280)

```javascript
if (state[x] === ' ') { state[x] = 'x'; } else throw "occupied!" } let o = moveLookupTable[state]; state[o] = 'o'; return o; } }; const aNaughtsAndCrossesGame = statefulNaughtsAndCrosses(); // our opponent makes the first move aNaughtsAndCrossesGame() //=> 0 // then we move, and get its next move back aNaughtsAndCrossesGame(1) //=> 6 // then we move, and get its next move back aNaughtsAndCrossesGame(4) //=> 3
```

### From [[javascriptallonge-representing-naughts-and-crosses-as-a-stateful-function]]: `technical-atom-37fcc5b39da4d3d0` code

Relation: nearby source page; matched terms `anaughtsandcrossesgame`, `crosses`, `first`, `function`, `its`, `naughts`

Citation: (raw/javascriptallonge.pdf p.279-280)

```javascript
const aNaughtsAndCrossesGame = statefulNaughtsAndCrosses(); // our opponent makes the first move aNaughtsAndCrossesGame() //=> 0 // then we move, and get its next move back aNaughtsAndCrossesGame(1) //=> 6 // then we move, and get its next move back aNaughtsAndCrossesGame(4) //=> 3
```

### From [[javascriptallonge-operations-that-transform-an-iterable-into-a-value]]: `technical-atom-381e027872bb52af` code

Relation: nearby source page; matched terms `first`, `iterator`, `next`, `value`

Citation: (raw/javascriptallonge.pdf p.286)

```javascript
const reduceWith = (fn, seed, iterable) => { let accumulator = seed; for ( const element of iterable) { accumulator = fn(accumulator, element); } return accumulator; }; const first = (iterable) => iterable[Symbol.iterator]().next().value;
```
