---
layout: post
title: Identity Elements for Binary Operations
use_math: True
subject: Math
---

One of my first exposures to the art of proof was
proving the uniqueness of the additive identity.
At the convergence of thoughts about algebraic structures
in the context of category theory and exposure to curious
binary operations from digging through legacy code -
I found myself brought full circle recently with a
re-investigation of the nature identity elements.

This investigation covers

1. What are the minimal conditions for uniqueness of an identity?
2. Understanding when uniqueness fails.

Definitions
-----------

For a binary operation $b : X \times X \rightarrow X$ defined on
a set $X$ we define :

* **left identity element** : $e_L \in X$ such that $b(e_L, x) = x$ for all $x \in X$
* **right identity element** : $e_R \in X$ such that $b(x, e_R) = x$ for all $x \in X$
* **(two-sided) identity element** : $e \in X$ such that $b(x, e) = b(e, x) = x$ for all $x \in X$

Two-sided identity elements - which we will mostly refer to as simply identity elements are quite familiar.

| **Binary op** | **Identity** |
| ------ | ------ |
| Addition | $0$ |
| Multiplication | $1$ |
| Matrix mult. | Identity matrix |
| String Concatenation | "" (Empty string) |

An example of a binary operation with only right identity is
exponentiation defined on positive integers.

$b(x, y) = x^y$

$b(x, 1) = x^1 = x$

Simple Results
---------------

The classic uniqueness result for an identity element

**Uniqueness of Identity** : For a binary operation $b: X \times X \rightarrow X$
there is at most one identity element.

Proof : Suppose that for a binary operation $b$ there are two identity elements $e$ and $f$. Then, $b(e, f) = f$ as $e$ is
an identity and $b(e, f) = e$ as $f$ is an identity. Thus $e=f$.

**Exclusivity** : For a binary operation $b: X \times X \rightarrow X$ it has one of
  1. One or more left identities
  2. One or more right identities
  3. One unique identity
  4. No left/right/two-sided identities.

Proof :
* Given a left identity $e$ and right identity $f$ we
find $b(e, f) = f = e$, so $e$ is also a right identity, so is an identity.
* Similarly given a pair of left (right) identity $e$ and identity $f$ - the identity is also a right (left) identity, so $e = f$.
Together these restrict us to one of the 4 cases.

Non-Uniqueness of Left/Right Identity
---------------------------

Suppose we have a set $X = \{e, f\}$, binary operation $b$ on $X$, and two
left identities $e$ and $f$.

* $b(e, e) = e$  and $b(e, f) = f$
* $b(f, f) = f$  and $b(f, e) = e$

This is a well defined binary operation with two left identities.

Multiple (Almost) Identity Elements
-----------------------

In the wilds of software development strange things abound...
that nearly break the pattern above.

One such example was observed when mixing ```Lists``` together with ```Options``` in Scala. Consider the set ```List[Int]``` whose elements are finite sequences of integers. A simple operation on
lists is concatenation

```
concat([3, 2, 4] , [7, 8, 9, 1]) = [3, 2, 4, 7, 8, 9, 1]
```

Given a set $X$ we can define the set $Option[X] = \{None\} \cup \{Some(x) \vert x \in X\}$. These are particularly helpful for any case where data may be missing.

Suppose we want to extend the definition of $$concat$$ to ```Option[List[Int]]```

```scala
concatenate : (Option[List[Int]], Option[List[Int]]) => Option[List[Int]]
```

We could define this by letting None act as an identity.


```scala
def concatenate(x: Option[List[Int]], y: Option[List[Int]]): Option[List[Int]] = {
    match (x,y) = {
        case (None, None) => None
        case (Some(x), None) => Some(x)
        case (None, Some(y)) => Some(y)
        case (Some(x), Some(y)) => Some(concatenate(x,y))
    }
}
```

With this choice we note that both ```None``` and ```Some([])```
act like identities. ```concatenate(Some(x), None) = concatenate(None, Some(x)) = Some(x)``` for all ```x```.
Similarly ```concatenate(Some([]), Some(x)) = concatenate(Some(x), Some([])) = Some(x)```

Where this breaks down is that ```concat(Some([]), None) = Some([])```
or that ```Some([])``` does not behave as the identity for ALL elements.

For the purposes of this binary operation ```Some([])``` and ```None``` behave nearly the same and it is possible to simplify things by treating
the two as being equivalent.

Near Identities
-----------------

What we see in the example above is that we have elements that
act as identity for **most** of the set.

We can call $e$ a $Y$ near left/right/two-sided identity for
$b : X \times X \rightarrow X$ if the appropriate identity
conditions hold for all $y \in Y$.

* For two sided : $b(e, y) = b(y, e) = y$ for all $y \in Y$.

If in addition we have that the binary operation is associative
then given two $Y$ near identities $(e, f)$, $b(e, f)$ is also
a $Y$ near identity.

$b(b(e, f), y) = b(e, b(f, y)) = b(e, y) = y$

$b(y, b(e, f)) = b(b(y, e), f) = b(y, f) = y$

If $X$ decomposes into a set $I$ of $X - I$ near identity
elements for binary operation $b$. We can then quotient $(X, b)$
by an equivalence relation equating all elements in $I$.

$Y = X/\tilde{} = X-I \cup \{I\}$

$b' : Y \times Y \rightarrow Y$ :

* $b'(x, y) = b(x, y)$ for $x,y \in X-I$
* $b'(I, y) = b'(y, I ) = y$ for $y \in Y$

We can concoct cases with no identity element that have a well-defined
quotient having an identity element.

In the example above if someone hard coded behavior for the empty set (weirder things have happened)

```scala
def concatenate(x: Option[List[Int]], y: Option[List[Int]]): Option[List[Int]] = {
    match (x,y) = {
        case (None, None) => None
        case (Some([]), None) => None
        case (Some(x), None) => Some(x)
        case (None, Some(y)) => Some(y)
        case (Some(x), Some(y)) => Some(concatenate(x,y))
    }
}
```

Then neither `None` nor `Some([])` are identity elements, but each
are near identities for $Option[List[Int]] - \{None, Some([])\}$.
We can quotient this with equivalence relation $Some([]) \sim None$
The quotient gets us back to `(List[Int], concatenate)` - so entirely avoiding the `Option`.

This is as far as I will follow this rabbit hole.
