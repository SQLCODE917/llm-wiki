---
page_id: javascriptallonge-problem
page_kind: concept
summary: Problem: 9 statement(s) and 4 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-29
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-problem@01c73396b9c197a871b193cbae482dce
---

# Problem

What [[javascriptallonge]] covers about problem:

## Statements

### Recipes with Basic Functions / Maybe

- A common problem in programming is checking for null or undefined (hereafter called 'nothing,' while all other values including 0 , [] and false will be called 'something'). Languages like JavaScript do not strongly enforce the notion that a particular variable or particular property be something, so programs are often written to account for values that may be nothing. _(javascriptallonge.pdf (source-range-7239e085-00695))_

### Composing and Decomposing Data / Self-Similarity / linear recursion

- When all small problems have been solved, compose the solutions into one big solution _(javascriptallonge.pdf (source-range-7239e085-00914))_

- Once again, the solution directly displays the important elements: Dividing a problem into subproblems, detecting terminal cases, solving the terminal cases, and composing a solution from the solved portions. _(javascriptallonge.pdf (source-range-7239e085-00923))_

### Composing and Decomposing Data / Self-Similarity / mapping

- Another common problem is applying a function to every element of an array. JavaScript has a built-in function for this, but let's write our own using linear recursion. _(javascriptallonge.pdf (source-range-7239e085-00925))_

### Composing and Decomposing Data / Garbage, Garbage Everywhere / so why arrays

- Arrays avoid this problem by pessimistically copying all the references whenever we extract an element or sequence of elements from them (We'll see this explained later in Mutation). _(javascriptallonge.pdf (source-range-7239e085-01057))_

### Composing and Decomposing Data / Plain Old JavaScript Objects / revisiting linked lists

- The problem here is that linked lists are constructed back-to-front, but we iterate over them frontto-back. So to copy a list, we have to save all the bits on the call stack and then construct the list from back-to-front as all the recursive calls return. _(javascriptallonge.pdf (source-range-7239e085-01111))_

### Yes. Consider this variation: / Copy on Write / copy-on-read

- So back to the problem of structure sharing. One strategy for avoiding problems is to be pessimistic . Whenever we take the rest of a list, make a copy. _(javascriptallonge.pdf (source-range-7239e085-01239))_

### We'll keep it simple: / Interlude: The Carpenter Interviews for a Job / the problem

- The problem is this: The game board is hidden from us. A player moves the chequer, following the rules. As the player moves the chequer, they calls out the direction of movement, e.g. '↑, →, ↑, ↓, ↑, →…' Write an algorithm that will determine whether the game halts, strictly from the called out directions, in finite time and space. _(javascriptallonge.pdf (source-range-7239e085-01819))_

### We'll keep it simple: / Interlude: The Carpenter Interviews for a Job / after another drink

- 'The hasCycle function, a/k/a Tortoise and Hare, requires two separate iterators to do its job. Whereas the problem as stated involves a single stream of directions. You're essentially calling for the player to clone themselves and call out the directions in parallel.' _(javascriptallonge.pdf (source-range-7239e085-01866))_


## Technical atoms

### Technical frame 1: Composing and Decomposing Data / Self-Similarity / linear recursion

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00919))_

> The usual 'terminal case' will be that flattening an empty array will produce an empty array. The next terminal case is that if an element isn't an array, we don't flatten it, and can put it together with the rest of our solution directly. Whereas if an element is an array, we'll flatten it and put it together with the rest of our solution.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00918))_

```
Array.isArray("foo")
//=> false
Array.isArray(["foo"])
//=> true
```

### Technical frame 2: Yes. Consider this variation: / Copy on Write / copy-on-read

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01241))_

> This strategy is called 'copy-on-read', because when we attempt the parent to 'read' the value of a child of the list, we make a copy and read the copy of the child. Thereafter, we can write to the parent or the copy of the child freely.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01240))_

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

### Technical frame 3: We'll keep it simple: / Interlude: The Carpenter Interviews for a Job / the problem

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01819))_

> The problem is this: The game board is hidden from us. A player moves the chequer, following the rules. As the player moves the chequer, they calls out the direction of movement, e.g. '↑, →, ↑, ↓, ↑, →…' Write an algorithm that will determine whether the game halts, strictly from the called out directions, in finite time and space.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01821))_

> You may use babeljs.io 95 , or ES6Fiddle 96 to check your work.

### Technical atom 4

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01823))_

> Christine quickly scribbled on the whiteboard:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01825))_

| entry | content |
| --- | --- |
| 95 | http://babeljs.io |
| 96 | http://www.es6fiddle.net |

<details>
<summary>Raw table text</summary>

```
95 http://babeljs.io
96 http://www.es6fiddle.net
```

</details>


## Related pages

- [[javascriptallonge-copy-write]] - shared statements and technical atoms: Copy on Write shares source evidence from Yes. Consider this variation: / Copy on Write / copy-on-read: So back to the problem of structure sharing. One strategy for avoiding problems is to be pessimistic . Whenever we take the rest of a list, make a copy.; Copy on Write shares technical record from Yes. Consider this variation: / Copy on Write / copy-on-read: const rest = ({first, rest}) => copy(rest); const parentList = { first: 1, rest: { first: 2, rest: { first: 3, rest: EMPTY }\ }}; const childList = rest(parentList); ... [truncated] (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-carpenter]] - shared technical atoms: Carpenter shares technical table: 95 http://babeljs.io 96 http://www.es6fiddle.net (1 shared atom(s))
- [[javascriptallonge-list]] - shared technical atoms: List shares technical record from Yes. Consider this variation: / Copy on Write / copy-on-read: const rest = ({first, rest}) => copy(rest); const parentList = { first: 1, rest: { first: 2, rest: { first: 3, rest: EMPTY }\ }}; const childList = rest(parentList); ... [truncated] (1 shared atom(s))
- [[javascriptallonge-rest]] - shared technical atoms: Rest shares technical record from Yes. Consider this variation: / Copy on Write / copy-on-read: const rest = ({first, rest}) => copy(rest); const parentList = { first: 1, rest: { first: 2, rest: { first: 3, rest: EMPTY }\ }}; const childList = rest(parentList); ... [truncated] (1 shared atom(s))
- [[javascriptallonge-write]] - shared technical atoms: Write shares technical record from We'll keep it simple: / Interlude: The Carpenter Interviews for a Job / the problem: You may use babeljs.io 95 , or ES6Fiddle 96 to check your work. (1 shared atom(s))
- [[javascriptallonge-element]] - shared statements: Element shares source evidence from Composing and Decomposing Data / Self-Similarity / linear recursion: Once again, the solution directly displays the important elements: Dividing a problem into subproblems, detecting terminal cases, solving the terminal cases, and com ... [truncated] (2 shared statement(s))
- [[javascriptallonge-copy]] - shared statements: Copy shares source evidence from Composing and Decomposing Data / Garbage, Garbage Everywhere / so why arrays: Arrays avoid this problem by pessimistically copying all the references whenever we extract an element or sequence of elements from them (We'll see this explained la ... [truncated] (1 shared statement(s))
- [[javascriptallonge-important]] - shared statements: Important shares source evidence from Composing and Decomposing Data / Self-Similarity / linear recursion: Once again, the solution directly displays the important elements: Dividing a problem into subproblems, detecting terminal cases, solving the terminal cases, and com ... [truncated] (1 shared statement(s))
- [[javascriptallonge-program]] - shared statements: Program shares source evidence from Recipes with Basic Functions / Maybe: A common problem in programming is checking for null or undefined (hereafter called 'nothing,' while all other values including 0 , [] and false will be called 'some ... [truncated] (1 shared statement(s))
- [[javascriptallonge-programming]] - shared statements: Programming shares source evidence from Recipes with Basic Functions / Maybe: A common problem in programming is checking for null or undefined (hereafter called 'nothing,' while all other values including 0 , [] and false will be called 'some ... [truncated] (1 shared statement(s))
- [[javascriptallonge-reference]] - shared statements: Reference shares source evidence from Composing and Decomposing Data / Garbage, Garbage Everywhere / so why arrays: Arrays avoid this problem by pessimistically copying all the references whenever we extract an element or sequence of elements from them (We'll see this explained la ... [truncated] (1 shared statement(s))
- [[javascriptallonge-section-we-ll-keep-it-simple-interlude-the-carpenter-interviews-for-a-job-the-problem-69f83674]] - source section: We'll keep it simple: / Interlude: The Carpenter Interviews for a Job / the problem shares source evidence from We'll keep it simple: / Interlude: The Carpenter Interviews for a Job / the problem: After some small talk, Christine explained that they liked to ask candidates to whiteboard some code. Despite his experience and industry longevity, the Carpenter di ... [truncated]; We'll keep it simple: / Interlude: The Carpenter Interviews for a Job / the problem shares technical record from We'll keep it simple: / Interlude: The Carpenter Interviews for a Job / the problem: If the arrow should cause the chequer to move off the edge of the board, the game halts. (7 shared statement(s), 4 shared atom(s))

## Source

- [[javascriptallonge]]
