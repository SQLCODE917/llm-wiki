---
page_id: javascriptallonge-recipe-tortoises-hares-and-teleporting-turtles
page_kind: recipe
page_family: recipe-pattern
summary: Tortoises, Hares, and Teleporting Turtles: reusable source-backed pattern with 8 statement(s) and 3 technical atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: tortoises-hares-and-teleporting-turtles
projection_coverage: recipe-javascriptallonge-recipe-tortoises-hares-and-teleporting-turtles@0e7cf948f29ad9b2ece04f6abfd7f0c0
---

# Tortoises, Hares, and Teleporting Turtles

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-yes-consider-this-variation-tortoises-hares-and-teleporting-turtles-091ad917]].
- Evidence roles: decision, explanation, example.

## Applicability And Rationale

- It was, 'Write an algorithm to detect a loop in a linked list, in constant space.' _(javascriptallonge.pdf (source-range-7239e085-01258))_
- This is the 'trick answer' to a question about finding a missing integer from a list, so I was trying the old, 'Transform this into a problem you've already solved 74 ' meta-algorithm. _(javascriptallonge.pdf (source-range-7239e085-01260))_
- Eventually, I came up with something and tried it (In Java!) on my home PC. _(javascriptallonge.pdf (source-range-7239e085-01261))_
- This algorithm is called 'The Tortoise and the Hare,' and was discovered by Robert Floyd in the 1960s. _(javascriptallonge.pdf (source-range-7239e085-01265))_
- You have two node references, and one traverses the list at twice the speed of the other. _(javascriptallonge.pdf (source-range-7239e085-01265))_
- No matter how large it is, you will eventually have the fast reference equal to the slow reference, and thus you'll detect the loop. _(javascriptallonge.pdf (source-range-7239e085-01265))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01262)_

```
const EMPTY = null;
const isEmpty = (node) => node === EMPTY;
const pair = (first, rest = EMPTY) => ({first, rest});
const list = (...elements) => {
const [first, ...rest] = elements;
return elements.length === 0
? EMPTY
: pair(first, list(...rest))
}
const forceAppend = (list1, list2) => {
if (isEmpty(list1)) {
return "FAIL!"
}
if (isEmpty(list1.rest)) {
list1.rest = list2;
}
else {
forceAppend(list1.rest, list2);
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01264)_

```
}
}
const tortoiseAndHare = (aPair) => {
let tortoisePair = aPair,
harePair = aPair.rest;
while (true) {
if (isEmpty(tortoisePair) || isEmpty(harePair)) {
return false;
}
if (tortoisePair.first === harePair.first) {
return true;
}
harePair = harePair.rest;
if (isEmpty(harePair)) {
return false;
}
if (tortoisePair.first === harePair.first) {
return true;
}
tortoisePair = tortoisePair.rest;
harePair = harePair.rest;
}
};
const aList = list(1, 2, 3, 4, 5);
tortoiseAndHare(aList)
//=> false
forceAppend(aList, aList.rest.rest);
tortoiseAndHare(aList);
//=> true
```

### Atom 3: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01267)_

```
const teleportingTurtle = (list) => {
let speed = 1,
rabbit = list,
turtle = rabbit;
while (true) {
for (let i = 0; i <= speed; i += 1) {
rabbit = rabbit.rest;
if (rabbit == null) {
return false;
}
if (rabbit === turtle) {
return true;
}
}
turtle = rabbit;
speed *= 2;
}
return false;
};
const aList = list(1, 2, 3, 4, 5);
teleportingTurtle(aList)
//=> false
forceAppend(aList, aList.rest.rest);
teleportingTurtle(aList);
//=> true
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-yes-consider-this-variation-tortoises-hares-and-teleporting-turtles-091ad917]]
