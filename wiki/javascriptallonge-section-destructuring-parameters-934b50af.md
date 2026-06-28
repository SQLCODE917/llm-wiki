---
page_id: javascriptallonge-section-destructuring-parameters-934b50af
page_kind: source
summary: destructuring parameters: 7 source-backed entries and 3 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-destructuring-parameters-934b50af@cf563cea1fd4929d29b6bdbfa96b9de2
---

# destructuring parameters

From [[javascriptallonge]].

## Statements

- It looks like destructuring. It acts like destructuring. There is only one difference: We have not tried gathering. Let's do that: _(javascriptallonge.pdf (source-range-31a4cf47-00878))_
- Gathering works with parameters! This is very useful indeed, and we'll see more of it in a moment. 59 _(javascriptallonge.pdf (source-range-31a4cf47-00880))_
- 59 Gathering in parameters has a long history, and the usual terms are to call gathering 'pattern matching' and to call a name that is bound to gathered values a 'rest parameter.' The term 'rest' is perfectly compatible with gather: 'Rest' is the noun, and 'gather' is the verb. We gather the rest of the parameters. _(javascriptallonge.pdf (source-range-31a4cf47-00881))_
- There is only one difference: We have not tried gathering. _(javascriptallonge.pdf (source-range-31a4cf47-00878))_

## Technical atoms

### Technical frame 1: destructuring parameters

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00878))_

> It looks like destructuring. It acts like destructuring. There is only one difference: We have not tried gathering. Let's do that:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00875))_

```
foo() bar("smaug") baz(1, 2, 3)
```

### Technical frame 2: destructuring parameters

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00878))_

> It looks like destructuring. It acts like destructuring. There is only one difference: We have not tried gathering. Let's do that:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00877))_

```
const foo = () => ... const bar = (name) => ... const baz = (a, b, c) => ...
```

### Technical frame 3: destructuring parameters

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00880))_

> Gathering works with parameters! This is very useful indeed, and we'll see more of it in a moment. 59

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00879))_

```
const numbers = (...nums) => nums; numbers(1, 2, 3, 4, 5) //=> [1,2,3,4,5] const headAndTail = (head, ...tail) => [head, tail]; headAndTail(1, 2, 3, 4, 5) //=> [1,[2,3,4,5]]
```
