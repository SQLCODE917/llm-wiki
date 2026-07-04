---
page_id: javascriptallonge-section-left-variadic-functions-93903312
page_kind: source
page_family: section-reference
summary: Left-Variadic Functions: 11 source-backed entries and 0 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-03
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-left-variadic-functions-93903312@60561de3dc81a0ea61da4adda63a8b01
---

# Left-Variadic Functions

From [[javascriptallonge]].

## Statements

- Recipes with Basic Functions 

66 

## **Left-Variadic Functions** 

A _variadic function_ is a function that is designed to accept a variable number of arguments.[52] In JavaScript, you can make a variadic function by gathering parameters. For example: 

**const** abccc = (a, b, ...c) => { console.log(a); console.log(b); console.log(c); }; abccc(1, 2, 3, 4, 5) 1 2 [3,4,5] 

This can be useful when writing certain kinds of destructuring algorithms. For example, we might want to have a function that builds some kind of team record. It accepts a coach, a captain, and an arbitrary number of players. Easy in ECMAScript 2015: 

**function** team(coach, captain, ...players) { console.log(` **${** captain **}** (captain)`); **for** ( **let** player **of** players) { console.log(player); } console.log(`squad coached by **${** coach **}** `); } team('Luis Enrique', 'Xavi Hernández', 'Marc-André ter Stegen', 'Martín Montoya', 'Gerard Piqué') _//=>_ Xavi Hernández (captain) Marc-André ter Stegen Martín Montoya Gerard Piqué squad coached by Luis Enrique 

## But we can’t go the other way around: 

> 52English is about as inconsistent as JavaScript: Functions with a fixed number of arguments can be unary, binary, ternary, and so forth. But can they be “variary?” No! They have to be “variadic.” _(javascriptallonge.pdf (source-range-af806fb1-00109))_
- Recipes with Basic Functions 

67 

**function** team2(...players, captain, coach) { console.log(` **${** captain **}** (captain)`); **for** ( **let** player **of** players) { console.log(player); } console.log(`squad coached by **${** coach **}** `); } _//=> Unexpected token_ 

ECMAScript 2015 only permits gathering parameters from the _end_ of the parameter list. Not the beginning. What to do? 

## **a history lesson** 

In “Ye Olde Days,”[53] JavaScript could not gather parameters, and we had to either do backflips with arguments and .slice, or we wrote ourselves a variadic decorator that could gather arguments into the last declared parameter. Here it is in all of its ECMAScript-5 glory: 

**var** __slice = Array.prototype.slice; 

**function** rightVariadic (fn) { **if** (fn.length < 1) **return** fn; **return function** () { **var** ordinaryArgs = (1 <= arguments.length ? __slice.call(arguments, 0, fn.length - 1) : []), restOfTheArgsList = __slice.call(arguments, fn.length - 1), args = (fn.length <= arguments.length ? ordinaryArgs.concat([restOfTheArgsList]) : []); **return** fn.apply( **this** , args); } }; **var** firstAndButFirst = rightVariadic( **function** test (first, butFirst) { **return** [first, butFirst] }); firstAndButFirst('why', 'hello', 'there', 'little', 'droid') _//=> ["why",["hello","there","little","droid"]]_ 

53Another history lesson. “Ye” in “Ye Olde,” was not actually spelled with a “Y” in days of old, it was spelled with a thorn, and is pronounced “the.” Another word, “Ye” in “Ye of little programming faith,” is pronounced “ye,” but it’s a different word altogether. _(javascriptallonge.pdf (source-range-af806fb1-00110))_
- Recipes with Basic Functions 

68 

We don’t need rightVariadic any more, because instead of: 

**var** firstAndButFirst = rightVariadic( **function** test (first, butFirst) { **return** [first, butFirst] }); 

We now simply write: 

**const** firstAndButFirst = (first, ...butFirst) => [first, butFirst]; 

This is a _right-variadic function_ , meaning that it has one or more fixed arguments, and the rest are gathered into the rightmost argument. 

## **overcoming limitations** 

It’s nice to have progress. But as noted above, we can’t write: 

**const** butLastAndLast = (...butLast, last) => [butLast, last]; 

That’s a _left-variadic function_ . All left-variadic functions have one or more fixed arguments, and the rest are gathered into the leftmost argument. JavaScript doesn’t do this. But if we wanted to write left-variadic functions, could we make ourselves a leftVariadic decorator to turn a function with one or more arguments into a left-variadic function? 

We sure can, by using the techniques from rightVariadic. Mind you, we can take advantage of modern JavaScript to simplify the code: 

**const** leftVariadic = (fn) => { **if** (fn.length < 1) { **return** fn; } **else** { **return function** (...args) { **const** gathered = args.slice(0, args.length - fn.length + 1), spread = args.slice(args.length - fn.length + 1); **return** fn.apply( **this** , [gathered].concat(spread) _(javascriptallonge.pdf (source-range-af806fb1-00111))_
- 69 

Recipes with Basic Functions 

); } } }; 

**const** butLastAndLast = leftVariadic((butLast, last) => [butLast, last]); 

butLastAndLast('why', 'hello', 'there', 'little', 'droid') _//=> [["why","hello","there","little"],"droid"]_ 

Our leftVariadic function is a decorator that turns any function into a function that gathers parameters _from the left_ , instead of from the right. 

## **left-variadic destructuring** 

Gathering arguments for functions is one of the ways JavaScript can _destructure_ arrays. Another way is when assigning variables, like this: 

**const** [first, ...butFirst] = ['why', 'hello', 'there', 'little', 'droid']; 

first _//=> 'why'_ butFirst _//=> ["hello","there","little","droid"]_ 

As with parameters, we can’t gather values from the left when destructuring an array: 

**const** [...butLast, last] = ['why', 'hello', 'there', 'little', 'droid']; _//=> Unexpected token_ 

We could use leftVariadic the hard way: _(javascriptallonge.pdf (source-range-af806fb1-00112))_
- 70 

Recipes with Basic Functions 

**const** [butLast, last] = leftVariadic((butLast, last) => [butLast, last])(...['wh\ y', 'hello', 'there', 'little', 'droid']); 

butLast _//=> ['why', 'hello', 'there', 'little']_ last _//=> 'droid'_ 

But we can write our own left-gathering function utility using the same principles without all the tedium: 

**const** leftGather = (outputArrayLength) => { **return function** (inputArray) { **return** [inputArray.slice(0, inputArray.length - outputArrayLength + 1)].conc\ at( inputArray.slice(inputArray.length - outputArrayLength + 1) ) } }; **const** [butLast, last] = leftGather(2)(['why', 'hello', 'there', 'little', 'droid\ ']); butLast _//=> ['why', 'hello', 'there', 'little']_ last _//=> 'droid'_ 

With leftGather, we have to supply the length of the array we wish to use as the result, and it gathers excess arguments into it from the left, just like leftVariadic gathers excess parameters for a function. _(javascriptallonge.pdf (source-range-af806fb1-00113))_
- For example, we might want to have a function that builds some kind of team record. _(javascriptallonge.pdf (source-range-af806fb1-00109))_
