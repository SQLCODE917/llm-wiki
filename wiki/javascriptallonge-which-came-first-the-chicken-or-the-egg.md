---
page_id: javascriptallonge-which-came-first-the-chicken-or-the-egg
page_kind: source
summary: Chapter summary for 'which came first, the chicken or the egg?' from JavaScript Allongé
sources: raw/javascriptallonge.pdf p.47-48
updated: 2026-06-20
source_id: javascriptallonge.pdf
---

## Source record

This chapter explores the ancestry of JavaScript functions and environments, specifically discussing pure functions, closures, and the global environment. It also touches on mutable state and how to avoid direct interaction with the global environment by creating isolated environments.

## Key supported claims

- JavaScript always has the notion of at least one environment we do not control: A global environment in which many useful things are bound such as libraries full of standard functions (raw/javascriptallonge.pdf p.47-48).
- As we'll see when we discuss mutable state, this helps to prevent programmers from accidentally changing the global state that is shared by all code in the program (raw/javascriptallonge.pdf p.47-48).
- This behaviour of pure functions and closures has many, many consequences that can be exploited to write software (raw/javascriptallonge.pdf p.47-48).
