---
page_id: javascriptallonge-recipe-reassignment-mixing-let-and-const
page_kind: recipe
page_family: recipe-pattern
summary: Reassignment > mixing let and const: Mixing let and const declarations in JavaScript allows for variable shadowing, where a const declaration inside a block scope can shadow a let...
sources: raw/javascriptallonge.pdf
updated: 2026-07-07
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
projection_coverage: human-article-javascriptallonge-recipe-reassignment-mixing-let-and-const@37a702083ceafde74bc3674b1599b981
---

# Reassignment > mixing let and const

## Variable Shadowing and Reassignment

Mixing let and const declarations in JavaScript allows for variable shadowing, where a const declaration inside a block scope can shadow a let declaration in an outer scope without affecting the reassignment capability of the outer variable. _(raw/javascriptallonge.pdf (p. 150))_ 

## Impact of Shadowing on Variable Reassignment

Shadowing a let with a const does not change the ability to rebind the variable in its original scope, but shadowing a const with a let does not permit reassignment in the original scope. _(raw/javascriptallonge.pdf (p. 150); raw/javascriptallonge.pdf (p. 151))_ 

## Evidence Details

### raw/javascriptallonge.pdf (p. 150)

```text
(() => {
let age = 49;
if (true) {
const age = 50;
}
age = 51;
return age;
})()
//=> 51
```

- raw/javascriptallonge.pdf (p. 150): `Some programmers dislike deliberately shadowing variables.`
- raw/javascriptallonge.pdf (p. 150): `The suggestion is that shadowing a variable is confusing code.`
- raw/javascriptallonge.pdf (p. 150): `If you buy that argument, the way that shadowing works in JavaScript exists to protect us from accidentally shadowing a variable when we move code around.`
- raw/javascriptallonge.pdf (p. 150): `If you dislike deliberately shadowing variables, you'll probably take an even more opprobrious view of mixing const and let semantics with a shadowed variable:`
- raw/javascriptallonge.pdf (p. 150): `Shadowing a let with a const does not change our ability to rebind the variable in its original scope.`
- raw/javascriptallonge.pdf (p. 151): `Shadowing a const with a let does not permit it to be rebound in its original scope.`

## Source Trail

- Source manifest: [[javascriptallonge]]
- raw/javascriptallonge.pdf (p. 150) - Reassignment > mixing let and const
- raw/javascriptallonge.pdf (p. 150) - Reassignment > mixing let and const
- raw/javascriptallonge.pdf (p. 150) - Reassignment > mixing let and const
- raw/javascriptallonge.pdf (p. 150) - Reassignment > mixing let and const
- raw/javascriptallonge.pdf (p. 150) - Reassignment > mixing let and const
- raw/javascriptallonge.pdf (p. 150) - Reassignment > mixing let and const
- raw/javascriptallonge.pdf (p. 151) - Reassignment > mixing let and const
