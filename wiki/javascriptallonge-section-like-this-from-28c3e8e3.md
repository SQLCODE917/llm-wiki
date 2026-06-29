---
page_id: javascriptallonge-section-like-this-from-28c3e8e3
page_kind: source
summary: Like this: / from: 10 source-backed entries and 3 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-29
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-like-this-from-28c3e8e3@d520a5c57ffea134733e531f11961d99
---

# Like this: / from

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-like-this-66cb3108]] - broader source section: Like this:

## Statements

- Having iterated over a collection, are we limited to for..do and/or gathering the elements in an array literal and/or gathering the elements into the parameters of a function? No, of course not, we can do anything we like with them. _(javascriptallonge.pdf (source-range-7239e085-01611))_
- One useful thing is to write a .from function that gathers an iterable into a particular collection type. JavaScript's built-in Array class already has one: _(javascriptallonge.pdf (source-range-7239e085-01612))_
- We can do the same with our own collections. As you recall, functions are mutable objects. And we can assign properties to functions with a . or even [ and ] . And if we assign a function to a property, we've created a method. _(javascriptallonge.pdf (source-range-7239e085-01614))_
- Nowwecan go 'end to end,' If we want to map a linked list of numbers to a linked list of the squares of some numbers, we can do that: _(javascriptallonge.pdf (source-range-7239e085-01617))_

## Technical atoms

### Technical frame 1: Like this: / from

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01614))_

> We can do the same with our own collections. As you recall, functions are mutable objects. And we can assign properties to functions with a . or even [ and ] . And if we assign a function to a property, we've created a method.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01613))_

```
Array.from(UpTo1000)
//=> [1,81,121,361,441,841,961]
```

### Technical frame 2: Like this: / from

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01617))_

> Nowwecan go 'end to end,' If we want to map a linked list of numbers to a linked list of the squares of some numbers, we can do that:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01616))_

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

### Technical frame 3: Like this: / from

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01617))_

> Nowwecan go 'end to end,' If we want to map a linked list of numbers to a linked list of the squares of some numbers, we can do that:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01618))_

```
const numberList = Pair1.from(untilWith((x) => x > 10, Numbers));
Pair1.from(Squares)
//=> {"first":0,
"rest":{"first":1,
"rest":{"first":4,
"rest":{ ...
```
