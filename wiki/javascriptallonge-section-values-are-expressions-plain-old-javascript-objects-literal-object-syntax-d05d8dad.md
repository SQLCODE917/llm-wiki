---
page_id: javascriptallonge-section-values-are-expressions-plain-old-javascript-objects-literal-object-syntax-d05d8dad
page_kind: source
summary: values are expressions / Plain Old JavaScript Objects / literal object syntax: 8 source-backed entries and 4 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-values-are-expressions-plain-old-javascript-objects-literal-object-syntax-d05d8dad@1d02399fa9a94db7cb35ad752426d727
---

# values are expressions / Plain Old JavaScript Objects / literal object syntax

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-values-are-expressions-plain-old-javascript-objects-cc77db27]] - broader source section

## Statements

- JavaScript has a literal syntax for creating objects. _(javascriptallonge.pdf (source-range-83ecb080-01080))_
- Names needn’t be alphanumeric strings. _(javascriptallonge.pdf (source-range-83ecb080-01087))_
- If the name is an alphanumeric string conforming to the same rules as names of variables, there’s a simplified syntax for accessing the values: _(javascriptallonge.pdf (source-range-83ecb080-01089))_
- Expressions can be used for keys as well. _(javascriptallonge.pdf (source-range-83ecb080-01092))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01081))_

> { year: 2012, month: 6, day: 14 } Two objects created with separate evaluations have differing identities, just like arrays:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01082))_

> - { year: 2012, month: 6, day: 14 } === { year: 2012, month: 6, day: 14 } _//=> false_

### Technical atom 2

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01083))_

> Objects use [] to access the values by name, using a string:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01084))_

> - { year: 2012, month: 6, day: 14 }['day'] _//=> 14_

### Technical atom 3

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01083))_

> Objects use [] to access the values by name, using a string:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01086))_

> - o['a'] === x && o['b'] === y && o['c'] === z _//=> true_

### Technical atom 4

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01089))_

> If the name is an alphanumeric string conforming to the same rules as names of variables, there’s a simplified syntax for accessing the values:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01091))_

> 111 **const** date = { year: 2012, month: 6, day: 14 }; date['day'] === date.day _//=> true_
