---
page_id: copy-on-write
page_kind: source
summary: Chapter on copy-on-write strategies for data structures.
sources: raw/javascriptallonge.pdf p.158-176
updated: 2026-06-19
---

## Copy on Write

This chapter explores copy-on-write (COW) strategies for managing data structures, particularly in the context of linked lists and arrays. It contrasts COW with copy-on-read and discusses the tradeoffs between these approaches.

### Key Concepts

- **Copy-on-Write (COW)**: A strategy where copies are made only when modifications are about to be made to shared data. This is more efficient than pessimistic copying when changes are infrequent.
- **Copy-on-Read**: A pessimistic strategy where copies are made whenever data is accessed, ensuring no sharing but at the cost of performance.
- **Structure Sharing**: The phenomenon where different data structures can share parts of their internal representation, leading to potential unintended side effects.

### The Coffee Cow Example

The chapter uses a metaphor of a coffee list to illustrate the difference between arrays and linked lists:

- When you take the rest of an array with destructuring (`[first, ...rest]`), you get a copy of the elements.
- When you take the rest of a linked list, you get the exact same nodes.

This leads to different behaviors:
- With arrays: modifications to parent don't affect the child, and vice versa.
- With linked lists: modifications to parent affect the child, and vice versa.

### COW Implementation

The chapter presents a COW implementation for linked lists:
1. `rest` function returns the rest of the list without copying.
2. `set` function creates a new node with the modified value and preserves the rest of the structure.
3. This approach allows for efficient operations when changes are infrequent.

### Tradeoffs

- COW is cheaper than copy-on-read when making infrequent changes.
- It becomes expensive if many changes are made to shared data.
- The implementation avoids copying during construction, then uses COW when needed.

### Related Concepts

- **Tortoise and Hare Algorithm**: An algorithm for detecting loops in linked lists.
- **Functional Iterators**: Patterns for separating traversal from operations on data structures.
- **Lazy Evaluation**: The idea that computations are deferred until needed.

### References

- Wikipedia: [Copy-on-write](https://en.wikipedia.org/wiki/Copy-on-write)
- Floyd's Tortoise and Hare algorithm for loop detection
- The Teleporting Turtle algorithm for loop detection

This chapter provides insights into how to manage shared data structures efficiently in functional programming contexts.
