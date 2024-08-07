---
title: "Function Notation : Evaluation"
layout: post
author: Adam Henderson
category: Math Notation
use_math: true
---

"What is the most efficient notation?" is a recurring question when I read math, machine learning, or other technical publications. Which is followed by the debate of working with the default syntax of the text - or mapping to my own preferred syntax.

For example : Do we convert expressions in "convential matrix notation" $A^TBv$ into abstract index notation $A_{ba} B_{bc} v_c$?

Given the repetition of the question and redundant efforts I want to collect observations on syntax to streamline this debate. I'm also inspired by deeper investigations into syntax from likes of Djikstra ([On Notation](https://www.cs.utexas.edu/users/EWD/ewd09xx/EWD950a.PDF) and [Adopted Notation](https://www.cs.utexas.edu/users/EWD/ewd13xx/EWD1300.PDF)), Knuth, and Iverson.

I'll start with the most recent obsession of syntax for functions. There are a few types of function notation that frequently occur : 

* Evaluating a function $f$ at a value $x$.
* Function composition - applying function $g$ to the output of $f$.
* Expressing "$f$ is a function from $X$ to $Y$".
* Expressing the set of all functions $X$ to $Y$.
* Currying 

To keep this short I'll focus further on function evaluation.

# **Notations for Function Evaluation :**

Function evaluation, or applying a function to an input, can be expressed in various ways, each with specific advantages and context-dependent appropriateness.

## Univariate

- **Bracketed** : 
    - $f(x)$ : Common notation for math & most programming languages.
    - $f[x]$ : Array access in programming languages, some use for functions whose domains are spaces of functions.

- **Subscript/Superscript** : $f_x$/$f^{x}$
    - Coordinates of a vector -  $v_i$
    - Element of a sequence - $x_n$

- **Dijkstra period**: $f.x$

- **Juxtaposition** : $fx$
    - Category theory as application of Functor - $Sf$
    - Linear Algebra : $Ax$ for matrix $A$, vector $x$.

- **Function Application** : 
    - `apply(f, x)`
    - **Lisp Style :** `(f x)`

## Why So Many?

Why can't we just pick one and standardize? The "best" notation depends on context. The key properties to balance are :

*Reading Time* as driven by ambiguity of parsing, ease of parsing, reliance on context and backtracking, amount of redundancy,consistency with notation in
related domains, and character count. These are in order of importance (to me)
with character count being *dangerous* to directly optimize for and unambiguous parsing being table stakes.

*Ease of Manipulation* : Does the syntax make it easier to perform common
transformations / calculations?

## My current viewpoint 

Adopted : A mixed use of parentheses $f(x)$ and subscript/superscript.

Avoiding : Juxtaposition, Mixing $f(x)$ and $g[x]$.

## Multivariate

- **Comma Delimited** : 
	- $f(x,y)$, $f_{x,y}$
	- Standard notation emphasizing the function's domain as a product space, $f : X_1 \times X_2 .. \to Y$

- **Parentheses w/ Different Delimiter :**
    - Vert - Conditional Probability (single param, single variable case) : $P(x \vert \phi)$
    - Semicolon - May be used to separate variables from fixed parameters - [link](https://en.wikipedia.org/wiki/Semicolon#:~:text=Mathematics,-In%20the%20argument&text=%2C%20a%20semicolon%20may%20be%20used,coordinate%20associated%20with%20that%20index.) - $f(x;y)$
      
- **Curry Everything :** $f(x)(y)$  
- **Lisp Style :** `(f x y)`
- **Mixed Syntax :**
	- $f_i(x)$
	- $\rho_{\theta}(x \vert \mu)$

## Equivalent Spaces of Functions but Different Emphasis

The different notations for multivariate functions emphasize different
isomorphic spaces of functions. The set of functions $f: X \times Y \to Z$ 
is equivalent to the set of functions $f: X \to (Y \to Z)$ or $f: Y \to (X \to Z)$. 
Each is tied to a family of notations for multivariate functions.

 * Comma delimited $f(x,y)$ => $f: X \times Y \to Z$
 * Currying $f(x)(y)$ => $f: Y \to (X \to Z)$
 * Parameters $f(x ; y)$ => $f: Y \to (X \to Z)$

 Mixed syntax behaves similar to currying

 * Vector valued function $v_i(x)$ => $v : X \to (I \to Y)$

The variety of syntax is valuable to emphasizing different isomorphic but
practically different representations.

## Positional vs Named Inputs

In function notation, distinguishing between positional and named inputs can significantly affect readability and clarity. The distinction of named and positional inputs is more common in programming where nearly everyone gets burned by positional arguments.

Positional Inputs:

 - Example: $f(2, 3, "Fred")$ - Inputs are provided directly in the order the function expects them.
 - Advantage: Conciseness and ease of writing.
 - Disadvantage: Can lead to confusion without clear documentation, as the meaning of each position must be remembered or looked up.

Named Inputs:

 - Syntax: $f(x=2, y=3, cat="fred")$ - Each argument is explicitly named.
 - Advantage: Enhances readability and self-documentation, especially in functions with many parameters or optional parameters.
 - Disadvantage: More verbose, can lead to cluttered expressions in complex formulas.

## Special Cases

There are functions that occur so commonly in their associated domain they get
special compact syntax. For example there is a wide variety of two arguments functions which use bracket syntax without a function `name`
 * Norms : $\vert x\vert$, $\vert \vert x \vert \vert$
 * Brackets : Commutator $[x,y]$, Poisson $\\{x,y\\}$
 * Inner products : $(x, y)$, $\langle x \vert y \rangle$.

Infix notation ($x+y$, $f \circ g$) is especially valuable for associative binary operations where $+(x, +(y, +(z, w))))$ is awful, but $x + y + z + w$ 
is easy to read.

There is similarly a large family of unary functions that occur commly enough to show up as little "decorations" on the arguments ($\bar{x}$, $x^*$, $x^{\dagger}$). These are most common in "involutions" where are their own inverse, so that painful expression like $x^{\dagger \dagger \dagger}$ don't occur.

## Conclusion

The choice of function notation depends on several factors including readability, ease of manipulation, and the specific mathematical or programming context. I am comfortable with the wide variety of syntax in this case as each emphasizes different ways to represent functions
or is valuable in different contexts.


