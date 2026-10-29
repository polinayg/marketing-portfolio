#!/usr/bin/env python3
"""Static site generator for the portfolio. Run from repo root: python3 tools/build.py
All content lives in tools/content.py; this file only renders HTML."""
import os, html, json, sys
from PIL import Image
sys.path.insert(0, os.path.dirname(__file__))
import content as C

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = C.SITE_URL
E = html.escape
_dims = {}

def dims(path):
    if path not in _dims:
        _dims[path] = Image.open(os.path.join(ROOT, path)).size
    return _dims[path]

def src(folder, name):
    return f"assets/img/{folder}/{name}.webp", f"assets/img/{folder}/{name}-sm.webp"

def picture(folder, name, alt, sizes="(max-width:760px) 60vw, 300px", eager=False, cls=""):
    full, sm = src(folder, name)
    w, h = dims(sm)
    W, _ = dims(full)
    load = 'fetchpriority="high"' if eager else 'loading="lazy"'
    c = f' class="{cls}"' if cls else ''
    return (f'<img{c} src="{sm}" srcset="{sm} 640w, {full} {W}w" sizes="{sizes}" '
            f'width="{w}" height="{h}" alt="{E(alt)}" {load} decoding="async">')

def head(title, desc, path, og_img="assets/img/og-cover.jpg", extra=""):
    url = SITE + path
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{E(title)}</title>
<meta name="description" content="{E(desc)}">
<meta name="author" content="Polina Gaydamachenko">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Polina Gaydamachenko — Marketing Portfolio">
<meta property="og:title" content="{E(title)}">
<meta property="og:description" content="{E(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}{og_img}">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#f4f0e8">
<link rel="icon" href="assets/img/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,300..500;1,9..144,300..500&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/site.css?v={C.VERSION}">
{extra}</head>
<body>
<a class="skip" href="#main">Skip to content</a>
"""

def header(active=""):
    links = [("index.html#work", "Selected Work", "work"), ("gallery.html", "Gallery", "gallery"),
             ("index.html#analytics", "Analytics", "analytics"), ("index.html#about", "About", "about")]
    items = "".join(f'<a href="{h}"{" aria-current=\"page\"" if k == active else ""}>{t}</a>' for h, t, k in links)
    return f"""<header class="site-head"><div class="wrap">
<a class="brand" href="index.html" aria-label="Polina Gaydamachenko — home"><b>Polina Gaydamachenko</b><i aria-hidden="true">✳</i></a>
<button class="menu-btn" aria-expanded="false" aria-controls="nav">Menu</button>
<nav class="nav" id="nav" aria-label="Primary">{items}<a class="cta" href="index.html#contact">Contact</a></nav>
</div></header>
"""

LIGHTBOX = """<dialog class="lb" id="lightbox" aria-label="Image viewer">
<div class="lb-inner">
<div class="lb-top"><span class="lb-count" aria-live="polite"></span><button class="close" type="button">Close ✕</button></div>
<div class="lb-stage"><img alt=""><button class="prev" type="button" aria-label="Previous image">←</button><button class="next" type="button" aria-label="Next image">→</button></div>
<p class="lb-cap"></p>
</div></dialog>
"""

def footer():
    return f"""<footer class="site-foot"><div class="wrap">
<span>© 2026 Polina Gaydamachenko · Social, content &amp; multi-brand marketing</span>
<a href="#top">Back to top ↑</a></div></footer>
{LIGHTBOX}<script src="assets/js/site.js?v={C.VERSION}" defer></script>
</body></html>
"""

def badges(s):
    out = []
    if s.get("original", True): out.append('<span class="badge orig">Original design</span>')
    else: out.append('<span class="badge curated">Curated · third-party</span>')
    if s.get("status"): out.append(f'<span class="badge sched">{E(s["status"])}</span>')
    if s.get("format"): out.append(f'<span class="badge">{E(s["format"])}</span>')
    return '<div class="badges">' + "".join(out) + '</div>'

def slideset(p, s, i):
    sq = (" sq" if s.get("square") else "") + (" wide" if s.get("wide") else "")
    group = f'{p["slug"]}-{i}'
    figs = []
    n = len(s["slides"])
    for k, (name, alt) in enumerate(s["slides"], 1):
        full, _ = src(s["folder"], name)
        cap = f'{p["name"]} — {s["title"]} ({k}/{n})'
        figs.append(f'<figure class="slide"><button type="button" data-lb data-group="{group}" data-full="{full}" data-caption="{E(cap)}" aria-label="Open larger: {E(alt)}">'
                    f'{picture(s["folder"], name, alt, "(max-width:760px) 62vw, 300px")}</button>'
                    f'<figcaption>{k:02d} / {n:02d}</figcaption></figure>')
    ctrl = ('<div class="car-ctrl"><button type="button" data-dir="-1" aria-label="Scroll back">←</button>'
            '<button type="button" data-dir="1" aria-label="Scroll forward">→</button></div>') if n > 3 else ""
    return f"""<section class="set" data-carousel aria-labelledby="{group}-t">
<div class="set-head"><div>{badges(s)}<h3 id="{group}-t">{E(s["title"])}</h3><p>{s["desc"]}</p></div>{ctrl}</div>
<div class="track{sq}"{(' style="--ar:'+s['ratio']+'"') if s.get('ratio') else ''} tabindex="0" aria-label="{E(s['title'])} slides">{"".join(figs)}</div>
</section>"""

def reels_block(p):
    if not p.get("reels"): return ""
    cards = []
    for r in p["reels"]:
        cards.append(f"""<article class="reel"><div class="badges"><span class="badge curated">Curated Reel · creator credited</span></div>
<h4>{E(r["title"])}</h4><p>{r["note"]}</p>
<dl><div><dt>Engagements</dt><dd>{r["eng"]}</dd></div><div><dt>Shares</dt><dd>{r["shares"]}</dd></div><div><dt>Saves</dt><dd>{r["saves"]}</dd></div></dl>
<a href="{r["url"]}" target="_blank" rel="noopener">View on Instagram ↗</a></article>""")
    return f"""<section class="set" aria-labelledby="{p["slug"]}-reels"><div class="set-head"><div>
<h3 id="{p["slug"]}-reels">Curated Reels (not my footage)</h3>
<p>I sourced, credited, captioned and published these Reels. The video belongs to the original creators and is shown here only as a link with its verified post metrics.</p></div></div>
<div class="reel-cards">{"".join(cards)}</div></section>"""

def brand_style(p):
    b = p["brand"]
    return f'--b-bg:{b["bg"]};--b-ink:{b["ink"]};--b-accent:{b["accent"]};--accent:{b["accent_on_paper"]}'

def case_page(p, nxt):
    chapters = [("challenge", "Challenge"), ("strategy", "Strategy"), ("role", "My Role"),
                ("execution", "Execution"), ("results", "Results"), ("takeaways", "Key Takeaways")]
    nav = "".join(f'<li><a href="#{k}">{t}</a></li>' for k, t in chapters) + '<li><a href="#work-' + p["slug"] + '">The Work</a></li>'
    body = []
    for k, t in chapters:
        body.append(f'<section class="chapter" id="{k}"><header><div class="eyebrow">{t}</div><h2>{p["cs"][k]["h"]}</h2></header><div class="body">{p["cs"][k]["body"]}</div></section>')
    sets = "".join(slideset(p, s, i) for i, s in enumerate(p.get("sets", [])))
    if not p.get("sets"):
        sets = f'<div class="callout">{p.get("pending_note","")}</div>'
    hero_stack = ""
    if p.get("cover"):
        wcls = ' wide-stack' if p.get("cover_wide") else ''
        hero_stack = f'<div class="stack cs-stack{wcls}">' + "".join(picture(p["cover_folder"], n, a, "(max-width:900px) 30vw, 200px", eager=True) for n, a in p["cover"]) + '</div>'
    facts = "".join(f'<div><dt>{E(a)}</dt><dd>{b}</dd></div>' for a, b in p["facts"])
    out = head(f'{p["name"]} — Case Study | Polina Gaydamachenko', p["meta"], p["file"])
    out += header("work")
    out += f"""<main id="main">
<section class="cs-hero" style="{brand_style(p)}" id="top"><div class="wrap">
<p class="crumbs"><a href="index.html#work">← Selected work</a> &nbsp;/&nbsp; {E(p["name"])}</p>
<div class="cs-hero-grid"><div>
<div class="eyebrow">{E(p["kicker"])}</div>
<h1>{p["headline"]}</h1>
<p class="lede">{p["lede"]}</p>
<p><a class="btn ghost" style="color:var(--b-ink);border-color:var(--line);margin-top:10px" href="#work-{p['slug']}">Jump to the work ↓</a></p>
</div>{hero_stack}</div>
<dl class="facts">{facts}</dl>
</div></section>
<nav class="cs-nav" aria-label="Case study sections"><ol>{nav}</ol></nav>
<div class="wrap" style="--accent:{p['brand']['accent_on_paper']}">
{"".join(body)}
</div>
<section class="work" id="work-{p['slug']}" style="--accent:{p['brand']['accent_on_paper']}"><div class="wrap">
<div class="eyebrow">The Work</div><h2>See the <em>work.</em></h2>
<p class="lede" style="margin-top:18px">Tap any slide to view it full size. Use arrow keys or swipe to move through a carousel.</p>
{sets}
{reels_block(p)}
</div></section>
<div class="wrap"><a class="next-proj" href="{nxt['file']}"><div class="eyebrow">Next case study</div><h2>{E(nxt['name'])} <span aria-hidden="true">→</span></h2></a></div>
</main>
"""
    out += footer()
    return out

def bars(rows, maxv, fmt="{:,}", unit=""):
    lis = []
    for label, v in rows:
        pct = 100 * v / maxv
        val = fmt.format(v)
        lis.append(f'<li title="{E(label)}: {val}{unit}"><span>{E(label)}</span><span class="track" aria-hidden="true"><span class="fill" style="width:{pct:.1f}%"></span></span><span class="val">{val}</span></li>')
    tbl = "".join(f"<tr><td>{E(l)}</td><td>{fmt.format(v)}</td></tr>" for l, v in rows)
    return f'<ul class="bars" role="list">{"".join(lis)}</ul><details class="table"><summary>View as table</summary><table><thead><tr><th>Item</th><th>Value</th></tr></thead><tbody>{tbl}</tbody></table></details>'

def home():
    A = C.ANALYTICS
    out = head("Polina Gaydamachenko — Social Media & Content Marketing Portfolio", C.HOME_META, "")
    out += f'<script type="application/ld+json">{json.dumps(C.JSONLD)}</script>\n'
    out += header()
    mosaic = "".join(f'<a href="{f}" aria-label="{E(lbl)}">{picture(fo, n, alt, "(max-width:760px) 33vw, 200px", eager=i < 3)}</a>'
                     for i, (f, fo, n, alt, lbl) in enumerate(C.MOSAIC))
    projects = []
    for i, p in enumerate(C.PROJECTS, 1):
        if p.get("cover"):
            imgs = "".join(picture(p["cover_folder"], n, a, "(max-width:900px) 30vw, 230px") for n, a in p["cover"])
            media = f'<div class="stack{" wide-stack" if p.get("cover_wide") else ""}">{imgs}</div>'
        else:
            media = f'<div class="pending"><div><strong>{E(p["name"])}</strong><span>{E(p.get("cover_label","Case study"))}</span></div></div>'
        kpis = "".join(f'<div><b>{v}</b><span>{E(l)}</span></div>' for v, l in p.get("kpis", []))
        chips = "".join(f"<li>{E(c)}</li>" for c in p["chips"])
        projects.append(f"""<article class="project">
<a class="project-media" href="{p['file']}" style="{brand_style(p)}" aria-label="Open the {E(p['name'])} case study">{media}</a>
<div><div class="project-num">{i:02d} — {E(p['kicker'])}</div>
<h3>{p['card_title']}</h3><p class="small" style="font-size:16px;color:var(--ink-2)">{p['card_text']}</p>
{f'<div class="kpis">{kpis}</div>' if kpis else ''}
<ul class="chips">{chips}</ul>
<a class="textlink" href="{p['file']}">Read the case study <span aria-hidden="true">→</span></a></div></article>""")
    stats = "".join(f'<div><b>{v}</b><span>{E(l)}</span></div>' for v, l in A["tiles"])
    out += f"""<main id="main">
<section class="hero" id="top"><div class="wrap">
<div class="hero-grid"><div>
<div class="eyebrow">Social media · Content marketing · Multi-brand</div>
<h1>Content with a <em>point of view.</em></h1>
<p class="lede" style="margin-top:28px">I'm Polina — a digital marketer who plans, designs, writes and publishes social and email content for five brands at once, from premium firewood to wholesale beverages to film-gear rentals. This is the work behind the résumé.</p>
<div class="btn-row"><a class="btn" href="#work">View selected work ↓</a><a class="btn ghost" href="#contact">Get in touch</a></div>
</div>
<dl class="hero-meta">
<div><dt>Focus</dt><dd>Social &amp; content strategy</dd></div>
<div><dt>Brands</dt><dd>5 across B2C &amp; B2B</dd></div>
<div><dt>Published (Sprout)</dt><dd>419 Instagram feed posts</dd></div>
<div><dt>Toolkit</dt><dd>Canva · Buffer · Drip · GA4 · Sprout</dd></div>
</dl></div>
<div class="mosaic" aria-label="A sample of original campaign designs">{mosaic}</div>
</div></section>
<div class="wrap"><p class="ticker" aria-label="Brands featured"><span>Axe &amp; Kindle</span><span>NxtDib</span><span>Equipio</span><span>Every Window</span><span>Levo Aero</span></p></div>

<section class="section" id="work"><div class="wrap">
<div class="split"><div><div class="eyebrow">01 — Selected Work</div><h2>Five brands. <em>Every</em> channel.</h2></div>
<p class="lede">Each case study follows the same structure — challenge, strategy, my role, execution, results and takeaways — and shows the actual campaign creative. Brand colors belong to the brands; the analysis is mine.</p></div>
<div class="projects">{"".join(projects)}</div>
<div class="btn-row" style="margin-top:70px"><a class="btn" href="gallery.html">Open the full creative gallery →</a></div>
</div></section>

<section class="section dark" id="analytics"><div class="wrap">
<div class="split"><div><div class="eyebrow">02 — Analytics</div><h2>Creative, with <em>receipts.</em></h2></div>
<div><p class="lede">Verified from a Sprout Social Instagram post-performance export covering {A['period']}. Every post in the export lists me as the sender. Nothing here is estimated, and none of it is presented as sales, conversions or follower growth — the export doesn't measure those.</p></div></div>
<div class="stat-grid">{stats}</div>
<div class="charts">
<figure class="chart" style="margin:0"><h3>Engagements by brand</h3><p class="sub">Total post engagements, Instagram feed (likes, comments, shares, saves).</p>{bars(A['by_brand'], A['by_brand'][0][1])}</figure>
<figure class="chart" style="margin:0"><h3>What earns attention</h3><p class="sub">Average engagements per post by format. Reels here are mostly curated third-party clips — a sourcing insight, not a claim about my own video.</p>{bars(A['by_format'], 35, "{:.1f}")}</figure>
</div>
<p class="source">{A['note']}</p>
<div class="btn-row"><a class="btn" style="background:var(--lime);color:var(--green);border-color:var(--lime)" href="analytics-reporting.html">Analytics &amp; Reporting case study →</a><a class="btn ghost" style="color:#eef0e4;border-color:#6d806f" href="email-marketing.html">Email Marketing case study →</a></div>
</div></section>

<section class="section" id="about"><div class="wrap split">
<div><div class="eyebrow">03 — About</div><h2>Strategist, <em>maker,</em> publisher.</h2></div>
<div>{C.ABOUT}</div>
</div></section>

<section class="section contact" id="contact"><div class="wrap">
<div class="eyebrow">04 — Contact</div>
<h2>Let's make something <em>worth saving.</em></h2>
<p class="lede" style="color:var(--green);margin-top:22px">Open to Social Media Manager, Content Marketing Manager and Marketing Manager roles.</p>
<div class="contact-links">
<a href="mailto:{C.EMAIL}">{C.EMAIL}<span>Email ↗</span></a>
<a href="{C.LINKEDIN}" target="_blank" rel="noopener">linkedin.com/in/polina-gaydamachenko<span>LinkedIn ↗</span></a>
<a href="https://github.com/polinayg" target="_blank" rel="noopener">github.com/polinayg<span>GitHub ↗</span></a>
</div></div></section>
</main>
"""
    out += footer()
    return out

def gallery():
    out = head("Creative Gallery | Polina Gaydamachenko", "Original social media carousels, posts, email headers and campaign graphics designed by Polina Gaydamachenko for five brands.", "gallery.html")
    out += header("gallery")
    brands, queues = [], []
    for p in C.PROJECTS:
        if not p.get("sets"): continue
        brands.append((p["slug"], p["name"]))
        q = []
        for s in p["sets"]:
            for name, alt in s["slides"][: s.get("gallery_take", 2)]:
                full, _ = src(s["folder"], name)
                cap = f'{p["name"]} — {s["title"]}'
                q.append(f'<figure data-brand="{p["slug"]}"><button type="button" data-lb data-group="gallery" data-full="{full}" data-caption="{E(cap)}" aria-label="Open larger: {E(alt)}">'
                         f'{picture(s["folder"], name, alt, "(max-width:600px) 92vw, (max-width:1100px) 45vw, 300px")}</button>'
                         f'<figcaption><span>{E(p["name"])}</span><span>{E(s["format"])}</span></figcaption></figure>')
        queues.append(q)
    figs = []
    while any(queues):
        for q in queues:
            if q: figs.append(q.pop(0))
    btns = '<button type="button" data-filter="all" aria-pressed="true">All work</button>' + "".join(
        f'<button type="button" data-filter="{s}" aria-pressed="false">{E(n)}</button>' for s, n in brands)
    out += f"""<main id="main"><section class="section" style="padding-top:clamp(48px,7vw,90px)"><div class="wrap">
<div class="eyebrow">Creative Gallery</div>
<h1 style="font-size:clamp(44px,7vw,96px)">Made to be <em>seen.</em></h1>
<p class="lede" style="margin-top:24px">A cross-brand selection of original carousels, posts and email headers I designed and wrote. Each image is an export of the real artwork. Curated third-party Reels are kept out of this gallery and labeled on their case-study pages.</p>
<div class="filters" role="group" aria-label="Filter by brand">{btns}</div>
<p id="filter-status" class="sr-only" aria-live="polite"></p>
<div class="masonry">{"".join(figs)}</div>
<p class="small" style="margin-top:30px">Some imagery inside these designs was produced with AI image tools as part of my production workflow; layout, copy and brand application are my work.</p>
</div></section></main>
"""
    out += footer()
    return out

def notfound():
    out = head("Page not found | Polina Gaydamachenko", "This page doesn't exist.", "404.html", extra='<base href="/marketing-portfolio/">\n<meta name="robots" content="noindex">\n')
    out += header()
    out += '<main id="main"><section class="section"><div class="wrap"><div class="eyebrow">404</div><h1>Nothing <em>here.</em></h1><p class="lede" style="margin-top:24px">That page moved or never existed.</p><div class="btn-row"><a class="btn" href="index.html">Back to the portfolio</a></div></div></section></main>'
    out += footer()
    return out

def write(name, s):
    with open(os.path.join(ROOT, name), "w") as f:
        f.write(s)

if __name__ == "__main__":
    write("index.html", home())
    write("gallery.html", gallery())
    write("404.html", notfound())
    ps = C.PROJECTS
    for i, p in enumerate(ps):
        write(p["file"], case_page(p, ps[(i + 1) % len(ps)]))
    urls = [""] + ["gallery.html"] + [p["file"] for p in ps]
    sm = "".join(f"<url><loc>{SITE}{u}</loc><lastmod>{C.DATE}</lastmod></url>" for u in urls)
    write("sitemap.xml", f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{sm}</urlset>\n')
    write("robots.txt", f"User-agent: *\nAllow: /\nSitemap: {SITE}sitemap.xml\n")
    print("built", 3 + len(ps), "pages")
