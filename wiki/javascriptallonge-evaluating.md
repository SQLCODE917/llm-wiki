---
page_id: javascriptallonge-evaluating
page_kind: concept
summary: Evaluating: 4 statement(s) and 8 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-evaluating@0d6d8f1c51113ddff9f0a63d0ba21c42
---

# Evaluating

What [[javascriptallonge]] covers about evaluating:

## Statements

### the simplest possible block

- It returns the result of evaluating a block that has no statements. What would that be? Let's try it: _(javascriptallonge.pdf (source-range-31a4cf47-00217))_

### void

- We said that the function returns the result of evaluating a block , and we said that a block is a (possibly empty) list of JavaScript statements separated by semicolons. 21 _(javascriptallonge.pdf (source-range-31a4cf47-00239))_

### shadowy variables from a shadowy planet

- When evaluating x + y + z , JavaScript will find x and y in the great-grandparent scope and z in the parent scope. The x in the great-great-grandparent scope is ignored, as are both w s. When a variable has the same name as an ancestor environment's binding, it is said to shadow the ancestor. _(javascriptallonge.pdf (source-range-31a4cf47-00378))_

### Reassignment

- Like evaluating variable labels, when a binding is rebound, JavaScript searches for the binding in the current environment and then each ancestor in turn until it finds one. It then rebinds the name in that environment. _(javascriptallonge.pdf (source-range-31a4cf47-01178))_


## Technical atoms

### Technical frame 1: the simplest possible block

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00217))_

> It returns the result of evaluating a block that has no statements. What would that be? Let's try it:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00216))_

```
() => {}
```

### Technical frame 2: the simplest possible block

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00217))_

> It returns the result of evaluating a block that has no statements. What would that be? Let's try it:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00218))_

```
(() => {})() //=> undefined
```

### Technical frame 3: void

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00239))_

> We said that the function returns the result of evaluating a block , and we said that a block is a (possibly empty) list of JavaScript statements separated by semicolons. 21

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00238))_

```
(() => {})() //=> undefined
```

### Technical frame 4: void

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00249))_

> 21 You can also separate statements with line breaks. Readers who follow internet flame-fests may be aware of something called automatic semicolon insertion. Basically, there's a step where JavaScript looks at your code and follows some rules to guess where you meant to put semicolons in should you leave them out. This feature was originally created as a kind of helpful error-correction. Some programmers argue that since it's part of the language's definition, it's fair game to write code that e

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00251))_

> So how do we get a function that evaluates a block to return a value when applied?

### Technical frame 5: void

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00249))_

> 21 You can also separate statements with line breaks. Readers who follow internet flame-fests may be aware of something called automatic semicolon insertion. Basically, there's a step where JavaScript looks at your code and follows some rules to guess where you meant to put semicolons in should you leave them out. This feature was originally created as a kind of helpful error-correction. Some programmers argue that since it's part of the language's definition, it's fair game to write code that e

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00252))_

```
(() => { return 0 })() //=> 0 (() => { return 1 })() //=> 1 (() => { return 'Hello ' + 'World' })() // 'Hello World'
```

### Technical frame 6: void

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00249))_

> 21 You can also separate statements with line breaks. Readers who follow internet flame-fests may be aware of something called automatic semicolon insertion. Basically, there's a step where JavaScript looks at your code and follows some rules to guess where you meant to put semicolons in should you leave them out. This feature was originally created as a kind of helpful error-correction. Some programmers argue that since it's part of the language's definition, it's fair game to write code that e

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00254))_

```
(() => { 1 + 1; return 2 + 2 })() //=> 4
```

### Technical frame 7: shadowy variables from a shadowy planet

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00376))_

> The function (x, y) => x + y is a pure function, because its x is defined within its own environment. Although its parent also defines an x , it is ignored when evaluating x + y . JavaScript always searches for a binding starting with the functions own environment and then each parent in turn until it finds one. The same is true of:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00375))_

```
(x) => (x, y) => x + y
```

### Technical frame 8: shadowy variables from a shadowy planet

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00378))_

> When evaluating x + y + z , JavaScript will find x and y in the great-grandparent scope and z in the parent scope. The x in the great-great-grandparent scope is ignored, as are both w s. When a variable has the same name as an ancestor environment's binding, it is said to shadow the ancestor.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00377))_

```
(x) => (x, y) => (w, z) => (w) => x + y + z
```


## Related pages

- [[javascriptallonge-result]] - shared statements and technical atoms: Result shares source evidence from the simplest possible block: It returns the result of evaluating a block that has no statements. What would that be? Let's try it:; Result shares technical record from the simplest possible block: () => {} (2 shared statement(s), 6 shared atom(s))
- [[javascriptallonge-return]] - shared statements and technical atoms: Return shares source evidence from the simplest possible block: It returns the result of evaluating a block that has no statements. What would that be? Let's try it:; Return shares technical record from the simplest possible block: () => {} (2 shared statement(s), 6 shared atom(s))
- [[javascriptallonge-block]] - shared statements and technical atoms: Block shares source evidence from the simplest possible block: It returns the result of evaluating a block that has no statements. What would that be? Let's try it:; Block shares technical record from the simplest possible block: () => {} (2 shared statement(s), 4 shared atom(s))
- [[javascriptallonge-function]] - shared statements and technical atoms: Function shares source evidence from void: We said that the function returns the result of evaluating a block , and we said that a block is a (possibly empty) list of JavaScript statements separated by semicolons. 21; Function shares technical record from void: (() => {})() //=> undefined (1 shared statement(s), 4 shared atom(s))
- [[javascriptallonge-javascript]] - shared statements and technical atoms: Javascript shares source evidence from shadowy variables from a shadowy planet: When evaluating x + y + z , JavaScript will find x and y in the great-grandparent scope and z in the parent scope. The x in the great-great-grandparent scope is igno ... [truncated]; Javascript shares technical record from void: (() => {})() //=> undefined (1 shared statement(s), 4 shared atom(s))
- [[javascriptallonge-expression]] - shared technical atoms: Expression shares technical record from void: So how do we get a function that evaluates a block to return a value when applied? (3 shared atom(s))
- [[javascriptallonge-code]] - shared technical atoms: Code shares technical record from void: So how do we get a function that evaluates a block to return a value when applied? (1 shared atom(s))
- [[javascriptallonge-evaluate]] - shared technical atoms: Evaluate shares technical record from void: (() => { return 0 })() //=> 0 (() => { return 1 })() //=> 1 (() => { return 'Hello ' + 'World' })() // 'Hello World' (1 shared atom(s))
- [[javascriptallonge-feature]] - shared technical atoms: Feature shares technical record from void: So how do we get a function that evaluates a block to return a value when applied? (1 shared atom(s))
- [[javascriptallonge-follow]] - shared technical atoms: Follow shares technical record from void: So how do we get a function that evaluates a block to return a value when applied? (1 shared atom(s))
- [[javascriptallonge-language]] - shared technical atoms: Language shares technical record from void: So how do we get a function that evaluates a block to return a value when applied? (1 shared atom(s))
- [[javascriptallonge-program]] - shared technical atoms: Program shares technical record from void: So how do we get a function that evaluates a block to return a value when applied? (1 shared atom(s))
- [[javascriptallonge-programmer]] - shared technical atoms: Programmer shares technical record from void: So how do we get a function that evaluates a block to return a value when applied? (1 shared atom(s))
- [[javascriptallonge-rule]] - shared technical atoms: Rule shares technical record from void: So how do we get a function that evaluates a block to return a value when applied? (1 shared atom(s))
- [[javascriptallonge-write]] - shared technical atoms: Write shares technical record from void: So how do we get a function that evaluates a block to return a value when applied? (1 shared atom(s))
- [[javascriptallonge-bind]] - shared statements: Bind shares source evidence from Reassignment: Like evaluating variable labels, when a binding is rebound, JavaScript searches for the binding in the current environment and then each ancestor in turn until it fi ... [truncated] (1 shared statement(s))
- [[javascriptallonge-binding]] - shared statements: Binding shares source evidence from Reassignment: Like evaluating variable labels, when a binding is rebound, JavaScript searches for the binding in the current environment and then each ancestor in turn until it fi ... [truncated] (1 shared statement(s))

## Source

- [[javascriptallonge]]
