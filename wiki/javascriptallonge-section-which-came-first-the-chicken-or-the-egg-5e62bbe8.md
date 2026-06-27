---
page_id: javascriptallonge-section-which-came-first-the-chicken-or-the-egg-5e62bbe8
page_kind: source
summary: **which came first, the chicken or the egg?**: 5 source-backed entries and 1 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-which-came-first-the-chicken-or-the-egg-5e62bbe8@934b06794a0a86e978f8ed22c69d3658
---

# **which came first, the chicken or the egg?**

From [[javascriptallonge]].

## Statements

- This behaviour of pure functions and closures has many, many consequences that can be exploited to write software. _(javascriptallonge.pdf (source-range-83ecb080-00527))_
- JavaScript always has the notion of at least one environment we do not control: A global environment in which many useful things are bound such as libraries full of standard functions. _(javascriptallonge.pdf (source-range-83ecb080-00531))_
- JavaScript always has the notion of at least one environment we do not control: A global environment in which many useful things are bound such as libraries full of standard functions. _(javascriptallonge.pdf (source-range-83ecb080-00531))_
- As we’ll see when we discuss mutable state, this helps to prevent programmers from accidentally changing the global state that is shared by all code in the program. _(javascriptallonge.pdf (source-range-83ecb080-00538))_

## Technical atoms

> Context: JavaScript always has the notion of at least one environment we do not control: A global environment in which many useful things are bound such as libraries full of standard functions. So when you invoke ((x) => x)(1) in the REPL, its full environment is going to look like this: {x: 1, '..': _global environment_ }.
_(context: javascriptallonge.pdf (source-range-83ecb080-00531))_

> If you don’t want your code to operate directly within the global environment, what can you do?
_(source: javascriptallonge.pdf (source-range-83ecb080-00532))_
