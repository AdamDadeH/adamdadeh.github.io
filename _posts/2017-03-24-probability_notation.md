---
title: "Notation in Statistics"
layout: post
category: Statistics
use_math: True
---

*Notation is powerful*

"By relieving the brain of all unnecessary work, a good notation sets it free to concentrate on
more advanced problems, and, in effect, increases the mental power of the race." (Alfred North
Whitehead, “An Introduction to Mathematics”)

"Good notation can make the difference between a readable paper and an unreadable one."
Terence Tao [Use Good Notation](https://terrytao.wordpress.com/advice-on-writing-papers/use-good-notation/)

See also this collection of references and thoughts on notation [hypotext - notation](https://github.com/hypotext/notation)

A good notation will allow one to work more efficiently, convey ideas more concisely, and
lead to new developments. A poor notation acts as a friction to development and confines
our thoughts to old ways of thinking. At least for my personal use statistics notation has room for improvement - in particular the language of 'Random Variables' and 'Expectation Values'. A focus on random variables and expectation values :

* Can mask that probability measures are the critical component of the probability.
* Artificially restrict analysis to distributions on $$\mathbb{R}^n$$.

Probability is about Measures
===============================

Modern probability theory is commonly said to derive from the work of
[Kolmogorov](https://en.wikipedia.org/wiki/Andrey_Kolmogorov) who laid a foundation using measure theory. Probability theory requires an efficient languages for discussing the measurement of probabilities of subsets of a space of possibilities, which coincides
with the aims of measure theory. Measure theory is commonly introduced as a pre-requisite
to integration - a theory where we similarly require an means to measure the area / volume
of subsets of a space. Despite being entangled in how they are taught, measure theory
is a subject with value of its own beyond the theory of integration. In particular in
probability theory - measure theory is the star of the show and integration is at best a
useful tool.

Sample Spaces
-----------------------------------

In the language of measure theory a sample space is a *measurable space*
being a set $$X$$ equipped with a sigma algebra $$\Sigma$$.

A sigma algebra is a set of subsets of $$X$$ ($$\Sigma$$ is a subset of $$\mathcal{P}X$$
the Power set of $$X$$) such that :

0. $$\Sigma$$ contains the empty set $$\emptyset$$
1. $$\Sigma$$ is closed under complements. If $$A \in \Sigma$$ then $$X - A \in \Sigma$$.
2. $$\Sigma$$ is closed under countable unions. So given $$A_n \in \Sigma$$ for n indexed
by the natural numbers - then $$\cup_n A_n \in \Sigma$$.

From these we have other derived properties, $$X \in \Sigma$$ and $$\Sigma$$ is closed under
countable unions. This pair $$(X,\Sigma)$$ gives us the space of possible outcomes $$X$$
and the sets for which it is possible to define probability. The simplest examples make
this formal definition appear silly.

* *Finite Discrete* A Finite Set $$X=[1,2,3,...,n]$$ with $$\Sigma = P(X)$$ or
all subsets of $$X$$. The typical discrete sample space describing the states
of a n-sided die,, the states of a deck of cards, etc with all sets of states
measurable.
* [Borel Algebra](https://en.wikipedia.org/wiki/Borel_set) : The smallest sigma
algebra containing all open sets in a given topology. The Borel algebra for the
the standard topology on $$\mathbb{R}^n$$ is the classic continuous sample space.

Probability Space
----------------------------------

A [Probability Space](https://en.wikipedia.org/wiki/Probability_space) is a measurable
space equipped with a measure $$P$$ satisfying

1. *Positivity* $$P : \Sigma \rightarrow \mathbb{R}^+ $$
2. *Normalized* $$P(X) = 1$$
3. $$P(\emptyset) = 0$$
4. *Countable additivity* : Given a countable number of disjoint $$A_n \in \Sigma$$ $$P(\cup_n A_n) = \sum_n P(A_n)$$

Given our sample space $$X$$ and our sigma algebra $$\Sigma$$ we can look at
$$\mathcal{P}(X, \Sigma)$$ the space of normalized measures. These are the possible
definitions of probability given our sample space. For the finite discrete measure
this space of measures is quite simple - just the space of non-negative functions
$$f : X \rightarrow \mathbb{R}$$ such that $$\sum_i f(i) = 1$$

At this stage we have a complete language for discussing probabilities - and this
is where integration typically creeps in.

Random Variables
--------------------------------------------------------------------

The standard definition of a [Random Variable](https://en.wikipedia.org/wiki/Random_variable#Standard_case) is a measurable function from a probability space
to the reals (with the Lebesgue measure). Such a measurable function can be integrated. The integral of our random variable is the standard expectation value and integrals of simple functions of our random variable lead to the various moments.

On their own measurable functions are natural to define given our
measurable spaces - they play the role of measurable space morphisms.

For meaurable spaces $$X$$,$$Y$$ a measurable function $$f: X \rightarrow Y$$ satisfies.

$$f^{-1}(B)$$ is measurable for all measureable sets B in Y.

What's with the inverse?

You may be familiar with the identities for any map $$f: X \rightarrow Y$$.

1. $$f^{-1}(Y)=X$$
2. $$f^{-1}(\emptyset) = \emptyset$$
3. $$f^{-1}(\cap_\alpha V_\alpha) = \cap_\alpha f^{-1} (V_\alpha)$$
4. $$f^{-1}(\cup_\alpha V_\alpha) = \cup_\alpha f^{-1} (V_\alpha)$$
5. $$f^{-1}(Y - V) = X - f^{-1}(V)$$

All together we have a morphism of the $$\sigma$$ algebras if f is measurable.
$$f^{-1} : \Sigma_Y \rightarrow \Sigma_X$$. Additionally if we restrict to the image of $$X$$,
$$f^{-1}: P(Y) \rightarrow P(X)$$ is one-to-one. So we have an isomorphism of $$\Sigma_Y$$ with
a subset of $$\Sigma_X$$.

We Really Care about Measures
-----------------------------------------------------------------------

Random Variables are really a means to define probability measures - and
probability measures are our primarily object of interest.

Given a measurable function $$f : X \rightarrow Y$$ and a probability
measure $$P$$ on $$X$$ we can construct a probability measure on $$Y$$.
This is called a push-forward of the measure.

$$f^*(p)(V) = p(f^{-1}(V))$$

Does $$f^*(p)$$ satisfy the conditions of a probability measure?

1. Empty set has 0 measure : $$f^*(p)(\emptyset) = p(\emptyset) = 0$$
2. Normalized : $$f^*(p)(Y) = p(X) = 1$$
3. Can also verify countable additivity.

Further this definition is consistent with how we think about probability.
The probablity measure we get from this is equivalent to drawing samples
from the original probability distribution and evaluating the function
on each sample.

So a real random variable is defining a probability distribution
on $$\mathbb{R}$$ and it is this push forward distribution that
we care about. Much of the machinery of expectation values and moments
is used to estimate properties of this push-forward distribution.
In my experience it is simpler to always think in terms of probability
measures - viewing Random Variables as simply one means to generate a
measure given an existing probability space.

Artifically Restricted Scope
--------------------------------------------------------------------

While measurable functions are meaningful for any measurable space as the range $$Y$$ -
the definition of a random variable typically restrict to real valued measurable functions.
(A restriction though to only real valued measurable functions - (which is common but
[NOT universal](https://en.wikipedia.org/wiki/Random_variable#Extensions)). Given the
emphasis on integration this restriction is reasonable - or strictly a restriction to
$$Y$$ where an integral is defined (Complex vector spaces, Banach spaces, ..).

* Quite often we are interested in functions of our domain probability space that are
not real valued. [Simple examples](https://en.wikipedia.org/wiki/Random_variable#Extensions)
include random sentences based on a generative model for text.

* Categorically we are interested in all measurable spaces and all measurable functions
between them. (Although recently noticed that we can write down the category of real
random variables as a [Comma Category](https://en.wikipedia.org/wiki/Comma_category) in
particular as the category over $$\mathbb{R}$$ with the Borel Algebra.)

* While the category point seems aesthetic - it does commonly occur that we are interested
in compositions of random variables, and Category theory is designed to make it easy to talk
about function composition.

At the very least a 'Random Variable' should be (and occasionally is) any measurable map
between a Probability space $$(X, P)$$ and a measurable space $$Y$$



Conflicting Notation
--------------------------

While working with a single sample space we have a notion of arithmetic on
real random variables which derives from arithmetic on the reals.

* Addition : $$(f + g)(x) = f(x) + g(x)$$
* Multiplication : $$(fg)(x) = f(x)g(x)$$

It is common to see statements of the form : We define $$h = f + g$$ where $$f$$ and
$$g$$ are independent Normal random variables. This actually introduces a second
notion of addition. This second case is really an abuse of $$+$$. Abuses of notation
are often fine as long as we are aware of them and they don't lead to abuses of mathematics.
We are really looking at a sequence of the following operations.

* Given inital measure spaces $$X$$ and $$Y$$ and random variables $$f$$,$$g$$.
* Construct the product space $$X \times Y$$.
* Extend $$f$$ and $$g$$ to be defined on product space $$f(x,y) = f(x)$$ and
$$g(x,y) = g(y)$$.
* Add the random variables $$f + g$$ with the standard notion of addition.

This is perhaps a silly amount of detail, but you see that the $$+$$ bundles
together operations on the sample space with operations on the random variables.
This is not quite a problem with Random Variables themselves - but a problem of
working without reference to the underlying sample spaces.

Real Random Variables are Coordinates
-----------------------------------------------------------------------

Random variables primarily act as 'Coordinates' - allowing us to map from our sample space to real valued coordinates that we can compute with - make approximations, etc, etc.
Why dont we just call them coordinate functions then?
Digging through the notation of other fields for a close analog we
come across - the use of coordinates & coordinate charts in the
discussion of manifolds.

$$f : U \rightarrow \mathbb{R}$$

for $$U \subset M$$.

Much like the study of manifolds - Even though we have real valued coordinate functions
it does not necessarily make sense to start integrating those coordinate values. It is
tempting to automatically start integrating these measurable real valued functions - but even though it is an allowed operation, is it meaningful? In simple cases -  
