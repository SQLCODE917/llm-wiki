---
page_id: javascriptallonge-section-and-also-that-constant-coffee-craving-nested-blocks-e1d3b152
page_kind: source
summary: And also: / That Constant Coffee Craving / nested blocks: 12 source-backed entries and 6 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-29
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-and-also-that-constant-coffee-craving-nested-blocks-e1d3b152@f75cfa5712d56e955ec53d8ea5e5cbd1
---

# And also: / That Constant Coffee Craving / nested blocks

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-and-also-that-constant-coffee-craving-7d1b2fd1]] - broader source section: And also: / That Constant Coffee Craving

## Statements

- Up to now, we've only ever seen blocks we use as the body of functions. But there are other kinds of blocks. One of the places you can find blocks is in an if statement. In JavaScript, an if statement looks like this: _(javascriptallonge.pdf (source-range-7239e085-00438))_
- The if statement is a statement, not an expression (an unfortunate design choice), and its clauses are statements or blocks. So we could also write something like: _(javascriptallonge.pdf (source-range-7239e085-00442))_
- We've used a block as the else clause, and since it's a block, we've placed a const statement inside it. _(javascriptallonge.pdf (source-range-7239e085-00446))_
- Up to now, we've only ever seen blocks we use as the body of functions. _(javascriptallonge.pdf (source-range-7239e085-00438))_
- We've used a block as the else clause, and since it's a block, we've placed a const statement inside it. _(javascriptallonge.pdf (source-range-7239e085-00446))_

## Technical atoms

### Technical frame 1: And also: / That Constant Coffee Craving / nested blocks

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00442))_

> The if statement is a statement, not an expression (an unfortunate design choice), and its clauses are statements or blocks. So we could also write something like:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00438))_

> One of the places you can find blocks is in an if statement.

### Technical frame 2: And also: / That Constant Coffee Craving / nested blocks

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00442))_

> The if statement is a statement, not an expression (an unfortunate design choice), and its clauses are statements or blocks. So we could also write something like:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00439))_

```
(n) => {
const even = (x) => {
if (x === 0)
return true;
else
return !even(x - 1);
}
return even(n)
}
```

### Technical frame 3: And also: / That Constant Coffee Craving / nested blocks

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00442))_

> The if statement is a statement, not an expression (an unfortunate design choice), and its clauses are statements or blocks. So we could also write something like:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00441))_

```
((n) => {
const even = (x) => {
if (x === 0)
return true;
else
return !even(x - 1);
}
return even(n)
})(13)
//=> false
```

### Technical frame 4: And also: / That Constant Coffee Craving / nested blocks

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00446))_

> We've used a block as the else clause, and since it's a block, we've placed a const statement inside it.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00443))_

```
(n) => {
const even = (x) => {
if (x === 0)
return true;
else {
const odd = (y) => !even(y);
return odd(x - 1);
}
```

### Technical frame 5: And also: / That Constant Coffee Craving / nested blocks

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00446))_

> We've used a block as the else clause, and since it's a block, we've placed a const statement inside it.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00444))_

```
}
return even(n)
}
And this also works:
((n) => {
const even = (x) => {
if (x === 0)
return true;
else {
const odd = (y) => !even(y);
return odd(x - 1);
}
}
return even(n)
})(42)
```

### Technical frame 6: And also: / That Constant Coffee Craving / nested blocks

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00446))_

> We've used a block as the else clause, and since it's a block, we've placed a const statement inside it.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00445))_

```
//=> true
```
