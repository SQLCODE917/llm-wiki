---
page_id: javascriptallonge-eager-collection
page_kind: concept
page_family: topic-concept
summary: Eager Collection: 1 statement(s) and 3 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-eager-collection@e2203eb40e54ead05cc98acf76b14622
---

# Eager Collection

What [[javascriptallonge]] covers about eager collection:

## Statements

### We'll keep it simple: / Lazy and Eager Collections / eager collections

- An eager collection, like an array, returns a collection of its own type from each of the methods. We can make an eager collection out of any collection that is gatherable , meaning it has a .from method: _(javascriptallonge.pdf (source-range-7239e085-01802))_


## Technical atoms

### Technical frame 1: We'll keep it simple: / Lazy and Eager Collections / eager collections

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01806))_

> Here is our Pair implementation. Pair is gatherable, because it implements .from() . We mix EagerCollection(Pair) into it, and this gives it all of our collection methods, which each method returning a new list of pairs:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01803))_

<a id="atom-technical-atom-260d903a41c4e031"></a>

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

<a id="atom-technical-atom-a84a9a6634bcef5c"></a>

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

<a id="atom-technical-atom-42f03cd992a4e79f"></a>

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


## Related pages

### Source structure

- [[javascriptallonge-section-we-ll-keep-it-simple-lazy-and-eager-collections-eager-collections-3cb2ca80]] - source section: We'll keep it simple: / Lazy and Eager Collections / eager collections shares source evidence from We'll keep it simple: / Lazy and Eager Collections / eager collections: An eager collection, like an array, returns a collection of its own type from each of the methods. We can make an eager collection out of any collection that is gath ... [truncated]; We'll keep it simple: / Lazy and Eager Collections / eager collections shares technical record from We'll keep it simple: / Lazy and Eager Collections / eager collections: const extend = function (consumer, ...providers) { for (let i = 0; i < providers.length; ++i) { const provider = providers[i]; for (let key in provider) { if (provid ... [truncated] (4 shared statement(s), 5 shared atom(s))

### Shared technical atoms

- [[javascriptallonge-method]] - shared technical atoms: Method shares technical record from We'll keep it simple: / Lazy and Eager Collections / eager collections: const extend = function (consumer, ...providers) { for (let i = 0; i < providers.length; ++i) { const provider = providers[i]; for (let key in provider) { if (provid ... [truncated] (3 shared atom(s))
- [[javascriptallonge-pair]] - shared technical atoms: Pair shares technical record from We'll keep it simple: / Lazy and Eager Collections / eager collections: const EagerCollection = (gatherable) => ({ map(fn) { const original = this; return gatherable.from( (function* () { for (let element of original) { yield fn(element) ... [truncated] (2 shared atom(s))

### Topics

- [[javascriptallonge-collection]] - broader topic: Collection shares technical record from We'll keep it simple: / Lazy and Eager Collections / eager collections: const extend = function (consumer, ...providers) { for (let i = 0; i < providers.length; ++i) { const provider = providers[i]; for (let key in provider) { if (provid ... [truncated] (3 shared atom(s))

## Source

- [[javascriptallonge]]
