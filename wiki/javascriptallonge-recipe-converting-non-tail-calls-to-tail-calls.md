---
page_id: javascriptallonge-recipe-converting-non-tail-calls-to-tail-calls
page_kind: recipe
page_family: recipe-pattern
summary: converting non-tail-calls to tail-calls: synthesized recipe pattern from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: converting-non-tail-calls-to-tail-calls
projection_coverage: page-synthesis-javascriptallonge-recipe-converting-non-tail-calls-to-tail-calls@0d575cf2a775b34f63947fdb6c03868c
---

# converting non-tail-calls to tail-calls

## Pattern

- The obvious solution is push the 1 + work into. _(raw/javascriptallonge.pdf (source-range-7239e085-00978))_
- Now that we've seen how it can clean up the 0 + numberToBeAdded. _(raw/javascriptallonge.pdf (source-range-7239e085-00980))_

## Applicability And Rationale

- The 1 + work is done before calling itself and by. _(raw/javascriptallonge.pdf (source-range-7239e085-00980))_
- This version of length calls uses lengthDelaysWork and JavaScript optimizes that not. _(raw/javascriptallonge.pdf (source-range-7239e085-00983))_
- We can map over large arrays without incurring. _(raw/javascriptallonge.pdf (source-range-7239e085-00986))_
- And this basic transformation from a does not make a tail call into. _(raw/javascriptallonge.pdf (source-range-7239e085-00986))_

## Technical Atoms

- Converting non-tail-calls to tail-calls includes a code block at #atom-technical-atom-d0492cb61af780f2. _(raw/javascriptallonge.pdf (source-range-7239e085-00979))_
- Converting non-tail-calls to tail-calls includes a code block at #atom-technical-atom-04ddfbb646c44eec. _(raw/javascriptallonge.pdf (source-range-7239e085-00981))_
- Converting non-tail-calls to tail-calls includes a code block at #atom-technical-atom-fb0a210bf03406d6. _(raw/javascriptallonge.pdf (source-range-7239e085-00982))_
- Converting non-tail-calls to tail-calls includes a code block at #atom-technical-atom-6dcf576313bfb287. _(raw/javascriptallonge.pdf (source-range-7239e085-00984))_

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-composing-and-decomposing-data-tail-calls-and-default-arguments-converting-non-tail-calls-to-tai-dc131bb9]]
