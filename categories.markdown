---
layout: page
title: Kategori
permalink: /categories/
lang: id
---

<div class="container py-4">
  <p>Jelajahi artikel berdasarkan kategori untuk menemukan konten yang sesuai dengan minat Anda.</p>

  {% assign categories = site.posts | map: 'categories' | join: ',' | split: ',' | uniq | sort %}

  <div class="accordion" id="categoriesAccordion">
  {% for category in categories %}
    {% if category != "" %}
      <div class="accordion-item">
        <h2 class="accordion-header" id="heading-{{ category | slugify }}">
          <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapse-{{ category | slugify }}" aria-expanded="false" aria-controls="collapse-{{ category | slugify }}">
            {{ category }}
          </button>
        </h2>
        <div id="collapse-{{ category | slugify }}" class="accordion-collapse collapse" aria-labelledby="heading-{{ category | slugify }}" data-bs-parent="#categoriesAccordion">
          <div class="accordion-body">
            <ul class="list-unstyled">
              {% for post in site.posts %}
                {% if post.categories contains category and post.lang != 'en' %}
                  <li class="mb-2">
                    <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
                    <small class="text-muted"> — {{ post.date | date: "%d %b %Y" }}</small>
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
