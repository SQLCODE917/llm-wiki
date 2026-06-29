---
page_id: javascriptallonge-eager-collection
page_kind: concept
summary: Eager Collection: 2 statement(s) and 5 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-29
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-eager-collection@ef58f08453398118577c5039a3487adb
---

# Eager Collection

What [[javascriptallonge]] covers about eager collection:

## Statements

### We'll keep it simple: / Lazy and Eager Collections / eager collections

- An eager collection, like an array, returns a collection of its own type from each of the methods. We can make an eager collection out of any collection that is gatherable , meaning it has a .from method: _(javascriptallonge.pdf (source-range-7239e085-01802))_

- Here is our Pair implementation. Pair is gatherable, because it implements .from() . We mix EagerCollection(Pair) into it, and this gives it all of our collection methods, which each method returning a new list of pairs: _(javascriptallonge.pdf (source-range-7239e085-01806))_


## Technical atoms

### Technical frame 1: We'll keep it simple: / Lazy and Eager Collections / eager collections

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01806))_

> Here is our Pair implementation. Pair is gatherable, because it implements .from() . We mix EagerCollection(Pair) into it, and this gives it all of our collection methods, which each method returning a new list of pairs:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01803))_

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

### Technical frame 2: We'll keep it simple: / Lazy and Eager Collections / eager collections

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01806))_

> Here is our Pair implementation. Pair is gatherable, because it implements .from() . We mix EagerCollection(Pair) into it, and this gives it all of our collection methods, which each method returning a new list of pairs:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01804))_

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

### Technical frame 3: We'll keep it simple: / Lazy and Eager Collections / eager collections

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01806))_

> Here is our Pair implementation. Pair is gatherable, because it implements .from() . We mix EagerCollection(Pair) into it, and this gives it all of our collection methods, which each method returning a new list of pairs:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01805))_

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

### Technical frame 4: We'll keep it simple: / Lazy and Eager Collections / eager collections

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01806))_

> Here is our Pair implementation. Pair is gatherable, because it implements .from() . We mix EagerCollection(Pair) into it, and this gives it all of our collection methods, which each method returning a new list of pairs:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01807))_

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

### Technical frame 5: We'll keep it simple: / Lazy and Eager Collections / eager collections

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01806))_

> Here is our Pair implementation. Pair is gatherable, because it implements .from() . We mix EagerCollection(Pair) into it, and this gives it all of our collection methods, which each method returning a new list of pairs:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01808))_

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


## Related pages

- [[javascriptallonge-collection]] - broader topic: Collection shares technical record from We'll keep it simple: / Lazy and Eager Collections / eager collections: const extend = function (consumer, ...providers) { for (let i = 0; i < providers.length; ++i) { const provider = providers[i]; for (let key in provider) { if (provid ... [truncated] (5 shared atom(s))
- [[javascriptallonge-pair]] - shared statements and technical atoms: Pair shares source evidence from We'll keep it simple: / Lazy and Eager Collections / eager collections: Here is our Pair implementation. Pair is gatherable, because it implements .from() . We mix EagerCollection(Pair) into it, and this gives it all of our collection me ... [truncated]; Pair shares technical record from We'll keep it simple: / Lazy and Eager Collections / eager collections: const EagerCollection = (gatherable) => ({ map(fn) { const original = this; return gatherable.from( (function* () { for (let element of original) { yield fn(element) ... [truncated] (1 shared statement(s), 4 shared atom(s))
- [[javascriptallonge-method]] - shared technical atoms: Method shares technical record from We'll keep it simple: / Lazy and Eager Collections / eager collections: const extend = function (consumer, ...providers) { for (let i = 0; i < providers.length; ++i) { const provider = providers[i]; for (let key in provider) { if (provid ... [truncated] (5 shared atom(s))
- [[javascriptallonge-section-we-ll-keep-it-simple-lazy-and-eager-collections-eager-collections-3cb2ca80]] - source section: We'll keep it simple: / Lazy and Eager Collections / eager collections shares source evidence from We'll keep it simple: / Lazy and Eager Collections / eager collections: An eager collection, like an array, returns a collection of its own type from each of the methods. We can make an eager collection out of any collection that is gath ... [truncated]; We'll keep it simple: / Lazy and Eager Collections / eager collections shares technical record from We'll keep it simple: / Lazy and Eager Collections / eager collections: const extend = function (consumer, ...providers) { for (let i = 0; i < providers.length; ++i) { const provider = providers[i]; for (let key in provider) { if (provid ... [truncated] (4 shared statement(s), 5 shared atom(s))

## Source

- [[javascriptallonge]]
