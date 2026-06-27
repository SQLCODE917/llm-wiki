---
page_id: javascriptallonge-section-tap-058569c1
page_kind: source
summary: Tap: 10 source-backed entries and 6 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-tap-058569c1@50d830c235261713e2a31761f27a2c93
---

# Tap

From [[javascriptallonge]].

## Statements

- It has some surprising applications. _(javascriptallonge.pdf (source-range-83ecb080-00979))_
- One is when you want to do something with a value for sideeffects, but keep the value around. _(javascriptallonge.pdf (source-range-83ecb080-00979))_
- tap is a traditional name borrowed from various Unix shell commands. _(javascriptallonge.pdf (source-range-83ecb080-00981))_
- tap can do more than just act as a debugging aid. _(javascriptallonge.pdf (source-range-83ecb080-00996))_

## Technical atoms

### Technical atom 1

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00978))_

> **const** K = (x) => (y) => x;

### Technical atom 2

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00979))_

> It has some surprising applications. One is when you want to do something with a value for sideeffects, but keep the value around. Behold:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00980))_

> **const** tap = (value) => (fn) => ( **typeof** (fn) === 'function' && fn(value), value )

### Technical atom 3

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00981))_

> tap is a traditional name borrowed from various Unix shell commands. It takes a value and returns a function that always returns the value, but if you pass it a function, it executes the function for side-effects. Let’s see it in action as a poor-man’s debugger:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00982))_

> tap('espresso')((it) => { console.log(`Our drink is ' **${** it **}** '`) }); _//=> Our drink is 'espresso'_ 'espresso'

### Technical atom 4

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00983))_

> It’s easy to turn off:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00984))_

> tap('espresso')(); _//=> 'espresso'_

### Technical atom 5

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00985))_

> Libraries like Underscore[49] use a version of tap that is “uncurried:”

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00986))_

> _.tap('espresso', (it) => console.log(`Our drink is ' **${** it **}** '`) ); _//=> Our drink is 'espresso'_ 'espresso'

### Technical atom 6

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00992))_

> Now we can write:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00993))_

> tap('espresso')((it) => { console.log(`Our drink is ' **${** it **}** '`) }); _//=> Our drink is 'espresso'_ 'espresso'
