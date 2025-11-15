---
layout: page
title: Home
lang: en
---

<div class="container py-5">
  <div class="row">
    <div class="col-lg-8">
      <!-- Topics Grid -->
      <div class="mb-5">
        <h3 class="mb-4 fw-bold">What You'll Find Here</h3>
        <div class="row g-3">
          <div class="col-md-6">
            <div class="topic-card p-3 rounded-3 bg-light border">
              <h6 class="fw-bold text-primary mb-2">⚙️ Process Automation</h6>
              <p class="small text-muted mb-0">Strategies for workflow optimization and business process automation</p>
            </div>
          </div>
          <div class="col-md-6">
            <div class="topic-card p-3 rounded-3 bg-light border">
              <h6 class="fw-bold text-primary mb-2">🤖 Robotic Process Automation</h6>
              <p class="small text-muted mb-0">Efficient implementation of bots and intelligent automation</p>
            </div>
          </div>
          <div class="col-md-6">
            <div class="topic-card p-3 rounded-3 bg-light border">
              <h6 class="fw-bold text-primary mb-2">🧪 Test Automation</h6>
              <p class="small text-muted mb-0">Automated testing practices and QA engineering</p>
            </div>
          </div>
          <div class="col-md-6">
            <div class="topic-card p-3 rounded-3 bg-light border">
              <h6 class="fw-bold text-primary mb-2">📊 DevOps Automation</h6>
              <p class="small text-muted mb-0">Infrastructure automation and continuous deployment</p>
            </div>
          </div>
          <div class="col-md-6">
            <div class="topic-card p-3 rounded-3 bg-light border">
              <h6 class="fw-bold text-primary mb-2">🔧 System Integration</h6>
              <p class="small text-muted mb-0">Building seamless integrations between systems</p>
            </div>
          </div>
          <div class="col-md-6">
            <div class="topic-card p-3 rounded-3 bg-light border">
              <h6 class="fw-bold text-primary mb-2">💡 Best Practices</h6>
              <p class="small text-muted mb-0">Industry standards and best optimization techniques</p>
            </div>
          </div>
        </div>
      </div>

      <!-- Articles Section -->
      <div class="articles-section">
        <div class="d-flex justify-content-between align-items-center mb-4">
          <h3 class="fw-bold mb-0">Latest Articles</h3>
          <a href="/blog/" class="btn btn-sm btn-outline-primary">View All</a>
        </div>
        <p class="text-muted mb-4">Explore my latest articles organized by topic and date. Choose categories that interest you.</p>

        <!-- Post List -->
        <div class="posts-container">
          {% assign posts = site.posts | sort: 'date' | reverse %}
          {% for post in posts limit:6 %}
              <article class="post-preview card mb-4 border-0">
                <div class="card-body p-4">
                  <div class="d-flex justify-content-between align-items-start mb-3">
                    <div>
                      <h5 class="card-title fw-bold mb-2">
                        <a href="{{ post.url | relative_url }}" class="text-decoration-none">{{ post.title }}</a>
                      </h5>
                      <div class="post-meta small text-muted mb-3">
                        <span class="me-3">📅 {{ post.date | date: "%d %b %Y" }}</span>
                        {% if post.categories %}
                          <span>📂
                            {% for category in post.categories %}
                              <a href="/categories/#{{ category | slugify }}" class="badge bg-info text-dark me-1">{{ category }}</a>
                            {% endfor %}
                          </span>
                        {% endif %}
                      </div>
                    </div>
                  </div>
                  <p class="card-text text-muted mb-3">{{ post.excerpt | strip_html | truncatewords: 30 }}</p>
                  <a href="{{ post.url | relative_url }}" class="btn btn-sm btn-primary">Read More →</a>
                </div>
              </article>
            {% endfor %}
          {% if posts.size == 0 %}
            <div class="alert alert-info" role="alert">
              No articles published yet. Check back later! 📝
            </div>
          {% endif %}
        </div>

        <!-- Call to Action -->
        {% if posts.size > 6 %}
          <div class="text-center mt-5">
            <a href="/blog/" class="btn btn-lg btn-primary">View All Articles</a>
          </div>
        {% endif %}
      </div>

      <!-- CTA Section -->
      <div class="cta-section mt-5 p-4 rounded-3 bg-primary bg-opacity-10 border border-primary border-opacity-25">
        <h4 class="fw-bold mb-3">Want to Connect?</h4>
        <p class="mb-3">Interested in discussing automation engineering? Find me on the following social platforms:</p>
        <div class="d-flex gap-2 flex-wrap">
          <a href="https://twitter.com/prakosogalih" target="_blank" class="btn btn-outline-primary">🐦 Twitter</a>
          <a href="https://github.com/prakosogalih" target="_blank" class="btn btn-outline-primary">🔗 GitHub</a>
          <a href="mailto:prakosogalih@proton.me" class="btn btn-outline-primary">✉️ Email</a>
        </div>
      </div>
    </div>

    <!-- Sidebar (optional for future widgets) -->
    <div class="col-lg-4">
      <aside class="sidebar">
        <div class="card mb-4">
          <div class="card-body">
            <h6 class="card-title fw-bold mb-3">About This Blog</h6>
            <p class="small text-muted">This blog contains articles and insights about automation engineering, tools, and best practices to optimize your workflow.</p>
          </div>
        </div>

        <div class="card">
          <div class="card-body">
            <h6 class="card-title fw-bold mb-3">Popular Categories</h6>
            <div class="d-flex flex-wrap gap-2">
              {% assign all_categories = site.posts | map: 'categories' | join: ',' | split: ',' | uniq | sort %}
              {% for category in all_categories limit:8 %}
                {% if category != "" %}
                  <a href="/categories/#{{ category | slugify }}" class="badge bg-secondary text-decoration-none">{{ category }}</a>
                {% endif %}
              {% endfor %}
            </div>
          </div>
        </div>
      </aside>
    </div>
  </div>
</div>

<style>
  .topic-card {
    transition: all 0.3s ease;
    cursor: pointer;
  }

  .topic-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    border-color: var(--primary) !important;
  }

  .post-preview {
    transition: all 0.3s ease;
  }

  .post-preview:hover {
    box-shadow: 0 4px 16px rgba(0,0,0,0.12);
    transform: translateY(-2px);
  }

  .post-preview .card-title a {
    color: #111;
  }

  .post-preview .card-title a:hover {
    color: var(--accent);
  }

  .hero-section {
    border-bottom: 2px solid #f0f0f0;
    padding-bottom: 2rem;
  }

  .cta-section {
    border-left: 44px solid var(--primary);
  }

  .sidebar {
    position: sticky;
    top: 20px;
  }

  @media (max-width: 991px) {
    .sidebar {
      position: relative;
      top: auto;
      margin-top: 2rem;
    }
  }
</style>
