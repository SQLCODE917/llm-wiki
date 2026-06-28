---
page_id: javascriptallonge-binding
page_kind: concept
summary: Binding: 3 statement(s) and 7 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-binding@6c1921229e08c04fcabcbd0bae05dca7
---

# Binding

What [[javascriptallonge]] covers about binding:

## Statements

### const and lexical scope

- Yes. Binding values to names with const works just like binding values to names with parameter invocations, it uses lexical scope. _(javascriptallonge.pdf (source-range-31a4cf47-00465))_

### are consts also from a shadowy planet?

- We can test this by creating another conflict. But instead of binding two different variables to the same name in two different places, we'll bind two different values to the same name, but one environment will be completely enclosed by the other. _(javascriptallonge.pdf (source-range-31a4cf47-00469))_

### Reassignment

- Like evaluating variable labels, when a binding is rebound, JavaScript searches for the binding in the current environment and then each ancestor in turn until it finds one. It then rebinds the name in that environment. _(javascriptallonge.pdf (source-range-31a4cf47-01178))_


## Technical atoms

### Technical frame 1: are consts also from a shadowy planet?

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00478))_

> Now we bind 3 to PI in an otherwise empty IIFE inside of our IIFE that binds 3.14159265 to PI . Does that binding 'overwrite' the outer one? Will our function return 6 or 6.2831853 ? This is a book, you've already scanned ahead, so you know that the answer is no , the inner binding does not overwrite the outer binding:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00477))_

```
((PI) => { ((PI) => {})(3); return (diameter) => diameter * PI; })(3.14159265)
```

### Technical frame 2: are consts also from a shadowy planet?

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00480))_

> We say that when we bind a variable using a parameter inside another binding, the inner binding shadows the outer binding. It has effect inside its own scope, but does not affect the binding in the enclosing scope.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00479))_

```
((PI) => { ((PI) => {})(3); return (diameter) => diameter * PI; })(3.14159265)(2) //=> 6.2831853
```

### Technical frame 3: are consts also from a shadowy planet?

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00484))_

> Parameters are only bound when we invoke a function. That's why we made all these IIFEs. But const statements can appear inside blocks. What happens when we use a const inside of a block? We'll need a gratuitous block. We've seen if statements, what could be more gratuitous than:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00482))_

```
((diameter) => { const PI = 3.14159265; (() => { const PI = 3; })(); return diameter * PI; })(2) //=> 6.2831853
```

### Technical frame 4: Reassignment

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01173))_

> Using let to bind 50 to age within the block does not change the binding of age in the outer environment because the binding of age in the block shadows the binding of age in the outer environment, just like const . We go from:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01172))_

```
(() => { let age = 49; if ( true ) { let age = 50; } return age; })() //=> 49
```

### Technical frame 5: Reassignment

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01178))_

> Like evaluating variable labels, when a binding is rebound, JavaScript searches for the binding in the current environment and then each ancestor in turn until it finds one. It then rebinds the name in that environment.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01174))_

```
{age: 49, '..': global-environment} To: {age: 50, '..': {age: 49, '..': global-environment}} Then back to:
```

### Technical frame 6: Reassignment

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01178))_

> Like evaluating variable labels, when a binding is rebound, JavaScript searches for the binding in the current environment and then each ancestor in turn until it finds one. It then rebinds the name in that environment.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01175))_

```
{age: 49, '..': global-environment}
```

### Technical atom 7

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00613))_

> arguments always contains all of the arguments passed to a function, regardless of how many are declared. Therefore, we can write plus like this:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00614))_

| entry | content |
| --- | --- |
| 42 | You should never attempt to define your own bindings against 'magic' names that JavaScript binds for you. It is wise to treat them as read-only at all times. |
| 43 | We'll look at arrays and plain old javascript objects in depth later. |

<details>
<summary>Raw table text</summary>

```
42 You should never attempt to define your own bindings against 'magic' names that JavaScript binds for you. It is wise to treat them as read-only at all times.
43 We'll look at arrays and plain old javascript objects in depth later.
```

</details>


## Related pages

- [[javascriptallonge-bind]] - shared statements and technical atoms: Bind shares source evidence from const and lexical scope: Yes. Binding values to names with const works just like binding values to names with parameter invocations, it uses lexical scope.; Bind shares technical record from are consts also from a shadowy planet?: ((PI) => { ((PI) => {})(3); return (diameter) => diameter * PI; })(3.14159265) (3 shared statement(s), 7 shared atom(s))
- [[javascriptallonge-different]] - shared statements and technical atoms: Different shares source evidence from are consts also from a shadowy planet?: We can test this by creating another conflict. But instead of binding two different variables to the same name in two different places, we'll bind two different valu ... [truncated]; Different shares technical record from are consts also from a shadowy planet?: ((PI) => { ((PI) => {})(3); return (diameter) => diameter * PI; })(3.14159265) (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-environment]] - shared statements and technical atoms: Environment shares source evidence from are consts also from a shadowy planet?: We can test this by creating another conflict. But instead of binding two different variables to the same name in two different places, we'll bind two different valu ... [truncated]; Environment shares technical record from are consts also from a shadowy planet?: ((PI) => { ((PI) => {})(3); return (diameter) => diameter * PI; })(3.14159265) (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-parameter]] - shared statements and technical atoms: Parameter shares source evidence from const and lexical scope: Yes. Binding values to names with const works just like binding values to names with parameter invocations, it uses lexical scope.; Parameter shares technical record from are consts also from a shadowy planet?: ((diameter) => { const PI = 3.14159265; (() => { const PI = 3; })(); return diameter * PI; })(2) //=> 6.2831853 (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-block]] - shared technical atoms: Block shares technical record from Reassignment: (() => { let age = 49; if ( true ) { let age = 50; } return age; })() //=> 49 (3 shared atom(s))
- [[javascriptallonge-array]] - shared technical atoms: Array shares technical table: 42 You should never attempt to define your own bindings against 'magic' names that JavaScript binds for you. It is wise to treat them as read-only at all times. 43 W ... [truncated] (1 shared atom(s))
- [[javascriptallonge-function]] - shared technical atoms: Function shares technical table: 42 You should never attempt to define your own bindings against 'magic' names that JavaScript binds for you. It is wise to treat them as read-only at all times. 43 W ... [truncated] (1 shared atom(s))
- [[javascriptallonge-function-keyword]] - shared technical atoms: the function keyword shares technical table: 42 You should never attempt to define your own bindings against 'magic' names that JavaScript binds for you. It is wise to treat them as read-only at all times. 43 W ... [truncated] (1 shared atom(s))
- [[javascriptallonge-javascript]] - shared technical atoms: Javascript shares technical table: 42 You should never attempt to define your own bindings against 'magic' names that JavaScript binds for you. It is wise to treat them as read-only at all times. 43 W ... [truncated] (1 shared atom(s))
- [[javascriptallonge-object]] - shared technical atoms: Object shares technical table: 42 You should never attempt to define your own bindings against 'magic' names that JavaScript binds for you. It is wise to treat them as read-only at all times. 43 W ... [truncated] (1 shared atom(s))
- [[javascriptallonge-value]] - shared statements: Value shares source evidence from const and lexical scope: Yes. Binding values to names with const works just like binding values to names with parameter invocations, it uses lexical scope. (2 shared statement(s))
- [[javascriptallonge-const]] - shared statements: Const shares source evidence from const and lexical scope: Yes. Binding values to names with const works just like binding values to names with parameter invocations, it uses lexical scope. (1 shared statement(s))
- [[javascriptallonge-evaluating]] - shared statements: Evaluating shares source evidence from Reassignment: Like evaluating variable labels, when a binding is rebound, JavaScript searches for the binding in the current environment and then each ancestor in turn until it fi ... [truncated] (1 shared statement(s))
- [[javascriptallonge-instead]] - shared statements: Instead shares source evidence from are consts also from a shadowy planet?: We can test this by creating another conflict. But instead of binding two different variables to the same name in two different places, we'll bind two different valu ... [truncated] (1 shared statement(s))

## Source

- [[javascriptallonge]]
