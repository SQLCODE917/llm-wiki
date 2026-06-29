---
page_id: javascriptallonge-copy
page_kind: concept
summary: Copy: 8 statement(s) and 11 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-copy@b7adf47bcb8a08ce0ca7cbdf6ad314e7
---

# Copy

What [[javascriptallonge]] covers about copy:

## Statements

### michael fogus

- As a life-long bibliophile and long-time follower of Reg's online work, I was excited when he started writing books. However, I'm very conservative about books - let's just say that if there was an aftershave scented to the essence of 'Used Book Store' then I would be first in line to buy. So as you might imagine I was 'skeptical' about the decision to release JavaScript Allongé as an ongoing ebook, with a pay-what-you-want model. However, Reg sent me a copy of his book and I was humbled. Not only was this a great book, but it was also a great way to write and distribute books. Having written books myself, I know the pain of soliciting and receiving feedback. _(javascriptallonge.pdf (source-range-8eb13d6b-00084))_

### Garbage, Garbage Everywhere

- The array we had in prepend is no longer used. In GC environments, it is marked as no longer being used, and eventually the garbage collector recycles the memory it is using. Lather, rinse, repeat: Ever time we call mapWith , we're creating a new array, copying all the elements from prepend into the new array, and then we no longer use prepend . _(javascriptallonge.pdf (source-range-8eb13d6b-01022))_

### so why arrays

- Arrays avoid this problem by pessimistically copying all the references whenever we extract an element or sequence of elements from them (We'll see this explained later in Mutation). _(javascriptallonge.pdf (source-range-8eb13d6b-01056))_

### revisiting linked lists

- The problem here is that linked lists are constructed back-to-front, but we iterate over them frontto-back. So to copy a list, we have to save all the bits on the call stack and then construct the list from back-to-front as all the recursive calls return. _(javascriptallonge.pdf (source-range-8eb13d6b-01110))_

### building with mutation

- As noted, one pattern is to be more liberal about mutation when building a data structure. Consider our copy algorithm. Without mutation, a copy of a linked list can be made in constant space by reversing a reverse of the list: _(javascriptallonge.pdf (source-range-8eb13d6b-01152))_

### copy-on-write

- This strategy of waiting to copy until you are writing is called copy-on-write, or 'COW:' _(javascriptallonge.pdf (source-range-8eb13d6b-01251))_

- Copy-on-write is the name given to the policy that whenever a task attempts to make a change to the shared information, it should first create a separate (private) copy of that information to prevent its changes from becoming visible to all the other tasks.Wikipedia 73 _(javascriptallonge.pdf (source-range-8eb13d6b-01252))_

- Looking at the code again, you see that the copy function doesn't copy on write: It follows the pattern that while constructing something, we own it and can be liberal with mutation. Once we're done with it and give it to someone else, we need to be conservative and use a strategy like copy-on-read or copy-on-write. _(javascriptallonge.pdf (source-range-8eb13d6b-01254))_


## Technical atoms

### Technical frame 1: Garbage, Garbage Everywhere

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01046))_

> Again, it's just extracting a reference from a cons cell, it's very fast. In Lisp, it's blazingly fast because it happens in hardware. There's no making copies of arrays, the time to cdr a list with five elements is the same as the time to cdr a list with 5,000 elements, and no temporary arrays are needed. In JavaScript, it's still much, much, much faster to get all the elements except the head from a linked list than from an array. Getting one reference to a structure that already exists is fas

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01045))_

```
cdr(oneToFive) //=> [2,[3,[4,[5,null]]]]
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

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01115))_

> Our mapWith function takes twice as long as a straight iteration, because it iterates over the entire list twice, once to map, and once to reverse the list. Likewise, it takes twice as much memory, because it constructs a reverse of the desired result before throwing it away.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01114))_

```
const reverse = (node, delayed = EMPTY) => node === EMPTY ? delayed : reverse(node.rest, { first: node.first, rest: delayed }); And now, we can make a reversing map: const reverseMapWith = (fn, node, delayed = EMPTY) => node === EMPTY ? delayed : reverseMapWith(fn, node.rest, { first: fn(node.first), rest: delayed }); reverseMapWith((x) => x * x, OneTwoThree) //=> {"first":9,"rest":{"first":4,"rest":{"first":1,"rest":{}}}} And a regular mapWith follows: const reverse = (node, delayed = EMPTY) => node === EMPTY ? delayed : reverse(node.rest, { first: node.first, rest: delayed }); const mapWith = (fn, node, delayed = EMPTY) => node === EMPTY ? reverse(delayed) : mapWith(fn, node.rest, { first: fn(node.first), rest: delayed }); mapWith((x) => x * x, OneTwoThree) //=> {"first":1,"rest":{"first":4,"rest":{"first":9,"rest":{}}}}
```

### Technical frame 6: building with mutation

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01154))_

> If we want to make a copy of a linked list without iterating over it twice and making a copy we discard later, we can use mutation:

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01153))_

```
const reverse = (node, delayed = EMPTY) => node === EMPTY ? delayed : reverse(node.rest, { first: node.first, rest: delayed }); const copy = (node) => reverse(reverse(node));
```

### Technical frame 7: building with mutation

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01156))_

> This algorithm makes copies of nodes as it goes, and mutates the last node in the list so that it can splice the next one on. Adding a node to an existing list is risky, as we saw when considering the fact that OneToFive and ThreeToFive share the same nodes. But when we're in the midst of creating a brand new list, we aren't sharing any nodes with any other lists, and we can afford to be more liberal about using mutation to save space and/or time.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01155))_

```
const copy = (node, head = null , tail = null ) => { if (node === EMPTY) { return head; } else if (tail === null ) { const { first, rest } = node; const newNode = { first, rest }; return copy(rest, newNode, newNode); } else { const { first, rest } = node; const newNode = { first, rest }; tail.rest = newNode; return copy(node.rest, head, newNode); } }
```

### Technical frame 8: building with mutation

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01156))_

> This algorithm makes copies of nodes as it goes, and mutates the last node in the list so that it can splice the next one on. Adding a node to an existing list is risky, as we saw when considering the fact that OneToFive and ThreeToFive share the same nodes. But when we're in the midst of creating a brand new list, we aren't sharing any nodes with any other lists, and we can afford to be more liberal about using mutation to save space and/or time.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01158))_

```
const mapWith = (fn, node, head = null , tail = null ) => { if (node === EMPTY) { return head; } else if (tail === null ) { const { first, rest } = node; const newNode = { first: fn(first), rest }; return mapWith(fn, rest, newNode, newNode); } else { const { first, rest } = node; const newNode = { first: fn(first), rest }; tail.rest = newNode; return mapWith(fn, node.rest, head, newNode); } } mapWith((x) => 1.0 / x, OneToFive)
```

### Technical frame 9: building with mutation

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01156))_

> This algorithm makes copies of nodes as it goes, and mutates the last node in the list so that it can splice the next one on. Adding a node to an existing list is risky, as we saw when considering the fact that OneToFive and ThreeToFive share the same nodes. But when we're in the midst of creating a brand new list, we aren't sharing any nodes with any other lists, and we can afford to be more liberal about using mutation to save space and/or time.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01159))_

```
//=> {"first":1,"rest":{"first":0.5,"rest":{"first":0.3333333333333333,"rest":\ {"first":0.25,"rest":{"first":0.2,"rest":{}}}}}}
```

### Technical frame 10: copy-on-write

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01248))_

> But our new parent and child lists are copies that contain the desired modifications, without interfering with each other:

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01245))_

```
const rest = ({first, rest}) => rest; const set = (index, value, list) => index === 0 ? { first: value, rest: list.rest } : { first: list.first, rest: set(index - 1, value, list.rest) }; const parentList = { first: 1, rest: { first: 2, rest: { first: 3, rest: EMPTY }\ }}; const childList = rest(parentList); const newParentList = set(2, "three", parentList); const newChildList = set(0, "two", childList);
```

### Technical frame 11: copy-on-write

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01250))_

> And now functions like mapWith that make copies without modifying anything, work at full speed.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01249))_

```
newParentList //=> {"first":1,"rest":{"first":2,"rest":{"first":"three","rest":{"first":{},"\ rest":{}}}}} newChildList //=> {"first":"two","rest":{"first":3,"rest":{"first":{},"rest":{}}}}
```


## Related pages

- [[javascriptallonge-copy-write]] - narrower topic: Copy on Write shares source evidence from copy-on-write: This strategy of waiting to copy until you are writing is called copy-on-write, or 'COW:'; Copy on Write shares technical record from copy-on-write: const rest = ({first, rest}) => rest; const set = (index, value, list) => index === 0 ? { first: value, rest: list.rest } : { first: list.first, rest: set(index - 1, ... [truncated] (3 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-list]] - shared statements and technical atoms: List shares source evidence from revisiting linked lists: The problem here is that linked lists are constructed back-to-front, but we iterate over them frontto-back. So to copy a list, we have to save all the bits on the ca ... [truncated]; List shares technical record from Garbage, Garbage Everywhere: cdr(oneToFive) //=> [2,[3,[4,[5,null]]]] (1 shared statement(s), 9 shared atom(s))
- [[javascriptallonge-array]] - shared statements and technical atoms: Array shares source evidence from Garbage, Garbage Everywhere: The array we had in prepend is no longer used. In GC environments, it is marked as no longer being used, and eventually the garbage collector recycles the memory it ... [truncated]; Array shares technical record from Garbage, Garbage Everywhere: cdr(oneToFive) //=> [2,[3,[4,[5,null]]]] (2 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-element]] - shared statements and technical atoms: Element shares source evidence from Garbage, Garbage Everywhere: The array we had in prepend is no longer used. In GC environments, it is marked as no longer being used, and eventually the garbage collector recycles the memory it ... [truncated]; Element shares technical record from Garbage, Garbage Everywhere: cdr(oneToFive) //=> [2,[3,[4,[5,null]]]] (2 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-reference]] - shared statements and technical atoms: Reference shares source evidence from so why arrays: Arrays avoid this problem by pessimistically copying all the references whenever we extract an element or sequence of elements from them (We'll see this explained la ... [truncated]; Reference shares technical record from Garbage, Garbage Everywhere: cdr(oneToFive) //=> [2,[3,[4,[5,null]]]] (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-algorithm]] - shared technical atoms: Algorithm shares technical record from building with mutation: const reverse = (node, delayed = EMPTY) => node === EMPTY ? delayed : reverse(node.rest, { first: node.first, rest: delayed }); const copy = (node) => reverse(reverse(node)); (1 shared atom(s))
- [[javascriptallonge-javascript]] - shared technical atoms: Javascript shares technical record from Garbage, Garbage Everywhere: cdr(oneToFive) //=> [2,[3,[4,[5,null]]]] (1 shared atom(s))
- [[javascriptallonge-rest]] - shared technical atoms: Rest shares technical record from Garbage, Garbage Everywhere: cdr(oneToFive) //=> [2,[3,[4,[5,null]]]] (1 shared atom(s))
- [[javascriptallonge-write]] - shared statements: Write shares source evidence from copy-on-write: Copy-on-write is the name given to the policy that whenever a task attempts to make a change to the shared information, it should first create a separate (private) c ... [truncated] (2 shared statement(s))
- [[javascriptallonge-code]] - shared statements: Code shares source evidence from copy-on-write: Looking at the code again, you see that the copy function doesn't copy on write: It follows the pattern that while constructing something, we own it and can be liber ... [truncated] (1 shared statement(s))
- [[javascriptallonge-follow]] - shared statements: Follow shares source evidence from copy-on-write: Looking at the code again, you see that the copy function doesn't copy on write: It follows the pattern that while constructing something, we own it and can be liber ... [truncated] (1 shared statement(s))
- [[javascriptallonge-function]] - shared statements: Function shares source evidence from copy-on-write: Looking at the code again, you see that the copy function doesn't copy on write: It follows the pattern that while constructing something, we own it and can be liber ... [truncated] (1 shared statement(s))
- [[javascriptallonge-mapwith]] - shared statements: Mapwith shares source evidence from Garbage, Garbage Everywhere: The array we had in prepend is no longer used. In GC environments, it is marked as no longer being used, and eventually the garbage collector recycles the memory it ... [truncated] (1 shared statement(s))
- [[javascriptallonge-pattern]] - shared statements: Pattern shares source evidence from copy-on-write: Looking at the code again, you see that the copy function doesn't copy on write: It follows the pattern that while constructing something, we own it and can be liber ... [truncated] (1 shared statement(s))
- [[javascriptallonge-problem]] - shared statements: Problem shares source evidence from so why arrays: Arrays avoid this problem by pessimistically copying all the references whenever we extract an element or sequence of elements from them (We'll see this explained la ... [truncated] (1 shared statement(s))

## Source

- [[javascriptallonge]]
