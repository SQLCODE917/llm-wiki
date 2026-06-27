---
page_id: javascriptallonge-tail-and-default-argument
page_kind: concept
summary: Tail Calls (and Default Arguments): 40 statement(s) and 25 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-tail-and-default-argument@8dc96e9f5c8ee2bcb3009fa88072c52a
---

# Tail Calls (and Default Arguments)

What [[javascriptallonge]] covers about tail calls (and default arguments):

## Statements

_Showing 14 of 40 statements selected for this topic._

- And in fact, it does exactly that: It throws the stack frame away, and does not consume extra memory when making a maybe-wrapped call. _(javascriptallonge.pdf (source-range-83ecb080-01421))_
- And this basic transformation from a recursive function that does not make a tail call, into a recursive function that calls itself in tail position, is a bread-and-butter pattern for programmers using a language that incorporates tail-call optimization. _(javascriptallonge.pdf (source-range-83ecb080-01459))_
- A default argument is concise and readable. _(javascriptallonge.pdf (source-range-83ecb080-01491))_
- How very useful: defaults can be supplied for destructuring assignments, just like defaults for parameters. _(javascriptallonge.pdf (source-range-83ecb080-01500))_
- The mapWith and foldWith functions we wrote in Self-Similarity are useful for illustrating the basic principles behind using recursion to work with self-similar data structures, but they are not “production-ready” implementations. _(javascriptallonge.pdf (source-range-83ecb080-01398))_
- To do that, it has to evaluate fn(first) and mapWith(fn, rest), then evaluate [fn(first), ...mapWith(fn, rest)]. _(javascriptallonge.pdf (source-range-83ecb080-01401))_
- It can start assembling the resulting array and start discarding the information it is saving. _(javascriptallonge.pdf (source-range-83ecb080-01409))_
- That information is saved on a _call stack_ , and it is quite expensive. _(javascriptallonge.pdf (source-range-83ecb080-01410))_
- In practice, using a method like this with more than about 50 items in an array may cause some implementations to run very slow, run out of memory and freeze, or cause an error. _(javascriptallonge.pdf (source-range-83ecb080-01411))_
- This is a tail-call, because it invokes another function and returns its result. _(javascriptallonge.pdf (source-range-83ecb080-01420))_
- This is interesting, because after sorting out what to supply as arguments (this, args), JavaScript can throw away everything in its current stack frame. _(javascriptallonge.pdf (source-range-83ecb080-01420))_
- This is a very important characteristic of JavaScript: **If a function makes a call in tail position, JavaScript optimizes away the function call overhead and stack space.** _(javascriptallonge.pdf (source-range-83ecb080-01421))_
- The length function calls itself, but it is not a tail-call, because it returns 1 + length(rest), not length(rest). _(javascriptallonge.pdf (source-range-83ecb080-01424))_
- The 1 + work is done before calling itself, and by the time it reaches the terminal position, it has the answer. _(javascriptallonge.pdf (source-range-83ecb080-01436))_

## Technical atoms

_Showing 6 of 25 technical atoms selected for this topic._

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01402))_

> This is roughly equivalent to writing:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01404))_

> Note that while evaluating mapWith(fn, rest), JavaScript must retain the value first or fn(first), plus some housekeeping information so it remembers what to do with mapWith(fn, rest) when it has a result.

### Technical atom 2

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01411))_

> In practice, using a method like this with more than about 50 items in an array may cause some implementations to run very slow, run out of memory and freeze, or cause an error.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01412))_

> mapWith((x) => x * x, [

### Technical atom 3

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01422, source-range-83ecb080-01424))_

> That is excellent, but one wrapping is not a big deal. When would we really care? Consider this implementation of length: The length function calls itself, but it is not a tail-call, because it returns 1 + length(rest), not length(rest).

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01423))_

> **const** length = ([first, ...rest]) => first === **undefined** ? 0 : 1 + length(rest);

### Technical atom 4

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01430))_

> The obvious solution is push the 1 + work into the call to length. Here’s our first cut:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01431))_

> **const** lengthDelaysWork = ([first, ...rest], numberToBeAdded) => first === **undefined**

### Technical atom 5

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01436))_

> This lengthDelaysWork function calls itself in tail position. The 1 + work is done before calling itself, and by the time it reaches the terminal position, it has the answer. Now that we’ve seen how it works, we can clean up the 0 + numberToBeAdded business. But while we’re doing that, it’s annoying to remember to call it with a zero. Let’s fix that:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01437))_

> **const** lengthDelaysWork = ([first, ...rest], numberToBeAdded) => first === **undefined**

### Technical atom 6

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01436))_

> This lengthDelaysWork function calls itself in tail position. The 1 + work is done before calling itself, and by the time it reaches the terminal position, it has the answer. Now that we’ve seen how it works, we can clean up the 0 + numberToBeAdded business. But while we’re doing that, it’s annoying to remember to call it with a zero. Let’s fix that:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01439))_

> **const** length = (n) => lengthDelaysWork(n, 0);


## Source

- [[javascriptallonge]]
