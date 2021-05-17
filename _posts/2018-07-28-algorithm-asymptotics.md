---
title: "Asymptotic Notation as Equivalence Relation"
layout: post
started: 2016-07-28
use_math: True
---

In lazily paging through [Cormen et al](https://mitpress.mit.edu/books/introduction-algorithms) 
I noticed that I have never seriously thought about the mathematical 
properties of the [asymptotic notations](https://en.wikipedia.org/wiki/Big_O_notation#Family_of_Bachmann.E2.80.93Landau_notations) used in analyzing the behavior of algorithms ($O$,$\Omega$,$\Theta$).
In particular I was curious about their properties as [binary relations](https://en.wikipedia.org/wiki/Binary_relation).

### As Binary Relations

Big-$$O$$ notations defines relationships between functions - in particular focusing on the
comparing the asymptotic behavior. The definitions are as follows.

$$
\begin{equation}
f \in O(g) \;\rm{if}\; \exists k>0 \; \rm{and} \; \exists n_{0} \; \rm{such} \; \rm{that} \; \forall n>n_{0}, \; f(n)\leq k\cdot g(n) 
\end{equation}
$$

$$
\begin{equation}
f \in \Omega(g) \;\rm{if}\; \exists k>0 \; \rm{and} \;\exists n_{0} \; \rm{such} \; \rm{that} \; \forall n>n_{0}, \; f(n)\geq k\cdot g(n)
\end{equation}
$$

$$
\begin{equation}
f \in \Theta(g) \; \rm{if} \; \exists k_1,k_2>0 \; \rm{and} \; \exists n_{0} \; \rm{such} \; \rm{that} \; \forall n>n_{0}, \; k_1\cdot g(n) \geq f(n)\geq k_2\cdot g(n)
\end{equation}
$$

Where I am restricting the definition to non-negative functions 
$\mathbb{N} \rightarrow \mathbb{R}$, which we can compactly denote 
$\mathbb{R}_{\ge 0}^\mathbb{N}$.

These 3 satisfy the conditions of an [equivalence relation](https://en.wikipedia.org/wiki/Equivalence_relation), $\Theta$, and a [pre-order](https://en.wikipedia.org/wiki/Preorder) $O$ or $\Omega$ (or a [partial
ordering](https://en.wikipedia.org/wiki/Partially_ordered_set) relative to the equivalence relation $\Theta$). As such it tempting to use binary relation notation, $f\;O\;g$ for $f \in O(g)$, 
$f \;\Omega\; g$ for $f \in \Omega(g)$ and $f \;\Theta\; g$ for $f \in \Theta(g)$.

Equivalence relation conditions
1. Reflexive : $f\;\Theta\;f$
2. Symmetric : $f\;\Theta\;g$ implies $g\;\Theta\;f$
3. Transitive : $f\;\Theta\;g$, $g\;\Theta\;h$, implies $f\;\Theta\;h$

Pre-Order relations hold for either $O$ or $\Omega$ so we restrict to $O$.
1. Transitive : $f\;O\;g$, $g\;O\;h$ implies $f\;O\;h$
2. Reflexive : $f\;O\;f$
3. Anti-symmetric (wrt $\Theta$) : $f\;O\;g$, $g\;O\;f$, implies $f\;\Theta\;g$

### Pre-Order

Why only a pre-order or partial order? We can easily construct functions for
which neither $f\;O\;g$ or $g\;O\;f$. Let $f(n)=n$ for all positive integers.
Let $g(n) = log(n)$ for all odd positive integers and $g(n)=n^2$ for all even 
positive integers. Then for any choice of constant $$k$$ and for any $N_o$$ there
exists $n,m > N_o$ such that $f(n) > k g(n)$ and $g(m) > k f(m)$, so neither
$f \; O \; g$ nor $g \; O \; f$. These two functions are incomparable. 

This pre-order is not totally wild - it is a directed pre-order. Given functions
$$f,g$$ we can define $h(n) = \max(f(n),g(n))$. Then $f \; O \; h$ and $g \; O \; h$ making $O$
a [directed pre-order](https://en.wikipedia.org/wiki/Directed_set).

### Equivalence Classes of $$\Theta$$

Given that $$\Theta$$ is an equivalence relation what does the quotient look like? 
The quotient \mathbb{R}_{\ge 0}^\mathbb{N} / \Theta$$ has some very familiar elements.
There are elements of the quotient that are very familiar

0. $$\Theta(1)$$ - which includes all bounded functions.
1. $$\Theta(n^a)$$ for $$a > 0$$
2. $$\Theta(\log(n)^a)$$ for $$a > 0$$
3. $$\Theta(e^{a\cdot n})$$ for $$a > 0$$

For 1, 2, and 3 there is an independent element of the quotient for each $$a > 0$$.
With just these elements and their products we already have fairly large quotient space.

How do the operations of the original function space descend to the quotient? For addition
there are 2 cases, $$f\;O\;g$$, $$f\;Theta\;g$$ that we can handle easily.

1. For $$f\;O\;g$$, $$\Theta(f) + \Theta(g) = \Theta(g)$$
2. For $$f\;\Theta\;g$$, $$\Theta(f) + \Theta(g) = \Theta(f)$$ (or g).

This is the operation Max with respect to the ordering $$O$$. If the two elements are not 
comparable there is nothing I can easily infer about $$\Theta(f) + \Theta(g)$$. 

For multiplication we remain close to original spirit of the operation with $$\Theta(f)\cdot\Theta(g) = \Theta(f\cdot g)$$ 
being a well defined product on the equivalence classes. This product has an identity $$\Theta(1)$$.
Together we have a Max-Times algebra with respect to the partial-ordering $$O$$.

If we restrict to looking at product of the simple elements above - each element of that subspace 
can be encdoed as a vector of positive real values for powers of $$n$$, $$\log(n)$$, 
$$\log(\log(n))$$, .., $$e^n$$, On those elements the product reduces to vector addition of the powers
and addition reduces to the max operation with respect to a dictionary ordering of the vectors.
While this does describe the behavior of this particular subspace it does not tell the whole story.
For instance one would hope that nothing is living between the powers of $$\log(n)$$ and powers of $$n$$ but
the functions encoded by [L notation](https://en.wikipedia.org/wiki/L-notation) common in 
algorthmic number theory live exactly in that space.

$$\Theta$$ and limsup/liminf
--------------------

Note that

$$f \;\Theta\; g$$ implies that for some $$N$$, $$\beta g(n) < f(n) < \alpha g(n)$$ for all $$n > N$$.

This implies that

$$\rm{limsup} \;g/f$$ and $$\rm{liminf} \;g/f$$ are finite. ([liminf/limsup](https://en.wikipedia.org/wiki/Limit_superior_and_limit_inferior))

Conversely if $$\rm{limsup} \;g/f$$ and $$\rm{liminf} \;g/f$$ are each finite then for $$\epsilon > 0$$, $$\exists N$$ such
that $$M > N$$ implies that $$sup_{n > M} (g(n)/f(n)) < \beta + \epsilon$$ and $$inf_{n<>M} g(n)/f(n) > \alpha - \epsilon$$.

So $$g(n) / f(n) < \beta + \epsilon$$ for all $$n > N$$

and $$g(n) / f(n) > \alpha - \epsilon$$ for all $$n > N$$, thus $$f \;\Theta\; g$$.

Non-Comparable Pairs
--------------------

I am curious restriction we can make on the space of functions to remove the 
non-comparable pairs. Clearly restriction to monotonic functions removes the 
non-comparable pair introduced above.

More general asymptotics
---------------------

Thinking about asymptotic behavior as $$N \rightarrow \infty$$ makes me curious about more 
general definitions.

1. To say $$f(x) = O(g(x))$$ as $$x \rightarrow a$$ if $$limsup_{x \rightarrow a} f/g$$ is finite.

    $$\exists M > 0, \delta$$ such that 
    $$|f(x)| \leq M|g(x)|$$ 
    for $$0 < |x-a| < \delta$$
    so 

2. For a more general topology $$X$$ looking at the asymptotic behavior near 
    $$a \in X$$ we take open neighborhoods of $$U$$ of $$a$$.

    $$limsup_{x \rightarrow a} f = inf_{ U \ni a} \left[sup_{x \in U - \{a\}} f(x) \right]$$ 

    Allowing us to again say $$f(x) = O(g(x))$$ as $$x \rightarrow a$$ if $$limsup_{x \rightarrow a} f/g$$ is finite.
