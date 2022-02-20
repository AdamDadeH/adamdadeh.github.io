---
title: "Coordinates"
layout: post
author: Adam Henderson
category: Math
use_math: true
---

**Coordinates**. A word so common that I rarely (perhaps never) consider how it is defined. In the following I browse common definitions & their ambiguity, propose definitions that capture standard types of coordinates.

Common Definitions
------------------

First, browsing definitions from standard sources:

[Coordinates (wikipedia)](https://en.wikipedia.org/wiki/Coordinate_system)

>In geometry, a coordinate system is a system that uses one or more numbers, or coordinates, to uniquely determine the position of the points or other geometric elements on a manifold such as Euclidean space ... The coordinates are taken to be real numbers in elementary mathematics, but may be complex numbers or elements of a more abstract system such as a commutative ring.

[Coordinates (encyclopedia of math)](https://www.encyclopediaofmath.org/index.php/Coordinates)

> Numbers, quantities, used to specify (or determine) the position of some kind of element (point) in a collection (a set M), e.g. on a plane or a surface, in a space, on a manifold.

[Coordinates (Wolfram Mathworld)](https://mathworld.wolfram.com/CoordinateSystem.html)

> A system for specifying points using coordinates measured in some specified way.

Perhaps unsurprisingly the definitions are ambiguous. It is likely with more digging I'll find the right definition. In the meantime it is amusing to construct my own.

First Definition
----------------

**Broadest Def** : A set of coordinates for a set $X$ is any pair of $(f, C)$ with $f$ a bijection, $f : X \rightarrow C$.

Where

* The set $X$ : Points to be "specified".
* The set $C$ : "Quantities" or "numbers" used to specify.
* $f$ : The process of uniquely identifying a point.

While accurate - this is broad enough to cover **nearly anything**. For example this degenerate / trivial case : $(X, i_X)$ is a set of coordinates for $X$, where $i_X$ is the identity function on X.

Clearly from experience there are "better" coordinates than others, so what distinguishes different choices of coordinates? From my perspective better is defined with respect to a specific structure defined on the set $X$ - such a binary operation, an inner product, or function.

Examples of Nice
--------
Let's consider situations where we have coordinates that simplify problem solving, computation, and theorem proving.

#### Linear Algebra

Given a finite dimensional (complex) vector space $V$ with a linear map, $A : V \rightarrow V$ we can choose a basis (coordinates) where $A$ is diagonal.

Coordinates :

* Coordinate set : $\mathbb{R}^n$
* Coordinate map : $f : V \rightarrow \mathbb{R}^n$ such that $f(Av)_i = \lambda_i f(v)_i$

Using this choice of coordinates/basis it is simpler to evaluate powers $A^n$ by taking powers of the diagonal values (eigenvalues). It further simplifies working with
more general functions of $A$.

Simplified Operations :

* $f(A^m v)_i$ = $(\lambda_i)^m f(v)_i$
* For more general functions $F$ the linear map: $f(F(A)v) = F(\lambda_i)f(v)_i$

#### Integer Arithmetic and Positional Representations

A familiar choice of coordinates for natural numbers $\mathbb{N}$ are decimal, binary, or other positional representations. For base $n$ we have a bijection between $\mathbb{N}$ and coordinate set $\prod_{i=1}^{\infty} [0, n-1]$ given by the map to digits $d_i(x)$.

With this representation there is the simple and familiar expression for addition ([Binary addition](https://en.wikipedia.org/wiki/Adder_(electronics))).

#### Integer Arithmetic and Prime Factors

A distinct choice of coordinates for $\mathbb{N}$ comes from prime factorization, $n = 2^{m_2} 3^{m_3} 5^{m_5}\dots = \prod_{p \,\rm{prime}} p^{m_p}$. This gives a unique bijection between the natural numbers $\mathbb{N}$ and the prime powers, $\prod_p \mathbb{N}$.

This set of coordinates has it's own simple operations.

* Multiplication : Given simply by addition of exponents $m_2 + m'_2$, ..
* Divisibility : n divides n' iff $m_p \leq m_p'$ for all $p$
* Is square? : $m_p$ even for all primes $p$.

#### Representation of Groups

For a faithful group representation we have coordinates given by the bijection $$\rho : G \rightarrow \mathbb{C}^{(n \times n)} $$ such that the image of the group binary operation is a simple quadratic function.

Given $g$ & $h$ in $G$,

\[
\begin{equation}
\rho(gh)_{ij} = \sum_k \rho(g)_{ik} \rho(h)_{kj}
\end{equation}
\]

Or more simply stated : That the image of the groups binary operation is the matrix product.

## What Defines Nice?

For each of the above we have a set $X$ with *structures* ([structure](https://en.wikipedia.org/wiki/Mathematical_structure) and the more familiar [algebraic structures](https://en.wikipedia.org/wiki/Algebraic_structure)) and the desire to find coordinates that make it easier to work with those structures.

*example structures*

* binary operations : $h : X \times X \rightarrow X$
* n-ary operations : $h : X^n \rightarrow X$
* functions $g : X^n \rightarrow Y$
* Subsets $U$ of $X$ which can be identified by indicator functions on $X$, $I_U : X \rightarrow \{0, 1\}$
* Marked points of $X$,  $m : 1 \rightarrow X$
* binary relations on $X$ which as subsets of $X \times X$ be identified with maps $R: X \times X \rightarrow \{0, 1\}$

For simplicity (and because it appears to cover the use cases of interest) I will restrict to *structures* that are given by functions $\phi : X^d \times Y \rightarrow X^r \times Z$ where $d,r$ can be zero and $Y$, $Z$ can be one element sets.

Nice coordinates for a set $X$ with a set of structures $\phi$ are $(f, C, \psi)$ with
* $C$ a set
* $\psi$ is a set of structures defined on $C$
* $f : X \rightarrow C$ a bijection

such that the image of each structure $\phi_i$ on $X$ in $C$ can be efficiently represented using the structures $\psi$ on $C$. Where the condition on the representation $(f \cdot \phi_i) : C^d \times Y \rightarrow C^r \times Z$ for a particular structure $\phi_i: X^{d} \times Y \rightarrow X^r \times Z$ is that

\[
\begin{equation}
(f \times f \times .. \times i_Z) (\phi_i(x_1, x_2, ...,x_d, y))) = (f\cdot\phi)_i (f(x_1), f(x_2), ..., f(x_d), y)
\end{equation}
\]

where $(f \cdot \phi)$ is a composition of the structures $\psi$ on $X$.

Example : Binary Operation
----

Given the single structure $b : X\times X \rightarrow X$.

Coordinates for $(X, b)$ are $(f, C, \psi)$ such that -
$f(b(x, x')) = (f \cdot b)(f(x), f(x'))$ where $(f \cdot b)$ defined by composition of $\psi$.

For group representations or more generally group morphisms  $(f \cdot b)$ is given by the binary operation on $C$.

\[
\begin{equation}
f(b(x, x')) = \psi_b(f(x), f(x'))
\end{equation}
\]

Efficiently?
-------------

Cheated above with the word "efficiently". The only means I currently have to approach that is to consider a cost associated with each use of structure $\psi_i$ given by $c_i$. With that we could generate an overall cost $c(\phi_i, f, C, \psi)$ of evaluating $\phi$ in the chosen
coordinates to be the sum of the costs of the structures used. Clearly depends on the choice of representation of
$(f \cdot \phi_i)$ as a composition of structures $\psi$, so in practice we can find upper bounds.

With this we have collided with the problem of evaluating algorithmic complexity. We also realize that the above discussion precisely covers the case of implementing an algorithm using the family of elementary functions available each with their own cost / complexity.

Conclusion
---------

We conclude for now having made some progress.

* There exists an obvious definition that is too broad to be of value.
* Recognizing that what are good coordinates depend on the common operations/structures you are using.
* Having a (still rough) formulation the problem of coordinates in terms of representation of structures.
* Realizing the connection between the concepts "coordinates" and "implementation" of an algorithm in a particular language.

I expect to return to this topic to further investigate

* The question of efficiency of representation.
* The relationship of nice coordinates to machine learning - which intuitively relates to what structures are natural to work with in the choice of coordinates and do they allow for optimization over the space of possible composition of structures.
