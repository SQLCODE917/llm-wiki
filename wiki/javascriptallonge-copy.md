---
page_id: javascriptallonge-copy
page_kind: concept
summary: Copy: 9 statement(s) and 8 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-copy@a589239d7567928f58a167f3724dd173
---

# Copy

What [[javascriptallonge]] covers about copy:

## Statements

- This strategy of waiting to copy until you are writing is called copy-on-write, or “COW:” _(javascriptallonge.pdf (source-range-83ecb080-01895))_
- Copy-on-write is the name given to the policy that whenever a task attempts to make a change to the shared information, it should first create a separate (private) copy of that information to prevent its changes from becoming visible to all the other tasks.— Wikipedia[73] _(javascriptallonge.pdf (source-range-83ecb080-01898))_
- However, Reg sent me a copy of his book and I was humbled. _(javascriptallonge.pdf (source-range-83ecb080-00123))_
- Lather, rinse, repeat: Ever time we call mapWith, we’re creating a new array, copying all the elements from prepend into the new array, and then we no longer use prepend. _(javascriptallonge.pdf (source-range-83ecb080-01517))_
- Arrays avoid this problem by pessimistically copying all the references whenever we extract an element or sequence of elements from them (We’ll see this explained later in Mutation). _(javascriptallonge.pdf (source-range-83ecb080-01567))_
- So to copy a list, we have to save all the bits on the call stack and then construct the list from back-to-front as all the recursive calls return. _(javascriptallonge.pdf (source-range-83ecb080-01661))_
- When we wrote ThreeToFive = OneToFive.rest.rest;, we weren’t making a brand new copy of we were getting a reference to the same chain of nodes. _(javascriptallonge.pdf (source-range-83ecb080-01731))_
- Without mutation, a copy of a linked list can be made in constant space by reversing a reverse of the list: _(javascriptallonge.pdf (source-range-83ecb080-01740))_
- Looking at the code again, you see that the copy function doesn’t copy on write: It follows the pattern that while constructing something, we own it and can be liberal with mutation. _(javascriptallonge.pdf (source-range-83ecb080-01900))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01654, source-range-83ecb080-01657))_

> Taking the length of a linked list is easy: What about mapping? Well, let’s start with the simplest possible thing, making a _copy_ of a list. As we saw above, and discussed in Garbage, Garbage Everywhere, it is fast to iterate forward through a linked list. What isn’t fast is naïvely copying a list:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01655))_

> **const** length = (node, delayed = 0) => node === EMPTY ? delayed : length(node.rest, delayed + 1);

### Technical atom 2

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01654, source-range-83ecb080-01657))_

> Taking the length of a linked list is easy: What about mapping? Well, let’s start with the simplest possible thing, making a _copy_ of a list. As we saw above, and discussed in Garbage, Garbage Everywhere, it is fast to iterate forward through a linked list. What isn’t fast is naïvely copying a list:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01656))_

> length(OneTwoThree) _//=> 3_

### Technical atom 3

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01657))_

> What about mapping? Well, let’s start with the simplest possible thing, making a _copy_ of a list. As we saw above, and discussed in Garbage, Garbage Everywhere, it is fast to iterate forward through a linked list. What isn’t fast is naïvely copying a list:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01658))_

> **const** slowcopy = (node) => node === EMPTY ? EMPTY : { first: node.first, rest: slowcopy(node.rest)};

### Technical atom 4

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01669))_

> Well, well, well. We have unwittingly _reversed_ the list. This makes sense, if lists are constructed from back to front, and we make a linked list out of items as we iterate through it, we’re going to get a backwards copy of the list. This isn’t a bad thing by any stretch of the imagination. Let’s call it what it is:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01670))_

> **const** reverse = (node, delayed = EMPTY) => node === EMPTY ? delayed : reverse(node.rest, { first: node.first, rest: delayed });

### Technical atom 5

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01731))_

> Changes made to ThreeToFive affect OneToFive, because they share the same structure. When we wrote ThreeToFive = OneToFive.rest.rest;, we weren’t making a brand new copy of we were getting a reference to the same chain of nodes.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01730))_

> OneToFive //=> {"first":1,"rest":{"first":2,"rest":{"first":"three","rest":{"first":"fou\ r","rest":{"first":"five","rest":{}}}}}}

### Technical atom 6

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01732))_

> Structure sharing like this is what makes linked lists so fast for taking everything but the first item of a list: We aren’t making a new list, we’re using some of the old list. Whereas destructuring an array with [first, ...rest] does make a copy, so:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01735))_

> **const** OneToFive = [1, 2, 3, 4, 5];

### Technical atom 7

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01740))_

> As noted, one pattern is to be more liberal about mutation when building a data structure. Consider our copy algorithm. Without mutation, a copy of a linked list can be made in constant space by reversing a reverse of the list:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01741))_

> **const** reverse = (node, delayed = EMPTY) => node === EMPTY ? delayed : reverse(node.rest, { first: node.first, rest: delayed });

### Technical atom 8

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01740))_

> As noted, one pattern is to be more liberal about mutation when building a data structure. Consider our copy algorithm. Without mutation, a copy of a linked list can be made in constant space by reversing a reverse of the list:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01742))_

> **const** copy = (node) => reverse(reverse(node));


## Related pages

- [[javascriptallonge-list]] - shared statements and technical atoms (1 shared statement(s), 6 shared atom(s))
- [[javascriptallonge-rest]] - shared statements and technical atoms (1 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-length]] - shared technical atoms (2 shared atom(s))
- [[javascriptallonge-element]] - shared statements (2 shared statement(s))
- [[javascriptallonge-write]] - shared statements (2 shared statement(s))
- [[javascriptallonge-code]] - shared statements (1 shared statement(s))
- [[javascriptallonge-function]] - shared statements (1 shared statement(s))
- [[javascriptallonge-mapwith]] - shared statements (1 shared statement(s))

## Source

- [[javascriptallonge]]
