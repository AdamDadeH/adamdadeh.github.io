---
title: Publications
layout: single
permalink: /publications/
---

{% for pub in site.data.publications %}

  {% if pub.type == "conference" %}
<li class="publication"><b>{{pub.date}}</b> - {{pub.authors | array_to_sentence_string: ''}}: <b>{{ pub.title }}</b>. In the proceedings of {{ pub.conference }}, {{ pub.location }} : {% for link in pub.links%}<a href="{{ link.link }}">[{{link.name}}]</a> {%endfor%}</li>
  {% endif %}

{% if pub.type == "paper" %}
<li class="publication"><b>{{pub.date}}</b> - {{pub.authors | array_to_sentence_string: ''}}: <b>{{ pub.title }}</b>. {{pub.journal}} {{pub.issue}}. {% for link in pub.links%}<a href="{{ link.link }}">[{{link.name}}]</a> {%endfor%}</li>
  {% endif %}
  
{% endfor %}
