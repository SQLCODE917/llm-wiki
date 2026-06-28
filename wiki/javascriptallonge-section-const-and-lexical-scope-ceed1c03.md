---
page_id: javascriptallonge-section-const-and-lexical-scope-ceed1c03
page_kind: source
summary: const and lexical scope: 15 source-backed entries and 4 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-const-and-lexical-scope-ceed1c03@5858dad59c475d35ee0d33bd0cedf806
---

# const and lexical scope

From [[javascriptallonge]].

## Statements

- This seems very straightforward, but alas, there are some semantics of binding names that we need to understand if we're to place const anywhere we like. The first thing to ask ourselves is, what happens if we use const to bind two different values to the 'same' name? _(javascriptallonge.pdf (source-range-31a4cf47-00451))_
- It's more than a bit convoluted, but it binds ((PI) => (diameter) => diameter * PI)(3.14159265) to diameter_fn and evaluates the expression that we've elided. We can use any expression in there, and that expression can invoke diameter_fn . For example: _(javascriptallonge.pdf (source-range-31a4cf47-00455))_
- We know this from the chapter on closures, but even though PI is not bound when we invoke diameter_fn by evaluating diameter_fn(2) , PI is bound when we evaluated (diameter) => diameter * PI , and thus the expression diameter * PI is able to access values for PI and diameter when we evaluate diameter_fn . _(javascriptallonge.pdf (source-range-31a4cf47-00457))_
- This is called lexical scoping 31 , because we can discover where a name is bound by looking at the source code for the program. We can see that PI is bound in an environment surrounding (diameter) => diameter * PI , we don't need to know where diameter_fn is invoked. _(javascriptallonge.pdf (source-range-31a4cf47-00458))_
- Although we have bound 3 to PI in the environment surrounding diameter_fn(2) , the value that counts is 3.14159265 , the value we bound to PI in the environment surrounding (diameter) ⇒ diameter * PI. _(javascriptallonge.pdf (source-range-31a4cf47-00461))_
- That much we can carefully work out from the way closures work. Does const work the same way? Let's find out: _(javascriptallonge.pdf (source-range-31a4cf47-00462))_
- Yes. Binding values to names with const works just like binding values to names with parameter invocations, it uses lexical scope. _(javascriptallonge.pdf (source-range-31a4cf47-00465))_
- We know this from the chapter on closures, but even though PI is not bound when we invoke diameter_fn by evaluating diameter_fn(2) , PI is bound when we evaluated (diameter) => diameter * PI , and thus the expression diameter * PI is able to access values for PI and diameter when we evaluate diameter_fn . _(javascriptallonge.pdf (source-range-31a4cf47-00457))_
- This is called lexical scoping 31 , because we can discover where a name is bound by looking at the source code for the program. _(javascriptallonge.pdf (source-range-31a4cf47-00458))_

## Technical atoms

### Technical frame 1: const and lexical scope

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00455))_

> It's more than a bit convoluted, but it binds ((PI) => (diameter) => diameter * PI)(3.14159265) to diameter_fn and evaluates the expression that we've elided. We can use any expression in there, and that expression can invoke diameter_fn . For example:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00454))_

```
((diameter_fn) => // ... )( ((PI) => (diameter) => diameter * PI )(3.14159265) )
```

### Technical frame 2: const and lexical scope

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00457))_

> We know this from the chapter on closures, but even though PI is not bound when we invoke diameter_fn by evaluating diameter_fn(2) , PI is bound when we evaluated (diameter) => diameter * PI , and thus the expression diameter * PI is able to access values for PI and diameter when we evaluate diameter_fn .

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00456))_

```
((diameter_fn) => diameter_fn(2) )( ((PI) => (diameter) => diameter * PI )(3.14159265) ) //=> 6.2831853
```

### Technical frame 3: const and lexical scope

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00461))_

> Although we have bound 3 to PI in the environment surrounding diameter_fn(2) , the value that counts is 3.14159265 , the value we bound to PI in the environment surrounding (diameter) ⇒ diameter * PI.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00460))_

```
((diameter_fn) => ((PI) => diameter_fn(2) )(3) )( ((PI) => (diameter) => diameter * PI )(3.14159265) ) //=> 6.2831853
```

### Technical frame 4: const and lexical scope

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00465))_

> Yes. Binding values to names with const works just like binding values to names with parameter invocations, it uses lexical scope.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00464))_

```
((diameter_fn) => { const PI = 3; return diameter_fn(2) })( (() => { const PI = 3.14159265; return (diameter) => diameter * PI })() ) //=> 6.2831853
```
