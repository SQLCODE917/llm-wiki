---
page_id: javascriptallonge-section-like-this-operations-on-ordered-collections-286a5f1c
page_kind: source
summary: Like this: / operations on ordered collections: 28 source-backed entries and 9 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-29
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-like-this-operations-on-ordered-collections-286a5f1c@1b0a146d0e522486faf9284fa909a9b9
---

# Like this: / operations on ordered collections

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-like-this-66cb3108]] - broader source section: Like this:

## Statements

- Let's define some operations on ordered collections. Here's mapWith , it takes an ordered collection, and returns another ordered collection representing a mapping over the original: 89 _(javascriptallonge.pdf (source-range-7239e085-01587))_
- 89 Yes, we also used the name mapWith for working with ordinary collections elsewhere. If we were writing a library of functions, we would have to disambiguate the two kinds of mapping functions with special names, namespaces, or modules. But for the purposes of discussing ideas, we can use the same name twice in two different contexts. It's the same idea, after all. _(javascriptallonge.pdf (source-range-7239e085-01588))_
- This illustrates the general pattern of working with ordered collections: We make them iterables , meaning that they have a [Symbol.iterator] method, that returns an iterator . An iterator is also an object, but with a .next() method that is invoked repeatedly to obtain the elements in order. _(javascriptallonge.pdf (source-range-7239e085-01590))_
- Many operations on ordered collections return another ordered collection. They do so by taking care to iterate over a result freshly every time we get an iterator for them. Consider this example for mapWith : _(javascriptallonge.pdf (source-range-7239e085-01591))_
- Numbers is an ordered collection. We invoke mapWith((x) => 2 * x, Numbers) and get Evens . Evens works just as if we'd written this: _(javascriptallonge.pdf (source-range-7239e085-01593))_
- So, Evens is also an ordered collection, because it starts at the beginning each time we get a fresh iterator over it. Thus, mapWith has the property of preserving the collection semantics of the iterable we give it. So we call it a collection operation . _(javascriptallonge.pdf (source-range-7239e085-01596))_
- Like mapWith , they preserve the ordered collection semantics of whatever you give them. _(javascriptallonge.pdf (source-range-7239e085-01603))_
- Andhere's a computation performed using operations on ordered collections: We'll create an ordered collection of square numbers that end in one and are less than 1,000: _(javascriptallonge.pdf (source-range-7239e085-01604))_
- As we expect from an ordered collection, each time we iterate over UpTo1000 , we begin at the beginning. _(javascriptallonge.pdf (source-range-7239e085-01606))_
- For completeness, here are two more handy iterable functions. first returns the first element of an iterable (if it has one), and rest returns an iterable that iterates over all but the first element of an iterable. They are equivalent to destructuring arrays with [first, ...rest] : _(javascriptallonge.pdf (source-range-7239e085-01607))_
- like our other operations, rest preserves the ordered collection semantics of its argument. _(javascriptallonge.pdf (source-range-7239e085-01609))_
- So, Evens is also an ordered collection, because it starts at the beginning each time we get a fresh iterator over it. _(javascriptallonge.pdf (source-range-7239e085-01596))_
- Thus, mapWith has the property of preserving the collection semantics of the iterable we give it. _(javascriptallonge.pdf (source-range-7239e085-01596))_

## Technical atoms

### Technical frame 1: Like this: / operations on ordered collections

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

### Technical frame 2: Like this: / operations on ordered collections

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

### Technical frame 3: Like this: / operations on ordered collections

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01596))_

> So, Evens is also an ordered collection, because it starts at the beginning each time we get a fresh iterator over it. Thus, mapWith has the property of preserving the collection semantics of the iterable we give it. So we call it a collection operation .

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01594))_

```
const Evens =
{
[Symbol.iterator] () {
const iterator = Numbers[Symbol.iterator]();
return {
next () {
const {done, value} = iterator.next();
return ({done, value: done ? undefined : 2 *value});
}
}
}
};
```

### Technical frame 4: Like this: / operations on ordered collections

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01603))_

> Like mapWith , they preserve the ordered collection semantics of whatever you give them.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01598))_

```
const ZeroesToNines = mapWith((n) => Math.floor(10 * limit), RandomNumbers);
for (const i of ZeroesToNines) {
console.log(i)
}
//=>
5
1
9
...
for (const i of ZeroesToNines) {
console.log(i)
}
//=>
3
```

### Technical frame 5: Like this: / operations on ordered collections

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01603))_

> Like mapWith , they preserve the ordered collection semantics of whatever you give them.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01599))_

```
6
1
...
```

### Technical frame 6: Like this: / operations on ordered collections

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01603))_

> Like mapWith , they preserve the ordered collection semantics of whatever you give them.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01600))_

> mapWith can get a new iterator from RandomNumbers each time we iterate over ZeroesToNines , but if RandomNumbers doesn't behave like an ordered collection, that's not mapWith 's fault.

### Technical frame 7: Like this: / operations on ordered collections

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

### Technical frame 8: Like this: / operations on ordered collections

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

### Technical frame 9: Like this: / operations on ordered collections

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01609))_

> like our other operations, rest preserves the ordered collection semantics of its argument.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01608))_

```
const first = (iterable) =>
iterable[Symbol.iterator]().next().value;
const rest = (iterable) =>
({
[Symbol.iterator] () {
const iterator = iterable[Symbol.iterator]();
iterator.next();
return iterator;
}
});
```
