---
layout: page
title: Beranda
lang: id
---

<div class="container py-5">
  <div class="row">
    <div class="col-lg-8">
      <!-- Hero Section -->
      <div class="hero-section mb-5">
        <h1 class="display-5 fw-bold mb-3">Selamat Datang di Blog Automation Engineering Saya</h1>
        <p class="lead text-muted">Halo! 👋 Saya <strong>Prakosogalih</strong>, seorang automation engineer yang berdedikasi untuk mengoptimalkan proses dan membangun sistem cerdas. Ruang ini didedikasikan untuk berbagi wawasan praktis tentang automation engineering, RPA, test automation, dan DevOps.</p>
      </div>

      <!-- Topics Grid -->
      <div class="mb-5">
        <h3 class="mb-4 fw-bold">Yang Akan Anda Temukan di Sini</h3>
        <div class="row g-3">
          <div class="col-md-6">
            <div class="topic-card p-3 rounded-3 bg-light border">
              <h6 class="fw-bold text-primary mb-2">⚙️ Otomasi Proses</h6>
              <p class="small text-muted mb-0">Strategi optimasi workflow dan otomasi proses bisnis</p>
            </div>
          </div>
          <div class="col-md-6">
            <div class="topic-card p-3 rounded-3 bg-light border">
              <h6 class="fw-bold text-primary mb-2">🤖 Robotic Process Automation</h6>
              <p class="small text-muted mb-0">Implementasi bot dan otomasi cerdas yang efisien</p>
            </div>
          </div>
          <div class="col-md-6">
            <div class="topic-card p-3 rounded-3 bg-light border">
              <h6 class="fw-bold text-primary mb-2">🧪 Test Automation</h6>
              <p class="small text-muted mb-0">Praktik pengujian otomatis dan QA engineering</p>
            </div>
          </div>
          <div class="col-md-6">
            <div class="topic-card p-3 rounded-3 bg-light border">
              <h6 class="fw-bold text-primary mb-2">📊 DevOps Automation</h6>
              <p class="small text-muted mb-0">Otomasi infrastruktur dan continuous deployment</p>
            </div>
          </div>
          <div class="col-md-6">
            <div class="topic-card p-3 rounded-3 bg-light border">
              <h6 class="fw-bold text-primary mb-2">🔧 Sistem Integrasi</h6>
              <p class="small text-muted mb-0">Membangun integrasi seamless antar sistem</p>
            </div>
          </div>
          <div class="col-md-6">
            <div class="topic-card p-3 rounded-3 bg-light border">
              <h6 class="fw-bold text-primary mb-2">💡 Best Practices</h6>
              <p class="small text-muted mb-0">Standar industri dan teknik optimasi terbaik</p>
            </div>
          </div>
        </div>
      </div>

      <!-- Articles Section -->
      <div class="articles-section">
        <div class="d-flex justify-content-between align-items-center mb-4">
          <h3 class="fw-bold mb-0">Artikel Terbaru</h3>
          <a href="/blog/" class="btn btn-sm btn-outline-primary">Lihat Semua</a>
        </div>
        <p class="text-muted mb-4">Jelajahi artikel terbaru saya yang diorganisir berdasarkan topik dan tanggal. Pilih kategori yang menarik minat Anda.</p>

        <!-- Post List -->
        <div class="posts-container">
          {% assign posts = site.posts | where_exp: "post", "post.lang != 'en'" %}
          {% if posts.size > 0 %}
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
                  <a href="{{ post.url | relative_url }}" class="btn btn-sm btn-primary">Baca Selengkapnya →</a>
                </div>
              </article>
            {% endfor %}
          {% else %}
            <div class="alert alert-info" role="alert">
              Belum ada artikel yang dipublikasikan. Kembali lagi nanti! 📝
            </div>
          {% endif %}
        </div>

        <!-- Call to Action -->
        {% if posts.size > 6 %}
          <div class="text-center mt-5">
            <a href="/blog/" class="btn btn-lg btn-primary">Lihat Semua Artikel</a>
          </div>
        {% endif %}
      </div>

      <!-- CTA Section -->
      <div class="cta-section mt-5 p-4 rounded-3 bg-primary bg-opacity-10 border border-primary border-opacity-25">
        <h4 class="fw-bold mb-3">Ingin Terhubung?</h4>
        <p class="mb-3">Tertarik untuk diskusi tentang automation engineering? Temukan saya di platform sosial berikut:</p>
        <div class="d-flex gap-2 flex-wrap">
          <a href="https://twitter.com/prakosogalih" target="_blank" class="btn btn-outline-primary">🐦 Twitter</a>
          <a href="https://github.com/prakosogalih" target="_blank" class="btn btn-outline-primary">🔗 GitHub</a>
          <a href="mailto:prakosogalih@proton.me" class="btn btn-outline-primary">✉️ Email</a>
        </div>
      </div>
    </div>

    <!-- Sidebar (optional untuk future widgets) -->
    <div class="col-lg-4">
      <aside class="sidebar">
        <div class="card mb-4">
          <div class="card-body">
            <h6 class="card-title fw-bold mb-3">Tentang Blog Ini</h6>
            <p class="small text-muted">Blog ini berisi artikel dan insights tentang automation engineering, tools, dan best practices untuk mengoptimalkan workflow Anda.</p>
          </div>
        </div>

        <div class="card">
          <div class="card-body">
            <h6 class="card-title fw-bold mb-3">Kategori Populer</h6>
            <div class="d-flex flex-wrap gap-2">
              {% assign all_categories = site.posts | where_exp: "post", "post.lang != 'en'" | map: 'categories' | join: ',' | split: ',' | uniq | sort %}
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
    border-left: 4px solid var(--primary);
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
