---
page_id: javascriptallonge-section-destructuring-objects-9c37a2b6
page_kind: source
summary: **destructuring objects**: 5 source-backed entries and 3 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-destructuring-objects-9c37a2b6@5dae60691af7f5a4de88e0f0fbe8db53
---

# **destructuring objects**

From [[javascriptallonge]].

## Statements

- It is very common to write things like title: title when destructuring objects. _(javascriptallonge.pdf (source-range-83ecb080-01636))_
- When the label is a valid variable name, it’s often the most obvious variable name as well. _(javascriptallonge.pdf (source-range-83ecb080-01636))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01627))_

> And we can also write:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01629))_

> surname _//=> "Braithwaite"_ title _//=> "Author"_

### Technical atom 2

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01636))_

> Terrible grammar and capitalization, but let’s move on. It is very common to write things like title: title when destructuring objects. When the label is a valid variable name, it’s often the most obvious variable name as well. So JavaScript supports a further syntactic optimization:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01637))_

> **const** description = ({name: { first }, occupation: { title } }) => ` **${** first **}** is a **${** title **}** `;

### Technical atom 3

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01640))_

> And that same syntax works for literals:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01641))_

> **const** abbrev = ({name: { first, last }, occupation: { title } }) => { **return** { first, last, title}; } abbrev(user)
