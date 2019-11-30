---
layout: post
---

Families of Parametrized Distributions
=======================================

Each of the following defines a 

* A sample space $$X$$ + sigma algebra $$\mathcal{S}$$
* A parameter space $$P$$
* A mapping from the parameter space $$P$$ to a subset
  of the set of measures defined on $$(X, \mathcal{S})$$
  * This mapping is typically defined by a probability density together with a reference 
  distribution.

* The notation $$F(P, Q, ..)$$ of application of a function $$F$$ to probability distributions $$P$$, $$Q$$ is defined to be the [pushforward](https://en.wikipedia.org/wiki/Pushforward_measure) by F of the
cartesian product of $$P$$, $$Q$$, ..

$$F_{*}(P \times Q \;\times ...)$$


{% for dist_kv in site.data.prob.distributions %}
{% assign dist = dist_kv[1] %}
<h3 id="{{ dist_kv[0] }}"> {{ dist.name }} </h3>
<b>Parameters :</b>
{% for param in dist.parameters %}
* {{ param.name }} $$\in$$ {{ param.range }}
{% endfor %}
<b>Sample Space :</b> {{ dist.sample_space }}<br>
<b>Sigma Algebra :</b> {{ dist.sigma_algebra }}<br>

{% if dist.measure %}
<b> Measure : </b>{{ dist.measure }}<br>
{% endif %}

{% if dist.density %}
<b> Density : </b>{{ dist.density }}<br>
{% endif %}

<b>Arithmetic</b>: 
{% for op in dist.operations %}
* {{ op.name }} : {{ op.formula }}
{% endfor %}

<b>Links</b>
<ul>
{% for link in dist.links %}
<li>{{ link.name }} : <a href="{{ link.link }}">{{ dist.name }}</a></li>
{% endfor %}
</ul>
{% endfor %}

<!--
Examples of generating links to parts of the page.
{% for dist_kv in site.data.prob.distributions %}
<A href="#{{dist_kv[0]}}"> {{ dist_kv[1].name }} </A>
{% endfor %}
-->