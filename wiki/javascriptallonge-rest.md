---
page_id: javascriptallonge-rest
page_kind: concept
summary: Rest: 11 statement(s) and 7 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-rest@b46072187ff350da2af5b2ed19aefd50
---

# Rest

What [[javascriptallonge]] covers about rest:

## Statements

### Building Blocks

- When you look at functions within functions in JavaScript, there's a bit of a 'spaghetti code' look to it. The strength of JavaScript is that you can do anything. The weakness is that you will. There are ifs, fors, returns, everything thrown higgledy piggledy together. Although you needn't restrict yourself to a small number of simple patterns, it can be helpful to understand the patterns so that you can structure your code around some basic building blocks. _(javascriptallonge.pdf (source-range-31a4cf47-00581))_

### Self-Similarity

- Thanks to the parallel between array literals + spreads with destructuring + rests, we can also use the same rules to decompose lists: _(javascriptallonge.pdf (source-range-31a4cf47-00892))_

### Tail Calls (and Default Arguments)

- Next, JavaScript invokes mapWith(fn, rest) , which is semantically equivalent to mapWith((x) => x * x, [2, 3, 4, 5]) . And the same thing happens: JavaScript has to hang on to 2 (or 4 , or both, depending on the implementation), plus some housekeeping information so it remembers what to do with that value, while it calls the equivalent of mapWith((x) => x * x, [3, 4, 5]) . _(javascriptallonge.pdf (source-range-31a4cf47-00961))_

### Garbage, Garbage Everywhere

- Key Point : Our [first, ...rest] approach to recursion is slow because that it creates a lot of temporary arrays, and it spends an enormous amount of time copying elements into arrays that end up being discarded. _(javascriptallonge.pdf (source-range-31a4cf47-01024))_

### Copy on Write

- When you take the rest of an array with destructuring ( [first, ...rest] ), you are given a copy of the elements of the array. _(javascriptallonge.pdf (source-range-31a4cf47-01226))_

- When you take the rest of a linked list with its reference, you are given the exact same nodes of the elements of the original list. _(javascriptallonge.pdf (source-range-31a4cf47-01227))_

### copy-on-read

- So back to the problem of structure sharing. One strategy for avoiding problems is to be pessimistic . Whenever we take the rest of a list, make a copy. _(javascriptallonge.pdf (source-range-31a4cf47-01239))_

### operations on ordered collections

- like our other operations, rest preserves the ordered collection semantics of its argument. _(javascriptallonge.pdf (source-range-31a4cf47-01609))_

### generators are coroutines

- The rest of the program continues along its way until it makes another call to iterator.next() . _(javascriptallonge.pdf (source-range-31a4cf47-01687))_

- The rest of the program continues along its way until it makes another call to iterator.next() . _(javascriptallonge.pdf (source-range-31a4cf47-01692))_

- The rest of the program continues along its way until it makes another call to iterator.next() . _(javascriptallonge.pdf (source-range-31a4cf47-01697))_


## Technical atoms

### Technical frame 1: Self-Similarity

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00897))_

> Armed with our definition of an empty list and with what we've already learned, we can build a great many functions that operate on arrays. We know that we can get the length of an array using its .length . But as an exercise, how would we write a length function using just what we have already?

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00895))_

```
const [first, ...rest] = []; first //=> undefined rest //=> []: const [first, ...rest] = ["foo"]; first //=> "foo" rest //=> [] const [first, ...rest] = ["foo", "bar"]; first //=> "foo" rest //=> ["bar"] const [first, ...rest] = ["foo", "bar", "baz"]; first //=> "foo" rest //=> ["bar","baz"] For the purpose of this exploration, we will presume the following: const isEmpty = ([first, ...rest]) => first === undefined ;
```

### Technical frame 2: Tail Calls (and Default Arguments)

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00960))_

> Note that while evaluating mapWith(fn, rest) , JavaScript must retain the value first or fn(first) , plus some housekeeping information so it remembers what to do with mapWith(fn, rest) when it has a result. JavaScript cannot throw first away. So we know that JavaScript is going to hang on to 1 .

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00959))_

```
const mapWith = function (fn, [first, ...rest]) { if (first === undefined ) { return []; } else { const _temp1 = fn(first), _temp2 = mapWith(fn, rest), _temp3 = [_temp1, ..._temp2]; return _temp3; } }
```

### Technical frame 3: Garbage, Garbage Everywhere

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01046))_

> Again, it's just extracting a reference from a cons cell, it's very fast. In Lisp, it's blazingly fast because it happens in hardware. There's no making copies of arrays, the time to cdr a list with five elements is the same as the time to cdr a list with 5,000 elements, and no temporary arrays are needed. In JavaScript, it's still much, much, much faster to get all the elements except the head from a linked list than from an array. Getting one reference to a structure that already exists is fas

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01045))_

```
cdr(oneToFive) //=> [2,[3,[4,[5,null]]]]
```

### Technical frame 4: Copy on Write

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01232))_

> This is remarkably unsafe. If we know that a list doesn't share any elements with another list, we can safely modify it. But how do we keep track of that? Add a bunch of bookkeeping to track references? We'll end up reinventing reference counting and garbage collection.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01228))_

> The consequence of this is that if you have an array, and you take it's 'rest,' your 'child' array is a copy of the elements of the parent array.

### Technical frame 5: Copy on Write

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01232))_

> This is remarkably unsafe. If we know that a list doesn't share any elements with another list, we can safely modify it. But how do we keep track of that? Add a bunch of bookkeeping to track references? We'll end up reinventing reference counting and garbage collection.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01229))_

> Whereas if you have a linked list, and you take it's 'rest,' your 'child' list shares its nodes with the 'parent' list.

### Technical frame 6: copy-on-read

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01241))_

> This strategy is called 'copy-on-read', because when we attempt the parent to 'read' the value of a child of the list, we make a copy and read the copy of the child. Thereafter, we can write to the parent or the copy of the child freely.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01240))_

```
const rest = ({first, rest}) => copy(rest); const parentList = { first: 1, rest: { first: 2, rest: { first: 3, rest: EMPTY }\ }}; const childList = rest(parentList); const newParentList = set(2, "three", parentList); set(0, "two", childList); parentList //=> {"first":1,"rest":{"first":2,"rest":{"first":"three","rest":{"first":{},"\ rest":{}}}}} childList //=> {"first":"two","rest":{"first":3,"rest":{"first":{},"rest":{}}}}
```

### Technical frame 7: operations on ordered collections

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01609))_

> like our other operations, rest preserves the ordered collection semantics of its argument.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01608))_

```
const first = (iterable) => iterable[Symbol.iterator]().next().value; const rest = (iterable) => ({ [Symbol.iterator] () { const iterator = iterable[Symbol.iterator](); iterator.next(); return iterator; } });
```


## Related pages

- [[javascriptallonge-list]] - shared statements and technical atoms: List shares source evidence from copy-on-read: So back to the problem of structure sharing. One strategy for avoiding problems is to be pessimistic . Whenever we take the rest of a list, make a copy.; List shares technical record from Self-Similarity: const [first, ...rest] = []; first //=> undefined rest //=> []: const [first, ...rest] = ["foo"]; first //=> "foo" rest //=> [] const [first, ...rest] = ["foo", "bar ... [truncated] (1 shared statement(s), 5 shared atom(s))
- [[javascriptallonge-array]] - shared statements and technical atoms: Array shares source evidence from Self-Similarity: Thanks to the parallel between array literals + spreads with destructuring + rests, we can also use the same rules to decompose lists:; Array shares technical record from Self-Similarity: const [first, ...rest] = []; first //=> undefined rest //=> []: const [first, ...rest] = ["foo"]; first //=> "foo" rest //=> [] const [first, ...rest] = ["foo", "bar ... [truncated] (2 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-copy-write]] - shared statements and technical atoms: Copy on Write shares source evidence from Copy on Write: When you take the rest of an array with destructuring ( [first, ...rest] ), you are given a copy of the elements of the array.; Copy on Write shares technical record from Copy on Write: The consequence of this is that if you have an array, and you take it's 'rest,' your 'child' array is a copy of the elements of the parent array. (2 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-javascript]] - shared statements and technical atoms: Javascript shares source evidence from Tail Calls (and Default Arguments): Next, JavaScript invokes mapWith(fn, rest) , which is semantically equivalent to mapWith((x) => x * x, [2, 3, 4, 5]) . And the same thing happens: JavaScript has to ... [truncated]; Javascript shares technical record from Tail Calls (and Default Arguments): const mapWith = function (fn, [first, ...rest]) { if (first === undefined ) { return []; } else { const _temp1 = fn(first), _temp2 = mapWith(fn, rest), _temp3 = [_te ... [truncated] (1 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-literal]] - shared statements and technical atoms: Literal shares source evidence from Self-Similarity: Thanks to the parallel between array literals + spreads with destructuring + rests, we can also use the same rules to decompose lists:; Literal shares technical record from Self-Similarity: const [first, ...rest] = []; first //=> undefined rest //=> []: const [first, ...rest] = ["foo"]; first //=> "foo" rest //=> [] const [first, ...rest] = ["foo", "bar ... [truncated] (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-mapwith]] - shared statements and technical atoms: Mapwith shares source evidence from Tail Calls (and Default Arguments): Next, JavaScript invokes mapWith(fn, rest) , which is semantically equivalent to mapWith((x) => x * x, [2, 3, 4, 5]) . And the same thing happens: JavaScript has to ... [truncated]; Mapwith shares technical record from Tail Calls (and Default Arguments): const mapWith = function (fn, [first, ...rest]) { if (first === undefined ) { return []; } else { const _temp1 = fn(first), _temp2 = mapWith(fn, rest), _temp3 = [_te ... [truncated] (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-element]] - shared technical atoms: Element shares technical record from Garbage, Garbage Everywhere: cdr(oneToFive) //=> [2,[3,[4,[5,null]]]] (4 shared atom(s))
- [[javascriptallonge-copy]] - shared technical atoms: Copy shares technical record from Garbage, Garbage Everywhere: cdr(oneToFive) //=> [2,[3,[4,[5,null]]]] (1 shared atom(s))
- [[javascriptallonge-problem]] - shared technical atoms: Problem shares technical record from copy-on-read: const rest = ({first, rest}) => copy(rest); const parentList = { first: 1, rest: { first: 2, rest: { first: 3, rest: EMPTY }\ }}; const childList = rest(parentList); ... [truncated] (1 shared atom(s))
- [[javascriptallonge-reference]] - shared technical atoms: Reference shares technical record from Garbage, Garbage Everywhere: cdr(oneToFive) //=> [2,[3,[4,[5,null]]]] (1 shared atom(s))
- [[javascriptallonge-return]] - shared technical atoms: Return shares technical record from operations on ordered collections: const first = (iterable) => iterable[Symbol.iterator]().next().value; const rest = (iterable) => ({ [Symbol.iterator] () { const iterator = iterable[Symbol.iterator] ... [truncated] (1 shared atom(s))
- [[javascriptallonge-rule]] - shared technical atoms: Rule shares technical record from Self-Similarity: const [first, ...rest] = []; first //=> undefined rest //=> []: const [first, ...rest] = ["foo"]; first //=> "foo" rest //=> [] const [first, ...rest] = ["foo", "bar ... [truncated] (1 shared atom(s))
- [[javascriptallonge-program]] - shared statements: Program shares source evidence from generators are coroutines: The rest of the program continues along its way until it makes another call to iterator.next() . (3 shared statement(s))
- [[javascriptallonge-needn]] - shared statements: Needn shares source evidence from Building Blocks: When you look at functions within functions in JavaScript, there's a bit of a 'spaghetti code' look to it. The strength of JavaScript is that you can do anything. Th ... [truncated] (1 shared statement(s))
- [[javascriptallonge-operation]] - shared statements: Operation shares source evidence from operations on ordered collections: like our other operations, rest preserves the ordered collection semantics of its argument. (1 shared statement(s))
- [[javascriptallonge-pattern]] - shared statements: Pattern shares source evidence from Building Blocks: When you look at functions within functions in JavaScript, there's a bit of a 'spaghetti code' look to it. The strength of JavaScript is that you can do anything. Th ... [truncated] (1 shared statement(s))

## Source

- [[javascriptallonge]]
