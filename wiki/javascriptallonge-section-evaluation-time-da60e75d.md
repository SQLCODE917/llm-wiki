---
page_id: javascriptallonge-section-evaluation-time-da60e75d
page_kind: source
summary: evaluation time: 6 source-backed entries and 2 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-evaluation-time-da60e75d@4299ced2f2a02bb7fd06141cd58a5e24
---

# evaluation time

From [[javascriptallonge]].

## Statements

- JavaScript evaluates the quasi-literal when the function is invoked and the quasi-literal inside the function's body is evaluated. Thus, name is not bound to "Harry" , it is bound to 'Arthur Dent' , the value of the parameter when the function is invoked. _(javascriptallonge.pdf (source-range-8eb13d6b-01518))_
- Thus, name is not bound to "Harry" , it is bound to 'Arthur Dent' , the value of the parameter when the function is invoked. _(javascriptallonge.pdf (source-range-8eb13d6b-01518))_
- JavaScript evaluates the quasi-literal when the function is invoked and the quasi-literal inside the function's body is evaluated. _(javascriptallonge.pdf (source-range-8eb13d6b-01518))_

## Technical atoms

### Technical frame 1: evaluation time

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01518))_

> JavaScript evaluates the quasi-literal when the function is invoked and the quasi-literal inside the function's body is evaluated. Thus, name is not bound to "Harry" , it is bound to 'Arthur Dent' , the value of the parameter when the function is invoked.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01517))_

```
const name = "Harry"; const greeting = (name) => `Hello my name is ${ name } `; greeting('Arthur Dent') //=> 'Hello my name is Arthur Dent'
```

### Technical frame 2: evaluation time

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01518))_

> JavaScript evaluates the quasi-literal when the function is invoked and the quasi-literal inside the function's body is evaluated. Thus, name is not bound to "Harry" , it is bound to 'Arthur Dent' , the value of the parameter when the function is invoked.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01520))_

```
const greeting = (name) => 'Hello my name is ' + name; greeting('Arthur Dent') //=> 'Hello my name is Arthur Dent'
```
