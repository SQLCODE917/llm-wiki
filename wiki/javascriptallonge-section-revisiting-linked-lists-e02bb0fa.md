---
page_id: javascriptallonge-section-revisiting-linked-lists-e02bb0fa
page_kind: source
summary: revisiting linked lists: 21 source-backed entries and 6 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-revisiting-linked-lists-e02bb0fa@25eab6b61ad0e4b7134cbbdf4bca5c5b
---

# revisiting linked lists

From [[javascriptallonge]].

## Statements

- In essence, this simple implementation used functions to create an abstraction with named elements. But now that we've looked at objects, we can use an object instead of a two-element array. While we're at it, let's use contemporary names. So our linked list nodes will be formed from { first, rest } _(javascriptallonge.pdf (source-range-8eb13d6b-01105))_
- What about mapping? Well, let's start with the simplest possible thing, making a copy of a list. As we saw above, and discussed in Garbage, Garbage Everywhere, it is fast to iterate forward through a linked list. What isn't fast is naïvely copying a list: _(javascriptallonge.pdf (source-range-8eb13d6b-01108))_
- The problem here is that linked lists are constructed back-to-front, but we iterate over them frontto-back. So to copy a list, we have to save all the bits on the call stack and then construct the list from back-to-front as all the recursive calls return. _(javascriptallonge.pdf (source-range-8eb13d6b-01110))_
- We could follow the strategy of delaying the work. Let's write that naively: _(javascriptallonge.pdf (source-range-8eb13d6b-01111))_
- Well, well, well. We have unwittingly reversed the list. This makes sense, if lists are constructed from back to front, and we make a linked list out of items as we iterate through it, we're going to get a backwards copy of the list. This isn't a bad thing by any stretch of the imagination. Let's call it what it is: _(javascriptallonge.pdf (source-range-8eb13d6b-01113))_
- Our mapWith function takes twice as long as a straight iteration, because it iterates over the entire list twice, once to map, and once to reverse the list. Likewise, it takes twice as much memory, because it constructs a reverse of the desired result before throwing it away. _(javascriptallonge.pdf (source-range-8eb13d6b-01115))_
- Mind you, this is still much, much faster than making partial copies of arrays. For a list of length n , wecreated n superfluous nodes and copied n superfluous values. Whereas our naïve array algorithm created 2 n superfluous arrays and copied n 2 superfluous values. _(javascriptallonge.pdf (source-range-8eb13d6b-01116))_
- So to copy a list, we have to save all the bits on the call stack and then construct the list from back-to-front as all the recursive calls return. _(javascriptallonge.pdf (source-range-8eb13d6b-01110))_
- Likewise, it takes twice as much memory, because it constructs a reverse of the desired result before throwing it away. _(javascriptallonge.pdf (source-range-8eb13d6b-01115))_
- Whereas our naïve array algorithm created 2 n superfluous arrays and copied n 2 superfluous values. _(javascriptallonge.pdf (source-range-8eb13d6b-01116))_

## Technical atoms

### Technical frame 1: revisiting linked lists

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01105))_

> In essence, this simple implementation used functions to create an abstraction with named elements. But now that we've looked at objects, we can use an object instead of a two-element array. While we're at it, let's use contemporary names. So our linked list nodes will be formed from { first, rest }

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01104))_

```
const cons = (a, d) => [a, d], car = ([a, d]) => a, cdr = ([a, d]) => d;
```

### Technical frame 2: revisiting linked lists

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01108))_

> What about mapping? Well, let's start with the simplest possible thing, making a copy of a list. As we saw above, and discussed in Garbage, Garbage Everywhere, it is fast to iterate forward through a linked list. What isn't fast is naïvely copying a list:

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01106))_

```
In that case, a linked list of the numbers 1 , 2 , and 3 will look like this: { first: 1, rest: { first: 2, rest: { first: 3, rest: EMPTY } } } . We can then perform the equivalent of [first, ...rest] with direct property accessors:
```

### Technical frame 3: revisiting linked lists

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01108))_

> What about mapping? Well, let's start with the simplest possible thing, making a copy of a list. As we saw above, and discussed in Garbage, Garbage Everywhere, it is fast to iterate forward through a linked list. What isn't fast is naïvely copying a list:

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01107))_

```
const EMPTY = {}; const OneTwoThree = { first: 1, rest: { first: 2, rest: { first: 3, rest: EMPTY \ } } }; OneTwoThree.first //=> 1 OneTwoThree.rest //=> {"first":2,"rest":{"first":3,"rest":{}}} OneTwoThree.rest.rest.first //=> 3 Taking the length of a linked list is easy: const length = (node, delayed = 0) => node === EMPTY ? delayed : length(node.rest, delayed + 1); length(OneTwoThree) //=> 3
```

### Technical frame 4: revisiting linked lists

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01110))_

> The problem here is that linked lists are constructed back-to-front, but we iterate over them frontto-back. So to copy a list, we have to save all the bits on the call stack and then construct the list from back-to-front as all the recursive calls return.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01109))_

```
const slowcopy = (node) => node === EMPTY ? EMPTY : { first: node.first, rest: slowcopy(node.rest)}; slowcopy(OneTwoThree) //=> {"first":1,"rest":{"first":2,"rest":{"first":3,"rest":{}}}}
```

### Technical frame 5: revisiting linked lists

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01113))_

> Well, well, well. We have unwittingly reversed the list. This makes sense, if lists are constructed from back to front, and we make a linked list out of items as we iterate through it, we're going to get a backwards copy of the list. This isn't a bad thing by any stretch of the imagination. Let's call it what it is:

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01112))_

```
const copy2 = (node, delayed = EMPTY) => node === EMPTY ? delayed : copy2(node.rest, { first: node.first, rest: delayed }); copy2(OneTwoThree) //=> {"first":3,"rest":{"first":2,"rest":{"first":1,"rest":{}}}}
```

### Technical frame 6: revisiting linked lists

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01115))_

> Our mapWith function takes twice as long as a straight iteration, because it iterates over the entire list twice, once to map, and once to reverse the list. Likewise, it takes twice as much memory, because it constructs a reverse of the desired result before throwing it away.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01114))_

```
const reverse = (node, delayed = EMPTY) => node === EMPTY ? delayed : reverse(node.rest, { first: node.first, rest: delayed }); And now, we can make a reversing map: const reverseMapWith = (fn, node, delayed = EMPTY) => node === EMPTY ? delayed : reverseMapWith(fn, node.rest, { first: fn(node.first), rest: delayed }); reverseMapWith((x) => x * x, OneTwoThree) //=> {"first":9,"rest":{"first":4,"rest":{"first":1,"rest":{}}}} And a regular mapWith follows: const reverse = (node, delayed = EMPTY) => node === EMPTY ? delayed : reverse(node.rest, { first: node.first, rest: delayed }); const mapWith = (fn, node, delayed = EMPTY) => node === EMPTY ? reverse(delayed) : mapWith(fn, node.rest, { first: fn(node.first), rest: delayed }); mapWith((x) => x * x, OneTwoThree) //=> {"first":1,"rest":{"first":4,"rest":{"first":9,"rest":{}}}}
```
