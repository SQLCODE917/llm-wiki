---
page_id: javascriptallonge-recipe-rewriting-iterable-operations
page_kind: recipe
page_family: recipe-pattern
summary: rewriting iterable operations: reusable source-backed pattern with 4 statement(s) and 5 technical atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: rewriting-iterable-operations
projection_coverage: recipe-javascriptallonge-recipe-rewriting-iterable-operations@14dd62b90a2a489c95bdf0b4ffa4a624
---

# rewriting iterable operations

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-we-ll-keep-it-simple-rewriting-iterable-operations-9606b732]].
- Evidence roles: decision, constraint, procedure, example.

## Applicability And Rationale

- Now that we know about iterables, we can rewrite our iterable operations as generators. _(javascriptallonge.pdf (source-range-7239e085-01748))_
- No need to explicitly construct an object that has a [Symbol.iterator] method. _(javascriptallonge.pdf (source-range-7239e085-01752))_
- No need to return an object with a .next() method. _(javascriptallonge.pdf (source-range-7239e085-01752))_
- We can do the same thing with our other operations like filterWith and untilWith . _(javascriptallonge.pdf (source-range-7239e085-01753))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01749)_

```
const mapWith = (fn, iterable) =>
({
[Symbol.iterator]: () => {
const iterator = iterable[Symbol.iterator]();
return {
next: () => {
const {done, value} = iterator.next();
return ({done, value: done ? undefined : fn(value)});
}
}
}
});
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01751)_

```
function * mapWith (fn, iterable) {
for (const element of iterable) {
yield fn(element);
}
}
```

### Atom 3: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01754)_

```
function * mapWith(fn, iterable) {
for (const element of iterable) {
yield fn(element);
}
}
function * filterWith (fn, iterable) {
for (const element of iterable) {
if (!!fn(element)) yield element;
}
}
```

### Atom 4: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01755)_

```
function * untilWith (fn, iterable) {
for (const element of iterable) {
if (fn(element)) break;
yield fn(element);
}
}
```

### Atom 5: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01757)_

```
const first = (iterable) =>
iterable[Symbol.iterator]().next().value;
function * rest (iterable) {
const iterator = iterable[Symbol.iterator]();
iterator.next();
yield * iterator;
}
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-we-ll-keep-it-simple-rewriting-iterable-operations-9606b732]]
