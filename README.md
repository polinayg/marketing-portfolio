# Polina Gaydamachenko — Marketing Portfolio

Live site: https://polinayg.github.io/marketing-portfolio/

A static, dependency-free portfolio for GitHub Pages: home (selected work, analytics, about, contact),
five case studies (Axe & Kindle, NxtDib, Equipio, Every Window, Levo Aero) plus Analytics & Reporting and Email Marketing capability studies, and a filterable creative gallery
with a keyboard/swipe lightbox.

## Structure
- `*.html` — generated pages (do not hand-edit; edit `tools/content.py` and rebuild)
- `assets/css/site.css`, `assets/js/site.js` — design system and interactions
- `assets/img/<brand>/` — WebP exports of original Canva work (`name.webp` 1080–1200px, `name-sm.webp` 640px)
- `tools/content.py` — all copy, case-study text, image lists, alt text and verified metrics
- `tools/build.py` — renders the pages, sitemap.xml and robots.txt

## Update content
```bash
pip install pillow
python3 tools/build.py
```
To add a carousel: drop WebP files into `assets/img/<brand>/`, create `-sm.webp` versions (640px wide),
Brand studies live in `PROJECTS`; capability studies live in `CAPABILITIES`. Both are built and included in the sitemap; only brands appear in the homepage project list and gallery.

Add a set to the project's `sets` list in `tools/content.py`, rebuild.

## Data integrity
Homepage social metrics come from the Sprout Social “Post Performance (NXT)” export, Sept 17, 2025 – Oct 26, 2026.
Capability studies separately cite the historical analytics presentation shown in `assets/img/analytics/`.
Email figures describe program-level observations; 2025 is an interim snapshot. No attributable email revenue or conversion lift is claimed.
The analytics study labels approximate follower gains as ad-assisted and omits company revenue. Curated third-party Reels are labeled and linked, never embedded as original work.

## Backup
The pre-redesign site is preserved at git tag `v1-original-backup`.
