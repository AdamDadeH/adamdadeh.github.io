---
title: Convolutions
author: Adam Henderson
layout: post
use_math: true
category: Math
tags: Math Analysis
---

These are quick notes on convolutions, their generalizations, and their relationship to Fourier transforms.

[Convolution (Wikipedia)](https://en.wikipedia.org/wiki/Convolution#Convolutions_on_groups)

Familiar Convolutions
-----

**Def: Discrete Convolution**

For functions $f, g : \mathbb{Z^m} \to \mathbb{C}$

The convolution is given by

\begin{equation}(f * g)(x) = \sum_{y \in \mathbb{Z^m}} f(y)g(x-y)\end{equation}

This is familiar from convolutional neural networks and discrete signals analysis.

**Def : Real convolution**
For $f, g : \mathbb{R} \rightarrow \mathbb{C}$ we can define their convolution $f * g$ by

\begin{equation}
(f * g)(x) = \int dy f(y)g(x - y)
\end{equation}

Familiar convolution appearing in real analysis, addition of random variables, ..

**Def : Group Convolution**
For a group $G$, functions $f, g : G \rightarrow \mathbb{C}$ and a measure $\mu$ on $G$.

\begin{equation}(f * g)(x) = \int d\mu(y) f(y)g(y^{-1}x)\end{equation}

The key components of these definitions are
* Two functions $f,g$ with a common domain $X$.
* A binary operation defined on $X$.
* A measure defined on $X$ (free when X is discrete)

We can then define convolution with respect to that binary operation and measure.

General Convolution for Binary Operation
-----

**Def : Binary Operation convolution**
For $f, g : M \rightarrow \mathbb{C}$, a measure $\mu$ on $M$, and a binary operation $b : M \times M \rightarrow M$.
\begin{equation}(f *_{b,\mu} g)(z) = \int d\mu(x) d\mu(y) f(x)g(y)\delta(z, b(x,y))\end{equation}

with $\delta(x,y)$ the dirac delta distribution, $\int d\mu(x) f(x) \delta(x,y) = f(y)$

For our real convolution this reduces to the expected:

\begin{equation}(f *_{+,\mu_L} g)(z) =\int dx f(x)g(y)\delta(z-x-y) = \int dx f(x)g(z-x)\end{equation}

For a group :

\begin{equation}(f *_{\cdot,\mu} g)(z) =  \int d\mu(x) d\mu(y) f(x) g(y) \delta(z, xy)\end{equation}

With a change of variables $y = x^{-1}y'$ (assuming the measure is invariant under group action)

\begin{equation}
\int  d\mu(x) d\mu(y') f(x) g(x^{-1}y') \delta(z, y') = \int  d\mu(x)  f(x) g(x^{-1}z)
\end{equation}

Example
---

**Dirichlet Convolution** is an example where the binary operation does not define a group.

Taking domain $\mathbb{N}$ and integer multiplication

\begin{equation}
(f * g)(n) = \sum_{m \in \mathbb{Z}} \sum_{d \in \mathbb{Z}} f(d)g(m) \delta(n, md)
\end{equation}

For a fixed $d$ the delta is non-zero if $d$ divides $n$

\begin{equation}
(f * g)(n) =  \sum_{d | n} f(d)g(n/d)  
\end{equation}

Properties
---

1. Linear in both $f$ and $g$
2. Is commutative and/or associative if the binary operation is.

More General Convolution
----

**Def: External Binary Operation Convolution**

Given an external binary operation from $e: K \times X \to X$.

Given a measure $\nu$ on $K$ and a measure $\mu$ on $X$.

\begin{equation}(f *_{e,\nu,\mu} g)(y) = \int d\nu(k) d\mu(x) f(k)g(x)\delta(y, b(k,x))\end{equation}

Familiar Example : Graph Convolution

Given a graph $G$

Fourier Transform
-----

For $*_{+,\mu_{L}}$ on $\mathbb{R}$ we have the nice property that

\begin{equation}\widehat{f*g}(\omega) = \widehat{f}(\omega)\widehat{g}(\omega)\end{equation}

there is an interplay between convolution and the fourier transform.

When is such an identity satisfied for a transform $f(\rho) = \int dx \rho(x) f(x)$?

\begin{equation} \int dz \int dx dy \rho(z) f(x)g(y) \delta(z = b(x,y)) = \int dx f(x) \rho(x) \int dy \rho(y) g(y).\end{equation}

Clearly this holds if $\rho(b(x,y)) = \rho(x) \rho(y)$ or if we have a one dimensional representation of the binary operation $b$.



For the group convolution - $*_{\cdot, \mu}$ - the convolution theorem involves the irreducible
representations of the group (often with dimension $\geq 2$.).

$(f * g)(\rho) = f(\rho)g(\rho)$

where the Fourier transform is matrix valued and on the right we have the matrix product.

External Action Transform
----

For the external binary operation is something similar available?

Consider a representation of the external binary operation to be a pair

\begin{equation}\phi : X \rightarrow V\end{equation}

\begin{equation}\rho : K \rightarrow GL(V)\end{equation}

$\phi$ a mapping of each $x\in X$ to a vector and $\rho$ a mapping of $k \in K$ to a linear map (matrix) on the vector space.

Such that

\begin{equation}\phi(e(k, x)) = \rho(k) \phi(x)\end{equation}

For this to be a faithful representation - we need to place restrictions on the external binary operation?

Given a function $f : X \to \mathbb{C}$ and $g: K \to \mathbb{C}$ we have

f(\phi) = \int dx f(x) \phi(x)
g(\rho) = \int dk g(k) \rho(k)

\begin{equation}(g * f)(\phi) = \int dy (g * f)(y) \phi(y)\end{equation}

\begin{equation} = \int dy \int dk \int dx g(k) f(x) \delta(y = e(k,x)) \phi(y)\end{equation}

\begin{equation} = \int dk \int dx g(k) f(x) \phi(e(k,x))\end{equation}

\begin{equation} = \int dx \int dy g(k) f(x) \rho(k) \phi(x) \end{equation}

\begin{equation} = g(\rho) f(\phi)\end{equation}

How fun :D  
