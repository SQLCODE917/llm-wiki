---
category: concept
summary: Algorithm to detect loops in linked lists using two pointers (tortoise and hare). See (raw/javascriptallonge.pdf p.158-176) for implementation details.
sources: raw/javascriptallonge.pdf, raw/javascriptallonge.pdf p.158-176
updated: 2026-06-12
---

## Tortoise and Hare Algorithm

This algorithm detects loops in linked lists by using two pointers that traverse the list at different speeds:

- **Tortoise** moves one node at a time.
- **Hare** moves two nodes at a time.

If a loop exists, the two pointers will eventually meet. If not, the hare will reach the end of the list.

### Code Example:
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

### Key Points:
- **Time Complexity**: O(n) where n is the number of nodes.
- **Space Complexity**: O(1) (constant space).
- **Use Case**: Detecting cycles in linked lists without additional memory.

### Sources:
- (raw/javascriptallonge.pdf p.158-176)
