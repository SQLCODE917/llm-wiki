---
page_id: javascriptallonge-collection
page_kind: concept
summary: Collection: 7 statement(s) and 2 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-collection@ff58d4ca334ec5e0c2d0e95fe7cc2dcf
---

# Collection

What [[javascriptallonge]] covers about collection:

## Statements

- Acting on the elements of a collection one at a time is called _iterating over the contents_ , and JavaScript has a standard way to iterate over the contents of collections. _(javascriptallonge.pdf (source-range-83ecb080-01530))_
- This “fat object” style springs from a misunderstanding: When we say a collection should know how to perform a map over itself, we don’t need for the collection to handle every single detail. _(javascriptallonge.pdf (source-range-83ecb080-01776))_
- In programs involving large collections of objects, it can be handy to implement iterators as objects, rather than functions. _(javascriptallonge.pdf (source-range-83ecb080-01547))_
- For example, if we spread a large collection just to find an element in the collection, it might have been wiser to iterate over the element using its iterator directly. _(javascriptallonge.pdf (source-range-83ecb080-01573))_
- We tell ourselves that, well, a collection ought to know how to map itself. _(javascriptallonge.pdf (source-range-83ecb080-01774))_
- If we mutate a collection after taking an iterable, we might get an unexpected result. _(javascriptallonge.pdf (source-range-83ecb080-01808))_
- It isn’t a collection, it has no meaning if we try to spread it into parameters or as the subject of a for...of block. _(javascriptallonge.pdf (source-range-83ecb080-01934))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01576))_

> Iterables needn’t represent finite collections: **const** Numbers = { [Symbol.iterator] () { **let** n = 0; **return** { next: () => ({done: **false** , value: n++}) } } } There are useful things we can do with iterables representing an infinitely large collection. But let’s point out what we can’t do with them:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01579))_

> firstAndSecondElement(...Numbers) _//=> infinite loop!_

### Technical atom 2

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01610))_

> And here’s a computation performed using operations on ordered collections: We’ll create an ordered collection of square numbers that end in one and are less than 1,000: **const** Squares = mapWith((x) => x * x, Numbers); **const** EndWithOne = filterWith((x) => x % 10 === 1, Squares); **const** UpTo1000 = untilWith((x) => (x > 1000), EndWithOne);

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01611))_

> [...UpTo1000] _//=>_ [1,81,121,361,441,841,961] [...UpTo1000] _//=>_ [1,81,121,361,441,841,961] As we expect from an ordered collection, each time we iterate over UpTo1000, we begin at the beginning.


## Related pages

- [[javascriptallonge-eager-collection]] - narrower topic (3 shared statement(s))
- [[javascriptallonge-iterable]] - shared technical atoms (1 shared atom(s))
- [[javascriptallonge-mapwith]] - shared technical atoms (1 shared atom(s))
- [[javascriptallonge-value]] - shared technical atoms (1 shared atom(s))
- [[javascriptallonge-element]] - shared statements (2 shared statement(s))
- [[javascriptallonge-object]] - shared statements (2 shared statement(s))
- [[javascriptallonge-program]] - shared statements (1 shared statement(s))

## Source

- [[javascriptallonge]]
