---
page_id: javascriptallonge-rest
page_kind: concept
page_family: topic-concept
summary: Rest: 9 statement(s) and 9 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-rest@fecef91c87b67f2aba993bccd6fac66d
---

# Rest

What [[javascriptallonge]] covers about rest:

## Statements

### Composing and Decomposing Data / Self-Similarity

- Thanks to the parallel between array literals + spreads with destructuring + rests, we can also use the same rules to decompose lists: _(javascriptallonge.pdf (source-range-7239e085-00892))_

### Composing and Decomposing Data / Tail Calls (and Default Arguments)

- Next, JavaScript invokes mapWith(fn, rest) , which is semantically equivalent to mapWith((x) => x * x, [2, 3, 4, 5]) . And the same thing happens: JavaScript has to hang on to 2 (or 4 , or both, depending on the implementation), plus some housekeeping information so it remembers what to do with that value, while it calls the equivalent of mapWith((x) => x * x, [3, 4, 5]) . _(javascriptallonge.pdf (source-range-7239e085-00961))_

### Composing and Decomposing Data / Garbage, Garbage Everywhere

- Key Point : Our [first, ...rest] approach to recursion is slow because that it creates a lot of temporary arrays, and it spends an enormous amount of time copying elements into arrays that end up being discarded. _(javascriptallonge.pdf (source-range-7239e085-01024))_

### Yes. Consider this variation: / Copy on Write

- When you take the rest of an array with destructuring ( [first, ...rest] ), you are given a copy of the elements of the array. _(javascriptallonge.pdf (source-range-7239e085-01226))_

- When you take the rest of a linked list with its reference, you are given the exact same nodes of the elements of the original list. _(javascriptallonge.pdf (source-range-7239e085-01227))_

### Yes. Consider this variation: / Copy on Write / copy-on-read

- So back to the problem of structure sharing. One strategy for avoiding problems is to be pessimistic . Whenever we take the rest of a list, make a copy. _(javascriptallonge.pdf (source-range-7239e085-01239))_

### We'll keep it simple: / generators are coroutines

- The rest of the program continues along its way until it makes another call to iterator.next() . _(javascriptallonge.pdf (source-range-7239e085-01686))_


## Technical atoms

### Technical frame 1: Composing and Decomposing Data / Self-Similarity

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00897))_

> Armed with our definition of an empty list and with what we've already learned, we can build a great many functions that operate on arrays. We know that we can get the length of an array using its .length . But as an exercise, how would we write a length function using just what we have already?

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00895))_

<a id="atom-technical-atom-ab90397824182d0e"></a>

```
const [first, ...rest] = [];
first
//=> undefined
rest
//=> []:
const [first, ...rest] = ["foo"];
first
//=> "foo"
rest
//=> []
const [first, ...rest] = ["foo", "bar"];
first
//=> "foo"
rest
//=> ["bar"]
const [first, ...rest] = ["foo", "bar", "baz"];
first
//=> "foo"
rest
//=> ["bar","baz"]
For the purpose of this exploration, we will presume the following:61
const isEmpty = ([first, ...rest]) => first === undefined;
```

### Technical frame 2: Composing and Decomposing Data / Tail Calls (and Default Arguments)

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00960))_

> Note that while evaluating mapWith(fn, rest) , JavaScript must retain the value first or fn(first) , plus some housekeeping information so it remembers what to do with mapWith(fn, rest) when it has a result. JavaScript cannot throw first away. So we know that JavaScript is going to hang on to 1 .

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00959))_

<a id="atom-technical-atom-f2ca5cb343939e2b"></a>

```
const mapWith = function (fn, [first, ...rest]) {
if (first === undefined) {
return [];
}
else {
const _temp1 = fn(first),
_temp2 = mapWith(fn, rest),
_temp3 = [_temp1, ..._temp2];
return _temp3;
}
}
```

### Technical frame 3: Composing and Decomposing Data / Tail Calls (and Default Arguments) / tail-call optimization

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00974))_

> The length function calls itself, but it is not a tail-call, because it returns 1 + length(rest) , not length(rest) .

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00973))_

<a id="atom-technical-atom-2634a0aa2029afd4"></a>

```
const length = ([first, ...rest]) =>
first === undefined
? 0
: 1 + length(rest);
```

### Technical frame 4: Composing and Decomposing Data / Garbage, Garbage Everywhere / some history

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01047))_

> Again, it's just extracting a reference from a cons cell, it's very fast. In Lisp, it's blazingly fast because it happens in hardware. There's no making copies of arrays, the time to cdr a list with five elements is the same as the time to cdr a list with 5,000 elements, and no temporary arrays are needed. In JavaScript, it's still much, much, much faster to get all the elements except the head from a linked list than from an array. Getting one reference to a structure that already exists is fas

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01046))_

<a id="atom-technical-atom-507de994e6577937"></a>

```
cdr(oneToFive)
//=> [2,[3,[4,[5,null]]]]
```

### Technical frame 5: Composing and Decomposing Data / Garbage, Garbage Everywhere / so why arrays

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01056))_

> We have avoided discussing rebinding and mutating values, but if we want to change elements of our lists, the naïve linked list implementation suffers as well: When we take the cdr of a linked list, we are sharing the elements. If we make any change other than cons-ing a new element to the front, we are changing both the new list and the old list.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01055))_

<a id="atom-technical-atom-a87d9f5009a86d7c"></a>

> And if you want an arbitrary item from a list, you have to iterate through the list element by element, whereas with the indexed array you just fetch it.

### Technical frame 6: Yes. Consider this variation: / Copy on Write

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01232))_

> This is remarkably unsafe. If we know that a list doesn't share any elements with another list, we can safely modify it. But how do we keep track of that? Add a bunch of bookkeeping to track references? We'll end up reinventing reference counting and garbage collection.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01228))_

<a id="atom-technical-atom-bba78c8b3994a437"></a>

> The consequence of this is that if you have an array, and you take it's 'rest,' your 'child' array is a copy of the elements of the parent array.

### Technical frame 7: Yes. Consider this variation: / Copy on Write

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01232))_

> This is remarkably unsafe. If we know that a list doesn't share any elements with another list, we can safely modify it. But how do we keep track of that? Add a bunch of bookkeeping to track references? We'll end up reinventing reference counting and garbage collection.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01229))_

<a id="atom-technical-atom-107209144ad81087"></a>

> Whereas if you have a linked list, and you take it's 'rest,' your 'child' list shares its nodes with the 'parent' list.

### Technical frame 8: Yes. Consider this variation: / Copy on Write / copy-on-read

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01241))_

> This strategy is called 'copy-on-read', because when we attempt the parent to 'read' the value of a child of the list, we make a copy and read the copy of the child. Thereafter, we can write to the parent or the copy of the child freely.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01240))_

<a id="atom-technical-atom-05e2937fc47dd397"></a>

```
const rest = ({first, rest}) => copy(rest);
const parentList = { first: 1, rest: { first: 2, rest: { first: 3, rest: EMPTY }\
}};
const childList = rest(parentList);
const newParentList = set(2, "three", parentList);
set(0, "two", childList);
parentList
//=> {"first":1,"rest":{"first":2,"rest":{"first":"three","rest":{"first":{},"\
rest":{}}}}}
childList
//=> {"first":"two","rest":{"first":3,"rest":{"first":{},"rest":{}}}}
```

### Technical frame 9: Yes. Consider this variation: / Copy on Write / copy-on-write

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01252))_

> This strategy of waiting to copy until you are writing is called copy-on-write, or 'COW:'

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01246))_

<a id="atom-technical-atom-e60d6ebf60601e8a"></a>

```
const rest = ({first, rest}) => rest;
const set = (index, value, list) =>
index === 0
? { first: value, rest: list.rest }
: { first: list.first, rest: set(index - 1, value, list.rest) };
const parentList = { first: 1, rest: { first: 2, rest: { first: 3, rest: EMPTY }\
}};
const childList = rest(parentList);
const newParentList = set(2, "three", parentList);
const newChildList = set(0, "two", childList);
```


## Related pages

### Shared technical atoms

- [[javascriptallonge-list]] - shared statements and technical atoms: List shares source evidence from Yes. Consider this variation: / Copy on Write / copy-on-read: So back to the problem of structure sharing. One strategy for avoiding problems is to be pessimistic . Whenever we take the rest of a list, make a copy.; List shares technical record from Composing and Decomposing Data / Self-Similarity: const [first, ...rest] = []; first //=> undefined rest //=> []: const [first, ...rest] = ["foo"]; first //=> "foo" rest //=> [] const [first, ...rest] = ["foo", "bar ... [truncated] (1 shared statement(s), 7 shared atom(s))
- [[javascriptallonge-copy-write]] - shared statements and technical atoms: Copy on Write shares source evidence from Yes. Consider this variation: / Copy on Write: When you take the rest of an array with destructuring ( [first, ...rest] ), you are given a copy of the elements of the array.; Copy on Write shares technical record from Yes. Consider this variation: / Copy on Write: The consequence of this is that if you have an array, and you take it's 'rest,' your 'child' array is a copy of the elements of the parent array. (3 shared statement(s), 4 shared atom(s))
- [[javascriptallonge-element]] - shared technical atoms: Element shares technical record from Composing and Decomposing Data / Garbage, Garbage Everywhere / some history: cdr(oneToFive) //=> [2,[3,[4,[5,null]]]] (3 shared atom(s))
- [[javascriptallonge-javascript]] - shared statements and technical atoms: Javascript shares source evidence from Composing and Decomposing Data / Tail Calls (and Default Arguments): Next, JavaScript invokes mapWith(fn, rest) , which is semantically equivalent to mapWith((x) => x * x, [2, 3, 4, 5]) . And the same thing happens: JavaScript has to ... [truncated]; Javascript shares technical record from Composing and Decomposing Data / Tail Calls (and Default Arguments): const mapWith = function (fn, [first, ...rest]) { if (first === undefined) { return []; } else { const _temp1 = fn(first), _temp2 = mapWith(fn, rest), _temp3 = [_tem ... [truncated] (1 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-copy]] - shared technical atoms: Copy shares technical record from Composing and Decomposing Data / Garbage, Garbage Everywhere / some history: cdr(oneToFive) //=> [2,[3,[4,[5,null]]]] (2 shared atom(s))
- [[javascriptallonge-literal]] - shared statements and technical atoms: Literal shares source evidence from Composing and Decomposing Data / Self-Similarity: Thanks to the parallel between array literals + spreads with destructuring + rests, we can also use the same rules to decompose lists:; Literal shares technical record from Composing and Decomposing Data / Self-Similarity: const [first, ...rest] = []; first //=> undefined rest //=> []: const [first, ...rest] = ["foo"]; first //=> "foo" rest //=> [] const [first, ...rest] = ["foo", "bar ... [truncated] (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-mapwith]] - shared statements and technical atoms: Mapwith shares source evidence from Composing and Decomposing Data / Tail Calls (and Default Arguments): Next, JavaScript invokes mapWith(fn, rest) , which is semantically equivalent to mapWith((x) => x * x, [2, 3, 4, 5]) . And the same thing happens: JavaScript has to ... [truncated]; Mapwith shares technical record from Composing and Decomposing Data / Tail Calls (and Default Arguments): const mapWith = function (fn, [first, ...rest]) { if (first === undefined) { return []; } else { const _temp1 = fn(first), _temp2 = mapWith(fn, rest), _temp3 = [_tem ... [truncated] (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-function]] - shared technical atoms: Function shares technical record from Composing and Decomposing Data / Tail Calls (and Default Arguments) / tail-call optimization: const length = ([first, ...rest]) => first === undefined ? 0 : 1 + length(rest); (1 shared atom(s))

## Source

- [[javascriptallonge]]
