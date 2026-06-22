---
page_id: javascriptallonge-a-history-lesson
page_kind: source
summary: A history lesson on variadic functions and argument gathering in JavaScript, from javascriptallonge.pdf p.90-91.
sources: raw/javascriptallonge.pdf p.90-91
updated: 2026-06-20
source_id: javascriptallonge.pdf
---

## Source record

In 'Ye Olde Days,' 53 JavaScript could not gather parameters, and we had to either do backflips with arguments and .slice , or we wrote ourselves a variadic decorator that could gather arguments into the last declared parameter.

## Key supported claims

- Older JavaScript needed arguments, .slice, or a variadic decorator to emulate gathered parameters. (raw/javascriptallonge.pdf p.90-91)
- A right-variadic function has one or more fixed arguments, and the rest are gathered into the rightmost argument. (raw/javascriptallonge.pdf p.90-91)
- The rightVariadic decorator gathers ordinary arguments and the rest of the argument list before applying the wrapped function. (raw/javascriptallonge.pdf p.90-91)
