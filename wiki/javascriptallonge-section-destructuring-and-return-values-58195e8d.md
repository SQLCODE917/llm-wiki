---
page_id: javascriptallonge-section-destructuring-and-return-values-58195e8d
page_kind: source
summary: destructuring and return values: 1 source-backed entries and 1 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-destructuring-and-return-values-58195e8d@78a6f16cf7c7eba7efac7f9eea2a4a7c
---

# destructuring and return values

From [[javascriptallonge]].

## Technical atoms

### Technical frame 1: destructuring and return values

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00872))_

```
const description = (nameAndOccupation) => { if (nameAndOccupation.length < 2) { return ["", "occupation missing"] } else { const [[first, last], occupation] = nameAndOccupation; return [` ${ first } is a ${ occupation } `, "ok"]; } } const [reg, status] = description([["Reginald", "Braithwaite"], "programmer"]); reg //=> "Reginald is a programmer" status //=> "ok"
```
