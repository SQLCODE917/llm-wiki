---
page_id: javascriptallonge-values-are-expressions
page_kind: source
summary: values are expressions from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.19-20
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

All values are expressions. The relationship between values and expressions is fundamental in JavaScript, illustrated through examples from a coffee shop and code.

## Key supported claims

- All values are expressions, as demonstrated by the example of a café Cubano, which is both an expression (you can use it to place an order) and a value (you get it back from the barista) (raw/javascriptallonge.pdf p.19-20).
- The number 42 is both an expression and a value in JavaScript; when typed into JavaScript, it returns the same value, just like the café Cubano example (raw/javascriptallonge.pdf p.19-20).
- In JavaScript, expressions are not values in and of themselves, unlike in some other languages like Lisp; for example, boiling water plus ground coffee is an expression but not a value (raw/javascriptallonge.pdf p.19-20).

## Technical details

### `technical-atom-5657b7a6b5da6242` code

Citation: (raw/javascriptallonge.pdf p.19-20)

```javascript
42 //=> 42
```

### `technical-atom-94a23ea65dd6d731` code

Citation: (raw/javascriptallonge.pdf p.19-20)

```javascript
"JavaScript" + " " + "Allonge" //=> "JavaScript Allonge"
```

### `technical-atom-50e1175a0913d352` worked-example

Citation: (raw/javascriptallonge.pdf p.19-20)

Now we know what was missing with our 'coffee grounds plus hot water' example.

## Related technical details

### From [[javascriptallonge-values-and-identity]]: `technical-atom-ce645dd09a6b9040` worked-example

Relation: nearby source page; matched terms `but`, `example`, `identity`, `javascript`, `not`, `number`

Citation: (raw/javascriptallonge.pdf p.21)

This corresponds to comparing two JavaScript values that have the same type but different 'content.' For example, the number 5 is not the same thing as the number 2 .

### From [[javascriptallonge-values-and-identity]]: `technical-atom-29882a09023a1a70` worked-example

Relation: nearby source page; matched terms `example`, `identity`, `not`, `number`, `same`, `values`

Citation: (raw/javascriptallonge.pdf p.21)

For example, the string "2" is not the same thing as the number 2 .

### From [[javascriptallonge-values-and-identity]]: `technical-atom-62ac41d9e7c334de` code

Relation: nearby source page; matched terms `code`, `identity`, `javascript`, `not`, `values`

Citation: (raw/javascriptallonge.pdf p.21)

```
In JavaScript, we test whether two values are identical with the === operator, and whether they are not identical with the !== operator:
```

### From [[javascriptallonge-why-the-six-edition]]: `technical-atom-4a46581d403c3e4f` worked-example

Relation: nearby source page; matched terms `example`, `javascript`, `not`

Citation: (raw/javascriptallonge.pdf p.7-9)

For example, JavaScript did not include block-structured variables.
