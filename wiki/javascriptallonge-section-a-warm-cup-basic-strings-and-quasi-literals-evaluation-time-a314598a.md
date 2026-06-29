---
page_id: javascriptallonge-section-a-warm-cup-basic-strings-and-quasi-literals-evaluation-time-a314598a
page_kind: source
summary: A Warm Cup: Basic Strings and Quasi-Literals / evaluation time: 6 source-backed entries and 2 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-29
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-a-warm-cup-basic-strings-and-quasi-literals-evaluation-time-a314598a@93229536c29cebdb49001e0909a7fb45
---

# A Warm Cup: Basic Strings and Quasi-Literals / evaluation time

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-a-warm-cup-basic-strings-and-quasi-literals-d5c66d04]] - broader source section: A Warm Cup: Basic Strings and Quasi-Literals

## Statements

- JavaScript evaluates the quasi-literal when the function is invoked and the quasi-literal inside the function's body is evaluated. Thus, name is not bound to "Harry" , it is bound to 'Arthur Dent' , the value of the parameter when the function is invoked. _(javascriptallonge.pdf (source-range-7239e085-01519))_
- Thus, name is not bound to "Harry" , it is bound to 'Arthur Dent' , the value of the parameter when the function is invoked. _(javascriptallonge.pdf (source-range-7239e085-01519))_
- JavaScript evaluates the quasi-literal when the function is invoked and the quasi-literal inside the function's body is evaluated. _(javascriptallonge.pdf (source-range-7239e085-01519))_

## Technical atoms

### Technical frame 1: A Warm Cup: Basic Strings and Quasi-Literals / evaluation time

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01519))_

> JavaScript evaluates the quasi-literal when the function is invoked and the quasi-literal inside the function's body is evaluated. Thus, name is not bound to "Harry" , it is bound to 'Arthur Dent' , the value of the parameter when the function is invoked.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01518))_

```
const name = "Harry";
const greeting = (name) => `Hello my name is ${name}`;
greeting('Arthur Dent')
//=> 'Hello my name is Arthur Dent'
```

### Technical frame 2: A Warm Cup: Basic Strings and Quasi-Literals / evaluation time

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01519))_

> JavaScript evaluates the quasi-literal when the function is invoked and the quasi-literal inside the function's body is evaluated. Thus, name is not bound to "Harry" , it is bound to 'Arthur Dent' , the value of the parameter when the function is invoked.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01521))_

```
const greeting = (name) => 'Hello my name is ' + name;
greeting('Arthur Dent')
//=> 'Hello my name is Arthur Dent'
```
