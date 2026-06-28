---
page_id: javascriptallonge-iteration
page_kind: concept
summary: Iteration: 2 statement(s) and 1 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-iteration@72b56e8f1017c339f1cd7696b73639bc
---

# Iteration

What [[javascriptallonge]] covers about iteration:

## Statements

- Iteration for functions and objects has been around for many, many decades. _(javascriptallonge.pdf (source-range-83ecb080-01546))_
- Our functions don’t need to know anything about how an object implements iteration, and we get the benefit of lazily traversing our objects. _(javascriptallonge.pdf (source-range-83ecb080-01543))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01620))_

> Stack3.from = **function** (iterable) { **const** stack = **this** (); **for** ( **let** element **of** iterable) { stack.push(element); } **return** stack; } Pair1.from = (iterable) => ( **function** iterationToList (iteration) { **const** {done, value} = iteration.next(); **return** done ? EMPTY : Pair1(value, iterationToList(iteration)); })(iterable[Symbol.iterator]()) Now we can go “end to end,” If we want to map a linked list of numbers to a linked list of the squares of some numbers, we ca

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01621))_

> Pair1.from(Squares) _//=> {"first":0,_ "rest":{"first":1, "rest":{"first":4, "rest":{ ... Served by the Pot: Collections 200


## Related pages

- [[javascriptallonge-function]] - shared statements and technical atoms (2 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-element]] - shared technical atoms (1 shared atom(s))
- [[javascriptallonge-iterable]] - shared technical atoms (1 shared atom(s))
- [[javascriptallonge-value]] - shared technical atoms (1 shared atom(s))
- [[javascriptallonge-functional-iterator]] - shared statements (1 shared statement(s))
- [[javascriptallonge-object]] - shared statements (1 shared statement(s))

## Source

- [[javascriptallonge]]
