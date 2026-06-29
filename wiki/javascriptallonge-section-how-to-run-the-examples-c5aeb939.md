---
page_id: javascriptallonge-section-how-to-run-the-examples-c5aeb939
page_kind: source
summary: How to run the examples: 16 source-backed entries and 8 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-how-to-run-the-examples-c5aeb939@2a33a1230181b61775736196091b5cd1
---

# How to run the examples

From [[javascriptallonge]].

## Statements

- At the time this book was written, ECMAScript 2015 was not yet widely available. All of the examples in this book were tested using either Google Traceur Compiler 100 , Babel 101 , or both. Traceur and Babel are both transpilers , they work by parsing ECMAScript 2015 code, then emitting valid ECMAScript-5 code that produces the same semantics. _(javascriptallonge.pdf (source-range-8eb13d6b-01964))_
- Both tools offer an online area where you can type ECMAScript code into a web browser and see the ECMAScript-5 equivalent, and you can run the code as well. To see the result of your expressions, you may have to use the console in your web browser. _(javascriptallonge.pdf (source-range-8eb13d6b-01975))_
- And 4 would appear in your browser's development console. _(javascriptallonge.pdf (source-range-8eb13d6b-01980))_
- You can also install the transpilers on your development system and use them with Node 102 on the command line 103 . The care and feeding of node and npm are beyond the scope of this book, but both tools offer clear instructions for those who have already installed node . _(javascriptallonge.pdf (source-range-8eb13d6b-01981))_
- Traceur and Babel are both transpilers , they work by parsing ECMAScript 2015 code, then emitting valid ECMAScript-5 code that produces the same semantics. _(javascriptallonge.pdf (source-range-8eb13d6b-01964))_

## Technical atoms

### Technical frame 1: How to run the examples

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01964))_

> At the time this book was written, ECMAScript 2015 was not yet widely available. All of the examples in this book were tested using either Google Traceur Compiler 100 , Babel 101 , or both. Traceur and Babel are both transpilers , they work by parsing ECMAScript 2015 code, then emitting valid ECMAScript-5 code that produces the same semantics.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01966))_

```
const before = (decoration) => (method) => function () { decoration.apply( this , arguments); return method.apply( this , arguments) };
```

### Technical frame 2: How to run the examples

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01975))_

> Both tools offer an online area where you can type ECMAScript code into a web browser and see the ECMAScript-5 equivalent, and you can run the code as well. To see the result of your expressions, you may have to use the console in your web browser.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01968))_

```
"use strict" var before = function (decoration) { return function (method) { return function () { decoration.apply( this , arguments); return method.apply( this , arguments); }; }; };
```

### Technical frame 3: How to run the examples

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01975))_

> Both tools offer an online area where you can type ECMAScript code into a web browser and see the ECMAScript-5 equivalent, and you can run the code as well. To see the result of your expressions, you may have to use the console in your web browser.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01970))_

> [Figure] (p.289)

### Technical frame 4: How to run the examples

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01975))_

> Both tools offer an online area where you can type ECMAScript code into a web browser and see the ECMAScript-5 equivalent, and you can run the code as well. To see the result of your expressions, you may have to use the console in your web browser.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01973))_

```
100 101 http://babeljs.io/
```

### Technical frame 5: How to run the examples

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01975))_

> Both tools offer an online area where you can type ECMAScript code into a web browser and see the ECMAScript-5 equivalent, and you can run the code as well. To see the result of your expressions, you may have to use the console in your web browser.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01974))_

```
const before = (decoration) => (method) => function (...args) { decoration.apply( this , args); return method.apply( this , args) }; And it would be 'transpiled' into: var before = function (decoration) { return function (method) { return function () { for ( let _len = arguments.length, args = Array(_len), _key = 0; _key < _le\ n; _key++) { args[_key] = arguments[_key]; } decoration.apply( this , args); return method.apply( this , args); }; }; };
```

### Technical frame 6: How to run the examples

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01980))_

> And 4 would appear in your browser's development console.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01977))_

```
(() => 2 + 2)()
```

### Technical frame 7: How to run the examples

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01980))_

> And 4 would appear in your browser's development console.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01979))_

```
console.log( (() => 2 + 2)() )
```

### Technical atom 8

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01981))_

> You can also install the transpilers on your development system and use them with Node 102 on the command line 103 . The care and feeding of node and npm are beyond the scope of this book, but both tools offer clear instructions for those who have already installed node .

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01982))_

| entry | content |
| --- | --- |
| 102 | http://nodejs.org/ |
| 103 | https://en.wikipedia.org/wiki/REPL |

<details>
<summary>Raw table text</summary>

```
102 http://nodejs.org/
103 https://en.wikipedia.org/wiki/REPL
```

</details>
