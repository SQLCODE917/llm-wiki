---
page_id: javascriptallonge-section-and-also-closures-and-scope-which-came-first-the-chicken-or-the-egg-48a59db6
page_kind: source
page_family: section-reference
summary: And also: / Closures and Scope / which came first, the chicken or the egg?: 6 source-backed entries and 0 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-and-also-closures-and-scope-which-came-first-the-chicken-or-the-egg-48a59db6@7b2f75995f23deecf13d6070094034de
---

# And also: / Closures and Scope / which came first, the chicken or the egg?

From [[javascriptallonge]].

## Related pages

### Source structure

- [[javascriptallonge-section-and-also-closures-and-scope-d1679ec0]] - broader source section: And also: / Closures and Scope

## Statements

- This behaviour of pure functions and closures has many, many consequences that can be exploited to write software. We are going to explore them in some detail as well as look at some of the other mechanisms JavaScript provides for working with variables and mutable state. _(javascriptallonge.pdf (source-range-7239e085-00378))_
- JavaScript always has the notion of at least one environment we do not control: A global environment in which many useful things are bound such as libraries full of standard functions. So when you invoke ((x) => x)(1) in the REPL, its full environment is going to look like this: {x: 1, '..': global environment } . _(javascriptallonge.pdf (source-range-7239e085-00380))_
- The effect is to insert a new, empty environment in between the global environment and your own functions: {x: 1, '..': {'..': global environment }} . As we'll see when we discuss mutable state, this helps to prevent programmers from accidentally changing the global state that is shared by all code in the program. _(javascriptallonge.pdf (source-range-7239e085-00383))_
- JavaScript always has the notion of at least one environment we do not control: A global environment in which many useful things are bound such as libraries full of standard functions. _(javascriptallonge.pdf (source-range-7239e085-00380))_
