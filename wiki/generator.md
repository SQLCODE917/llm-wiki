---
category: entity
summary: A function that produces values via yield, enabling coroutine-like behavior in JavaScript.
sources: javascriptallonge.pdf p.224-245
updated: 2026-06-12
---

A **generator** is a special function in JavaScript defined with `function *` that uses `yield` to produce values incrementally. Unlike traditional iterators, generators implicitly manage state via JavaScript's control flow, making them ideal for recursive iteration, state machines, and coroutines. Key features include:

- **Yield**: Pauses execution and returns a value, resuming when `.next()` is called again.
- **Coroutine behavior**: Allows suspension and resumption of execution between producer and consumer code (see [[coroutine]].
- **Iterable creation**: Generators simplify making objects iterable by defining `[Symbol.iterator]` as a generator function (see [[iterable]].

Example: `function * fibonacci() { yield 0; yield 1; while (true) { [a, b] = [b, a + b]; yield b; } }` (see [[javascriptallonge-generating-iterables]].
