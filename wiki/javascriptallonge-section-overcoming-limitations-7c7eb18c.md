---
page_id: javascriptallonge-section-overcoming-limitations-7c7eb18c
page_kind: source
summary: **overcoming limitations**: 5 source-backed entries and 2 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-overcoming-limitations-7c7eb18c@33fb8f93df213b5309af11f35d3214e6
---

# **overcoming limitations**

From [[javascriptallonge]].

## Statements

- All left-variadic functions have one or more fixed arguments, and the rest are gathered into the leftmost argument. _(javascriptallonge.pdf (source-range-83ecb080-01064))_
- We sure can, by using the techniques from rightVariadic. _(javascriptallonge.pdf (source-range-83ecb080-01065))_
- Our leftVariadic function is a decorator that turns any function into a function that gathers parameters _from the left_ , instead of from the right. _(javascriptallonge.pdf (source-range-83ecb080-01072))_

## Technical atoms

> Context: It’s nice to have progress. But as noted above, we can’t write:
_(context: javascriptallonge.pdf (source-range-83ecb080-01062))_

> **const** butLastAndLast = (...butLast, last) => [butLast, last];
_(source: javascriptallonge.pdf (source-range-83ecb080-01063))_

> **const** butLastAndLast = leftVariadic((butLast, last) => [butLast, last]);
_(source: javascriptallonge.pdf (source-range-83ecb080-01070))_
