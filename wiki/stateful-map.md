---
category: concept
summary: A lazy mapping technique that preserves state between iterations, used to track position in the chequer game problem.
sources: raw/javascriptallonge.pdf
updated: 2026-06-12
---

The statefulMapWith function, introduced in the JavaScriptAllonge interlude, is a lazy mapping technique that maintains state across iterations. It allows transforming an iterable of directions into an iterable of positions by preserving the current position state. This approach is crucial for detecting cycles in the chequer game using the Tortoise and Hare algorithm. (raw/javascriptallonge.pdf p.261-272)
