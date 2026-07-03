---
page_id: javascriptallonge-recipe-iterating
page_kind: recipe
page_family: recipe-pattern
summary: iterating: reusable source-backed pattern with 9 statement(s) and 6 technical atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: iterating
projection_coverage: recipe-javascriptallonge-recipe-iterating@929e9a6d487370fd327be3920300f7ec
---

# iterating

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-yes-consider-this-variation-functional-iterators-iterating-c8ddd51e]].
- Evidence roles: decision, constraint, explanation, example.

## Applicability And Rationale

- Nevertheless, there is some value in being able to express some algorithms as iteration. _(javascriptallonge.pdf (source-range-7239e085-01285))_
- Folding is a universal operation, and with care we can accomplish any task with folds that could be accomplished with that stalwart of structured programming, the for loop. _(javascriptallonge.pdf (source-range-7239e085-01285))_
- JavaScript has a particularly low-level version of for loop that mimics the semantics of the C language. _(javascriptallonge.pdf (source-range-7239e085-01286))_
- And worst of all, we're getting really low-level with details like knowing that the elements of an array are indexed with consecutive integers that begin with 0 . _(javascriptallonge.pdf (source-range-7239e085-01288))_
- We can put those into a POJO (a Plain Old JavaScript Object). _(javascriptallonge.pdf (source-range-7239e085-01291))_
- Notice that buried inside our loop, we have bound the names done and value . _(javascriptallonge.pdf (source-range-7239e085-01291))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01287)_

```
const arraySum = (array) => {
let sum = 0;
for (let i = 0; i < array.length; ++i) {
sum += array[i];
}
return sum
}
arraySum([1, 4, 9, 16, 25])
//=> 55
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01290)_

```
const arraySum = (array) => {
let done,
sum = 0,
i = 0;
while ((done = i == array.length, !done)) {
const value = array[i++];
sum += value;
}
return sum
}
arraySum([1, 4, 9, 16, 25])
//=> 55
```

### Atom 3: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01292)_

```
const arraySum = (array) => {
let iter,
sum = 0,
index = 0;
while (
(eachIteration = {
done: index === array.length,
value: index < array.length ? array[index] : undefined
},
++index,
!eachIteration.done)
) {
sum += eachIteration.value;
}
return sum;
}
arraySum([1, 4, 9, 16, 25])
//=> 55
With this code, we make a POJO that has done and value keys. All the summing code needs to know
is to add eachIteration.value. Now we can extract the ickiness into a separate function:
const arrayIterator = (array) => {
let i = 0;
return () => {
const done = i === array.length;
return {
done,
value: done ? undefined : array[i++]
}
}
}
const iteratorSum = (iterator) => {
let eachIteration,
sum = 0;
while ((eachIteration = iterator(), !eachIteration.done)) {
```

### Atom 4: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01293)_

```
sum += eachIteration.value;
}
return sum;
}
iteratorSum(arrayIterator([1, 4, 9, 16, 25]))
//=> 55
```

### Atom 5: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01296)_

```
const EMPTY = null;
const isEmpty = (node) => node === EMPTY;
const pair = (first, rest = EMPTY) => ({first, rest});
const list = (...elements) => {
const [first, ...rest] = elements;
return elements.length === 0
? EMPTY
: pair(first, list(...rest))
}
const print = (aPair) =>
isEmpty(aPair)
? ""
: `${aPair.first} ${print(aPair.rest)}`
const listIterator = (aPair) =>
() => {
const done = isEmpty(aPair);
if (done) {
return {done};
}
else {
const {first, rest} = aPair;
aPair = aPair.rest;
```

### Atom 6: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01297)_

```
return { done, value: first }
}
}
const iteratorSum = (iterator) => {
let eachIteration,
sum = 0;;
while ((eachIteration = iterator(), !eachIteration.done)) {
sum += eachIteration.value;
}
return sum
}
const aListIterator = listIterator(list(1, 4, 9, 16, 25));
iteratorSum(aListIterator)
//=> 55
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-yes-consider-this-variation-functional-iterators-iterating-c8ddd51e]]
