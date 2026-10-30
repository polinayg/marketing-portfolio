# Polina Gaydamachenko — Marketing Portfolio

Live site: https://polinayg.github.io/marketing-portfolio/

A static, dependency-free portfolio for GitHub Pages: home (selected work, analytics, about, contact),
four featured brand case studies (Axe & Kindle, NxtDib, Equipio and Every Window), four marketing capability studies,
and a filterable creative gallery with a keyboard/swipe lightbox.

Polina's overall professional experience spans five brands; the four brands currently showcased are a selected public subset.
Levo Aero is not currently featured. Its source content and historical assets are retained, while `levo-aero.html`
displays an unavailable page with `noindex, nofollow` and is excluded from the sitemap and featured navigation.

## Published marketing capabilities

- [Website Design & Builds](website-redesigns.html) — NxtDib built from scratch; six before-and-after redesign comparisons for Every Window and Axe & Kindle, plus mobile examples.
- [Email Marketing](email-marketing.html) — Axe & Kindle campaigns in Drip, seasonal creative and copy, and historical program reporting.
- [Paid Advertising](paid-advertising.html) — October 2026 Axe & Kindle Google Ads audit and Every Window report analysis, with findings, proposed actions and measurement plans clearly separated from implementation and measured results.
- [Analytics & Reporting](analytics-reporting.html) — cross-channel analysis for Axe & Kindle and Every Window using GA4, Google Search Console, Instagram Insights and Drip, with findings and recommendations.

Social content, copywriting, creative design and publishing are demonstrated throughout the featured brand studies and gallery.

## Structure

- `*.html` — generated pages (do not hand-edit; edit `tools/content.py` and rebuild)
- `assets/css/site.css`, `assets/js/site.js` — design system and interactions
- `assets/img/<brand>/` — WebP exports of original Canva work (`name.webp` 1080–1200px, `name-sm.webp` 640px)
- `tools/content.py` — all copy, case-study text, image lists, alt text and verified metrics
- `tools/build.py` — renders the pages, sitemap.xml and robots.txt
- `assets/docs/Polina_Gaydamachenko_Resume.pdf` — downloadable résumé
- `tools/build_resume.py` — rebuilds the résumé PDF from confirmed résumé content (requires ReportLab; set `RESUME_FONT_DIR` to a directory containing Liberation Sans fonts for embedding)

## Update content

```bash
pip install pillow
python3 tools/build.py
```
To rebuild the résumé: `pip install reportlab` then `python3 tools/build_resume.py`. Its homepage download path is set by `RESUME_FILE` in `tools/content.py`.

Featured brand studies live in `PROJECTS`; published capability studies live in `CAPABILITIES`.
`CASE_STUDIES` combines those lists for page generation and the sitemap. Only featured brands appear in the homepage project list and gallery.
Retained Levo source content is outside those lists; the build writes an unavailable page at its former URL.

To add a carousel: drop WebP files into `assets/img/<brand>/`, create `-sm.webp` versions (640px wide),
add a set to the featured project's `sets` list in `tools/content.py`, and rebuild.

## Website redesign comparisons
`website-redesigns.html` features the confirmed NxtDib website build from scratch and compares supplied before-and-after full-page PDF captures for Every Window (homepage, single-hung product page, installation page) and Axe & Kindle (homepage, oak firewood product page, blog page). `comparisons` in `tools/content.py` controls the copy, page type and file prefix (`<prefix>-before` / `<prefix>-after`) for each pair. Each pair uses the unchanged PDF in `assets/docs/pdf/<prefix>-before.pdf` / `-after.pdf` (opened and downloaded directly) and a scrollable WebP preview of it in `assets/img/web-redesigns/<prefix>-before-pdf-preview.webp` (about 1000px wide, rendered from the PDF with `pdftoppm`). To add a pair, drop in the two PDFs and previews and add an entry to `comparisons`. Fresh current-site desktop crops dated October 29, 2026 illustrate design details separately; `-current-preview.webp` and `-current-preview-sm.webp` support the hero. `assets/css/web-redesigns.css` is loaded only for this page. Scroll regions and native links work without JavaScript. Captures document visible design changes, not measured performance gains. `pdf-viewer.html` and `assets/docs/pdf/ak-before|ak-after/` are the earlier split-PDF viewer for the original Axe & Kindle homepage pair and are no longer linked from this page.

## Data integrity
Homepage social metrics come from the Sprout Social “Post Performance (NXT)” export, Sept 17, 2025 – Oct 26, 2026.
Analytics and Email capability studies separately cite the historical analytics presentation shown in `assets/img/analytics/`.
Paid Advertising summarizes the October 2026 Axe & Kindle Google Ads audit and Every Window report analysis, explicitly distinguishing recommendations from implementation and measured impact. The Axe & Kindle audit was view-only; the Every Window analysis used GA4/Data Studio reports and a monthly performance sheet without direct Google Ads account access. It omits internal spend/revenue and contains no Levo artwork or examples. `work_examples` provides native HTML finding/action/measurement summaries; `next_case` can preserve an existing navigation destination.
Email figures describe program-level observations; 2025 is an interim snapshot. No attributable email revenue or conversion lift is claimed.
The analytics study labels approximate follower gains as ad-assisted and omits company revenue. Curated third-party Reels are labeled and linked, never embedded as original work.

## Backup
The pre-redesign site is preserved at git tag `v1-original-backup`.

The earlier Axe & Kindle split-PDF viewer retains the supplied high-resolution PDF pair in `assets/docs/pdf/ak-{before,after}/`. The PDFs are stored as byte-preserving parts to fit the publishing transfer limits; `pdf-viewer.html` reassembles them and validates SHA-256 before showing open/download controls. The page displays 1008px-wide previews derived from their embedded 3024px-wide captures, with direct open/download links to the PDFs for full-quality zoom. Its review detail is cropped from the supplied after PDF. Earlier PNG URLs remain available.
