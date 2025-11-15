---
layout: page
title: Blog
permalink: /en/blog/
lang: en
---

<div class="container py-5">
  <!-- Hero Section -->
  <div class="mb-5 pb-4 border-bottom-2" style="border-bottom: 2px solid #f0f0f0; padding-bottom: 2rem;">
    <h1 class="display-4 fw-bold mb-3">Automation Engineering Blog</h1>
    <p class="lead text-muted mb-0">Explore my comprehensive collection of articles on automation, RPA, DevOps, and industry best practices. Each article is crafted to provide practical, actionable insights.</p>
  </div>

  <!-- Filter Section -->
  <div class="mb-5">
    <div class="d-flex align-items-center gap-3 mb-4">
      {% assign blog_posts = site.posts | where_exp: "post", "post.lang != 'id'" %}
      <span class="text-muted small fw-bold">📊 Total Posts: <strong>{{ blog_posts.size }}</strong></span>
    </div>
  </div>

  <!-- Posts Grid -->
  <div class="row g-4">
    {% for post in site.posts %}
      {% if post.lang != 'id' %}
        <div class="col-12">
          <article class="card post-card border-0 shadow-sm h-100" style="transition: all 0.3s ease; border-radius: 8px;">
            <div class="card-body p-5">
              <div class="d-flex justify-content-between align-items-start mb-3">
                <div style="flex: 1;">
                  <h3 class="card-title fw-bold mb-2">
                    <a href="{{ post.url | relative_url }}" class="text-decoration-none" style="color: #111; transition: color 0.3s ease;">
                      {{ post.title }}
                    </a>
                  </h3>
                  <div class="post-meta small text-muted mb-3">
                    <span style="display: inline-block; margin-right: 1rem;">📅 {{ post.date | date: "%B %d, %Y" }}</span>
                    {% if post.categories %}
                      <span style="display: inline-block;">
                        📂
                        {% for category in post.categories %}
                          <a href="/en/categories/#{{ category | slugify }}" class="badge bg-info text-dark me-1" style="text-decoration: none; transition: all 0.3s ease;">
                            {{ category }}
                          </a>
                        {% endfor %}
                      </span>
                    {% endif %}
                  </div>
                </div>
              </div>
              <p class="card-text text-muted mb-4 lh-lg">{{ post.excerpt | strip_html | truncatewords: 40 }}</p>
              <a href="{{ post.url | relative_url }}" class="btn btn-sm btn-primary fw-bold" style="border-radius: 6px; padding: 0.5rem 1.25rem; transition: all 0.3s ease;">
                Read More →
              </a>
            </div>
          </article>
        </div>
      {% endif %}
    {% endfor %}
  </div>

  <!-- Empty State -->
  {% if blog_posts.size == 0 %}
    <div class="text-center py-5">
      <h4 class="text-muted mb-3">📝 No Posts Yet</h4>
      <p class="text-muted">Posts will appear here. Check back soon!</p>
    </div>
  {% endif %}
</div>

<style>
  .post-card {
    overflow: hidden;
  }

  .post-card:hover {
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.12) !important;
    transform: translateY(-4px);
  }

  .post-card .card-title a:hover {
    color: var(--accent, #11a8cd) !important;
  }

  .post-card .badge:hover {
    opacity: 0.8;
    transform: translateY(-2px);
  }

  .post-card .btn:hover {
    transform: translateX(4px);
  }
</style>
