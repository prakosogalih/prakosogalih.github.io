---
layout: page
title: Blog
permalink: /blog/
lang: en
pagination:
  enabled: true
---

<div class="container py-5">
  <!-- Hero Section -->
  <div class="mb-5 pb-4 border-bottom-2" style="border-bottom: 2px solid #f0f0f0; padding-bottom: 2rem;">
    <h1 class="display-4 fw-bold mb-3">Automation Engineering Blog</h1>
    <p class="lead text-muted mb-0">Explore my complete collection of articles on automation, RPA, DevOps, and best practices. Each article is designed to provide practical and actionable insights.</p>
  </div>

  <!-- Debugging: Check paginator posts -->
  <p>Paginator Posts Debug: {{ paginator.posts | inspect }}</p>

  <!-- Filter Section -->
  <div class="mb-5">
    <div class="d-flex align-items-center gap-3 mb-4">
      <span class="text-muted small fw-bold">📊 Number of Articles: <strong>{{ paginator.posts.size }}</strong></span>
    </div>
  </div>

  <!-- Posts Grid -->
  <div class="row g-4">
    {% for post in paginator.posts %}
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
                    <span style="display: inline-block; margin-right: 1rem;">📅 {{ post.date | date: "%d %B %Y" }}</span>
                    {% if post.categories %}
                      <span style="display: inline-block;">
                        📂
                        {% for category in post.categories %}
                          <a href="/categories/#{{ category | slugify }}" class="badge bg-info text-dark me-1" style="text-decoration: none; transition: all 0.3s ease;">
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
    {% endfor %}
  </div>

  <!-- Pagination links -->
  {% if paginator.total_pages > 1 %}
    <nav aria-label="Page navigation">
      <ul class="pagination justify-content-center mt-5">
        {% if paginator.previous_page %}
          <li class="page-item">
            <a class="page-link" href="{{ paginator.previous_page_path | relative_url }}" aria-label="Previous">
              <span aria-hidden="true">&laquo;</span>
            </a>
          </li>
        {% else %}
          <li class="page-item disabled">
            <span class="page-link" aria-hidden="true">&laquo;</span>
          </li>
        {% endif %}

        {% for pager in paginator.array %}
          <li class="page-item {% if pager.is_active %}active{% endif %}">
            <a class="page-link" href="{{ pager.url | relative_url }}">{{ pager.title }}</a>
          </li>
        {% endfor %}

        {% if paginator.next_page %}
          <li class="page-item">
            <a class="page-link" href="{{ paginator.next_page_path | relative_url }}" aria-label="Next">
              <span aria-hidden="true">&raquo;</span>
            </a>
          </li>
        {% else %}
          <li class="page-item disabled">
            <span class="page-link" aria-hidden="true">&raquo;</span>
          </li>
        {% endif %}
      </ul>
    </nav>
  {% endif %}

  <!-- Empty State -->
  {% if paginator.posts.size == 0 %}
    <div class="text-center py-5">
      <h4 class="text-muted mb-3">📝 No Articles Yet</h4>
      <p class="text-muted">Articles will appear here. Check back later!</p>
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
