---
page_id: javascriptallonge-section-values-are-expressions-closures-and-scope-which-came-first-the-chicken-or-the-egg-711ff2a1
page_kind: source
summary: values are expressions / Closures and Scope / which came first, the chicken or the egg?: 6 source-backed entries and 2 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-values-are-expressions-closures-and-scope-which-came-first-the-chicken-or-the-egg-711ff2a1@7c2d3b74748cc515a823eb036441cc7a
---

# values are expressions / Closures and Scope / which came first, the chicken or the egg?

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-values-are-expressions-closures-and-scope-27942b9b]] - broader source section

## Statements

- This behaviour of pure functions and closures has many, many consequences that can be exploited to write software. _(javascriptallonge.pdf (source-range-83ecb080-00417))_
- JavaScript always has the notion of at least one environment we do not control: A global environment in which many useful things are bound such as libraries full of standard functions. _(javascriptallonge.pdf (source-range-83ecb080-00421))_
- JavaScript always has the notion of at least one environment we do not control: A global environment in which many useful things are bound such as libraries full of standard functions. _(javascriptallonge.pdf (source-range-83ecb080-00421))_
- As we’ll see when we discuss mutable state, this helps to prevent programmers from accidentally changing the global state that is shared by all code in the program. _(javascriptallonge.pdf (source-range-83ecb080-00425))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00421))_

> JavaScript always has the notion of at least one environment we do not control: A global environment in which many useful things are bound such as libraries full of standard functions. So when you invoke ((x) => x)(1) in the REPL, its full environment is going to look like this: {x: 1, '..': _global environment_ }.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00422))_

> If you don’t want your code to operate directly within the global environment, what can you do?

### Technical atom 2

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00422))_

> Sometimes, programmers wish to avoid this. If you don’t want your code to operate directly within the global environment, what can you do? Create an environment for them, of course. Many programmers choose to write every JavaScript file like this:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00423))_

> _// top of the file_ (() => { _// ... lots of JavaScript ..._ })();
