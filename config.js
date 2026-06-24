/* ===========================================================
   SITE CONFIG — Edit this file to update all content
   ===========================================================
   Every text string on the site lives here.
   Change names, descriptions, links, stats — without touching HTML.
   =========================================================== */

const SITE_DATA = {

  /* ── Site-wide ── */
  site: {
    title: "Portfolio | Full Stack Engineer",
    logo: "Portfolio",
    footer: '<p>&copy; 2026 Your Name. Crafted with <span style="color:#f5576c;">&hearts;</span></p>',
  },

  /* ── Navigation ── */
  nav: {
    links: [
      { href: "#slide-0", label: "Home" },
      { href: "#slide-1", label: "Work" },
      { href: "#slide-2", label: "Contact" },
      { href: "#slide-3", label: "Superpowers" },
    ],
  },

  /* ── Hero (left half of slide 0) ── */
  hero: {
    badge: "Full Stack Engineer",
    name: "Your Name",
    tagline: "Building The Future",
    highlights: ["Java", "React", "LLM Apps"],
    subtitle: "Full-stack engineer crafting scalable systems & intelligent experiences",
    cta: [
      { text: "View My Work", href: "#", slide: 1, icon: "fas fa-arrow-right" },
      { text: "Get in Touch", href: "#", slide: 2, icon: "fas fa-envelope" },
    ],
  },

  /* ── About (right half of slide 0) ── */
  about: {
    title: "About Me",
    heading: "Full Stack Developer & AI Enthusiast",
    avatarIcon: "fa-user-astronaut",
    paragraphs: [
      'I build end-to-end applications from the ground up — from robust <strong>Java Spring Boot</strong> backends to dynamic <strong>React</strong> frontends and intelligent <strong>LLM-powered</strong> solutions.',
      'With a passion for clean architecture and user-centric design, I create applications that are both powerful and delightful to use.',
    ],
    stats: [
      { number: "3+",  label: "Years Exp" },
      { number: "20+", label: "Projects" },
      { number: "10+", label: "Clients" },
    ],
  },

  /* ── Skills (left half of slide 1) ── */
  skills: {
    title: "Tech Stack",
    categories: [
      {
        icon: "fab fa-java",
        name: "Backend",
        tags: ["Java","Spring Boot","Microservices","REST APIs","JPA / Hibernate","PostgreSQL","MongoDB","MySQL"],
      },
      {
        icon: "fab fa-react",
        name: "Frontend",
        tags: ["React","TypeScript","Next.js","Tailwind CSS","Redux","HTML5 / CSS3","JavaScript"],
      },
      {
        icon: "fas fa-brain",
        name: "LLM & AI",
        tags: ["LangChain","OpenAI API","LlamaIndex","RAG Pipelines","Vector DBs","Hugging Face","Prompt Engineering","Fine-tuning"],
      },
    ],
  },

  /* ── Projects (right half of slide 1) ── */
  projects: {
    title: "Projects",
    items: [
      {
        imageClass: "java",
        icon: "fas fa-server",
        tags: ["Java","Spring Boot","PostgreSQL"],
        title: "E-Commerce Platform",
        desc: "Scalable microservices with JWT auth, payment gateway, real-time inventory.",
        links: [
          { icon: "fab fa-github", text: "Code", href: "#" },
        ],
      },
      {
        imageClass: "react",
        icon: "fab fa-react",
        tags: ["React","TypeScript","Node.js"],
        title: "Dashboard Analytics",
        desc: "Real-time data viz dashboard with interactive charts and dark mode.",
        links: [
          { icon: "fab fa-github", text: "Code", href: "#" },
        ],
      },
      {
        imageClass: "llm",
        icon: "fas fa-robot",
        tags: ["LangChain","OpenAI","Python"],
        title: "AI Knowledge Assistant",
        desc: "RAG-based chatbot using vector search and LLM reasoning on documents.",
        links: [
          { icon: "fab fa-github", text: "Code", href: "#" },
        ],
      },
    ],
  },

  /* ── Experience (left half of slide 2) ── */
  experience: {
    title: "Experience",
    items: [
      {
        date: "2024 — Present",
        company: "TechCorp Inc.",
        role: "Senior Full Stack Engineer",
        desc: "Architected microservices handling 1M+ daily requests. Led monolith-to-cloud migration.",
        dotColor: "#f5576c",
      },
      {
        date: "2022 — 2024",
        company: "StartupXYZ",
        role: "Full Stack Developer",
        desc: "Built React SaaS platform from scratch. Integrated LLM features for document processing.",
        dotColor: "#4facfe",
      },
      {
        date: "2021 — 2022",
        company: "WebAgency",
        role: "Junior Developer",
        desc: "Delivered 10+ web apps using Java, Spring Boot, and React.",
        dotColor: "#43e97b",
      },
    ],
  },

  /* ── Contact (right half of slide 2) ── */
  contact: {
    title: "Contact",
    heading: "Let's build something amazing",
    subtext: "No backend — just copy my email and send me a message directly.",
    email: "hello@yourname.dev",
    emailLabel: "Click to copy email",
    copiedText: "Copied! Ready to paste in your email app.",
    social: [
      { icon: "fab fa-github",     href: "#", label: "GitHub" },
      { icon: "fab fa-linkedin-in", href: "#", label: "LinkedIn" },
      { icon: "fab fa-twitter",    href: "#", label: "Twitter" },
    ],
  },

  /* ════════════════════════════════════════════════════════════
     ADHD SUPERPOWERS (standalone slide 3)
     ════════════════════════════════════════════════════════════ */
  adhd: {
    enabled: true,

    badge: "Neurodivergent by Design",
    title: "Built Different",
    subtitle: "High-Functioning ADHD in Engineering",

    intro: [
      "The same wiring that makes focus a challenge is the exact wiring that makes me exceptional at what I do. <strong>I don't work despite my brain — I work because of it.</strong>",
      "Here is how my brain operates — and why it is an unfair advantage for the teams I join.",
    ],

    superpowers: [
      {
        icon: "fa-bolt",
        title: "Hyperfocus Engine",
        tagline: "Deep work on demand",
        description:
          "When the problem is interesting, the world disappears. I don't 'try' to focus — I lock in. Complex debugging, system architecture, high-stakes deployments — this is when my brain performs at its peak. What takes others a full day takes me a focused sprint.",
        intensity: 95,
      },
      {
        icon: "fa-eye",
        title: "Radar Pattern Recognition",
        tagline: "See what others miss",
        description:
          "My brain constantly scans for connections — across codebases, through conversations. I spot architecture flaws before they surface, debug by intuition, and connect dots that aren't visible on any diagram. It's not magic; it's how my attention is wired.",
        intensity: 92,
      },
      {
        icon: "fa-code-branch",
        title: "Divergent Problem-Solving",
        tagline: "10 solutions while others search for 1",
        description:
          "While linear thinkers follow one path, my brain branches. I generate multiple approaches simultaneously, test mental models in parallel, and arrive at creative solutions that don't appear on any roadmap. Great for novel problems. Essential for AI.",
        intensity: 88,
      },
      {
        icon: "fa-fire",
        title: "Crisis Mode Superpower",
        tagline: "Pressure turns chaos into clarity",
        description:
          "When everything is on fire, I get calm. Production down? Client emergency? Tight deadline? My brain shifts into high gear — prioritises, delegates, and executes. The adrenaline that frazzles others fuels me. I've shipped critical fixes at 2 AM with a smile.",
        intensity: 97,
      },
      {
        icon: "fa-graduation-cap",
        title: "Rapid-Fire Learning",
        tagline: "Curiosity is a competitive advantage",
        description:
          "I deep-dive new frameworks in days, not weeks. When a project demands a technology I don't know, I learn it at speed — and apply it immediately. My brain treats the unfamiliar as a puzzle, not a barrier. New stack? Show me the docs and give me a weekend.",
        intensity: 90,
      },
      {
        icon: "fa-rocket",
        title: "Relentless Innovation",
        tagline: "Boredom is the enemy of 'good enough'",
        description:
          "I can't leave well enough alone — and that's a feature. When a system feels clunky, I refactor it. When a process is slow, I automate it. The restlessness that comes with ADHD drives continuous improvement. I don't accept 'that's how it's always been done.'",
        intensity: 85,
      },
      {
        icon: "fa-random",
        title: "Multimodal Processing",
        tagline: "Juggle everything at once",
        description:
          "Code, architecture, client calls, strategy — I switch contexts faster than most people switch tabs. My brain thrives on multiple inputs. In stand-ups I'm listening, reading a PR, and sketching a solution — simultaneously. It's not distraction; it's parallel processing.",
        intensity: 82,
      },
      {
        icon: "fa-heart",
        title: "Unfiltered Intensity",
        tagline: "All in or nothing",
        description:
          "When I commit to a project, I commit fully. The passion is real, the energy is contagious, and the delivery is relentless. I don't do half-measures. If a problem matters to the business, it matters to me — and I will push through barriers that stop others cold.",
        intensity: 93,
      },
    ],

    cta: {
      headline: "This is what intensity looks like in production.",
      subtext: "If you need someone who thinks different, ships fast, and cares deeply — let's talk.",
      buttonText: "Let's Put This Brain to Work",
      buttonHref: "#",
      buttonSlide: 2,
    },
  },

};
