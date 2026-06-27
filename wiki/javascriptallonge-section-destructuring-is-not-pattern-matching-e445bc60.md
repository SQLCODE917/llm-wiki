---
page_id: javascriptallonge-section-destructuring-is-not-pattern-matching-e445bc60
page_kind: source
summary: **destructuring is not pattern matching**: 11 source-backed entries and 2 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-destructuring-is-not-pattern-matching-e445bc60@a14ae59888ef9aea2abc2239f3e337b6
---

# **destructuring is not pattern matching**

From [[javascriptallonge]].

## Statements

- If it does, assignments are made where appropriate. _(javascriptallonge.pdf (source-range-83ecb080-01264))_
- JavaScript tries its best to assign things, and if there isn’t something that fits, JavaScript binds undefined to the name. _(javascriptallonge.pdf (source-range-83ecb080-01269))_
- But this is not how JavaScript works. _(javascriptallonge.pdf (source-range-83ecb080-01269))_
- That match would fail because the array doesn’t have an element to assign to what. _(javascriptallonge.pdf (source-range-83ecb080-01269))_
- That match would fail because the array doesn’t have an element to assign to what. _(javascriptallonge.pdf (source-range-83ecb080-01269))_
- As a result, it often coerces values, passes undefined around, or does whatever it can to keep executing without failing. _(javascriptallonge.pdf (source-range-83ecb080-01274))_
- From its very inception, JavaScript has striven to avoid catastrophic errors. _(javascriptallonge.pdf (source-range-83ecb080-01274))_
- This often means that we must write our own code to detect failure conditions, as we cannot reply on the language to point out when we are doing semantically meaningless things. _(javascriptallonge.pdf (source-range-83ecb080-01274))_
- This often means that we must write our own code to detect failure conditions, as we cannot reply on the language to point out when we are doing semantically meaningless things. _(javascriptallonge.pdf (source-range-83ecb080-01274))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01269))_

> That match would fail because the array doesn’t have an element to assign to what. But this is not how JavaScript works. JavaScript tries its best to assign things, and if there isn’t something that fits, JavaScript binds undefined to the name. Therefore:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01271))_

> what _//=> undefined_ **const** [which, what, who] = ["duck feet", "tiger tail"]; who _//=> undefined_

### Technical atom 2

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01272, source-range-83ecb080-01274))_

> And if there aren’t any items to assign with ..., JavaScript assigns an empty array: From its very inception, JavaScript has striven to avoid catastrophic errors. As a result, it often coerces values, passes undefined around, or does whatever it can to keep executing without failing. This often means that we must write our own code to detect failure conditions, as we cannot reply on the language to point out when we are doing semantically meaningless things.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01273))_

> **const** [...they] = []; they _//=> []_ **const** [which, what, ...they] = ["duck feet", "tiger tail"]; they _//=> []_
