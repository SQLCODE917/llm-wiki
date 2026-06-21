---
page_id: javascriptallonge-iteration
page_kind: source
summary: Summary of the iteration chapter from JavaScript Allongé.
sources: raw/javascriptallonge.pdf p.227-228
updated: 2026-06-20
source_id: javascriptallonge.pdf
---

## Source record

This chapter discusses iteration in JavaScript, comparing iterative and generative approaches to handling data structures like trees.

## Key supported claims

- If you peel off isIterable and ignore the way that the iteration version uses [Symbol.iterator] and .next, we're left with the fact that the generating version calls itself recursively, and the iteration version maintains an explicit stack. (raw/javascriptallonge.pdf p.227-228)
- In essence, both the generation and iteration implementations have stacks, but the generation version's stack is implicit, while the iteration version's stack is explicit. (raw/javascriptallonge.pdf p.227-228)
- A less kind way to put it is that the iteration version is greenspunning something built into our programming language: We're reinventing the use of a stack to manage recursion, because writing our code to respond to a function call makes us turn a simple recursive algorithm inside-out. (raw/javascriptallonge.pdf p.227-228)
