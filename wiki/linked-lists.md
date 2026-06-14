---
category: concept
summary: JavaScript linked lists use structure sharing, where mutation of one alias affects all shared nodes. Contrast with array destructuring which creates copies. See (raw/javascriptallonge.pdf p.158-176) for copy-on-write strategies.
sources: raw/javascriptallonge.pdf, raw/javascriptallonge.pdf p.158-176
updated: 2026-06-11
---

## Linked Lists in JavaScript

Linked lists in JavaScript use **structure sharing**, where modifying one reference affects all shared nodes. This contrasts with arrays, where destructuring creates a copy (see [[array-destructuring]]).

### Key Characteristics:
- **Mutation Aliases**: Changing a node's `rest` pointer affects all references to the list.
- **Copy-on-Write**: To avoid unintended side effects, modifications create new nodes rather than altering shared ones (see [[javascriptallonge-copy-on-write]]).
- **Performance Tradeoffs**: Structure sharing is memory efficient but risky; copy-on-write adds overhead but ensures isolation.

### Example:
```javascript
const parentList = { first: 1, rest: { first: 2, rest: { first: 3, rest: EMPTY } } };
const childList = parentList.rest;
// Modifying childList also changes parentList unless using copy-on-write
```

### Related Concepts:
- [[javascriptallonge-copy-on-write]] for strategies to manage shared data.
- [[arrays]] for comparison with copy-on-destructure behavior.
