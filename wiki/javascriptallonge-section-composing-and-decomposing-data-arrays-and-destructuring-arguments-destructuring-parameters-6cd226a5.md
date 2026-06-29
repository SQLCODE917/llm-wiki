---
page_id: javascriptallonge-section-composing-and-decomposing-data-arrays-and-destructuring-arguments-destructuring-parameters-6cd226a5
page_kind: source
summary: Composing and Decomposing Data / Arrays and Destructuring Arguments / destructuring parameters: 7 source-backed entries and 3 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-29
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-composing-and-decomposing-data-arrays-and-destructuring-arguments-destructuring-parameters-6cd226a5@a63e2f6779c7da7d00c37a720412af23
---

# Composing and Decomposing Data / Arrays and Destructuring Arguments / destructuring parameters

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-composing-and-decomposing-data-arrays-and-destructuring-arguments-c1f61fb6]] - broader source section: Composing and Decomposing Data / Arrays and Destructuring Arguments

## Statements

- It looks like destructuring. It acts like destructuring. There is only one difference: We have not tried gathering. Let's do that: _(javascriptallonge.pdf (source-range-7239e085-00878))_
- Gathering works with parameters! This is very useful indeed, and we'll see more of it in a moment. 59 _(javascriptallonge.pdf (source-range-7239e085-00880))_
- 59 Gathering in parameters has a long history, and the usual terms are to call gathering 'pattern matching' and to call a name that is bound to gathered values a 'rest parameter.' The term 'rest' is perfectly compatible with gather: 'Rest' is the noun, and 'gather' is the verb. We gather the rest of the parameters. _(javascriptallonge.pdf (source-range-7239e085-00881))_
- There is only one difference: We have not tried gathering. _(javascriptallonge.pdf (source-range-7239e085-00878))_

## Technical atoms

### Technical frame 1: Composing and Decomposing Data / Arrays and Destructuring Arguments / destructuring parameters

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00878))_

> It looks like destructuring. It acts like destructuring. There is only one difference: We have not tried gathering. Let's do that:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00875))_

```
foo()
bar("smaug")
baz(1, 2, 3)
```

### Technical frame 2: Composing and Decomposing Data / Arrays and Destructuring Arguments / destructuring parameters

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00878))_

> It looks like destructuring. It acts like destructuring. There is only one difference: We have not tried gathering. Let's do that:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00877))_

```
const foo = () => ...
const bar = (name) => ...
const baz = (a, b, c) => ...
```

### Technical frame 3: Composing and Decomposing Data / Arrays and Destructuring Arguments / destructuring parameters

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00880))_

> Gathering works with parameters! This is very useful indeed, and we'll see more of it in a moment. 59

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00879))_

```
const numbers = (...nums) => nums;
numbers(1, 2, 3, 4, 5)
//=> [1,2,3,4,5]
const headAndTail = (head, ...tail) => [head, tail];
headAndTail(1, 2, 3, 4, 5)
//=> [1,[2,3,4,5]]
```
