# BUILD BLUEPRINT (BBP)
## Apsara Realcon — Growth Partner Programme Walkthrough

---

### Project Identity

| Field | Value |
|---|---|
| **Project Name** | Apsara Growth Partner Programme — Interactive Walkthrough |
| **Repository** | `apsara-growth-programme` (GitHub Pages) |
| **Owner** | asha8-8 (Asha Prakash Panda) |
| **Created** | 2026-04-10 |
| **Status** | Active Development |
| **Live URL** | _TBD — GitHub Pages deployment_ |

---

### Purpose

Build a single-file, zero-dependency, offline-capable interactive HTML presentation that replaces the static PDF (`Growth Partner Presentation v01.pdf`) with a premium, modern walkthrough experience suitable for sharing with prospective investors and partners via a public URL.

---

### Design Philosophy

- **2026 Silicon Valley grade** — glassmorphism, micro-animations, fluid transitions
- **Single file architecture** — no CDN, no build tools, works offline, prints cleanly
- **Mobile-first responsive** — investors will open this on WhatsApp/phone first
- **Trust-forward design** — legal disclaimers visible, verify links prominent, no hype without substance

---

### Brand System

| Token | Value | Usage |
|---|---|---|
| `--forest-dark` | `#1a3a2a` | Primary backgrounds, cards |
| `--forest-mid` | `#2d5016` | Secondary backgrounds |
| `--lime` | `#8bc34a` | Accents, highlights, CTAs |
| `--lime-soft` | `#a8c96e` | Softer accent, hover states |
| `--cream` | `#f0f4e8` | Page background |
| `--gold` | `#d4a843` | Highlight text, badges |
| `--white` | `#ffffff` | Card text on dark |
| Heading font | Georgia / serif fallback | Bold, uppercase where needed |
| Body font | system-ui, -apple-system, sans-serif | Clean, readable |

---

### Architecture — 13 Sections

| # | Section | Key Content |
|---|---|---|
| 1 | Hero Cover | Brand intro, 4 stat cards |
| 2 | Investment Overview | Programme structure, snapshot table |
| 3 | Financial Returns | Bar chart, cumulative cash view |
| 4 | Exit Options | Option A (retain) vs Option B (buyback) |
| 5 | Appreciation Opportunity | Odisha growth drivers, 2x-4x thesis |
| 6 | Location Advantages | Proximity list, Bajpur positioning |
| 7 | Proposed Amenities | 3x4 amenity grid, road specs |
| 8 | Project Roadmap | 5-stage horizontal timeline |
| 9 | Investor Safeguards | Protection framework, 4 safeguard cards |
| 10 | Legal Framework | 5 governing laws with badges |
| 11 | Why This Investment | 6 feature cards, CTA |
| 12 | Comparison Table | vs FD, Debt MF, Raw Land |
| 13 | Contact CTA | Office, phone, email, website |

---

### Technical Specifications

| Feature | Implementation |
|---|---|
| Auto-advance | 8s per slide, pause on hover/interaction, resume after 12s |
| Navigation | Prev/Next arrows, dot nav, keyboard arrows, progress bar |
| Animations | CSS transitions (fade+slide), IntersectionObserver triggers |
| Counters | Animated number counting on section entry |
| Charts | Pure CSS/SVG bar chart (no libraries) |
| Fullscreen | Fullscreen API button |
| Print | `@media print` — each section = one clean page |
| Responsive | Mobile-first, fluid grid, touch-friendly |
| Dependencies | Zero. Single HTML file. |

---

### Safety & Governance (Public URL)

| Concern | Mitigation |
|---|---|
| **Regulatory** | Pre-RERA disclosure visible in Section 2. Legal framework in Section 10. Independent due diligence advised throughout. |
| **Repository visibility** | Public repo (required for free GitHub Pages). No secrets, API keys, or private data in repo. |
| **Content integrity** | All financial figures match source PDF. No exaggerated claims beyond source material. |
| **Brand protection** | Repository name is professional. README states this is an official Apsara Realcon resource. |
| **Link sharing** | GitHub Pages URL is clean: `https://asha8-8.github.io/apsara-growth-programme/` |
| **Versioning** | Git history tracks every change. Dev log records decisions. |
| **Disclaimer** | Footer disclaimer on every section visible in print. |

---

### File Structure

```
apsara-growth-programme/
  index.html              # The complete walkthrough (single file)
  docs/
    BBP.md                # This document — project blueprint
    DEVLOG.md             # Daily development journal
  source/
    Growth Partner Presentation v01.pdf   # Original reference PDF
  README.md               # Public-facing repo description
  LICENSE                  # Appropriate license
  .gitignore              # Standard ignores
```

---

### Success Criteria

- [ ] All 13 sections render correctly on Chrome, Safari, Firefox
- [ ] Mobile experience is smooth on iPhone and Android
- [ ] Auto-advance and manual navigation work together without conflict
- [ ] Animated counters fire only once per section view
- [ ] Print produces 13 clean pages
- [ ] GitHub Pages URL loads under 3 seconds
- [ ] All financial figures verified against source PDF
- [ ] Legal disclaimers visible without scrolling on relevant sections
