---
page_id: javascriptallonge-ecmascript
page_kind: concept
page_family: topic-concept
summary: Ecmascript: 11 statement(s) and 7 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-ecmascript@56023b45f593cde576a435daa6fa7113
---

# Ecmascript

What [[javascriptallonge]] covers about ecmascript:

## Statements

### A Pull of the Lever: Prefaces / About JavaScript Allongé / why the 'six' edition?

- ECMAScript 2015 (formerly called ECMAScript 6 or 'ES6'), is ushering in a very large number of improvements to the way programmers can write small, powerful components and combine them into larger, fully featured programs. Features like destructuring, block-structured variables, iterables, generators, and the class keyword are poised to make JavaScript programming more expressive. _(javascriptallonge.pdf (source-range-7239e085-00021))_

- Prior to ECMAScript 2015, JavaScript did not include many features that programmers have discovered are vital to writing great software. For example, JavaScript did not include block-structured variables. Over time, programmers discovered ways to roll their own versions of important features. _(javascriptallonge.pdf (source-range-7239e085-00022))_

- And the variable i is scoped locally to the code within the braces. Prior to ECMAScript 2015, JavaScript did not support block-structuring, so programmers borrowed a trick from the Scheme programming language, and would write: _(javascriptallonge.pdf (source-range-7239e085-00025))_

- Prior to ECMAScript 2015, JavaScript did not support collecting a variable number of arguments into a parameter, so programmers would take advantage of an awkward work-around and write things like: _(javascriptallonge.pdf (source-range-7239e085-00030))_

### A Pull of the Lever: Prefaces / About JavaScript Allongé / that's nice. is that the only reason?

- ECMAScript 2015 does more than simply update the language with some simpler syntax for a few things and help us avoid warts. It makes a number of interesting programming techniques easy to explain and easy to use. And these techniques dovetail nicely with Allongé's focus on composing entities and working with functions. _(javascriptallonge.pdf (source-range-7239e085-00045))_

### A Pull of the Lever: Prefaces / Foreword to the 'Six' edition

- ECMAScript 6 (short name: ES6; official name: ECMAScript 2015) was ratified as a standard on June 17. Getting there took a while - in a way, the origins of ES6 date back to the year 2000: After ECMAScript 3 was finished, TC39 (the committee evolving JavaScript) started to work on ECMAScript 4. That version was planned to have numerous new features (interfaces, namespaces, packages, multimethods, etc.), which would have turned JavaScript into a completely new language. After internal conflict, a settlement was reached in July 2008 and a new plan was made - to abandon ECMAScript 4 and to replace it with two upgrades: _(javascriptallonge.pdf (source-range-7239e085-00069))_

- A larger upgrade would substantially improve JavaScript, but without being as radical as ECMAScript 4. This upgrade became ECMAScript 6 (some features that were initially discussed will show up later, in upcoming ECMAScript versions). _(javascriptallonge.pdf (source-range-7239e085-00071))_

### ECMAScript 6 has three major groups of features:

- With ECMAScript 6, JavaScript has become much larger as a language. JavaScript Allongé, the 'Six' Edition is both a comprehensive tour of its features and a rich collection of techniques for making better use of them. You will learn much about functional programming and object-oriented programming. And you'll do so via ES6 code, handed to you in small, easily digestible pieces. _(javascriptallonge.pdf (source-range-7239e085-00079))_

### And also: / Naming Functions / the function keyword

- JavaScript does have a syntax for naming a function, we use the function keyword. Until ECMAScript 2015 was created, function was the usual syntax for writing functions. _(javascriptallonge.pdf (source-range-7239e085-00503))_

### Recipes with Basic Functions / Left-Variadic Functions

- ECMAScript 2015 only permits gathering parameters from the end of the parameter list. Not the beginning. What to do? _(javascriptallonge.pdf (source-range-7239e085-00723))_


## Technical atoms

### Technical frame 1: A Pull of the Lever: Prefaces / About JavaScript Allongé / why the 'six' edition?

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00028))_

> Likewise, many programming languages permit functions to have a variable number of arguments, and to collect the arguments into a single variable as an array. In Ruby, we can write:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00026))_

<a id="atom-technical-atom-4cc33f6651c07c8e"></a>

```
var i;
for (i = 0; i < array.length; ++i) {
(function (i) {
// ...
})(i)
}
```

### Technical frame 2: A Pull of the Lever: Prefaces / About JavaScript Allongé / why the 'six' edition?

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00032))_

> The first edition of JavaScript Allongé explained these and many other patterns for writing flexible and composable programs in JavaScript, but the intention wasn't to explain how to work around JavaScript's missing features: The intention was to explain why the style of programming exemplified by the missing features is important.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00031))_

<a id="atom-technical-atom-a9a0cf0809cc9f83"></a>

```
function foo () {
var first = arguments[0],
rest
= [].slice.call(arguments, 1);
// ...
}
```

### Technical frame 3: A Pull of the Lever: Prefaces / About JavaScript Allongé / why the 'six' edition?

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00038))_

> And presto, rest collects the rest of the arguments without a lot of malarky involving slicing arguments . Not having to work around these kinds of missing features makes JavaScript Allongé a better book , because it can focus on the why to do something and when to do it, instead of on the how to make it work

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00035))_

<a id="atom-technical-atom-f498e15a31d305c9"></a>

```
for (let i = 0; i < array.length; ++i) {
// ...
}
```

### Technical frame 4: Recipes with Basic Functions / Left-Variadic Functions

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00721))_

> 52 English is about as inconsistent as JavaScript: Functions with a fixed number of arguments can be unary, binary, ternary, and so forth. But can they be 'variary?' No! They have to be 'variadic.'

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00720))_

<a id="atom-technical-atom-f601b03ee56b156a"></a>

```
function team(coach, captain, ...players) {
console.log(`${captain} (captain)`);
for (let player of players) {
console.log(player);
}
console.log(`squad coached by ${coach}`);
}
team('Luis Enrique', 'Xavi Hernández', 'Marc-André ter Stegen',
'Martín Montoya', 'Gerard Piqué')
//=>
Xavi Hernández (captain)
Marc-André ter Stegen
Martín Montoya
Gerard Piqué
squad coached by Luis Enrique
But we can’t go the other way around:
```

### Technical frame 5: Recipes with Basic Functions / Left-Variadic Functions

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00723))_

> ECMAScript 2015 only permits gathering parameters from the end of the parameter list. Not the beginning. What to do?

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00722))_

<a id="atom-technical-atom-99a0f4a090bc346d"></a>

```
function team2(...players, captain, coach) {
console.log(`${captain} (captain)`);
for (let player of players) {
console.log(player);
}
console.log(`squad coached by ${coach}`);
}
//=> Unexpected token
```

### Technical frame 6: Recipes with Basic Functions / Left-Variadic Functions / a history lesson

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00731))_

> This is a right-variadic function , meaning that it has one or more fixed arguments, and the rest are gathered into the rightmost argument.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00726))_

<a id="atom-technical-atom-8365f6546f74797b"></a>

```
var __slice = Array.prototype.slice;
function rightVariadic (fn) {
if (fn.length < 1) return fn;
return function () {
var ordinaryArgs = (1 <= arguments.length ?
__slice.call(arguments, 0, fn.length - 1) : []),
restOfTheArgsList = __slice.call(arguments, fn.length - 1),
args = (fn.length <= arguments.length ?
ordinaryArgs.concat([restOfTheArgsList]) : []);
return fn.apply(this, args);
}
};
var firstAndButFirst = rightVariadic(function test (first, butFirst) {
return [first, butFirst]
});
firstAndButFirst('why', 'hello', 'there', 'little', 'droid')
//=> ["why",["hello","there","little","droid"]]
```


## Related pages

### Shared technical atoms

- [[javascriptallonge-javascript]] - shared statements and technical atoms: Javascript shares source evidence from A Pull of the Lever: Prefaces / About JavaScript Allongé / why the 'six' edition?: Prior to ECMAScript 2015, JavaScript did not include many features that programmers have discovered are vital to writing great software. For example, JavaScript did ... [truncated]; Javascript shares technical record from A Pull of the Lever: Prefaces / About JavaScript Allongé / why the 'six' edition?: var i; for (i = 0; i < array.length; ++i) { (function (i) { // ... })(i) } (4 shared statement(s), 5 shared atom(s))
- [[javascriptallonge-function]] - shared technical atoms: Function shares technical record from Recipes with Basic Functions / Left-Variadic Functions: function team(coach, captain, ...players) { console.log(`${captain} (captain)`); for (let player of players) { console.log(player); } console.log(`squad coached by $ ... [truncated] (3 shared atom(s))
- [[javascriptallonge-programmer]] - shared technical atoms: Programmer shares technical record from A Pull of the Lever: Prefaces / About JavaScript Allongé / why the 'six' edition?: var i; for (i = 0; i < array.length; ++i) { (function (i) { // ... })(i) } (3 shared atom(s))
- [[javascriptallonge-feature]] - shared statements and technical atoms: Feature shares source evidence from A Pull of the Lever: Prefaces / Foreword to the 'Six' edition: A larger upgrade would substantially improve JavaScript, but without being as radical as ECMAScript 4. This upgrade became ECMAScript 6 (some features that were init ... [truncated]; Feature shares technical record from A Pull of the Lever: Prefaces / About JavaScript Allongé / why the 'six' edition?: for (let i = 0; i < array.length; ++i) { // ... } (1 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-language]] - shared technical atoms: Language shares technical record from A Pull of the Lever: Prefaces / About JavaScript Allongé / why the 'six' edition?: var i; for (i = 0; i < array.length; ++i) { (function (i) { // ... })(i) } (2 shared atom(s))
- [[javascriptallonge-programming]] - shared technical atoms: Programming shares technical record from A Pull of the Lever: Prefaces / About JavaScript Allongé / why the 'six' edition?: var i; for (i = 0; i < array.length; ++i) { (function (i) { // ... })(i) } (2 shared atom(s))
- [[javascriptallonge-parameter]] - shared statements and technical atoms: Parameter shares source evidence from Recipes with Basic Functions / Left-Variadic Functions: ECMAScript 2015 only permits gathering parameters from the end of the parameter list. Not the beginning. What to do?; Parameter shares technical record from Recipes with Basic Functions / Left-Variadic Functions / a history lesson: var __slice = Array.prototype.slice; function rightVariadic (fn) { if (fn.length < 1) return fn; return function () { var ordinaryArgs = (1 <= arguments.length ? __s ... [truncated] (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-allong]] - shared technical atoms: Allong shares technical table: matthew knox A different kind of language requires a different kind of book. JavaScript holds surprising depths-its scoping rules are neither strictly lexical nor st ... [truncated] (1 shared atom(s))

### Shared claims

- [[javascriptallonge-function-keyword]] - shared statements: the function keyword shares source evidence from And also: / Naming Functions / the function keyword: JavaScript does have a syntax for naming a function, we use the function keyword. Until ECMAScript 2015 was created, function was the usual syntax for writing functions. (1 shared statement(s))
- [[javascriptallonge-gathering]] - shared statements: Gathering shares source evidence from Recipes with Basic Functions / Left-Variadic Functions: ECMAScript 2015 only permits gathering parameters from the end of the parameter list. Not the beginning. What to do? (1 shared statement(s))

## Source

- [[javascriptallonge]]
