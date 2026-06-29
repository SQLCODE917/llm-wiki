---
page_id: javascriptallonge-section-will-be-represented-as-4332c18a
page_kind: source
summary: Will be represented as:: 5 source-backed entries and 3 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-29
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-will-be-represented-as-4332c18a@38f209eb1a7a86269880c5417a99c833
---

# Will be represented as:

From [[javascriptallonge]].

## Statements

- We can use a POJO to make a map from positions to moves. We'll use the [] notation for keys, it allows us to use any expression as a key, and JavaScript will convert it to a string. So if we write: _(javascriptallonge.pdf (source-range-7239e085-01912))_

## Technical atoms

### Technical frame 1: Will be represented as:

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01912))_

> We can use a POJO to make a map from positions to moves. We'll use the [] notation for keys, it allows us to use any expression as a key, and JavaScript will convert it to a string. So if we write:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01911))_

```
[
'o', 'x', ' ',
'x', ' ', ' ',
'o', ' ', ' '
]
```

### Technical frame 2: Will be represented as:

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01912))_

> We can use a POJO to make a map from positions to moves. We'll use the [] notation for keys, it allows us to use any expression as a key, and JavaScript will convert it to a string. So if we write:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01913))_

```
const moveLookupTable = {
[[
' ', ' ', ' ',
' ', ' ', ' ',
' ', ' ', ' '
]]: 0,
[[
'o', 'x', ' ',
' ', ' ', ' ',
' ', ' ', ' '
]]: 6,
[[
'o', 'x', 'x',
' ', ' ', ' ',
'o', ' ', ' '
]]: 3,
[[
'o', 'x', ' ',
'x', ' ', ' ',
'o', ' ', ' '
]]: 8,
[[
'o', 'x', ' ',
' ', 'x', ' ',
'o', ' ', ' '
```

### Technical frame 3: Will be represented as:

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01912))_

> We can use a POJO to make a map from positions to moves. We'll use the [] notation for keys, it allows us to use any expression as a key, and JavaScript will convert it to a string. So if we write:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01914))_

```
]]: 3,
[[
'o', 'x', ' ',
' ', ' ', 'x',
'o', ' ', ' '
]]: 3,
[[
'o', 'x', ' ',
' ', ' ', ' ',
'o', 'x', ' '
]]: 3,
[[
'o', 'x', ' ',
' ', ' ', ' ',
'o', ' ', 'x'
]]: 3
// ...
};
```
