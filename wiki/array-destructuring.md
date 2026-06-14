---
category: concept
summary: Array destructuring creates a copy of elements, unlike linked list structure sharing which references the same nodes. See (raw/javascriptallonge.pdf p.158-176) for copy-on-write strategies.
sources: raw/javascriptallonge.pdf, raw/javascriptallonge.pdf p.158-176
updated: 2026-06-11
---

## Array Destructuring

In JavaScript, array destructuring creates a **copy** of the elements, unlike linked lists which share nodes by reference (see [[linked-lists]]).

### Example:
```javascript
const parentArray = [1, 2, 3];
const [aFirst, ...childArray] = parentArray;
parentArray[2] = "three";
childArray[0] = "two";
// parentArray => [1,2,"three"], childArray => ["two",3]
```

### Key Differences:
- **Copy Semantics**: Destructuring creates a new array with copied elements.
- **Mutation Isolation**: Modifying the parent array does not affect the child array created via destructuring.

### Contrast with Linked Lists:
Linked lists share nodes by reference, so modifications to one alias affect all (see [[javascriptallonge-copy-on-write]] for strategies to manage this).

### Sources:
- (raw/javascriptallonge.pdf p.158-176)
