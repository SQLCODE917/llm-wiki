---
page_id: javascriptallonge-recipe-recursive-iterators
page_kind: recipe
page_family: recipe-pattern
summary: recursive iterators: synthesized recipe pattern from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: recursive-iterators
projection_coverage: page-synthesis-javascriptallonge-recipe-recursive-iterators@2ec0d519d282d38423024e490aa725c7
---

# recursive iterators

## Pattern

- Recursive iterators has applicability evidence. _(raw/javascriptallonge.pdf (source-range-7239e085-01637))_
- Generators have to manage the exact same amount. _(raw/javascriptallonge.pdf (source-range-7239e085-01637))_

## Applicability And Rationale

- Elements that are not themselves iterable. _(raw/javascriptallonge.pdf (source-range-7239e085-01638))_
- If you peel off isIterable and uses [Symbol.iterator] and next we're left with. _(raw/javascriptallonge.pdf (source-range-7239e085-01643))_
- In essence both the generation and have stacks but the generation version's stack. _(raw/javascriptallonge.pdf (source-range-7239e085-01643))_
- A less kind way to put is that the iteration version is greenspunning. _(raw/javascriptallonge.pdf (source-range-7239e085-01644))_

## Technical Atoms

- Recursive iterators includes a code block at #atom-technical-atom-d14c6a73cd2e1891. _(raw/javascriptallonge.pdf (source-range-7239e085-01639))_
- Recursive iterators includes a code block at #atom-technical-atom-83d9e3adc3013b32. _(raw/javascriptallonge.pdf (source-range-7239e085-01642))_

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-like-this-generating-iterables-recursive-iterators-7e4e68e5]]
