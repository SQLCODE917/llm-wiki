---
page_id: javascriptallonge-section-representing-naughts-and-crosses-as-a-stateless-function-a924b35d
page_kind: source
summary: **representing naughts and crosses as a stateless function**: 7 source-backed entries and 2 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-representing-naughts-and-crosses-as-a-stateless-function-a924b35d@70be159601c11943fdc88a5a3099ad93
---

# **representing naughts and crosses as a stateless function**

From [[javascriptallonge]].

## Statements

- We could plays naughts and crosses as a stateless function. _(javascriptallonge.pdf (source-range-83ecb080-02952))_
- We encode each position of the board in some fashion, and then we build a dictionary from positions to moves. _(javascriptallonge.pdf (source-range-83ecb080-02952))_
- We can encode the board in several different ways. _(javascriptallonge.pdf (source-range-83ecb080-02962))_
- We’ll use the [] notation for keys, it allows us to use any expression as a key, and JavaScript will convert it to a string. _(javascriptallonge.pdf (source-range-83ecb080-02973))_
- We can use a POJO to make a map from positions to moves. _(javascriptallonge.pdf (source-range-83ecb080-02973))_

## Technical atoms

> Context: And if we want to look up what move to make, we can write:
_(context: javascriptallonge.pdf (source-range-83ecb080-02984))_

> 'o', 'x', ' ', ' ' ' ' ' ' , , , 'o', 'x', ' ' _//=> 3_
_(source: javascriptallonge.pdf (source-range-83ecb080-02986))_

> 'o', 'x', ' ', ' ' ' ' ' ' , , , 'o', 'x', ' ' ]) _//=> 3_
_(source: javascriptallonge.pdf (source-range-83ecb080-02992))_
