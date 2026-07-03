---
page_id: javascriptallonge-recipe-from
page_kind: recipe
page_family: recipe-pattern
summary: from: reusable source-backed pattern with 7 statement(s) and 3 technical atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: from
projection_coverage: recipe-javascriptallonge-recipe-from@203bcaacc2f35d9bcfeb290251a3ea98
---

# from

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-like-this-from-28c3e8e3]].
- Evidence roles: decision, constraint, example.

## Applicability And Rationale

- No, of course not, we can do anything we like with them. _(javascriptallonge.pdf (source-range-7239e085-01611))_
- One useful thing is to write a .from function that gathers an iterable into a particular collection type. _(javascriptallonge.pdf (source-range-7239e085-01612))_
- We can do the same with our own collections. _(javascriptallonge.pdf (source-range-7239e085-01614))_
- As you recall, functions are mutable objects. _(javascriptallonge.pdf (source-range-7239e085-01614))_
- And we can assign properties to functions with a . _(javascriptallonge.pdf (source-range-7239e085-01614))_
- And if we assign a function to a property, we've created a method. _(javascriptallonge.pdf (source-range-7239e085-01614))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01613)_

```
Array.from(UpTo1000)
//=> [1,81,121,361,441,841,961]
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01616)_

```
Stack3.from = function (iterable) {
const stack = this();
for (let element of iterable) {
stack.push(element);
}
return stack;
}
Pair1.from = (iterable) =>
(function iterationToList (iteration) {
const {done, value} = iteration.next();
return done ? EMPTY : Pair1(value, iterationToList(iteration));
})(iterable[Symbol.iterator]())
```

### Atom 3: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01618)_

```
const numberList = Pair1.from(untilWith((x) => x > 10, Numbers));
Pair1.from(Squares)
//=> {"first":0,
"rest":{"first":1,
"rest":{"first":4,
"rest":{ ...
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-like-this-from-28c3e8e3]]
