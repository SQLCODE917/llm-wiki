---
page_id: javascriptallonge-lazy-and-eager-collections
page_kind: source
summary: eager collections from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.256-260
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

Chapter on eager and lazy collections in JavaScript Allongé.

## Key supported claims

- An eager collection returns a collection of its own type from each method, and can be made from any gatherable collection. (raw/javascriptallonge.pdf p.256-260)
- EagerCollection is a mixin that adds methods like map, filter, and reduce to gatherable collections. (raw/javascriptallonge.pdf p.256-260)
- The Pair implementation shows how to mix EagerCollection into a gatherable type to get collection methods. (raw/javascriptallonge.pdf p.256-260)

## Technical details

### `technical-atom-99a2145043bdd766` code

Citation: (raw/javascriptallonge.pdf p.256-260)

```javascript
const extend = function (consumer, ...providers) { for ( let i = 0; i < providers.length; ++i) { const provider = providers[i]; for ( let key in provider) { if (provider.hasOwnProperty(key)) { consumer[key] = provider[key] } } } return consumer };
```

### `technical-atom-f43855f5c684acd6` code

Citation: (raw/javascriptallonge.pdf p.256-260)

```javascript
const EagerCollection = (gatherable) => ({ map(fn) { const original = this ; return gatherable.from( ( function * () { for ( let element of original) { yield fn(element); } })() ); }, reduce(fn, seed) { let accumulator = seed; for ( let element of this ) { accumulator = fn(accumulator, element); } return accumulator; }, filter(fn) { const original = this ; return gatherable.from( ( function * () { for ( let element of original) { if (fn(element)) yield element; } })() ); }, find(fn) { for ( let element of this ) { if (fn(element)) return element; } }, until(fn) {
```

### `technical-atom-d9ccc197c7d25dc0` code

Citation: (raw/javascriptallonge.pdf p.256-260)

```javascript
const original = this ; return gatherable.from( ( function * () { for ( let element of original) { if (fn(element)) break ; yield element; } })() ); }, first() { return this [Symbol.iterator]().next().value; }, rest() { const iteration = this [Symbol.iterator](); iteration.next(); return gatherable.from( ( function * () { yield * iteration; })() ); return gatherable.from(iterable); }, take(numberToTake) { const original = this ; let numberRemaining = numberToTake; return gatherable.from( ( function * () { for ( let element of original) { if (numberRemaining-- <= 0) break ; yield element; } })() ); } });
```

### `technical-atom-f3a0c8d86a0e5487` code

Citation: (raw/javascriptallonge.pdf p.256-260)

```javascript
const EMPTY = { isEmpty: () => true }; const isEmpty = (node) => node === EMPTY; const Pair = (car, cdr = EMPTY) => Object.assign({ car, cdr, isEmpty: () => false , [Symbol.iterator]: function () { let currentPair = this ; return { next: () => { if (currentPair.isEmpty()) { return {done: true } } else { const value = currentPair.car; currentPair = currentPair.cdr; return {done: false , value} } } } } }, EagerCollection(Pair)); Pair.from = (iterable) => ( function iterationToList (iteration) { const {done, value} = iteration.next(); return done ? EMPTY : Pair(value, iterationToList(iteration)); })(iterable[Symbol.iterator]()); Pair.from([1, 2, 3, 4, 5]).map(x => x * 2) //=>
```

### `technical-atom-5a4607f472992078` code

Citation: (raw/javascriptallonge.pdf p.256-260)

```
{"car": 2, "cdr": {"car": 4, "cdr": {"car": 6, "cdr": {"car": 8, "cdr": {"car": 10, "cdr": {} } } } } }
```

### `technical-atom-abd3ac01fe75ed23` requirement

Citation: (raw/javascriptallonge.pdf p.246)

That's a sign that we should work at a higher level of abstraction, and working with iterables is that higher level of abstraction.

### `technical-atom-d0ae077ae5d77a24` requirement

Citation: (raw/javascriptallonge.pdf p.246)

This 'fat object' style springs from a misunderstanding: When we say a collection should know how to perform a map over itself, we don't need for the collection to handle every single detail.

### `technical-atom-e475d2ad170b8179` exception

Citation: (raw/javascriptallonge.pdf p.246)

Some methods are only added to a few collections, some are added to all.

## Related technical details

### From [[javascriptallonge-lazy-collection-operations]]: `technical-atom-73ed00db8219d949` code

Relation: nearby source page; matched terms `collection`, `filter`, `lazy`, `map`, `pair`, `reduce`

Citation: (raw/javascriptallonge.pdf p.253-256)

```javascript
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10] .map((x) => x * x) .filter((x) => x % 2 == 0) .reduce((seed, element) => seed + element, 0) Pair.from([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) .map((x) => x * x) .filter((x) => x % 2 == 0) .reduce((seed, element) => seed + element, 0)
```

### From [[javascriptallonge-implementing-methods-with-iteration]]: `technical-atom-0432dbb698bbba10` code

Relation: nearby source page; matched terms `filter`, `map`, `methods`, `pair`, `reduce`

Citation: (raw/javascriptallonge.pdf p.246-253)

```javascript
// Pair and Stack in action Stack.from([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) .map((x) => x * x) .filter((x) => x % 2 == 0) .first() //=> 100 Pair.from([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) .map((x) => x * x) .filter((x) => x % 2 == 0) .reduce((seed, element) => seed + element, 0)
```

### From [[javascriptallonge-lazy-collection-operations]]: `technical-atom-f67fb88b9bd0b506` code

Relation: nearby source page; matched terms `collection`, `filter`, `lazy`, `map`

Citation: (raw/javascriptallonge.pdf p.253-256)

```javascript
Stack.from([ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]) .map((x) => x * x) .filter((x) => x % 2 == 0) .first()
```

### From [[javascriptallonge-lazy-collection-operations]]: `technical-atom-94dd91d8f0291f4d` code

Relation: nearby source page; matched terms `collection`, `filter`, `lazy`, `map`

Citation: (raw/javascriptallonge.pdf p.253-256)

```javascript
const Numbers = Object.assign({ [Symbol.iterator]: () => { let n = 0; return { next: () => ({done: false , value: n++}) } } }, LazyCollection); const firstCubeOver1234 = Numbers .map((x) => x * x * x) .filter((x) => x > 1234) .first() //=> 1331
```
