---
page_id: javascriptallonge-node
page_kind: concept
summary: Node: 4 statement(s) and 0 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-node@ade37abfce47c428be30d5328b70df70
---

# Node

What [[javascriptallonge]] covers about node:

## Statements

### A Rich Aroma: Basic Numbers

- A Rich Aroma: Basic Numbers

2 all numbers are base ten. If we start a literal with a zero, it is an octal literal. So the literal 042 is 42 base 8, which is actually 34 base 10.

Internally, both 042 and 34 have the same representation, as double-precision floating point[13] numbers. A computer’s internal representation for numbers is important to understand. The machine’s representation of a number almost never lines up perfectly with our understanding of how a number behaves, and thus there will be places where the computer’s behaviour surprises us if we don’t know a little about what it’s doing “under the hood.” For example, the largest integer JavaScript can safely[14] handle is 9007199254740991, or 2[‘53‘] - 1. Like most programming languages, JavaScript does not allow us to use commas to separate groups of digits.

## **floating**

Most programmers never encounter the limit on the magnitude of an integer. But we mentioned that numbers are represented internally as floating point, meaning that they need not be just integers. We can, for example, write 1.5 or 33.33, and JavaScript represents these literals as floating point numbers.

It’s tempting to think we now have everything we need to do things like handle amounts of money, but as the late John Belushi would say, “Nooooooooooooooooooooo.” A computer’s internal representation for a floating point number is binary, while our literal number was in base ten. This makes no meaningful difference for integers, but it does for fractions, because some fractions base 10 do not have exact representations base 2.

One of the most oft-repeated examples is this:

- 1.0 _//=> 1_

- 1.0 + 1.0 _//=> 2_

- 1.0 + 1.0 + 1.0 _//=> 3_ However:

> 13http://en.wikipedia.org/wiki/Double-precision_floating-point_format

> 14Implementations of JavaScript are free to handle larger numbers. For example, if you type 9007199254740991 + 9007199254740991 into node.js, it will happily report that the answer is 18014398509481982. But code that depends upon numbers larger than 9007199254740991 may not be reliable when moved to other implementations. _(javascriptallonge.pdf (source-range-83ecb080-00038))_

### Mutation

- 123

Composing and Decomposing Data **const** copy = (node, head = **null** , tail = **null** ) => { **if** (node === EMPTY) { **return** head; } **else if** (tail === **null** ) { **const** { first, rest } = node; **const** newNode = { first, rest }; **return** copy(rest, newNode, newNode); } **else** { **const** { first, rest } = node; **const** newNode = { first, rest }; tail.rest = newNode; **return** copy(node.rest, head, newNode); } } This algorithm makes copies of nodes as it goes, and mutates the last node in the list so that it can splice the next one on. Adding a node to an existing list is risky, as we saw when considering the fact that OneToFive and ThreeToFive share the same nodes. But when we’re in the midst of creating a brand new list, we aren’t sharing any nodes with any other lists, and we can afford to be more liberal about using mutation to save space and/or time.

Armed with this basic copy implementation, we can write mapWith: **const** mapWith = (fn, node, head = **null** , tail = **null** ) => { **if** (node === EMPTY) { **return** head; } **else if** (tail === **null** ) { **const** { first, rest } = node; **const** newNode = { first: fn(first), rest }; **return** mapWith(fn, rest, newNode, newNode); } **else** { **const** { first, rest } = node; **const** newNode = { first: fn(first), rest }; tail.rest = newNode; **return** mapWith(fn, node.rest, head, newNode); } } mapWith((x) => 1.0 / x, OneToFive) _(javascriptallonge.pdf (source-range-83ecb080-00174))_

### How to run the examples

- The Golden Crema: Appendices and Afterwords

267 **const** before = (decoration) => (method) => **function** (...args) { decoration.apply( **this** , args); **return** method.apply( **this** , args) }; And it would be “transpiled” into: **var** before = **function** (decoration) { **return function** (method) { **return function** () { **for** ( **let** _len = arguments.length, args = Array(_len), _key = 0; _key < _le\ n; _key++) { args[_key] = arguments[_key]; } decoration.apply( **this** , args); **return** method.apply( **this** , args); }; }; };

Both tools offer an online area where you can type ECMAScript code into a web browser and see the ECMAScript-5 equivalent, and you can run the code as well. To see the result of your expressions, you may have to use the console in your web browser.

So instead of just writing: (() => 2 + 2)() And having 4 displayed, you’d need to write: console.log( (() => 2 + 2)() ) And 4 would appear in your browser’s development console.

You can also install the transpilers on your development system and use them with Node[102] on the command line[103] . The care and feeding of node and npm are beyond the scope of this book, but both tools offer clear instructions for those who have already installed node.

> 102http://nodejs.org/

> 103https://en.wikipedia.org/wiki/REPL _(javascriptallonge.pdf (source-range-83ecb080-00336))_


## Related pages

- [[javascriptallonge-list]] - shared statements: List shares source evidence from Mutation: 123  Composing and Decomposing Data **const** copy = (node, head = **null** , tail = **null** ) => { **if** (node === EMPTY) { **return** head; } **else if** (tail = ... [truncated] (2 shared statement(s))
- [[javascriptallonge-type]] - shared statements: Type shares source evidence from A Rich Aroma: Basic Numbers: A Rich Aroma: Basic Numbers  2 all numbers are base ten. If we start a literal with a zero, it is an octal literal. So the literal 042 is 42 base 8, which is actuall ... [truncated] (1 shared statement(s))

## Source

- [[javascriptallonge]]
