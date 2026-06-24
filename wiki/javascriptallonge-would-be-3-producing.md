---
page_id: javascriptallonge-would-be-3-producing
page_kind: source
summary: Would be 3 , producing: from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.276-276
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

This section discusses encoding game boards in JavaScript, emphasizing the use of arrays over multiline strings for better design and modularity.

## Key supported claims

- We can encode the board in several different ways, such as using multiline strings or arrays. (raw/javascriptallonge.pdf p.276-276)

## Technical details

### `technical-atom-2dcc1053d4ea80a5` requirement

Citation: (raw/javascriptallonge.pdf p.276)

Our function should be just as useful on a teletype as it would be backing a DOM game that uses a table, or a browser game that draws on Canvas.

## Related technical details

### From [[javascriptallonge-so-why-arrays]]: `technical-atom-8b9bc553c75c20d8` procedure

Relation: nearby source page; matched terms `arrays`, `javascript`, `use`

Citation: (raw/javascriptallonge.pdf p.131)

If [first, ...rest] is so slow, why does JavaScript use arrays instead of making everything a linked list?

### From [[javascriptallonge-representing-naughts-and-crosses-as-a-stateless-function]]: `technical-atom-203cbced3f1f6964` procedure

Relation: nearby source page; matched terms `board`, `encode`, `function`

Citation: (raw/javascriptallonge.pdf p.275)

We encode each position of the board in some fashion, and then we build a dictionary from positions to moves.
