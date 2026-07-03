---
page_id: javascriptallonge-recipe-tail-call-optimization
page_kind: recipe
page_family: recipe-pattern
summary: tail-call optimization: synthesized recipe pattern from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: tail-call-optimization
projection_coverage: page-synthesis-javascriptallonge-recipe-tail-call-optimization@23be8eed784cc98853d846ec2b0dff49
---

# tail-call optimization

## Pattern

- There are three places it returns. _(raw/javascriptallonge.pdf (source-range-7239e085-00970))_
- It isn't going to do any more work so it can. _(raw/javascriptallonge.pdf (source-range-7239e085-00970))_

## Applicability And Rationale

- This is a tail-call because it invokes another. _(raw/javascriptallonge.pdf (source-range-7239e085-00970))_
- This is interesting because after sorting out what. _(raw/javascriptallonge.pdf (source-range-7239e085-00970))_
- But the third is fn.apply(this args). _(raw/javascriptallonge.pdf (source-range-7239e085-00970))_
- This is a very important characteristic of JavaScript. _(raw/javascriptallonge.pdf (source-range-7239e085-00971))_
- And in fact it does exactly that It throws the stack. _(raw/javascriptallonge.pdf (source-range-7239e085-00971))_
- That is excellent but one wrapping is not. _(raw/javascriptallonge.pdf (source-range-7239e085-00972))_

## Technical Atoms

- Tail-call optimization includes a code block at #atom-technical-atom-a6d838fc3442cb2f. _(raw/javascriptallonge.pdf (source-range-7239e085-00969))_
- Tail-call optimization includes a code block at #atom-technical-atom-2634a0aa2029afd4. _(raw/javascriptallonge.pdf (source-range-7239e085-00973))_

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-composing-and-decomposing-data-tail-calls-and-default-arguments-tail-call-optimization-755a53cb]]
