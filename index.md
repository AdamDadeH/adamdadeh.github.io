---
layout: page
title: Adam Henderson
tagline: Math, Stats, and Coffee
description: Math, Stats, and Coffee
---

Background : PhD in theoretical physics - focusing on quantum and classical gravity. Since PhD, I have gravitated more towards research in applied mathematics with a focus on statistics and data science as it is a fertile area for new advancements. 

[List of Publications](http://inspirehep.net/author/profile/A.Henderson.1) from my quantum gravity era. Without academic pressure I have lacked the impetus to write. Although - this page will exist as an outlet for random ideas.

* [Research Gate](https://www.researchgate.net/profile/Adam_Henderson12)
* [Linkedin](https://www.linkedin.com/in/adam-henderson-b4887b29)

Publications :
-------------

{% for pub in site.data.publications %}
  {% if pub.type == "conference" %}
<li class="publication"><b>{{pub.date}}</b> - {{pub.authors | array_to_sentence_string: ''}}: <b>{{ pub.title }}</b>. In the proceedings of {{ pub.conference }}, {{ pub.location }} : {% for link in pub.links%}<a href="{{ link.link }}">[{{link.name}}]</a> {%endfor%}</li>
  {% endif %}

  {% if pub.type == "paper" %}
<li class="publication"><b>{{pub.date}}</b> - {{pub.authors | array_to_sentence_string: ''}}: <b>{{ pub.title }}</b>. {{pub.journal}} {{pub.issue}}. {% for link in pub.links%}<a href="{{ link.link }}">[{{link.name}}]</a> {%endfor%}</li>
  {% endif %}
{% endfor %}

Posts : 
--------------

<ul>
  {% for post in site.posts %}
  <li class="post-title"> <b>{{ post.date | date: '%Y-%m-%d' }}</b> : <a href="{{ post.url }}">{{ post.title }}</a></li>
  {% endfor %}
</ul>

Reading : 
-------------

[Categories for the Working Mathematician](https://en.wikipedia.org/wiki/Categories_for_the_Working_Mathematician)
  * A hole in my mathematical background that needed filling.

Past Reading :
---------------
{% for book in site.books %}
  {% if book.review > 3 %}
  <h5>{{ book.title }} : <a href="{{ book.url }}">Notes</a></h5>
  <p>Subject : {{ book.subject }}<br>
  Author : {{ book.author }}<br>
  {% endif %}
{% endfor %}

