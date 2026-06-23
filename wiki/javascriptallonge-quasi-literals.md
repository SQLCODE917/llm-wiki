---
page_id: javascriptallonge-quasi-literals
page_kind: source
summary: quasi-literals from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.203-204
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

Chapter on quasi-literals in JavaScript Allongé, covering template strings and string interpolation expressions.

## Key supported claims

- Quasi-literal strings are denoted with back quotes and resemble string literals, e.g., `foobar` (raw/javascriptallonge.pdf p.203-204).
- Quasi-literals can contain expressions to be evaluated with ${expression}, and are computationally equivalent to expressions using + (raw/javascriptallonge.pdf p.203-204).
- Quasi-literals go much further and are easier to read, avoiding errors like concatenating without spaces (raw/javascriptallonge.pdf p.203-204).

## Technical details

### `technical-atom-bed3953b28b96e6e` code

Citation: (raw/javascriptallonge.pdf p.203-204)

```javascript
`foobar` //=> 'foobar' `fizz` + `buzz` //=> 'fizzbuzz'
```

### `technical-atom-29b1b123d8e45648` code

Citation: (raw/javascriptallonge.pdf p.203-204)

```javascript
`A popular number for nerds is ${ 40 + 2 } ` //=> 'A popular number for nerds is 42'
```

### `technical-atom-88bd9e0b4e57da74` code

Citation: (raw/javascriptallonge.pdf p.203-204)

```javascript
'A popular number for nerds is ' + (40 + 2) //=> 'A popular number for nerds is 42'
```

### `technical-atom-02f4aea8e109eb5d` code

Citation: (raw/javascriptallonge.pdf p.203-204)

```javascript
'A popular number for nerds is' + (40 + 2) //=> 'A popular number for nerds is42'
```

### `technical-atom-46fa8cdbb930a009` code

Citation: (raw/javascriptallonge.pdf p.203-204)

```
Old-school lispers call this 'unquoting,' the more contemporary term is 'interpolation.' An unquoted expression is inserted in a quasi-literal with ${expression} .
```

### `technical-atom-0397927ede51fe53` procedure

Citation: (raw/javascriptallonge.pdf p.203-204)

The expression is evaluated, and the result is coerced to a string, then inserted in the quasi-string.
