---
page_id: javascriptallonge-environment
page_kind: concept
summary: Environment: 9 statement(s) and 8 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-29
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-environment@ae9b8e934682808144b55cfea7acf5e3
---

# Environment

What [[javascriptallonge]] covers about environment:

## Statements

### And also: / Ah. I'd Like to Have an Argument, Please. 22 / variables and bindings

- Every time a function is invoked ('invoked' means 'applied to zero or more arguments'), a new environment is created. An environment is a (possibly empty) dictionary that maps variables to values by name. The x in the expression that we call a 'variable' is itself an expression that is evaluated by looking up the value in the environment. _(javascriptallonge.pdf (source-range-7239e085-00303))_

- When we talk about environments, we'll use an unsurprising syntax 25 for showing their bindings: {x: 2, ...} . meaning, that the environment is a dictionary, and that the value 2 is bound to the name x , and that there might be other stuff in that dictionary we aren't discussing right now. _(javascriptallonge.pdf (source-range-7239e085-00318))_

### And also: / Ah. I'd Like to Have an Argument, Please. 22 / call by sharing

- Whatabout reference types? JavaScript does not place copies of reference values in any environment. JavaScript places references to reference types in environments, and when the value needs to be used, JavaScript uses the reference to obtain the original. _(javascriptallonge.pdf (source-range-7239e085-00324))_

### And also: / That Constant Coffee Craving / are consts also from a shadowy planet?

- We can test this by creating another conflict. But instead of binding two different variables to the same name in two different places, we'll bind two different values to the same name, but one environment will be completely enclosed by the other. _(javascriptallonge.pdf (source-range-7239e085-00466))_

### And also: / Naming Functions

- It doesn't name the function 'repeat' for the same reason that const answer = 42 doesn't name the number 42 . This syntax binds an anonymous function to a name in an environment, but the function itself remains anonymous. _(javascriptallonge.pdf (source-range-7239e085-00501))_

### And also: / Naming Functions / the function keyword

- So 'actualName' isn't bound in the environment where we use the named function expression. Is it bound anywhere else? Yes it is. Here's a function that determines whether a positive integer is even or not. We'll use it in an IIFE so that we don't have to bind it to a name with const : _(javascriptallonge.pdf (source-range-7239e085-00531))_

### And also: / Naming Functions / function declarations

- In that it binds a name in the environment to a named function. However, there are two important differences. First, function declarations are hoisted to the top of the function in which they occur. _(javascriptallonge.pdf (source-range-7239e085-00540))_

### And also: / Naming Functions / function declaration caveats 34

- Function declarations are formally only supposed to be made at what we might call the 'top level' of a function. Although some JavaScript environments permit the following code, this example is technically illegal and definitely a bad idea: _(javascriptallonge.pdf (source-range-7239e085-00548))_

### Composing and Decomposing Data / Garbage, Garbage Everywhere

- The array we had in prepend is no longer used. In GC environments, it is marked as no longer being used, and eventually the garbage collector recycles the memory it is using. Lather, rinse, repeat: Ever time we call mapWith , we're creating a new array, copying all the elements from prepend into the new array, and then we no longer use prepend . _(javascriptallonge.pdf (source-range-7239e085-01022))_


## Technical atoms

### Technical frame 1: And also: / Ah. I'd Like to Have an Argument, Please. 22 / variables and bindings

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00314))_

> The value '2' is bound to the name 'x' in the environment.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00306))_

```
((x) => x)(2)
//=> 2
```

### Technical frame 2: And also: / That Constant Coffee Craving / are consts also from a shadowy planet?

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00475))_

> Now we bind 3 to PI in an otherwise empty IIFE inside of our IIFE that binds 3.14159265 to PI . Does that binding 'overwrite' the outer one? Will our function return 6 or 6.2831853 ? This is a book, you've already scanned ahead, so you know that the answer is no , the inner binding does not overwrite the outer binding:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00474))_

```
((PI) => {
((PI) => {})(3);
return (diameter) => diameter * PI;
})(3.14159265)
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

### Technical frame 5: And also: / Naming Functions

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00501))_

> It doesn't name the function 'repeat' for the same reason that const answer = 42 doesn't name the number 42 . This syntax binds an anonymous function to a name in an environment, but the function itself remains anonymous.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00500))_

```
const repeat = (str) => str + str
```

### Technical frame 6: And also: / Naming Functions / the function keyword

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00531))_

> So 'actualName' isn't bound in the environment where we use the named function expression. Is it bound anywhere else? Yes it is. Here's a function that determines whether a positive integer is even or not. We'll use it in an IIFE so that we don't have to bind it to a name with const :

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00530))_

```
const bindingName = function actualName () {
//...
};
bindingName
//=> [Function: actualName]
actualName
//=> ReferenceError: actualName is not defined
```

### Technical frame 7: And also: / Naming Functions / the function keyword

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

### Technical frame 8: And also: / Naming Functions / the function keyword

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00535))_

> even is bound within the function itself, but not outside it. This is useful for making recursive functions as we see above, and it speaks to the principle of least privilege: If you don't need to name it anywhere else, you needn't.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00534))_

```
even
//=> Can't find variable: even
```


## Related pages

- [[javascriptallonge-function]] - shared statements and technical atoms: Function shares source evidence from And also: / Naming Functions: It doesn't name the function 'repeat' for the same reason that const answer = 42 doesn't name the number 42 . This syntax binds an anonymous function to a name in an ... [truncated]; Function shares technical record from And also: / Ah. I'd Like to Have an Argument, Please. 22 / variables and bindings: ((x) => x)(2) //=> 2 (1 shared statement(s), 8 shared atom(s))
- [[javascriptallonge-bind]] - shared statements and technical atoms: Bind shares source evidence from And also: / That Constant Coffee Craving / are consts also from a shadowy planet?: We can test this by creating another conflict. But instead of binding two different variables to the same name in two different places, we'll bind two different valu ... [truncated]; Bind shares technical record from And also: / That Constant Coffee Craving / are consts also from a shadowy planet?: ((PI) => { ((PI) => {})(3); return (diameter) => diameter * PI; })(3.14159265) (3 shared statement(s), 4 shared atom(s))
- [[javascriptallonge-bound]] - shared statements and technical atoms: Bound shares source evidence from And also: / Naming Functions / the function keyword: So 'actualName' isn't bound in the environment where we use the named function expression. Is it bound anywhere else? Yes it is. Here's a function that determines wh ... [truncated]; Bound shares technical record from And also: / That Constant Coffee Craving / are consts also from a shadowy planet?: ((diameter) => { const PI = 3.14159265; if (true) { const PI = 3; } return diameter * PI; })(2) //=> would return 6 if const had function scope (1 shared statement(s), 4 shared atom(s))
- [[javascriptallonge-value]] - shared statements and technical atoms: Value shares source evidence from And also: / Ah. I'd Like to Have an Argument, Please. 22 / call by sharing: Whatabout reference types? JavaScript does not place copies of reference values in any environment. JavaScript places references to reference types in environments, ... [truncated]; Value shares technical record from And also: / Ah. I'd Like to Have an Argument, Please. 22 / variables and bindings: ((x) => x)(2) //=> 2 (2 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-function-keyword]] - shared statements and technical atoms: the function keyword shares source evidence from And also: / Naming Functions / the function keyword: So 'actualName' isn't bound in the environment where we use the named function expression. Is it bound anywhere else? Yes it is. Here's a function that determines wh ... [truncated]; the function keyword shares technical record from And also: / Naming Functions / the function keyword: const bindingName = function actualName () { //... }; bindingName //=> [Function: actualName] actualName //=> ReferenceError: actualName is not defined (1 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-binding]] - shared statements and technical atoms: Binding shares source evidence from And also: / That Constant Coffee Craving / are consts also from a shadowy planet?: We can test this by creating another conflict. But instead of binding two different variables to the same name in two different places, we'll bind two different valu ... [truncated]; Binding shares technical record from And also: / That Constant Coffee Craving / are consts also from a shadowy planet?: ((PI) => { ((PI) => {})(3); return (diameter) => diameter * PI; })(3.14159265) (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-different]] - shared statements and technical atoms: Different shares source evidence from And also: / That Constant Coffee Craving / are consts also from a shadowy planet?: We can test this by creating another conflict. But instead of binding two different variables to the same name in two different places, we'll bind two different valu ... [truncated]; Different shares technical record from And also: / That Constant Coffee Craving / are consts also from a shadowy planet?: ((PI) => { ((PI) => {})(3); return (diameter) => diameter * PI; })(3.14159265) (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-expression]] - shared technical atoms: Expression shares technical record from And also: / That Constant Coffee Craving / are consts also from a shadowy planet?: ((PI) => { ((PI) => {})(3); return (diameter) => diameter * PI; })(3.14159265) (3 shared atom(s))
- [[javascriptallonge-statement]] - shared technical atoms: Statement shares technical record from And also: / That Constant Coffee Craving / are consts also from a shadowy planet?: ((diameter) => { const PI = 3.14159265; if (true) { const PI = 3; } return diameter * PI; })(2) //=> would return 6 if const had function scope (2 shared atom(s))
- [[javascriptallonge-argument]] - shared technical atoms: Argument shares technical record from And also: / Ah. I'd Like to Have an Argument, Please. 22 / variables and bindings: ((x) => x)(2) //=> 2 (1 shared atom(s))
- [[javascriptallonge-javascript]] - shared statements: Javascript shares source evidence from And also: / Ah. I'd Like to Have an Argument, Please. 22 / call by sharing: Whatabout reference types? JavaScript does not place copies of reference values in any environment. JavaScript places references to reference types in environments, ... [truncated] (2 shared statement(s))
- [[javascriptallonge-code]] - shared statements: Code shares source evidence from And also: / Naming Functions / function declaration caveats 34: Function declarations are formally only supposed to be made at what we might call the 'top level' of a function. Although some JavaScript environments permit the fol ... [truncated] (1 shared statement(s))
- [[javascriptallonge-follow]] - shared statements: Follow shares source evidence from And also: / Naming Functions / function declaration caveats 34: Function declarations are formally only supposed to be made at what we might call the 'top level' of a function. Although some JavaScript environments permit the fol ... [truncated] (1 shared statement(s))
- [[javascriptallonge-instead]] - shared statements: Instead shares source evidence from And also: / That Constant Coffee Craving / are consts also from a shadowy planet?: We can test this by creating another conflict. But instead of binding two different variables to the same name in two different places, we'll bind two different valu ... [truncated] (1 shared statement(s))
- [[javascriptallonge-reference]] - shared statements: Reference shares source evidence from And also: / Ah. I'd Like to Have an Argument, Please. 22 / call by sharing: Whatabout reference types? JavaScript does not place copies of reference values in any environment. JavaScript places references to reference types in environments, ... [truncated] (1 shared statement(s))
- [[javascriptallonge-type]] - shared statements: Type shares source evidence from And also: / Ah. I'd Like to Have an Argument, Please. 22 / call by sharing: Whatabout reference types? JavaScript does not place copies of reference values in any environment. JavaScript places references to reference types in environments, ... [truncated] (1 shared statement(s))
- [[javascriptallonge-variable]] - shared statements: Variable shares source evidence from And also: / Ah. I'd Like to Have an Argument, Please. 22 / variables and bindings: Every time a function is invoked ('invoked' means 'applied to zero or more arguments'), a new environment is created. An environment is a (possibly empty) dictionary ... [truncated] (1 shared statement(s))
- [[javascriptallonge-section-and-also-closures-and-scope-it-s-always-the-environment-47a785c5]] - source section: And also: / Closures and Scope / it's always the environment shares source evidence from And also: / Closures and Scope / it's always the environment: To understand how closures are evaluated, we need to revisit environments. As we've said before, all functions are associated with an environment. We also hand-waved ... [truncated]; And also: / Closures and Scope / it's always the environment shares technical record from And also: / Closures and Scope / it's always the environment: So whenever a function is applied to arguments, its environment always has a reference to its parent environment. (8 shared statement(s), 5 shared atom(s))

## Source

- [[javascriptallonge]]
