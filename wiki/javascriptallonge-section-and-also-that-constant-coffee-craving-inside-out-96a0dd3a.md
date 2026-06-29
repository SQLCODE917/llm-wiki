---
page_id: javascriptallonge-section-and-also-that-constant-coffee-craving-inside-out-96a0dd3a
page_kind: source
summary: And also: / That Constant Coffee Craving / inside-out: 23 source-backed entries and 6 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-29
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-and-also-that-constant-coffee-craving-inside-out-96a0dd3a@b7c61aa74cb3f48a70f0f83c85f6f07f
---

# And also: / That Constant Coffee Craving / inside-out

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-and-also-that-constant-coffee-craving-7d1b2fd1]] - broader source section: And also: / That Constant Coffee Craving

## Statements

- There's another way we can make a function that binds 3.14159265 to the name PI and then uses that in its expression. We can turn things inside-out by putting the binding inside our diameter calculating function, like this: _(javascriptallonge.pdf (source-range-7239e085-00398))_
- Which one is better? Well, the first one seems simplest, but a half-century of experience has taught us that names matter. A 'magic literal' like 3.14159265 is anathema to sustainable software development. _(javascriptallonge.pdf (source-range-7239e085-00402))_
- The third one is easiest for most people to read. It separates concerns nicely: The 'outer' function describes its parameters: _(javascriptallonge.pdf (source-range-7239e085-00403))_
- 29 JavaScript programmers regularly use the idea of writing an expression that denotes a function and then immediately applying it to arguments. Explaining the pattern, Ben Alman coined the term [Immediately Invoked Function Expression][iife] for it, often abbreviated 'IIFE.' _(javascriptallonge.pdf (source-range-7239e085-00404))_
- Everything else is encapsulated in its body. That's how it should be, naming PI is its concern, not ours. The other formulation: _(javascriptallonge.pdf (source-range-7239e085-00406))_
- Well, the wrinkle with this is that typically, invoking functions is considerably more expensive than evaluating expressions. Every time we invoke the outer function, we'll invoke the inner function. We could get around this by writing _(javascriptallonge.pdf (source-range-7239e085-00410))_
- But then we've obfuscated our code, and we don't want to do that unless we absolutely have to. _(javascriptallonge.pdf (source-range-7239e085-00412))_
- What would be very nice is if the language gave us a way to bind names inside of blocks without incurring the cost of a function invocation. And JavaScript does. _(javascriptallonge.pdf (source-range-7239e085-00413))_
- We can turn things inside-out by putting the binding inside our diameter calculating function, like this: _(javascriptallonge.pdf (source-range-7239e085-00398))_
- There's another way we can make a function that binds 3.14159265 to the name PI and then uses that in its expression. _(javascriptallonge.pdf (source-range-7239e085-00398))_
- 29 JavaScript programmers regularly use the idea of writing an expression that denotes a function and then immediately applying it to arguments. _(javascriptallonge.pdf (source-range-7239e085-00404))_
- But then we've obfuscated our code, and we don't want to do that unless we absolutely have to. _(javascriptallonge.pdf (source-range-7239e085-00412))_
- What would be very nice is if the language gave us a way to bind names inside of blocks without incurring the cost of a function invocation. _(javascriptallonge.pdf (source-range-7239e085-00413))_

## Technical atoms

### Technical frame 1: And also: / That Constant Coffee Craving / inside-out

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00402))_

> Which one is better? Well, the first one seems simplest, but a half-century of experience has taught us that names matter. A 'magic literal' like 3.14159265 is anathema to sustainable software development.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00399))_

```
(diameter) =>
((PI) =>
diameter * PI)(3.14159265)
```

### Technical frame 2: And also: / That Constant Coffee Craving / inside-out

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00402))_

> Which one is better? Well, the first one seems simplest, but a half-century of experience has taught us that names matter. A 'magic literal' like 3.14159265 is anathema to sustainable software development.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00401))_

```
((diameter) => diameter * 3.14159265)(2)
//=> 6.2831853
((PI) =>
(diameter) => diameter * PI
)(3.14159265)(2)
//=> 6.2831853
((diameter) =>
((PI) =>
diameter * PI)(3.14159265))(2)
//=> 6.2831853
```

### Technical frame 3: And also: / That Constant Coffee Craving / inside-out

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00406))_

> Everything else is encapsulated in its body. That's how it should be, naming PI is its concern, not ours. The other formulation:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00405))_

```
(diameter) =>
// ...
```

### Technical frame 4: And also: / That Constant Coffee Craving / inside-out

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00410))_

> Well, the wrinkle with this is that typically, invoking functions is considerably more expensive than evaluating expressions. Every time we invoke the outer function, we'll invoke the inner function. We could get around this by writing

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00407))_

```
((PI) =>
// ...
)(3.14159265)
```

### Technical frame 5: And also: / That Constant Coffee Craving / inside-out

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00410))_

> Well, the wrinkle with this is that typically, invoking functions is considerably more expensive than evaluating expressions. Every time we invoke the outer function, we'll invoke the inner function. We could get around this by writing

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00409))_

```
(diameter) =>
((PI) =>
diameter * PI)(3.14159265)
```

### Technical frame 6: And also: / That Constant Coffee Craving / inside-out

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00412))_

> But then we've obfuscated our code, and we don't want to do that unless we absolutely have to.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00411))_

```
((PI) =>
(diameter) => diameter * PI
)(3.14159265)
```
