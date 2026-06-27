---
page_id: javascriptallonge-section-left-variadic-functions-2167177b
page_kind: source
summary: Left-Variadic Functions: 26 source-backed entries and 11 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-left-variadic-functions-2167177b@7808d71ab088fc73958bcdac585c9508
---

# Left-Variadic Functions

From [[javascriptallonge]].

## Statements

- A _variadic function_ is a function that is designed to accept a variable number of arguments.[52] In JavaScript, you can make a variadic function by gathering parameters. _(javascriptallonge.pdf (source-range-83ecb080-01039))_
- This can be useful when writing certain kinds of destructuring algorithms. _(javascriptallonge.pdf (source-range-83ecb080-01041))_
- For example, we might want to have a function that builds some kind of team record. _(javascriptallonge.pdf (source-range-83ecb080-01041))_
- For example, we might want to have a function that builds some kind of team record. _(javascriptallonge.pdf (source-range-83ecb080-01041))_
- > 52English is about as inconsistent as JavaScript: Functions with a fixed number of arguments can be unary, binary, ternary, and so forth. _(javascriptallonge.pdf (source-range-83ecb080-01044))_
- ECMAScript 2015 only permits gathering parameters from the _end_ of the parameter list. _(javascriptallonge.pdf (source-range-83ecb080-01048))_
- In “Ye Olde Days,”[53] JavaScript could not gather parameters, and we had to either do backflips with arguments and .slice, or we wrote ourselves a variadic decorator that could gather arguments into the last declared parameter. _(javascriptallonge.pdf (source-range-83ecb080-01050))_
- “Ye” in “Ye Olde,” was not actually spelled with a “Y” in days of old, it was spelled with a thorn, and is pronounced “the.” Another word, “Ye” in “Ye of little programming faith,” is pronounced “ye,” but it’s a different word altogether. _(javascriptallonge.pdf (source-range-83ecb080-01053))_
- This is a _right-variadic function_ , meaning that it has one or more fixed arguments, and the rest are gathered into the rightmost argument. _(javascriptallonge.pdf (source-range-83ecb080-01060))_
- All left-variadic functions have one or more fixed arguments, and the rest are gathered into the leftmost argument. _(javascriptallonge.pdf (source-range-83ecb080-01064))_
- We sure can, by using the techniques from rightVariadic. _(javascriptallonge.pdf (source-range-83ecb080-01065))_
- Our leftVariadic function is a decorator that turns any function into a function that gathers parameters _from the left_ , instead of from the right. _(javascriptallonge.pdf (source-range-83ecb080-01072))_
- Gathering arguments for functions is one of the ways JavaScript can _destructure_ arrays. _(javascriptallonge.pdf (source-range-83ecb080-01074))_
- But we can write our own left-gathering function utility using the same principles without all the tedium: _(javascriptallonge.pdf (source-range-83ecb080-01084))_
- With leftGather, we have to supply the length of the array we wish to use as the result, and it gathers excess arguments into it from the left, just like leftVariadic gathers excess parameters for a function. _(javascriptallonge.pdf (source-range-83ecb080-01086))_

## Technical atoms

> Context: A _variadic function_ is a function that is designed to accept a variable number of arguments.[52] In JavaScript, you can make a variadic function by gathering parameters. For example:
_(context: javascriptallonge.pdf (source-range-83ecb080-01039))_

> **const** abccc = (a, b, ...c) => { console.log(a); console.log(b); console.log(c); }; abccc(1, 2, 3, 4, 5) 1 2 [3,4,5]
_(source: javascriptallonge.pdf (source-range-83ecb080-01040))_

> Context: In “Ye Olde Days,”[53] JavaScript could not gather parameters, and we had to either do backflips with arguments and .slice, or we wrote ourselves a variadic decorator that could gather arguments into the last declared parameter. Here it is in all of its ECMAScript-5 glory:
_(context: javascriptallonge.pdf (source-range-83ecb080-01050))_

> **var** __slice = Array.prototype.slice;
_(source: javascriptallonge.pdf (source-range-83ecb080-01051))_

> Context: We don’t need rightVariadic any more, because instead of:
_(context: javascriptallonge.pdf (source-range-83ecb080-01056))_

> **var** firstAndButFirst = rightVariadic( **function** test (first, butFirst) { **return** [first, butFirst] });
_(source: javascriptallonge.pdf (source-range-83ecb080-01057))_

> Context: We now simply write:
_(context: javascriptallonge.pdf (source-range-83ecb080-01058))_

> **const** firstAndButFirst = (first, ...butFirst) => [first, butFirst];
_(source: javascriptallonge.pdf (source-range-83ecb080-01059))_

> Context: It’s nice to have progress. But as noted above, we can’t write:
_(context: javascriptallonge.pdf (source-range-83ecb080-01062))_

> **const** butLastAndLast = (...butLast, last) => [butLast, last];
_(source: javascriptallonge.pdf (source-range-83ecb080-01063))_

> **const** butLastAndLast = leftVariadic((butLast, last) => [butLast, last]);
_(source: javascriptallonge.pdf (source-range-83ecb080-01070))_

> Context: Gathering arguments for functions is one of the ways JavaScript can _destructure_ arrays. Another way is when assigning variables, like this:
_(context: javascriptallonge.pdf (source-range-83ecb080-01074))_

> **const** [first, ...butFirst] = ['why', 'hello', 'there', 'little', 'droid'];
_(source: javascriptallonge.pdf (source-range-83ecb080-01075))_

> Context: Gathering arguments for functions is one of the ways JavaScript can _destructure_ arrays. Another way is when assigning variables, like this:
_(context: javascriptallonge.pdf (source-range-83ecb080-01074))_

> first _//=> 'why'_ butFirst _//=> ["hello","there","little","droid"]_
_(source: javascriptallonge.pdf (source-range-83ecb080-01076))_

> Context: As with parameters, we can’t gather values from the left when destructuring an array:
_(context: javascriptallonge.pdf (source-range-83ecb080-01077))_

> **const** [...butLast, last] = ['why', 'hello', 'there', 'little', 'droid']; _//=> Unexpected token_
_(source: javascriptallonge.pdf (source-range-83ecb080-01078))_

> Context: We could use leftVariadic the hard way:
_(context: javascriptallonge.pdf (source-range-83ecb080-01079))_

> **const** [butLast, last] = leftVariadic((butLast, last) => [butLast, last])(...['wh\ y', 'hello', 'there', 'little', 'droid']);
_(source: javascriptallonge.pdf (source-range-83ecb080-01082))_

> butLast _//=> ['why', 'hello', 'there', 'little']_ last _//=> 'droid'_
_(source: javascriptallonge.pdf (source-range-83ecb080-01083))_
