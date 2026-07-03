---
page_id: javascriptallonge-section-a-rich-aroma-basic-numbers-663a3fb7
page_kind: source
page_family: section-reference
summary: A Rich Aroma: Basic Numbers: 33 source-backed entries and 1 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-a-rich-aroma-basic-numbers-663a3fb7@5e45dd0af39d6637ca4e6f3a9d13154d
---

# A Rich Aroma: Basic Numbers

From [[javascriptallonge]].

## Related pages

### Source structure

- [[javascriptallonge-section-a-rich-aroma-basic-numbers-floating-ebe9399e]] - narrower source section: A Rich Aroma: Basic Numbers / floating
- [[javascriptallonge-section-a-rich-aroma-basic-numbers-operations-on-numbers-57cbae24]] - narrower source section: A Rich Aroma: Basic Numbers / operations on numbers

## Statements

- In computer science, a literal is a notation for representing a fixed value in source code. Almost all programming languages have notations for atomic values such as integers, floating-point numbers, and strings, and usually for booleans and characters; some also have notations for elements of enumerated types and compound values such as arrays, records, and objects. An anonymous function is a literal for the function type.Wikipedia 12 _(javascriptallonge.pdf (source-range-7239e085-00141))_
- JavaScript, like most languages, has a collection of literals. We saw that an expression consisting solely of numbers, like 42 , is a literal. It represents the number forty-two, which is 42 base 10. Not all numbers are base ten. If we start a literal with a zero, it is an octal literal. So the literal 042 is 42 base 8, which is actually 34 base 10. _(javascriptallonge.pdf (source-range-7239e085-00142))_
- Internally, both 042 and 34 have the same representation, as double-precision floating point 13 numbers. A computer's internal representation for numbers is important to understand. The machine's representation of a number almost never lines up perfectly with our understanding of how a number behaves, and thus there will be places where the computer's behaviour surprises us if we don't know a little about what it's doing 'under the hood.' _(javascriptallonge.pdf (source-range-7239e085-00144))_
- For example, the largest integer JavaScript can safely 14 handle is 9007199254740991 , or 2 '53' - 1 . Like most programming languages, JavaScript does not allow us to use commas to separate groups of digits. _(javascriptallonge.pdf (source-range-7239e085-00145))_
- Almost all programming languages have notations for atomic values such as integers, floating-point numbers, and strings, and usually for booleans and characters; some also have notations for elements of enumerated types and compound values such as arrays, records, and objects. _(javascriptallonge.pdf (source-range-7239e085-00141))_
- For example, the largest integer JavaScript can safely 14 handle is 9007199254740991 , or 2 '53' - 1 . _(javascriptallonge.pdf (source-range-7239e085-00145))_

## Statements by subsection

### A Rich Aroma: Basic Numbers / floating

- Most programmers never encounter the limit on the magnitude of an integer. But we mentioned that numbers are represented internally as floating point, meaning that they need not be just integers. We can, for example, write 1.5 or 33.33 , and JavaScript represents these literals as floating point numbers. _(javascriptallonge.pdf (source-range-7239e085-00147))_
- It's tempting to think we now have everything we need to do things like handle amounts of money, but as the late John Belushi would say, 'Nooooooooooooooooooooo.' A computer's internal representation for a floating point number is binary, while our literal number was in base ten. This makes no meaningful difference for integers, but it does for fractions, because some fractions base 10 do not have exact representations base 2. _(javascriptallonge.pdf (source-range-7239e085-00148))_
- But as a rule, if you need to work with real numbers, you should have more than a nodding acquaintance with the IEEE Standard for Floating-Point Arithmetic 15 . Professional programmers almost never use floating point numbers to represent monetary amounts. For example, '$43.21' will nearly always be presented as two numbers: 43 for dollars and 21 for cents, not 43.21 . In this book, we need not think about such details, but outside of this book, we must. _(javascriptallonge.pdf (source-range-7239e085-00155))_
- We can, for example, write 1.5 or 33.33 , and JavaScript represents these literals as floating point numbers. _(javascriptallonge.pdf (source-range-7239e085-00147))_
- This makes no meaningful difference for integers, but it does for fractions, because some fractions base 10 do not have exact representations base 2. _(javascriptallonge.pdf (source-range-7239e085-00148))_
- For example, '$43.21' will nearly always be presented as two numbers: 43 for dollars and 21 for cents, not 43.21 . _(javascriptallonge.pdf (source-range-7239e085-00155))_

### A Rich Aroma: Basic Numbers / operations on numbers

- As we've seen, JavaScript has many common arithmetic operators. We can create expressions that look very much like mathematical expressions, for example we can write 1 + 1 or 2 * 3 or 42 34 or even 6 / 2 . These can be combined to make more complex expressions, like 2 * 5 + 1 . _(javascriptallonge.pdf (source-range-7239e085-00157))_
- In JavaScript, operators have an order of precedence designed to mimic the way humans typically parse written arithmetic. So: _(javascriptallonge.pdf (source-range-7239e085-00158))_
- JavaScript treats the expressions as if we had written (2 * 5) + 1 and 1 + (5 * 2) , because the * operator has a higher precedence than the + operator. JavaScript has many more operators. In a sense, they behave like little functions. If we write 1 + 2 , this is conceptually similar to writing plus(1, 2) (assuming we have a function that adds two numbers bound to the name plus , of course). _(javascriptallonge.pdf (source-range-7239e085-00160))_

## Technical atoms

### Technical atom 1

<a id="atom-technical-atom-22beebdf7dbbbd52"></a>

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00152))_

```text
13 http://en.wikipedia.org/wiki/Double-precision_floating-point_format
14 Implementations of JavaScript are free to handle larger numbers. For example, if you type 9007199254740991 + 9007199254740991 into node.js , it will happily report that the answer is 18014398509481982 . But code that depends upon numbers larger than 9007199254740991 may not be reliable when moved to other implementations.
```

<details>
<summary>Parsed table preview (needs review)</summary>

| entry | content |
| --- | --- |
| 13 | http://en.wikipedia.org/wiki/Double-precision_floating-point_format |
| 14 | Implementations of JavaScript are free to handle larger numbers. For example, if you type 9007199254740991 + 9007199254740991 into node.js, it will happily report that the answer is 18014398509481982. But code that depends upon numbers larger than 9007199254740991 may not be reliable when moved to other implementations. |

</details>
