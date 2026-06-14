---
category: source
summary: Explains copy-on-write strategy for linked lists vs arrays, structure sharing, and trade-offs with copy-on-read. Includes code examples and the tortoise-and-hare loop detection algorithm.
sources: raw/javascriptallonge.pdf
updated: 2026-06-11
---

## Copy-on-Write Strategy

This chapter discusses how JavaScript handles data structure sharing between arrays and linked lists. Key concepts include:

- **Structure Sharing**: Arrays use copy-on-destructure (creates a copy), while linked lists share nodes by reference.
- **Copy-on-Write**: A strategy where copies are made only when modifications occur, avoiding unnecessary duplication.
- **Trade-offs**: Copy-on-read is safer but slower, while copy-on-write optimizes performance for infrequent modifications.

### Code Examples

```javascript
// Array vs linked list behavior
const parentArray = [1, 2, 3];
const [aFirst, ...childArray] = parentArray;
parentArray[2] = "three";
childArray[0] = "two";
// parentArray => [1,2,"three"], childArray => ["two",3]
```

```javascript
// Copy-on-write implementation
const set = (index, value, list) => 
  index === 0 
    ? { first: value, rest: list.rest } 
    : { first: list.first, rest: set(index - 1, value, list.rest) };
```

### Tortoise and Hare Algorithm

Detects loops in linked lists using two pointers:

```javascript
const tortoiseAndHare = (aPair) => {
  let tortoise = aPair, hare = aPair.rest;
  while (true) {
    if (isEmpty(tortoise) || isEmpty(hare)) return false;
    if (tortoise.first === hare.first) return true;
    hare = hare.rest;
    if (isEmpty(hare)) return false;
    if (tortoise.first === hare.first) return true;
    tortoise = tortoise.rest;
    hare = hare.rest;
  }
};
```

### Functional Iterators

Separates traversal from operations, enabling lazy evaluation:

```javascript
const arrayIterator = (array) => {
  let i = 0;
  return () => ({
    done: i === array.length,
    value: i < array.length ? array[i++] : undefined
  });
};
```

Sources: (raw/javascriptallonge.pdf p.158-176)
