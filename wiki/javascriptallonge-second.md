---
page_id: javascriptallonge-second
page_kind: concept
summary: Second: 9 statement(s) and 5 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-second@6abde59df25681764a723ec85ef329ad
---

# Second

What [[javascriptallonge]] covers about second:

## Statements

- The second form works most of the time, but it is possible to break it by reassigning undefined to a different value, something we’ll discuss in Reassignment and Mutation. _(javascriptallonge.pdf (source-range-83ecb080-00337))_
- The second x, the one in => x, is not an argument, _it’s an expression referring to a variable_ . _(javascriptallonge.pdf (source-range-83ecb080-00433))_
- The second doesn’t have any free variables, because its only variable is bound. _(javascriptallonge.pdf (source-range-83ecb080-00494))_
- > 30We’re into the second chapter and we’ve finally named a function. _(javascriptallonge.pdf (source-range-83ecb080-00608))_
- The second magic name is very interesting, it’s called arguments, and the most interesting thing about it is that it contains a list of arguments passed to a function: _(javascriptallonge.pdf (source-range-83ecb080-00866))_
- The fact that either the second or the third (but not both) expressions are evaluated can have important repercussions. _(javascriptallonge.pdf (source-range-83ecb080-01119))_
- Our first and second functions are a little different than what most people are used to when we talk about functions that access data. _(javascriptallonge.pdf (source-range-83ecb080-02076))_
- In both cases, the functions first and second know how the data is represented, whether it be an array or an object. _(javascriptallonge.pdf (source-range-83ecb080-02085))_
- The second element of the fibonacci sequence is one. _(javascriptallonge.pdf (source-range-83ecb080-02562))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00334, source-range-83ecb080-00336))_

> There’s a third way, with JavaScript’s void operator. Behold: void is an operator that takes any value and evaluates to undefined, always. So, when we deliberately want an undefined value, should we use the first, second, or third form?[19] The answer is, use void. By convention, use void 0.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00335))_

> **void** 0 _//=> undefined_ **void** 1 _//=> undefined_ **void** (2 + 2) _//=> undefined_

### Technical atom 2

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00490, source-range-83ecb080-00494))_

> Pure functions are easiest to understand. They always mean the same thing wherever you use them. Here are some pure functions we’ve already seen: The first function doesn’t have any variables, therefore doesn’t have any free variables. The second doesn’t have any free variables, because its only variable is bound. The third one is actually two functions, one inside the other. (y) => ... has a free variable, but the entire expression refers to (x) => ..., and it doesn’t have a free variable: The 

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00493))_

> - (x) => (y) => x

### Technical atom 3

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00866))_

> The first magic name is this, and it is bound to something called the function’s context. We will explore this in more detail when we start discussing objects and classes. The second magic name is very interesting, it’s called arguments, and the most interesting thing about it is that it contains a list of arguments passed to a function:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00867))_

> **const** plus = **function** (a, b) { **return** arguments[0] + arguments[1]; } plus(2,3) _//=> 5_

### Technical atom 4

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01119))_

> The fact that either the second or the third (but not both) expressions are evaluated can have important repercussions. Consider this hypothetical example:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01120))_

> **const** status = isAuthorized(currentUser) ? deleteRecord(currentRecord) : 'Forbid\ den';

### Technical atom 5

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02076))_

> Our first and second functions are a little different than what most people are used to when we talk about functions that access data. If we represented a pair of values as an array, we’d write them like this:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02079))_

> **const** first = ([first, second]) => first, second = ([first, second]) => second;


## Related pages

- [[javascriptallonge-function]] - shared statements and technical atoms (2 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-expression]] - shared statements and technical atoms (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-argument]] - shared technical atoms (1 shared atom(s))
- [[javascriptallonge-evaluate]] - shared technical atoms (1 shared atom(s))
- [[javascriptallonge-javascript]] - shared technical atoms (1 shared atom(s))
- [[javascriptallonge-element]] - shared statements (1 shared statement(s))

## Source

- [[javascriptallonge]]
