---
page_id: javascriptallonge-section-and-also-closures-and-scope-which-came-first-the-chicken-or-the-egg-48a59db6
page_kind: source
summary: And also: / Closures and Scope / which came first, the chicken or the egg?: 6 source-backed entries and 2 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-29
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-and-also-closures-and-scope-which-came-first-the-chicken-or-the-egg-48a59db6@c6af7039f350e0c2ac171195786d196d
---

# And also: / Closures and Scope / which came first, the chicken or the egg?

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-and-also-closures-and-scope-d1679ec0]] - broader source section: And also: / Closures and Scope

## Statements

- This behaviour of pure functions and closures has many, many consequences that can be exploited to write software. We are going to explore them in some detail as well as look at some of the other mechanisms JavaScript provides for working with variables and mutable state. _(javascriptallonge.pdf (source-range-7239e085-00378))_
- JavaScript always has the notion of at least one environment we do not control: A global environment in which many useful things are bound such as libraries full of standard functions. So when you invoke ((x) => x)(1) in the REPL, its full environment is going to look like this: {x: 1, '..': global environment } . _(javascriptallonge.pdf (source-range-7239e085-00380))_
- The effect is to insert a new, empty environment in between the global environment and your own functions: {x: 1, '..': {'..': global environment }} . As we'll see when we discuss mutable state, this helps to prevent programmers from accidentally changing the global state that is shared by all code in the program. _(javascriptallonge.pdf (source-range-7239e085-00383))_
- JavaScript always has the notion of at least one environment we do not control: A global environment in which many useful things are bound such as libraries full of standard functions. _(javascriptallonge.pdf (source-range-7239e085-00380))_

## Technical atoms

### Technical frame 1: And also: / Closures and Scope / which came first, the chicken or the egg?

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00383))_

> The effect is to insert a new, empty environment in between the global environment and your own functions: {x: 1, '..': {'..': global environment }} . As we'll see when we discuss mutable state, this helps to prevent programmers from accidentally changing the global state that is shared by all code in the program.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00381))_

> If you don't want your code to operate directly within the global environment, what can you do?

### Technical frame 2: And also: / Closures and Scope / which came first, the chicken or the egg?

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00383))_

> The effect is to insert a new, empty environment in between the global environment and your own functions: {x: 1, '..': {'..': global environment }} . As we'll see when we discuss mutable state, this helps to prevent programmers from accidentally changing the global state that is shared by all code in the program.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00382))_

```
// top of the file
(() => {
// ... lots of JavaScript ...
})();
// bottom of the file
```
