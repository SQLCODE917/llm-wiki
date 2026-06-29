---
page_id: javascriptallonge-section-or-even-the-simplest-possible-block-undefined-19cd59e5
page_kind: source
summary: Or even: / the simplest possible block / undefined: 15 source-backed entries and 3 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-29
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-or-even-the-simplest-possible-block-undefined-19cd59e5@7d50f04e15eba94734252e5c8aa61c96
---

# Or even: / the simplest possible block / undefined

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-or-even-the-simplest-possible-block-528c8472]] - broader source section: Or even: / the simplest possible block

## Statements

- In JavaScript, the absence of a value is written undefined , and it means there is no value. It will crop up again. undefined is its own type of value, and it acts like a value type: _(javascriptallonge.pdf (source-range-7239e085-00217))_
- Like numbers, booleans and strings, JavaScript can print out the value undefined . _(javascriptallonge.pdf (source-range-7239e085-00220))_
- No matter how you evaluate undefined , you get an identical value back. undefined is a value that means 'I don't have a value.' But it's still a value :-) _(javascriptallonge.pdf (source-range-7239e085-00222))_
- 18 Sometimes, you will find JavaScript that has statements that are separated by newlines without semi-colons. This works because JavaScript has a feature that can infer where the semi-colons should be most of the time. We will not take advantage of this feature, but it's helpful to know it exists. _(javascriptallonge.pdf (source-range-7239e085-00223))_
- You might think that undefined in JavaScript is equivalent to NULL in SQL. No. In SQL, two things that are NULL are not equal to nor share the same identity, because two unknowns can't be equal. In JavaScript, every undefined is identical to every other undefined . _(javascriptallonge.pdf (source-range-7239e085-00224))_
- In JavaScript, the absence of a value is written undefined , and it means there is no value. _(javascriptallonge.pdf (source-range-7239e085-00217))_
- This works because JavaScript has a feature that can infer where the semi-colons should be most of the time. _(javascriptallonge.pdf (source-range-7239e085-00223))_
- In SQL, two things that are NULL are not equal to nor share the same identity, because two unknowns can't be equal. _(javascriptallonge.pdf (source-range-7239e085-00224))_

## Technical atoms

### Technical frame 1: Or even: / the simplest possible block / undefined

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00220))_

> Like numbers, booleans and strings, JavaScript can print out the value undefined .

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00218))_

```
undefined
```

### Technical frame 2: Or even: / the simplest possible block / undefined

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00220))_

> Like numbers, booleans and strings, JavaScript can print out the value undefined .

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00219))_

```
//=> undefined
```

### Technical frame 3: Or even: / the simplest possible block / undefined

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00222))_

> No matter how you evaluate undefined , you get an identical value back. undefined is a value that means 'I don't have a value.' But it's still a value :-)

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00221))_

```
undefined === undefined
//=> true
(() => {})() === (() => {})()
//=> true
(() => {})() === undefined
//=> true
```
