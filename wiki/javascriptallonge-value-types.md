---
page_id: javascriptallonge-value-types
page_kind: source
summary: value types from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.22-22
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

JavaScript Allongé - A modular guide to JavaScript fundamentals and advanced techniques, covering value types and identity.

## Key supported claims

- Third, some types of cups have no distinguishing marks on them. If they are the same kind of cup, and they hold the same contents, we have no way to tell the difference between them. This is the case with the strings, numbers, and booleans we have seen so far. (raw/javascriptallonge.pdf p.22-22)
- Note well what is happening with these examples: Even when we obtain a string, number, or boolean as the result of evaluating an expression, it is identical to another value of the same type with the same 'content.' Strings, numbers, and booleans are examples of what JavaScript calls 'value' or 'primitive' types. We'll use both terms interchangeably. (raw/javascriptallonge.pdf p.22-22)
- So even if you have two cups of the same type, and their contents are the same, you can still distinguish between them. (raw/javascriptallonge.pdf p.22-22)

## Technical details

### `technical-atom-d40b2e0bf130325b` code

Citation: (raw/javascriptallonge.pdf p.22)

```javascript
2 + 2 === 4 //=> true (2 + 2 === 4) === (2 !== 5) //=> true
```

## Related technical details

### From [[javascriptallonge-values-and-identity]]: `technical-atom-ce645dd09a6b9040` worked-example

Relation: nearby source page; matched terms `content`, `have`, `identity`, `javascript`, `number`, `same`

Citation: (raw/javascriptallonge.pdf p.21)

This corresponds to comparing two JavaScript values that have the same type but different 'content.' For example, the number 5 is not the same thing as the number 2 .

### From [[javascriptallonge-floating]]: `technical-atom-54ca14d0839771d1` worked-example

Relation: nearby source page; matched terms `between`, `difference`, `javascript`, `some`, `what`, `when`

Citation: (raw/javascriptallonge.pdf p.25-26)

For example, when centering some text on a page, as long as the difference between what you might calculate longhand and JavaScript's calculation is less than a pixel, there is no observable error.

### From [[javascriptallonge-reference-types]]: `technical-atom-d255ca48e1a9dd4f` requirement

Relation: nearby source page; matched terms `contents`, `same`, `types`, `you`

Citation: (raw/javascriptallonge.pdf p.22-23)

Notice that you are always generating arrays with the same contents.

### From [[javascriptallonge-values-and-identity]]: `technical-atom-62ac41d9e7c334de` code

Relation: nearby source page; matched terms `identical`, `identity`, `javascript`, `they`, `two`

Citation: (raw/javascriptallonge.pdf p.21)

```
In JavaScript, we test whether two values are identical with the === operator, and whether they are not identical with the !== operator:
```
