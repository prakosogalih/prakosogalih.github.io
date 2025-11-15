---
layout: page
title: Categories
permalink: /en/categories/
lang: en
---

<div class="container py-4">
  <h1 class="mb-4">Post Categories</h1>
  <p>Browse posts by category to find content related to your interests.</p>

  {% assign categories = site.posts | map: 'categories' | join: ',' | split: ',' | uniq | sort %}

  <div class="accordion" id="categoriesAccordionEn">
  {% for category in categories %}
    {% if category != "" %}
      <div class="accordion-item">
        <h2 class="accordion-header" id="heading-en-{{ category | slugify }}">
          <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapse-en-{{ category | slugify }}" aria-expanded="false" aria-controls="collapse-en-{{ category | slugify }}">
            {{ category }}
          </button>
        </h2>
        <div id="collapse-en-{{ category | slugify }}" class="accordion-collapse collapse" aria-labelledby="heading-en-{{ category | slugify }}" data-bs-parent="#categoriesAccordionEn">
          <div class="accordion-body">
            <ul class="list-unstyled">
              {% for post in site.posts %}
                {% if post.categories contains category and (post.lang == 'en' or post.lang == nil) %}
                  <li class="mb-2">
                    <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
                    <small class="text-muted"> — {{ post.date | date: "%b %d, %Y" }}</small>
                  </li>
                {% endif %}
              {% endfor %}
            </ul>
          </div>
        </div>
      </div>
    {% endif %}
  {% endfor %}
  </div>
</div>
