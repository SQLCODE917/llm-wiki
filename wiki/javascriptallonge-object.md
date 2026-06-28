---
page_id: javascriptallonge-object
page_kind: concept
summary: Object: 14 statement(s) and 6 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-object@b8c242d1552ab092bfa6dee96777162c
---

# Object

What [[javascriptallonge]] covers about object:

## Statements

- In programs involving large collections of objects, it can be handy to implement iterators as objects, rather than functions. _(javascriptallonge.pdf (source-range-83ecb080-01547))_
- When working with objects, we do things the object way. _(javascriptallonge.pdf (source-range-83ecb080-01553))_
- The for...of loop works directly with any object that is _iterable_ , meaning it works with any object that has a Symbol.iterator method that returns an object iterator. _(javascriptallonge.pdf (source-range-83ecb080-01566))_
- In JavaScript, an object is a map from string keys to values. _(javascriptallonge.pdf (source-range-83ecb080-01075))_
- Specifically, arrays and objects can mutate. _(javascriptallonge.pdf (source-range-83ecb080-01124))_
- Mutating existing objects has special implications when two bindings are aliases of the same value. _(javascriptallonge.pdf (source-range-83ecb080-01134))_
- Many objects in JavaScript can model collections of things. _(javascriptallonge.pdf (source-range-83ecb080-01529))_
- Iteration for functions and objects has been around for many, many decades. _(javascriptallonge.pdf (source-range-83ecb080-01546))_
- Fortunately, an iterator object is almost as simple as an iterator function. _(javascriptallonge.pdf (source-range-83ecb080-01550))_
- Whether it’s a simple functional iterator, or an iterable object with a .next() method, an iterator is something we call repeatedly until it tells us that it’s done. _(javascriptallonge.pdf (source-range-83ecb080-01632))_
- Using a generator instead of writing an iterator object that has a .next() method allows us to write code that can be much simpler for cases like recursive iterations or state patterns. _(javascriptallonge.pdf (source-range-83ecb080-01766))_
- This “fat object” style springs from a misunderstanding: When we say a collection should know how to perform a map over itself, we don’t need for the collection to handle every single detail. _(javascriptallonge.pdf (source-range-83ecb080-01776))_
- Object-oriented collections should definitely have methods for mapping, reducing, filtering, and finding. _(javascriptallonge.pdf (source-range-83ecb080-01778))_
- They produce small iterable objects that refer back to the original iteration. _(javascriptallonge.pdf (source-range-83ecb080-01792))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01081))_

> { year: 2012, month: 6, day: 14 } Two objects created with separate evaluations have differing identities, just like arrays:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01082))_

> - { year: 2012, month: 6, day: 14 } === { year: 2012, month: 6, day: 14 } _//=> false_

### Technical atom 2

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01083))_

> Objects use [] to access the values by name, using a string:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01084))_

> - { year: 2012, month: 6, day: 14 }['day'] _//=> 14_

### Technical atom 3

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01083))_

> Objects use [] to access the values by name, using a string:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01086))_

> - o['a'] === x && o['b'] === y && o['c'] === z _//=> true_

### Technical atom 4

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01632))_

> Let’s consider how they work. Whether it’s a simple functional iterator, or an iterable object with a .next() method, an iterator is something we call repeatedly until it tells us that it’s done.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01633))_

> Iterators have to arrange its own state such that when you call them, they compute and return the next item.

### Technical atom 5

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01721, source-range-83ecb080-01724))_

> Our generator function oneTwoThree is not an iterator. It’s a function that returns an iterator when we invoke it. We write the function to yield values instead of return a single value, and JavaScript takes care of turning this into an object with a .next() function we can call. Served by the Pot: Collections **const** ThreeNumbers = { [Symbol.iterator]: **function** * () { **yield** 1; **yield** 2; **yield** 3 } } **for** ( **const** i **of** ThreeNumbers) { console.log(i); } _//=>_ 1 2 3 [...

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01722))_

> If we call our generator function more than once, we get new iterators.

### Technical atom 6

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01744))_

> Here’s a first crack at a function that returns an iterable object for iterating over trees:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01747))_

> But if you can write it as a simple generator, write it as a simple generator.


## Related pages

- [[javascriptallonge-function]] - shared statements and technical atoms (2 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-iterator]] - shared statements and technical atoms (3 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-method]] - shared statements and technical atoms (1 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-javascript]] - shared statements and technical atoms (2 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-functional]] - shared statements and technical atoms (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-instead]] - shared statements and technical atoms (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-value]] - shared technical atoms (3 shared atom(s))
- [[javascriptallonge-generator]] - shared technical atoms (1 shared atom(s))
- [[javascriptallonge-iterable]] - shared technical atoms (1 shared atom(s))
- [[javascriptallonge-return]] - shared technical atoms (1 shared atom(s))
- [[javascriptallonge-collection]] - shared statements (2 shared statement(s))
- [[javascriptallonge-eager-collection]] - shared statements (2 shared statement(s))
- [[javascriptallonge-iteration]] - shared statements (1 shared statement(s))
- [[javascriptallonge-program]] - shared statements (1 shared statement(s))

## Source

- [[javascriptallonge]]
