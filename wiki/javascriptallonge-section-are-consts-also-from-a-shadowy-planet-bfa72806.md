---
page_id: javascriptallonge-section-are-consts-also-from-a-shadowy-planet-bfa72806
page_kind: source
summary: are consts also from a shadowy planet?: 30 source-backed entries and 11 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-are-consts-also-from-a-shadowy-planet-bfa72806@a9f21b8335c3a31005e34b9dbfe2dcce
---

# are consts also from a shadowy planet?

From [[javascriptallonge]].

## Statements

- We just saw that values bound with const use lexical scope, just like values bound with parameters. They are looked up in the environment where they are declared. And we know that functions create environments. Parameters are declared when we create functions, so it makes sense that parameters are bound to environments created when we invoke functions. _(javascriptallonge.pdf (source-range-8eb13d6b-00467))_
- But const statements can appear inside blocks, and we saw that blocks can appear inside of other blocks, including function bodies. So where are const variables bound? In the function environment? Or in an environment corresponding to the block? _(javascriptallonge.pdf (source-range-8eb13d6b-00468))_
- We can test this by creating another conflict. But instead of binding two different variables to the same name in two different places, we'll bind two different values to the same name, but one environment will be completely enclosed by the other. _(javascriptallonge.pdf (source-range-8eb13d6b-00469))_
- And we can see that our diameter * PI expression uses the binding for PI in the closest parent environment. but one question: Did binding 3.14159265 to PI somehow change the binding in the 'outer' environment? Let's rewrite things slightly differently: _(javascriptallonge.pdf (source-range-8eb13d6b-00476))_
- Now we bind 3 to PI in an otherwise empty IIFE inside of our IIFE that binds 3.14159265 to PI . Does that binding 'overwrite' the outer one? Will our function return 6 or 6.2831853 ? This is a book, you've already scanned ahead, so you know that the answer is no , the inner binding does not overwrite the outer binding: _(javascriptallonge.pdf (source-range-8eb13d6b-00478))_
- We say that when we bind a variable using a parameter inside another binding, the inner binding shadows the outer binding. It has effect inside its own scope, but does not affect the binding in the enclosing scope. _(javascriptallonge.pdf (source-range-8eb13d6b-00480))_
- Parameters are only bound when we invoke a function. That's why we made all these IIFEs. But const statements can appear inside blocks. What happens when we use a const inside of a block? We'll need a gratuitous block. We've seen if statements, what could be more gratuitous than: _(javascriptallonge.pdf (source-range-8eb13d6b-00484))_
- Again, confusing. Typically, we want to bind our names as close to where we need them as possible. This design rule is called the Principle of Least Privilege 32 , and it has both quality and security implications. Being able to bind a name inside of a block means that if the name is only needed in the block, we are not 'leaking' its binding to other parts of the code that do not need to interact with it. _(javascriptallonge.pdf (source-range-8eb13d6b-00492))_
- But const statements can appear inside blocks, and we saw that blocks can appear inside of other blocks, including function bodies. _(javascriptallonge.pdf (source-range-8eb13d6b-00468))_
- It has effect inside its own scope, but does not affect the binding in the enclosing scope. _(javascriptallonge.pdf (source-range-8eb13d6b-00480))_
- But const statements can appear inside blocks. _(javascriptallonge.pdf (source-range-8eb13d6b-00484))_
- Parameters are only bound when we invoke a function. _(javascriptallonge.pdf (source-range-8eb13d6b-00484))_
- This design rule is called the Principle of Least Privilege 32 , and it has both quality and security implications. _(javascriptallonge.pdf (source-range-8eb13d6b-00492))_

## Technical atoms

### Technical frame 1: are consts also from a shadowy planet?

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00476))_

> And we can see that our diameter * PI expression uses the binding for PI in the closest parent environment. but one question: Did binding 3.14159265 to PI somehow change the binding in the 'outer' environment? Let's rewrite things slightly differently:

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00471))_

```
((PI) => (diameter) => diameter * PI )(3.14159265)
```

### Technical frame 2: are consts also from a shadowy planet?

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00476))_

> And we can see that our diameter * PI expression uses the binding for PI in the closest parent environment. but one question: Did binding 3.14159265 to PI somehow change the binding in the 'outer' environment? Let's rewrite things slightly differently:

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00473))_

```
((PI) => ((PI) => (diameter) => diameter * PI )(3.14159265) )(3)
```

### Technical frame 3: are consts also from a shadowy planet?

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00476))_

> And we can see that our diameter * PI expression uses the binding for PI in the closest parent environment. but one question: Did binding 3.14159265 to PI somehow change the binding in the 'outer' environment? Let's rewrite things slightly differently:

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00475))_

```
((PI) => ((PI) => (diameter) => diameter * PI )(3.14159265) )(3)(2) //=> 6.2831853
```

### Technical frame 4: are consts also from a shadowy planet?

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00478))_

> Now we bind 3 to PI in an otherwise empty IIFE inside of our IIFE that binds 3.14159265 to PI . Does that binding 'overwrite' the outer one? Will our function return 6 or 6.2831853 ? This is a book, you've already scanned ahead, so you know that the answer is no , the inner binding does not overwrite the outer binding:

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00477))_

```
((PI) => { ((PI) => {})(3); return (diameter) => diameter * PI; })(3.14159265)
```

### Technical frame 5: are consts also from a shadowy planet?

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00480))_

> We say that when we bind a variable using a parameter inside another binding, the inner binding shadows the outer binding. It has effect inside its own scope, but does not affect the binding in the enclosing scope.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00479))_

```
((PI) => { ((PI) => {})(3); return (diameter) => diameter * PI; })(3.14159265)(2) //=> 6.2831853
```

### Technical frame 6: are consts also from a shadowy planet?

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00484))_

> Parameters are only bound when we invoke a function. That's why we made all these IIFEs. But const statements can appear inside blocks. What happens when we use a const inside of a block? We'll need a gratuitous block. We've seen if statements, what could be more gratuitous than:

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00482))_

```
((diameter) => { const PI = 3.14159265; (() => { const PI = 3; })(); return diameter * PI; })(2) //=> 6.2831853
```

### Technical frame 7: are consts also from a shadowy planet?

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00492))_

> Again, confusing. Typically, we want to bind our names as close to where we need them as possible. This design rule is called the Principle of Least Privilege 32 , and it has both quality and security implications. Being able to bind a name inside of a block means that if the name is only needed in the block, we are not 'leaking' its binding to other parts of the code that do not need to interact with it.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00485))_

```
if ( true ) { // an immediately invoked block statement (IIBS) } Let's try it: ((diameter) => { const PI = 3; if ( true ) { const PI = 3.14159265; return diameter * PI; } })(2) //=> 6.2831853 ((diameter) => { const PI = 3.14159265; if ( true ) { const PI = 3; } return diameter * PI;
```

### Technical frame 8: are consts also from a shadowy planet?

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00492))_

> Again, confusing. Typically, we want to bind our names as close to where we need them as possible. This design rule is called the Principle of Least Privilege 32 , and it has both quality and security implications. Being able to bind a name inside of a block means that if the name is only needed in the block, we are not 'leaking' its binding to other parts of the code that do not need to interact with it.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00486))_

```
})(2) //=> 6.2831853
```

### Technical frame 9: are consts also from a shadowy planet?

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00492))_

> Again, confusing. Typically, we want to bind our names as close to where we need them as possible. This design rule is called the Principle of Least Privilege 32 , and it has both quality and security implications. Being able to bind a name inside of a block means that if the name is only needed in the block, we are not 'leaking' its binding to other parts of the code that do not need to interact with it.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00489))_

```
((diameter) => { const PI = 3.14159265; if ( true ) { const PI = 3; } return diameter * PI; })(2) //=> would return 6 if const had function scope
```

### Technical frame 10: are consts also from a shadowy planet?

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00492))_

> Again, confusing. Typically, we want to bind our names as close to where we need them as possible. This design rule is called the Principle of Least Privilege 32 , and it has both quality and security implications. Being able to bind a name inside of a block means that if the name is only needed in the block, we are not 'leaking' its binding to other parts of the code that do not need to interact with it.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00490))_

> If const always bound its value to the name defined in the function's environment, placing a const statement inside of a block would merely rebind the existing name, overwriting its old contents.

### Technical frame 11: are consts also from a shadowy planet?

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00492))_

> Again, confusing. Typically, we want to bind our names as close to where we need them as possible. This design rule is called the Principle of Least Privilege 32 , and it has both quality and security implications. Being able to bind a name inside of a block means that if the name is only needed in the block, we are not 'leaking' its binding to other parts of the code that do not need to interact with it.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00491))_

```
((diameter) => { if ( true ) { const PI = 3.14159265; } return diameter * PI; })(2) //=> would return 6.2831853 if const had function scope
```
