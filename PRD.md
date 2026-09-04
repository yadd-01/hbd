# Product Requirements Document (PRD)
## Web Ulang Tahun Interaktif - Happy Birthday Website

---

## 1. Overview

| Item | Detail |
|------|--------|
| **Project Name** | HBD Website |
| **Version** | 1.0.0 |
| **Target Launch** | 04 September 2026 |
| **Framework** | Django 5.x (Python) |
| **Deployment** | PythonAnywhere |
| **Platform** | Web (Responsive) |

---

## 2. Problem Statement

Membuat website pribadi yang interaktif dan romantis untuk mengucapkan selamat ulang tahun sekaligus hari jadian kepada pacar, dengan nuansa personal dan momen yang memorable.

---

## 3. Goals & Objectives

| Goal | Metric |
|------|--------|
| Website bisa diakses publik | URL aktif di PythonAnywhere |
| Tampilan responsif | Optimal di mobile & desktop |
| Interaktif | Minimal 5 interaksi user |
| Romantis & personal | Sentuhan personal di setiap section |
| Loading cepat | < 3 detik pada koneksi normal |

---

## 4. Target User

- **Primary User**: Pacar (target penerima)
- **Secondary User**: Pembuat (admin)

---

## 5. Functional Requirements

### 5.1 Landing Page (Countdown)

| ID | Requirement | Priority | Status |
|----|-------------|----------|--------|
| F-001 | Countdown timer real-time ke 04 September 2026 | High | TODO |
| F-002 | Animated gradient background (pink → purple) | High | TODO |
| F-003 | Efek typewriter untuk nama pacar | High | TODO |
| F-004 | Tombol "Buka Hadiah" dengan glow effect | High | TODO |
| F-005 | Floating love particles | Medium | TODO |
| F-006 | Auto-play musik saat klik tombol | Medium | TODO |

### 5.2 Main Page

| ID | Requirement | Priority | Status |
|----|-------------|----------|--------|
| F-010 | Navigasi antar section | High | TODO |
| F-011 | Floating hearts particles | Medium | TODO |
| F-012 | Music player dengan play/pause | Medium | TODO |

### 5.3 Galeri Foto

| ID | Requirement | Priority | Status |
|----|-------------|----------|--------|
| F-020 | Carousel/slider foto | High | TODO |
| F-021 | Navigasi prev/next | High | TODO |
| F-022 | Lightbox untuk zoom foto | Medium | TODO |
| F-023 | Auto-play slideshow | Low | TODO |
| F-024 | Caption per foto | Medium | TODO |

### 5.4 Pesan Personal

| ID | Requirement | Priority | Status |
|----|-------------|----------|--------|
| F-030 | Teks muncul dengan efek typewriter | High | TODO |
| F-031 | Triggered saat section visible | Medium | TODO |
| F-032 | Background kertas bertekstur | Low | TODO |

### 5.5 Surat Cinta (Love Letter)

| ID | Requirement | Priority | Status |
|----|-------------|----------|--------|
| F-040 | Animasi amplop membuka | High | TODO |
| F-041 | Surat keluar dari amplop | High | TODO |
| F-042 | Teks surat muncul per kata | High | TODO |
| F-043 | Efek kertas bertekstur | Medium | TODO |
| F-044 | Confetti saat surat terbuka | Medium | TODO |

### 5.6 Timeline Cinta

| ID | Requirement | Priority | Status |
|----|-------------|----------|--------|
| F-050 | Garis waktu visual | High | TODO |
| F-051 | Milestone: Pertama kenal | Medium | TODO |
| F-052 | Milestone: Jadian (04 Sep) | High | TODO |
| F-053 | Milestone: Momen penting lainnya | Medium | TODO |
| F-054 | Icon per milestone | Low | TODO |

### 5.7 Efek & Animasi

| ID | Requirement | Priority | Status |
|----|-------------|----------|--------|
| F-060 | Confetti celebration | High | TODO |
| F-061 | Floating hearts particles | High | TODO |
| F-062 | Transisi halus antar section | Medium | TODO |
| F-063 | Parallax scrolling | Low | TODO |

### 5.8 Musik

| ID | Requirement | Priority | Status |
|----|-------------|----------|--------|
| F-070 | Background music player | Medium | TODO |
| F-071 | Kontrol play/pause | High | TODO |
| F-072 | Volume control | Low | TODO |
| F-073 | Musik otomatis play (dengan interaksi user) | Medium | TODO |

---

## 6. Non-Functional Requirements

| Category | Requirement |
|----------|-------------|
| **Performance** | Loading time < 3 detik |
| **Compatibility** | Chrome, Firefox, Safari, Edge |
| **Responsive** | Mobile (320px+) sampai Desktop (1920px) |
| **Accessibility** | Semantic HTML, alt text pada gambar |
| **Security** | Tidak ada sensitive data exposed |
| **SEO** | Meta tags untuk sharing di social media |

---

## 7. Tech Stack

| Layer | Technology |
|-------|------------|
| Backend | Django 5.x |
| Frontend | HTML5, CSS3, JavaScript (Vanilla) |
| Animations | CSS Animations, Canvas API |
| Particles | Custom JavaScript |
| Music | HTML5 Audio API |
| Database | SQLite |
| Deployment | PythonAnywhere |

---

## 8. User Flow

```
┌─────────────────────────────────────────────────────────────┐
│                     LANDING PAGE                            │
│  - Countdown Timer                                          │
│  - Nama Pacar (Typewriter)                                  │
│  - Tombol "Buka Hadiah"                                     │
└─────────────────────────┬───────────────────────────────────┘
                          │ Klik Tombol
                          ▼
┌─────────────────────────────────────────────────────────────┐
│                      MAIN PAGE                              │
│  ┌──────────┬──────────┬──────────┬──────────┐              │
│  │ Galeri   │ Pesan    │ Surat    │ Timeline │              │
│  │ Foto     │ Personal │ Cinta    │ Cinta    │              │
│  └──────────┴──────────┴──────────┴──────────┘              │
│  + Floating Hearts + Music Player                           │
└─────────────────────────────────────────────────────────────┘
```

---

## 9. Data Models

### 9.1 Photo Model
```python
class Photo(models.Model):
    image = models.ImageField(upload_to='photos/')
    caption = models.CharField(max_length=200, blank=True)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
```

### 9.2 Timeline Model
```python
class TimelineEvent(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    date = models.DateField()
    icon = models.CharField(max_length=50, default='❤️')
    order = models.IntegerField(default=0)
```

### 9.3 Letter Model
```python
class LoveLetter(models.Model):
    content = models.TextField()
    author = models.CharField(max_length=100, default='Untukmu')
    created_at = models.DateTimeField(auto_now_add=True)
```

---

## 10. Milestones

| Phase | Description | Estimasi |
|-------|-------------|----------|
| Phase 1 | Setup Django + Struktur | 15 menit |
| Phase 2 | Landing Page + Countdown | 20 menit |
| Phase 3 | Main Page + Navigasi | 15 menit |
| Phase 4 | Galeri Foto | 15 menit |
| Phase 5 | Surat Cinta | 15 menit |
| Phase 6 | Timeline | 10 menit |
| Phase 7 | Efek & Animasi | 15 menit |
| Phase 8 | Musik Player | 10 menit |
| Phase 9 | Responsive + Polish | 15 menit |
| Phase 10 | Testing + Deployment | 15 menit |
| **Total** | | **~2.5 jam** |

---

## 11. Success Criteria

- [ ] Website bisa diakses via URL publik
- [ ] Countdown timer akurat ke 04 September 2026
- [ ] Semua section berfungsi dengan baik
- [ ] Foto galeri bisa navigasi
- [ ] Musik bisa play/pause
- [ ] Efek animasi berjalan smooth
- [ ] Tampilan responsif di mobile
- [ ] Pacar tersenyum saat buka website 😊

---

## 12. Risks & Mitigations

| Risk | Impact | Mitigation |
|------|--------|------------|
| PythonAnywhere free tier limit | Medium | Gunakan layanan minimal |
| Musik belum ada | Low | Gunakan royalty free music |
| Foto terlalu besar | Medium | Compress sebelum upload |
| Browser compatibility | Low | Test di 4 browser utama |

---

## 13. Future Enhancement

- Guestbook untuk tamu
- Video player
- Quiz "Seberapa kenal kamu sama aku"
- Efek 3D
- Dark/Light mode toggle

---

*Document created: September 4, 2026*
*Author: Opencode Assistant*
