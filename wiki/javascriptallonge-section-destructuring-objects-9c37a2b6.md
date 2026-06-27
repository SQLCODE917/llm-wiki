---
page_id: javascriptallonge-section-destructuring-objects-9c37a2b6
page_kind: source
summary: **destructuring objects**: 5 source-backed entries and 3 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-destructuring-objects-9c37a2b6@dffa6ca40a66f745a0e3f8f545273b0b
---

# **destructuring objects**

From [[javascriptallonge]].

## Statements

- It is very common to write things like title: title when destructuring objects. _(javascriptallonge.pdf (source-range-83ecb080-01636))_
- When the label is a valid variable name, it’s often the most obvious variable name as well. _(javascriptallonge.pdf (source-range-83ecb080-01636))_

## Technical atoms

> Context: And we can also write:
_(context: javascriptallonge.pdf (source-range-83ecb080-01627))_

> surname _//=> "Braithwaite"_ title _//=> "Author"_
_(source: javascriptallonge.pdf (source-range-83ecb080-01629))_

> Context: Terrible grammar and capitalization, but let’s move on. It is very common to write things like title: title when destructuring objects. When the label is a valid variable name, it’s often the most obvious variable name as well. So JavaScript supports a further syntactic optimization:
_(context: javascriptallonge.pdf (source-range-83ecb080-01636))_

> **const** description = ({name: { first }, occupation: { title } }) => ` **${** first **}** is a **${** title **}** `;
_(source: javascriptallonge.pdf (source-range-83ecb080-01637))_

> Context: And that same syntax works for literals:
_(context: javascriptallonge.pdf (source-range-83ecb080-01640))_

> **const** abbrev = ({name: { first, last }, occupation: { title } }) => { **return** { first, last, title}; } abbrev(user)
_(source: javascriptallonge.pdf (source-range-83ecb080-01641))_
