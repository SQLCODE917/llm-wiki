---
page_id: javascriptallonge-section-composing-and-decomposing-data-tail-calls-and-default-arguments-tail-call-optimization-755a53cb
page_kind: source
page_family: section-reference
summary: Composing and Decomposing Data / Tail Calls (and Default Arguments) / tail-call optimization: 16 source-backed entries and 0 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-composing-and-decomposing-data-tail-calls-and-default-arguments-tail-call-optimization-755a53cb@810b9a9f141dfe4a63c7d95367984938
---

# Composing and Decomposing Data / Tail Calls (and Default Arguments) / tail-call optimization

From [[javascriptallonge]].

## Related pages

### Source structure

- [[javascriptallonge-section-composing-and-decomposing-data-tail-calls-and-default-arguments-e2a54ac1]] - broader source section: Composing and Decomposing Data / Tail Calls (and Default Arguments)

## Statements

- There are three places it returns. The first two don't return anything, they don't matter. But the third is fn.apply(this, args) . This is a tail-call, because it invokes another function and returns its result. This is interesting, because after sorting out what to supply as arguments ( this , args ), JavaScript can throw away everything in its current stack frame. It isn't going to do any more work, so it can throw its existing stack frame away. _(javascriptallonge.pdf (source-range-7239e085-00970))_
- And in fact, it does exactly that: It throws the stack frame away, and does not consume extra memory when making a maybe -wrapped call. This is a very important characteristic of JavaScript: If a function makes a call in tail position, JavaScript optimizes away the function call overhead and stack space. _(javascriptallonge.pdf (source-range-7239e085-00971))_
- That is excellent, but one wrapping is not a big deal. When would we really care? Consider this implementation of length : _(javascriptallonge.pdf (source-range-7239e085-00972))_
- The length function calls itself, but it is not a tail-call, because it returns 1 + length(rest) , not length(rest) . _(javascriptallonge.pdf (source-range-7239e085-00974))_
- The problem can be stated in such a way that the answer is obvious: length does not call itself in tail position, because it has to do two pieces of work, and while one of them is in the recursive call to length , the other happens after the recursive call. _(javascriptallonge.pdf (source-range-7239e085-00975))_
- This is a tail-call, because it invokes another function and returns its result. _(javascriptallonge.pdf (source-range-7239e085-00970))_
- This is interesting, because after sorting out what to supply as arguments ( this , args ), JavaScript can throw away everything in its current stack frame. _(javascriptallonge.pdf (source-range-7239e085-00970))_
- The length function calls itself, but it is not a tail-call, because it returns 1 + length(rest) , not length(rest) . _(javascriptallonge.pdf (source-range-7239e085-00974))_
- The problem can be stated in such a way that the answer is obvious: length does not call itself in tail position, because it has to do two pieces of work, and while one of them is in the recursive call to length , the other happens after the recursive call. _(javascriptallonge.pdf (source-range-7239e085-00975))_
