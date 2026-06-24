---
page_id: javascriptallonge-reference-types
page_kind: source
summary: reference types from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.22-23
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

This chapter discusses reference types in JavaScript, particularly arrays, and how they are not identical even when they have the same contents.

## Key supported claims

- This is an expression, and you can combine [] with other expressions (raw/javascriptallonge.pdf p.22-23).
- When you type [1, 2, 3] or any of its variations, you are typing an expression that generates its own unique array that is not identical to any other array, even if that other array also looks like [1, 2, 3] (raw/javascriptallonge.pdf p.22-23).
- An array looks like this: [1, 2, 3] (raw/javascriptallonge.pdf p.22-23).

## Technical details

### `technical-atom-7e575d3c8c40b76b` code

Citation: (raw/javascriptallonge.pdf p.22-23)

```
[2-1, 2, 2+1] [1, 1+1, 1+1+1]
```

### `technical-atom-0e9f8149ade6173c` code

Citation: (raw/javascriptallonge.pdf p.22-23)

```
[2-1, 2, 2+1] === [1,2,3] [1,2,3] === [1, 2, 3] [1, 2, 3] === [1, 2, 3]
```

### `technical-atom-d255ca48e1a9dd4f` requirement

Citation: (raw/javascriptallonge.pdf p.22-23)

Notice that you are always generating arrays with the same contents.

## Related technical details

### From [[javascriptallonge-values-and-identity]]: `technical-atom-62ac41d9e7c334de` code

Relation: nearby source page; matched terms `identical`, `identity`, `javascript`, `not`, `they`

Citation: (raw/javascriptallonge.pdf p.21)

```
In JavaScript, we test whether two values are identical with the === operator, and whether they are not identical with the !== operator:
```

### From [[javascriptallonge-values-and-identity]]: `technical-atom-ce645dd09a6b9040` worked-example

Relation: nearby source page; matched terms `have`, `identity`, `javascript`, `not`, `same`, `type`

Citation: (raw/javascriptallonge.pdf p.21)

This corresponds to comparing two JavaScript values that have the same type but different 'content.' For example, the number 5 is not the same thing as the number 2 .

### From [[javascriptallonge-floating]]: `technical-atom-12967e399641f4b8` worked-example

Relation: nearby source page; matched terms `type`, `you`

Citation: (raw/javascriptallonge.pdf p.25-26)

For example, if you type 9007199254740991 + 9007199254740991 into node.js , it will happily report that the answer is 18014398509481982 .

### From [[javascriptallonge-operations-on-numbers]]: `technical-atom-d0aad52ee8c53e7f` worked-example

Relation: nearby source page; matched terms `can`, `even`, `expressions`, `like`

Citation: (raw/javascriptallonge.pdf p.26-27)

We can create expressions that look very much like mathematical expressions, for example we can write 1 + 1 or 2 * 3 or 42 34 or even 6 / 2 .
