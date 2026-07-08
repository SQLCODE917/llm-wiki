---
page_id: javascriptallonge-recipe-closures-and-scope-shadowy-variables-from-a-shadowy-planet
page_kind: recipe
page_family: recipe-pattern
summary: Closures and Scope > shadowy variables from a shadowy planet: JavaScript resolves variable bindings by searching a function's own environment first, then each parent environment...
sources: raw/javascriptallonge.pdf
updated: 2026-07-07
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
projection_coverage: human-article-javascriptallonge-recipe-closures-and-scope-shadowy-variables-from-a-shadowy-planet@1f63409821bf24fe43e1a35b15cd875c
---

# Closures and Scope > shadowy variables from a shadowy planet

## How JavaScript Resolves Variable Bindings

JavaScript resolves variable bindings by searching a function's own environment first, then each parent environment in turn. _(raw/javascriptallonge.pdf (p. 47))_ A function such as (x, y) => x + y treats its own x as the binding for x, ignoring any x from a parent scope. _(raw/javascriptallonge.pdf (p. 47))_ In nested functions, variables from outer scopes can be shadowed by variables with the same name in inner scopes. _(raw/javascriptallonge.pdf (p. 47))_ This behavior is often a good thing, as it allows for clearer and more predictable code. _(raw/javascriptallonge.pdf (p. 47))_ 

## Variable Shadowing in JavaScript Closures

When a variable is declared with the same name in a child scope, it shadows the parent's variable binding. _(raw/javascriptallonge.pdf (p. 47))_ 

## Evidence Details

### raw/javascriptallonge.pdf (p. 47)

```text
(x) =>
(x, y) => x + y
```

### raw/javascriptallonge.pdf (p. 47)

```text
(x) =>
(x, y) =>
(w, z) =>
(w) =>
x + y + z
```

- raw/javascriptallonge.pdf (p. 47): `An interesting thing happens when a variable has the same name as an ancestor environment's variable.`
- raw/javascriptallonge.pdf (p. 47): `The function (x, y) => x + y is a pure function, because its x is defined within its own environment.`
- raw/javascriptallonge.pdf (p. 47): `Although its parent also defines an x , it is ignored when evaluating x + y .`
- raw/javascriptallonge.pdf (p. 47): `JavaScript always searches for a binding starting with the functions own environment and then each parent in turn until it finds one.`
- raw/javascriptallonge.pdf (p. 47): `When evaluating x + y + z , JavaScript will find x and y in the great-grandparent scope and z in the parent scope.`
- raw/javascriptallonge.pdf (p. 47): `The x in the great-great-grandparent scope is ignored, as are both w s.`
- raw/javascriptallonge.pdf (p. 47): `When a variable has the same name as an ancestor environment's binding, it is said to shadow the ancestor.`
- raw/javascriptallonge.pdf (p. 47): `This is often a good thing.`

## Source Trail

- Source manifest: [[javascriptallonge]]
- Closures and Scope > shadowy variables from a shadowy planet
- raw/javascriptallonge.pdf (p. 47) - Closures and Scope > shadowy variables from a shadowy planet
- raw/javascriptallonge.pdf (p. 47) - Closures and Scope > shadowy variables from a shadowy planet
- raw/javascriptallonge.pdf (p. 47) - Closures and Scope > shadowy variables from a shadowy planet
- raw/javascriptallonge.pdf (p. 47) - Closures and Scope > shadowy variables from a shadowy planet
- raw/javascriptallonge.pdf (p. 47) - Closures and Scope > shadowy variables from a shadowy planet
- raw/javascriptallonge.pdf (p. 47) - Closures and Scope > shadowy variables from a shadowy planet
- raw/javascriptallonge.pdf (p. 47) - Closures and Scope > shadowy variables from a shadowy planet
- raw/javascriptallonge.pdf (p. 47) - Closures and Scope > shadowy variables from a shadowy planet
- raw/javascriptallonge.pdf (p. 47) - Closures and Scope > shadowy variables from a shadowy planet
- raw/javascriptallonge.pdf (p. 47) - Closures and Scope > shadowy variables from a shadowy planet
