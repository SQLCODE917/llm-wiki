---
page_id: javascriptallonge-section-operations-on-numbers-c424d882
page_kind: source
summary: operations on numbers: 6 source-backed entries and 2 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-operations-on-numbers-c424d882@ef92702ae8db8c1e19939edab01ef452
---

# operations on numbers

From [[javascriptallonge]].

## Statements

- As we've seen, JavaScript has many common arithmetic operators. We can create expressions that look very much like mathematical expressions, for example we can write 1 + 1 or 2 * 3 or 42 34 or even 6 / 2 . These can be combined to make more complex expressions, like 2 * 5 + 1 . _(javascriptallonge.pdf (source-range-8eb13d6b-00161))_
- In JavaScript, operators have an order of precedence designed to mimic the way humans typically parse written arithmetic. So: _(javascriptallonge.pdf (source-range-8eb13d6b-00162))_
- JavaScript treats the expressions as if we had written (2 * 5) + 1 and 1 + (5 * 2) , because the * operator has a higher precedence than the + operator. JavaScript has many more operators. In a sense, they behave like little functions. If we write 1 + 2 , this is conceptually similar to writing plus(1, 2) (assuming we have a function that adds two numbers bound to the name plus , of course). _(javascriptallonge.pdf (source-range-8eb13d6b-00164))_

## Technical atoms

### Technical frame 1: operations on numbers

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00164))_

> JavaScript treats the expressions as if we had written (2 * 5) + 1 and 1 + (5 * 2) , because the * operator has a higher precedence than the + operator. JavaScript has many more operators. In a sense, they behave like little functions. If we write 1 + 2 , this is conceptually similar to writing plus(1, 2) (assuming we have a function that adds two numbers bound to the name plus , of course).

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00163))_

```
2 * 5 + 1 //=> 11 1 + 5 * 2 //=> 11
```

### Technical frame 2: operations on numbers

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00164))_

> JavaScript treats the expressions as if we had written (2 * 5) + 1 and 1 + (5 * 2) , because the * operator has a higher precedence than the + operator. JavaScript has many more operators. In a sense, they behave like little functions. If we write 1 + 2 , this is conceptually similar to writing plus(1, 2) (assuming we have a function that adds two numbers bound to the name plus , of course).

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00167))_

> [Figure] (p.27)
