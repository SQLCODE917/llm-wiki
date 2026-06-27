---
page_id: javascriptallonge-section-x-x-cafe8f8b
page_kind: source
summary: (x) => x: 17 source-backed entries and 2 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-x-x-cafe8f8b@dc0d13b15b8fa5f16131779a24359aaf
---

# (x) => x

From [[javascriptallonge]].

## Statements

- The third one is actually two functions, one inside the other. _(javascriptallonge.pdf (source-range-83ecb080-00494))_
- The second doesn’t have any free variables, because its only variable is bound. _(javascriptallonge.pdf (source-range-83ecb080-00494))_
- The first function doesn’t have any variables, therefore doesn’t have any free variables. _(javascriptallonge.pdf (source-range-83ecb080-00494))_
- The second doesn’t have any free variables, because its only variable is bound. _(javascriptallonge.pdf (source-range-83ecb080-00494))_
- The third one is actually two functions, one inside the other. _(javascriptallonge.pdf (source-range-83ecb080-00494))_
- The first function doesn’t have any variables, therefore doesn’t have any free variables. _(javascriptallonge.pdf (source-range-83ecb080-00494))_
- has a free variable, but the entire expression refers to (x) => ..., and it doesn’t have a free variable: The only variable anywhere in its body is x, which is certainly bound within (x) => .... _(javascriptallonge.pdf (source-range-83ecb080-00494))_
- From this, we learn something: A pure function can contain a closure. _(javascriptallonge.pdf (source-range-83ecb080-00495))_
- If you can’t, give your reasoning for why it’s impossible. _(javascriptallonge.pdf (source-range-83ecb080-00497))_
- Using only what we’ve learned so far, attempt to compose a closure that contains a pure function. _(javascriptallonge.pdf (source-range-83ecb080-00497))_
- Using only what we’ve learned so far, attempt to compose a closure that contains a pure function. _(javascriptallonge.pdf (source-range-83ecb080-00497))_
- We can’t say what it will do with argument (2) without understanding the magic for evaluating the free variable x. _(javascriptallonge.pdf (source-range-83ecb080-00498))_
- Pure functions always mean the same thing because all of their “inputs” are fully defined by their arguments. _(javascriptallonge.pdf (source-range-83ecb080-00498))_
- Pure functions always mean the same thing because all of their “inputs” are fully defined by their arguments. _(javascriptallonge.pdf (source-range-83ecb080-00498))_
- 27You may also hear the term “non-local variable.” Both are correct. _(javascriptallonge.pdf (source-range-83ecb080-00499))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00490, source-range-83ecb080-00494))_

> Pure functions are easiest to understand. They always mean the same thing wherever you use them. Here are some pure functions we’ve already seen: The first function doesn’t have any variables, therefore doesn’t have any free variables. The second doesn’t have any free variables, because its only variable is bound. The third one is actually two functions, one inside the other. (y) => ... has a free variable, but the entire expression refers to (x) => ..., and it doesn’t have a free variable: The

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00493))_

> - (x) => (y) => x

### Technical atom 2

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00498))_

> Pure functions always mean the same thing because all of their “inputs” are fully defined by their arguments. Not so with a closure. If I present to you this pure function (x, y) => x + y, we know exactly what it does with (2, 2). But what about this closure: (y) => x + y? We can’t say what it will do with argument (2) without understanding the magic for evaluating the free variable x.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00497))_

> If pure functions can contain closures, can a closure contain a pure function?
