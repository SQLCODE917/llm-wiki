---
page_id: javascriptallonge-bound
page_kind: concept
summary: Bound: 4 statement(s) and 9 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-29
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-bound@a69b9f8c1cd496ac2e603dd99b9a3b99
---

# Bound

What [[javascriptallonge]] covers about bound:

## Statements

### And also: / That Constant Coffee Craving / const

- Notice calc(d) ? This underscores what we've said: if we have an expression that evaluates to a function, we apply it with () . A name that's bound to a function is a valid expression evaluating to a function. 30 _(javascriptallonge.pdf (source-range-7239e085-00432))_

### And also: / That Constant Coffee Craving / are consts also from a shadowy planet?

- We just saw that values bound with const use lexical scope, just like values bound with parameters. They are looked up in the environment where they are declared. And we know that functions create environments. Parameters are declared when we create functions, so it makes sense that parameters are bound to environments created when we invoke functions. _(javascriptallonge.pdf (source-range-7239e085-00464))_

### And also: / Naming Functions / the function keyword

- So 'actualName' isn't bound in the environment where we use the named function expression. Is it bound anywhere else? Yes it is. Here's a function that determines whether a positive integer is even or not. We'll use it in an IIFE so that we don't have to bind it to a name with const : _(javascriptallonge.pdf (source-range-7239e085-00531))_

### And also: / Naming Functions / function declarations

- We haven't actually bound a function to the name fizzbuzz before we try to use it, so we get an error. But a function declaration works differently: _(javascriptallonge.pdf (source-range-7239e085-00543))_


## Technical atoms

### Technical frame 1: And also: / That Constant Coffee Craving / are consts also from a shadowy planet?

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00489))_

> Again, confusing. Typically, we want to bind our names as close to where we need them as possible. This design rule is called the Principle of Least Privilege 32 , and it has both quality and security implications. Being able to bind a name inside of a block means that if the name is only needed in the block, we are not 'leaking' its binding to other parts of the code that do not need to interact with it.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00482))_

```
if (true) {
// an immediately invoked block statement (IIBS)
}
Let’s try it:
((diameter) => {
const PI = 3;
if (true) {
const PI = 3.14159265;
return diameter * PI;
}
})(2)
//=> 6.2831853
((diameter) => {
const PI = 3.14159265;
if (true) {
const PI = 3;
}
return diameter * PI;
```

### Technical frame 2: And also: / That Constant Coffee Craving / are consts also from a shadowy planet?

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00489))_

> Again, confusing. Typically, we want to bind our names as close to where we need them as possible. This design rule is called the Principle of Least Privilege 32 , and it has both quality and security implications. Being able to bind a name inside of a block means that if the name is only needed in the block, we are not 'leaking' its binding to other parts of the code that do not need to interact with it.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00483))_

```
})(2)
//=> 6.2831853
```

### Technical frame 3: And also: / That Constant Coffee Craving / are consts also from a shadowy planet?

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00489))_

> Again, confusing. Typically, we want to bind our names as close to where we need them as possible. This design rule is called the Principle of Least Privilege 32 , and it has both quality and security implications. Being able to bind a name inside of a block means that if the name is only needed in the block, we are not 'leaking' its binding to other parts of the code that do not need to interact with it.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00486))_

```
((diameter) => {
const PI = 3.14159265;
if (true) {
const PI = 3;
}
return diameter * PI;
})(2)
//=> would return 6 if const had function scope
```

### Technical frame 4: And also: / That Constant Coffee Craving / are consts also from a shadowy planet?

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00489))_

> Again, confusing. Typically, we want to bind our names as close to where we need them as possible. This design rule is called the Principle of Least Privilege 32 , and it has both quality and security implications. Being able to bind a name inside of a block means that if the name is only needed in the block, we are not 'leaking' its binding to other parts of the code that do not need to interact with it.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00487))_

> If const always bound its value to the name defined in the function's environment, placing a const statement inside of a block would merely rebind the existing name, overwriting its old contents.

### Technical frame 5: And also: / That Constant Coffee Craving / are consts also from a shadowy planet?

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00489))_

> Again, confusing. Typically, we want to bind our names as close to where we need them as possible. This design rule is called the Principle of Least Privilege 32 , and it has both quality and security implications. Being able to bind a name inside of a block means that if the name is only needed in the block, we are not 'leaking' its binding to other parts of the code that do not need to interact with it.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00488))_

```
((diameter) => {
if (true) {
const PI = 3.14159265;
}
return diameter * PI;
})(2)
//=> would return 6.2831853 if const had function scope
```

### Technical frame 6: And also: / Naming Functions / the function keyword

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00533))_

> Clearly, the name even is bound to the function within the function's body . Is it bound to the function outside of the function's body?

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00532))_

```
(function even (n) {
if (n === 0) {
return true
}
else return !even(n - 1)
})(5)
//=> false
(function even (n) {
if (n === 0) {
return true
}
else return !even(n - 1)
})(2)
//=> true
```

### Technical frame 7: And also: / Naming Functions / the function keyword

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00535))_

> even is bound within the function itself, but not outside it. This is useful for making recursive functions as we see above, and it speaks to the principle of least privilege: If you don't need to name it anywhere else, you needn't.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00534))_

```
even
//=> Can't find variable: even
```

### Technical frame 8: And also: / Naming Functions / function declarations

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00546))_

> The definition of the fizzbuzz is 'hoisted' to the top of its enclosing scope (an IIFE in this case). This behaviour is intentional on the part of JavaScript's design to facilitate a certain style of programming where you put the main logic up front, and the 'helper functions' at the bottom. It is not necessary to declare functions in this way in JavaScript, but understanding the syntax and its behaviour (especially the way it differs from const ) is essential for working with production code.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00544))_

```
(function () {
return fizzbuzz();
function fizzbuzz () {
return "Fizz" + "Buzz";
}
})()
//=> 'FizzBuzz'
Although fizzbuzz is declared later in the function, JavaScript behaves as if we’d written:
(function () {
const fizzbuzz = function fizzbuzz () {
```

### Technical frame 9: And also: / Naming Functions / function declarations

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00546))_

> The definition of the fizzbuzz is 'hoisted' to the top of its enclosing scope (an IIFE in this case). This behaviour is intentional on the part of JavaScript's design to facilitate a certain style of programming where you put the main logic up front, and the 'helper functions' at the bottom. It is not necessary to declare functions in this way in JavaScript, but understanding the syntax and its behaviour (especially the way it differs from const ) is essential for working with production code.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00545))_

```
const fizzbuzz = function fizzbuzz ()
return "Fizz" + "Buzz";
}
return fizzbuzz();
})()
```


## Related pages

- [[javascriptallonge-function]] - shared statements and technical atoms: Function shares source evidence from And also: / That Constant Coffee Craving / const: Notice calc(d) ? This underscores what we've said: if we have an expression that evaluates to a function, we apply it with () . A name that's bound to a function is ... [truncated]; Function shares technical record from And also: / That Constant Coffee Craving / are consts also from a shadowy planet?: if (true) { // an immediately invoked block statement (IIBS) } Let’s try it: ((diameter) => { const PI = 3; if (true) { const PI = 3.14159265; return diameter * PI; ... [truncated] (2 shared statement(s), 9 shared atom(s))
- [[javascriptallonge-environment]] - shared statements and technical atoms: Environment shares source evidence from And also: / Naming Functions / the function keyword: So 'actualName' isn't bound in the environment where we use the named function expression. Is it bound anywhere else? Yes it is. Here's a function that determines wh ... [truncated]; Environment shares technical record from And also: / That Constant Coffee Craving / are consts also from a shadowy planet?: ((diameter) => { const PI = 3.14159265; if (true) { const PI = 3; } return diameter * PI; })(2) //=> would return 6 if const had function scope (1 shared statement(s), 4 shared atom(s))
- [[javascriptallonge-function-keyword]] - shared statements and technical atoms: the function keyword shares source evidence from And also: / Naming Functions / the function keyword: So 'actualName' isn't bound in the environment where we use the named function expression. Is it bound anywhere else? Yes it is. Here's a function that determines wh ... [truncated]; the function keyword shares technical record from And also: / Naming Functions / the function keyword: (function even (n) { if (n === 0) { return true } else return !even(n - 1) })(5) //=> false (function even (n) { if (n === 0) { return true } else return !even(n - 1 ... [truncated] (1 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-value]] - shared statements and technical atoms: Value shares source evidence from And also: / That Constant Coffee Craving / are consts also from a shadowy planet?: We just saw that values bound with const use lexical scope, just like values bound with parameters. They are looked up in the environment where they are declared. An ... [truncated]; Value shares technical record from And also: / That Constant Coffee Craving / are consts also from a shadowy planet?: ((diameter) => { const PI = 3.14159265; if (true) { const PI = 3; } return diameter * PI; })(2) //=> would return 6 if const had function scope (1 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-statement]] - shared technical atoms: Statement shares technical record from And also: / That Constant Coffee Craving / are consts also from a shadowy planet?: if (true) { // an immediately invoked block statement (IIBS) } Let’s try it: ((diameter) => { const PI = 3; if (true) { const PI = 3.14159265; return diameter * PI; ... [truncated] (4 shared atom(s))
- [[javascriptallonge-bind]] - shared technical atoms: Bind shares technical record from And also: / Naming Functions / the function keyword: (function even (n) { if (n === 0) { return true } else return !even(n - 1) })(5) //=> false (function even (n) { if (n === 0) { return true } else return !even(n - 1 ... [truncated] (2 shared atom(s))
- [[javascriptallonge-declaration]] - shared technical atoms: Declaration shares technical record from And also: / Naming Functions / function declarations: (function () { return fizzbuzz(); function fizzbuzz () { return "Fizz" + "Buzz"; } })() //=> 'FizzBuzz' Although fizzbuzz is declared later in the function, JavaScri ... [truncated] (2 shared atom(s))
- [[javascriptallonge-expression]] - shared technical atoms: Expression shares technical record from And also: / Naming Functions / the function keyword: (function even (n) { if (n === 0) { return true } else return !even(n - 1) })(5) //=> false (function even (n) { if (n === 0) { return true } else return !even(n - 1 ... [truncated] (2 shared atom(s))
- [[javascriptallonge-parameter]] - shared technical atoms: Parameter shares technical record from And also: / That Constant Coffee Craving / are consts also from a shadowy planet?: if (true) { // an immediately invoked block statement (IIBS) } Let’s try it: ((diameter) => { const PI = 3; if (true) { const PI = 3.14159265; return diameter * PI; ... [truncated] (2 shared atom(s))
- [[javascriptallonge-seen]] - shared technical atoms: Seen shares technical record from And also: / That Constant Coffee Craving / are consts also from a shadowy planet?: if (true) { // an immediately invoked block statement (IIBS) } Let’s try it: ((diameter) => { const PI = 3; if (true) { const PI = 3.14159265; return diameter * PI; ... [truncated] (2 shared atom(s))

## Source

- [[javascriptallonge]]
