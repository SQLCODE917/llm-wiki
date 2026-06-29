---
page_id: javascriptallonge-section-destructuring-and-return-values-263798f7
page_kind: source
summary: destructuring and return values: 1 source-backed entries and 1 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-destructuring-and-return-values-263798f7@656b74dd8ab7a5b3b623553694dd6829
---

# destructuring and return values

From [[javascriptallonge]].

## Technical atoms

### Technical frame 1: destructuring and return values

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00872))_

```
const description = (nameAndOccupation) => { if (nameAndOccupation.length < 2) { return ["", "occupation missing"] } else { const [[first, last], occupation] = nameAndOccupation; return [` ${ first } is a ${ occupation } `, "ok"]; } } const [reg, status] = description([["Reginald", "Braithwaite"], "programmer"]); reg //=> "Reginald is a programmer" status //=> "ok"
```
