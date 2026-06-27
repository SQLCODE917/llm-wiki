---
page_id: javascriptallonge-section-are-consts-also-from-a-shadowy-planet-4a9e1ee2
page_kind: source
summary: **are consts also from a shadowy planet?**: 32 source-backed entries and 10 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-are-consts-also-from-a-shadowy-planet-4a9e1ee2@0471a8561f1ebf379ef250e6214860c8
---

# **are consts also from a shadowy planet?**

From [[javascriptallonge]].

## Statements

- They are looked up in the environment where they are declared. _(javascriptallonge.pdf (source-range-83ecb080-00644))_
- Parameters are declared when we create functions, so it makes sense that parameters are bound to environments created when we invoke functions. _(javascriptallonge.pdf (source-range-83ecb080-00644))_
- We just saw that values bound with const use lexical scope, just like values bound with parameters. _(javascriptallonge.pdf (source-range-83ecb080-00644))_
- But const statements can appear inside blocks, and we saw that blocks can appear inside of other blocks, including function bodies. _(javascriptallonge.pdf (source-range-83ecb080-00645))_
- But const statements can appear inside blocks, and we saw that blocks can appear inside of other blocks, including function bodies. _(javascriptallonge.pdf (source-range-83ecb080-00645))_
- We can test this by creating another conflict. _(javascriptallonge.pdf (source-range-83ecb080-00646))_
- But instead of binding two different variables to the same name in two different places, we’ll bind two different values to the same name, but one environment will be completely enclosed by the other. _(javascriptallonge.pdf (source-range-83ecb080-00646))_
- And we can see that our diameter * PI expression uses the binding for PI in the closest parent environment. _(javascriptallonge.pdf (source-range-83ecb080-00655))_
- This is a book, you’ve already scanned ahead, so you know that the answer is **no** , the inner binding does not overwrite the outer binding: _(javascriptallonge.pdf (source-range-83ecb080-00657))_
- Now we bind 3 to PI in an otherwise empty IIFE inside of our IIFE that binds 3.14159265 to PI. _(javascriptallonge.pdf (source-range-83ecb080-00657))_
- It has effect inside its own scope, but does not affect the binding in the enclosing scope. _(javascriptallonge.pdf (source-range-83ecb080-00659))_
- It has effect inside its own scope, but does not affect the binding in the enclosing scope. _(javascriptallonge.pdf (source-range-83ecb080-00659))_
- We say that when we bind a variable using a parameter inside another binding, the inner binding _shadows_ the outer binding. _(javascriptallonge.pdf (source-range-83ecb080-00659))_
- Parameters are only bound when we invoke a function. _(javascriptallonge.pdf (source-range-83ecb080-00665))_
- But const statements can appear inside blocks. _(javascriptallonge.pdf (source-range-83ecb080-00665))_
- But const statements can appear inside blocks. _(javascriptallonge.pdf (source-range-83ecb080-00665))_
- Parameters are only bound when we invoke a function. _(javascriptallonge.pdf (source-range-83ecb080-00665))_
- We’ll need a gratuitous block. _(javascriptallonge.pdf (source-range-83ecb080-00666))_
- This design rule is called the Principle of Least Privilege[32] , and it has both quality and security implications. _(javascriptallonge.pdf (source-range-83ecb080-00679))_
- Typically, we want to bind our names as close to where we need them as possible. _(javascriptallonge.pdf (source-range-83ecb080-00679))_
- Being able to bind a name inside of a block means that if the name is only needed in the block, we are not “leaking” its binding to other parts of the code that do not need to interact with it. _(javascriptallonge.pdf (source-range-83ecb080-00679))_
- This design rule is called the Principle of Least Privilege[32] , and it has both quality and security implications. _(javascriptallonge.pdf (source-range-83ecb080-00679))_

## Technical atoms

> Context: Let’s start, as above, by doing this with parameters. We’ll start with:
_(context: javascriptallonge.pdf (source-range-83ecb080-00647))_

> ((PI) => (diameter) => diameter * PI )(3.14159265)
_(source: javascriptallonge.pdf (source-range-83ecb080-00648))_

> Context: And gratuitously wrap it in another IIFE so that we can bind PI to something else:
_(context: javascriptallonge.pdf (source-range-83ecb080-00649))_

> ((PI) => ((PI) => (diameter) => diameter * PI )(3.14159265) )(3)
_(source: javascriptallonge.pdf (source-range-83ecb080-00652))_

> Context: This still evaluates to a function that calculates diameters:
_(context: javascriptallonge.pdf (source-range-83ecb080-00653))_

> ((PI) => ((PI) => (diameter) => diameter * PI )(3.14159265) )(3)(2) _//=> 6.2831853_
_(source: javascriptallonge.pdf (source-range-83ecb080-00654))_

> Context: And we can see that our diameter * PI expression uses the binding for PI in the closest parent environment. but one question: Did binding 3.14159265 to PI somehow change the binding in the “outer” environment? Let’s rewrite things slightly differently: Now we bind 3 to PI in an otherwise empty IIFE inside of our IIFE that binds 3.14159265 to PI. Does that binding “overwrite” the outer one? Will our function return 6 or 6.2831853? This is a book, you’ve already scanned ahead, so you know that the
_(context: javascriptallonge.pdf (source-range-83ecb080-00655, source-range-83ecb080-00657))_

> ((PI) => { ((PI) => {})(3); **return** (diameter) => diameter * PI; })(3.14159265)
_(source: javascriptallonge.pdf (source-range-83ecb080-00656))_

> Context: Now we bind 3 to PI in an otherwise empty IIFE inside of our IIFE that binds 3.14159265 to PI. Does that binding “overwrite” the outer one? Will our function return 6 or 6.2831853? This is a book, you’ve already scanned ahead, so you know that the answer is **no** , the inner binding does not overwrite the outer binding:
_(context: javascriptallonge.pdf (source-range-83ecb080-00657))_

> ((PI) => { ((PI) => {})(3); **return** (diameter) => diameter * PI; })(3.14159265)(2) _//=> 6.2831853_
_(source: javascriptallonge.pdf (source-range-83ecb080-00658))_

> ((diameter) => { **const** PI = 3.14159265; (() => { **const** PI = 3; })(); **return** diameter * PI; })(2) _//=> 6.2831853_
_(source: javascriptallonge.pdf (source-range-83ecb080-00663))_

> Context: This is enormously important. Consider the alternative: What if const could be declared inside of a block, but it always bound the name in the function’s scope. In that case, we’d see things like this: If const always bound its value to the name defined in the function’s environment, placing a const statement inside of a block would merely rebind the existing name, overwriting its old contents. That would be super-confusing. And this code would “work:”
_(context: javascriptallonge.pdf (source-range-83ecb080-00673, source-range-83ecb080-00676))_

> ((diameter) => { **const** PI = 3.14159265;
_(source: javascriptallonge.pdf (source-range-83ecb080-00674))_

> Context: This is enormously important. Consider the alternative: What if const could be declared inside of a block, but it always bound the name in the function’s scope. In that case, we’d see things like this: If const always bound its value to the name defined in the function’s environment, placing a const statement inside of a block would merely rebind the existing name, overwriting its old contents. That would be super-confusing. And this code would “work:”
_(context: javascriptallonge.pdf (source-range-83ecb080-00673, source-range-83ecb080-00676))_

> **if** ( **true** ) { **const** PI = 3; } **return** diameter * PI; })(2) _//=> would return 6 if const had function scope_
_(source: javascriptallonge.pdf (source-range-83ecb080-00675))_

> Context: This is enormously important. Consider the alternative: What if const could be declared inside of a block, but it always bound the name in the function’s scope. In that case, we’d see things like this:
_(context: javascriptallonge.pdf (source-range-83ecb080-00673))_

> If const always bound its value to the name defined in the function’s environment, placing a const statement inside of a block would merely rebind the existing name, overwriting its old contents.
_(source: javascriptallonge.pdf (source-range-83ecb080-00676))_

> Context: If const always bound its value to the name defined in the function’s environment, placing a const statement inside of a block would merely rebind the existing name, overwriting its old contents. That would be super-confusing. And this code would “work:”
_(context: javascriptallonge.pdf (source-range-83ecb080-00676))_

> **if** ( **true** ) { **const** PI = 3.14159265; } **return** diameter * PI; })(2) _//=> would return 6.2831853 if const had function scope_
_(source: javascriptallonge.pdf (source-range-83ecb080-00678))_
