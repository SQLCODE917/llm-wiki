---
page_id: javascriptallonge-statement
page_kind: concept
summary: Statement: 6 statement(s) and 11 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-statement@a6dcb9204cd1c85470d0361db7eb5e9a
---

# Statement

What [[javascriptallonge]] covers about statement:

## Statements

### a quick summary of functions and bodies

- One of the important possible statements is a return statement. A return statement accepts any valid JavaScript expression. _(javascriptallonge.pdf (source-range-8eb13d6b-00291))_

### nested blocks

- The if statement is a statement, not an expression (an unfortunate design choice), and its clauses are statements or blocks. So we could also write something like: _(javascriptallonge.pdf (source-range-8eb13d6b-00445))_

### are consts also from a shadowy planet?

- But const statements can appear inside blocks, and we saw that blocks can appear inside of other blocks, including function bodies. So where are const variables bound? In the function environment? Or in an environment corresponding to the block? _(javascriptallonge.pdf (source-range-8eb13d6b-00468))_

- Parameters are only bound when we invoke a function. That's why we made all these IIFEs. But const statements can appear inside blocks. What happens when we use a const inside of a block? We'll need a gratuitous block. We've seen if statements, what could be more gratuitous than: _(javascriptallonge.pdf (source-range-8eb13d6b-00484))_

### Functions

- Blocks also create scopes if const statements are within them. _(javascriptallonge.pdf (source-range-8eb13d6b-00650))_

### destructuring arrays

- The statement const [something] = wrapped; destructures the array represented by wrapped , binding the value of its single element to the name something . We can do the same thing with more than one element: _(javascriptallonge.pdf (source-range-8eb13d6b-00847))_


## Technical atoms

### Technical frame 1: nested blocks

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00445))_

> The if statement is a statement, not an expression (an unfortunate design choice), and its clauses are statements or blocks. So we could also write something like:

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00442))_

```
(n) => { const even = (x) => { if (x === 0) return true ; else return !even(x - 1); } return even(n) }
```

### Technical frame 2: nested blocks

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00449))_

> We've used a block as the else clause, and since it's a block, we've placed a const statement inside it.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00446))_

```
(n) => { const even = (x) => { if (x === 0) return true ; else { const odd = (y) => !even(y); return odd(x - 1); }
```

### Technical frame 3: nested blocks

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00449))_

> We've used a block as the else clause, and since it's a block, we've placed a const statement inside it.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00447))_

```
} return even(n) } And this also works: ((n) => { const even = (x) => { if (x === 0) return true ; else { const odd = (y) => !even(y); return odd(x - 1); } } return even(n) })(42)
```

### Technical frame 4: nested blocks

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00449))_

> We've used a block as the else clause, and since it's a block, we've placed a const statement inside it.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00448))_

```
//=> true
```

### Technical frame 5: are consts also from a shadowy planet?

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00492))_

> Again, confusing. Typically, we want to bind our names as close to where we need them as possible. This design rule is called the Principle of Least Privilege 32 , and it has both quality and security implications. Being able to bind a name inside of a block means that if the name is only needed in the block, we are not 'leaking' its binding to other parts of the code that do not need to interact with it.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00485))_

```
if ( true ) { // an immediately invoked block statement (IIBS) } Let's try it: ((diameter) => { const PI = 3; if ( true ) { const PI = 3.14159265; return diameter * PI; } })(2) //=> 6.2831853 ((diameter) => { const PI = 3.14159265; if ( true ) { const PI = 3; } return diameter * PI;
```

### Technical frame 6: are consts also from a shadowy planet?

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00492))_

> Again, confusing. Typically, we want to bind our names as close to where we need them as possible. This design rule is called the Principle of Least Privilege 32 , and it has both quality and security implications. Being able to bind a name inside of a block means that if the name is only needed in the block, we are not 'leaking' its binding to other parts of the code that do not need to interact with it.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00486))_

```
})(2) //=> 6.2831853
```

### Technical frame 7: are consts also from a shadowy planet?

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00492))_

> Again, confusing. Typically, we want to bind our names as close to where we need them as possible. This design rule is called the Principle of Least Privilege 32 , and it has both quality and security implications. Being able to bind a name inside of a block means that if the name is only needed in the block, we are not 'leaking' its binding to other parts of the code that do not need to interact with it.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00489))_

```
((diameter) => { const PI = 3.14159265; if ( true ) { const PI = 3; } return diameter * PI; })(2) //=> would return 6 if const had function scope
```

### Technical frame 8: are consts also from a shadowy planet?

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00492))_

> Again, confusing. Typically, we want to bind our names as close to where we need them as possible. This design rule is called the Principle of Least Privilege 32 , and it has both quality and security implications. Being able to bind a name inside of a block means that if the name is only needed in the block, we are not 'leaking' its binding to other parts of the code that do not need to interact with it.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00491))_

```
((diameter) => { if ( true ) { const PI = 3.14159265; } return diameter * PI; })(2) //=> would return 6.2831853 if const had function scope
```

### Technical frame 9: destructuring arrays

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00847))_

> The statement const [something] = wrapped; destructures the array represented by wrapped , binding the value of its single element to the name something . We can do the same thing with more than one element:

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00846))_

```
const unwrap = (wrapped) => { const [something] = wrapped; return something; } unwrap(["present"]) //=> "present"
```

### Technical frame 10: destructuring arrays

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00849))_

> We could do the same thing with (name) => name[1] , but destructuring is code that resembles the data it consumes, a valuable coding style.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00848))_

```
const surname = (name) => { const [first, last] = name; return last; } surname(["Reginald", "Braithwaite"]) //=> "Braithwaite"
```

### Technical atom 11

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00571))_

| entry | content |
| --- | --- |
| 37 | As we'll discuss later, this implementation of the B Combinator is correct in languages like Scheme, but for truly general-purpose use in JavaScript, it needs to correctly manage the function context. |
| 38 | We'll see later why an even more useful version would be written (fn) => (...args) => !fn(...args) |

<details>
<summary>Raw table text</summary>

```
function decorators
A function decorator is a higher-order function that takes one function as an argument, returns another function, and the returned function is a variation of the argument function. Here's a ridiculously simple decorator: 38
37 As we'll discuss later, this implementation of the B Combinator is correct in languages like Scheme, but for truly general-purpose use in JavaScript, it needs to correctly manage the function context.
38 We'll see later why an even more useful version would be written (fn) => (...args) => !fn(...args)
```

</details>


## Related pages

- [[javascriptallonge-block]] - shared statements and technical atoms: Block shares source evidence from Functions: Blocks also create scopes if const statements are within them.; Block shares technical record from nested blocks: (n) => { const even = (x) => { if (x === 0) return true ; else return !even(x - 1); } return even(n) } (1 shared statement(s), 4 shared atom(s))
- [[javascriptallonge-bound]] - shared technical atoms: Bound shares technical record from are consts also from a shadowy planet?: if ( true ) { // an immediately invoked block statement (IIBS) } Let's try it: ((diameter) => { const PI = 3; if ( true ) { const PI = 3.14159265; return diameter * ... [truncated] (4 shared atom(s))
- [[javascriptallonge-environment]] - shared technical atoms: Environment shares technical record from are consts also from a shadowy planet?: ((diameter) => { const PI = 3.14159265; if ( true ) { const PI = 3; } return diameter * PI; })(2) //=> would return 6 if const had function scope (2 shared atom(s))
- [[javascriptallonge-javascript]] - shared technical atoms: Javascript shares technical record from destructuring arrays: const unwrap = (wrapped) => { const [something] = wrapped; return something; } unwrap(["present"]) //=> "present" (2 shared atom(s))
- [[javascriptallonge-parameter]] - shared technical atoms: Parameter shares technical record from are consts also from a shadowy planet?: if ( true ) { // an immediately invoked block statement (IIBS) } Let's try it: ((diameter) => { const PI = 3; if ( true ) { const PI = 3.14159265; return diameter * ... [truncated] (2 shared atom(s))
- [[javascriptallonge-value]] - shared technical atoms: Value shares technical record from are consts also from a shadowy planet?: ((diameter) => { const PI = 3.14159265; if ( true ) { const PI = 3; } return diameter * PI; })(2) //=> would return 6 if const had function scope (2 shared atom(s))
- [[javascriptallonge-argument]] - shared technical atoms: Argument shares technical table: function decorators A function decorator is a higher-order function that takes one function as an argument, returns another function, and the returned function is a ... [truncated] (1 shared atom(s))
- [[javascriptallonge-function]] - shared technical atoms: Function shares technical table: function decorators A function decorator is a higher-order function that takes one function as an argument, returns another function, and the returned function is a ... [truncated] (1 shared atom(s))
- [[javascriptallonge-language]] - shared technical atoms: Language shares technical table: function decorators A function decorator is a higher-order function that takes one function as an argument, returns another function, and the returned function is a ... [truncated] (1 shared atom(s))
- [[javascriptallonge-purpose]] - shared technical atoms: Purpose shares technical table: function decorators A function decorator is a higher-order function that takes one function as an argument, returns another function, and the returned function is a ... [truncated] (1 shared atom(s))
- [[javascriptallonge-return]] - shared technical atoms: Return shares technical table: function decorators A function decorator is a higher-order function that takes one function as an argument, returns another function, and the returned function is a ... [truncated] (1 shared atom(s))
- [[javascriptallonge-seen]] - shared technical atoms: Seen shares technical record from nested blocks: (n) => { const even = (x) => { if (x === 0) return true ; else return !even(x - 1); } return even(n) } (1 shared atom(s))
- [[javascriptallonge-works-just-fine-because-arguments]] - shared technical atoms: Works Just Fine, Because Arguments[0 shares technical table: function decorators A function decorator is a higher-order function that takes one function as an argument, returns another function, and the returned function is a ... [truncated] (1 shared atom(s))
- [[javascriptallonge-important]] - shared statements: Important shares source evidence from a quick summary of functions and bodies: One of the important possible statements is a return statement. A return statement accepts any valid JavaScript expression. (1 shared statement(s))

## Source

- [[javascriptallonge]]
