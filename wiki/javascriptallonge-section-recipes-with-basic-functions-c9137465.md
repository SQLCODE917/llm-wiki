---
page_id: javascriptallonge-section-recipes-with-basic-functions-c9137465
page_kind: source
summary: Recipes with Basic Functions: 84 source-backed entries and 37 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-29
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-recipes-with-basic-functions-c9137465@7a9ed0bcdce876cad3a2a163d6fa542d
---

# Recipes with Basic Functions

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-recipes-with-basic-functions-disclaimer-d5150889]] - narrower source section: Recipes with Basic Functions / Disclaimer
- [[javascriptallonge-section-recipes-with-basic-functions-partial-application-583028a8]] - narrower source section: Recipes with Basic Functions / Partial Application
- [[javascriptallonge-section-recipes-with-basic-functions-unary-5deba4e9]] - narrower source section: Recipes with Basic Functions / Unary
- [[javascriptallonge-section-recipes-with-basic-functions-tap-904019d9]] - narrower source section: Recipes with Basic Functions / Tap
- [[javascriptallonge-section-recipes-with-basic-functions-maybe-bddfd1b7]] - narrower source section: Recipes with Basic Functions / Maybe
- [[javascriptallonge-section-recipes-with-basic-functions-once-99d6b11d]] - narrower source section: Recipes with Basic Functions / Once
- [[javascriptallonge-section-recipes-with-basic-functions-left-variadic-functions-d00f2bc0]] - narrower source section: Recipes with Basic Functions / Left-Variadic Functions

## Statements

- Before combining ingredients, begin with implements so clean, they gleam. _(javascriptallonge.pdf (source-range-7239e085-00654))_
- Having looked at basic pure functions and closures, we're going to see some practical recipes that focus on the premise of functions that return functions. _(javascriptallonge.pdf (source-range-7239e085-00655))_
- Before combining ingredients, begin with implements so clean, they gleam. _(javascriptallonge.pdf (source-range-7239e085-00654))_

## Statements by subsection

### Recipes with Basic Functions / Disclaimer

- The recipes are written for practicality, and their implementation may introduce JavaScript features that haven't been discussed in the text to this point, such as methods and/or prototypes. The overall use of each recipe will fit within the spirit of the language discussed so far, even if the implementations may not. _(javascriptallonge.pdf (source-range-7239e085-00657))_
- The recipes are written for practicality, and their implementation may introduce JavaScript features that haven't been discussed in the text to this point, such as methods and/or prototypes. _(javascriptallonge.pdf (source-range-7239e085-00657))_
- The overall use of each recipe will fit within the spirit of the language discussed so far, even if the implementations may not. _(javascriptallonge.pdf (source-range-7239e085-00657))_

### Recipes with Basic Functions / Partial Application

- These two recipes are for quickly and simply applying a single argument, either the leftmost or rightmost. 48 If you want to bind more than one argument, or you want to leave a 'hole' in the argument list, you will need to either use a generalized partial recipe, or you will need to repeatedly apply arguments. They are context-agnostic. _(javascriptallonge.pdf (source-range-7239e085-00660))_
- As noted above, our partial recipe allows us to create functions that are partial applications of functions that are context aware. We'd need a different recipe if we wish to create partial applications of object methods. _(javascriptallonge.pdf (source-range-7239e085-00662))_
- callFirst and callLast were inspired by Michael Fogus' Lemonad. Thanks! _(javascriptallonge.pdf (source-range-7239e085-00664))_
- We take it a step further, and can use gathering and spreading to allow for partial application with more than one argument: _(javascriptallonge.pdf (source-range-7239e085-00665))_

### Recipes with Basic Functions / Unary

- The most common use case is to fix a problem. JavaScript has a .map method for arrays, and many libraries offer a map function with the same semantics. Here it is in action: _(javascriptallonge.pdf (source-range-7239e085-00669))_
- If you pass in a function taking only one argument, it simply ignores the additional arguments. But some functions have optional second or even third arguments. For example: _(javascriptallonge.pdf (source-range-7239e085-00674))_
- This doesn't work because parseInt is defined as parseInt(string[, radix]) . It takes an optional radix argument. And when you call parseInt with map , the index is interpreted as a radix. Not good! What we want is to convert parseInt into a function taking only one argument. _(javascriptallonge.pdf (source-range-7239e085-00676))_
- This doesn't work because parseInt is defined as parseInt(string[, radix]) . _(javascriptallonge.pdf (source-range-7239e085-00676))_
- What we want is to convert parseInt into a function taking only one argument. _(javascriptallonge.pdf (source-range-7239e085-00676))_

### Recipes with Basic Functions / Tap

- It has some surprising applications. One is when you want to do something with a value for sideeffects, but keep the value around. Behold: _(javascriptallonge.pdf (source-range-7239e085-00685))_
- tap is a traditional name borrowed from various Unix shell commands. It takes a value and returns a function that always returns the value, but if you pass it a function, it executes the function for side-effects. Let's see it in action as a poor-man's debugger: _(javascriptallonge.pdf (source-range-7239e085-00687))_
- p.s. tap can do more than just act as a debugging aid. It's also useful for working with object and instance methods. _(javascriptallonge.pdf (source-range-7239e085-00693))_

### Recipes with Basic Functions / Maybe

- A common problem in programming is checking for null or undefined (hereafter called 'nothing,' while all other values including 0 , [] and false will be called 'something'). Languages like JavaScript do not strongly enforce the notion that a particular variable or particular property be something, so programs are often written to account for values that may be nothing. _(javascriptallonge.pdf (source-range-7239e085-00695))_
- This recipe concerns a pattern that is very common: A function fn takes a value as a parameter, and its behaviour by design is to do nothing if the parameter is nothing: _(javascriptallonge.pdf (source-range-7239e085-00696))_
- Alternately, the function may be intended to work with any value, but the code calling the function wishes to emulate the behaviour of doing nothing by design when given nothing: _(javascriptallonge.pdf (source-range-7239e085-00698))_
- Naturally, there's a function decorator recipe for that, borrowed from Haskell's maybe monad 50 , Ruby's andand 51 , and CoffeeScript's existential method invocation: _(javascriptallonge.pdf (source-range-7239e085-00700))_
- If some code ever tries to call model.setSomething with nothing, the operation will be skipped. _(javascriptallonge.pdf (source-range-7239e085-00708))_

### Recipes with Basic Functions / Once

- once is an extremely helpful combinator. It ensures that a function can only be called, well, once . Here's the recipe: _(javascriptallonge.pdf (source-range-7239e085-00710))_
- It ensures that a function can only be called, well, once . _(javascriptallonge.pdf (source-range-7239e085-00710))_

### Recipes with Basic Functions / Left-Variadic Functions

- A variadic function is a function that is designed to accept a variable number of arguments. 52 In JavaScript, you can make a variadic function by gathering parameters. For example: _(javascriptallonge.pdf (source-range-7239e085-00717))_
- This can be useful when writing certain kinds of destructuring algorithms. For example, we might want to have a function that builds some kind of team record. It accepts a coach, a captain, and an arbitrary number of players. Easy in ECMAScript 2015: _(javascriptallonge.pdf (source-range-7239e085-00719))_
- 52 English is about as inconsistent as JavaScript: Functions with a fixed number of arguments can be unary, binary, ternary, and so forth. But can they be 'variary?' No! They have to be 'variadic.' _(javascriptallonge.pdf (source-range-7239e085-00721))_
- ECMAScript 2015 only permits gathering parameters from the end of the parameter list. Not the beginning. What to do? _(javascriptallonge.pdf (source-range-7239e085-00723))_
- For example, we might want to have a function that builds some kind of team record. _(javascriptallonge.pdf (source-range-7239e085-00719))_
- ECMAScript 2015 only permits gathering parameters from the end of the parameter list. _(javascriptallonge.pdf (source-range-7239e085-00723))_

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

### Technical frame 1: Recipes with Basic Functions

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00654))_

> Before combining ingredients, begin with implements so clean, they gleam.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00653))_

> [Figure] (p.79)

### Technical frame 2: Recipes with Basic Functions / Partial Application

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00662))_

> As noted above, our partial recipe allows us to create functions that are partial applications of functions that are context aware. We'd need a different recipe if we wish to create partial applications of object methods.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00661))_

```
const callFirst = (fn, larg) =>
function (...rest) {
return fn.call(this, larg, ...rest);
}
const callLast = (fn, rarg) =>
function (...rest) {
return fn.call(this, ...rest, rarg);
}
const greet = (me, you) =>
`Hello, ${you}, my name is ${me}`;
const heliosSaysHello = callFirst(greet, 'Helios');
heliosSaysHello('Eartha')
//=> 'Hello, Eartha, my name is Helios'
const sayHelloToCeline = callLast(greet, 'Celine');
sayHelloToCeline('Eartha')
//=> 'Hello, Celine, my name is Eartha'
```

### Technical frame 3: Recipes with Basic Functions / Partial Application

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00665))_

> We take it a step further, and can use gathering and spreading to allow for partial application with more than one argument:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00666))_

```
const callLeft = (fn, ...args) =>
(...remainingArgs) =>
fn(...args, ...remainingArgs);
const callRight = (fn, ...args) =>
(...remainingArgs) =>
fn(...remainingArgs, ...args);
```

### Technical frame 4: Recipes with Basic Functions / Unary

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00674))_

> If you pass in a function taking only one argument, it simply ignores the additional arguments. But some functions have optional second or even third arguments. For example:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00670))_

```
['1', '2', '3'].map(parseFloat)
//=> [1, 2, 3]
```

### Technical frame 5: Recipes with Basic Functions / Unary

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00674))_

> If you pass in a function taking only one argument, it simply ignores the additional arguments. But some functions have optional second or even third arguments. For example:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00673))_

```
[1, 2, 3].map(function (element, index, arr) {
console.log({element: element, index: index, arr: arr})
})
//=> { element: 1, index: 0, arr: [ 1, 2, 3 ] }
//
{ element: 2, index: 1, arr: [ 1, 2, 3 ] }
//
{ element: 3, index: 2, arr: [ 1, 2, 3 ] }
```

### Technical frame 6: Recipes with Basic Functions / Unary

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00676))_

> This doesn't work because parseInt is defined as parseInt(string[, radix]) . It takes an optional radix argument. And when you call parseInt with map , the index is interpreted as a radix. Not good! What we want is to convert parseInt into a function taking only one argument.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00674))_

> If you pass in a function taking only one argument, it simply ignores the additional arguments.

### Technical frame 7: Recipes with Basic Functions / Unary

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00676))_

> This doesn't work because parseInt is defined as parseInt(string[, radix]) . It takes an optional radix argument. And when you call parseInt with map , the index is interpreted as a radix. Not good! What we want is to convert parseInt into a function taking only one argument.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00675))_

```
['1', '2', '3'].map(parseInt)
//=> [1, NaN, NaN]
```

### Technical frame 8: Recipes with Basic Functions / Unary

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00676))_

> This doesn't work because parseInt is defined as parseInt(string[, radix]) . It takes an optional radix argument. And when you call parseInt with map , the index is interpreted as a radix. Not good! What we want is to convert parseInt into a function taking only one argument.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00677))_

> Wecould write ['1', '2', '3'].map((s) => parseInt(s)) , or we could come up with a decorator to do the job for us:

### Technical frame 9: Recipes with Basic Functions / Unary

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00676))_

> This doesn't work because parseInt is defined as parseInt(string[, radix]) . It takes an optional radix argument. And when you call parseInt with map , the index is interpreted as a radix. Not good! What we want is to convert parseInt into a function taking only one argument.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00678))_

```
const unary = (fn) =>
fn.length === 1
? fn
: function (something) {
return fn.call(this, something)
}
```

### Technical frame 10: Recipes with Basic Functions / Unary

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00676))_

> This doesn't work because parseInt is defined as parseInt(string[, radix]) . It takes an optional radix argument. And when you call parseInt with map , the index is interpreted as a radix. Not good! What we want is to convert parseInt into a function taking only one argument.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00680))_

```
['1', '2', '3'].map(unary(parseInt))
//=> [1, 2, 3]
```

### Technical frame 11: Recipes with Basic Functions / Tap

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00685))_

> It has some surprising applications. One is when you want to do something with a value for sideeffects, but keep the value around. Behold:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00684))_

```
const K = (x) => (y) => x;
```

### Technical frame 12: Recipes with Basic Functions / Tap

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00687))_

> tap is a traditional name borrowed from various Unix shell commands. It takes a value and returns a function that always returns the value, but if you pass it a function, it executes the function for side-effects. Let's see it in action as a poor-man's debugger:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00686))_

```
const tap = (value) =>
(fn) => (
typeof(fn) === 'function' && fn(value),
value
)
```

### Technical frame 13: Recipes with Basic Functions / Tap

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00693))_

> p.s. tap can do more than just act as a debugging aid. It's also useful for working with object and instance methods.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00691))_

```
const tap = (value, fn) => {
const curried = (fn) => (
typeof(fn) === 'function' && fn(value),
value
);
return fn === undefined
? curried
: curried(fn);
}
Now we can write:
tap('espresso')((it) => {
console.log(`Our drink is '${it}'`)
});
//=> Our drink is 'espresso'
'espresso'
Or:
tap('espresso', (it) => {
console.log(`Our drink is '${it}'`)
});
//=> Our drink is 'espresso'
'espresso'
```

### Technical frame 14: Recipes with Basic Functions / Maybe

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00698))_

> Alternately, the function may be intended to work with any value, but the code calling the function wishes to emulate the behaviour of doing nothing by design when given nothing:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00697))_

```
const isSomething = (value) =>
value !== null && value !== void 0;
const checksForSomething = (value) => {
if (isSomething(value)) {
// function's true logic
}
}
```

### Technical frame 15: Recipes with Basic Functions / Maybe

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00700))_

> Naturally, there's a function decorator recipe for that, borrowed from Haskell's maybe monad 50 , Ruby's andand 51 , and CoffeeScript's existential method invocation:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00699))_

```
var something =
isSomething(value)
? doesntCheckForSomething(value)
: value;
```

### Technical frame 16: Recipes with Basic Functions / Maybe

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00708))_

> If some code ever tries to call model.setSomething with nothing, the operation will be skipped.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00701))_

```
const maybe = (fn) =>
function (...args) {
if (args.length === 0) {
return
}
else {
for (let arg of args) {
if (arg == null) return;
}
```

### Technical frame 17: Recipes with Basic Functions / Maybe

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00708))_

> If some code ever tries to call model.setSomething with nothing, the operation will be skipped.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00703))_

```
return fn.apply(this, args)
}
}
```

### Technical frame 18: Recipes with Basic Functions / Maybe

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00708))_

> If some code ever tries to call model.setSomething with nothing, the operation will be skipped.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00705))_

```
maybe((a, b, c) => a + b + c)(1, 2, 3)
//=> 6
maybe((a, b, c) => a + b + c)(1, null, 3)
//=> undefined
```

### Technical frame 19: Recipes with Basic Functions / Maybe

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00708))_

> If some code ever tries to call model.setSomething with nothing, the operation will be skipped.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00707))_

```
function Model () {};
Model.prototype.setSomething = maybe(function (value) {
this.something = value;
});
```

### Technical frame 20: Recipes with Basic Functions / Once

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00710))_

> once is an extremely helpful combinator. It ensures that a function can only be called, well, once . Here's the recipe:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00711))_

```
const once = (fn) => {
let done = false;
return function () {
return done ? void 0 : ((done = true), fn.apply(this, arguments))
}
}
```

### Technical frame 21: Recipes with Basic Functions / Once

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00710))_

> once is an extremely helpful combinator. It ensures that a function can only be called, well, once . Here's the recipe:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00713))_

```
const askedOnBlindDate = once(
() => "sure, why not?"
);
askedOnBlindDate()
//=> 'sure, why not?'
askedOnBlindDate()
//=> undefined
askedOnBlindDate()
//=> undefined
```

### Technical frame 22: Recipes with Basic Functions / Left-Variadic Functions

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

### Technical frame 23: Recipes with Basic Functions / Left-Variadic Functions

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

### Technical frame 24: Recipes with Basic Functions / Left-Variadic Functions

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

### Technical frame 25: Recipes with Basic Functions / Left-Variadic Functions / a history lesson

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

### Technical frame 26: Recipes with Basic Functions / Left-Variadic Functions / a history lesson

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

### Technical frame 27: Recipes with Basic Functions / Left-Variadic Functions / a history lesson

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00731))_

> This is a right-variadic function , meaning that it has one or more fixed arguments, and the rest are gathered into the rightmost argument.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00730))_

```
=>
```

### Technical frame 28: Recipes with Basic Functions / Left-Variadic Functions / overcoming limitations

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00735))_

> That's a left-variadic function . All left-variadic functions have one or more fixed arguments, and the rest are gathered into the leftmost argument. JavaScript doesn't do this. But if we wanted to write left-variadic functions, could we make ourselves a leftVariadic decorator to turn a function with one or more arguments into a left-variadic function?

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00734))_

```
const butLastAndLast = (...butLast, last) =>
[butLast, last];
```

### Technical frame 29: Recipes with Basic Functions / Left-Variadic Functions / overcoming limitations

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

### Technical frame 30: Recipes with Basic Functions / Left-Variadic Functions / overcoming limitations

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

### Technical frame 31: Recipes with Basic Functions / Left-Variadic Functions / left-variadic destructuring

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

### Technical frame 32: Recipes with Basic Functions / Left-Variadic Functions / left-variadic destructuring

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00747))_

> But we can write our own left-gathering function utility using the same principles without all the tedium:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00744))_

```
const [...butLast, last] = ['why', 'hello', 'there', 'little', 'droid'];
//=> Unexpected token
```

### Technical frame 33: Recipes with Basic Functions / Left-Variadic Functions / left-variadic destructuring

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

### Technical frame 34: Recipes with Basic Functions / Left-Variadic Functions / left-variadic destructuring

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

### Technical atom 35

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00659))_

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

### Technical atom 36

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00660))_

> These two recipes are for quickly and simply applying a single argument, either the leftmost or rightmost. 48 If you want to bind more than one argument, or you want to leave a 'hole' in the argument list, you will need to either use a generalized partial recipe, or you will need to repeatedly apply arguments. They are context-agnostic.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00663))_

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

### Technical atom 37

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00700))_

> Naturally, there's a function decorator recipe for that, borrowed from Haskell's maybe monad 50 , Ruby's andand 51 , and CoffeeScript's existential method invocation:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00702))_

| entry | content |
| --- | --- |
| 50 | https://en.wikipedia.org/wiki/Monad_(functional_programming)#The_Maybe_monad |
| 51 | https://github.com/raganwald/andand |

<details>
<summary>Raw table text</summary>

```
50 https://en.wikipedia.org/wiki/Monad_(functional_programming)#The_Maybe_monad
51 https://github.com/raganwald/andand
```

</details>
