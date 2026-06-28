---
page_id: javascriptallonge-write
page_kind: concept
summary: Write: 11 statement(s) and 10 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-write@bbdef2636ab693cd27e61c530baf9f4b
---

# Write

What [[javascriptallonge]] covers about write:

## Statements

- If we write a program with the presumption that “everything is an object,” we can write maps, folds, and filters that work on objects. _(javascriptallonge.pdf (source-range-83ecb080-02393))_
- Some programmers argue that since it’s part of the language’s definition, it’s fair game to write code that exploits it, so they deliberately omit any semicolon that JavaScript will insert for them. _(javascriptallonge.pdf (source-range-83ecb080-00358))_
- Another way to write our “circumference” function would be to pass PI along with the diameter argument, something like this: _(javascriptallonge.pdf (source-range-83ecb080-00582))_
- before we go any further, let’s write a few naïve list utilities so that we can work at a slightly higher level of abstraction: _(javascriptallonge.pdf (source-range-83ecb080-01865))_
- Copy-on-write is the name given to the policy that whenever a task attempts to make a change to the shared information, it should first create a separate (private) copy of that information to prevent its changes from becoming visible to all the other tasks.— Wikipedia[73] _(javascriptallonge.pdf (source-range-83ecb080-01898))_
- Looking at the code again, you see that the copy function doesn’t copy on write: It follows the pattern that while constructing something, we own it and can be liberal with mutation. _(javascriptallonge.pdf (source-range-83ecb080-01900))_
- It’s possible to write a generic unfold mechanism, but let’s pass on to what we can do with unfolded iterators. _(javascriptallonge.pdf (source-range-83ecb080-01995))_
- We write them in a backwards way, but they seem to work. _(javascriptallonge.pdf (source-range-83ecb080-02131))_
- So, when a standard way to write iterators was added to the JavaScript language, it didn’t make sense to use a method like .iterator() for it: That would conflict with existing code. _(javascriptallonge.pdf (source-range-83ecb080-02413))_
- In a generator, we write “do this, then this, then this.” In an iterator, we have to wrap that up and explicitly keep track of what step we’re on. _(javascriptallonge.pdf (source-range-83ecb080-02587))_
- “↑, →, ↑, ↓, ↑, →…” Write an algorithm that will determine whether the game halts, strictly from the called out directions, in finite time and space. _(javascriptallonge.pdf (source-range-83ecb080-02836))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00582))_

> Another way to write our “circumference” function would be to pass PI along with the diameter argument, something like this:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00583))_

> (diameter, PI) => diameter * PI

### Technical atom 2

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00598))_

> We write:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00601))_

> ((diameter) => { **const** PI = 3.14159265; **return** diameter * PI })(2) _//=> 6.2831853_

### Technical atom 3

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02009))_

> We could also write a filter for iterators to accompany our mapping function:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02011))_

> **const** oddsOf = callLeft(filterIteratorWith, (n) => n % 2 === 1);

### Technical atom 4

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02009))_

> We could also write a filter for iterators to accompany our mapping function:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02012))_

> toArray(take(squareOf(oddsOf(NumberIterator(1))), 5)) _//=> [1, 9, 25, 49, 81]_

### Technical atom 5

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02119))_

> We can write length and mapWith functions over it:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02122))_

> **const** length = (aPair) => aPair === EMPTY ? 0 : 1 + length(rest(aPair));

### Technical atom 6

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02388))_

> We could save a step and write collectionSum, a function that folds over any object, provided that the object implements an .iterator method:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02389))_

> **const** collectionSum = (collection) => { **const** iterator = collection.iterator();

### Technical atom 7

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02388))_

> We could save a step and write collectionSum, a function that folds over any object, provided that the object implements an .iterator method:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02390))_

> **let** eachIteration, sum = 0;

### Technical atom 8

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02388))_

> We could save a step and write collectionSum, a function that folds over any object, provided that the object implements an .iterator method:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02391))_

> **while** ((eachIteration = iterator(), !eachIteration.done)) { sum += eachIteration.value; } **return** sum }

### Technical atom 9

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02564))_

> Let’s write a generator:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02566))_

> **const** fibonacci = () => { **let** a, b;

### Technical atom 10

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02564))_

> Let’s write a generator:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02567))_

> console.log(a = 0);


## Related pages

- [[javascriptallonge-function]] - shared statements and technical atoms (2 shared statement(s), 7 shared atom(s))
- [[javascriptallonge-iterator]] - shared statements and technical atoms (1 shared statement(s), 5 shared atom(s))
- [[javascriptallonge-collection]] - shared technical atoms (3 shared atom(s))
- [[javascriptallonge-object]] - shared technical atoms (3 shared atom(s))
- [[javascriptallonge-length]] - shared technical atoms (1 shared atom(s))
- [[javascriptallonge-code]] - shared statements (2 shared statement(s))
- [[javascriptallonge-copy]] - shared statements (2 shared statement(s))
- [[javascriptallonge-program]] - shared statements (2 shared statement(s))
- [[javascriptallonge-javascript]] - shared statements (1 shared statement(s))
- [[javascriptallonge-language]] - shared statements (1 shared statement(s))
- [[javascriptallonge-list]] - shared statements (1 shared statement(s))

## Source

- [[javascriptallonge]]
