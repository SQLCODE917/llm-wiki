---
page_id: javascriptallonge-tortoises-hares-and-teleporting-turtles
page_kind: source
summary: Tortoises, Hares, and Teleporting Turtles from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.164-166
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

This chapter discusses loop detection algorithms in linked lists, specifically the Tortoise and Hare algorithm and the Teleporting Turtle algorithm.

## Key supported claims

- The Tortoise and Hare algorithm, discovered by Robert Floyd in the 1960s, uses two node references traversing the list at different speeds to detect loops. No matter how large the list is, the fast reference will eventually equal the slow reference, thus detecting the loop (raw/javascriptallonge.pdf p.164-166).
- The Tortoise and Hare algorithm is a classic solution for detecting loops in a linked list using constant space, where one pointer moves at twice the speed of the other (raw/javascriptallonge.pdf p.164-166).
- The Teleporting Turtle algorithm is an alternative approach that can be faster under certain circumstances, depending on the size of the loop and the relative costs of certain operations (raw/javascriptallonge.pdf p.164-166).

## Technical details

### `technical-atom-e92d2e6767bad8ac` code

Citation: (raw/javascriptallonge.pdf p.164-166)

```javascript
const EMPTY = null ; const isEmpty = (node) => node === EMPTY; const pair = (first, rest = EMPTY) => ({first, rest}); const list = (...elements) => { const [first, ...rest] = elements; return elements.length === 0 ? EMPTY : pair(first, list(...rest)) } const forceAppend = (list1, list2) => { if (isEmpty(list1)) { return "FAIL!" } if (isEmpty(list1.rest)) { list1.rest = list2; } else { forceAppend(list1.rest, list2);
```

### `technical-atom-648da12c9dbc46c1` code

Citation: (raw/javascriptallonge.pdf p.164-166)

```javascript
} } const tortoiseAndHare = (aPair) => { let tortoisePair = aPair, harePair = aPair.rest; while ( true ) { if (isEmpty(tortoisePair) || isEmpty(harePair)) { return false ; } if (tortoisePair.first === harePair.first) { return true ; } harePair = harePair.rest; if (isEmpty(harePair)) { return false ; } if (tortoisePair.first === harePair.first) { return true ; } tortoisePair = tortoisePair.rest; harePair = harePair.rest; } }; const aList = list(1, 2, 3, 4, 5); tortoiseAndHare(aList) //=> false forceAppend(aList, aList.rest.rest); tortoiseAndHare(aList); //=> true
```

### `technical-atom-3772c8e58b945650` code

Citation: (raw/javascriptallonge.pdf p.164-166)

```javascript
const teleportingTurtle = (list) => { let speed = 1, rabbit = list, turtle = rabbit; while ( true ) { for ( let i = 0; i <= speed; i += 1) { rabbit = rabbit.rest; if (rabbit == null ) { return false ; } if (rabbit === turtle) { return true ; } } turtle = rabbit; speed *= 2; } return false ; }; const aList = list(1, 2, 3, 4, 5); teleportingTurtle(aList) //=> false forceAppend(aList, aList.rest.rest); teleportingTurtle(aList); //=> true
```

### `technical-atom-5ae6e5445ed43280` procedure

Citation: (raw/javascriptallonge.pdf p.164-166)

I then forgot about it for a while.

## Related technical details

### From [[javascriptallonge-functional-iterators]]: `technical-atom-66284ad4815503e0` code

Relation: nearby source page; matched terms `function`, `one`, `other`, `uses`, `where`

Citation: (raw/javascriptallonge.pdf p.206-209)

```javascript
The .iterator() method is defined with shorthand equivalent to iterator: function iterator() { ... } . Note that it uses the function keyword, so when we invoke it with stack.iterator() , JavaScript sets this to the value of stack . But what about the function .iterator() returns? It is defined with a fat arrow () => { ... } . What is the value of this within that function? Since JavaScript doesn't bind this within a fat arrow function, we follow the same rules of variable scoping as any other variable name: We check in the environment enclosing the function. Although the .iterator() method has returned, its environment is the one that encloses our () => { ... } function, and that's where this is bound to the value of stack . Therefore, the iterator function returned by the .iterator() method has this bound to the stack object, even though we call it with iter() .
```
