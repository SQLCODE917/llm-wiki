---
page_id: javascriptallonge-section-from-3f6d6c43
page_kind: source
summary: from: 10 source-backed entries and 3 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-from-3f6d6c43@84da4145fc1635e30de9744893aec130
---

# from

From [[javascriptallonge]].

## Statements

- Having iterated over a collection, are we limited to for..do and/or gathering the elements in an array literal and/or gathering the elements into the parameters of a function? No, of course not, we can do anything we like with them. _(javascriptallonge.pdf (source-range-8eb13d6b-01610))_
- One useful thing is to write a .from function that gathers an iterable into a particular collection type. JavaScript's built-in Array class already has one: _(javascriptallonge.pdf (source-range-8eb13d6b-01611))_
- We can do the same with our own collections. As you recall, functions are mutable objects. And we can assign properties to functions with a . or even [ and ] . And if we assign a function to a property, we've created a method. _(javascriptallonge.pdf (source-range-8eb13d6b-01613))_
- Nowwecan go 'end to end,' If we want to map a linked list of numbers to a linked list of the squares of some numbers, we can do that: _(javascriptallonge.pdf (source-range-8eb13d6b-01616))_

## Technical atoms

### Technical frame 1: from

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01613))_

> We can do the same with our own collections. As you recall, functions are mutable objects. And we can assign properties to functions with a . or even [ and ] . And if we assign a function to a property, we've created a method.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01612))_

```
Array.from(UpTo1000) //=> [1,81,121,361,441,841,961]
```

### Technical frame 2: from

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01616))_

> Nowwecan go 'end to end,' If we want to map a linked list of numbers to a linked list of the squares of some numbers, we can do that:

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01615))_

```
Stack3.from = function (iterable) { const stack = this (); for ( let element of iterable) { stack.push(element); } return stack; } Pair1.from = (iterable) => ( function iterationToList (iteration) { const {done, value} = iteration.next(); return done ? EMPTY : Pair1(value, iterationToList(iteration)); })(iterable[Symbol.iterator]())
```

### Technical frame 3: from

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01616))_

> Nowwecan go 'end to end,' If we want to map a linked list of numbers to a linked list of the squares of some numbers, we can do that:

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01617))_

```
const numberList = Pair1.from(untilWith((x) => x > 10, Numbers)); Pair1.from(Squares) //=> {"first":0, "rest":{"first":1, "rest":{"first":4, "rest":{ ...
```
