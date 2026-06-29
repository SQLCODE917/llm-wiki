---
page_id: javascriptallonge-section-recipes-with-basic-functions-left-variadic-functions-d00f2bc0
page_kind: source
summary: Recipes with Basic Functions / Left-Variadic Functions: 29 source-backed entries and 13 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-29
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-recipes-with-basic-functions-left-variadic-functions-d00f2bc0@89420a2218c19e49994eb278f66ba80c
---

# Recipes with Basic Functions / Left-Variadic Functions

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-recipes-with-basic-functions-c9137465]] - broader source section: Recipes with Basic Functions
- [[javascriptallonge-section-recipes-with-basic-functions-left-variadic-functions-a-history-lesson-7dceb2fe]] - narrower source section: Recipes with Basic Functions / Left-Variadic Functions / a history lesson
- [[javascriptallonge-section-recipes-with-basic-functions-left-variadic-functions-overcoming-limitations-96b730f4]] - narrower source section: Recipes with Basic Functions / Left-Variadic Functions / overcoming limitations
- [[javascriptallonge-section-recipes-with-basic-functions-left-variadic-functions-left-variadic-destructuring-81ee3116]] - narrower source section: Recipes with Basic Functions / Left-Variadic Functions / left-variadic destructuring

## Statements

- A variadic function is a function that is designed to accept a variable number of arguments. 52 In JavaScript, you can make a variadic function by gathering parameters. For example: _(javascriptallonge.pdf (source-range-7239e085-00717))_
- This can be useful when writing certain kinds of destructuring algorithms. For example, we might want to have a function that builds some kind of team record. It accepts a coach, a captain, and an arbitrary number of players. Easy in ECMAScript 2015: _(javascriptallonge.pdf (source-range-7239e085-00719))_
- 52 English is about as inconsistent as JavaScript: Functions with a fixed number of arguments can be unary, binary, ternary, and so forth. But can they be 'variary?' No! They have to be 'variadic.' _(javascriptallonge.pdf (source-range-7239e085-00721))_
- ECMAScript 2015 only permits gathering parameters from the end of the parameter list. Not the beginning. What to do? _(javascriptallonge.pdf (source-range-7239e085-00723))_
- For example, we might want to have a function that builds some kind of team record. _(javascriptallonge.pdf (source-range-7239e085-00719))_
- ECMAScript 2015 only permits gathering parameters from the end of the parameter list. _(javascriptallonge.pdf (source-range-7239e085-00723))_

## Statements by subsection

### Recipes with Basic Functions / Left-Variadic Functions / a history lesson

- In 'Ye Olde Days,' 53 JavaScript could not gather parameters, and we had to either do backflips with arguments and .slice , or we wrote ourselves a variadic decorator that could gather arguments into the last declared parameter. Here it is in all of its ECMAScript-5 glory: _(javascriptallonge.pdf (source-range-7239e085-00725))_
- This is a right-variadic function , meaning that it has one or more fixed arguments, and the rest are gathered into the rightmost argument. _(javascriptallonge.pdf (source-range-7239e085-00731))_

### Recipes with Basic Functions / Left-Variadic Functions / overcoming limitations

- That's a left-variadic function . All left-variadic functions have one or more fixed arguments, and the rest are gathered into the leftmost argument. JavaScript doesn't do this. But if we wanted to write left-variadic functions, could we make ourselves a leftVariadic decorator to turn a function with one or more arguments into a left-variadic function? _(javascriptallonge.pdf (source-range-7239e085-00735))_
- We sure can, by using the techniques from rightVariadic . Mind you, we can take advantage of modern JavaScript to simplify the code: _(javascriptallonge.pdf (source-range-7239e085-00736))_
- Our leftVariadic function is a decorator that turns any function into a function that gathers parameters from the left , instead of from the right. _(javascriptallonge.pdf (source-range-7239e085-00739))_

### Recipes with Basic Functions / Left-Variadic Functions / left-variadic destructuring

- Gathering arguments for functions is one of the ways JavaScript can destructure arrays. Another way is when assigning variables, like this: _(javascriptallonge.pdf (source-range-7239e085-00741))_
- But we can write our own left-gathering function utility using the same principles without all the tedium: _(javascriptallonge.pdf (source-range-7239e085-00747))_
- With leftGather , we have to supply the length of the array we wish to use as the result, and it gathers excess arguments into it from the left, just like leftVariadic gathers excess parameters for a function. _(javascriptallonge.pdf (source-range-7239e085-00749))_

## Technical atoms

### Technical frame 1: Recipes with Basic Functions / Left-Variadic Functions

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00719))_

> This can be useful when writing certain kinds of destructuring algorithms. For example, we might want to have a function that builds some kind of team record. It accepts a coach, a captain, and an arbitrary number of players. Easy in ECMAScript 2015:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00718))_

```
const abccc = (a, b, ...c) => {
console.log(a);
console.log(b);
console.log(c);
};
abccc(1, 2, 3, 4, 5)
1
2
[3,4,5]
```

### Technical frame 2: Recipes with Basic Functions / Left-Variadic Functions

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00721))_

> 52 English is about as inconsistent as JavaScript: Functions with a fixed number of arguments can be unary, binary, ternary, and so forth. But can they be 'variary?' No! They have to be 'variadic.'

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00720))_

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

### Technical frame 3: Recipes with Basic Functions / Left-Variadic Functions

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00723))_

> ECMAScript 2015 only permits gathering parameters from the end of the parameter list. Not the beginning. What to do?

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00722))_

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

### Technical frame 4: Recipes with Basic Functions / Left-Variadic Functions / a history lesson

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00731))_

> This is a right-variadic function , meaning that it has one or more fixed arguments, and the rest are gathered into the rightmost argument.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00726))_

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

### Technical frame 5: Recipes with Basic Functions / Left-Variadic Functions / a history lesson

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00731))_

> This is a right-variadic function , meaning that it has one or more fixed arguments, and the rest are gathered into the rightmost argument.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00729))_

```
var firstAndButFirst = rightVariadic(
function test (first, butFirst) {
return [first, butFirst]
});
We now simply write:
const firstAndButFirst = (first, ...butFirst)
[first, butFirst];
```

### Technical frame 6: Recipes with Basic Functions / Left-Variadic Functions / a history lesson

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00731))_

> This is a right-variadic function , meaning that it has one or more fixed arguments, and the rest are gathered into the rightmost argument.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00730))_

```
=>
```

### Technical frame 7: Recipes with Basic Functions / Left-Variadic Functions / overcoming limitations

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00735))_

> That's a left-variadic function . All left-variadic functions have one or more fixed arguments, and the rest are gathered into the leftmost argument. JavaScript doesn't do this. But if we wanted to write left-variadic functions, could we make ourselves a leftVariadic decorator to turn a function with one or more arguments into a left-variadic function?

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00734))_

```
const butLastAndLast = (...butLast, last) =>
[butLast, last];
```

### Technical frame 8: Recipes with Basic Functions / Left-Variadic Functions / overcoming limitations

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00739))_

> Our leftVariadic function is a decorator that turns any function into a function that gathers parameters from the left , instead of from the right.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00737))_

```
const leftVariadic = (fn) => {
if (fn.length < 1) {
return fn;
}
else {
return function (...args) {
const gathered = args.slice(0, args.length - fn.length + 1),
spread
= args.slice(args.length - fn.length + 1);
return fn.apply(
this, [gathered].concat(spread)
```

### Technical frame 9: Recipes with Basic Functions / Left-Variadic Functions / overcoming limitations

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00739))_

> Our leftVariadic function is a decorator that turns any function into a function that gathers parameters from the left , instead of from the right.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00738))_

```
);
}
}
};
const butLastAndLast = leftVariadic((butLast, last) => [butLast, last]);
butLastAndLast('why', 'hello', 'there', 'little', 'droid')
//=> [["why","hello","there","little"],"droid"]
```

### Technical frame 10: Recipes with Basic Functions / Left-Variadic Functions / left-variadic destructuring

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00747))_

> But we can write our own left-gathering function utility using the same principles without all the tedium:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00742))_

```
const [first, ...butFirst] = ['why', 'hello', 'there', 'little', 'droid'];
first
//=> 'why'
butFirst
//=> ["hello","there","little","droid"]
```

### Technical frame 11: Recipes with Basic Functions / Left-Variadic Functions / left-variadic destructuring

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00747))_

> But we can write our own left-gathering function utility using the same principles without all the tedium:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00744))_

```
const [...butLast, last] = ['why', 'hello', 'there', 'little', 'droid'];
//=> Unexpected token
```

### Technical frame 12: Recipes with Basic Functions / Left-Variadic Functions / left-variadic destructuring

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00747))_

> But we can write our own left-gathering function utility using the same principles without all the tedium:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00746))_

```
const [butLast, last] = leftVariadic((butLast, last) => [butLast, last])(...['wh\
y', 'hello', 'there', 'little', 'droid']);
butLast
//=> ['why', 'hello', 'there', 'little']
last
//=> 'droid'
```

### Technical frame 13: Recipes with Basic Functions / Left-Variadic Functions / left-variadic destructuring

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00749))_

> With leftGather , we have to supply the length of the array we wish to use as the result, and it gathers excess arguments into it from the left, just like leftVariadic gathers excess parameters for a function.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00748))_

```
const leftGather = (outputArrayLength) => {
return function (inputArray) {
return [inputArray.slice(0, inputArray.length - outputArrayLength + 1)].conc\
at(
inputArray.slice(inputArray.length - outputArrayLength + 1)
)
}
};
const [butLast, last] = leftGather(2)(['why', 'hello', 'there', 'little', 'droid\
']);
butLast
//=> ['why', 'hello', 'there', 'little']
last
//=> 'droid'
```
