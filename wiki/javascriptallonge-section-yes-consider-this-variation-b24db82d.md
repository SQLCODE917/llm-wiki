---
page_id: javascriptallonge-section-yes-consider-this-variation-b24db82d
page_kind: source
summary: Yes. Consider this variation:: 16 source-backed entries and 6 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-yes-consider-this-variation-b24db82d@9c350f084634b8aba590da759267f427
---

# Yes. Consider this variation:

From [[javascriptallonge]].

## Statements

- What went wrong? Why didn't it give us 'Hello, Raganwald, my name is Friedrich'? The answer is that pesky var i . Remember that i is bound in the surrounding environment, so it's as if we wrote: _(javascriptallonge.pdf (source-range-31a4cf47-01213))_
- Now, at the time we created each function, i had a sensible value, like 0 , 1 , or 2 . But at the time we call one of the functions, i has the value 3 , which is why the loop terminated. So when the function is called, JavaScript looks i up in its enclosing environment (its closure, obviously), and gets the value 3 . That's not what we want at all. _(javascriptallonge.pdf (source-range-31a4cf47-01215))_
- This small error was a frequent cause of confusion, and in the days when there was no block-scoped let , programmers would need to know how to fake it, usually with an IIFE: _(javascriptallonge.pdf (source-range-31a4cf47-01218))_
- Now we're creating a new inner parameter, i and binding it to the value of the outer i . This works, but let is so much simpler and cleaner that it was added to the language in the ECMAScript 2015 specification. _(javascriptallonge.pdf (source-range-31a4cf47-01220))_
- In this book, we will use function declarations sparingly, and not use var at all. That does not mean that you should follow the exact same practice in your own code: The purpose of this book is to illustrate certain principles of programming. The purpose of your own code is to get things done. The two goals are often, but not always, aligned. _(javascriptallonge.pdf (source-range-31a4cf47-01221))_
- So when the function is called, JavaScript looks i up in its enclosing environment (its closure, obviously), and gets the value 3 . _(javascriptallonge.pdf (source-range-31a4cf47-01215))_

## Technical atoms

### Technical frame 1: Yes. Consider this variation:

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01213))_

> What went wrong? Why didn't it give us 'Hello, Raganwald, my name is Friedrich'? The answer is that pesky var i . Remember that i is bound in the surrounding environment, so it's as if we wrote:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01208))_

```
var introductions = [], names = ['Karl', 'Friedrich', 'Gauss']; for ( var i = 0; i < 3; i++) { introductions[i] = "Hello, my name is " + names[i] } introductions //=> [ 'Hello, my name is Karl', // 'Hello, my name is Friedrich', // 'Hello, my name is Gauss' ]
```

### Technical frame 2: Yes. Consider this variation:

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01213))_

> What went wrong? Why didn't it give us 'Hello, Raganwald, my name is Friedrich'? The answer is that pesky var i . Remember that i is bound in the surrounding environment, so it's as if we wrote:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01210))_

```
var introductions = [], names = ['Karl', 'Friedrich', 'Gauss']; for ( var i = 0; i < 3; i++) { introductions[i] = (soAndSo) => `Hello, ${ soAndSo } , my name is ${ names[i] } ` } introductions //=> [ [Function], // [Function], // [Function] ]
```

### Technical frame 3: Yes. Consider this variation:

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01213))_

> What went wrong? Why didn't it give us 'Hello, Raganwald, my name is Friedrich'? The answer is that pesky var i . Remember that i is bound in the surrounding environment, so it's as if we wrote:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01212))_

```
introductions[1]('Raganwald') //=> 'Hello, Raganwald, my name is undefined'
```

### Technical frame 4: Yes. Consider this variation:

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01215))_

> Now, at the time we created each function, i had a sensible value, like 0 , 1 , or 2 . But at the time we call one of the functions, i has the value 3 , which is why the loop terminated. So when the function is called, JavaScript looks i up in its enclosing environment (its closure, obviously), and gets the value 3 . That's not what we want at all.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01214))_

```
var introductions = [], names = ['Karl', 'Friedrich', 'Gauss'], i = undefined ; for (i = 0; i < 3; i++) { introductions[i] = function (soAndSo) { return "Hello, " + soAndSo + ", my name is " + names[i] } } introductions
```

### Technical frame 5: Yes. Consider this variation:

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01218))_

> This small error was a frequent cause of confusion, and in the days when there was no block-scoped let , programmers would need to know how to fake it, usually with an IIFE:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01217))_

```
let introductions = [], names = ['Karl', 'Friedrich', 'Gauss']; for ( let i = 0; i < 3; i++) { introductions[i] = (soAndSo) => `Hello, ${ soAndSo } , my name is ${ names[i] } ` } introductions[1]('Raganwald') //=> 'Hello, Raganwald, my name is Friedrich'
```

### Technical frame 6: Yes. Consider this variation:

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01220))_

> Now we're creating a new inner parameter, i and binding it to the value of the outer i . This works, but let is so much simpler and cleaner that it was added to the language in the ECMAScript 2015 specification.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01219))_

```
var introductions = [], names = ['Karl', 'Friedrich', 'Gauss']; for ( var i = 0; i < 3; i++) { ((i) => { introductions[i] = (soAndSo) => `Hello, ${ soAndSo } , my name is ${ names[i] } ` } })(i) } introductions[1]('Raganwald') //=> 'Hello, Raganwald, my name is Friedrich'
```
