"""Generate Omkar Amale's portfolio from the cloned PortFolioWebsite editor.

Fills the visual editor with real data and clicks "Generate HTML", capturing the
downloaded standalone portfolio as index.html (ready for GitHub Pages).

Run:  uv run --with playwright python build_portfolio.py
"""
from __future__ import annotations

from pathlib import Path

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent
EDITOR = (ROOT / "editor.html").as_uri()
OUTPUT = ROOT / "index.html"
AVATAR = ROOT / "avatar.png"
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

FIELDS = {
    "f-site-title": "Omkar Amale | Senior Software Engineer",
    "f-site-logo": "Omkar Amale",
    "f-site-footer": '<p>&copy; 2026 Omkar Amale. Built with Java, Spring AI &amp; Three.js.</p>',
    "f-hero-badge": "Senior Software Engineer \u00b7 Applied AI",
    "f-hero-name": "Omkar Amale",
    "f-hero-tagline": "Building systems that think.",
    "f-hero-highlights": "Java, Spring Boot, Spring AI, Microservices",
    "f-hero-subtitle": "9+ years of enterprise Java and applied AI \u2014 from resilient microservices to LLM-powered products.",
    "f-hero-btn1": "View My Work",
    "f-hero-btn1s": "1",
    "f-hero-btn2": "Get in Touch",
    "f-hero-btn2s": "2",
    "f-about-title": "About Me",
    "f-about-heading": "Senior Software Engineer & Applied AI Builder",
    "f-about-p1": "I build enterprise systems with <strong>Java, Spring Boot, and microservices</strong>, then pair that foundation with <strong>Spring AI, LLMs, and React</strong> to ship products that actually think.",
    "f-about-p2": "Based in Pune, I'm a Senior Software Engineer at Synechron, hold a PG Diploma in Machine Learning & AI from IIIT Bangalore, and received the Synechron Star Award. I care about clean architecture, automation, and work that survives production.",
    "f-stat1n": "9+",
    "f-stat1l": "Years Experience",
    "f-stat2n": "45",
    "f-stat2l": "Public Repos",
    "f-stat3n": "4",
    "f-stat3l": "Featured Projects",
    "f-skills-title": "Tech Stack",
    "f-projects-title": "Selected Projects",
    "f-experience-title": "Experience",
    "f-contact-title": "Contact",
    "f-contact-heading": "Let's build something reliable.",
    "f-contact-subtext": "Open to senior backend and applied-AI roles. Copy my email or reach out on LinkedIn.",
    "f-contact-email": "omkar.amale5@gmail.com",
    "f-contact-hint": "Click to copy email",
    "f-contact-copied": "Copied \u2014 paste it into your mail app.",
    "f-social-gh": "https://github.com/coder5omkar",
    "f-social-li": "https://www.linkedin.com/in/omkaramale",
    "f-social-docker": "#",
    "f-adhd-enabled": "true",
    "f-adhd-badge": "How I Work",
    "f-adhd-title": "built to ship",
    "f-adhd-subtitle": "",
    "f-adhd-intro1": "I care about systems that hold up under real traffic, real deadlines, and real users.",
    "f-adhd-intro2": "These aren't personality claims \u2014 they're how I operate day to day.",
    "f-adhd-cta-h": "Let's build the next one.",
    "f-adhd-cta-s": "I'm open to senior backend and applied-AI roles. If you're solving a hard systems problem, I'd like to hear about it.",
    "f-adhd-cta-btn": "Start a conversation",
    "f-adhd-cta-slide": "2",
}

SKILLS = [
    {
        "icon": "fab fa-java",
        "name": "Backend",
        "tags": ["Java", "Spring Boot", "Microservices", "REST APIs", "JPA / Hibernate", "PostgreSQL", "MySQL", "Apache Kafka"],
    },
    {
        "icon": "fas fa-brain",
        "name": "AI & Data",
        "tags": ["Spring AI", "LLM Integration", "Ollama", "OpenAI API", "RAG", "Python", "SQL", "Machine Learning"],
    },
    {
        "icon": "fab fa-react",
        "name": "Frontend & DevOps",
        "tags": ["React", "TypeScript", "Tailwind CSS", "Docker", "Kubernetes", "CI/CD", "GitHub Actions", "Flyway"],
    },
]

PROJECTS = [
    {
        "imageClass": "llm",
        "icon": "fas fa-robot",
        "tags": ["Java", "Spring AI", "React", "Ollama"],
        "title": "AI Tutor",
        "desc": "AI tutor generating syllabi, explanations, and MCQ checks with Spring AI.",
        "github": "https://github.com/coder5omkar/AIBasedLearningSystem",
    },
    {
        "imageClass": "java",
        "icon": "fas fa-heart",
        "tags": ["Spring Boot", "PostgreSQL", "React", "Docker"],
        "title": "TheBridge",
        "desc": "Journal and wellness tracker with JWT auth, Flyway, and React 19.",
        "github": "https://github.com/coder5omkar/TheBridge",
    },
    {
        "imageClass": "java",
        "icon": "fas fa-server",
        "tags": ["Java", "Spring Boot", "JPA", "REST"],
        "title": "Banking Microservices",
        "desc": "Accounts, cards, and loans microservices with REST APIs and JPA.",
        "github": "https://github.com/coder5omkar/Microservices",
    },
    {
        "imageClass": "react",
        "icon": "fas fa-mobile-screen",
        "tags": ["Kotlin", "Jetpack Compose", "Android"],
        "title": "D-Tox",
        "desc": "Zero-permission Android app for a 30-second pause before distracting apps.",
        "github": "https://github.com/coder5omkar/D-Tox",
    },
]

EXPERIENCE = [
    {
        "date": "2023 \u2014 Present",
        "company": "Synechron",
        "role": "Senior Software Engineer",
        "desc": "Design and deliver Java/Spring Boot microservices for enterprise data platforms; automate data workflows with Python/SQL; build CI/CD and containerized services.",
        "dotColor": "#f5576c",
    },
    {
        "date": "2021 \u2014 2023",
        "company": "Ness Digital Engineering",
        "role": "Software Engineer",
        "desc": "Built Spring Boot services and REST APIs for client applications; optimized SQL and data access layers; worked in Agile delivery teams.",
        "dotColor": "#4facfe",
    },
    {
        "date": "2019 \u2014 2021",
        "company": "Globemind Technology",
        "role": "Java Software Developer",
        "desc": "Built Java backend modules and relational database integrations; diagnosed and resolved production issues.",
        "dotColor": "#43e97b",
    },
    {
        "date": "2017 \u2014 2019",
        "company": "Johnson Controls",
        "role": "Application Developer",
        "desc": "Developed and maintained enterprise application features and resolved defects with stakeholders.",
        "dotColor": "#a78bfa",
    },
]

SUPERPOWERS = [
    {
        "icon": "fa-sitemap",
        "title": "System Design",
        "tagline": "Structure before speed",
        "description": "I break ambiguous problems into services, contracts, and failure modes before writing code. The goal is a system the next engineer can reason about.",
        "intensity": 92,
    },
    {
        "icon": "fa-bug",
        "title": "Deep Debugging",
        "tagline": "Follow the signal",
        "description": "Stack traces, logs, and reproduction steps are clues. I stay with a bug until the root cause is understood, not just the symptom hidden.",
        "intensity": 95,
    },
    {
        "icon": "fa-gears",
        "title": "Automation",
        "tagline": "Remove the repeat",
        "description": "If a task happens twice, it becomes a script or a pipeline. I automate data workflows, builds, and checks so the team spends time on the problem.",
        "intensity": 93,
    },
    {
        "icon": "fa-check-double",
        "title": "Ownership",
        "tagline": "Close the loop",
        "description": "From requirement to rollout, I track the work through edge cases, reviews, and production. 'Done' means it runs without me.",
        "intensity": 94,
    },
    {
        "icon": "fa-graduation-cap",
        "title": "Fast Learning",
        "tagline": "Docs, then depth",
        "description": "New stack? I read the docs, build a small proof, and go deeper as the problem demands. The PG Diploma in ML & AI came from the same habit.",
        "intensity": 90,
    },
    {
        "icon": "fa-lightbulb",
        "title": "Product Thinking",
        "tagline": "Code is the means",
        "description": "I ask what the user is trying to do before choosing the implementation. The best technical decision is the one that moves the product.",
        "intensity": 88,
    },
    {
        "icon": "fa-comments",
        "title": "Clear Communication",
        "tagline": "Make it legible",
        "description": "I write decisions down, keep APIs and docs honest, and explain trade-offs without hiding behind jargon.",
        "intensity": 87,
    },
    {
        "icon": "fa-shield-alt",
        "title": "Calm Under Pressure",
        "tagline": "Steady in production",
        "description": "Incidents reward a clear head. I prioritize impact, communicate what I know, and fix the smallest thing that restores service first.",
        "intensity": 92,
    },
]

INJECT = """
(data) => {
  const set = (id, value) => { const el = document.getElementById(id); if (el) el.value = value; };
  Object.entries(data.fields).forEach(([id, value]) => set(id, value));
  renderSkillCats(data.skills);
  renderProjects(data.projects);
  renderExperience(data.experience);
  renderSuperpowers(data.superpowers);
}
"""

# Appended after generation: the default cards are too tall for a 900px
# viewport once there are four projects, which makes the centred column clip.
WORK_CSS = """
<style>
.split-right .split-title{margin-bottom:0.9rem}
.split-right .proj-grid{gap:0.55rem}
.split-right .proj-card{padding:0.85rem 1rem;gap:0.85rem}
.split-right .proj-icon-box{width:42px;height:42px;font-size:1.15rem;border-radius:10px}
.split-right .proj-body h4{font-size:0.95rem;margin-bottom:0.15rem}
.split-right .proj-body p{font-size:0.78rem;line-height:1.35;margin-bottom:0.28rem}
.split-right .proj-tags{gap:0.3rem}
.split-right .proj-tags span{padding:0.1rem 0.5rem;font-size:0.62rem}
.split-right .proj-links{margin-top:0.22rem}
.split-right .proj-links a{font-size:0.72rem}
@media (max-width:800px){
  .slide{height:100vh;overflow-y:auto;overflow-x:hidden;display:block;padding:4.5rem 0 2rem}
  .split{display:block;height:auto;min-height:0;max-width:none;padding:0}
  .split-left,.split-right{overflow:visible;padding:0.5rem 1.2rem}
  .split-right{margin-top:1.6rem}
  .split-title{margin-bottom:0.9rem}
  .hero-content h1{font-size:clamp(2.1rem,8vw,3rem)}
  .hero-badge{white-space:nowrap;font-size:0.62rem;letter-spacing:0.08em;padding:0.35rem 0.9rem;margin-bottom:1rem}
  .about-grid{gap:1rem}
  .about-avatar .avatar-ring{width:130px;height:130px}
  .about-text h3{font-size:1.25rem}
  .about-text p{font-size:0.92rem}
  .stat-item{padding:0.55rem}
  .stat-num{font-size:1.3rem}
  .contact-email-card{padding:1.2rem}
  .contact-email-card .email-addr{font-size:1rem}
  #adhd .adhd-grid{grid-template-columns:1fr}
}
</style>
"""


def main() -> None:
    payload = {
        "fields": FIELDS,
        "skills": SKILLS,
        "projects": PROJECTS,
        "experience": EXPERIENCE,
        "superpowers": SUPERPOWERS,
    }
    with sync_playwright() as p:
        browser = p.chromium.launch(executable_path=CHROME, headless=True)
        page = browser.new_page(viewport={"width": 1600, "height": 1000}, accept_downloads=True)
        page.goto(EDITOR, wait_until="load")
        page.wait_for_selector("#f-hero-name", state="attached")
        page.set_input_files("#f-photo", str(AVATAR))
        page.wait_for_timeout(400)
        page.evaluate(INJECT, payload)
        page.wait_for_timeout(300)
        with page.expect_download(timeout=60000) as download_info:
            page.click("button.btn-gen.primary")
        download = download_info.value
        download.save_as(OUTPUT)
        browser.close()

    html = OUTPUT.read_text(encoding="utf-8")
    html = html.replace("</head>", WORK_CSS + "</head>", 1)
    # On phones the slides scroll internally; a vertical swipe must scroll the
    # slide instead of jumping to the next one. Menu links and dots still work.
    html = html.replace(
        "document.addEventListener('touchend', e => {",
        "document.addEventListener('touchend', e => {\n  if (window.matchMedia('(max-width:800px)').matches) return;",
        1,
    )
    OUTPUT.write_text(html, encoding="utf-8")
    print(f"wrote {OUTPUT} ({OUTPUT.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
