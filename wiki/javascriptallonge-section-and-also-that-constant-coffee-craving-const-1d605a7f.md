---
page_id: javascriptallonge-section-and-also-that-constant-coffee-craving-const-1d605a7f
page_kind: source
summary: And also: / That Constant Coffee Craving / const: 22 source-backed entries and 10 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-29
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-and-also-that-constant-coffee-craving-const-1d605a7f@0a349a3142355bae477a875d25b6538e
---

# And also: / That Constant Coffee Craving / const

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-and-also-that-constant-coffee-craving-7d1b2fd1]] - broader source section: And also: / That Constant Coffee Craving
- [[javascriptallonge-const]] - topic hub: opens the topic page for Const

## Statements

- Another way to write our 'circumference' function would be to pass PI along with the diameter argument, something like this: _(javascriptallonge.pdf (source-range-7239e085-00415))_
- This differs from our example above in that there is only one environment, rather than two. We have one binding in the environment representing our regular argument, and another our 'constant.' That's more efficient, and it's almost what we wanted all along: A way to bind 3.14159265 to a readable name. _(javascriptallonge.pdf (source-range-7239e085-00419))_
- JavaScript gives us a way to do that, the const keyword. We'll learn a lot more about const in future chapters, but here's the most important thing we can do with const : _(javascriptallonge.pdf (source-range-7239e085-00420))_
- The const keyword introduces one or more bindings in the block that encloses it. It doesn't incur the cost of a function invocation. That's great. Even better, it puts the symbol (like PI ) close to the value ( 3.14159265 ). That's much better than what we were writing. _(javascriptallonge.pdf (source-range-7239e085-00422))_
- We use the const keyword in a const statement . const statements occur inside blocks, we can't use them when we write a fat arrow that has an expression as its body. _(javascriptallonge.pdf (source-range-7239e085-00423))_
- We can bind any expression. Functions are expressions, so we can bind helper functions: _(javascriptallonge.pdf (source-range-7239e085-00430))_
- Notice calc(d) ? This underscores what we've said: if we have an expression that evaluates to a function, we apply it with () . A name that's bound to a function is a valid expression evaluating to a function. 30 _(javascriptallonge.pdf (source-range-7239e085-00432))_
- Amazing how such an important idea-naming functions-can be explained en passant in just a few words. That emphasizes one of the things JavaScript gets really, really right: Functions as 'first class entities. ' Functions are values that can be bound to names like any other value, passed as arguments, returned from other functions, and so forth. _(javascriptallonge.pdf (source-range-7239e085-00433))_
- 30 We're into the second chapter and we've finally named a function. Sheesh. _(javascriptallonge.pdf (source-range-7239e085-00436))_
- This differs from our example above in that there is only one environment, rather than two. _(javascriptallonge.pdf (source-range-7239e085-00419))_

## Technical atoms

### Technical frame 1: And also: / That Constant Coffee Craving / const

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00419))_

> This differs from our example above in that there is only one environment, rather than two. We have one binding in the environment representing our regular argument, and another our 'constant.' That's more efficient, and it's almost what we wanted all along: A way to bind 3.14159265 to a readable name.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00416))_

```
(diameter, PI) => diameter * PI
```

### Technical frame 2: And also: / That Constant Coffee Craving / const

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00419))_

> This differs from our example above in that there is only one environment, rather than two. We have one binding in the environment representing our regular argument, and another our 'constant.' That's more efficient, and it's almost what we wanted all along: A way to bind 3.14159265 to a readable name.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00418))_

```
((diameter, PI) => diameter * PI)(2, 3.14159265)
//=> 6.2831853
```

### Technical frame 3: And also: / That Constant Coffee Craving / const

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00422))_

> The const keyword introduces one or more bindings in the block that encloses it. It doesn't incur the cost of a function invocation. That's great. Even better, it puts the symbol (like PI ) close to the value ( 3.14159265 ). That's much better than what we were writing.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00421))_

```
(diameter) => {
const PI = 3.14159265;
return diameter * PI
}
```

### Technical frame 4: And also: / That Constant Coffee Craving / const

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00430))_

> We can bind any expression. Functions are expressions, so we can bind helper functions:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00425))_

```
((diameter) =>
((PI) =>
```

### Technical frame 5: And also: / That Constant Coffee Craving / const

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00430))_

> We can bind any expression. Functions are expressions, so we can bind helper functions:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00426))_

```
diameter * PI)(3.14159265))(2)
Or:
((diameter, PI) => diameter * PI)(2, 3.14159265)
```

### Technical frame 6: And also: / That Constant Coffee Craving / const

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00430))_

> We can bind any expression. Functions are expressions, so we can bind helper functions:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00427))_

```
//=> 6.2831853
```

### Technical frame 7: And also: / That Constant Coffee Craving / const

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00430))_

> We can bind any expression. Functions are expressions, so we can bind helper functions:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00429))_

```
((diameter) => {
const PI = 3.14159265;
return diameter * PI
})(2)
//=> 6.2831853
```

### Technical frame 8: And also: / That Constant Coffee Craving / const

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00432))_

> Notice calc(d) ? This underscores what we've said: if we have an expression that evaluates to a function, we apply it with () . A name that's bound to a function is a valid expression evaluating to a function. 30

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00431))_

```
(d) => {
const calc = (diameter) => {
const PI = 3.14159265;
return diameter * PI
};
return "The circumference is " + calc(d)
}
```

### Technical frame 9: And also: / That Constant Coffee Craving / const

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00433))_

> Amazing how such an important idea-naming functions-can be explained en passant in just a few words. That emphasizes one of the things JavaScript gets really, really right: Functions as 'first class entities. ' Functions are values that can be bound to names like any other value, passed as arguments, returned from other functions, and so forth.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00432))_

> This underscores what we've said: if we have an expression that evaluates to a function, we apply it with () .

### Technical frame 10: And also: / That Constant Coffee Craving / const

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00436))_

> 30 We're into the second chapter and we've finally named a function. Sheesh.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00435))_

```
(d) => {
const PI
= 3.14159265,
calc = (diameter) => diameter * PI;
return "The circumference is " + calc(d)
}
```
