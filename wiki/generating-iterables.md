---
page_id: generating-iterables
page_kind: source
summary: Chapter on generating iterables using JavaScript generators.
sources: raw/javascriptallonge.pdf p.224-245
updated: 2026-06-19
---

## Generating Iterables

This chapter covers the concept of generating iterables using JavaScript generators. It explains how generators can simplify the implementation of iterators, especially for complex cases like recursive iteration and state management.

Key concepts include:
- The difference between iteration and generation
- How generators can be used to implement recursive iterators
- The use of generators for state machines (like Fibonacci sequences)
- How generators are coroutines and how they differ from ordinary functions
- The relationship between generators and iterable objects
- How to use yield and yield* to produce values from generators
- Rewriting traditional iterable operations using generators

The chapter demonstrates how generators allow for more natural and simpler code compared to traditional iterator implementations, particularly for recursive structures and stateful operations.

## Key Examples

### Recursive Iterators
The chapter shows how generators simplify recursive iteration over tree structures. Instead of manually managing an explicit stack, a generator can recursively yield elements from nested iterables.

### Fibonacci Generator
A Fibonacci sequence generator is shown that uses implicit state management, which is simpler than the explicit state management required in traditional iterators.

### Tree Traversal
The chapter demonstrates how to write a generator function to traverse tree structures, using `yield*` to yield all elements from nested iterables.

### Iterable Operations
Traditional iterable operations like `mapWith`, `filterWith`, and `untilWith` are rewritten using generators, showing how much simpler the code becomes.

## Conclusion

Generators provide a powerful way to create iterables in JavaScript. They allow developers to write code that looks like regular sequential code, while still providing the lazy evaluation and state management benefits of iterators. This makes it much easier to work with complex data structures and algorithms that would otherwise be cumbersome to implement with traditional iterators.
