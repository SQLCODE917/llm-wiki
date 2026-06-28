---
page_id: javascriptallonge-section-will-be-represented-as-7334da19
page_kind: source
summary: Will be represented as:: 5 source-backed entries and 3 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-will-be-represented-as-7334da19@3b8a1147b919ac24d2696bfd467d1c73
---

# Will be represented as:

From [[javascriptallonge]].

## Statements

- We can use a POJO to make a map from positions to moves. We'll use the [] notation for keys, it allows us to use any expression as a key, and JavaScript will convert it to a string. So if we write: _(javascriptallonge.pdf (source-range-31a4cf47-01913))_

## Technical atoms

### Technical frame 1: Will be represented as:

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01913))_

> We can use a POJO to make a map from positions to moves. We'll use the [] notation for keys, it allows us to use any expression as a key, and JavaScript will convert it to a string. So if we write:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01912))_

```
[ 'o', 'x', ' ', 'x', ' ', ' ', 'o', ' ', ' ' ]
```

### Technical frame 2: Will be represented as:

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01913))_

> We can use a POJO to make a map from positions to moves. We'll use the [] notation for keys, it allows us to use any expression as a key, and JavaScript will convert it to a string. So if we write:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01914))_

```
const moveLookupTable = { [[ ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ' ]]: 0, [[ 'o', 'x', ' ', ' ', ' ', ' ', ' ', ' ', ' ' ]]: 6, [[ 'o', 'x', 'x', ' ', ' ', ' ', 'o', ' ', ' ' ]]: 3, [[ 'o', 'x', ' ', 'x', ' ', ' ', 'o', ' ', ' ' ]]: 8, [[ 'o', 'x', ' ', ' ', 'x', ' ', 'o', ' ', ' '
```

### Technical frame 3: Will be represented as:

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01913))_

> We can use a POJO to make a map from positions to moves. We'll use the [] notation for keys, it allows us to use any expression as a key, and JavaScript will convert it to a string. So if we write:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01915))_

```
]]: 3, [[ 'o', 'x', ' ', ' ', ' ', 'x', 'o', ' ', ' ' ]]: 3, [[ 'o', 'x', ' ', ' ', ' ', ' ', 'o', 'x', ' ' ]]: 3, [[ 'o', 'x', ' ', ' ', ' ', ' ', 'o', ' ', 'x' ]]: 3 // ... };
```
