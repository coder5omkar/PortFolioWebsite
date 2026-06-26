# Portfolio Website — Visual Editor + 3D Slide Deck

<p align="center">
  <img src="https://img.shields.io/badge/status-production-ready-brightgreen" alt="Status">
  <img src="https://img.shields.io/badge/Three.js-r128-blueviolet" alt="Three.js">
  <img src="https://img.shields.io/badge/Font_Awesome-6.5.1-528DD7" alt="Font Awesome">
  <img src="https://img.shields.io/badge/license-MIT-blue" alt="License">
  <img src="https://img.shields.io/badge/PRs-welcome-orange" alt="PRs Welcome">
</p>

A self-contained portfolio generator built for **Forward Deployed Engineers**. Fill in your data in the visual editor, hit **Generate HTML**, and get a production-ready single-file portfolio featuring a 3D Three.js background, full-screen slide deck, and an ADHD Superpowers section.

---

## ✨ Features at a Glance

### 🎬 Slide Deck
- **4 full-screen slides** with keyboard navigation (`↑ ↓ ← →`, `Home`, `End`), mouse wheel, and touch swipe support
- Slide counter & progress dots
- Split-panel layout on slides 0–2 for side-by-side content

### 📋 Sections
| Slide | Content |
|-------|---------|
| **0** | Hero (name, tagline, highlights, CTA) + About (photo, bio, stats) |
| **1** | Skills (editable categories with tags) + Projects (cards with GitHub links) |
| **2** | Experience (timeline) + Contact (click-to-copy email, social links) |
| **3** | ADHD Superpowers (8 expandable cards with intensity bars + golden CTA) |

### ⚡ Superpowers Section
- 8 cards in a 2×4 grid — each with icon, title, tagline, description, and intensity meter
- **Click any card** to open a pop-out modal with full-size readable text
- Can be disabled entirely from the editor

### 🎨 Visual Design
- Dark theme with **pink → purple → blue** gradient accents
- Gold gradient "Superpowers" badge centered in the nav bar
- Animated 3D background: stars, floating orbs, rotating icosahedron, orbiting particles
- Slide-reveal animations on content
- Responsive layout with hamburger menu & stacked mobile views

### 🛠️ Editor Features
- Sidebar navigation across **8 sections**
- Dynamic **add / remove** for skill categories, projects, experience items, and superpower cards
- Photo upload with live circular preview
- GitHub URL field per project (auto-prefixes `https://` if missing)
- Social links: GitHub, LinkedIn, Docker
- Reset to defaults button
- Generates a fully self-contained `.html` file with all data inlined

---

## 🚀 Getting Started

| File | Purpose |
|------|---------|
| `editor.html` | **Visual editor** — form-based UI to edit all content and download the final HTML |
| `index.html` | Pre-built example portfolio (same output as the editor generates) |
| `config.js` | External data file used by `index.html` (not needed for `editor.html`) |

**Quick start:**

```bash
# 1. Open the editor in your browser
open editor.html

# 2. Fill in your data across all sections
# 3. Upload a profile photo (optional)
# 4. Add GitHub repo URLs to each project
# 5. Click "Generate HTML" → downloads standalone portfolio.html
# 6. Open portfolio.html or deploy to any static host
```

---

## 🧱 Tech Stack

| Technology | Usage |
|------------|-------|
| **Three.js** (r128) | 3D background scene |
| **Font Awesome** 6.5.1 | Icons |
| **Vanilla HTML / CSS / JS** | Core application — no frameworks, no build step, no dependencies |

---

## 🌐 Deployment

The generated `portfolio.html` is a **single file** — deploy it anywhere:

<p align="center">
  <code>GitHub Pages</code> •
  <code>Netlify</code> •
  <code>Vercel</code> •
  <code>Any static file host</code>
</p>

---

<p align="center">
  <sub>Built with ❤️ for engineers who ship.</sub>
</p>
