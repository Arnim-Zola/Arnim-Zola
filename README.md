<div align="center">

  <!-- Native Animated Cyberpunk GitHub Dark & Emerald Green Banner -->
  <a href="https://github.com/Arnim-Zola">
    <img src="assets/header-v2.svg" alt="Mohammed Sahil - Full-Stack & GenAI Engineer" width="100%" />
  </a>

  <!-- Real-Time Looping Iris Text Subtitle (GitHub Green) -->
  <a href="https://github.com/Arnim-Zola/Eden">
    <img src="assets/taglines.svg?v=1.2" alt="Mohammed Sahil Technical Taglines - Iris Reveal Animation" width="100%" />
  </a>

  <!-- Unified Emerald Green Social Connect HUD -->
  <p align="center">
    <a href="https://www.linkedin.com/in/mohammed-sahil-2b0583336/"><img src="assets/btn-linkedin-v9.svg" height="42" alt="Connect on LinkedIn" /></a>&nbsp;&nbsp;&nbsp;&nbsp;<a href="mailto:mohammedsahil0003@gmail.com"><img src="assets/btn-email-v9.svg" height="42" alt="Send Email" /></a>
  </p>

</div>

---

<img src="assets/about-me-perfect.svg" alt="About Me &amp; Identity" width="100%" />

<img src="assets/terminal-profile-v5.svg" alt="Terminal Profile &amp; Cartoon Green Bookshelf Spotlight" width="100%" />

| Pillar & Domain | Real-World Architecture & Integration (Eden & Portfolio) | Core Stack |
| :--- | :--- | :--- |
| **Distributed Systems & Async Tasks** | In **Eden**, video ingestion and frame extraction are offloaded to asynchronous background worker pools via **Celery + Redis**, preventing HTTP server bottlenecks with rate-limit resilient retry fallbacks. | `FastAPI` `Celery` `Redis` `Asyncio` |
| **Relational & Vector Search Architecture** | In **Eden**, forensic claims are embedded and indexed in **PostgreSQL (pgvector)** using **HNSW graphs** for sub-120ms nearest-neighbor retrieval, paired with **Redis** caching for high-frequency queries. | `PostgreSQL` `pgvector (HNSW)` `Redis` |
| **Multimodal Perception & Fact RAG** | In **Eden**, parallel streams demux visual frames (**OpenCV**) for OCR scanning and audio (**OpenAI Whisper**) for speech transcription, synthesized by deep reasoning LLM agents into an authenticity truth index. | `OpenCV` `Whisper` `EasyOCR` `Multi-Agent RAG` |
| **Full-Stack & 60FPS 3D WebGL** | In **Quantum OS** *(In Progress / Active Build)*, architecting an interactive cyberpunk terminal portfolio with **Next.js 15** and **Three.js**, running custom GPU **GLSL fragment shaders** at 60FPS alongside Web Audio API synthesis. | `Next.js 15` `React 19` `Three.js` `GLSL Shaders` |
| **Containerization & Multi-Service Infra** | Orchestrated the full multi-service architecture with **Docker Compose**, isolating FastAPI/Django API layers, Celery workers, Redis brokers, and React frontends into reproducible networks. | `Docker Compose` `Linux/Bash` `Nginx` `Git` |

---

### PRIMARY FLAGSHIP: EDEN (Autonomous Misinformation Analysis Engine)

<div align="center">
  <a href="https://github.com/Arnim-Zola/Eden">
    <img src="assets/eden-logo.svg" width="340px" alt="EDEN — Autonomous Multimodal Misinformation &amp; Media Forensics Engine" />
  </a>
</div>

<br/>

> **[Eden](https://github.com/Arnim-Zola/Eden)** is a state-of-the-art **forensic media fact-checking and multimodal analysis terminal**. It ingests short-form social media content (Instagram Reels, posts, and direct video uploads), decomposes visual & auditory streams into discrete temporal artifacts, detects political bias & narrative agendas, cross-references claims against real-time authoritative news sources via OSINT pipelines, and computes a comprehensive forensic truth index.

<div align="center">
  <img src="assets/eden-pipeline.svg" width="100%" alt="EDEN Multimodal Architecture Pipeline" />
</div>

<br/>

#### Multimodal Pipeline Execution (Stage-by-Stage)

| Stage & Node | Name | Plain English Breakdown (What Happens Here) | Core Stack |
| :--- | :--- | :--- | :--- |
| **Stage 01** | **Stream Ingestion** | Ingests Instagram Reels, carousel posts, and raw video files without crashing the server by queueing tasks in background worker pools. | `Celery` `Redis` `FastAPI` |
| **Stage 02A** | **Visual Perception** | Extracts clean image frames from the video (4 frames/sec) and uses OCR to scan and read all on-screen captions, headlines, and overlay text. | `OpenCV` `EasyOCR` |
| **Stage 02B** | **Auditory Perception** | Slices the audio track, transcribes spoken speech to text using Whisper, and breaks long audio into time-stamped factual claim sentences. | `OpenAI Whisper` `FFmpeg` |
| **Stage 03** | **Temporal Fusion** | Synchronizes spoken words with on-screen visual text at the exact millisecond so every claim is tied to its visual context. | `Cross-Modal Alignment` |
| **Stage 04** | **OSINT Engine** | Autonomous AI agents query live news search APIs and cross-check verified knowledge bases using sub-120ms vector database retrieval. | `Multi-Agent RAG` `pgvector (HNSW)` |
| **Stage 05** | **Forensic Truth Dossier** | Evaluates political bias and manipulative framing, calculates an authenticity score (Truth Index %), and compiles a 1-click PDF dossier. | `LLM Reasoners` `PDF Dossier` |

#### Eden Architectural Innovations

- **Multimodal Perception**: Synchronized **EasyOCR** (on-screen text localization) + **OpenAI Whisper** (temporal speech transcription) + **OpenCV** (4fps keyframe extraction)—watching video frames, reading on-screen captions, and transcribing spoken dialogue simultaneously to match words with visuals at exact seconds.
- **Political Agenda & Bias Analysis**: Quantifies narrative framing, manipulative bias, and partisan spin using specialized agentic LLM reasoning to detect whether content is pushing biased propaganda, one-sided spin, or intentional exaggeration instead of objective truth.
- **Real-Time OSINT News Verification**: Dynamically queries live news search APIs and cross-checks authoritative source evidence for every extracted assertion, instantly verifying claims against real-time breaking news and reputable journalism.
- **Dual-Path Fallback Orchestration**: Asynchronous task chaining via **Celery + Redis** with graceful degradation under API quota limits and GPU constraints, preventing server crashes and slowdowns during viral traffic spikes by queueing requests and rerouting through backup models.
- **Sub-120ms Vector Retrieval**: Forensic claim embeddings indexed in **PostgreSQL (pgvector)** with **HNSW graphs** for high-speed similarity search, scanning through massive databases of past claims and known hoaxes in under 120 milliseconds to find matching patterns.
- **Forensic Command HUD & Dossier**: Threat index telemetry, ⌘K command palette, and one-click PDF intelligence dossier generation with verifiable citations, packaging the entire forensic investigation into an exportable, shareable summary report with clickable proof links.
- **Infrastructure**: Fully containerized multi-container deployment with **Docker Compose**, **FastAPI / Django REST Framework**, and **React 18**, isolating APIs, database services, and frontend interfaces into self-contained Docker containers for consistent deployment anywhere.

**[Access Eden OSINT Pipeline & System Architecture →](https://github.com/Arnim-Zola/Eden)**

---

### SECONDARY ARSENAL & CREATIVE WEBGL LABS

| Project & Domain | Architecture & Systems Highlights | Core Stack | Source Code |
| :--- | :--- | :--- | :--- |
| **CampusCart**<br/>`Campus Logistics` | Standing in a 40-person line at 8:55 AM just to print two pages before submission deadline? Absolutely not. CampusCart kills the campus queue forever with an instantaneous zero-queue utility powered by client-side **PDF.js** page parsing & dynamic pricing calculus, 3s automated polling queues via **Django REST**, and real-time vendor ticketing dashboards in **Next.js 14** + **PostgreSQL**. | `Next.js 14` `Django REST` `PostgreSQL` `PDF.js` | [Arnim-Zola/CampusCart](https://github.com/Arnim-Zola/CampusCart) |
| **Zemo**<br/>`E-Commerce Intel` | That "50% OFF Limited Deal" with 4.8 stars written by bots? We called its bluff. Zemo is an autonomous radar built to expose fake hype and predatory price hikes by automating headless **Playwright** scraping across dynamic DOMs, synthesizing 100+ raw customer reviews into structured sentiment vectors via **Meta Llama 3 8B**, and plotting historical price trends with **Plotly.js**. | `Python` `Playwright` `Meta Llama 3` `FastAPI` `Plotly.js` | [Arnim-Zola/Zemo](https://github.com/Arnim-Zola/Zemo) |
| **Brainiac**<br/>`Cognitive AI` | Ever wondered what 3 AM caffeine-fueled burnout actually looks like inside your head? Brainiac renders your brain's cognitive chaos into a living 3D simulation, featuring an interactive **@react-three/fiber** brain cortex mesh, computing 30-factor psychometric scoring vectors via **PyTorch**, and generating personalized AI improvement protocols. | `React 18` `@react-three/fiber` `Three.js` `FastAPI` `PyTorch` | [Arnim-Zola/Brainiac](https://github.com/Arnim-Zola/Brainiac) |
| **Quantum OS**<br/>`Interactive Portfolio` | Why should developer portfolios look like another generic resume template from 2015? Quantum OS turns my personal portfolio into a full-blown sci-fi cybernetic desktop operating system, powered by custom GPU **GLSL fragment shaders** locked at 60FPS, **Web Audio API** synthesis for real-time acoustic feedback, and a streaming edge AI terminal shell. | `Next.js 15` `React 19` `Three.js` `GLSL Shaders` `Web Audio` | [Arnim-Zola/Portfolio](https://github.com/Arnim-Zola/Portfolio)<br/>*(Active Build)* |

---

### TECHNICAL ARSENAL

| System Domain | Core Technologies & Production Tooling |
| :--- | :--- |
| **Languages & Shaders** | `Python 3.11` `TypeScript` `JavaScript (ES6+)` `GLSL Shaders` `C++` `SQL` `Bash / Linux` |
| **Applied AI, Vision & NLP** | `Google Gemini 2.0` `Meta Llama 3 (8B)` `PyTorch` `OpenCV` `OpenAI Whisper` `EasyOCR` `pgvector (HNSW)` `LangChain` |
| **Distributed Backend & Scraping** | `FastAPI` `Django` `Django REST Framework` `Celery` `Redis` `Playwright` `RESTful APIs` |
| **Creative WebGL, 3D & Frontend** | `Next.js 15` `React 19` `Three.js` `@react-three/fiber` `Web Audio API` `Plotly.js` `PDF.js` `Tailwind CSS` |
| **Databases, DevOps & Media** | `PostgreSQL` `SQLite` `MongoDB` `Docker` `Docker Compose` `Git` `GitHub Actions` `FFmpeg` |

---

### REAL-TIME TELEMETRY & CODING STATS

<div align="center">

  <!-- GitHub Streak Stats (Obsidian & Emerald Neon Theme) -->
  <img src="https://streak-stats.demolab.com/?user=Arnim-Zola&theme=dark&background=040906&border=1b4d2e&stroke=1b4d2e&ring=00ff66&fire=00ff66&currStreakLabel=00ff66&currStreakNum=ffffff&sideNums=ffffff&sideLabels=8b949e&dates=8b949e&border_radius=8" alt="GitHub Streak" width="48%" />
  
  <!-- GitHub Overall Stats (Obsidian & Emerald Neon Theme) -->
  <img src="https://github-stats-extended.vercel.app/api?username=Arnim-Zola&show_icons=true&bg_color=040906&border_color=1b4d2e&icon_color=00ff66&title_color=00ff66&text_color=e6edf3&border_radius=8&include_all_commits=true&count_private=true" alt="GitHub Stats" width="48%" />

  <br/><br/>

  <!-- Top Languages Card (Obsidian & Emerald Neon Theme) -->
  <img src="https://github-stats-extended.vercel.app/api/top-langs/?username=Arnim-Zola&layout=compact&bg_color=040906&border_color=1b4d2e&title_color=00ff66&text_color=e6edf3&border_radius=8" alt="Top Languages" width="55%" />

</div>

---

<div align="center">
  <p><b>Engineered by Mohammed Sahil • 3rd Year CSE @ DSATM, Bengaluru</b></p>
  <img src="https://capsule-render.vercel.app/api?type=rect&color=0:040906,50:00ff66,100:040906&height=3" width="100%" />
</div>

