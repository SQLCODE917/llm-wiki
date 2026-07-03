---
page_id: javascriptallonge-recipe-generators-are-coroutines
page_kind: recipe
page_family: recipe-pattern
summary: generators are coroutines: synthesized recipe pattern from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: generators-are-coroutines
projection_coverage: page-synthesis-javascriptallonge-recipe-generators-are-coroutines@51cdc786b799c4b2e6efdfc0c19f48e6
---

# generators are coroutines

## Pattern

- This is where generators behave very very differently. _(raw/javascriptallonge.pdf (source-range-7239e085-01679))_
- The iterator is in a nascent or 'newborn' state. _(raw/javascriptallonge.pdf (source-range-7239e085-01681))_

## Applicability And Rationale

- When we call interator.next() the begins to be evaluated. _(raw/javascriptallonge.pdf (source-range-7239e085-01682))_
- The rest of the program makes another call to iterator.next(). _(raw/javascriptallonge.pdf (source-range-7239e085-01686))_
- The iterator resumes execution from yielded the last value. _(raw/javascriptallonge.pdf (source-range-7239e085-01687))_
- The body of our generator ends or encounters the next yield statement. _(raw/javascriptallonge.pdf (source-range-7239e085-01698))_
- There are no more lines of code so. _(raw/javascriptallonge.pdf (source-range-7239e085-01698))_
- This behaviour is not unique to JavaScript generators are. _(raw/javascriptallonge.pdf (source-range-7239e085-01700))_

## Technical Atoms

- Generators are coroutines includes a code block at #atom-technical-atom-5f287b47dc681f91. _(raw/javascriptallonge.pdf (source-range-7239e085-01678))_
- Generators are coroutines includes a code block at #atom-technical-atom-e0bca2d9e767995c. _(raw/javascriptallonge.pdf (source-range-7239e085-01705))_

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-we-ll-keep-it-simple-generators-are-coroutines-a23babe6]]
