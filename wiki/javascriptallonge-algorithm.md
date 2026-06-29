---
page_id: javascriptallonge-algorithm
page_kind: concept
summary: Algorithm: 6 statement(s) and 2 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-algorithm@648925bede663a870c19e1f9e9e335fc
---

# Algorithm

What [[javascriptallonge]] covers about algorithm:

## Statements

### Tail Calls (and Default Arguments)

- Is there a better way? Yes. In fact, there are several better ways. Making algorithms faster is a very highly studied field of computer science. The one we're going to look at here is called tail-call optimization , or 'TCO.' _(javascriptallonge.pdf (source-range-8eb13d6b-00966))_

### Garbage, Garbage Everywhere

- Having these instructions be very fast was important to those early designers: They were working on one of the first high-level languages (COBOL and FORTRAN being the others), and computers in the late 1950s were extremely small and slow by today's standards. Although the 704 used core memory, it still used vacuum tubes for its logic. Thus, the design of programming languages and algorithms was driven by what could be accomplished with limited memory and performance. _(javascriptallonge.pdf (source-range-8eb13d6b-01033))_

### revisiting linked lists

- Mind you, this is still much, much faster than making partial copies of arrays. For a list of length n , wecreated n superfluous nodes and copied n superfluous values. Whereas our naïve array algorithm created 2 n superfluous arrays and copied n 2 superfluous values. _(javascriptallonge.pdf (source-range-8eb13d6b-01116))_

### building with mutation

- This algorithm makes copies of nodes as it goes, and mutates the last node in the list so that it can splice the next one on. Adding a node to an existing list is risky, as we saw when considering the fact that OneToFive and ThreeToFive share the same nodes. But when we're in the midst of creating a brand new list, we aren't sharing any nodes with any other lists, and we can afford to be more liberal about using mutation to save space and/or time. _(javascriptallonge.pdf (source-range-8eb13d6b-01156))_

### Tortoises, Hares, and Teleporting Turtles

- This algorithm is called 'The Tortoise and the Hare,' and was discovered by Robert Floyd in the 1960s. You have two node references, and one traverses the list at twice the speed of the other. No matter how large it is, you will eventually have the fast reference equal to the slow reference, and thus you'll detect the loop. _(javascriptallonge.pdf (source-range-8eb13d6b-01264))_

- What's interesting about these two algorithms is that they both tangle two separate concerns: How to traverse a data structure, and what to do with the elements that you encounter. In Functional Iterators, we'll investigate one pattern for separating these concerns. _(javascriptallonge.pdf (source-range-8eb13d6b-01268))_


## Technical atoms

### Technical frame 1: building with mutation

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01154))_

> If we want to make a copy of a linked list without iterating over it twice and making a copy we discard later, we can use mutation:

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01153))_

```
const reverse = (node, delayed = EMPTY) => node === EMPTY ? delayed : reverse(node.rest, { first: node.first, rest: delayed }); const copy = (node) => reverse(reverse(node));
```

### Technical frame 2: Tortoises, Hares, and Teleporting Turtles

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01267))_

> Years later, I came across a discussion of this algorithm, The Tale of the Teleporting Turtle 75 . It seems to be faster under certain circumstances, depending on the size of the loop and the relative costs of certain operations.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01266))_

```
const teleportingTurtle = (list) => { let speed = 1, rabbit = list, turtle = rabbit; while ( true ) { for ( let i = 0; i <= speed; i += 1) { rabbit = rabbit.rest; if (rabbit == null ) { return false ; } if (rabbit === turtle) { return true ; } } turtle = rabbit; speed *= 2; } return false ; }; const aList = list(1, 2, 3, 4, 5); teleportingTurtle(aList) //=> false forceAppend(aList, aList.rest.rest); teleportingTurtle(aList); //=> true
```


## Related pages

- [[javascriptallonge-copy]] - shared technical atoms: Copy shares technical record from building with mutation: const reverse = (node, delayed = EMPTY) => node === EMPTY ? delayed : reverse(node.rest, { first: node.first, rest: delayed }); const copy = (node) => reverse(reverse(node)); (1 shared atom(s))
- [[javascriptallonge-list]] - shared technical atoms: List shares technical record from building with mutation: const reverse = (node, delayed = EMPTY) => node === EMPTY ? delayed : reverse(node.rest, { first: node.first, rest: delayed }); const copy = (node) => reverse(reverse(node)); (1 shared atom(s))
- [[javascriptallonge-array]] - shared statements: Array shares source evidence from revisiting linked lists: Mind you, this is still much, much faster than making partial copies of arrays. For a list of length n , wecreated n superfluous nodes and copied n superfluous value ... [truncated] (1 shared statement(s))
- [[javascriptallonge-language]] - shared statements: Language shares source evidence from Garbage, Garbage Everywhere: Having these instructions be very fast was important to those early designers: They were working on one of the first high-level languages (COBOL and FORTRAN being th ... [truncated] (1 shared statement(s))
- [[javascriptallonge-program]] - shared statements: Program shares source evidence from Garbage, Garbage Everywhere: Having these instructions be very fast was important to those early designers: They were working on one of the first high-level languages (COBOL and FORTRAN being th ... [truncated] (1 shared statement(s))
- [[javascriptallonge-programming]] - shared statements: Programming shares source evidence from Garbage, Garbage Everywhere: Having these instructions be very fast was important to those early designers: They were working on one of the first high-level languages (COBOL and FORTRAN being th ... [truncated] (1 shared statement(s))

## Source

- [[javascriptallonge]]
