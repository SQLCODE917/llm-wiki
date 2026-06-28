---
page_id: javascriptallonge-section-how-to-run-the-examples-b750eb0e
page_kind: source
summary: How to run the examples: 9 source-backed entries and 0 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-how-to-run-the-examples-b750eb0e@26e6dfaefba9294036ebcf9aa7fe228a
---

# How to run the examples

From [[javascriptallonge]].

## Statements

- The Golden Crema: Appendices and Afterwords

266

## **How to run the examples**

At the time this book was written, ECMAScript 2015 was not yet widely available. All of the examples in this book were tested using either Google Traceur Compiler[100] , Babel[101] , or both. Traceur and Babel are both _transpilers_ , they work by parsing ECMAScript 2015 code, then emitting valid ECMAScript-5 code that produces the same semantics.

For example, this ECMAScript 2015 code: **const** before = (decoration) => (method) => **function** () { decoration.apply( **this** , arguments); **return** method.apply( **this** , arguments) };

Is translated into this ECMAScript-5 code: "use strict" **var** before = **function** (decoration) { **return function** (method) { **return function** () { decoration.apply( **this** , arguments); **return** method.apply( **this** , arguments); }; }; };

**==> picture [244 x 135] intentionally omitted <==**

**The Babel “try it out” page**

If we make it even more idiomatic, we could write:

> 100https://github.com/google/traceur-compiler 101http://babeljs.io/ _(javascriptallonge.pdf (source-range-83ecb080-00335))_
- The Golden Crema: Appendices and Afterwords

267 **const** before = (decoration) => (method) => **function** (...args) { decoration.apply( **this** , args); **return** method.apply( **this** , args) }; And it would be “transpiled” into: **var** before = **function** (decoration) { **return function** (method) { **return function** () { **for** ( **let** _len = arguments.length, args = Array(_len), _key = 0; _key < _le\ n; _key++) { args[_key] = arguments[_key]; } decoration.apply( **this** , args); **return** method.apply( **this** , args); }; }; };

Both tools offer an online area where you can type ECMAScript code into a web browser and see the ECMAScript-5 equivalent, and you can run the code as well. To see the result of your expressions, you may have to use the console in your web browser.

So instead of just writing: (() => 2 + 2)() And having 4 displayed, you’d need to write: console.log( (() => 2 + 2)() ) And 4 would appear in your browser’s development console.

You can also install the transpilers on your development system and use them with Node[102] on the command line[103] . The care and feeding of node and npm are beyond the scope of this book, but both tools offer clear instructions for those who have already installed node.

> 102http://nodejs.org/

> 103https://en.wikipedia.org/wiki/REPL _(javascriptallonge.pdf (source-range-83ecb080-00336))_
- Traceur and Babel are both _transpilers_ , they work by parsing ECMAScript 2015 code, then emitting valid ECMAScript-5 code that produces the same semantics. _(javascriptallonge.pdf (source-range-83ecb080-00335))_
