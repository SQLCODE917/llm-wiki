---
page_id: javascriptallonge-iterable
page_kind: concept
summary: Iterable: 10 statement(s) and 3 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-iterable@de6d2d2c0859624ec9dc0e495b8ab483
---

# Iterable

What [[javascriptallonge]] covers about iterable:

## Statements

- first returns the first element of an iterable (if it has one), and rest returns an iterable that iterates over all but the first element of an iterable. _(javascriptallonge.pdf (source-range-83ecb080-01612))_
- Attempting to spread an infinite iterable into an array is always going to fail. _(javascriptallonge.pdf (source-range-83ecb080-01580))_
- The iterables we’re discussing represent _ordered collections_ . _(javascriptallonge.pdf (source-range-83ecb080-01582))_
- Iterables needn’t represent ordered collections. _(javascriptallonge.pdf (source-range-83ecb080-01583))_
- Whether you work with the same iterator over and over, or get a fresh iterable every time, you are always going to get fresh random numbers. _(javascriptallonge.pdf (source-range-83ecb080-01587))_
- Now is the time to note that we can spread any iterable. _(javascriptallonge.pdf (source-range-83ecb080-01571))_
- Thus, mapWith has the property of preserving the collection semantics of the iterable we give it. _(javascriptallonge.pdf (source-range-83ecb080-01599))_
- For completeness, here are two more handy iterable functions. _(javascriptallonge.pdf (source-range-83ecb080-01612))_
- One useful thing is to write a .from function that gathers an iterable into a particular collection type. _(javascriptallonge.pdf (source-range-83ecb080-01617))_
- So to summarize, ThreeNumbers is an object that we’ve made iterable, by way of writing a _generator_ method for [Symbol.iterator]. _(javascriptallonge.pdf (source-range-83ecb080-01728))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01576))_

> Iterables needn’t represent finite collections: **const** Numbers = { [Symbol.iterator] () { **let** n = 0; **return** { next: () => ({done: **false** , value: n++}) } } } There are useful things we can do with iterables representing an infinitely large collection. But let’s point out what we can’t do with them:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01579))_

> firstAndSecondElement(...Numbers) _//=> infinite loop!_

### Technical atom 2

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01620))_

> Stack3.from = **function** (iterable) { **const** stack = **this** (); **for** ( **let** element **of** iterable) { stack.push(element); } **return** stack; } Pair1.from = (iterable) => ( **function** iterationToList (iteration) { **const** {done, value} = iteration.next(); **return** done ? EMPTY : Pair1(value, iterationToList(iteration)); })(iterable[Symbol.iterator]()) Now we can go “end to end,” If we want to map a linked list of numbers to a linked list of the squares of some numbers, we ca

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01621))_

> Pair1.from(Squares) _//=> {"first":0,_ "rest":{"first":1, "rest":{"first":4, "rest":{ ... Served by the Pot: Collections 200

### Technical atom 3

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01721, source-range-83ecb080-01724))_

> Our generator function oneTwoThree is not an iterator. It’s a function that returns an iterator when we invoke it. We write the function to yield values instead of return a single value, and JavaScript takes care of turning this into an object with a .next() function we can call. Served by the Pot: Collections **const** ThreeNumbers = { [Symbol.iterator]: **function** * () { **yield** 1; **yield** 2; **yield** 3 } } **for** ( **const** i **of** ThreeNumbers) { console.log(i); } _//=>_ 1 2 3 [...

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01722))_

> If we call our generator function more than once, we get new iterators.


## Related pages

- [[javascriptallonge-element]] - shared statements and technical atoms (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-iterator]] - shared statements and technical atoms (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-value]] - shared technical atoms (3 shared atom(s))
- [[javascriptallonge-function]] - shared technical atoms (2 shared atom(s))
- [[javascriptallonge-collection]] - shared technical atoms (1 shared atom(s))
- [[javascriptallonge-generator]] - shared technical atoms (1 shared atom(s))
- [[javascriptallonge-instead]] - shared technical atoms (1 shared atom(s))
- [[javascriptallonge-iteration]] - shared technical atoms (1 shared atom(s))
- [[javascriptallonge-javascript]] - shared technical atoms (1 shared atom(s))
- [[javascriptallonge-method]] - shared technical atoms (1 shared atom(s))
- [[javascriptallonge-object]] - shared technical atoms (1 shared atom(s))
- [[javascriptallonge-mapwith]] - shared statements (1 shared statement(s))
- [[javascriptallonge-return]] - shared statements (1 shared statement(s))
- [[javascriptallonge-section-values-are-expressions-iteration-and-iterables-iterables-c8af297d]] - source section (14 shared statement(s))

## Source

- [[javascriptallonge]]
