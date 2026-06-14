---
category: source
summary: A chapter where The Carpenter solves a cycle detection problem using iterables and Floyd's algorithm during a job interview.
sources: raw/javascriptallonge.pdf
updated: 2026-06-12
---

This chapter describes The Carpenter's solution to a technical interview problem involving detecting if a chequer game halts. The solution involves transforming the game into an iterable, using stateful mapping to track positions, and applying Floyd's cycle-finding algorithm (Tortoise and Hare) to detect infinite loops. Key code examples include the `statefulMapWith` function and the `tortoiseAndHare` implementation. (raw/javascriptallonge.pdf p.261-272)
