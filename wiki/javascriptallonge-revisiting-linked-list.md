---
page_id: javascriptallonge-revisiting-linked-list
page_kind: concept
summary: **revisiting linked lists**: 13 statement(s) and 13 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-revisiting-linked-list@29b11eecf25a60a6a5c4b4a41c264b21
---

# **revisiting linked lists**

What [[javascriptallonge]] covers about **revisiting linked lists**:

## Statements

- So to copy a list, we have to save all the bits on the call stack and then construct the list from back-to-front as all the recursive calls return. _(javascriptallonge.pdf (source-range-83ecb080-01661))_
- For a list of length _n_ , we created _n_ superfluous nodes and copied _n_ superfluous values. _(javascriptallonge.pdf (source-range-83ecb080-01681))_
- As we saw above, and discussed in Garbage, Garbage Everywhere, it is fast to iterate forward through a linked list. _(javascriptallonge.pdf (source-range-83ecb080-01657))_
- The problem here is that linked lists are constructed back-to-front, but we iterate over them frontto-back. _(javascriptallonge.pdf (source-range-83ecb080-01661))_
- We have unwittingly _reversed_ the list. _(javascriptallonge.pdf (source-range-83ecb080-01669))_
- This makes sense, if lists are constructed from back to front, and we make a linked list out of items as we iterate through it, we’re going to get a backwards copy of the list. _(javascriptallonge.pdf (source-range-83ecb080-01669))_
- But now that we’ve looked at objects, we can use an object instead of a two-element array. _(javascriptallonge.pdf (source-range-83ecb080-01646))_
- In essence, this simple implementation used functions to create an abstraction with named elements. _(javascriptallonge.pdf (source-range-83ecb080-01646))_
- While we’re at it, let’s use contemporary names. _(javascriptallonge.pdf (source-range-83ecb080-01646))_
- We could follow the strategy of delaying the work. _(javascriptallonge.pdf (source-range-83ecb080-01662))_
- Likewise, it takes twice as much memory, because it constructs a reverse of the desired result before throwing it away. _(javascriptallonge.pdf (source-range-83ecb080-01680))_
- Mind you, this is still much, much faster than making partial copies of arrays. _(javascriptallonge.pdf (source-range-83ecb080-01681))_
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


## Source

- [[javascriptallonge]]
