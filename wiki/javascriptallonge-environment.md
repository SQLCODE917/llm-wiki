---
page_id: javascriptallonge-environment
page_kind: concept
summary: Environment: 10 statement(s) and 10 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-environment@5a460ee6747e500c78423ecf0cbe9a24
---

# Environment

What [[javascriptallonge]] covers about environment:

## Statements

- The variable x isn’t in (y) => ...’s immediate environment, but it is in its parent’s environment, so it evaluates to 1 and that’s what ((y) => x)(2) returns even though it ended up ignoring its own argument. _(javascriptallonge.pdf (source-range-83ecb080-00505))_
- An environment is a (possibly empty) dictionary that maps variables to values by name. _(javascriptallonge.pdf (source-range-83ecb080-00434))_
- meaning, that the environment is a dictionary, and that the value 2 is bound to the name x, and that there might be other stuff in that dictionary we aren’t discussing right now. _(javascriptallonge.pdf (source-range-83ecb080-00451))_
- JavaScript places _references_ to reference types in environments, and when the value needs to be used, JavaScript uses the reference to obtain the original. _(javascriptallonge.pdf (source-range-83ecb080-00460))_
- But instead of binding two different variables to the same name in two different places, we’ll bind two different values to the same name, but one environment will be completely enclosed by the other. _(javascriptallonge.pdf (source-range-83ecb080-00646))_
- This syntax binds an anonymous function to a name in an environment, but the function itself remains anonymous. _(javascriptallonge.pdf (source-range-83ecb080-00696))_
- So “actualName” isn’t bound in the environment where we use the named function expression. _(javascriptallonge.pdf (source-range-83ecb080-00733))_
- In that it binds a name in the environment to a named function. _(javascriptallonge.pdf (source-range-83ecb080-00750))_
- Although some JavaScript environments permit the following code, this example is technically illegal and definitely a bad idea: _(javascriptallonge.pdf (source-range-83ecb080-00764))_
- In GC environments, it is marked as no longer being used, and eventually the garbage collector recycles the memory it is using. _(javascriptallonge.pdf (source-range-83ecb080-01517))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00438))_

> How does the value get put in the environment? Well for arguments, that is very simple. When you apply the function to the arguments, an entry is placed in the dictionary for each argument. So when we write:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00439))_

> ((x) => x)(2) _//=> 2_

### Technical atom 2

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00503))_

> To understand how closures are evaluated, we need to revisit environments. As we’ve said before, all functions are associated with an environment. We also hand-waved something when describing our environment. Remember that we said the environment for ((x) => (y) => x)(1) is {x: 1, ...} and that the environment for ((y) => x)(2) is {y: 2, ...}? Let’s fill in the blanks!

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00504))_

> So whenever a function is applied to arguments, its environment always has a reference to its parent environment.

### Technical atom 3

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00655, source-range-83ecb080-00657))_

> And we can see that our diameter * PI expression uses the binding for PI in the closest parent environment. but one question: Did binding 3.14159265 to PI somehow change the binding in the “outer” environment? Let’s rewrite things slightly differently: Now we bind 3 to PI in an otherwise empty IIFE inside of our IIFE that binds 3.14159265 to PI. Does that binding “overwrite” the outer one? Will our function return 6 or 6.2831853? This is a book, you’ve already scanned ahead, so you know that the

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00656))_

> ((PI) => { ((PI) => {})(3); **return** (diameter) => diameter * PI; })(3.14159265)

### Technical atom 4

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00673, source-range-83ecb080-00676))_

> This is enormously important. Consider the alternative: What if const could be declared inside of a block, but it always bound the name in the function’s scope. In that case, we’d see things like this: If const always bound its value to the name defined in the function’s environment, placing a const statement inside of a block would merely rebind the existing name, overwriting its old contents. That would be super-confusing. And this code would “work:”

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00674))_

> ((diameter) => { **const** PI = 3.14159265;

### Technical atom 5

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00673, source-range-83ecb080-00676))_

> This is enormously important. Consider the alternative: What if const could be declared inside of a block, but it always bound the name in the function’s scope. In that case, we’d see things like this: If const always bound its value to the name defined in the function’s environment, placing a const statement inside of a block would merely rebind the existing name, overwriting its old contents. That would be super-confusing. And this code would “work:”

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00675))_

> **if** ( **true** ) { **const** PI = 3; } **return** diameter * PI; })(2) _//=> would return 6 if const had function scope_

### Technical atom 6

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00676))_

> If const always bound its value to the name defined in the function’s environment, placing a const statement inside of a block would merely rebind the existing name, overwriting its old contents. That would be super-confusing. And this code would “work:”

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00678))_

> **if** ( **true** ) { **const** PI = 3.14159265; } **return** diameter * PI; })(2) _//=> would return 6.2831853 if const had function scope_

### Technical atom 7

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00694, source-range-83ecb080-00696))_

> Let’s get right to it. This code does _not_ name a function: It doesn’t name the function “repeat” for the same reason that const answer = 42 doesn’t name the number 42. This syntax binds an anonymous function to a name in an environment, but the function itself remains anonymous.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00695))_

> **const** repeat = (str) => str + str

### Technical atom 8

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00729))_

> Now, the function’s actual name has no effect on the environment in which it is used. To whit:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00730))_

> **const** bindingName = **function** actualName () { _//..._

### Technical atom 9

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00729))_

> Now, the function’s actual name has no effect on the environment in which it is used. To whit:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00731))_

> }; bindingName _//=> [Function: actualName]_

### Technical atom 10

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00729))_

> Now, the function’s actual name has no effect on the environment in which it is used. To whit:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00732))_

> actualName _//=> ReferenceError: actualName is not defined_


## Related pages

- [[javascriptallonge-function]] - shared statements and technical atoms (1 shared statement(s), 10 shared atom(s))
- [[javascriptallonge-value]] - shared statements and technical atoms (2 shared statement(s), 4 shared atom(s))
- [[javascriptallonge-bind]] - shared statements and technical atoms (3 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-argument]] - shared technical atoms (1 shared atom(s))
- [[javascriptallonge-evaluate]] - shared technical atoms (1 shared atom(s))
- [[javascriptallonge-expression]] - shared technical atoms (1 shared atom(s))
- [[javascriptallonge-javascript]] - shared statements (2 shared statement(s))
- [[javascriptallonge-code]] - shared statements (1 shared statement(s))
- [[javascriptallonge-type]] - shared statements (1 shared statement(s))

## Source

- [[javascriptallonge]]
