---
layout: post
title: Symmetries in Machine Learning I
use_math: true
---

In this digression into the topic of symmetries in Machine Learning we

* define invariance and covariance of supervised ML under a family of transformations.
* present a simple idealized supervised learning problem with symmetries to explore the concept.

This investigation is inspired by [Invariant Information Clustering](https://arxiv.org/abs/1807.06653) in which the concept that a model should be invariant under certain transformations is leveraged for unsupervised learning.

### Exact Symmetries in ML

Simple **Supervised machine learning** tasks can be classified by

* **Domain** $X$ - or the function **inputs**
* **Range** $Y$ - or the function **outputs**

A particular instance of a task consists of

* A set of observations of input, output pairs. $\mathcal{D} \subset X \times Y$
* **Cost function** defined given a candidate function $f: X \rightarrow Y$ and a probability distribution on $X \times Y$ (typically defined by observed data). $C : (X \rightarrow Y) \times \mathcal{P}(X \times Y) \rightarrow \mathbb{R}$

  _We say 'simple' here as there are plenty of cases where observations are from $X \times Y$ while the function to learn has a different range $Y'$. The most common example being Logistic regression where the observations are from a discrete set $L$ and the function output is a probability distribution over $L$._

Symmetries are typically observed for tasks where the domain $X$ has
**transformations**, $\phi_{\alpha} : X \rightarrow X$, such that either

a. The outputs are **invariant** under transformation of the inputs by $\phi_{\alpha}$, so the outputs $y$ associated to $x$ and $\phi_{\alpha}(x)$ would be the same for all $\alpha$.

b. The outputs are **covariant** under under $\phi_{\alpha}$ - which qualitatively means that the outputs associated to $x$ and $\phi_{\alpha}(x)$ are related in a known way.

Denoting our symmetry actions $\phi_{\alpha} : X \rightarrow X$ by $\phi_{\alpha} \cdot x$ we have the requirements that the optimal $f$ given the cost
function should satisfy.

1. **Invariance** :
  $f(\phi_{\alpha} \cdot x) = f(x)$ for all $\alpha, x$
2. **Covariance** : There exists a function $G$ taking transformation of $X$ and producing a transformation of $Y$ - $G : (X \rightarrow X) \rightarrow (Y \rightarrow Y)$ such that it
  - **Defines transformation of outputs** : $f(\phi_{\alpha} \cdot x) = G(\phi_{\alpha}) \cdot f(x)$ for all $\alpha, x$
  - Is a **Functor** : $f(\phi_{\alpha} \cdot (\phi_{\beta} \cdot x)) = G(\phi_{\alpha} \cdot \phi_{\beta}) \cdot f(x) = G(\phi_{\alpha}) \cdot G(\phi_{\beta}) \cdot f(x)$ for all $\alpha, \beta, x$

Such exact symmetries are rare in practice but idealized versions of standard problems do admit exact symmetries.

**Idealized Images** : If we remove questions of "what happens at the boundary", allowing images composed of pixels that are infinite (functions $\mathbb{Z}^2$ to $\mathbb{R}^3$). Then we expect:
  - **Classification** of image content to be **translation invariant**.
  - Detection of **bounding boxes** to be **translation covariant** with the bounding box being translated along with the image.
  - **Classification** to be **dilation invariant** where we allow transformations that take each pixel and "blow it up" to a $K \times K$ square of pixels of
  identical color.

Once we introduce image boundaries we are reduced to having "near" or
"approximate" symmetries that will be discussed another time.

### Simple Idealized Example

A **highly** idealized example that is similar to image models takes as domain $X$
functions from [The cyclic group](https://en.wikipedia.org/wiki/Cyclic_group) $\mathbb{Z}_N$ (addition mod N) to $\mathbb{Z}_2$.

- **Domain** $X$ : $\mathbb{Z}_N \rightarrow \mathbb{Z}_2$
  - Interpretation : Finite strings of bits.
- **Range** $Y$ : Any
- **Group of Transformations** : Self-Group action of $\mathbb{Z}_N$
    - For $n \in \mathbb{Z}_N$ define $(\phi_n \cdot x)(m) = x(m - n)$
    - Interpretation : Translation with [periodic boundary conditions](https://en.wikipedia.org/wiki/Periodic_boundary_conditions).

Suppose we have domain expert knowledge that the task is
exactly invariant with respect to the transformations - how
do we incorporate that knowledge? Can we directly work with
functions $f: (\mathbb{Z}_N \rightarrow \mathbb{Z}_2) \rightarrow \mathbb{R}$ that were invariant under the group of transformations?

$$f(\phi_n \cdot x) = f(x) \;\rm{for}\;\rm{all}\; n \in \mathbb{Z}_N$$

What do these invariant functions look like?

#### Exploring Invariant Functions

If $f(x) = f(\phi_n(x))$ for all $n$ then clearly it is sufficient
to specify $f$ for any single element of the following subset of $X$,

$$[x] = \{\phi_n(x) | n \in \mathbb{Z}_N\}$$

to know the value of $f$ on the entire subset. This set consists of
all possible translations / transformations of the element $x$.

For $N=3$ and writing the input $x$ as a string of bits - $[101] = \\\{ 101, 011, 110 \\\}$

Each such subset is called an equivalence class under $\sim_\phi$ and we denote the set of these equivalence classes as $X/\sim_{\phi}$.
One avenue to understanding the invariant functions is to
directly define the functions on $X / \sim_{\phi}$  (typically called the
quotient of $X$ with respect to $\sim_{\phi}$).

For our simple example it is amusing to note that these equivalence classes are
called "Necklaces" [necklaces - mathworld](http://mathworld.wolfram.com/Necklace.html) and have been actively studied within [combinatorics](https://oeis.org/A000031) - where the primary object of study is the number of distinct equivalence classes. This also hints that the study of these objects is non-trivial!

For different $N$ we can write down representatives of the equivalence
classes.

* $N=1$: `0`, `1`
* $N=2$: `00`, `10`, `11`
* $N=3$: `000`, `100`, `110`, `111`
* $N=4$: `0000`, `1000`, `1100`, `1010`, `1110`, `1111`
* $N=5$: `00000` ,`10000`,  `11000`,  `10100`, `11100`, `10110`, `11110`,`11111`
* $N=6$:  `000000`, `100000`, `110000`, `101000`, `100100`, `111000`, `110100`, `110010`, `111111`, `011111`, `001111`, `111010`, `011011`, `101010`

With access to these it is possible to define a general invariant function
by assigning a value $f([x])$ to each equivalence class $[x]$ and then
generally we have $f(x) = f([y])$ if $x \in [y]$. While this allows us
to construct invariant functions they are not pleasant or efficient to work with.

With this understanding one can imagine taking each observation $(x, y)$
and mapping to $([x], y)$, so using $\mathcal{D}' = \\\{ ([x], y) \vert (x,y) \in \mathcal{D} \\\}$ as training data.

1. Efficiently determining which equivalence class the input $x$ belongs to may be burdensome.
2. Where elements of $X$ could be simply expressed as elements of $\mathbb{Z}^N_2$ providing simple coordinates (features) and so a means to define a parametrized family of functions $\phi_{\alpha}$ to optimize over - the quotient $X / \sim_{\phi}$ does not have such obvious coordinates.

#### Equivalence classes of $\mathbb{Z}_N \rightarrow \mathbb{R}$

Given that the boolean case reduces to a complex combinatorics
problem - we can look at a slightly simpler case.
For functions $\mathbb{Z}_N \rightarrow \mathbb{R}$
what do the quotients look like?

The 'largest' part of the quotient can be obtained for all functions having unique maximum. We can qauntify largest using the standard
measure on $\mathbb{R}^N$. Denoting the function with unique maximum
as $A_{unique}$ - we note that the complement $\mathbb{R}^{N} - A_{unique}$ is contained in $\\\{x \vert \exists n,m \;\rm{st}\; x(n)=x(m)\\\}$.

So $\mu(\mathbb{R}^{N} - A_{unique}) \leq \mu(\\\{x \vert \exists n,m \;\rm{st}\; x(n)=x(m)\\\}) = 0$

The complement of our set of functions with unique maximum is measure 0.

For any element $x$ with unique maximum we can rotate until the maximum is at 0. Any such $x$ is equivalent to an element of the set of functions with unique maximum at 0, $\\\{x  \vert x(0) > x(n) \forall n \neq 0\\\}$.

We can rather compactly describe the quotient as,  $\cup_y \\\{y\\\} \times [-\infty, y)^{n-1}$.
