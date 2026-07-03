---
page_id: javascriptallonge-recipe-eager-collections
page_kind: recipe
page_family: recipe-pattern
summary: eager collections: reusable source-backed pattern with 4 statement(s) and 5 technical atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: eager-collections
projection_coverage: recipe-javascriptallonge-recipe-eager-collections@509a89be43d7ff2fbdc8a61bf92e3a87
---

# eager collections

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-we-ll-keep-it-simple-lazy-and-eager-collections-eager-collections-3cb2ca80]].
- Evidence roles: decision, constraint, explanation, example.

## Applicability And Rationale

- We can make an eager collection out of any collection that is gatherable , meaning it has a .from method: _(javascriptallonge.pdf (source-range-7239e085-01802))_
- We mix EagerCollection(Pair) into it, and this gives it all of our collection methods, which each method returning a new list of pairs: _(javascriptallonge.pdf (source-range-7239e085-01806))_
- Pair is gatherable, because it implements .from() . _(javascriptallonge.pdf (source-range-7239e085-01806))_
- Here is our Pair implementation. _(javascriptallonge.pdf (source-range-7239e085-01806))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01803)_

```
const extend = function (consumer, ...providers) {
for (let i = 0; i < providers.length; ++i) {
const provider = providers[i];
for (let key in provider) {
if (provider.hasOwnProperty(key)) {
consumer[key] = provider[key]
}
}
}
return consumer
};
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01804)_

```
const EagerCollection = (gatherable) =>
({
map(fn) {
const
original = this;
return gatherable.from(
(function* () {
for (let element of original) {
yield fn(element);
}
})()
);
},
reduce(fn, seed) {
let accumulator = seed;
for(let element of this) {
accumulator = fn(accumulator, element);
}
return accumulator;
},
filter(fn) {
const original = this;
return gatherable.from(
(function* () {
for (let element of original) {
if (fn(element)) yield element;
}
})()
);
},
find(fn) {
for (let element of this) {
if (fn(element)) return element;
}
},
until(fn) {
```

### Atom 3: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01805)_

```
const original = this;
return gatherable.from(
(function* () {
for (let element of original) {
if (fn(element)) break;
yield element;
}
})()
);
},
first() {
return this[Symbol.iterator]().next().value;
},
rest() {
const iteration = this[Symbol.iterator]();
iteration.next();
return gatherable.from(
(function* () {
yield * iteration;
})()
);
return gatherable.from(iterable);
},
take(numberToTake) {
const original = this;
let numberRemaining = numberToTake;
return gatherable.from(
(function* () {
for (let element of original) {
if (numberRemaining-- <= 0) break;
yield element;
}
})()
);
}
});
```

### Atom 4: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01807)_

```
const EMPTY = {
isEmpty: () => true
};
const isEmpty = (node) => node === EMPTY;
const Pair = (car, cdr = EMPTY) =>
Object.assign({
car,
cdr,
isEmpty: () => false,
[Symbol.iterator]: function () {
let currentPair = this;
return {
next: () => {
if (currentPair.isEmpty()) {
return {done: true}
}
else {
const value = currentPair.car;
currentPair = currentPair.cdr;
return {done: false, value}
}
}
}
}
}, EagerCollection(Pair));
Pair.from = (iterable) =>
(function iterationToList (iteration) {
const {done, value} = iteration.next();
return done ? EMPTY : Pair(value, iterationToList(iteration));
})(iterable[Symbol.iterator]());
Pair.from([1, 2, 3, 4, 5]).map(x => x * 2)
//=>
```

### Atom 5: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01808)_

```
{"car": 2,
"cdr": {"car": 4,
"cdr": {"car": 6,
"cdr": {"car": 8,
"cdr": {"car": 10,
"cdr": {}
}
}
}
}
}
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-we-ll-keep-it-simple-lazy-and-eager-collections-eager-collections-3cb2ca80]]
