# Design Document
## Web Ulang Tahun Interaktif - Architecture & UI/UX

---

## 1. System Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                        CLIENT (Browser)                         │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐             │
│  │   HTML5     │  │   CSS3      │  │ JavaScript  │             │
│  │  Templates  │  │   Styles    │  │   Scripts   │             │
│  └─────────────┘  └─────────────┘  └─────────────┘             │
│         │               │                │                      │
│         └───────────────┴────────────────┘                      │
│                         │                                       │
│                    Static Files                                 │
│                   (CSS, JS, Images)                             │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
                              │
                              │ HTTP Request
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                      DJANGO SERVER                               │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐             │
│  │    URL      │  │    View     │  │  Template   │             │
│  │  Router     │──│  Handler    │──│   Engine    │             │
│  └─────────────┘  └─────────────┘  └─────────────┘             │
│         │               │                │                      │
│         │               ▼                                       │
│         │        ┌─────────────┐                                │
│         │        │   Models    │                                │
│         │        │  (SQLite)   │                                │
│         │        └─────────────┘                                │
│         │               │                                       │
│         │               ▼                                       │
│         │        ┌─────────────┐                                │
│         └───────►│   Static    │                                │
│                  │   Files     │                                │
│                  └─────────────┘                                │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                     PYTHONANYWHERE                               │
├─────────────────────────────────────────────────────────────────┤
│  - WSGI Application                                             │
│  - Static Files Serving                                         │
│  - SQLite Database                                              │
│  - Public URL                                                   │
└─────────────────────────────────────────────────────────────────┘
```

---

## 2. UI/UX Design

### 2.1 Color Palette

| Color | Hex Code | Usage |
|-------|----------|-------|
| Primary Pink | #FF6B9D | Background, accents |
| Primary Purple | #C44DFF | Gradients, hover effects |
| Light Pink | #FFE5F0 | Light backgrounds |
| Gold | #FFD700 | Highlights, buttons |
| White | #FFFFFF | Text on dark backgrounds |
| Dark | #1a1a2e | Text, shadows |

### 2.2 Typography

| Element | Font | Size | Weight |
|---------|------|------|--------|
| Headings | 'Dancing Script' (cursive) | 48-72px | Bold |
| Body Text | 'Poppins' (sans-serif) | 16-18px | Regular |
| Accent Text | 'Dancing Script' | 24-32px | Regular |
| Countdown | 'Orbitron' (monospace) | 32-48px | Bold |

### 2.3 Layout Structure

```
┌─────────────────────────────────────────────────────────────────┐
│                    LANDING PAGE                                  │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │                    Gradient Background                   │    │
│  │                                                         │    │
│  │              ✨ Happy Birthday ✨                        │    │
│  │                                                         │    │
│  │            [Nama Pacar] (Typewriter)                   │    │
│  │                                                         │    │
│  │         ┌─────────────────────────────┐                 │    │
│  │         │     COUNTDOWN TIMER         │                 │    │
│  │         │  00 : 00 : 00 : 00          │                 │    │
│  │         │  Hari  Jam  Menit Detik     │                 │    │
│  │         └─────────────────────────────┘                 │    │
│  │                                                         │    │
│  │         ┌─────────────────────────────┐                 │    │
│  │         │     🎁 Buka Hadiah 🎁       │                 │    │
│  │         └─────────────────────────────┘                 │    │
│  │                                                         │    │
│  │              💕 Floating Hearts 💕                       │    │
│  └─────────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                    MAIN PAGE                                     │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │  [🏠 Home] [📷 Galeri] [💌 Surat] [📅 Timeline]        │    │
│  └─────────────────────────────────────────────────────────┘    │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │                   SECTION 1                             │    │
│  │                   Galeri Foto                           │    │
│  │  ┌─────────────────────────────────────────────────┐   │    │
│  │  │         ← [  Foto  ] →                          │   │    │
│  │  │         Caption foto                             │   │    │
│  │  └─────────────────────────────────────────────────┘   │    │
│  └─────────────────────────────────────────────────────────┘    │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │                   SECTION 2                             │    │
│  │                   Pesan Personal                        │    │
│  │  ┌─────────────────────────────────────────────────┐   │    │
│  │  │  "Pesan yang muncul dengan efek typewriter..."  │   │    │
│  │  └─────────────────────────────────────────────────┘   │    │
│  └─────────────────────────────────────────────────────────┘    │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │                   SECTION 3                             │    │
│  │                   Surat Cinta                           │    │
│  │  ┌─────────────────────────────────────────────────┐   │    │
│  │  │              📩 Amplop                           │   │    │
│  │  │         (Klik untuk membuka)                    │   │    │
│  │  │              ↓                                  │   │    │
│  │  │         📜 Surat                                │   │    │
│  │  │         (Teks muncul)                          │   │    │
│  │  └─────────────────────────────────────────────────┘   │    │
│  └─────────────────────────────────────────────────────────┘    │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │                   SECTION 4                             │    │
│  │                   Timeline Cinta                        │    │
│  │                                                         │    │
│  │    ●─────────●─────────●─────────●                      │    │
│  │    │         │         │         │                      │    │
│  │  Kenal     Jadian    ...       ...                     │    │
│  │  202X      04 Sep                                   │    │
│  └─────────────────────────────────────────────────────────┘    │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │              🎵 Music Player                            │    │
│  │              [▶ Play] [⏸ Pause] [🔊 Vol]              │    │
│  └─────────────────────────────────────────────────────────┘    │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │              💕 Floating Hearts (sepanjang halaman)     │    │
│  └─────────────────────────────────────────────────────────┘    │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## 3. CSS Animations

### 3.1 Gradient Background
```css
@keyframes gradientShift {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

.landing {
    background: linear-gradient(135deg, #FF6B9D, #C44DFF, #FF6B9D);
    background-size: 400% 400%;
    animation: gradientShift 8s ease infinite;
}
```

### 3.2 Typewriter Effect
```css
@keyframes typewriter {
    from { width: 0; }
    to { width: 100%; }
}

@keyframes blink {
    50% { border-color: transparent; }
}

.typewriter {
    overflow: hidden;
    border-right: 3px solid #FFD700;
    white-space: nowrap;
    animation: typewriter 3s steps(40) 1s forwards,
               blink 0.75s step-end infinite;
}
```

### 3.3 Floating Hearts
```css
@keyframes float {
    0% {
        transform: translateY(100vh) rotate(0deg);
        opacity: 1;
    }
    100% {
        transform: translateY(-100vh) rotate(720deg);
        opacity: 0;
    }
}

.heart {
    position: fixed;
    animation: float linear infinite;
}
```

### 3.4 Glow Button
```css
@keyframes glow {
    0% { box-shadow: 0 0 5px #FF6B9D, 0 0 10px #FF6B9D; }
    50% { box-shadow: 0 0 20px #FF6B9D, 0 0 30px #C44DFF; }
    100% { box-shadow: 0 0 5px #FF6B9D, 0 0 10px #FF6B9D; }
}

.btn-glow {
    animation: glow 2s ease-in-out infinite;
}
```

### 3.5 Envelope Open
```css
@keyframes openEnvelope {
    0% { transform: rotateX(0deg); }
    100% { transform: rotateX(-180deg); }
}

.envelope-flap {
    transform-origin: top;
    transition: transform 0.6s ease;
}

.envelope.open .envelope-flap {
    animation: openEnvelope 0.6s ease forwards;
}
```

---

## 4. JavaScript Modules

### 4.1 countdown.js
```javascript
// Countdown Timer Module
const Countdown = {
    targetDate: new Date('2026-09-04T00:00:00').getTime(),
    
    init() {
        this.update();
        setInterval(() => this.update(), 1000);
    },
    
    update() {
        const now = new Date().getTime();
        const distance = this.targetDate - now;
        
        const days = Math.floor(distance / (1000 * 60 * 60 * 24));
        const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
        const seconds = Math.floor((distance % (1000 * 60)) / 1000);
        
        // Update DOM
        document.getElementById('days').textContent = days.toString().padStart(2, '0');
        document.getElementById('hours').textContent = hours.toString().padStart(2, '0');
        document.getElementById('minutes').textContent = minutes.toString().padStart(2, '0');
        document.getElementById('seconds').textContent = seconds.toString().padStart(2, '0');
    }
};
```

### 4.2 particles.js
```javascript
// Floating Hearts Particles Module
const Particles = {
    container: null,
    hearts: ['❤️', '💕', '💖', '💗', '💝'],
    
    init(containerId) {
        this.container = document.getElementById(containerId);
        this.createParticles();
    },
    
    createParticles() {
        setInterval(() => {
            const heart = document.createElement('div');
            heart.className = 'heart';
            heart.textContent = this.hearts[Math.floor(Math.random() * this.hearts.length)];
            heart.style.left = Math.random() * 100 + 'vw';
            heart.style.animationDuration = (Math.random() * 3 + 4) + 's';
            heart.style.fontSize = (Math.random() * 20 + 10) + 'px';
            
            this.container.appendChild(heart);
            
            setTimeout(() => heart.remove(), 7000);
        }, 300);
    }
};
```

### 4.3 confetti.js
```javascript
// Confetti Effect Module
const Confetti = {
    canvas: null,
    ctx: null,
    particles: [],
    colors: ['#FF6B9D', '#C44DFF', '#FFD700', '#FFE5F0', '#FFFFFF'],
    
    init() {
        this.canvas = document.getElementById('confetti-canvas');
        this.ctx = this.canvas.getContext('2d');
        this.resize();
        window.addEventListener('resize', () => this.resize());
    },
    
    resize() {
        this.canvas.width = window.innerWidth;
        this.canvas.height = window.innerHeight;
    },
    
    burst(x, y, count = 100) {
        for (let i = 0; i < count; i++) {
            this.particles.push({
                x: x,
                y: y,
                vx: (Math.random() - 0.5) * 20,
                vy: (Math.random() - 0.5) * 20 - 10,
                color: this.colors[Math.floor(Math.random() * this.colors.length)],
                size: Math.random() * 8 + 4,
                rotation: Math.random() * 360,
                rotationSpeed: (Math.random() - 0.5) * 10,
                gravity: 0.3,
                opacity: 1
            });
        }
        this.animate();
    },
    
    animate() {
        this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);
        
        this.particles = this.particles.filter(p => p.opacity > 0);
        
        this.particles.forEach(p => {
            p.x += p.vx;
            p.y += p.vy;
            p.vy += p.gravity;
            p.rotation += p.rotationSpeed;
            p.opacity -= 0.01;
            
            this.ctx.save();
            this.ctx.translate(p.x, p.y);
            this.ctx.rotate(p.rotation * Math.PI / 180);
            this.ctx.fillStyle = p.color;
            this.ctx.globalAlpha = p.opacity;
            this.ctx.fillRect(-p.size / 2, -p.size / 2, p.size, p.size);
            this.ctx.restore();
        });
        
        if (this.particles.length > 0) {
            requestAnimationFrame(() => this.animate());
        }
    }
};
```

### 4.4 gallery.js
```javascript
// Photo Gallery Module
const Gallery = {
    photos: [],
    currentIndex: 0,
    
    init(photos) {
        this.photos = photos;
        this.render();
        this.bindEvents();
    },
    
    render() {
        const container = document.getElementById('gallery-container');
        container.innerHTML = `
            <div class="gallery-slide">
                <img src="${this.photos[this.currentIndex].url}" alt="${this.photos[this.currentIndex].caption}">
                <p class="caption">${this.photos[this.currentIndex].caption}</p>
            </div>
            <button class="prev">←</button>
            <button class="next">→</button>
        `;
    },
    
    next() {
        this.currentIndex = (this.currentIndex + 1) % this.photos.length;
        this.render();
    },
    
    prev() {
        this.currentIndex = (this.currentIndex - 1 + this.photos.length) % this.photos.length;
        this.render();
    },
    
    bindEvents() {
        document.addEventListener('click', (e) => {
            if (e.target.classList.contains('prev')) this.prev();
            if (e.target.classList.contains('next')) this.next();
        });
    }
};
```

---

## 5. File Structure

```
hbd_project/
├── hbd_project/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── birthday/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   └── templates/
│       └── birthday/
│           ├── base.html
│           ├── landing.html
│           └── main.html
├── static/
│   ├── css/
│   │   ├── main.css
│   │   ├── landing.css
│   │   ├── gallery.css
│   │   ├── letter.css
│   │   ├── timeline.css
│   │   └── animations.css
│   ├── js/
│   │   ├── main.js
│   │   ├── countdown.js
│   │   ├── particles.js
│   │   ├── confetti.js
│   │   ├── gallery.js
│   │   ├── music.js
│   │   ├── letter.js
│   │   └── timeline.js
│   └── images/
│       ├── photos/
│       └── assets/
│           ├── envelope.svg
│           ├── heart.svg
│           └── confetti.svg
├── media/
│   └── photos/
├── templates/
│   └── admin/
├── staticfiles/
├── manage.py
├── requirements.txt
└── .gitignore
```

---

## 6. Responsive Breakpoints

| Breakpoint | Width | Layout |
|------------|-------|--------|
| Mobile | 320px - 767px | Single column, stacked |
| Tablet | 768px - 1023px | 2 columns |
| Desktop | 1024px+ | Full layout |

---

## 7. Browser Support

| Browser | Version | Status |
|---------|---------|--------|
| Chrome | 90+ | ✅ Supported |
| Firefox | 88+ | ✅ Supported |
| Safari | 14+ | ✅ Supported |
| Edge | 90+ | ✅ Supported |

---

*Document created: September 4, 2026*
*Author: Opencode Assistant*
