---
page_id: javascriptallonge-section-tortoises-hares-and-teleporting-turtles-a6e5979e
page_kind: source
summary: Tortoises, Hares, and Teleporting Turtles: 13 source-backed entries and 3 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-tortoises-hares-and-teleporting-turtles-a6e5979e@c7105705d878def7cc3a8a3ef511e142
---

# Tortoises, Hares, and Teleporting Turtles

From [[javascriptallonge]].

## Statements

- A good long while ago (The First Age of Internet Startups), someone asked me one of those pet algorithm questions. It was, 'Write an algorithm to detect a loop in a linked list, in constant space.' _(javascriptallonge.pdf (source-range-31a4cf47-01258))_
- I think I told him that I was trying to figure out if I could adapt a hashing algorithm such as XORing everything together. This is the 'trick answer' to a question about finding a missing integer from a list, so I was trying the old, 'Transform this into a problem you've already solved 74 ' meta-algorithm. We moved on from there, and he didn't reveal the 'solution.' _(javascriptallonge.pdf (source-range-31a4cf47-01260))_
- I went home and pondered the problem. I wanted to solve it. Eventually, I came up with something and tried it (In Java!) on my home PC. I sent him an email sharing my result, to demonstrate my ability to follow through. I then forgot about it for a while. Some time later, I was told that the correct solution was: _(javascriptallonge.pdf (source-range-31a4cf47-01261))_
- This algorithm is called 'The Tortoise and the Hare,' and was discovered by Robert Floyd in the 1960s. You have two node references, and one traverses the list at twice the speed of the other. No matter how large it is, you will eventually have the fast reference equal to the slow reference, and thus you'll detect the loop. _(javascriptallonge.pdf (source-range-31a4cf47-01265))_
- Years later, I came across a discussion of this algorithm, The Tale of the Teleporting Turtle 75 . It seems to be faster under certain circumstances, depending on the size of the loop and the relative costs of certain operations. _(javascriptallonge.pdf (source-range-31a4cf47-01268))_
- What's interesting about these two algorithms is that they both tangle two separate concerns: How to traverse a data structure, and what to do with the elements that you encounter. In Functional Iterators, we'll investigate one pattern for separating these concerns. _(javascriptallonge.pdf (source-range-31a4cf47-01269))_
- No matter how large it is, you will eventually have the fast reference equal to the slow reference, and thus you'll detect the loop. _(javascriptallonge.pdf (source-range-31a4cf47-01265))_
- This algorithm is called 'The Tortoise and the Hare,' and was discovered by Robert Floyd in the 1960s. _(javascriptallonge.pdf (source-range-31a4cf47-01265))_

## Technical atoms

### Technical frame 1: Tortoises, Hares, and Teleporting Turtles

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01265))_

> This algorithm is called 'The Tortoise and the Hare,' and was discovered by Robert Floyd in the 1960s. You have two node references, and one traverses the list at twice the speed of the other. No matter how large it is, you will eventually have the fast reference equal to the slow reference, and thus you'll detect the loop.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01262))_

```
const EMPTY = null ; const isEmpty = (node) => node === EMPTY; const pair = (first, rest = EMPTY) => ({first, rest}); const list = (...elements) => { const [first, ...rest] = elements; return elements.length === 0 ? EMPTY : pair(first, list(...rest)) } const forceAppend = (list1, list2) => { if (isEmpty(list1)) { return "FAIL!" } if (isEmpty(list1.rest)) { list1.rest = list2; } else { forceAppend(list1.rest, list2);
```

### Technical frame 2: Tortoises, Hares, and Teleporting Turtles

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01265))_

> This algorithm is called 'The Tortoise and the Hare,' and was discovered by Robert Floyd in the 1960s. You have two node references, and one traverses the list at twice the speed of the other. No matter how large it is, you will eventually have the fast reference equal to the slow reference, and thus you'll detect the loop.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01264))_

```
} } const tortoiseAndHare = (aPair) => { let tortoisePair = aPair, harePair = aPair.rest; while ( true ) { if (isEmpty(tortoisePair) || isEmpty(harePair)) { return false ; } if (tortoisePair.first === harePair.first) { return true ; } harePair = harePair.rest; if (isEmpty(harePair)) { return false ; } if (tortoisePair.first === harePair.first) { return true ; } tortoisePair = tortoisePair.rest; harePair = harePair.rest; } }; const aList = list(1, 2, 3, 4, 5); tortoiseAndHare(aList) //=> false forceAppend(aList, aList.rest.rest); tortoiseAndHare(aList); //=> true
```

### Technical frame 3: Tortoises, Hares, and Teleporting Turtles

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01268))_

> Years later, I came across a discussion of this algorithm, The Tale of the Teleporting Turtle 75 . It seems to be faster under certain circumstances, depending on the size of the loop and the relative costs of certain operations.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01267))_

```
const teleportingTurtle = (list) => { let speed = 1, rabbit = list, turtle = rabbit; while ( true ) { for ( let i = 0; i <= speed; i += 1) { rabbit = rabbit.rest; if (rabbit == null ) { return false ; } if (rabbit === turtle) { return true ; } } turtle = rabbit; speed *= 2; } return false ; }; const aList = list(1, 2, 3, 4, 5); teleportingTurtle(aList) //=> false forceAppend(aList, aList.rest.rest); teleportingTurtle(aList); //=> true
```
