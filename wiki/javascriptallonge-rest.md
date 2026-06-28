---
page_id: javascriptallonge-rest
page_kind: concept
summary: Rest: 12 statement(s) and 10 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-rest@f8a61d21ac7c49862b9cb6c89b5fece7
---

# Rest

What [[javascriptallonge]] covers about rest:

## Statements

- Although you needn’t restrict yourself to a small number of simple patterns, it can be helpful to understand the patterns so that you can structure your code around some basic building blocks. _(javascriptallonge.pdf (source-range-83ecb080-00824))_
- Thanks to the parallel between array literals + spreads with destructuring + rests, we can also use the same rules to decompose lists: _(javascriptallonge.pdf (source-range-83ecb080-01306))_
- Next, JavaScript invokes mapWith(fn, rest), which is semantically equivalent to mapWith((x) => x * x, [2, 3, 4, 5]). _(javascriptallonge.pdf (source-range-83ecb080-01405))_
- **Key Point** : Our [first, ...rest] approach to recursion is slow because that it creates a lot of temporary arrays, and it spends an enormous amount of time copying elements into arrays that end up being discarded. _(javascriptallonge.pdf (source-range-83ecb080-01519))_
- When we wrote ThreeToFive = OneToFive.rest.rest;, we weren’t making a brand new copy of we were getting a reference to the same chain of nodes. _(javascriptallonge.pdf (source-range-83ecb080-01731))_
- When you take the rest of an array with destructuring ([first, ...rest]), you are given a _copy_ of the elements of the array. _(javascriptallonge.pdf (source-range-83ecb080-01853))_
- When you take the rest of a linked list with its reference, you are given the exact same nodes of the elements of the original list. _(javascriptallonge.pdf (source-range-83ecb080-01854))_
- Whenever we take the rest of a list, make a copy. _(javascriptallonge.pdf (source-range-83ecb080-01875))_
- like our other operations, rest preserves the ordered collection semantics of its argument. _(javascriptallonge.pdf (source-range-83ecb080-02503))_
- The rest of the program continues along its way until it makes another call to iterator.next(). _(javascriptallonge.pdf (source-range-83ecb080-02626))_
- The rest of the program continues along its way until it makes another call to iterator.next(). _(javascriptallonge.pdf (source-range-83ecb080-02631))_
- The rest of the program continues along its way until it makes another call to iterator.next(). _(javascriptallonge.pdf (source-range-83ecb080-02636))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01422, source-range-83ecb080-01424))_

> That is excellent, but one wrapping is not a big deal. When would we really care? Consider this implementation of length: The length function calls itself, but it is not a tail-call, because it returns 1 + length(rest), not length(rest).

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01423))_

> **const** length = ([first, ...rest]) => first === **undefined** ? 0 : 1 + length(rest);

### Technical atom 2

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01564))_

> If [first, ...rest] is so slow, why does JavaScript use arrays instead of making everything a linked list?

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01565))_

> And if you want an arbitrary item from a list, you have to iterate through the list element by element, whereas with the indexed array you just fetch it.

### Technical atom 3

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01731))_

> Changes made to ThreeToFive affect OneToFive, because they share the same structure. When we wrote ThreeToFive = OneToFive.rest.rest;, we weren’t making a brand new copy of we were getting a reference to the same chain of nodes.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01730))_

> OneToFive //=> {"first":1,"rest":{"first":2,"rest":{"first":"three","rest":{"first":"fou\ r","rest":{"first":"five","rest":{}}}}}}

### Technical atom 4

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01732))_

> Structure sharing like this is what makes linked lists so fast for taking everything but the first item of a list: We aren’t making a new list, we’re using some of the old list. Whereas destructuring an array with [first, ...rest] does make a copy, so:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01735))_

> **const** OneToFive = [1, 2, 3, 4, 5];

### Technical atom 5

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01854))_

> When you take the rest of a linked list with its reference, you are given the exact same nodes of the elements of the original list.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01855))_

> The consequence of this is that if you have an array, and you take it’s “rest,” your “child” array is a copy of the elements of the parent array.

### Technical atom 6

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01868))_

> **const** copy = (node, head = **null** , tail = **null** ) => { **if** (node === EMPTY) { **return** head; } **else if** (tail === **null** ) { **const** { first, rest } = node; **const** newNode = { first, rest }; **return** copy(rest, newNode, newNode); } **else** { **const** { first, rest } = node; **const** newNode = { first, rest }; tail.rest = newNode; **return** copy(node.rest, head, newNode); } } **const** first = ({first, rest}) => first; **const** rest = ({first, rest}) => rest; **con

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01871))_

> **const** childList = rest(parentList);

### Technical atom 7

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01875))_

> So back to the problem of structure sharing. One strategy for avoiding problems is to be _pessimistic_ . Whenever we take the rest of a list, make a copy.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01876))_

> **const** rest = ({first, rest}) => copy(rest);

### Technical atom 8

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01875, source-range-83ecb080-01879))_

> So back to the problem of structure sharing. One strategy for avoiding problems is to be _pessimistic_ . Whenever we take the rest of a list, make a copy. This strategy is called “copy-on-read”, because when we attempt the parent to “read” the value of a child of the list, we make a copy and read the copy of the child. Thereafter, we can write to the parent or the copy of the child freely.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01878))_

> parentList _//=> {"first":1,"rest":{"first":2,"rest":{"first":"three","rest":{"first":{},"\_ rest":{}}}}} childList //=> {"first":"two","rest":{"first":3,"rest":{"first":{},"rest":{}}}}

### Technical atom 9

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01885))_

> Why are we copying? In case we modify a child list. Ok, what if we do this: Make the copy when we know we are modifying the list. When do we know that? When we call set. We’ll restore our original definition for rest, but change set:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01886))_

> **const** rest = ({first, rest}) => rest;

### Technical atom 10

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02501))_

> For completeness, here are two more handy iterable functions. first returns the first element of an iterable (if it has one), and rest returns an iterable that iterates over all but the first element of an iterable. They are equivalent to destructuring arrays with [first, ...rest]:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02502))_

> **const** first = (iterable) => iterable[Symbol.iterator]().next().value; **const** rest = (iterable) => ({ [Symbol.iterator] () { **const** iterator = iterable[Symbol.iterator](); iterator.next(); **return** iterator; } });


## Related pages

- [[javascriptallonge-list]] - shared statements and technical atoms (1 shared statement(s), 6 shared atom(s))
- [[javascriptallonge-copy]] - shared statements and technical atoms (1 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-element]] - shared technical atoms (2 shared atom(s))
- [[javascriptallonge-function]] - shared technical atoms (1 shared atom(s))
- [[javascriptallonge-iterable]] - shared technical atoms (1 shared atom(s))
- [[javascriptallonge-length]] - shared technical atoms (1 shared atom(s))
- [[javascriptallonge-return]] - shared technical atoms (1 shared atom(s))
- [[javascriptallonge-program]] - shared statements (3 shared statement(s))
- [[javascriptallonge-javascript]] - shared statements (1 shared statement(s))
- [[javascriptallonge-literal]] - shared statements (1 shared statement(s))
- [[javascriptallonge-mapwith]] - shared statements (1 shared statement(s))

## Source

- [[javascriptallonge]]
