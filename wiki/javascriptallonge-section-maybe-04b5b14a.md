---
page_id: javascriptallonge-section-maybe-04b5b14a
page_kind: source
summary: Maybe: 12 source-backed entries and 7 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-maybe-04b5b14a@d9d347db550b14f185be03c47323a8cb
---

# Maybe

From [[javascriptallonge]].

## Statements

- A common problem in programming is checking for null or undefined (hereafter called 'nothing,' while all other values including 0 , [] and false will be called 'something'). Languages like JavaScript do not strongly enforce the notion that a particular variable or particular property be something, so programs are often written to account for values that may be nothing. _(javascriptallonge.pdf (source-range-31a4cf47-00695))_
- This recipe concerns a pattern that is very common: A function fn takes a value as a parameter, and its behaviour by design is to do nothing if the parameter is nothing: _(javascriptallonge.pdf (source-range-31a4cf47-00696))_
- Alternately, the function may be intended to work with any value, but the code calling the function wishes to emulate the behaviour of doing nothing by design when given nothing: _(javascriptallonge.pdf (source-range-31a4cf47-00698))_
- Naturally, there's a function decorator recipe for that, borrowed from Haskell's maybe monad 50 , Ruby's andand 51 , and CoffeeScript's existential method invocation: _(javascriptallonge.pdf (source-range-31a4cf47-00700))_
- If some code ever tries to call model.setSomething with nothing, the operation will be skipped. _(javascriptallonge.pdf (source-range-31a4cf47-00708))_

## Technical atoms

### Technical frame 1: Maybe

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00698))_

> Alternately, the function may be intended to work with any value, but the code calling the function wishes to emulate the behaviour of doing nothing by design when given nothing:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00697))_

```
const isSomething = (value) => value !== null && value !== void 0; const checksForSomething = (value) => { if (isSomething(value)) { // function's true logic } }
```

### Technical frame 2: Maybe

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00700))_

> Naturally, there's a function decorator recipe for that, borrowed from Haskell's maybe monad 50 , Ruby's andand 51 , and CoffeeScript's existential method invocation:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00699))_

```
var something = isSomething(value) ? doesntCheckForSomething(value) : value;
```

### Technical frame 3: Maybe

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00708))_

> If some code ever tries to call model.setSomething with nothing, the operation will be skipped.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00701))_

```
const maybe = (fn) => function (...args) { if (args.length === 0) { return } else { for ( let arg of args) { if (arg == null ) return ; }
```

### Technical frame 4: Maybe

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00708))_

> If some code ever tries to call model.setSomething with nothing, the operation will be skipped.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00703))_

```
return fn.apply( this , args) } }
```

### Technical frame 5: Maybe

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00708))_

> If some code ever tries to call model.setSomething with nothing, the operation will be skipped.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00705))_

```
maybe((a, b, c) => a + b + c)(1, 2, 3) //=> 6 maybe((a, b, c) => a + b + c)(1, null , 3) //=> undefined
```

### Technical frame 6: Maybe

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00708))_

> If some code ever tries to call model.setSomething with nothing, the operation will be skipped.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00707))_

```
function Model () {}; Model.prototype.setSomething = maybe( function (value) { this .something = value; });
```

### Technical atom 7

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00700))_

> Naturally, there's a function decorator recipe for that, borrowed from Haskell's maybe monad 50 , Ruby's andand 51 , and CoffeeScript's existential method invocation:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00702))_

| entry | content |
| --- | --- |
| 50 | https://en.wikipedia.org/wiki/Monad_(functional_programming)#The_Maybe_monad |
| 51 | https://github.com/raganwald/andand |

<details>
<summary>Raw table text</summary>

```
50 https://en.wikipedia.org/wiki/Monad_(functional_programming)#The_Maybe_monad
51 https://github.com/raganwald/andand
```

</details>
