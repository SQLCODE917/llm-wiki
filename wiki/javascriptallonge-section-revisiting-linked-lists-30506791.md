---
page_id: javascriptallonge-section-revisiting-linked-lists-30506791
page_kind: source
summary: **revisiting linked lists**: 30 source-backed entries and 13 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-revisiting-linked-lists-30506791@f912854960bdbbd6e7512fd43bedf137
---

# **revisiting linked lists**

From [[javascriptallonge]].

## Statements

- But now that we’ve looked at objects, we can use an object instead of a two-element array. _(javascriptallonge.pdf (source-range-83ecb080-01646))_
- In essence, this simple implementation used functions to create an abstraction with named elements. _(javascriptallonge.pdf (source-range-83ecb080-01646))_
- While we’re at it, let’s use contemporary names. _(javascriptallonge.pdf (source-range-83ecb080-01646))_
- As we saw above, and discussed in Garbage, Garbage Everywhere, it is fast to iterate forward through a linked list. _(javascriptallonge.pdf (source-range-83ecb080-01657))_
- The problem here is that linked lists are constructed back-to-front, but we iterate over them frontto-back. _(javascriptallonge.pdf (source-range-83ecb080-01661))_
- So to copy a list, we have to save all the bits on the call stack and then construct the list from back-to-front as all the recursive calls return. _(javascriptallonge.pdf (source-range-83ecb080-01661))_
- So to copy a list, we have to save all the bits on the call stack and then construct the list from back-to-front as all the recursive calls return. _(javascriptallonge.pdf (source-range-83ecb080-01661))_
- We could follow the strategy of delaying the work. _(javascriptallonge.pdf (source-range-83ecb080-01662))_
- We have unwittingly _reversed_ the list. _(javascriptallonge.pdf (source-range-83ecb080-01669))_
- This makes sense, if lists are constructed from back to front, and we make a linked list out of items as we iterate through it, we’re going to get a backwards copy of the list. _(javascriptallonge.pdf (source-range-83ecb080-01669))_
- Likewise, it takes twice as much memory, because it constructs a reverse of the desired result before throwing it away. _(javascriptallonge.pdf (source-range-83ecb080-01680))_
- Likewise, it takes twice as much memory, because it constructs a reverse of the desired result before throwing it away. _(javascriptallonge.pdf (source-range-83ecb080-01680))_
- Our mapWith function takes twice as long as a straight iteration, because it iterates over the entire list twice, once to map, and once to reverse the list. _(javascriptallonge.pdf (source-range-83ecb080-01680))_
- Mind you, this is still much, much faster than making partial copies of arrays. _(javascriptallonge.pdf (source-range-83ecb080-01681))_
- For a list of length _n_ , we created _n_ superfluous nodes and copied _n_ superfluous values. _(javascriptallonge.pdf (source-range-83ecb080-01681))_
- Whereas our naïve array algorithm created 2 _n_ superfluous arrays and copied _n_[2] superfluous values. _(javascriptallonge.pdf (source-range-83ecb080-01681))_
- Whereas our naïve array algorithm created 2 _n_ superfluous arrays and copied _n_[2] superfluous values. _(javascriptallonge.pdf (source-range-83ecb080-01681))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01644))_

> Earlier, we used two-element arrays as nodes in a linked list:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01645))_

> **const** cons = (a, d) => [a, d], car = ([a, d]) => a, cdr = ([a, d]) => d;

### Technical atom 2

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01648))_

> We can then perform the equivalent of [first, ...rest] with direct property accessors:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01651))_

> **const** EMPTY = {}; **const** OneTwoThree = { first: 1, rest: { first: 2, rest: { first: 3, rest: EMPTY \ } } };

### Technical atom 3

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01652))_

> OneTwoThree.first _//=> 1_ OneTwoThree.rest _//=> {"first":2,"rest":{"first":3,"rest":{}}}_

### Technical atom 4

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01653))_

> OneTwoThree.rest.rest.first _//=> 3_

### Technical atom 5

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01654, source-range-83ecb080-01657))_

> Taking the length of a linked list is easy: What about mapping? Well, let’s start with the simplest possible thing, making a _copy_ of a list. As we saw above, and discussed in Garbage, Garbage Everywhere, it is fast to iterate forward through a linked list. What isn’t fast is naïvely copying a list:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01655))_

> **const** length = (node, delayed = 0) => node === EMPTY ? delayed : length(node.rest, delayed + 1);

### Technical atom 6

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01654, source-range-83ecb080-01657))_

> Taking the length of a linked list is easy: What about mapping? Well, let’s start with the simplest possible thing, making a _copy_ of a list. As we saw above, and discussed in Garbage, Garbage Everywhere, it is fast to iterate forward through a linked list. What isn’t fast is naïvely copying a list:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01656))_

> length(OneTwoThree) _//=> 3_

### Technical atom 7

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01657))_

> What about mapping? Well, let’s start with the simplest possible thing, making a _copy_ of a list. As we saw above, and discussed in Garbage, Garbage Everywhere, it is fast to iterate forward through a linked list. What isn’t fast is naïvely copying a list:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01658))_

> **const** slowcopy = (node) => node === EMPTY ? EMPTY : { first: node.first, rest: slowcopy(node.rest)};

### Technical atom 8

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01662))_

> We could follow the strategy of delaying the work. Let’s write that naively:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01665))_

> **const** copy2 = (node, delayed = EMPTY) => node === EMPTY

### Technical atom 9

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01669))_

> Well, well, well. We have unwittingly _reversed_ the list. This makes sense, if lists are constructed from back to front, and we make a linked list out of items as we iterate through it, we’re going to get a backwards copy of the list. This isn’t a bad thing by any stretch of the imagination. Let’s call it what it is:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01670))_

> **const** reverse = (node, delayed = EMPTY) => node === EMPTY ? delayed : reverse(node.rest, { first: node.first, rest: delayed });

### Technical atom 10

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01671))_

> And now, we can make a reversing map:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01672))_

> **const** reverseMapWith = (fn, node, delayed = EMPTY) => node === EMPTY

### Technical atom 11

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01674))_

> And a regular mapWith follows:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01675))_

> **const** reverse = (node, delayed = EMPTY) => node === EMPTY ? delayed : reverse(node.rest, { first: node.first, rest: delayed });

### Technical atom 12

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01674))_

> And a regular mapWith follows:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01676))_

> **const** mapWith = (fn, node, delayed = EMPTY) => node === EMPTY ? reverse(delayed) : mapWith(fn, node.rest, { first: fn(node.first), rest: delayed });

### Technical atom 13

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01674))_

> And a regular mapWith follows:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01677))_

> mapWith((x) => x * x, OneTwoThree) _//=> {"first":1,"rest":{"first":4,"rest":{"first":9,"rest":{}}}}_
