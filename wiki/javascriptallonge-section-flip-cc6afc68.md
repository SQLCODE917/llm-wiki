---
page_id: javascriptallonge-section-flip-cc6afc68
page_kind: source
summary: Flip: 11 source-backed entries and 10 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-flip-cc6afc68@8b494aeebdcf74f264de160462d02710
---

# Flip

From [[javascriptallonge]].

## Statements

- What we have now is a function that takes a function and 'flips' the order of arguments around, then curries it. So let's call it flipAndCurry : _(javascriptallonge.pdf (source-range-8eb13d6b-01461))_
- What we have now is a function that takes a function and 'flips' the order of arguments around, then curries it. _(javascriptallonge.pdf (source-range-8eb13d6b-01461))_

## Technical atoms

### Technical frame 1: Flip

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01448))_

```
const mapWith = (fn) => (list) => list.map(fn);
```

### Technical frame 2: Flip

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01450))_

```
const mapWith = (fn) => (list) => map(list, fn);
```

### Technical frame 3: Flip

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01451))_

> You can see that if we simplify it:

### Technical frame 4: Flip

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01452))_

```
const mapWith = (fn, list) => map(list, fn);
```

### Technical frame 5: Flip

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01461))_

> What we have now is a function that takes a function and 'flips' the order of arguments around, then curries it. So let's call it flipAndCurry :

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01454))_

```
const mapper = (list) => (fn) => map(list, fn);
```

### Technical frame 6: Flip

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01461))_

> What we have now is a function that takes a function and 'flips' the order of arguments around, then curries it. So let's call it flipAndCurry :

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01456))_

```
const mapWith = (fn) => (list) => map(list, fn);
```

### Technical frame 7: Flip

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01461))_

> What we have now is a function that takes a function and 'flips' the order of arguments around, then curries it. So let's call it flipAndCurry :

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01458))_

```
const mapWith = (first) => (second) => map(second, first);
```

### Technical frame 8: Flip

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01461))_

> What we have now is a function that takes a function and 'flips' the order of arguments around, then curries it. So let's call it flipAndCurry :

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01460))_

```
const wrapper = (fn) => (first) => (second) => fn(second, first);
```

### Technical frame 9: Flip

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01461))_

> What we have now is a function that takes a function and 'flips' the order of arguments around, then curries it. So let's call it flipAndCurry :

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01463))_

```
const flipAndCurry = (fn) => (first) => (second) => fn(second, first); Sometimes you want to flip, but not curry: const flip = (fn) => (first, second) => fn(second, first); This is gold. Consider how we define mapWith now: var mapWith = flipAndCurry(map); Much nicer!
```

### Technical atom 10

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01461))_

> What we have now is a function that takes a function and 'flips' the order of arguments around, then curries it. So let's call it flipAndCurry :

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01462))_

| entry | content |
| --- | --- |
| 84 | https://github.com/raganwald/allong.es |
| 85 | http://underscorejs.org |

<details>
<summary>Raw table text</summary>

```
84 https://github.com/raganwald/allong.es
85 http://underscorejs.org
```

</details>
