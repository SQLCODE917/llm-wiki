---
page_id: javascriptallonge-section-values-and-identity-8050145d
page_kind: source
summary: values and identity: 11 source-backed entries and 3 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-values-and-identity-8050145d@a26d61eff66c61241054350ef58cdb51
---

# values and identity

From [[javascriptallonge]].

## Statements

- First, sometimes, the cups are of different kinds. One is a demitasse, the other a mug. This corresponds to comparing two things in JavaScript that have different types . For example, the string "2" is not the same thing as the number 2 . Strings and numbers are different types, so strings and numbers are never identical: _(javascriptallonge.pdf (source-range-31a4cf47-00122))_
- Second, sometimes, the cups are of the same type-perhaps two espresso cups-but they have different contents. One holds a single, one a double. This corresponds to comparing two JavaScript values that have the same type but different 'content.' For example, the number 5 is not the same thing as the number 2 . _(javascriptallonge.pdf (source-range-31a4cf47-00124))_
- For example, the string "2" is not the same thing as the number 2 . _(javascriptallonge.pdf (source-range-31a4cf47-00122))_
- This corresponds to comparing two JavaScript values that have the same type but different 'content.' For example, the number 5 is not the same thing as the number 2 . _(javascriptallonge.pdf (source-range-31a4cf47-00124))_

## Technical atoms

### Technical frame 1: values and identity

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00122))_

> First, sometimes, the cups are of different kinds. One is a demitasse, the other a mug. This corresponds to comparing two things in JavaScript that have different types . For example, the string "2" is not the same thing as the number 2 . Strings and numbers are different types, so strings and numbers are never identical:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00120))_

```
2 === 2 //=> true 'hello' !== 'goodbye' //=> true
```

### Technical frame 2: values and identity

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00124))_

> Second, sometimes, the cups are of the same type-perhaps two espresso cups-but they have different contents. One holds a single, one a double. This corresponds to comparing two JavaScript values that have the same type but different 'content.' For example, the number 5 is not the same thing as the number 2 .

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00123))_

```
2 === '2' //=> false true !== 'true' //=> true
```

### Technical frame 3: values and identity

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00124))_

> Second, sometimes, the cups are of the same type-perhaps two espresso cups-but they have different contents. One holds a single, one a double. This corresponds to comparing two JavaScript values that have the same type but different 'content.' For example, the number 5 is not the same thing as the number 2 .

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00125))_

```
true === false //=> false 2 !== 5 //=> true 'two' === 'five' //=> false
```
