# DEVELOPMENT LOG
## Apsara Growth Partner Programme — Walkthrough Project

---

## 2026-04-10 — Day 1: Project Inception

### Session Summary
- **Started**: Evening session
- **Architect**: Claude (AI pair programmer)
- **Human Lead**: Asha Prakash Panda

### Decisions Made

1. **Single-file HTML architecture chosen** — No frameworks, no build tools. The entire walkthrough lives in one `index.html`. Rationale: maximum portability, works offline, shareable as a single file via WhatsApp/email, and deployable on GitHub Pages without any build step.

2. **GitHub Pages for hosting** — Free, reliable, SSL by default, clean URL. Repository will be public (required for free Pages). No sensitive data in the codebase — all content is already in the public-facing PDF.

3. **BBP created first** — Before writing code, documented the full blueprint: brand tokens, section architecture, technical specs, safety/governance considerations. This ensures we don't drift during implementation.

4. **Development journal established** — This file. Every session gets an entry documenting what was built, what changed, and why. Future reference for the team.

5. **Safety-first approach for public deployment**:
   - Pre-RERA disclaimers prominently placed
   - Legal framework section with verifiable references
   - "Verify Everything" bar with official government URLs
   - No secrets or credentials in repository
   - Professional repository naming

### Work Completed
- [x] Project directory structured
- [x] BBP (Build Blueprint) document created
- [x] Development journal initialized
- [ ] index.html — 13-section walkthrough (in progress)
- [ ] Git repository initialized
- [ ] GitHub repository created
- [ ] GitHub Pages enabled
- [ ] Live URL verified and shared

### Technical Notes
- Color scheme extracted from source PDF: dark forest greens, lime accents, cream backgrounds, gold highlights
- All rupee values use the `₹` character directly (Unicode U+20B9)
- Animated counters use `IntersectionObserver` to fire only when section scrolls into view
- Auto-advance timer: 8s default, pauses on any user interaction, resumes after 12s of inactivity

### Open Items
- Verify all financial figures against source PDF before going live
- Test on physical mobile devices (not just responsive mode)
- Consider adding `og:image` meta tags for rich link previews when shared

---

_Next entry will be added in the next working session._
