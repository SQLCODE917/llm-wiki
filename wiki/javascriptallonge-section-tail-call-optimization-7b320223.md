---
page_id: javascriptallonge-section-tail-call-optimization-7b320223
page_kind: source
summary: **tail-call optimization**: 15 source-backed entries and 1 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-tail-call-optimization-7b320223@35a51520de896a823661611fcf0f58f7
---

# **tail-call optimization**

From [[javascriptallonge]].

## Statements

- This is a tail-call, because it invokes another function and returns its result. _(javascriptallonge.pdf (source-range-83ecb080-01420))_
- It isn’t going to do any more work, so it can throw its existing stack frame away. _(javascriptallonge.pdf (source-range-83ecb080-01420))_
- There are three places it returns. _(javascriptallonge.pdf (source-range-83ecb080-01420))_
- This is interesting, because after sorting out what to supply as arguments (this, args), JavaScript can throw away everything in its current stack frame. _(javascriptallonge.pdf (source-range-83ecb080-01420))_
- But the third is fn.apply(this, args). _(javascriptallonge.pdf (source-range-83ecb080-01420))_
- This is interesting, because after sorting out what to supply as arguments (this, args), JavaScript can throw away everything in its current stack frame. _(javascriptallonge.pdf (source-range-83ecb080-01420))_
- This is a tail-call, because it invokes another function and returns its result. _(javascriptallonge.pdf (source-range-83ecb080-01420))_
- This is a very important characteristic of JavaScript: **If a function makes a call in tail position, JavaScript optimizes away the function call overhead and stack space.** _(javascriptallonge.pdf (source-range-83ecb080-01421))_
- And in fact, it does exactly that: It throws the stack frame away, and does not consume extra memory when making a maybe-wrapped call. _(javascriptallonge.pdf (source-range-83ecb080-01421))_
- That is excellent, but one wrapping is not a big deal. _(javascriptallonge.pdf (source-range-83ecb080-01422))_
- The length function calls itself, but it is not a tail-call, because it returns 1 + length(rest), not length(rest). _(javascriptallonge.pdf (source-range-83ecb080-01424))_
- The length function calls itself, but it is not a tail-call, because it returns 1 + length(rest), not length(rest). _(javascriptallonge.pdf (source-range-83ecb080-01424))_
- The problem can be stated in such a way that the answer is obvious: length does not call itself in tail position, because it has to do two pieces of work, and while one of them is in the recursive call to length, the other happens after the recursive call. _(javascriptallonge.pdf (source-range-83ecb080-01425))_
- The problem can be stated in such a way that the answer is obvious: length does not call itself in tail position, because it has to do two pieces of work, and while one of them is in the recursive call to length, the other happens after the recursive call. _(javascriptallonge.pdf (source-range-83ecb080-01425))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01422, source-range-83ecb080-01424))_

> That is excellent, but one wrapping is not a big deal. When would we really care? Consider this implementation of length: The length function calls itself, but it is not a tail-call, because it returns 1 + length(rest), not length(rest).

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01423))_

> **const** length = ([first, ...rest]) => first === **undefined** ? 0 : 1 + length(rest);
