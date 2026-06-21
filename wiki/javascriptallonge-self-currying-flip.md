---
page_id: javascriptallonge-self-currying-flip
page_kind: source
summary: Summary of the self-currying flip concept from 'JavaScript Allongé'.
sources: raw/javascriptallonge.pdf p.196-196
updated: 2026-06-20
source_id: javascriptallonge.pdf
---

## Source record

Chapter on self-currying flip function in JavaScriptAllongé, covering flip function and argument order reversal.

## Key supported claims

- Sometimes we'll want to flip a function, but retain the flexibility to call it in its curried form (pass one parameter) or non-curried form (pass both). (raw/javascriptallonge.pdf p.196-196)
- Now if we write mapWith = flip(map) , we can call mapWith(fn, list) or mapWith(fn)(list) , our choice. (raw/javascriptallonge.pdf p.196-196)
