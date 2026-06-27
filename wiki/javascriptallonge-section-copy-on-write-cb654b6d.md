---
page_id: javascriptallonge-section-copy-on-write-cb654b6d
page_kind: source
summary: **copy-on-write**: 1 source-backed entries and 1 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-copy-on-write-cb654b6d@49cdbbc4eadf12afb8f1697db763c873
---

# **copy-on-write**

From [[javascriptallonge]].

## Technical atoms

> Context: Why are we copying? In case we modify a child list. Ok, what if we do this: Make the copy when we know we are modifying the list. When do we know that? When we call set. We’ll restore our original definition for rest, but change set:
_(context: javascriptallonge.pdf (source-range-83ecb080-01885))_

> **const** rest = ({first, rest}) => rest;
_(source: javascriptallonge.pdf (source-range-83ecb080-01886))_
