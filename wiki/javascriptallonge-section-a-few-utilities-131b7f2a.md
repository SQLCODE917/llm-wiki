---
page_id: javascriptallonge-section-a-few-utilities-131b7f2a
page_kind: source
summary: **a few utilities**: 4 source-backed entries and 1 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-a-few-utilities-131b7f2a@145aae683b5e1b915f6e7d0eca789935
---

# **a few utilities**

From [[javascriptallonge]].

## Statements

- before we go any further, let’s write a few naïve list utilities so that we can work at a slightly higher level of abstraction: _(javascriptallonge.pdf (source-range-83ecb080-01865))_
- before we go any further, let’s write a few naïve list utilities so that we can work at a slightly higher level of abstraction: _(javascriptallonge.pdf (source-range-83ecb080-01865))_
- The main difference is that array[index] = value evaluates to value, while set(index, value, list) evaluates to the modified list. _(javascriptallonge.pdf (source-range-83ecb080-01873))_

## Technical atoms

> Context: **const** copy = (node, head = **null** , tail = **null** ) => { **if** (node === EMPTY) { **return** head; } **else if** (tail === **null** ) { **const** { first, rest } = node; **const** newNode = { first, rest }; **return** copy(rest, newNode, newNode); } **else** { **const** { first, rest } = node; **const** newNode = { first, rest }; tail.rest = newNode; **return** copy(node.rest, head, newNode); } } **const** first = ({first, rest}) => first; **const** rest = ({first, rest}) => rest; **con
_(context: javascriptallonge.pdf (source-range-83ecb080-01868))_

> **const** childList = rest(parentList);
_(source: javascriptallonge.pdf (source-range-83ecb080-01871))_
