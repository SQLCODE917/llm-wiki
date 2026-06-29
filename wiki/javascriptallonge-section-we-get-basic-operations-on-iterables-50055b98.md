---
page_id: javascriptallonge-section-we-get-basic-operations-on-iterables-50055b98
page_kind: source
summary: We get: / Basic Operations on Iterables: 7 source-backed entries and 6 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-29
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-we-get-basic-operations-on-iterables-50055b98@f65814db35f86824970692847b9c72ea
---

# We get: / Basic Operations on Iterables

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-we-get-2605e005]] - broader source section: We get:
- [[javascriptallonge-section-we-get-basic-operations-on-iterables-operations-that-transform-one-iterable-into-another-51605abc]] - narrower source section: We get: / Basic Operations on Iterables / operations that transform one iterable into another
- [[javascriptallonge-section-we-get-basic-operations-on-iterables-operations-that-compose-two-or-more-iterables-into-an-itera-31eb9626]] - narrower source section: We get: / Basic Operations on Iterables / operations that compose two or more iterables into an iterable
- [[javascriptallonge-section-we-get-basic-operations-on-iterables-operations-that-transform-an-iterable-into-a-value-7603882e]] - narrower source section: We get: / Basic Operations on Iterables / operations that transform an iterable into a value
- [[javascriptallonge-section-we-get-basic-operations-on-iterables-memoizing-an-iterable-b731679a]] - narrower source section: We get: / Basic Operations on Iterables / memoizing an iterable

## Statements

- Here are the operations we've defined on Iterables. As discussed, they preserve the collection semantics of the iterable they are given: _(javascriptallonge.pdf (source-range-7239e085-01948))_

## Technical atoms

### Technical frame 1: We get: / Basic Operations on Iterables / operations that transform one iterable into another

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

### Technical frame 2: We get: / Basic Operations on Iterables / operations that transform one iterable into another

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

### Technical frame 3: We get: / Basic Operations on Iterables / operations that compose two or more iterables into an iterable

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

### Technical frame 4: We get: / Basic Operations on Iterables / operations that compose two or more iterables into an iterable

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01955))_

```
const zip = callFirst(zipWith, (...values) => values);
```

### Technical frame 5: We get: / Basic Operations on Iterables / operations that transform an iterable into a value

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

### Technical frame 6: We get: / Basic Operations on Iterables / memoizing an iterable

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
