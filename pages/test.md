---
title: "Notation in Statistics"
layout: post
---
Notation is powerful.

By relieving the brain of all unnecessary work, a good notation sets it free to concentrate on more advanced problems, and, in effect, increases the mental power of the race. (Alfred North Whitehead, “An Introduction to Mathematics”)

"Good notation can make the difference between a readable paper and an unreadable one." Terence Tao [https://terrytao.wordpress.com/advice-on-writing-papers/use-good-notation/]

A good notation will allow one to work more efficiently, convey ideas more concisely, and even lead to new developments. A poor notation acts as a 
friction to development and confines our thoughts to old ways of thinking.

Probability & Measure Theory
============================

Modern probability theory is commonly said to derive from the work of
Kolmogorov [https://en.wikipedia.org/wiki/Andrey_Kolmogorov] who laid a
foundation using the language of measure theory.

Probability *is* most naturally expressed in the language of measure theory. 
The only qualm I have with the standard formulation is the importance we place 
on the theory of integration and expectation values.

Sample Spaces
-----------------------------------

In the language of measure theory a sample space is a *measurable space*
being a set $$X$$ equipped with a sigma algebra $$\mathcal{A}$$.

A sigma algebra is a set of subsets of $$X$$ ($$\mathcal{A} \sub \mathcal{P}X$$) such that

0. Contains the empty set.
1. $$\mathcal{A}$$ is closed under complements. So $$A \in \mathcal{A}$$ then $$X - A \in \mathcal{A}$$
}
2. $$\mathcal{A}$$ is closed un
der countable unions. So if $$A_n \in \mathcal{A}$$ for n indexed by the natural numbers - then $$\cup_n A_n \in \mathcal{A}$$.
}

Probability Space
----------------------------------

A probability space is simple a measurable space equiped with a normalized measure. Ok nothing new here.

Given our sample space $$X$$ and our sigma algebra $$\sigma$$ we can look at 
$$\mc{M}(X, \sigma)$$the space of possible measures that can be defined on it or
$$\mc{P}(X, \sigma)$$ the space of normalized measures.

Where a measure satisfies
\begin{itemize}
\item $$p : \sigma \rightarrow \RR^+ $$
\item $$p(X) = 1$$
\item $$p(\empty) = 0$$
\item Countable additivity.
\end{itemize}

Ingredients:
1) A set $$X$$ which will denote the range of values our variable can take.
2) A sigma algebra (define) on $$X$$ which defines the events/outcomes/circumstances/properties we 
can measurethe probability of.
3) A normalized (to 1) measure on this measurable space $$(X,\Sigma)$$.

At this stage I am complete agreement with the standard views.

Random Variables
----------------------------------

The standard definition of a Random Variable is a measurable function from
a probability space to the reals. Measurable functions are the natural
thing to write down given our measurable spaces - being the morphisms of
measurable spaces.

This definition enables us to : 

1. Compose $$f: X \rightarrow Y$$ and $$g: Y \rightarrow R$$ leading to an *integrable* function.
2. 

A measurable function $$f: X \rightarrow Y$$ satisfies

1. $$f^{-1}(B)$$ is measurable for all B measurable in Y.

What's with the inverse? You may be familiar with the identities
$$f^{-1}(\cup_a U_a) = \cup_a f^{-1} (U_a)$$ and similarly for intersection
and for complementation. These do not necessarily hold for the other
direction.

Initial and Final Sigma Algebras
-------------------------------------

Given a function $$f: X \rightarrow Y$$ and a sigma algebra on $$X$$ we can generate a sigma algebra on $$Y$$ that makes $$f$$ a measurable function. There are many such $$\sigma_Y$$ ranging
from $$\{\emptyset, Y\}$$ (the coarsest measure) to $$\{A | f^{-1}(A) \in \sigma_X \}$$ (the finest measure such that $$f$$ is measurable. The coarsest makes all functions measurable and the finest is more restrictive - while the coarsest allows us to measure the smallest number of sets and the finest the most. In our case we are far more interested in being able to
measure the maximum number of measurable sets (and thus measurable maps from $$Y$$ to other spaces).

From here on let us denote this as $$f^{*}(\sigma_X)$$ the push forward of $$\sigma_X$$.

Similarly we can pull back a sigma algebra from $$Y$$ to $$X$$ given a map $$f:X \rightarrow Y$$. Again we have a range of options - from the minimal to the most discrete sigma algebra on $$X$$.

Best way to think about both of these.

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

This also gives up the ability to push forward and pull back topologies (?) The push forward topology is the quotient topology construction - also called the final topology. The opposite is referred as the initial/weak topology (and the resulting sets are cylinder sets)

Construction of new random variables by mapping a given random variable with an arbitrary map.

Factorization of a random variable. We have a sub-algebra of $$\sigma_X$$ induced by $$f$$ and $$Y
$$. When does this enable us to factor the space in two independent components?

What? What happened to random variable being a measurable function from
our probability space to the reals?

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

\section{Push Forward Measure}

So - prior we had that $$f:X \rightarrow Y$$ gives us a sigma algebra on $$Y$$ : $$f^{*}(\sigma)$$.
Given this we can push forward any measure on $$(X,\sigma)$$.

$$f^*(\mu)(V) = \mu(f^{-1}(V))$$

\section{Pull Back Measure}

Given a measure on $$Y$$ we can pull it back to a measure on $$X$$.

We can consider the push-forward of the measure - followed by pull-back - then ask if
we can factor our original measure in terms of this.

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

There are multiple things to consider - first the precise formulation of the problem
we wish to tackle and then efficient methods to compute.

Consider - first that the primary goal of such computations is the estimation
of properties of the probability measure on the space to enable more efficient
computation of probabilities and second to obtain values that summarize the
distribution enabling us to have an easier grasp on the content of this mathematical
object.

So in order to tackle a more general family of random variables - or to tackle them
without resort a particular set of coordinates.
