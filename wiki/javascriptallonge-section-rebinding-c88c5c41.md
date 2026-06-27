---
page_id: javascriptallonge-section-rebinding-c88c5c41
page_kind: source
summary: **rebinding**: 3 source-backed entries and 0 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-rebinding-c88c5c41@1e807b202db221b56c206427f3a5805d
---

# **rebinding**

From [[javascriptallonge]].

## Statements

- JavaScript does not permit us to rebind a name that has been bound with const. _(javascriptallonge.pdf (source-range-83ecb080-00688))_
- We can _shadow_ it by using const to declare a new binding with a new function or block scope, but we cannot rebind a name that was bound with const in an existing scope. _(javascriptallonge.pdf (source-range-83ecb080-00688))_
- This is valuable, as it greatly simplifies the analysis of programs to see at a glance that when something is bound with const, we need never worry that its value may change. _(javascriptallonge.pdf (source-range-83ecb080-00689))_
