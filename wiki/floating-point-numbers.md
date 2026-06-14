---
category: concept
summary: JavaScript's representation of real numbers using IEEE 754 standard, with precision limitations.
sources: raw/javascriptallonge.pdf
updated: 2026-06-12
---

JavaScript represents numbers as 64-bit floating-point values per IEEE 754 standard. This leads to precision issues like 0.1 + 0.2 !== 0.3. Financial calculations should use integers to avoid rounding errors. The maximum safe integer is 9007199254740991. [[javascriptallonge-forewords-to-the-first-edition]] [[value-types]]
