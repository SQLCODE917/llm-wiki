---
category: concept
summary: A computational construct enabling suspension and resumption of execution, implemented via JavaScript generators.
sources: javascriptallonge.pdf p.224-245
updated: 2026-06-12
---

A **coroutine** is a generalization of subroutines that allows multiple entry points and suspension/resumption of execution. In JavaScript, generators implement coroutine behavior by using `yield` to pause execution and return control to the consumer, resuming when `.next()` is called again. This enables cooperative multitasking between producer (generator) and consumer (iterating code).

Key characteristics:
- **Suspension**: Execution halts at `yield` and resumes from the same point on subsequent `.next()` calls.
- **State retention**: The generator retains its state between yields, eliminating the need for explicit state management.
- **Use cases**: Ideal for iterators, infinite sequences, and asynchronous operations (though not directly covered here).

JavaScript generators are a form of coroutine, as demonstrated in [[javascriptallonge-generating-iterables]] where generators yield values and resume execution on each iteration step.
