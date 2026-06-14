---
category: concept
summary: JavaScript template strings with backticks and interpolation using ${expression}.
sources: raw/javascriptallonge.pdf
updated: 2026-06-11
---

Quasi-literals (template strings) in JavaScript are denoted with backticks (`) and allow embedded expressions via ${}. Example:

```js
`A popular number for nerds is ${40 + 2}` // 'A popular number for nerds is 42'
```

They offer better readability than string concatenation and avoid common errors like missing spaces. See [[javascriptallonge-object-assign]] for implementation details and comparison to traditional string operations. (raw/javascriptallonge.pdf p.198-205)
