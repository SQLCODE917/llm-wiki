---
page_id: javascriptallonge-section-functions-that-evaluate-to-functions-47133f51
page_kind: source
summary: functions that evaluate to functions: 10 source-backed entries and 5 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-functions-that-evaluate-to-functions-47133f51@5226342ca6a3b4244f8ae823ff446ee9
---

# functions that evaluate to functions

From [[javascriptallonge]].

## Statements

- That's a function! It's a function that when applied, evaluates to a function that when applied, evaluates to 0 . So we have a function, that returns a function, that returns zero . Likewise: _(javascriptallonge.pdf (source-range-8eb13d6b-00264))_
- Well. We've been very clever, but so far this all seems very abstract. Diffraction of a crystal is beautiful and interesting in its own right, but you can't blame us for wanting to be shown a practical use for it, like being able to determine the composition of a star millions of light years away. So… In the next chapter, 'I'd Like to Have an Argument, Please,' we'll see how to make functions practical. _(javascriptallonge.pdf (source-range-8eb13d6b-00271))_

## Technical atoms

### Technical frame 1: functions that evaluate to functions

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00264))_

> That's a function! It's a function that when applied, evaluates to a function that when applied, evaluates to 0 . So we have a function, that returns a function, that returns zero . Likewise:

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00261))_

> If an expression that evaluates to a function is, well, an expression, and if a return statement can have any expression on its right side… Can we put an expression that evaluates to a function on the right side of a function expression?

### Technical frame 2: functions that evaluate to functions

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00264))_

> That's a function! It's a function that when applied, evaluates to a function that when applied, evaluates to 0 . So we have a function, that returns a function, that returns zero . Likewise:

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00263))_

```
() => () => 0
```

### Technical frame 3: functions that evaluate to functions

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00271))_

> Well. We've been very clever, but so far this all seems very abstract. Diffraction of a crystal is beautiful and interesting in its own right, but you can't blame us for wanting to be shown a practical use for it, like being able to determine the composition of a star millions of light years away. So… In the next chapter, 'I'd Like to Have an Argument, Please,' we'll see how to make functions practical.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00265))_

```
() => () => true
```

### Technical frame 4: functions that evaluate to functions

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00271))_

> Well. We've been very clever, but so far this all seems very abstract. Diffraction of a crystal is beautiful and interesting in its own right, but you can't blame us for wanting to be shown a practical use for it, like being able to determine the composition of a star millions of light years away. So… In the next chapter, 'I'd Like to Have an Argument, Please,' we'll see how to make functions practical.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00267))_

```
(() => () => true )()() //=> true
```

### Technical frame 5: functions that evaluate to functions

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00271))_

> Well. We've been very clever, but so far this all seems very abstract. Diffraction of a crystal is beautiful and interesting in its own right, but you can't blame us for wanting to be shown a practical use for it, like being able to determine the composition of a star millions of light years away. So… In the next chapter, 'I'd Like to Have an Argument, Please,' we'll see how to make functions practical.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00269))_

```
() => () => { return true ; }
```
