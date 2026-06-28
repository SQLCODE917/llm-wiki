---
page_id: javascriptallonge-section-eager-collections-04ca2770
page_kind: source
summary: eager collections: 10 source-backed entries and 5 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-eager-collections-04ca2770@7ec8de4955d5be2c23576fad3b4f0100
---

# eager collections

From [[javascriptallonge]].

## Statements

- An eager collection, like an array, returns a collection of its own type from each of the methods. We can make an eager collection out of any collection that is gatherable , meaning it has a .from method: _(javascriptallonge.pdf (source-range-31a4cf47-01803))_
- Here is our Pair implementation. Pair is gatherable, because it implements .from() . We mix EagerCollection(Pair) into it, and this gives it all of our collection methods, which each method returning a new list of pairs: _(javascriptallonge.pdf (source-range-31a4cf47-01807))_
- Pair is gatherable, because it implements .from() . _(javascriptallonge.pdf (source-range-31a4cf47-01807))_

## Technical atoms

### Technical frame 1: eager collections

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01807))_

> Here is our Pair implementation. Pair is gatherable, because it implements .from() . We mix EagerCollection(Pair) into it, and this gives it all of our collection methods, which each method returning a new list of pairs:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01804))_

```
const extend = function (consumer, ...providers) { for ( let i = 0; i < providers.length; ++i) { const provider = providers[i]; for ( let key in provider) { if (provider.hasOwnProperty(key)) { consumer[key] = provider[key] } } } return consumer };
```

### Technical frame 2: eager collections

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01807))_

> Here is our Pair implementation. Pair is gatherable, because it implements .from() . We mix EagerCollection(Pair) into it, and this gives it all of our collection methods, which each method returning a new list of pairs:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01805))_

```
const EagerCollection = (gatherable) => ({ map(fn) { const original = this ; return gatherable.from( ( function * () { for ( let element of original) { yield fn(element); } })() ); }, reduce(fn, seed) { let accumulator = seed; for ( let element of this ) { accumulator = fn(accumulator, element); } return accumulator; }, filter(fn) { const original = this ; return gatherable.from( ( function * () { for ( let element of original) { if (fn(element)) yield element; } })() ); }, find(fn) { for ( let element of this ) { if (fn(element)) return element; } }, until(fn) {
```

### Technical frame 3: eager collections

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01807))_

> Here is our Pair implementation. Pair is gatherable, because it implements .from() . We mix EagerCollection(Pair) into it, and this gives it all of our collection methods, which each method returning a new list of pairs:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01806))_

```
const original = this ; return gatherable.from( ( function * () { for ( let element of original) { if (fn(element)) break ; yield element; } })() ); }, first() { return this [Symbol.iterator]().next().value; }, rest() { const iteration = this [Symbol.iterator](); iteration.next(); return gatherable.from( ( function * () { yield * iteration; })() ); return gatherable.from(iterable); }, take(numberToTake) { const original = this ; let numberRemaining = numberToTake; return gatherable.from( ( function * () { for ( let element of original) { if (numberRemaining-- <= 0) break ; yield element; } })() ); } });
```

### Technical frame 4: eager collections

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01807))_

> Here is our Pair implementation. Pair is gatherable, because it implements .from() . We mix EagerCollection(Pair) into it, and this gives it all of our collection methods, which each method returning a new list of pairs:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01808))_

```
const EMPTY = { isEmpty: () => true }; const isEmpty = (node) => node === EMPTY; const Pair = (car, cdr = EMPTY) => Object.assign({ car, cdr, isEmpty: () => false , [Symbol.iterator]: function () { let currentPair = this ; return { next: () => { if (currentPair.isEmpty()) { return {done: true } } else { const value = currentPair.car; currentPair = currentPair.cdr; return {done: false , value} } } } } }, EagerCollection(Pair)); Pair.from = (iterable) => ( function iterationToList (iteration) { const {done, value} = iteration.next(); return done ? EMPTY : Pair(value, iterationToList(iteration)); })(iterable[Symbol.iterator]()); Pair.from([1, 2, 3, 4, 5]).map(x => x * 2) //=>
```

### Technical frame 5: eager collections

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01807))_

> Here is our Pair implementation. Pair is gatherable, because it implements .from() . We mix EagerCollection(Pair) into it, and this gives it all of our collection methods, which each method returning a new list of pairs:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01809))_

```
{"car": 2, "cdr": {"car": 4, "cdr": {"car": 6, "cdr": {"car": 8, "cdr": {"car": 10, "cdr": {} } } } } }
```
