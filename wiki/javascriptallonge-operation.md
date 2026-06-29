---
page_id: javascriptallonge-operation
page_kind: concept
summary: Operation: 4 statement(s) and 5 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-29
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-operation@352186bdd84904ed90fa8a78eab21892
---

# Operation

What [[javascriptallonge]] covers about operation:

## Statements

### Recipes with Basic Functions / Maybe

- If some code ever tries to call model.setSomething with nothing, the operation will be skipped. _(javascriptallonge.pdf (source-range-7239e085-00708))_

### Composing and Decomposing Data / Mutation / mutation and data structures

- The gathering operation [a, b, ...ThreeToFive] is slower, but 'safer. ' _(javascriptallonge.pdf (source-range-7239e085-01150))_

### Like this: / operations on ordered collections

- Many operations on ordered collections return another ordered collection. They do so by taking care to iterate over a result freshly every time we get an iterator for them. Consider this example for mapWith : _(javascriptallonge.pdf (source-range-7239e085-01591))_

- like our other operations, rest preserves the ordered collection semantics of its argument. _(javascriptallonge.pdf (source-range-7239e085-01609))_


## Technical atoms

### Technical frame 1: Yes. Consider this variation: / Functional Iterators / bonus

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01319))_

> This is interesting, because it is lazy: It doesn't apply fn to every element in an iteration, just enough to find the first that passes the test. Whereas if we wrote something like:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01318))_

```
const firstInIteration = (fn, iterator) =>
take(filterIteratorWith(fn, iterator), 1);
```

### Technical frame 2: Like this: / operations on ordered collections

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01590))_

> This illustrates the general pattern of working with ordered collections: We make them iterables , meaning that they have a [Symbol.iterator] method, that returns an iterator . An iterator is also an object, but with a .next() method that is invoked repeatedly to obtain the elements in order.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01589))_

```
const mapWith = (fn, collection) =>
({
[Symbol.iterator] () {
const iterator = collection[Symbol.iterator]();
return {
next () {
const {done, value} = iterator.next();
return ({done, value: done ? undefined : fn(value)});
}
}
}
});
```

### Technical frame 3: Like this: / operations on ordered collections

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01593))_

> Numbers is an ordered collection. We invoke mapWith((x) => 2 * x, Numbers) and get Evens . Evens works just as if we'd written this:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01592))_

```
const Evens = mapWith((x) => 2 * x, Numbers);
for (const i of Evens) {
console.log(i)
}
//=>
0
2
4
...
for (const i of Evens) {
console.log(i)
}
//=>
0
2
4
...
```

### Technical frame 4: Like this: / operations on ordered collections

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01603))_

> Like mapWith , they preserve the ordered collection semantics of whatever you give them.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01602))_

```
const filterWith = (fn, iterable) =>
({
[Symbol.iterator] () {
const iterator = iterable[Symbol.iterator]();
return {
next () {
do {
const {done, value} = iterator.next();
} while (!done && !fn(value));
return {done, value};
}
}
}
});
const untilWith = (fn, iterable) =>
({
[Symbol.iterator] () {
const iterator = iterable[Symbol.iterator]();
return {
next () {
let {done, value} = iterator.next();
done = done || fn(value);
return ({done, value: done ? undefined : value});
}
}
}
});
```

### Technical frame 5: Like this: / operations on ordered collections

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01606))_

> As we expect from an ordered collection, each time we iterate over UpTo1000 , we begin at the beginning.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01605))_

```
const Squares = mapWith((x) => x * x, Numbers);
const EndWithOne = filterWith((x) => x % 10 === 1, Squares);
const UpTo1000 = untilWith((x) => (x > 1000), EndWithOne);
[...UpTo1000]
//=>
[1,81,121,361,441,841,961]
[...UpTo1000]
//=>
[1,81,121,361,441,841,961]
```


## Related pages

- [[javascriptallonge-iterator]] - shared technical atoms: Iterator shares technical record from Like this: / operations on ordered collections: const mapWith = (fn, collection) => ({ [Symbol.iterator] () { const iterator = collection[Symbol.iterator](); return { next () { const {done, value} = iterator.next( ... [truncated] (2 shared atom(s))
- [[javascriptallonge-mapwith]] - shared technical atoms: Mapwith shares technical record from Like this: / operations on ordered collections: const mapWith = (fn, collection) => ({ [Symbol.iterator] () { const iterator = collection[Symbol.iterator](); return { next () { const {done, value} = iterator.next( ... [truncated] (2 shared atom(s))
- [[javascriptallonge-return]] - shared technical atoms: Return shares technical record from Like this: / operations on ordered collections: const mapWith = (fn, collection) => ({ [Symbol.iterator] () { const iterator = collection[Symbol.iterator](); return { next () { const {done, value} = iterator.next( ... [truncated] (2 shared atom(s))
- [[javascriptallonge-discussing]] - shared technical atoms: Discussing shares technical record from Like this: / operations on ordered collections: const mapWith = (fn, collection) => ({ [Symbol.iterator] () { const iterator = collection[Symbol.iterator](); return { next () { const {done, value} = iterator.next( ... [truncated] (1 shared atom(s))
- [[javascriptallonge-functional-iterator]] - shared technical atoms: Functional Iterators shares technical record from Yes. Consider this variation: / Functional Iterators / bonus: const firstInIteration = (fn, iterator) => take(filterIteratorWith(fn, iterator), 1); (1 shared atom(s))
- [[javascriptallonge-idea]] - shared technical atoms: Idea shares technical record from Like this: / operations on ordered collections: const mapWith = (fn, collection) => ({ [Symbol.iterator] () { const iterator = collection[Symbol.iterator](); return { next () { const {done, value} = iterator.next( ... [truncated] (1 shared atom(s))
- [[javascriptallonge-javascript]] - shared technical atoms: Javascript shares technical record from Yes. Consider this variation: / Functional Iterators / bonus: const firstInIteration = (fn, iterator) => take(filterIteratorWith(fn, iterator), 1); (1 shared atom(s))
- [[javascriptallonge-language]] - shared technical atoms: Language shares technical record from Yes. Consider this variation: / Functional Iterators / bonus: const firstInIteration = (fn, iterator) => take(filterIteratorWith(fn, iterator), 1); (1 shared atom(s))
- [[javascriptallonge-program]] - shared technical atoms: Program shares technical record from Yes. Consider this variation: / Functional Iterators / bonus: const firstInIteration = (fn, iterator) => take(filterIteratorWith(fn, iterator), 1); (1 shared atom(s))
- [[javascriptallonge-programmer]] - shared technical atoms: Programmer shares technical record from Yes. Consider this variation: / Functional Iterators / bonus: const firstInIteration = (fn, iterator) => take(filterIteratorWith(fn, iterator), 1); (1 shared atom(s))
- [[javascriptallonge-purpose]] - shared technical atoms: Purpose shares technical record from Like this: / operations on ordered collections: const mapWith = (fn, collection) => ({ [Symbol.iterator] () { const iterator = collection[Symbol.iterator](); return { next () { const {done, value} = iterator.next( ... [truncated] (1 shared atom(s))
- [[javascriptallonge-code]] - shared statements: Code shares source evidence from Recipes with Basic Functions / Maybe: If some code ever tries to call model.setSomething with nothing, the operation will be skipped. (1 shared statement(s))
- [[javascriptallonge-gathering]] - shared statements: Gathering shares source evidence from Composing and Decomposing Data / Mutation / mutation and data structures: The gathering operation [a, b, ...ThreeToFive] is slower, but 'safer. ' (1 shared statement(s))
- [[javascriptallonge-rest]] - shared statements: Rest shares source evidence from Like this: / operations on ordered collections: like our other operations, rest preserves the ordered collection semantics of its argument. (1 shared statement(s))

## Source

- [[javascriptallonge]]
