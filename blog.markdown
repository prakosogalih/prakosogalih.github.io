---
layout: page
title: Blog
permalink: /blog/
lang: id
---

<div class="container py-4">
  <h1 class="mb-4">Semua Artikel</h1>
  <div class="row">
    {% for post in site.posts %}
      {% if post.lang != 'en' %}
        <div class="col-12 mb-3">
          <div class="card">
            <div class="card-body">
              <h5 class="card-title"><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h5>
              <h6 class="card-subtitle mb-2 text-muted">{{ post.date | date: "%d %B %Y" }}</h6>
              {% if post.categories %}
                <p class="mb-2">
                  {% for category in post.categories %}
                    <span class="badge bg-secondary">{{ category }}</span>
                  {% endfor %}
                </p>
              {% endif %}
              <p class="card-text">{{ post.excerpt }}</p>
              <a href="{{ post.url | relative_url }}" class="btn btn-sm btn-primary">Baca selengkapnya</a>
            </div>
          </div>
        </div>
      {% endif %}
    {% endfor %}
  </div>
</div>
