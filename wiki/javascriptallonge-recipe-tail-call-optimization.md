---
page_id: javascriptallonge-recipe-tail-call-optimization
page_kind: recipe
page_family: recipe-pattern
summary: tail-call optimization: reusable source-backed pattern with 10 statement(s) and 2 technical atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: tail-call-optimization
projection_coverage: recipe-javascriptallonge-recipe-tail-call-optimization@0bf04438186ce628ae6d16c7fcd4f6c9
---

# tail-call optimization

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-composing-and-decomposing-data-tail-calls-and-default-arguments-tail-call-optimization-755a53cb]].
- Evidence roles: decision, constraint, explanation, example.

## Applicability And Rationale

- There are three places it returns. _(javascriptallonge.pdf (source-range-7239e085-00970))_
- It isn't going to do any more work, so it can throw its existing stack frame away. _(javascriptallonge.pdf (source-range-7239e085-00970))_
- This is a tail-call, because it invokes another function and returns its result. _(javascriptallonge.pdf (source-range-7239e085-00970))_
- This is interesting, because after sorting out what to supply as arguments ( this , args ), JavaScript can throw away everything in its current stack frame. _(javascriptallonge.pdf (source-range-7239e085-00970))_
- But the third is fn.apply(this, args) . _(javascriptallonge.pdf (source-range-7239e085-00970))_
- This is a very important characteristic of JavaScript: If a function makes a call in tail position, JavaScript optimizes away the function call overhead and stack space. _(javascriptallonge.pdf (source-range-7239e085-00971))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00969)_

```
const maybe = (fn) =>
function (...args) {
if (args.length === 0) {
return;
}
else {
for (let arg of args) {
if (arg == null) return;
}
return fn.apply(this, args);
}
}
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00973)_

```
const length = ([first, ...rest]) =>
first === undefined
? 0
: 1 + length(rest);
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-composing-and-decomposing-data-tail-calls-and-default-arguments-tail-call-optimization-755a53cb]]
