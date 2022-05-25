---
- author: adamhenderson
- date: 2019-08-25
---

Convolutions
==========

Quick notes on convolutions and their relationship to fourier transforms.

[Convolution (Wikipedia)](https://en.wikipedia.org/wiki/Convolution#Convolutions_on_groups)

Familiar Convolutions
---

**Def : Real convolution**
For $f, g : \mathbb{R} \rightarrow \mathbb{C}$ we can define their convolution $f * g$ by

$$
(f * g)(x) = \int dy f(y)g(x - y)
$$

**Def : Group Convolution**
For a group $G$, functions $f, g : G \rightarrow \mathbb{C}$ and a measure $\mu$ on $G$.
$$(f * g)(x) = \int d\mu(y) f(y)g(y^{-1}x)$$

The key components of these definitions are
* Two functions $f,g$ with a common domain $X$.
* A binary operation defined on $X$.
* A measure defined on $X$.

We can then define convolution with respect to that binary operation and measure.

General Convolution for Binary Operation
-----

**Def : Binary Operation convolution**
For $f, g : M \rightarrow \mathbb{C}$, a measure $\mu$ on $M$, and a binary operation $b : M \times M \rightarrow M$.
$$(f *_{b,\mu} g)(z) = \int d\mu(x) d\mu(y) f(x)g(y)\delta(z, b(x,y))$$

For our real convolution this reduces to the expected:

$$(f *_{+,\mu_L} g)(z) =\int f(x)g(y)\delta(z-x-y) = \int f(x)g(z-x)$$

For a group :

$$(f * g)(z) =  \int d\mu(x) d\mu(y) f(x) g(y) \delta(z, xy)$$

With a change of variables $y = x^{-1}y'$ (assuming the measure is invariant under group action)

$$\int  d\mu(x) d\mu(y') f(x) g(x^{-1}y') \delta(z, y') = \int  d\mu(x)  f(x) g(x^{-1}z)$$

Example
---

**Dirichlet Convolution** is an example where the binary operation does not define a group.

Taking domain $\mathbb{N}$ and integer multiplication

$$
(f * g)(n) = \sum_{m \in \mathbb{Z}} \sum_{d \in \mathbb{Z}} f(d)g(m) \delta(n, md)
$$

For a fixed $d$ the delta is non-zero if $d$ divides $n$

$$
(f * g)(n) =  \sum_{d | n} f(d)g(n/d)  
$$

Properties
---

1. Linear in both $f$ and $g$
2. Is commutative and/or associative if the binary operation is.

Fourier Transform
-----

For $*_{+,\mu_{L}}$ on $\mathbb{R}$ we have the nice property that

$$\widehat{f*g}(\omega) = \widehat{f}(\omega)\widehat{g}(\omega)$$

there is an interplay between convolution and the fourier transform.

When is such an identity satisfied for a transform $f(\rho) = \int dx \rho(x) f(x)$?

$$ \int dz \int dx dy \rho(z) f(x)g(y) \delta(z = b(x,y)) = \int dx f(x) \rho(x) \int dy \rho(y) g(y).$$

Clearly this holds if $\rho(b(x,y)) = \rho(x) \rho(y)$ or if we have a one dimensional representation of the binary operation $b$.



For the group convolution - $*_{\cdot, \mu}$ - the convolution theorem involves the irreducible
representations of the group (often with dimension $\geq 2$.).

$(f * g)(\rho) = f(\rho)g(\rho)$

where the Fourier transform is matrix valued and on the right we have the matrix product.
