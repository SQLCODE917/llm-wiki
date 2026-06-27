---
page_id: javascriptallonge-section-literal-object-syntax-2d1e00bd
page_kind: source
summary: **literal object syntax**: 19 source-backed entries and 10 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-literal-object-syntax-2d1e00bd@dbd12f67b6172a671acf6bcc5944f340
---

# **literal object syntax**

From [[javascriptallonge]].

## Statements

- JavaScript has a literal syntax for creating objects. _(javascriptallonge.pdf (source-range-83ecb080-01590))_
- Values contained within an object work just like values contained within an array, we access them by reference to the original: _(javascriptallonge.pdf (source-range-83ecb080-01596))_
- Values contained within an object work just like values contained within an array, we access them by reference to the original: _(javascriptallonge.pdf (source-range-83ecb080-01596))_
- Names needn’t be alphanumeric strings. _(javascriptallonge.pdf (source-range-83ecb080-01602))_
- If the name is an alphanumeric string conforming to the same rules as names of variables, there’s a simplified syntax for accessing the values: _(javascriptallonge.pdf (source-range-83ecb080-01604))_
- Expressions can be used for keys as well. _(javascriptallonge.pdf (source-range-83ecb080-01609))_
- It is very common to associate named function expressions with keys in objects, and there is a “compact method syntax” for binding named function expressions to keywords: _(javascriptallonge.pdf (source-range-83ecb080-01618))_
- (There are some other technical differences between binding a named function expression and using _(javascriptallonge.pdf (source-range-83ecb080-01620))_
- compact method syntax, but they are not relevant here. _(javascriptallonge.pdf (source-range-83ecb080-01623))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01592))_

> Two objects created with separate evaluations have differing identities, just like arrays:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01593))_

> - { year: 2012, month: 6, day: 14 } === { year: 2012, month: 6, day: 14 } _//=> false_

### Technical atom 2

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01594))_

> Objects use [] to access the values by name, using a string:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01595))_

> - { year: 2012, month: 6, day: 14 }['day'] _//=> 14_

### Technical atom 3

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01596))_

> Values contained within an object work just like values contained within an array, we access them by reference to the original:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01598))_

> - x = unique(),

### Technical atom 4

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01596))_

> Values contained within an object work just like values contained within an array, we access them by reference to the original:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01599))_

> - y = unique(),

### Technical atom 5

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01600))_

> - z = unique(), o = { a: x, b: y, c: z };

### Technical atom 6

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01601))_

> - o['a'] === x && o['b'] === y && o['c'] === z _//=> true_

### Technical atom 7

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01604))_

> If the name is an alphanumeric string conforming to the same rules as names of variables, there’s a simplified syntax for accessing the values:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01607))_

> **const** date = { year: 2012, month: 6, day: 14 };

### Technical atom 8

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01608))_

> date['day'] === date.day _//=> true_

### Technical atom 9

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01609))_

> Expressions can be used for keys as well. The syntax is to enclose the key’s expression in [ and ]:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01610))_

> { ["p" + "i"]: 3.14159265 } _//=> {"pi":3.14159265}_

### Technical atom 10

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01611))_

> All containers can contain any value, including functions or other containers, like a fat arrow function:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01612))_

> **const** Mathematics = { abs: (a) => a < 0 ? -a : a }; Mathematics.abs(-5) _//=> 5_
