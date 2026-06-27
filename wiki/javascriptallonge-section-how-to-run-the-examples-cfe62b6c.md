---
page_id: javascriptallonge-section-how-to-run-the-examples-cfe62b6c
page_kind: source
summary: How to run the examples: 14 source-backed entries and 5 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-how-to-run-the-examples-cfe62b6c@05848f9949ac0596b273fe9d3e530968
---

# How to run the examples

From [[javascriptallonge]].

## Statements

- At the time this book was written, ECMAScript 2015 was not yet widely available. _(javascriptallonge.pdf (source-range-83ecb080-03084))_
- Traceur and Babel are both _transpilers_ , they work by parsing ECMAScript 2015 code, then emitting valid ECMAScript-5 code that produces the same semantics. _(javascriptallonge.pdf (source-range-83ecb080-03084))_
- All of the examples in this book were tested using either Google Traceur Compiler[100] , Babel[101] , or both. _(javascriptallonge.pdf (source-range-83ecb080-03084))_
- Traceur and Babel are both _transpilers_ , they work by parsing ECMAScript 2015 code, then emitting valid ECMAScript-5 code that produces the same semantics. _(javascriptallonge.pdf (source-range-83ecb080-03084))_
- Both tools offer an online area where you can type ECMAScript code into a web browser and see the ECMAScript-5 equivalent, and you can run the code as well. _(javascriptallonge.pdf (source-range-83ecb080-03104))_
- To see the result of your expressions, you may have to use the console in your web browser. _(javascriptallonge.pdf (source-range-83ecb080-03104))_
- And 4 would appear in your browser’s development console. _(javascriptallonge.pdf (source-range-83ecb080-03109))_
- The care and feeding of node and npm are beyond the scope of this book, but both tools offer clear instructions for those who have already installed node. _(javascriptallonge.pdf (source-range-83ecb080-03110))_
- You can also install the transpilers on your development system and use them with Node[102] on the command line[103] . _(javascriptallonge.pdf (source-range-83ecb080-03110))_

## Technical atoms

> Context: For example, this ECMAScript 2015 code:
_(context: javascriptallonge.pdf (source-range-83ecb080-03085))_

> **const** before = (decoration) => (method) => **function** () { decoration.apply( **this** , arguments); **return** method.apply( **this** , arguments) };
_(source: javascriptallonge.pdf (source-range-83ecb080-03086))_

> Context: "use strict"
_(context: javascriptallonge.pdf (source-range-83ecb080-03088))_

> **var** before = **function** (decoration) {
_(source: javascriptallonge.pdf (source-range-83ecb080-03089))_

> **const** before = (decoration) => (method) => **function** (...args) { decoration.apply( **this** , args); **return** method.apply( **this** , args) };
_(source: javascriptallonge.pdf (source-range-83ecb080-03101))_

> Context: So instead of just writing:
_(context: javascriptallonge.pdf (source-range-83ecb080-03105))_

> (() => 2 + 2)()
_(source: javascriptallonge.pdf (source-range-83ecb080-03106))_

> Context: And having 4 displayed, you’d need to write:
_(context: javascriptallonge.pdf (source-range-83ecb080-03107))_

> console.log( (() => 2 + 2)() )
_(source: javascriptallonge.pdf (source-range-83ecb080-03108))_
