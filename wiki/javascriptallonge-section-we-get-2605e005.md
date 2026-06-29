---
page_id: javascriptallonge-section-we-get-2605e005
page_kind: source
summary: We get:: 35 source-backed entries and 14 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-29
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-we-get-2605e005@d5374372e523d67ca171202ac6553358
---

# We get:

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-we-get-representing-naughts-and-crosses-as-a-stateful-function-fe9d0cf3]] - narrower source section: We get: / representing naughts and crosses as a stateful function
- [[javascriptallonge-section-we-get-this-seems-familiar-0d4230cb]] - narrower source section: We get: / this seems familiar
- [[javascriptallonge-section-we-get-interactive-generators-6808178d]] - narrower source section: We get: / interactive generators
- [[javascriptallonge-section-we-get-summary-db42c4cd]] - narrower source section: We get: / summary
- [[javascriptallonge-section-we-get-basic-operations-on-iterables-50055b98]] - narrower source section: We get: / Basic Operations on Iterables

## Statements by subsection

### We get: / representing naughts and crosses as a stateful function

- Our statelessNaughtsAndCrosses function pushes the work of tracking the game's state onto us, the player. What if we want to exchange moves with the function? In that case, we need a stateful function. Our 'API' will work like this: When we want a new game, we'll call a function that will return a game function, We'll call the game function repeatedly, passing our moves, and get the opponent's moves from it. _(javascriptallonge.pdf (source-range-7239e085-01922))_
- Let's recap what we have: We have a stateful function, but we built it by wrapping a stateless function in a function that updates state based on the moves we provide. The state is encoded entirely in data. _(javascriptallonge.pdf (source-range-7239e085-01928))_

### We get: / this seems familiar

- When we looked at generators, we saw that some iterators are inherently stateful, but sometimes it is awkward to represent them in a fully stateless fashion. Sometimes there is a state machine that is naturally represented implicitly in JavaScript's control flow rather than explicitly in data. _(javascriptallonge.pdf (source-range-7239e085-01930))_
- We've done almost the exact same thing here with our naughts and crosses game. A game like this is absolutely a state machine, and we've explicitly coded those states into the lookup table. Which leads us to wonder: Is there a way to encode those states implicitly , in JavaScript control flow? _(javascriptallonge.pdf (source-range-7239e085-01931))_
- If we were in full control of the interaction, it would be easy to encode the game play as a decision tree instead of as a lookup table. For example, we could do this in a browser: _(javascriptallonge.pdf (source-range-7239e085-01932))_
- Naughts and crosses is simple enough that the lookup function seems substantially simpler, in part because linear code doesn't represent trees particularly well. But we can clearly see that if we wanted to, we could represent the state of the program implicitly in a decision tree. _(javascriptallonge.pdf (source-range-7239e085-01934))_
- Canwedothesamethinghere?Atfirst glance, no. How do we get the player's moves to the generator function? But the first glance is deceptive, because we only see what we've seen so far. Let's see how it would actually work. _(javascriptallonge.pdf (source-range-7239e085-01936))_
- Naughts and crosses is simple enough that the lookup function seems substantially simpler, in part because linear code doesn't represent trees particularly well. _(javascriptallonge.pdf (source-range-7239e085-01934))_
- But the first glance is deceptive, because we only see what we've seen so far. _(javascriptallonge.pdf (source-range-7239e085-01936))_

### We get: / interactive generators

- So far, we have called iterators (and generators) with .next() . But what if we pass a value to .next() ? If we could do that, a generator function that played naughts and crosses would look like this: _(javascriptallonge.pdf (source-range-7239e085-01938))_
- Served by the Pot: Collections 260 } } break ; // ... } } const aNaughtsAndCrossesGame = generatorNaughtsAndCrosses(); We can then get the first move by calling .next() . Thereafter, we call .next(...) and pass in our moves (The very first call has to be .next() without any arguments, because the generator hasn't started yet. If we wanted to pass some state to the generator before it begins, we'd do that with parameters.): aNaughtsAndCrossesGame.next().value //=> 0 aNaughtsAndCrossesGame.next(1).value //=> 6 aNaughtsAndCrossesGame.next(3).value //=> 8 aNaughtsAndCrossesGame.next(7).value //=> 4 _(javascriptallonge.pdf (source-range-7239e085-01941))_
- Our generator function maintains state implicitly in its control flow, but returns an iterator that we call, it doesn't call us. It isn't a collection, it has no meaning if we try to spread it into parameters or as the subject of a for...of block. _(javascriptallonge.pdf (source-range-7239e085-01942))_
- But the generator function allows us to maintain state implicitly. And sometimes, we want to use implicit state instead of explicitly storing state in our data. _(javascriptallonge.pdf (source-range-7239e085-01943))_
- If we wanted to pass some state to the generator before it begins, we'd do that with parameters.): aNaughtsAndCrossesGame.next().value //=> 0 aNaughtsAndCrossesGame.next(1).value //=> 6 aNaughtsAndCrossesGame.next(3).value //=> 8 aNaughtsAndCrossesGame.next(7).value //=> 4 _(javascriptallonge.pdf (source-range-7239e085-01941))_

### We get: / summary

- We have looked at generators as ways of making iterators over static collections, where state is modelled implicitly in control flow. But as we see here, it's also possible to use a generator interactively, passing values in and receiving a value in return, just like an ordinary function. _(javascriptallonge.pdf (source-range-7239e085-01945))_
- Again, the salient difference is that an 'interactive' generator is stateful, and it embodies its state in its control flow. _(javascriptallonge.pdf (source-range-7239e085-01946))_

### We get: / Basic Operations on Iterables

- Here are the operations we've defined on Iterables. As discussed, they preserve the collection semantics of the iterable they are given: _(javascriptallonge.pdf (source-range-7239e085-01948))_

## Technical atoms

### Technical frame 1: We get:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01916))_

```
{
"o,x, , , , , , , ":6,
"o,x,x, , , ,o, , ":3,
"o,x, ,x, , ,o, , ":8,
"o,x, , ,x, ,o, , ":3,
"o,x, , , ,x,o, , ":3,
"o,x, , , , ,o,x, ":3,
"o,x, , , , ,o, ,x":3
}
```

### Technical frame 2: We get:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01918))_

```
moveLookupTable[[
'o', 'x', ' ',
' ', ' ', ' ',
'o', 'x', ' '
]]
//=> 3
```

### Technical frame 3: We get:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01920))_

```
statelessNaughtsAndCrosses([
'o', 'x', ' ',
' ', ' ', ' ',
'o', 'x', ' '
])
//=> 3
```

### Technical frame 4: We get: / representing naughts and crosses as a stateful function

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01928))_

> Let's recap what we have: We have a stateful function, but we built it by wrapping a stateless function in a function that updates state based on the moves we provide. The state is encoded entirely in data.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01924))_

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

### Technical frame 5: We get: / representing naughts and crosses as a stateful function

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01928))_

> Let's recap what we have: We have a stateful function, but we built it by wrapping a stateless function in a function that updates state based on the moves we provide. The state is encoded entirely in data.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01926))_

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

### Technical frame 6: We get: / representing naughts and crosses as a stateful function

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01928))_

> Let's recap what we have: We have a stateful function, but we built it by wrapping a stateless function in a function that updates state based on the moves we provide. The state is encoded entirely in data.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01927))_

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

### Technical frame 7: We get: / this seems familiar

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01934))_

> Naughts and crosses is simple enough that the lookup function seems substantially simpler, in part because linear code doesn't represent trees particularly well. But we can clearly see that if we wanted to, we could represent the state of the program implicitly in a decision tree.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01933))_

```
function browserNaughtsAndCrosses () {
const x1 = parseInt(prompt('o plays 0, where does x play?'));
switch (x1) {
case 1:
const x2 = parseInt(prompt('o plays 6, where does x play?'));
switch (x2) {
case 2:
case 4:
case 5:
case 7:
case 8:
alert('o plays 3');
break;
case 3:
const x3 = parseInt(prompt('o plays 8, where does x play?'));
switch (x3) {
case 2:
case 5:
case 7:
alert('o plays 4');
break;
case 4:
alert('o plays 7');
break;
}
}
break;
// ...
}
}
```

### Technical frame 8: We get: / interactive generators

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01941))_

> Served by the Pot: Collections 260 } } break ; // ... } } const aNaughtsAndCrossesGame = generatorNaughtsAndCrosses(); We can then get the first move by calling .next() . Thereafter, we call .next(...) and pass in our moves (The very first call has to be .next() without any arguments, because the generator hasn't started yet. If we wanted to pass some state to the generator before it begins, we'd do that with parameters.): aNaughtsAndCrossesGame.next().value //=> 0 aNaughtsAndCrossesGame.next(1)

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01940))_

```
function* generatorNaughtsAndCrosses () {
const x1 = yield 0;
switch (x1) {
case 1:
const x2 = yield 6;
switch (x2) {
case 2:
case 4:
case 5:
case 7:
case 8:
yield 3;
break;
case 3:
const x3 = yield 8;
switch (x3) {
case 2:
case 5:
case 7:
yield 4;
break;
case 4:
yield 7;
break;
```

### Technical frame 9: We get: / Basic Operations on Iterables / operations that transform one iterable into another

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01950))_

```
function * mapWith(fn, iterable) {
for (const element of iterable) {
yield fn(element);
}
}
function * mapAllWith (fn, iterable) {
for (const element of iterable) {
yield * fn(element);
}
}
function * filterWith (fn, iterable) {
for (const element of iterable) {
if (!!fn(element)) yield element;
}
}
function * compact (iterable) {
for (const element of iterable) {
if (element != null) yield element;
}
}
function * untilWith (fn, iterable) {
for (const element of iterable) {
if (fn(element)) break;
yield fn(element);
}
}
function * rest (iterable) {
const iterator = iterable[Symbol.iterator]();
iterator.next();
```

### Technical frame 10: We get: / Basic Operations on Iterables / operations that transform one iterable into another

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01951))_

```
yield * iterator;
}
function * take (numberToTake, iterable) {
const iterator = iterable[Symbol.iterator]();
for (let i = 0; i < numberToTake; ++i) {
const { done, value } = iterator.next();
if (!done) yield value;
}
}
```

### Technical frame 11: We get: / Basic Operations on Iterables / operations that compose two or more iterables into an iterable

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01953))_

```
function * zip (...iterables) {
const iterators = iterables.map(i => i[Symbol.iterator]());
while (true) {
const pairs = iterators.map(j => j.next()),
dones = pairs.map(p => p.done),
values = pairs.map(p => p.value);
if (dones.indexOf(true) >= 0) break;
yield values;
}
};
function * zipWith (zipper, ...iterables) {
const iterators = iterables.map(i => i[Symbol.iterator]());
while (true) {
const pairs = iterators.map(j => j.next()),
dones = pairs.map(p => p.done),
values = pairs.map(p => p.value);
if (dones.indexOf(true) >= 0) break;
yield zipper(...values);
}
};
```

### Technical frame 12: We get: / Basic Operations on Iterables / operations that compose two or more iterables into an iterable

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01955))_

```
const zip = callFirst(zipWith, (...values) => values);
```

### Technical frame 13: We get: / Basic Operations on Iterables / operations that transform an iterable into a value

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01957))_

```
const reduceWith = (fn, seed, iterable) => {
let accumulator = seed;
for (const element of iterable) {
accumulator = fn(accumulator, element);
}
return accumulator;
};
const first = (iterable) =>
iterable[Symbol.iterator]().next().value;
```

### Technical frame 14: We get: / Basic Operations on Iterables / memoizing an iterable

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01959))_

```
function memoize (generator) {
const memos = {},
iterators = {};
return function * (...args) {
const key = JSON.stringify(args);
let i = 0;
if (memos[key] == null) {
memos[key] = [];
iterators[key] = generator(...args);
}
while (true) {
if (i < memos[key].length) {
yield memos[key][i++];
}
else {
const { done, value } = iterators[key].next();
if (done) {
return;
} else {
yield memos[key][i++] = value;
```
