---
page_id: javascriptallonge-section-values-are-expressions-plain-old-javascript-objects-revisiting-linked-lists-f1f1e57e
page_kind: source
summary: values are expressions / Plain Old JavaScript Objects / revisiting linked lists: 17 source-backed entries and 2 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-values-are-expressions-plain-old-javascript-objects-revisiting-linked-lists-f1f1e57e@9e7fe1577f52a0271c34ffe3edfbc5cd
---

# values are expressions / Plain Old JavaScript Objects / revisiting linked lists

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-values-are-expressions-plain-old-javascript-objects-cc77db27]] - broader source section

## Statements

- While we’re at it, let’s use contemporary names. _(javascriptallonge.pdf (source-range-83ecb080-01103))_
- In essence, this simple implementation used functions to create an abstraction with named elements. _(javascriptallonge.pdf (source-range-83ecb080-01103))_
- But now that we’ve looked at objects, we can use an object instead of a two-element array. _(javascriptallonge.pdf (source-range-83ecb080-01103))_
- As we saw above, and discussed in Garbage, Garbage Everywhere, it is fast to iterate forward through a linked list. _(javascriptallonge.pdf (source-range-83ecb080-01109))_
- So to copy a list, we have to save all the bits on the call stack and then construct the list from back-to-front as all the recursive calls return. _(javascriptallonge.pdf (source-range-83ecb080-01109))_
- So to copy a list, we have to save all the bits on the call stack and then construct the list from back-to-front as all the recursive calls return. _(javascriptallonge.pdf (source-range-83ecb080-01109))_
- We could follow the strategy of delaying the work. _(javascriptallonge.pdf (source-range-83ecb080-01110))_
- We have unwittingly _reversed_ the list. _(javascriptallonge.pdf (source-range-83ecb080-01113))_
- This makes sense, if lists are constructed from back to front, and we make a linked list out of items as we iterate through it, we’re going to get a backwards copy of the list. _(javascriptallonge.pdf (source-range-83ecb080-01113))_
- Likewise, it takes twice as much memory, because it constructs a reverse of the desired result before throwing it away. _(javascriptallonge.pdf (source-range-83ecb080-01116))_
- Likewise, it takes twice as much memory, because it constructs a reverse of the desired result before throwing it away. _(javascriptallonge.pdf (source-range-83ecb080-01116))_
- For a list of length _n_ , we created _n_ superfluous nodes and copied _n_ superfluous values. _(javascriptallonge.pdf (source-range-83ecb080-01117))_
- Whereas our naïve array algorithm created 2 _n_ superfluous arrays and copied _n_[2] superfluous values. _(javascriptallonge.pdf (source-range-83ecb080-01117))_
- Mind you, this is still much, much faster than making partial copies of arrays. _(javascriptallonge.pdf (source-range-83ecb080-01117))_
- Whereas our naïve array algorithm created 2 _n_ superfluous arrays and copied _n_[2] superfluous values. _(javascriptallonge.pdf (source-range-83ecb080-01117))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01104, source-range-83ecb080-01109))_

> We can then perform the equivalent of [first, ...rest] with direct property accessors: What about mapping? Well, let’s start with the simplest possible thing, making a _copy_ of a list. As we saw above, and discussed in Garbage, Garbage Everywhere, it is fast to iterate forward through a linked list. What isn’t fast is naïvely copying a list: **const** slowcopy = (node) => node === EMPTY ? EMPTY : { first: node.first, rest: slowcopy(node.rest)}; slowcopy(OneTwoThree) _//=> {"first":1,"rest":{"fi

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01107))_

> OneTwoThree.first _//=> 1_ OneTwoThree.rest _//=> {"first":2,"rest":{"first":3,"rest":{}}}_ OneTwoThree.rest.rest.first _//=> 3_

### Technical atom 2

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01110))_

> We could follow the strategy of delaying the work. Let’s write that naively:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01112))_

> 116 **const** copy2 = (node, delayed = EMPTY) => node === EMPTY
