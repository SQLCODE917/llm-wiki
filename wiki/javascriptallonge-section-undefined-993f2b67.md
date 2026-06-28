---
page_id: javascriptallonge-section-undefined-993f2b67
page_kind: source
summary: undefined: 15 source-backed entries and 3 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-undefined-993f2b67@74fd70d3af75b6d3355075345bbb036b
---

# undefined

From [[javascriptallonge]].

## Statements

- In JavaScript, the absence of a value is written undefined , and it means there is no value. It will crop up again. undefined is its own type of value, and it acts like a value type: _(javascriptallonge.pdf (source-range-31a4cf47-00221))_
- Like numbers, booleans and strings, JavaScript can print out the value undefined . _(javascriptallonge.pdf (source-range-31a4cf47-00224))_
- No matter how you evaluate undefined , you get an identical value back. undefined is a value that means 'I don't have a value.' But it's still a value :-) _(javascriptallonge.pdf (source-range-31a4cf47-00226))_
- 18 Sometimes, you will find JavaScript that has statements that are separated by newlines without semi-colons. This works because JavaScript has a feature that can infer where the semi-colons should be most of the time. We will not take advantage of this feature, but it's helpful to know it exists. _(javascriptallonge.pdf (source-range-31a4cf47-00227))_
- You might think that undefined in JavaScript is equivalent to NULL in SQL. No. In SQL, two things that are NULL are not equal to nor share the same identity, because two unknowns can't be equal. In JavaScript, every undefined is identical to every other undefined . _(javascriptallonge.pdf (source-range-31a4cf47-00228))_
- In JavaScript, the absence of a value is written undefined , and it means there is no value. _(javascriptallonge.pdf (source-range-31a4cf47-00221))_
- This works because JavaScript has a feature that can infer where the semi-colons should be most of the time. _(javascriptallonge.pdf (source-range-31a4cf47-00227))_
- In SQL, two things that are NULL are not equal to nor share the same identity, because two unknowns can't be equal. _(javascriptallonge.pdf (source-range-31a4cf47-00228))_

## Technical atoms

### Technical frame 1: undefined

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00224))_

> Like numbers, booleans and strings, JavaScript can print out the value undefined .

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00222))_

```
undefined
```

### Technical frame 2: undefined

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00224))_

> Like numbers, booleans and strings, JavaScript can print out the value undefined .

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00223))_

```
//=> undefined
```

### Technical frame 3: undefined

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00226))_

> No matter how you evaluate undefined , you get an identical value back. undefined is a value that means 'I don't have a value.' But it's still a value :-)

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00225))_

```
undefined === undefined //=> true (() => {})() === (() => {})() //=> true (() => {})() === undefined //=> true
```
