---
page_id: javascriptallonge-section-inside-out-42d13885
page_kind: source
summary: inside-out: 23 source-backed entries and 6 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-inside-out-42d13885@980111955c082dfa04ae961c1ea17e05
---

# inside-out

From [[javascriptallonge]].

## Statements

- There's another way we can make a function that binds 3.14159265 to the name PI and then uses that in its expression. We can turn things inside-out by putting the binding inside our diameter calculating function, like this: _(javascriptallonge.pdf (source-range-8eb13d6b-00401))_
- Which one is better? Well, the first one seems simplest, but a half-century of experience has taught us that names matter. A 'magic literal' like 3.14159265 is anathema to sustainable software development. _(javascriptallonge.pdf (source-range-8eb13d6b-00405))_
- The third one is easiest for most people to read. It separates concerns nicely: The 'outer' function describes its parameters: _(javascriptallonge.pdf (source-range-8eb13d6b-00406))_
- 29 JavaScript programmers regularly use the idea of writing an expression that denotes a function and then immediately applying it to arguments. Explaining the pattern, Ben Alman coined the term [Immediately Invoked Function Expression][iife] for it, often abbreviated 'IIFE.' _(javascriptallonge.pdf (source-range-8eb13d6b-00407))_
- Everything else is encapsulated in its body. That's how it should be, naming PI is its concern, not ours. The other formulation: _(javascriptallonge.pdf (source-range-8eb13d6b-00409))_
- Well, the wrinkle with this is that typically, invoking functions is considerably more expensive than evaluating expressions. Every time we invoke the outer function, we'll invoke the inner function. We could get around this by writing _(javascriptallonge.pdf (source-range-8eb13d6b-00413))_
- But then we've obfuscated our code, and we don't want to do that unless we absolutely have to. _(javascriptallonge.pdf (source-range-8eb13d6b-00415))_
- What would be very nice is if the language gave us a way to bind names inside of blocks without incurring the cost of a function invocation. And JavaScript does. _(javascriptallonge.pdf (source-range-8eb13d6b-00416))_
- We can turn things inside-out by putting the binding inside our diameter calculating function, like this: _(javascriptallonge.pdf (source-range-8eb13d6b-00401))_
- There's another way we can make a function that binds 3.14159265 to the name PI and then uses that in its expression. _(javascriptallonge.pdf (source-range-8eb13d6b-00401))_
- 29 JavaScript programmers regularly use the idea of writing an expression that denotes a function and then immediately applying it to arguments. _(javascriptallonge.pdf (source-range-8eb13d6b-00407))_
- But then we've obfuscated our code, and we don't want to do that unless we absolutely have to. _(javascriptallonge.pdf (source-range-8eb13d6b-00415))_
- What would be very nice is if the language gave us a way to bind names inside of blocks without incurring the cost of a function invocation. _(javascriptallonge.pdf (source-range-8eb13d6b-00416))_

## Technical atoms

### Technical frame 1: inside-out

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00405))_

> Which one is better? Well, the first one seems simplest, but a half-century of experience has taught us that names matter. A 'magic literal' like 3.14159265 is anathema to sustainable software development.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00402))_

```
(diameter) => ((PI) => diameter * PI)(3.14159265)
```

### Technical frame 2: inside-out

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00405))_

> Which one is better? Well, the first one seems simplest, but a half-century of experience has taught us that names matter. A 'magic literal' like 3.14159265 is anathema to sustainable software development.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00404))_

```
((diameter) => diameter * 3.14159265)(2) //=> 6.2831853 ((PI) => (diameter) => diameter * PI )(3.14159265)(2) //=> 6.2831853 ((diameter) => ((PI) => diameter * PI)(3.14159265))(2) //=> 6.2831853
```

### Technical frame 3: inside-out

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00409))_

> Everything else is encapsulated in its body. That's how it should be, naming PI is its concern, not ours. The other formulation:

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00408))_

```
(diameter) => // ...
```

### Technical frame 4: inside-out

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00413))_

> Well, the wrinkle with this is that typically, invoking functions is considerably more expensive than evaluating expressions. Every time we invoke the outer function, we'll invoke the inner function. We could get around this by writing

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00410))_

```
((PI) => // ... )(3.14159265)
```

### Technical frame 5: inside-out

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00413))_

> Well, the wrinkle with this is that typically, invoking functions is considerably more expensive than evaluating expressions. Every time we invoke the outer function, we'll invoke the inner function. We could get around this by writing

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00412))_

```
(diameter) => ((PI) => diameter * PI)(3.14159265)
```

### Technical frame 6: inside-out

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00415))_

> But then we've obfuscated our code, and we don't want to do that unless we absolutely have to.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00414))_

```
((PI) => (diameter) => diameter * PI )(3.14159265)
```
