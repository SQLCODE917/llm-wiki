---
page_id: javascriptallonge-section-values-are-expressions-iteration-and-iterables-from-1535a852
page_kind: source
summary: values are expressions / Iteration and Iterables / from: 7 source-backed entries and 1 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-values-are-expressions-iteration-and-iterables-from-1535a852@e933716c203fd734474bb98d3deaf105
---

# values are expressions / Iteration and Iterables / from

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-values-are-expressions-iteration-and-iterables-70b2511b]] - broader source section

## Statements

- No, of course not, we can do anything we like with them. _(javascriptallonge.pdf (source-range-83ecb080-01614))_
- One useful thing is to write a .from function that gathers an iterable into a particular collection type. _(javascriptallonge.pdf (source-range-83ecb080-01617))_
- And we can assign properties to functions with a . _(javascriptallonge.pdf (source-range-83ecb080-01618))_
- And if we assign a function to a property, we’ve created a method. _(javascriptallonge.pdf (source-range-83ecb080-01618))_
- As you recall, functions are mutable objects. _(javascriptallonge.pdf (source-range-83ecb080-01618))_
- Array.from(UpTo1000) _//=> [1,81,121,361,441,841,961]_ We can do the same with our own collections. _(javascriptallonge.pdf (source-range-83ecb080-01618))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01620))_

> Stack3.from = **function** (iterable) { **const** stack = **this** (); **for** ( **let** element **of** iterable) { stack.push(element); } **return** stack; } Pair1.from = (iterable) => ( **function** iterationToList (iteration) { **const** {done, value} = iteration.next(); **return** done ? EMPTY : Pair1(value, iterationToList(iteration)); })(iterable[Symbol.iterator]()) Now we can go “end to end,” If we want to map a linked list of numbers to a linked list of the squares of some numbers, we ca

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01621))_

> Pair1.from(Squares) _//=> {"first":0,_ "rest":{"first":1, "rest":{"first":4, "rest":{ ... Served by the Pot: Collections 200
