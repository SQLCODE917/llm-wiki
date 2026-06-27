---
page_id: javascriptallonge-section-inside-out-d1381084
page_kind: source
summary: **inside-out**: 22 source-backed entries and 3 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-inside-out-d1381084@27e509932738ab70fa7442c52a86ca31
---

# **inside-out**

From [[javascriptallonge]].

## Statements

- There’s another way we can make a function that binds 3.14159265 to the name PI and then uses that in its expression. _(javascriptallonge.pdf (source-range-83ecb080-00561))_
- We can turn things inside-out by putting the binding inside our diameter calculating function, like this: _(javascriptallonge.pdf (source-range-83ecb080-00561))_
- We can turn things inside-out by putting the binding inside our diameter calculating function, like this: _(javascriptallonge.pdf (source-range-83ecb080-00561))_
- There’s another way we can make a function that binds 3.14159265 to the name PI and then uses that in its expression. _(javascriptallonge.pdf (source-range-83ecb080-00561))_
- A “magic literal” like 3.14159265 is anathema to sustainable software development. _(javascriptallonge.pdf (source-range-83ecb080-00565))_
- Well, the first one seems simplest, but a half-century of experience has taught us that names matter. _(javascriptallonge.pdf (source-range-83ecb080-00565))_
- The third one is easiest for most people to read. _(javascriptallonge.pdf (source-range-83ecb080-00566))_
- Explaining the pattern, Ben Alman coined the term [Immediately Invoked Function Expression][iife] for it, often abbreviated “IIFE.” _(javascriptallonge.pdf (source-range-83ecb080-00567))_
- > 29JavaScript programmers regularly use the idea of writing an expression that denotes a function and then immediately applying it to arguments. _(javascriptallonge.pdf (source-range-83ecb080-00567))_
- > 29JavaScript programmers regularly use the idea of writing an expression that denotes a function and then immediately applying it to arguments. _(javascriptallonge.pdf (source-range-83ecb080-00567))_
- That’s how it should be, naming PI is its concern, not ours. _(javascriptallonge.pdf (source-range-83ecb080-00571))_
- Everything else is encapsulated in its body. _(javascriptallonge.pdf (source-range-83ecb080-00571))_
- “Exposes” naming PI first, and we have to look inside to find out why we care. _(javascriptallonge.pdf (source-range-83ecb080-00575))_
- “Exposes” naming PI first, and we have to look inside to find out why we care. _(javascriptallonge.pdf (source-range-83ecb080-00575))_
- Well, the wrinkle with this is that typically, invoking functions is considerably more expensive than evaluating expressions. _(javascriptallonge.pdf (source-range-83ecb080-00577))_
- But then we’ve obfuscated our code, and we don’t want to do that unless we absolutely have to. _(javascriptallonge.pdf (source-range-83ecb080-00579))_
- But then we’ve obfuscated our code, and we don’t want to do that unless we absolutely have to. _(javascriptallonge.pdf (source-range-83ecb080-00579))_
- What would be very nice is if the language gave us a way to bind names inside of blocks without incurring the cost of a function invocation. _(javascriptallonge.pdf (source-range-83ecb080-00580))_
- What would be very nice is if the language gave us a way to bind names inside of blocks without incurring the cost of a function invocation. _(javascriptallonge.pdf (source-range-83ecb080-00580))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00561, source-range-83ecb080-00563))_

> There’s another way we can make a function that binds 3.14159265 to the name PI and then uses that in its expression. We can turn things inside-out by putting the binding inside our diameter calculating function, like this: It produces the same result as our previous expressions for a diameter-calculating function:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00562))_

> (diameter) => ((PI) => diameter * PI)(3.14159265)

### Technical atom 2

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00576))_

> - (diameter) => ((PI) => diameter * PI)(3.14159265)

### Technical atom 3

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00578))_

> ((PI) => (diameter) => diameter * PI )(3.14159265)
