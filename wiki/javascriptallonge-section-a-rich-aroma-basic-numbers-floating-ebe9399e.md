---
page_id: javascriptallonge-section-a-rich-aroma-basic-numbers-floating-ebe9399e
page_kind: source
page_family: section-reference
summary: A Rich Aroma: Basic Numbers / floating: 14 source-backed entries and 1 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-a-rich-aroma-basic-numbers-floating-ebe9399e@e9781ba391be10269e5a63fd941e483a
---

# A Rich Aroma: Basic Numbers / floating

From [[javascriptallonge]].

## Related pages

### Source structure

- [[javascriptallonge-section-a-rich-aroma-basic-numbers-663a3fb7]] - broader source section: A Rich Aroma: Basic Numbers

## Statements

- Most programmers never encounter the limit on the magnitude of an integer. But we mentioned that numbers are represented internally as floating point, meaning that they need not be just integers. We can, for example, write 1.5 or 33.33 , and JavaScript represents these literals as floating point numbers. _(javascriptallonge.pdf (source-range-7239e085-00147))_
- It's tempting to think we now have everything we need to do things like handle amounts of money, but as the late John Belushi would say, 'Nooooooooooooooooooooo.' A computer's internal representation for a floating point number is binary, while our literal number was in base ten. This makes no meaningful difference for integers, but it does for fractions, because some fractions base 10 do not have exact representations base 2. _(javascriptallonge.pdf (source-range-7239e085-00148))_
- But as a rule, if you need to work with real numbers, you should have more than a nodding acquaintance with the IEEE Standard for Floating-Point Arithmetic 15 . Professional programmers almost never use floating point numbers to represent monetary amounts. For example, '$43.21' will nearly always be presented as two numbers: 43 for dollars and 21 for cents, not 43.21 . In this book, we need not think about such details, but outside of this book, we must. _(javascriptallonge.pdf (source-range-7239e085-00155))_
- We can, for example, write 1.5 or 33.33 , and JavaScript represents these literals as floating point numbers. _(javascriptallonge.pdf (source-range-7239e085-00147))_
- This makes no meaningful difference for integers, but it does for fractions, because some fractions base 10 do not have exact representations base 2. _(javascriptallonge.pdf (source-range-7239e085-00148))_
- For example, '$43.21' will nearly always be presented as two numbers: 43 for dollars and 21 for cents, not 43.21 . _(javascriptallonge.pdf (source-range-7239e085-00155))_

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
