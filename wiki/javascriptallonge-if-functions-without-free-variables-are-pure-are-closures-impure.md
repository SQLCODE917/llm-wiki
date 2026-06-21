---
page_id: javascriptallonge-if-functions-without-free-variables-are-pure-are-closures-impure
page_kind: source
summary: Chapter discussing the distinction between pure functions and closures, focusing on free variables.
sources: raw/javascriptallonge.pdf p.45-45
updated: 2026-06-20
source_id: javascriptallonge.pdf
---

## Source record

This chapter discusses the distinction between pure functions and closures, focusing on free variables.

## Key supported claims

- Now that we know that variables used in a function are either bound or free, we can bifurcate functions into those with free variables and those without: Functions containing no free variables are called pure functions. (raw/javascriptallonge.pdf p.45-45)
- Functions containing one or more free variables are called closures. (raw/javascriptallonge.pdf p.45-45)
- The second doesn't have any free variables, because its only variable is bound. (raw/javascriptallonge.pdf p.45-45)
- We can't say what it will do with argument (2) without understanding the magic for evaluating the free variable x. (raw/javascriptallonge.pdf p.45-45)
