---
title: "Notation in Statistics"
layout: page
---
*Notation is powerful*

"By relieving the brain of all unnecessary work, a good notation sets it free to concentrate on more advanced problems, and, in effect, increases the mental power of the race." (Alfred North Whitehead, “An Introduction to Mathematics”)

"Good notation can make the difference between a readable paper and an unreadable one." Terence Tao [Use Good Notation|https://terrytao.wordpress.com/advice-on-writing-papers/use-good-notation/]

A good notation will allow one to work more efficiently, convey ideas more concisely, and lead to new developments. A poor notation acts as a 
friction to development and confines our thoughts to old ways of thinking.
I argue that statistics is held back with such poor notation.

Probability & Measure Theory
----------------------------

Modern probability theory is commonly said to derive from the 
work of [Kolmogorov|https://en.wikipedia.org/wiki/Andrey_Kolmogorov] 
who laid a foundation using measure theory. From my experience probability 
*is* most naturally expressed in the language of measure theory.
Quite often though measure theory & the theory of integration are
introduced in probability with the same emphasis - Probability Spaces &
Random Variables are given equal weight or Random Variables are given
priority. While it is natural to bundle the two together since measure
theory is primarily a pre-requisite to integration - In probability
measure theory is by far the star of the show.

Lets start by going through the regular song and dance.

Sample Spaces
-----------------------------------

In the language of measure theory a sample space is a *measurable space*
being a set $$X$$ equipped with a sigma algebra $$\Sigma$$.

A sigma algebra is a set of subsets of $$X$$ ($$\Sigma is a subset of \mathcal{P}X$$, the Power set of $$X$$) such that :

0. $$\Sigma$$ contains the empty set $$\emptyset$$
1. $$\Sigma$$ is closed under complements. If $$A \in \Sigma$$ then $$X - A \in \Sigma$$
}.
2. $$\Sigma$$ is closed under countable unions. So given $$A_n \in \Sigma$$ for n indexed by the natural numbers - then $$\cup_n A_n \in \Sigma$$.
}

From these we have other derived properties, $$X \in \Sigma$$, $$\Sigma$$ is closed under countable unions.

This pair $$(X,\Sigma)$$ gives us the space of possible outcomes. Typical
examples

* *Discrete* A Countable Set $$X=[1,2,3,...,n]$$ with $$\Sigma = P(X)$$ or 
all subsets of $$X$$. The typical discrete sample space describing the states 
of your D6,D20,etc die, the states of a deck of cards.
* *Lebesgue* The classic 'continuous' sample space.

Probability Space
----------------------------------

A probability space is a measurable space equiped with 
a measure $$P$$ that satisfying

1. *Positivity* $$P : \sigma \rightarrow \RR^+ $$
2. *Normalized* $$P(X) = 1$$
3. $$P(\emptyset) = 0$$
4. *Countable additivity* : Given a countable number of disjoint $$A_n \in \Sigma$$ $$P(\cup_n A_n) = \sum_n P(A_n)$$

Given our sample space $$X$$ and our sigma algebra $$\Sigma$$ we can look at 
$$\mathcal{M}(X, \Sigma)$$the space of possible measures that can be defined on it or
$$\mc{P}(X, \sigma)$$ the space of normalized measures.

At this stage we have not deviated from the norm.

Random Variables
----------------------------------

The standard definition of a Random Variable is a measurable function from
a probability space to the reals (with the Lebesgue measure). This is where integration typically  creeps in - as such a measurable function can be integrated. The integral of our random variable is the standard expectation
value and integrals of simple functions of our random variable lead to the
various moments.

On their own measurable functions are natural to define given our 
measurable spaces - they play the role of measurable space morphisms.

For meaurable spaces $$X$$,$$Y$$ a measurable function $$f: X \rightarrow Y$$ satisfies.

1. $$f^{-1}(B)$$ is measurable for all measureable sets B in Y.

What's with the inverse? You may be familiar with the identities
$$f^{-1}(\cup_a U_a) = \cup_a f^{-1} (U_a)$$ and similarly for intersection
and for complementation. There are not corresponding identities for $f$.

Given a map $$f: X \rightarrow Y$$. If we restrict to the image of $$X$$, $$f(X) = Y'$$ (or
equivalently assume that f is an onto map). Then the pre-image mapping $$f^{-1}: PY \rightarrow PX$$ is a one-to-one function of $$PY$$ into $$PX$$. Since if $$V_1$$ and $$V_2$$ are such that
$$f^{-1}(V_1) = f^{-1}(V_2)$$ we have that for any $$y \in V_1$$ there is a set of values in $$X$$ that are in it's pre-image - these values must be in the pre-image of $$V_2$$ - so $$y$$ must be
in $$V_2$$. Further this one-to-one mapping preserves a (an even larger set than) the natural
operations of a sigma algebra.

\bnum
\item $$f^{-1}(Y)=X$$
\item $$f^{-1}(\emptyset) = \emptyset$$
\item $$f^{-1}(\cap_\alpha V_\alpha) = \cap_\alpha f^{-1} V_alpha$$
\item $$f^{-1}(\cup_\alpha V_\alpha) = \cup_\alpha f^{-1} V_alpha$$
\item $$f^{-1}(Y - V) = X - f^{-1}(V)$$
\enum

So this an isomorphism of $$\sigma$$ algebras. We have then that the mapping $$f:X \rightarrow Y$$ induces a natural isomorphism of sigma algebras - allowing us to either map a sigma algebra
on $$X$$ to one on $$Y$$ or vice-versa.

With these identities + the condition for measurability of $$f$$ we find that
$$f^{-1}$$ acts as a morphism of sigma algebras

$$f^{-1} : \mathcal{B} -> \Sigma$$

Random Variable == Measure on R
-------------------------------------

Given a measurable function $$f : X \rightarrow R$$ we and a probability
measure $$p$$ on $$X$$ we can construct a probability measure on $$R$$.
We will refer to this a push-forward of the measure.

$$f^*(p)(V) = p(f^{-1}(V))$$

Does $$f^*(p)$$ satisfy the conditions of a probability measure?

1. $$f^*(p)(\emptyset)$$ = p(\emptyset) = 0$$
2. $$f^*(p)(Y)$$ = p(X) = 1$$
3. Can also verify countable additivity.

Further this definition is consistent with how we think about probability.

Thus our random variables are really defining a probability distribution
on $$R$$. The random variable produces an image of our probability
distribution in $$R$$. 

This triple defines $$(X,\Sigma,\rho)$$ our Random Variable. Why do we eschew to
standard name of Probability Space - we don't necessarily need to - we could just
entirely remove the term.

One of the elementary operations we consider in probability is the mapping of our
probability space by functions. Pushforward. This enables us to push forward a measure
to the new space - thus defining a new random variable. 

Random Variables
=====================

A random variable is the full triple : $$(X,\sigma, \rho)$$

Most often in literature we refer to a Borel measurable functions $$f: X \rightarrow \RR$$
as a random variable. . In what sense is
this a random (scalar) variable? More generally we can talk about $$Y$$ valued random
variables being measurable functions from $$f: X \rightarrow Y$$.


* Given this function we can push forward the measure on $$X$$ to obtain a measure on $$\RR$$. We then have a real valued probability space.
* Perhaps variable hearks back to thoughts of solving algebraic equations for unknown 
variables in which case we desire a variable to take values in a space that admits algebraic
operations.
* Especially in the more general case we find that the core componenet is the IMAGE of
the function as opposed to the function itself. In that sense we should consider the target
$$(Y,\sigma_Y,f^*\rho)$$ to be the random variable and $$f$$ then simply being a morphism
between these two probability spaces. In that sense any triple then
corresponds to a random variable - so what is the point!

Point 2 reveals the primary use of random variables - as random 'Coordinates' the ability
to map from a more abstract system to real or complex valued coordinates that we can compute
with - make approximations, etc, etc.

Then we have random variables being any element of a category of probability spaces.
Random coordinates being measurable real valued functions (which naturally themselves
are 'random variables' - but in the same way that the real line is a manifold, but it
is the prototypical manifold.

A Dependence on Expectation Values
===================================

Nearly everything we do in probability involves expectation values. From the discussion
above we've noted that these are not natural within probability, but are a convenience
given the formulation in terms of measure theory.

Where do we use them without thinking?

*  Mean error for model performance. We are always computing the mean over training data
and over test data - without considering the more general properties of the distribution. Does mean
describe it well?


Coordinate Independence
===========================

If we are thinking about random variables in a broader sense it is natural 
to shy away from the classic methods of computing expectation values and 
moments. To be clear - expectation values and moments of distributions are
extremely useful for standard/nice distributions, but it is valuable to step
outside this paradigm.
