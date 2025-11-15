---
layout: page
title: Categories
permalink: /en/categories/
lang: en
---

# Post Categories

Browse posts by category to find content related to your interests.

{% assign categories = site.posts | map: 'categories' | join: ',' | split: ',' | uniq | sort %}

{% for category in categories %}
  {% if category != "" %}
    <h3>{{ category }}</h3>
    <ul>
      {% for post in site.posts %}
        {% if post.categories contains category and (post.lang == 'en' or post.lang == nil) %}
          <li>
            <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
            <span class="post-date">{{ post.date | date: "%b %d, %Y" }}</span>
          </li>
        {% endif %}
      {% endfor %}
    </ul>
  {% endif %}
{% endfor %}
