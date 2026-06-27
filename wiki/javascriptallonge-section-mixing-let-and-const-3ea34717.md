---
page_id: javascriptallonge-section-mixing-let-and-const-3ea34717
page_kind: source
summary: **mixing let and const**: 4 source-backed entries and 1 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-mixing-let-and-const-3ea34717@c61c38a379ba7a1137dca596ba26981d
---

# **mixing let and const**

From [[javascriptallonge]].

## Statements

- The suggestion is that shadowing a variable is confusing code. _(javascriptallonge.pdf (source-range-83ecb080-01784))_
- Shadowing a let with a const does not change our ability to rebind the variable in its original scope. _(javascriptallonge.pdf (source-range-83ecb080-01787))_
- Shadowing a const with a let does not permit it to be rebound in its original scope. _(javascriptallonge.pdf (source-range-83ecb080-01791))_

## Technical atoms

### Technical atom 1

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01785))_

> If you dislike deliberately shadowing variables, you’ll probably take an even more opprobrious view of mixing const and let semantics with a shadowed variable:
