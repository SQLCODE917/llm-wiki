---
page_id: javascriptallonge-section-disclaimer-da38fc1d
page_kind: source
summary: Disclaimer: 12 source-backed entries and 4 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-disclaimer-da38fc1d@72945bf3f5527d37ae6a2151987f9aba
---

# Disclaimer

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-disclaimer-1eabd0c5]] - same source heading: another source section with the same heading, Disclaimer

## Statements

- The recipes are written for practicality, and their implementation may introduce JavaScript features that haven't been discussed in the text to this point, such as methods and/or prototypes. The overall use of each recipe will fit within the spirit of the language discussed so far, even if the implementations may not. _(javascriptallonge.pdf (source-range-31a4cf47-00658))_
- These two recipes are for quickly and simply applying a single argument, either the leftmost or rightmost. 48 If you want to bind more than one argument, or you want to leave a 'hole' in the argument list, you will need to either use a generalized partial recipe, or you will need to repeatedly apply arguments. They are context-agnostic. _(javascriptallonge.pdf (source-range-31a4cf47-00660))_
- As noted above, our partial recipe allows us to create functions that are partial applications of functions that are context aware. We'd need a different recipe if we wish to create partial applications of object methods. _(javascriptallonge.pdf (source-range-31a4cf47-00662))_
- callFirst and callLast were inspired by Michael Fogus' Lemonad. Thanks! _(javascriptallonge.pdf (source-range-31a4cf47-00664))_
- We take it a step further, and can use gathering and spreading to allow for partial application with more than one argument: _(javascriptallonge.pdf (source-range-31a4cf47-00665))_
- The recipes are written for practicality, and their implementation may introduce JavaScript features that haven't been discussed in the text to this point, such as methods and/or prototypes. _(javascriptallonge.pdf (source-range-31a4cf47-00658))_
- The overall use of each recipe will fit within the spirit of the language discussed so far, even if the implementations may not. _(javascriptallonge.pdf (source-range-31a4cf47-00658))_

## Technical atoms

### Technical frame 1: Disclaimer

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00662))_

> As noted above, our partial recipe allows us to create functions that are partial applications of functions that are context aware. We'd need a different recipe if we wish to create partial applications of object methods.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00661))_

```
const callFirst = (fn, larg) => function (...rest) { return fn.call( this , larg, ...rest); } const callLast = (fn, rarg) => function (...rest) { return fn.call( this , ...rest, rarg); } const greet = (me, you) => `Hello, ${ you } , my name is ${ me } `; const heliosSaysHello = callFirst(greet, 'Helios'); heliosSaysHello('Eartha') //=> 'Hello, Eartha, my name is Helios' const sayHelloToCeline = callLast(greet, 'Celine'); sayHelloToCeline('Eartha') //=> 'Hello, Celine, my name is Eartha'
```

### Technical frame 2: Disclaimer

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00665))_

> We take it a step further, and can use gathering and spreading to allow for partial application with more than one argument:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00666))_

```
const callLeft = (fn, ...args) => (...remainingArgs) => fn(...args, ...remainingArgs); const callRight = (fn, ...args) => (...remainingArgs) => fn(...remainingArgs, ...args);
```

### Technical atom 3

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

### Technical atom 4

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00660))_

> These two recipes are for quickly and simply applying a single argument, either the leftmost or rightmost. 48 If you want to bind more than one argument, or you want to leave a 'hole' in the argument list, you will need to either use a generalized partial recipe, or you will need to repeatedly apply arguments. They are context-agnostic.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00663))_

| entry | content |
| --- | --- |
| 45 | https://github.com/fogus/lemonad |
| 46 | http://osteele.com/sources/javascript/functional/ |
| 47 | https://github.com/substack/node-ap 48 |

<details>
<summary>Raw table text</summary>

```
45 https://github.com/fogus/lemonad 46 http://osteele.com/sources/javascript/functional/ 47 https://github.com/substack/node-ap 48
```

</details>
