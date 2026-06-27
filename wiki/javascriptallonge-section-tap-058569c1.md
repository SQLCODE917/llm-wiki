---
page_id: javascriptallonge-section-tap-058569c1
page_kind: source
summary: Tap: 10 source-backed entries and 6 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-tap-058569c1@49ef111a147eb59be02a9332d92ec7d9
---

# Tap

From [[javascriptallonge]].

## Statements

- It has some surprising applications. _(javascriptallonge.pdf (source-range-83ecb080-00979))_
- One is when you want to do something with a value for sideeffects, but keep the value around. _(javascriptallonge.pdf (source-range-83ecb080-00979))_
- tap is a traditional name borrowed from various Unix shell commands. _(javascriptallonge.pdf (source-range-83ecb080-00981))_
- tap can do more than just act as a debugging aid. _(javascriptallonge.pdf (source-range-83ecb080-00996))_

## Technical atoms

> **const** K = (x) => (y) => x;
_(source: javascriptallonge.pdf (source-range-83ecb080-00978))_

> Context: It has some surprising applications. One is when you want to do something with a value for sideeffects, but keep the value around. Behold:
_(context: javascriptallonge.pdf (source-range-83ecb080-00979))_

> **const** tap = (value) => (fn) => ( **typeof** (fn) === 'function' && fn(value), value )
_(source: javascriptallonge.pdf (source-range-83ecb080-00980))_

> Context: tap is a traditional name borrowed from various Unix shell commands. It takes a value and returns a function that always returns the value, but if you pass it a function, it executes the function for side-effects. Let’s see it in action as a poor-man’s debugger:
_(context: javascriptallonge.pdf (source-range-83ecb080-00981))_

> tap('espresso')((it) => { console.log(`Our drink is ' **${** it **}** '`) }); _//=> Our drink is 'espresso'_ 'espresso'
_(source: javascriptallonge.pdf (source-range-83ecb080-00982))_

> Context: It’s easy to turn off:
_(context: javascriptallonge.pdf (source-range-83ecb080-00983))_

> tap('espresso')(); _//=> 'espresso'_
_(source: javascriptallonge.pdf (source-range-83ecb080-00984))_

> Context: Libraries like Underscore[49] use a version of tap that is “uncurried:”
_(context: javascriptallonge.pdf (source-range-83ecb080-00985))_

> _.tap('espresso', (it) => console.log(`Our drink is ' **${** it **}** '`) ); _//=> Our drink is 'espresso'_ 'espresso'
_(source: javascriptallonge.pdf (source-range-83ecb080-00986))_

> Context: Now we can write:
_(context: javascriptallonge.pdf (source-range-83ecb080-00992))_

> tap('espresso')((it) => { console.log(`Our drink is ' **${** it **}** '`) }); _//=> Our drink is 'espresso'_ 'espresso'
_(source: javascriptallonge.pdf (source-range-83ecb080-00993))_
