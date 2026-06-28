---
page_id: javascriptallonge-copy
page_kind: concept
summary: Copy: 7 statement(s) and 3 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-copy@2b766060744486030158d711a6f04aa9
---

# Copy

What [[javascriptallonge]] covers about copy:

## Statements

- This strategy of waiting to copy until you are writing is called copy-on-write, or “COW:” Composing and Decomposing Data _(javascriptallonge.pdf (source-range-83ecb080-01246))_
- However, Reg sent me a copy of his book and I was humbled. _(javascriptallonge.pdf (source-range-83ecb080-00095))_
- Lather, rinse, repeat: Ever time we call mapWith, we’re creating a new array, copying all the elements from prepend into the new array, and then we no longer use prepend. _(javascriptallonge.pdf (source-range-83ecb080-01023))_
- Arrays avoid this problem by pessimistically copying all the references whenever we extract an element or sequence of elements from them (We’ll see this explained later in Mutation). _(javascriptallonge.pdf (source-range-83ecb080-01062))_
- So to copy a list, we have to save all the bits on the call stack and then construct the list from back-to-front as all the recursive calls return. _(javascriptallonge.pdf (source-range-83ecb080-01109))_
- When we wrote ThreeToFive = OneToFive.rest.rest;, we weren’t making a brand new copy of we were getting a reference to the same chain of nodes. _(javascriptallonge.pdf (source-range-83ecb080-01149))_
- Looking at the code again, you see that the copy function doesn’t copy on write: It follows the pattern that while constructing something, we own it and can be liberal with mutation. _(javascriptallonge.pdf (source-range-83ecb080-01249))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01104, source-range-83ecb080-01109))_

> We can then perform the equivalent of [first, ...rest] with direct property accessors: What about mapping? Well, let’s start with the simplest possible thing, making a _copy_ of a list. As we saw above, and discussed in Garbage, Garbage Everywhere, it is fast to iterate forward through a linked list. What isn’t fast is naïvely copying a list: **const** slowcopy = (node) => node === EMPTY ? EMPTY : { first: node.first, rest: slowcopy(node.rest)}; slowcopy(OneTwoThree) _//=> {"first":1,"rest":{"fi

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01107))_

> OneTwoThree.first _//=> 1_ OneTwoThree.rest _//=> {"first":2,"rest":{"first":3,"rest":{}}}_ OneTwoThree.rest.rest.first _//=> 3_

### Technical atom 2

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01150))_

> Structure sharing like this is what makes linked lists so fast for taking everything but the first item of a list: We aren’t making a new list, we’re using some of the old list. Whereas destructuring an array with [first, ...rest] does make a copy, so:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01152))_

> 122 **const** OneToFive = [1, 2, 3, 4, 5];

### Technical atom 3

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01150))_

> Structure sharing like this is what makes linked lists so fast for taking everything but the first item of a list: We aren’t making a new list, we’re using some of the old list. Whereas destructuring an array with [first, ...rest] does make a copy, so:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01153))_

> We don’t have to remember to use copying operations when we pass it as a value to a function, or extract some data from it.


## Related pages

- [[javascriptallonge-rest]] - shared statements and technical atoms (1 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-list]] - shared statements and technical atoms (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-structure]] - shared technical atoms (2 shared atom(s))
- [[javascriptallonge-element]] - shared statements (2 shared statement(s))
- [[javascriptallonge-code]] - shared statements (1 shared statement(s))
- [[javascriptallonge-follow]] - shared statements (1 shared statement(s))
- [[javascriptallonge-function]] - shared statements (1 shared statement(s))
- [[javascriptallonge-mapwith]] - shared statements (1 shared statement(s))
- [[javascriptallonge-pattern]] - shared statements (1 shared statement(s))
- [[javascriptallonge-problem]] - shared statements (1 shared statement(s))
- [[javascriptallonge-reference]] - shared statements (1 shared statement(s))
- [[javascriptallonge-write]] - shared statements (1 shared statement(s))

## Source

- [[javascriptallonge]]
