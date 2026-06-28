---
page_id: javascriptallonge-second
page_kind: concept
summary: Second: 7 statement(s) and 2 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-second@6ac74db7550f5c411e6ede15150f5652
---

# Second

What [[javascriptallonge]] covers about second:

## Statements

- The second form works most of the time, but it is possible to break it by reassigning undefined to a different value, something we’ll discuss in Reassignment and Mutation. _(javascriptallonge.pdf (source-range-83ecb080-00279))_
- The second x, the one in => x, is not an argument, _it’s an expression referring to a variable_ . _(javascriptallonge.pdf (source-range-83ecb080-00334))_
- The second doesn’t have any free variables, because its only variable is bound. _(javascriptallonge.pdf (source-range-83ecb080-00387))_
- The fact that either the second or the third (but not both) expressions are evaluated can have important repercussions. _(javascriptallonge.pdf (source-range-83ecb080-00778))_
- Our first and second functions are a little different than what most people are used to when we talk about functions that access data. _(javascriptallonge.pdf (source-range-83ecb080-01353))_
- In both cases, the functions first and second know how the data is represented, whether it be an array or an object. _(javascriptallonge.pdf (source-range-83ecb080-01356))_
- The second element of the fibonacci sequence is one. _(javascriptallonge.pdf (source-range-83ecb080-01657))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00383, source-range-83ecb080-00387))_

> Pure functions are easiest to understand. They always mean the same thing wherever you use them. Here are some pure functions we’ve already seen: The first function doesn’t have any variables, therefore doesn’t have any free variables. The second doesn’t have any free variables, because its only variable is bound. The third one is actually two functions, one inside the other. (y) => ... has a free variable, but the entire expression refers to (x) => ..., and it doesn’t have a free variable: The 

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00386))_

> - (x) => (y) => x

### Technical atom 2

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01364))_

> For “data” we access with K and K(I), our “structure” is the function (selector) => selector("primus")("secundus"). Let’s extract those into parameters: (first, second) => (selector) => selector(first)(second) For consistency with the way combinators are written as functions taking just one parameter, we’ll curry[78] the function: (first) => (second) => (selector) => selector(first)(second) Let’s try it, we’ll use the word pair for the function that makes data (When we need to refer to a specifi

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01365))_

> If we change the names to x, y, and z, we get: (x) => (y) => (z) => z(x)(y).


## Related pages

- [[javascriptallonge-function]] - shared statements and technical atoms (2 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-expression]] - shared statements and technical atoms (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-alway]] - shared technical atoms (1 shared atom(s))
- [[javascriptallonge-parameter]] - shared technical atoms (1 shared atom(s))
- [[javascriptallonge-pure]] - shared technical atoms (1 shared atom(s))
- [[javascriptallonge-data]] - shared statements (1 shared statement(s))
- [[javascriptallonge-element]] - shared statements (1 shared statement(s))
- [[javascriptallonge-variable]] - shared statements (1 shared statement(s))

## Source

- [[javascriptallonge]]
