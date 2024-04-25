---
layout: home
title: Adam Henderson
tagline: For Abstractions Sake
description: For Abstractions Sake
---

"One of the principle objects of theoretical research in any department of knowledge is to find the point of view from which the subject appears in its greatest simplicity." - Josiah Willard Gibbs

This is the core thread of my research / professional career across Theoretical Physics (Quantum Gravity & General Relativity), applied math, machine learning, and software engineering. 

[List of Publications](http://inspirehep.net/author/profile/A.Henderson.1) from my quantum gravity era. Without the academic pressure to write papers I am less and less inclined to share research. 

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
