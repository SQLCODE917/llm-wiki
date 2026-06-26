---
page_id: javascriptallonge-basic-operations-on-iterables
page_kind: source
summary: Basic Operations on Iterables from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.284-287
updated: 2026-06-25
source_id: javascriptallonge.pdf
---

## Source record

Chapter on basic operations on iterables from JavaScript Allongé.

## Key supported claims

- The chapter defines operations that transform one iterable into another, preserving collection semantics (raw/javascriptallonge.pdf p.284-287).
- Operations such as mapWith, filterWith, and compact are defined to work with iterables (raw/javascriptallonge.pdf p.284-287).
- Functions like zip and zipWith compose iterables into new iterables (raw/javascriptallonge.pdf p.284-287).

## Technical details

### `technical-atom-06f854f6dd0c3ede` code

Citation: (raw/javascriptallonge.pdf p.284-287)

```javascript
function * mapWith(fn, iterable) { for ( const element of iterable) { yield fn(element); } } function * mapAllWith (fn, iterable) { for ( const element of iterable) { yield * fn(element); } } function * filterWith (fn, iterable) { for ( const element of iterable) { if (!!fn(element)) yield element; } } function * compact (iterable) { for ( const element of iterable) { if (element != null) yield element; } } function * untilWith (fn, iterable) { for ( const element of iterable) { if (fn(element)) break; yield fn(element); } } function * rest (iterable) { const iterator = iterable[Symbol.iterator](); iterator.next();
```

### `technical-atom-df7b24412c801324` code

Citation: (raw/javascriptallonge.pdf p.284-287)

```
yield * iterator;
```

### `technical-atom-63329da7d920a7fa` code

Citation: (raw/javascriptallonge.pdf p.284-287)

```javascript
function * take (numberToTake, iterable) { const iterator = iterable[Symbol.iterator]();
```

### `technical-atom-2b89d49174101755` code

Citation: (raw/javascriptallonge.pdf p.284-287)

```javascript
for ( let i = 0; i < numberToTake; ++i) { const { done, value } = iterator.next(); if (!done) yield value; } }
```

### `technical-atom-4cea242ebaa5e4ee` code

Citation: (raw/javascriptallonge.pdf p.284-287)

```javascript
function * zip (...iterables) { const iterators = iterables.map(i => i[Symbol.iterator]());
```

### `technical-atom-0f13977ab1af3729` code

Citation: (raw/javascriptallonge.pdf p.284-287)

```javascript
const zip = callFirst(zipWith, (...values) => values);
```

### `technical-atom-f2f0a17d2e54f703` code

Citation: (raw/javascriptallonge.pdf p.284-287)

```javascript
const reduceWith = (fn, seed, iterable) => { let accumulator = seed;
```

### `technical-atom-35b2273acd61afdb` code

Citation: (raw/javascriptallonge.pdf p.284-287)

```javascript
for ( const element of iterable) { accumulator = fn(accumulator, element); } return accumulator; }; const first = (iterable) => iterable[Symbol.iterator]().next().value;
```

## Related technical details

### From [[javascriptallonge-lazy-and-eager-collections]]: `technical-atom-8d6f83afe6ff7090` code

Relation: nearby source page; matched terms `const`, `function`, `iterable`, `true`

Citation: (raw/javascriptallonge.pdf p.246-260)

```javascript
const Pair = (car, cdr = EMPTY) => Object.assign({ car, cdr, isEmpty: () => false, [Symbol.iterator]: function () { let currentPair = this; return { next: () => { if (currentPair.isEmpty()) { return {done: true } } else { const value = currentPair.car; currentPair = currentPair.cdr; return {done: false, value} } } } } }, LazyCollection); Pair.from = (iterable) => ( function iterationToList (iteration) { const {done, value} = iteration.next();
```

### From [[javascriptallonge-generating-iterables]]: `technical-atom-7ed179c7b89bbe8f` code

Relation: nearby source page; matched terms `const`, `element`, `iterable`, `iterables`

Citation: (raw/javascriptallonge.pdf p.224-245)

```javascript
const generate = (iterable) => { for ( let element of iterable) { if (isIterable(element)) { generate(element) } else { console.log(element) } } } generate([1, [2, [3, 4], 5]]) //=> 1 2 3 4 5
```

### From [[javascriptallonge-interactive-generators]]: `technical-atom-f2826d58755cc716` code

Relation: nearby source page; matched terms `function`, `like`, `new`, `work`

Citation: (raw/javascriptallonge.pdf p.273-283)

```javascript
Our statelessNaughtsAndCrosses function pushes the work of tracking the game’s state onto us, the player. What if we want to exchange moves with the function? In that case, we need a stateful function. Our “API” will work like this: When we want a new game, we’ll call a function that will return a game function, We’ll call the game function repeatedly, passing our moves, and get the opponent’s moves from it.
```

### From [[javascriptallonge-lazy-and-eager-collections]]: `technical-atom-a52c46f037bbeeb7` code

Relation: nearby source page; matched terms `const`, `function`, `key`, `map`

Citation: (raw/javascriptallonge.pdf p.246-260)

```javascript
const extend = function (consumer, ...providers) { for ( let i = 0; i < providers.length; ++i) { const provider = providers[i]; for ( let key in provider) { if (provider.hasOwnProperty(key)) { consumer[key] = provider[key] } } } return consumer }; const LazyCollection = { map(fn) { return Object.assign({ [Symbol.iterator]: () => { const iterator = this [Symbol.iterator](); return { next: () => { const { done, value } = iterator.next(); return ({ done, value: done ? undefined: fn(value) }); } } } }, LazyCollection); }, reduce(fn, seed) { const iterator = this [Symbol.iterator](); let iterationResult, accumulator = seed; while ((iterationResult = iterator.next(), !iterationResult.done)) { accumulator = fn(accumulator, iterationResult.value); } return accumulator;
```
