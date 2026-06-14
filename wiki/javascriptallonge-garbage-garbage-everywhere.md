---
category: source
summary: Analysis of JavaScript array recursion inefficiency, comparison to Lisp's linked lists, and object-based cons cell implementations. sources: raw/javascriptallonge.pdf p.126-140
sources: raw/javascriptallonge.pdf
updated: 2026-06-11
---

## Garbage, Garbage Everywhere

This chapter examines the performance pitfalls of using JavaScript arrays for recursive operations like `mapWith`, which creates temporary arrays and incurs significant copying overhead. Key points:

- **Array Copying Overhead**: The `[first, ...rest]` pattern creates new arrays at each recursion step, leading to O(n) memory allocation and copying for large datasets. This is slower than Lisp's linked lists, which use cons cells with O(1) operations.

- **Lisp's Cons Cells**: Early Lisp implementations on the IBM 704 used hardware-optimized CAR/CDR operations on 36-bit words, enabling efficient linked lists. JavaScript's array-based approach lacks this efficiency.

- **Object-Based Cons Cells**: JavaScript can emulate cons cells with objects `{ first, rest }`, avoiding array copying. However, recursive operations still require careful implementation to avoid stack bloat.

- **Destructuring and Performance**: Object destructuring syntax (`{ first, rest } = node`) provides cleaner access to cons cell properties compared to array indexing.

- **MapWith Optimization**: A tail-recursive `mapWith` using cons cells can avoid array copying but requires reversing the result, doubling the traversal time.

Cite: (raw/javascriptallonge.pdf p.126-140)
