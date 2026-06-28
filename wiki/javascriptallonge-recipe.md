---
page_id: javascriptallonge-recipe
page_kind: concept
summary: Recipe: 5 statement(s) and 5 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-recipe@bfb8a0d6d06e841b2aaef71eca07c96a
---

# Recipe

What [[javascriptallonge]] covers about recipe:

## Statements

### Disclaimer

- The recipes are written for practicality, and their implementation may introduce JavaScript features that haven't been discussed in the text to this point, such as methods and/or prototypes. The overall use of each recipe will fit within the spirit of the language discussed so far, even if the implementations may not. _(javascriptallonge.pdf (source-range-31a4cf47-00658))_

- These two recipes are for quickly and simply applying a single argument, either the leftmost or rightmost. 48 If you want to bind more than one argument, or you want to leave a 'hole' in the argument list, you will need to either use a generalized partial recipe, or you will need to repeatedly apply arguments. They are context-agnostic. _(javascriptallonge.pdf (source-range-31a4cf47-00660))_

### Maybe

- This recipe concerns a pattern that is very common: A function fn takes a value as a parameter, and its behaviour by design is to do nothing if the parameter is nothing: _(javascriptallonge.pdf (source-range-31a4cf47-00696))_

- Naturally, there's a function decorator recipe for that, borrowed from Haskell's maybe monad 50 , Ruby's andand 51 , and CoffeeScript's existential method invocation: _(javascriptallonge.pdf (source-range-31a4cf47-00700))_

### Disclaimer

- The recipes are written for practicality, and their implementation may introduce JavaScript features that haven't been discussed in the text to this point, such as methods and/or prototypes. The overall use of each recipe will fit within the spirit of the language discussed so far, even if the implementations may not. _(javascriptallonge.pdf (source-range-31a4cf47-01428))_


## Technical atoms

### Technical frame 1: Disclaimer

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00662))_

> As noted above, our partial recipe allows us to create functions that are partial applications of functions that are context aware. We'd need a different recipe if we wish to create partial applications of object methods.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00661))_

```
const callFirst = (fn, larg) => function (...rest) { return fn.call( this , larg, ...rest); } const callLast = (fn, rarg) => function (...rest) { return fn.call( this , ...rest, rarg); } const greet = (me, you) => `Hello, ${ you } , my name is ${ me } `; const heliosSaysHello = callFirst(greet, 'Helios'); heliosSaysHello('Eartha') //=> 'Hello, Eartha, my name is Helios' const sayHelloToCeline = callLast(greet, 'Celine'); sayHelloToCeline('Eartha') //=> 'Hello, Celine, my name is Eartha'
```

### Technical frame 2: Maybe

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00698))_

> Alternately, the function may be intended to work with any value, but the code calling the function wishes to emulate the behaviour of doing nothing by design when given nothing:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00697))_

```
const isSomething = (value) => value !== null && value !== void 0; const checksForSomething = (value) => { if (isSomething(value)) { // function's true logic } }
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

### Technical atom 5

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00659))_

| entry | content |
| --- | --- |
| 45 | from Michael Fogus, Functional JavaScript |
| 46 | from Oliver Steele and the terse but handy node-ap |
| 47 | from James Halliday. |

<details>
<summary>Raw table text</summary>

```
Partial Application
In Building Blocks, we discussed partial application, but we didn't write a generalized recipe for it. This is such a common tool that many libraries provide some form of partial application. You'll find examples in Lemonad 45 from Michael Fogus, Functional JavaScript 46 from Oliver Steele and the terse but handy node-ap 47 from James Halliday.
```

</details>


## Related pages

- [[javascriptallonge-function]] - shared statements and technical atoms: Function shares source evidence from Maybe: Naturally, there's a function decorator recipe for that, borrowed from Haskell's maybe monad 50 , Ruby's andand 51 , and CoffeeScript's existential method invocation:; Function shares technical record from Maybe: const isSomething = (value) => value !== null && value !== void 0; const checksForSomething = (value) => { if (isSomething(value)) { // function's true logic } } (1 shared statement(s), 4 shared atom(s))
- [[javascriptallonge-pattern]] - shared statements and technical atoms: Pattern shares source evidence from Maybe: This recipe concerns a pattern that is very common: A function fn takes a value as a parameter, and its behaviour by design is to do nothing if the parameter is nothing:; Pattern shares technical record from Maybe: const isSomething = (value) => value !== null && value !== void 0; const checksForSomething = (value) => { if (isSomething(value)) { // function's true logic } } (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-argument]] - shared technical atoms: Argument shares technical record from Disclaimer: const callFirst = (fn, larg) => function (...rest) { return fn.call( this , larg, ...rest); } const callLast = (fn, rarg) => function (...rest) { return fn.call( thi ... [truncated] (1 shared atom(s))
- [[javascriptallonge-bind]] - shared technical atoms: Bind shares technical record from Disclaimer: const callFirst = (fn, larg) => function (...rest) { return fn.call( this , larg, ...rest); } const callLast = (fn, rarg) => function (...rest) { return fn.call( thi ... [truncated] (1 shared atom(s))
- [[javascriptallonge-block]] - shared technical atoms: Block shares technical table: Partial Application In Building Blocks, we discussed partial application, but we didn't write a generalized recipe for it. This is such a common tool that many libra ... [truncated] (1 shared atom(s))
- [[javascriptallonge-functional]] - shared technical atoms: Functional shares technical table: Partial Application In Building Blocks, we discussed partial application, but we didn't write a generalized recipe for it. This is such a common tool that many libra ... [truncated] (1 shared atom(s))
- [[javascriptallonge-javascript]] - shared technical atoms: Javascript shares technical table: Partial Application In Building Blocks, we discussed partial application, but we didn't write a generalized recipe for it. This is such a common tool that many libra ... [truncated] (1 shared atom(s))
- [[javascriptallonge-list]] - shared technical atoms: List shares technical record from Disclaimer: const callFirst = (fn, larg) => function (...rest) { return fn.call( this , larg, ...rest); } const callLast = (fn, rarg) => function (...rest) { return fn.call( thi ... [truncated] (1 shared atom(s))
- [[javascriptallonge-write]] - shared technical atoms: Write shares technical table: Partial Application In Building Blocks, we discussed partial application, but we didn't write a generalized recipe for it. This is such a common tool that many libra ... [truncated] (1 shared atom(s))

## Source

- [[javascriptallonge]]
