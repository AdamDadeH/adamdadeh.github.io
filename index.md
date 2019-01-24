---
layout: page
title: Adam Henderson
tagline: Math, Stats, and Coffee
description: Math, Stats, and Coffee
---

Background : PhD in theoretical physics - focusing on quantum and classical gravity. Since PhD, I have gravitated more towards research in applied mathematics with a focus on statistics and data science as it is a fertile area for new advancements. 

[List of Publications](http://inspirehep.net/author/profile/A.Henderson.1) from my quantum gravity era. Without academic pressure I have lacked the impetus to write. Although - this page will exist as an outlet for random ideas.

Posts : 
--------------

<ul>
  {% for post in site.posts %}
  <li class="post-title"><a href="{{ post.url }}">{{ post.title }}</a></li>
  {% endfor %}
</ul>

Now Reading : 
-------------

[Categories for the Working Mathematician](https://en.wikipedia.org/wiki/Categories_for_the_Working_Mathematician)
  * A hole in my mathematical background that needed filling.

Past Reading :
---------------

{% for book in site.books %}
  <h3>{{ book.name }} - {{ book.subject }}</h3>
  <p>{{ book.content | markdownify }}</p>
{% endfor %}

