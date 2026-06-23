---
page_id: javascriptallonge-a-rich-aroma-basic-numbers
page_kind: source
summary: A Rich Aroma: Basic Numbers from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.24-25
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

Chapter on basic numbers in JavaScriptAllonge, covering literals, representations, and numeric types.

## Key supported claims

- Internally, both 042 and 34 have the same representation, as double-precision floating point numbers. (raw/javascriptallonge.pdf p.24-25)
- A computer's internal representation for numbers is important to understand. (raw/javascriptallonge.pdf p.24-25)
- The machine's representation of a number almost never lines up perfectly with our understanding of how a number behaves, and thus there will be places where the computer's behaviour surprises us if we don't know a little about what it's doing 'under the hood.' (raw/javascriptallonge.pdf p.24-25)
- We saw that an expression consisting solely of numbers, like 42 , is a literal. (raw/javascriptallonge.pdf p.24-25)
- Almost all programming languages have notations for atomic values such as integers, floating-point numbers, and strings, and usually for booleans and characters; some also have notations for elements of enumerated types and compound values such as arrays, records, and objects. (raw/javascriptallonge.pdf p.24-25)

## Technical details

### `technical-atom-d45aace5472aaf85` worked-example

Citation: (raw/javascriptallonge.pdf p.24-25)

For example, the largest integer JavaScript can safely 14 handle is 9007199254740991 , or 2 '53' - 1 .

### `technical-atom-2cf4c49c142c3894` exception

Citation: (raw/javascriptallonge.pdf p.24-25)

Like most programming languages, JavaScript does not allow us to use commas to separate groups of digits.
