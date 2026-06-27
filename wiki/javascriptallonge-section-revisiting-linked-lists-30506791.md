---
page_id: javascriptallonge-section-revisiting-linked-lists-30506791
page_kind: source
summary: **revisiting linked lists**: 30 source-backed entries and 13 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-revisiting-linked-lists-30506791@b999ba7d9993aaf9ce523df26613516e
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

> Context: Earlier, we used two-element arrays as nodes in a linked list:
_(context: javascriptallonge.pdf (source-range-83ecb080-01644))_

> **const** cons = (a, d) => [a, d], car = ([a, d]) => a, cdr = ([a, d]) => d;
_(source: javascriptallonge.pdf (source-range-83ecb080-01645))_

> Context: We can then perform the equivalent of [first, ...rest] with direct property accessors:
_(context: javascriptallonge.pdf (source-range-83ecb080-01648))_

> **const** EMPTY = {}; **const** OneTwoThree = { first: 1, rest: { first: 2, rest: { first: 3, rest: EMPTY \ } } };
_(source: javascriptallonge.pdf (source-range-83ecb080-01651))_

> OneTwoThree.first _//=> 1_ OneTwoThree.rest _//=> {"first":2,"rest":{"first":3,"rest":{}}}_
_(source: javascriptallonge.pdf (source-range-83ecb080-01652))_

> OneTwoThree.rest.rest.first _//=> 3_
_(source: javascriptallonge.pdf (source-range-83ecb080-01653))_

> Context: Taking the length of a linked list is easy: What about mapping? Well, let’s start with the simplest possible thing, making a _copy_ of a list. As we saw above, and discussed in Garbage, Garbage Everywhere, it is fast to iterate forward through a linked list. What isn’t fast is naïvely copying a list:
_(context: javascriptallonge.pdf (source-range-83ecb080-01654, source-range-83ecb080-01657))_

> **const** length = (node, delayed = 0) => node === EMPTY ? delayed : length(node.rest, delayed + 1);
_(source: javascriptallonge.pdf (source-range-83ecb080-01655))_

> Context: Taking the length of a linked list is easy: What about mapping? Well, let’s start with the simplest possible thing, making a _copy_ of a list. As we saw above, and discussed in Garbage, Garbage Everywhere, it is fast to iterate forward through a linked list. What isn’t fast is naïvely copying a list:
_(context: javascriptallonge.pdf (source-range-83ecb080-01654, source-range-83ecb080-01657))_

> length(OneTwoThree) _//=> 3_
_(source: javascriptallonge.pdf (source-range-83ecb080-01656))_

> Context: What about mapping? Well, let’s start with the simplest possible thing, making a _copy_ of a list. As we saw above, and discussed in Garbage, Garbage Everywhere, it is fast to iterate forward through a linked list. What isn’t fast is naïvely copying a list:
_(context: javascriptallonge.pdf (source-range-83ecb080-01657))_

> **const** slowcopy = (node) => node === EMPTY ? EMPTY : { first: node.first, rest: slowcopy(node.rest)};
_(source: javascriptallonge.pdf (source-range-83ecb080-01658))_

> Context: We could follow the strategy of delaying the work. Let’s write that naively:
_(context: javascriptallonge.pdf (source-range-83ecb080-01662))_

> **const** copy2 = (node, delayed = EMPTY) => node === EMPTY
_(source: javascriptallonge.pdf (source-range-83ecb080-01665))_

> Context: Well, well, well. We have unwittingly _reversed_ the list. This makes sense, if lists are constructed from back to front, and we make a linked list out of items as we iterate through it, we’re going to get a backwards copy of the list. This isn’t a bad thing by any stretch of the imagination. Let’s call it what it is:
_(context: javascriptallonge.pdf (source-range-83ecb080-01669))_

> **const** reverse = (node, delayed = EMPTY) => node === EMPTY ? delayed : reverse(node.rest, { first: node.first, rest: delayed });
_(source: javascriptallonge.pdf (source-range-83ecb080-01670))_

> Context: And now, we can make a reversing map:
_(context: javascriptallonge.pdf (source-range-83ecb080-01671))_

> **const** reverseMapWith = (fn, node, delayed = EMPTY) => node === EMPTY
_(source: javascriptallonge.pdf (source-range-83ecb080-01672))_

> Context: And a regular mapWith follows:
_(context: javascriptallonge.pdf (source-range-83ecb080-01674))_

> **const** reverse = (node, delayed = EMPTY) => node === EMPTY ? delayed : reverse(node.rest, { first: node.first, rest: delayed });
_(source: javascriptallonge.pdf (source-range-83ecb080-01675))_

> Context: And a regular mapWith follows:
_(context: javascriptallonge.pdf (source-range-83ecb080-01674))_

> **const** mapWith = (fn, node, delayed = EMPTY) => node === EMPTY ? reverse(delayed) : mapWith(fn, node.rest, { first: fn(node.first), rest: delayed });
_(source: javascriptallonge.pdf (source-range-83ecb080-01676))_

> Context: And a regular mapWith follows:
_(context: javascriptallonge.pdf (source-range-83ecb080-01674))_

> mapWith((x) => x * x, OneTwoThree) _//=> {"first":1,"rest":{"first":4,"rest":{"first":9,"rest":{}}}}_
_(source: javascriptallonge.pdf (source-range-83ecb080-01677))_
