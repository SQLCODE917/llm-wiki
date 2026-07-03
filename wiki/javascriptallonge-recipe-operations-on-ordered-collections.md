---
page_id: javascriptallonge-recipe-operations-on-ordered-collections
page_kind: recipe
page_family: recipe-pattern
summary: operations on ordered collections: reusable source-backed pattern with 15 statement(s) and 8 technical atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: operations-on-ordered-collections
projection_coverage: recipe-javascriptallonge-recipe-operations-on-ordered-collections@0daaa4d2739d8c4b4d928f4b80a98a8e
---

# operations on ordered collections

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-like-this-operations-on-ordered-collections-286a5f1c]].
- Evidence roles: decision, constraint, procedure, explanation, example, structured-state.

## Applicability And Rationale

- Here's mapWith , it takes an ordered collection, and returns another ordered collection representing a mapping over the original: 89 _(javascriptallonge.pdf (source-range-7239e085-01587))_
- If we were writing a library of functions, we would have to disambiguate the two kinds of mapping functions with special names, namespaces, or modules. _(javascriptallonge.pdf (source-range-7239e085-01588))_
- But for the purposes of discussing ideas, we can use the same name twice in two different contexts. _(javascriptallonge.pdf (source-range-7239e085-01588))_
- 89 Yes, we also used the name mapWith for working with ordinary collections elsewhere. _(javascriptallonge.pdf (source-range-7239e085-01588))_
- An iterator is also an object, but with a .next() method that is invoked repeatedly to obtain the elements in order. _(javascriptallonge.pdf (source-range-7239e085-01590))_
- This illustrates the general pattern of working with ordered collections: We make them iterables , meaning that they have a [Symbol.iterator] method, that returns an iterator . _(javascriptallonge.pdf (source-range-7239e085-01590))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01589)_

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

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01592)_

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

### Atom 3: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01594)_

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

### Atom 4: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01598)_

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

### Atom 5: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01599)_

```
6
1
...
```

### Atom 6: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01602)_

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

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-like-this-operations-on-ordered-collections-286a5f1c]]
