---
page_id: lazy-and-eager-collections
page_kind: source
summary: Chapter on lazy and eager collections in JavaScript Allongé.
sources: raw/javascriptallonge.pdf p.246-260
updated: 2026-06-19
---

## Lazy and Eager Collections

This chapter explores the concepts of lazy and eager collections in JavaScript, focusing on how iterables can be used to build more flexible and efficient data structures. It discusses the benefits of lazy evaluation, where operations are not performed until the result is needed, and how this can reduce memory usage. The chapter also covers eager collections, which compute and return results immediately.

The chapter contrasts the "fat object" style of object-oriented programming, where each collection knows how to perform various operations like mapping, filtering, and reducing, with a more abstract approach using iterables. This approach allows for composition of operations without the need for each collection to implement every method, reducing code duplication.

Key concepts include:
- Lazy evaluation: operations are deferred until the result is actually needed.
- Eager evaluation: operations are performed immediately.
- Iterables and their role in implementing lazy and eager collections.
- Examples using linked lists (Pair) and stacks to demonstrate lazy and eager behaviors.

## Key Examples

The chapter provides examples using:
- `Numbers` - a lazy collection that generates an infinite sequence of numbers.
- `Pair` - a linked list implementation that can be used with lazy collections.
- `Stack` - a stack implementation that can also be used with lazy collections.

These examples demonstrate how lazy evaluation can be used to efficiently process large datasets by only computing what is needed.

## Lazy vs Eager Collections

Lazy collections defer computation until the result is needed, which can save memory and processing time. Eager collections, on the other hand, compute results immediately and return collections of their own type.

The chapter also touches on the trade-offs between lazy and eager collections, such as the need for immutable collections when using lazy evaluation to avoid unexpected results from mutations.

[[iteration-and-iterables]] and [[generating-iterables]] provide foundational knowledge about iterables and how they are used in JavaScript.
