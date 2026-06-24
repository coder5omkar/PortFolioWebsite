# Portfolio Website — Visual Editor + 3D Slide Deck

A self-contained portfolio generator for Forward Deployed Engineers. Fill in your data in the **Editor**, hit **Generate HTML**, and get a production-ready single-file portfolio with a 3D Three.js background, full-screen slide deck, and an ADHD Superpowers section.

## Files

| File | Purpose |
|------|---------|
| `editor.html` | **Visual editor** — form-based UI to edit all content and download the final HTML |
| `index.html` | Pre-built example portfolio (same output as the editor generates) |
| `config.js` | External data file used by `index.html` (not needed for `editor.html`) |

## How to Use

1. Open **`editor.html`** in any modern browser
2. Fill in your data across all sections (Site, Hero, About, Skills, Projects, Experience, Contact, ADHD)
3. Upload a profile photo (optional) — replaces the avatar icon
4. Add GitHub repo URLs to each project
5. Click **"Generate HTML"** — downloads a standalone `portfolio.html`
6. Open `portfolio.html` in a browser or deploy to any static host

## Features

### Slide Deck
- 4 full-screen slides with keyboard (↑↓←→ / Home / End), mouse wheel, and touch swipe navigation
- Slide counter + progress dots
- Split-panel layout on slides 0–2 (side-by-side content)

### Sections
- **Slide 0** — Hero (name, tagline, highlights, CTA buttons) + About (photo, bio, stats)
- **Slide 1** — Skills (editable categories with tags) + Projects (cards with GitHub links)
- **Slide 2** — Experience (timeline) + Contact (click-to-copy email, social links)
- **Slide 3** — ADHD Superpowers (8 expandable cards with intensity bars + golden CTA)

### ADHD Superpowers Section
- 8 cards in a 2×4 grid, each with icon, title, tagline, description, and intensity meter
- **Click any card** to open a pop-out modal with full-size readable text
- Can be disabled entirely from the editor

### Visual Design
- Dark theme with gradient accents (pink → purple → blue)
- Gold gradient "Superpowers" badge in the center of the nav bar
- Animated 3D background (stars, floating orbs, rotating icosahedron, orbiting particles)
- Slide-reveal animations on content
- Responsive for mobile (hamburger menu, stacked layout)

### Editor Features
- Sidebar navigation across 8 sections
- Dynamic add/remove for skill categories, projects, experience items, superpower cards
- Photo upload with live circular preview
- GitHub URL field per project (auto-prefixes `https://` if missing)
- Social links: GitHub, LinkedIn, Docker
- Reset to defaults button
- Generates a fully self-contained `.html` file with all data inline

## Tech Stack

- **Three.js** (r128) — 3D background scene
- **Font Awesome** 6.5.1 — icons
- Vanilla HTML / CSS / JS — no frameworks, no build step, no dependencies

## Deploy

The generated `portfolio.html` is a single file — deploy anywhere:
- GitHub Pages
- Netlify
- Vercel
- Any static file host
