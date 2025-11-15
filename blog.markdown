---
layout: page
title: Blog
permalink: /blog/
---

# All Posts

Here you'll find all my blog posts organized by date. Use the navigation or search to find topics that interest you.

{% for post in site.posts %}
  <h3>
    <a href="{{ post.url | relative_url }}">
      {{ post.title }}
    </a>
  </h3>
  <p class="post-date">{{ post.date | date: "%B %d, %Y" }}</p>
  {% if post.categories %}
    <p class="post-categories">
      Categories: 
      {% for category in post.categories %}
        <span class="badge">{{ category }}</span>
      {% endfor %}
    </p>
  {% endif %}
  <p>{{ post.excerpt }}</p>
  <a href="{{ post.url | relative_url }}">Read more →</a>
  <hr>
{% endfor %}
