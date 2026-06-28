---
page_id: javascriptallonge-section-tail-call-optimization-152dac4b
page_kind: source
summary: tail-call optimization: 16 source-backed entries and 2 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-tail-call-optimization-152dac4b@49be49cd9c2f922087a78b57d905dd91
---

# tail-call optimization

From [[javascriptallonge]].

## Statements

- There are three places it returns. The first two don't return anything, they don't matter. But the third is fn.apply(this, args) . This is a tail-call, because it invokes another function and returns its result. This is interesting, because after sorting out what to supply as arguments ( this , args ), JavaScript can throw away everything in its current stack frame. It isn't going to do any more work, so it can throw its existing stack frame away. _(javascriptallonge.pdf (source-range-31a4cf47-00970))_
- And in fact, it does exactly that: It throws the stack frame away, and does not consume extra memory when making a maybe -wrapped call. This is a very important characteristic of JavaScript: If a function makes a call in tail position, JavaScript optimizes away the function call overhead and stack space. _(javascriptallonge.pdf (source-range-31a4cf47-00971))_
- That is excellent, but one wrapping is not a big deal. When would we really care? Consider this implementation of length : _(javascriptallonge.pdf (source-range-31a4cf47-00972))_
- The length function calls itself, but it is not a tail-call, because it returns 1 + length(rest) , not length(rest) . _(javascriptallonge.pdf (source-range-31a4cf47-00974))_
- The problem can be stated in such a way that the answer is obvious: length does not call itself in tail position, because it has to do two pieces of work, and while one of them is in the recursive call to length , the other happens after the recursive call. _(javascriptallonge.pdf (source-range-31a4cf47-00975))_
- This is interesting, because after sorting out what to supply as arguments ( this , args ), JavaScript can throw away everything in its current stack frame. _(javascriptallonge.pdf (source-range-31a4cf47-00970))_
- This is a tail-call, because it invokes another function and returns its result. _(javascriptallonge.pdf (source-range-31a4cf47-00970))_
- The length function calls itself, but it is not a tail-call, because it returns 1 + length(rest) , not length(rest) . _(javascriptallonge.pdf (source-range-31a4cf47-00974))_
- The problem can be stated in such a way that the answer is obvious: length does not call itself in tail position, because it has to do two pieces of work, and while one of them is in the recursive call to length , the other happens after the recursive call. _(javascriptallonge.pdf (source-range-31a4cf47-00975))_

## Technical atoms

### Technical frame 1: tail-call optimization

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00970))_

> There are three places it returns. The first two don't return anything, they don't matter. But the third is fn.apply(this, args) . This is a tail-call, because it invokes another function and returns its result. This is interesting, because after sorting out what to supply as arguments ( this , args ), JavaScript can throw away everything in its current stack frame. It isn't going to do any more work, so it can throw its existing stack frame away.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00969))_

```
const maybe = (fn) => function (...args) { if (args.length === 0) { return ; } else { for ( let arg of args) { if (arg == null ) return ; } return fn.apply( this , args); } }
```

### Technical frame 2: tail-call optimization

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00974))_

> The length function calls itself, but it is not a tail-call, because it returns 1 + length(rest) , not length(rest) .

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00973))_

```
const length = ([first, ...rest]) => first === undefined ? 0 : 1 + length(rest);
```
