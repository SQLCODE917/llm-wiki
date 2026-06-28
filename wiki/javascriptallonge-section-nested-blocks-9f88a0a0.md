---
page_id: javascriptallonge-section-nested-blocks-9f88a0a0
page_kind: source
summary: nested blocks: 12 source-backed entries and 6 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-nested-blocks-9f88a0a0@1e7c960b00d413411bba94789b910e84
---

# nested blocks

From [[javascriptallonge]].

## Statements

- Up to now, we've only ever seen blocks we use as the body of functions. But there are other kinds of blocks. One of the places you can find blocks is in an if statement. In JavaScript, an if statement looks like this: _(javascriptallonge.pdf (source-range-31a4cf47-00441))_
- The if statement is a statement, not an expression (an unfortunate design choice), and its clauses are statements or blocks. So we could also write something like: _(javascriptallonge.pdf (source-range-31a4cf47-00445))_
- We've used a block as the else clause, and since it's a block, we've placed a const statement inside it. _(javascriptallonge.pdf (source-range-31a4cf47-00449))_
- Up to now, we've only ever seen blocks we use as the body of functions. _(javascriptallonge.pdf (source-range-31a4cf47-00441))_
- We've used a block as the else clause, and since it's a block, we've placed a const statement inside it. _(javascriptallonge.pdf (source-range-31a4cf47-00449))_

## Technical atoms

### Technical frame 1: nested blocks

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00445))_

> The if statement is a statement, not an expression (an unfortunate design choice), and its clauses are statements or blocks. So we could also write something like:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00441))_

> One of the places you can find blocks is in an if statement.

### Technical frame 2: nested blocks

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00445))_

> The if statement is a statement, not an expression (an unfortunate design choice), and its clauses are statements or blocks. So we could also write something like:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00442))_

```
(n) => { const even = (x) => { if (x === 0) return true ; else return !even(x - 1); } return even(n) }
```

### Technical frame 3: nested blocks

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00445))_

> The if statement is a statement, not an expression (an unfortunate design choice), and its clauses are statements or blocks. So we could also write something like:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00444))_

```
((n) => { const even = (x) => { if (x === 0) return true ; else return !even(x - 1); } return even(n) })(13) //=> false
```

### Technical frame 4: nested blocks

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00449))_

> We've used a block as the else clause, and since it's a block, we've placed a const statement inside it.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00446))_

```
(n) => { const even = (x) => { if (x === 0) return true ; else { const odd = (y) => !even(y); return odd(x - 1); }
```

### Technical frame 5: nested blocks

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00449))_

> We've used a block as the else clause, and since it's a block, we've placed a const statement inside it.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00447))_

```
} return even(n) } And this also works: ((n) => { const even = (x) => { if (x === 0) return true ; else { const odd = (y) => !even(y); return odd(x - 1); } } return even(n) })(42)
```

### Technical frame 6: nested blocks

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00449))_

> We've used a block as the else clause, and since it's a block, we've placed a const statement inside it.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00448))_

```
//=> true
```
