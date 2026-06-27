---
page_id: javascriptallonge-section-closures-and-scope-36951343
page_kind: source
summary: **Closures and Scope**: 2 source-backed entries and 1 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-closures-and-scope-36951343@d5a4a4ed0129ee7df96f47d128a8e213
---

# **Closures and Scope**

From [[javascriptallonge]].

## Statements

- First off, let’s use what we learned above. _(javascriptallonge.pdf (source-range-83ecb080-00472))_

## Technical atoms

> Context: It’s time to see how a function within a function works: First off, let’s use what we learned above. Given ( _some function_ )( _some argument_ ), we know that we apply the function to the argument, create an environment, bind the value of the argument to the name, and evaluate the function’s expression. So we do that first with this code:
_(context: javascriptallonge.pdf (source-range-83ecb080-00470, source-range-83ecb080-00472))_

> - ((x) => (y) => x)(1)(2) _//=> 1_
_(source: javascriptallonge.pdf (source-range-83ecb080-00471))_
