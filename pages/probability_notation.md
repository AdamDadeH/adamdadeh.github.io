---
title: "Notation in Statistics"
layout: page
---

*Notation is powerful*

"By relieving the brain of all unnecessary work, a good notation sets it free to concentrate on more advanced problems, and, in effect, increases the mental power of the race." (Alfred North Whitehead, “An Introduction to Mathematics”)

"Good notation can make the difference between a readable paper and an unreadable one." Terence Tao [Use Good Notation](https://terrytao.wordpress.com/advice-on-writing-papers/use-good-notation/)

See also [hypotext - notation](https://github.com/hypotext/notation)

A good notation will allow one to work more efficiently, convey ideas more 
concisely, and lead to new developments. A poor notation acts as a 
friction to development and confines our thoughts to old ways of thinking.
I argue that statistics is held back with such poor notation.

Probability & Measure Theory
----------------------------

Modern probability theory is commonly said to derive from the 
work of [Kolmogorov](https://en.wikipedia.org/wiki/Andrey_Kolmogorov)
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

A sigma algebra is a set of subsets of $$X$$ ($$\Sigma$$ is a subset of $$\mathcal{P}X$$, 
the Power set of $$X$$) such that :

0. $$\Sigma$$ contains the empty set $$\emptyset$$
1. $$\Sigma$$ is closed under complements. If $$A \in \Sigma$$ then $$X - A \in \Sigma$$.
2. $$\Sigma$$ is closed under countable unions. So given $$A_n \in \Sigma$$ for n indexed 
by the natural numbers - then $$\cup_n A_n \in \Sigma$$.

From these we have other derived properties, $$X \in \Sigma$$, $$\Sigma$$ is closed under 
countable unions.

This pair $$(X,\Sigma)$$ gives us the space of possible outcomes. Typical
examples

* *Discrete* A Countable Set $$X=[1,2,3,...,n]$$ with $$\Sigma = P(X)$$ or 
all subsets of $$X$$. The typical discrete sample space describing the states 
of your D6,D20,etc die, the states of a deck of cards.
* *Lebesgue* The classic 'continuous' sample space.

Probability Space
----------------------------------

A [Probability Space](https://en.wikipedia.org/wiki/Probability_space) is a measurable
space equiped with a measure $$P$$ satisfying

1. *Positivity* $$P : \Sigma \rightarrow \mathbb{R}^+ $$
2. *Normalized* $$P(X) = 1$$
3. (Implied by 4) $$P(\emptyset) = 0$$
4. *Countable additivity* : Given a countable number of disjoint $$A_n \in \Sigma$$ $$P(\cup_n A_n) = \sum_n P(A_n)$$

Given our sample space $$X$$ and our sigma algebra $$\Sigma$$ we can look at
$$\mc{P}(X, \Sigma)$$ the space of normalized measures. These are the possible definitions
of probability given our sample space.

At this stage we have not deviated from the norm.

Random Variables 1
----------------------------------

The standard definition of a Random Variable is a measurable function from
a probability space to the reals (with the Lebesgue measure). This is where integration typically 
creeps in - as such a measurable function can be integrated. The integral of our random variable 
is the standard expectation value and integrals of simple functions of our random variable 
lead to the various moments.

On their own measurable functions are natural to define given our 
measurable spaces - they play the role of measurable space morphisms.

For meaurable spaces $$X$$,$$Y$$ a measurable function $$f: X \rightarrow Y$$ satisfies.

1. $$f^{-1}(B)$$ is measurable for all measureable sets B in Y.

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

This all seems Fine - What's the Big Deal?

Artifical Restricted Scope
--------------------------

A restriction though to only real valued measurable functions (which is common but NOT
universal) is overly limiting. 

* Categorically we would look at all measurable spaces and all measurable functions 
between these spaces.

Conflicting Notation
--------------------------

While working with a single sample space we have a notion of arithmetic on
real random variables which derives from arithmetic on the reals.

* $$(f + g)(x) = f(x) + g(x)$$
* $$(fg)(x) = f(x)g(x)$$

Nothing surprising there.

You also see though statements like.

$$h = f + g$$

where f and g are independent Bernoulli random variables. All the sudden we have
2 notions of addition?

The second case is really an abuse of $$+$$. Abuses of notation are often fine as
long as we are aware of them and they don't lead to abuses of mathematics. We
are really looking at a sequence of the following operations.

* Given inital measure spaces $$X$$ and $$Y$$ and random variables $$f$$,$$g$$.
* Construct the product space $$X \times Y$$
* Extend $$f$$ and $$g$$ to be defined on product space $$f(x,y) = f(x)$$ and
$$g(x,y) = g(y)$$.
* Add the random variables $$f + g$$ with the standard notion of addition.

This is perhaps a silly amount of detail, but you see that the $$+$$ bundles
together operations on the sample space with operations on the random variables.

We Really Care about Measures
-----------------------------

Given a measurable function $$f : X \rightarrow \mathbb{R}$$ we and a probability
measure $$P$$ on $$X$$ we can construct a probability measure on $$\mathbb{R}$$.
We will refer to this a push-forward of the measure. (Strictly this extends
to any measurable function $$f: X \rightarrow Y$$.

$$f^*(p)(V) = p(f^{-1}(V))$$

Does $$f^*(p)$$ satisfy the conditions of a probability measure?

1. $$f^*(p)(\emptyset) = p(\emptyset) = 0$$
2. $$f^*(p)(Y) = p(X) = 1$$
3. Can also verify countable additivity.

Further this definition is consistent with how we think about probability.

Thus our random variables are defining a probability distribution
on $$\mathbb{R}$$ and it is this push forward distribution that 
we are often looking to estimate the properties of.

Real Random Variables are Coordinates
-------------------------------------

Point 2 reveals the primary use of random variables - as random 'Coordinates' the ability
to map from a more abstract system to real or complex valued coordinates that we can compute
with - make approximations, etc, etc.

Then we have random variables being any element of a category of probability spaces.
Random coordinates being measurable real valued functions (which naturally themselves
are 'random variables' - but in the same way that the real line is a manifold, but it
is the prototypical manifold.

Digging through the notation of other fields for a close analog we
come across - the use of coordinates & coordinate charts in the
discussion of manifolds.

$$f : U \rightarrow \mathbb{R}$$

for $$U \subset M$$.

If we are thinking about random variables in a broader sense it is natural 
to shy away from the classic methods of computing expectation values and 
moments. To be clear - expectation values and moments of distributions are
extremely useful for standard/nice distributions, but it is valuable to step
outside this paradigm.


A Dependence on Expectation Values
-----------------------------------

Much of probability theory, statistics, & data science involves expectation values or
other structures we inherit from working with 'random coordinates'. Some of these are
natural and some can get us in trouble ..

* Central Limit Theorem
*  Mean error for model performance. We are always computing the mean over training data
and over test data - without considering the more general properties of the distribution. Does mean
describe it well?

They but are certainly a convenience but much like geometry - not something we want
to rely on as a foundational element of the theory.



