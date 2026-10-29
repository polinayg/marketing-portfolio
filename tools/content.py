# -*- coding: utf-8 -*-
"""All portfolio content. Metrics come only from the Sprout Social export
'Post Performance (NXT) September 17, 2025 - October 26, 2026.csv' (Instagram feed posts; 2 Stories excluded)."""

SITE_URL = "https://polinayg.github.io/marketing-portfolio/"
VERSION = "2026-10-28"
DATE = "2026-10-28"
EMAIL = "polinayg99@gmail.com"
LINKEDIN = "https://www.linkedin.com/in/polina-gaydamachenko/"

HOME_META = ("Portfolio of Polina Gaydamachenko, a multi-brand digital marketer: social media strategy, original "
             "carousel and email creative, and verified Sprout Social results for Axe & Kindle, NxtDib, Equipio, "
             "Every Window and Levo Aero.")

JSONLD = {
    "@context": "https://schema.org", "@type": "Person", "name": "Polina Gaydamachenko",
    "jobTitle": "Digital Marketer — Social Media & Content", "url": SITE_URL,
    "email": "mailto:" + EMAIL, "sameAs": [LINKEDIN, "https://github.com/polinayg"],
    "knowsAbout": ["Social media marketing", "Content strategy", "Email marketing", "Canva", "Sprout Social", "Buffer"],
}

ANALYTICS = {
    "period": "September 17, 2025 – October 26, 2026",
    "tiles": [("419", "Instagram feed posts published across 3 brand accounts"),
              ("7,057", "Post engagements (likes, comments, shares, saves)"),
              ("1,115", "Saves — content people kept to come back to"),
              ("964", "Shares — content people sent to someone else")],
    "by_brand": [("Equipio", 3685), ("Axe & Kindle", 3082), ("NxtDib", 290)],
    "by_format": [("A&K · Reels", 28.9), ("A&K · Carousels", 7.2), ("A&K · Photos", 4.9),
                  ("Equipio · Reels", 31.6), ("Equipio · Carousels", 8.5), ("Equipio · Photos", 8.9)],
    "note": ("Source: Sprout Social “Post Performance” export for the @axeandkindle, @goequipio and @nxtdib Instagram "
             "accounts, Sept 17, 2025 – Oct 26, 2026 (421 rows; 2 Stories excluded). All 419 feed posts list "
             "“Polina Gaydamachenko” as sender. Figures are sums of post-level interactions, not unique people. "
             "The export contains no revenue, conversion, booking or follower-growth data, so none is claimed. "
             "Every Window and Levo Aero are not in this export."),
}

ABOUT = """<p class="lede">I'm a one-person marketing team at NXT Companies, a vertical-AI venture studio, where I run marketing across its brands — B2C and B2B, products and marketplaces.</p>
<p>My week moves between building monthly content calendars, designing carousels and statics in Canva, writing captions and calls to action, scheduling in Buffer, building email campaigns in Drip, and reading performance in Sprout Social. I adapt voice and visual system to each brand — premium-rustic for firewood, industry-savvy for wholesale beverages, technical for film crews — while keeping the same disciplined process underneath.</p>
<p>I'm now growing into a combined Marketing + AI role: I use AI image generation and writing tools inside a human-edited production workflow to ship more content without lowering the bar.</p>
<ul class="about-list">
<li>Social strategy &amp; content calendars</li><li>Carousel &amp; static design (Canva)</li>
<li>Copywriting, captions &amp; CTAs</li><li>Email campaigns (Drip)</li>
<li>Scheduling &amp; publishing (Buffer)</li><li>Analytics (Sprout Social)</li>
<li>Creator content sourcing &amp; credit</li><li>Landing pages &amp; CMS updates</li>
<li>AI-assisted production</li><li>Instagram · Facebook · LinkedIn</li>
</ul>"""

# Hero mosaic: (link, folder, image, alt, aria-label)
MOSAIC = [
    ("axe-and-kindle.html", "ak", "hickory-oak-01", "Axe & Kindle carousel cover: “Hickory or oak?” over a stacked-firewood fireplace scene", "Axe & Kindle case study"),
    ("nxtdib.html", "nxtdib", "holiday-menu-01", "NxtDib carousel cover: “Plan your holiday drink menu now” with zero-proof cocktails on a bar", "NxtDib case study"),
    ("every-window.html", "every-window", "7-questions-01", "Every Window carousel cover: “7 questions to ask before you sign a window quote”", "Every Window case study"),
    ("axe-and-kindle.html", "ak", "skip-crowds-01", "Axe & Kindle carousel cover: “Skip the crowds. Stay by the fire.”", "Axe & Kindle case study"),
    ("nxtdib.html", "nxtdib", "dry-january-01", "NxtDib carousel cover: “Your Dry January stock list”", "NxtDib case study"),
    ("every-window.html", "every-window", "how-it-works-01", "Every Window carousel cover: “Windows, without the sales visit”", "Every Window case study"),
]

def S(prefix, alts):
    """Helper: build slide list prefix-01..N with matching alt text."""
    return [(f"{prefix}-{i:02d}", a) for i, a in enumerate(alts, 1)]

AK = {
    "slug": "axe-and-kindle", "file": "axe-and-kindle.html", "name": "Axe & Kindle",
    "kicker": "Lifestyle e-commerce · Social + Email",
    "meta": "Axe & Kindle case study: social and email content that sells kiln-dried firewood through fireside lifestyle, education and social proof. Original Canva creative and verified Sprout Social results.",
    "brand": {"bg": "#1f1712", "ink": "#f3e9dc", "accent": "#d6a560", "accent_on_paper": "#8a5a1f"},
    "headline": "Making firewood feel like a <em>ritual.</em>",
    "lede": "Kiln-dried firewood is a practical purchase. My job was to make it feel like the start of something — a fire-lit evening, a cook-out, a slow weekend — and give people a reason to save, share and order.",
    "facts": [("Role", "Social &amp; email marketer"), ("Channels", "Instagram · Facebook · LinkedIn · Email"),
              ("Tools", "Canva · Buffer · Drip · Sprout Social · AI image tools"), ("Period shown", "Sept 2025 – Nov 2026")],
    "card_title": "Making firewood feel like a <em>ritual.</em>",
    "card_text": "Seasonal storytelling, fire-building education and customer proof for a premium kiln-dried firewood brand — across social and email.",
    "kpis": [("3,082", "Engagements"), ("597", "Shares"), ("585", "Saves")],
    "chips": ["Content calendars", "Carousels", "Email headers", "Creator curation"],
    "cover_folder": "ak", "cover": [("top-down-fire-01", "Axe & Kindle “Fire-building 101: the top-down fire” carousel cover"),
                                     ("hickory-oak-01", "Axe & Kindle “Hickory or oak?” carousel cover"),
                                     ("reviews-01", "Axe & Kindle customer review graphic with five stars")],
    "cs": {
        "challenge": {"h": "A commodity that has to <em>feel</em> premium.",
            "body": """<p>Axe &amp; Kindle sells kiln-dried hickory, oak and mixed hardwood with free nationwide delivery. Online, firewood competes with “I'll grab some at the gas station.” The brand needed content that explains why kiln-dried wood is worth it, keeps the account active through the seasons, and earns trust from people who have never bought firewood online.</p>"""},
        "strategy": {"h": "Lifestyle first, then <em>proof.</em>",
            "body": """<ul>
<li><strong>Lead with the moment, not the log.</strong> Fireside evenings, holidays and live-fire cooking carry the emotion; the product shows up as the reason the moment works.</li>
<li><strong>Teach in carousels.</strong> Short, swipeable explainers (hickory vs. oak, the top-down fire, what “kiln-dried” really means) built to be saved.</li>
<li><strong>Borrow attention responsibly.</strong> Curate standout fire-cooking Reels from creators, always credited, to reach new people.</li>
<li><strong>Close with proof and a clear ask.</strong> Real customer reviews, consistent end slides and a single CTA: order at axeandkindle.com, free delivery.</li>
</ul>"""},
        "role": {"h": "Planner, designer, <em>writer</em>, publisher.",
            "body": """<p>I own Axe &amp; Kindle's social and email execution end to end:</p>
<ul><li>Build the monthly content calendar and seasonal themes.</li>
<li>Design carousels, statics, Stories and email headers in Canva, using AI image generation for scene photography and finishing everything by hand.</li>
<li>Write captions, hashtags and CTAs in the brand's premium-rustic voice (“seasoned wood,” never “wet wood”).</li>
<li>Source and credit creator Reels; schedule posts in Buffer; send campaigns in Drip; review results in Sprout Social.</li></ul>
<div class="callout"><b>Verified:</b> all 152 Axe &amp; Kindle Instagram feed posts in the Sprout export list me as the sender.</div>"""},
        "execution": {"h": "A repeatable <em>system</em>, season after season.",
            "body": """<ul>
<li><strong>Carousel formula:</strong> 5–6 slides — a hook cover, numbered steps, and a branded “Firewood, perfected.” end slide with the delivery offer.</li>
<li><strong>Seasonal bridge:</strong> calendars that roll from summer cook-outs into fall fires and holiday hosting (Friendsgiving, gifting, “skip the crowds” on Black Friday).</li>
<li><strong>Email:</strong> a library of 69 email header designs covering every season and holiday, from National Firewood Day to Father's Day.</li>
<li><strong>Social proof:</strong> customer review cards built from real customer quotes.</li>
<li><strong>Channel mix:</strong> Instagram, Facebook and a restaurant- and hospitality-focused LinkedIn angle.</li></ul>"""},
        "results": {"h": "What the data <em>actually</em> shows.",
            "body": """<div class="metric-grid"><div><b>152</b><span>Feed posts published</span></div><div><b>3,082</b><span>Engagements</span></div><div><b>597</b><span>Shares</span></div><div><b>585</b><span>Saves</span></div></div>
<ul>
<li><strong>Top post:</strong> a curated wood-fired cooking Reel (Nov 28, 2025) earned <strong>686 engagements, 208 shares and 162 saves</strong> from 7,011 accounts reached and 10,089 views. It is a standout, not a typical post.</li>
<li><strong>Format matters:</strong> Reels averaged <strong>28.9</strong> engagements per post vs. <strong>7.2</strong> for carousels and <strong>4.9</strong> for photos, with a median reach of 263 vs. about 105.</li>
<li><strong>Original carousels earn saves:</strong> carousels averaged 1.3 saves per post vs. 0.3 for single photos; the Oct 1, 2026 “five fall meals” carousel led original posts with 22 engagements.</li>
</ul>
<p class="small">Source: Sprout Social Instagram post-performance export, Sept 17, 2025 – Oct 26, 2026. Interaction totals are not unique users. The export has no sales or conversion data, so no revenue impact is claimed. November 2026 work shown below was scheduled after this export.</p>"""},
        "takeaways": {"h": "What I'd carry <em>forward.</em>",
            "body": """<ol class="takeaways">
<li>Earn the save or the share before asking for the sale — moments and how-tos outperform product shots.</li>
<li>Curated video reaches people; original carousels give them something to keep. A healthy calendar needs both, clearly credited.</li>
<li>A strict template (hook → steps → branded end slide) is what makes a one-person team consistent across months.</li>
<li>Next step: tie social and email to site traffic and orders so content decisions can be judged on revenue, not just engagement.</li>
</ol>"""},
    },
    "sets": [
        {"folder": "ak", "title": "Hickory or oak?", "format": "Carousel · 6 slides", "status": "Scheduled · Nov 2026",
         "desc": "A buying guide disguised as a fireside scroll: what each species does best, and when to mix them.",
         "slides": S("hickory-oak", ["Cover: “Hickory or oak?” over a stacked woodpile beside a lit fireplace",
             "Slide 1: “Hickory burns hot” — dense hardwood with serious heat and a sweet aroma",
             "Slide 2: “Oak burns long” — slow, steady flames and a deep bed of coals",
             "Slide 3: “Cooking? Reach for hickory” — sweet smoke for fire-pit cooking",
             "Slide 4: “Can't decide? Mix them” — hickory for heat, oak to keep it going",
             "End slide: “Firewood, perfected.” with free nationwide curbside delivery and order link"])},
        {"folder": "ak", "title": "Fire-building 101: the top-down fire", "format": "Carousel · 6 slides", "status": "Scheduled · Nov 2026",
         "desc": "A four-step how-to designed to be saved and used — and to show why dry wood matters.",
         "slides": S("top-down-fire", ["Cover: “Fire-building 101: the top-down fire” in a stone fireplace",
             "Step 1: “Big splits on the bottom” laid side by side on the grate",
             "Step 2: “Medium splits, crosswise” as a second layer",
             "Step 3: “Kindling on top” to finish the stack",
             "Step 4: “Light the top. Let it burn down.” — no tending needed",
             "End slide: “Firewood, perfected.” with delivery offer"])},
        {"folder": "ak", "title": "Skip the crowds, stay by the fire", "format": "Carousel · 6 slides", "status": "Scheduled · Nov 2026",
         "desc": "A Black Friday counter-programming story: a slow, fireside day — with delivery as the quiet hero.",
         "slides": S("skip-crowds", ["Cover: “Skip the crowds. Stay by the fire.” cozy living room by a fireplace",
             "“Fire on by breakfast” — a slow morning fire by a frosty window",
             "“Leftovers, fireside” — a holiday sandwich plate by the hearth",
             "“Slippers on, phone down” — wool socks up by the fire",
             "“Running low? We deliver.” — a wrapped firewood stack at a front porch",
             "End slide: “Firewood, perfected.” with order link"])},
        {"folder": "ak", "title": "Customer review series", "format": "Social proof · 4 posts",
         "desc": "Real customer quotes turned into a consistent, on-brand review format.",
         "slides": S("reviews", ["Customer review card from Mark B., Illinois, with five stars over a woodpile",
             "Customer review card from Keith D. with five stars",
             "Customer review card from Christopher H., Florida, with five stars",
             "Customer review card from Richard C., Maryland, with five stars"])},
        {"folder": "ak", "title": "What “kiln-dried” really means", "format": "Carousel · 5 slides", "status": "Published · Jan 2026",
         "desc": "Product education in five bold statements, from “wet wood smokes” to “order now.”",
         "slides": S("jan-carousel", ["Cover: “Firewood, answered. What kiln-dried really means.” over flames",
             "“Wet wood smokes. Dry wood performs.” split-screen fireplace comparison",
             "“Kiln-dried firewood = low moisture” — cleaner burn, more heat, less smoke",
             "“Less moisture = better fires. Every time.” modern living room fireplace",
             "“Kiln-dried isn't marketing. It's performance.” with order link"])},
        {"folder": "ak-email", "title": "Email header library", "format": "Email · 69 designs (12 shown)", "square": True,
         "desc": "Seasonal and holiday email headers for Drip campaigns — a year of reasons to light a fire.", "gallery_take": 4,
         "slides": [("email-01", "Email header: “Celebrate National Firewood Day — stock up on the best firewood!”"),
                    ("email-05", "Email header: “Winter is here — stock up on premium firewood” with a family by the fire"),
                    ("email-09", "Email header: “Happy Thanksgiving from Axe & Kindle!” dinner table by the fireplace"),
                    ("email-12", "Email header: Valentine's Day — “Turn up the romance” fireside couple"),
                    ("email-19", "Email header: “Maximize your firewood's performance with premium kiln-dried wood!”"),
                    ("email-24", "Email header: “Elevate every fire: why chefs and homeowners choose kiln-dried wood” with pizza"),
                    ("email-30", "Email header: “See why kitchens and campfires alike rely on Axe & Kindle”"),
                    ("email-36", "Email header: “Perfectly smoked meats start with hickory firewood”"),
                    ("email-42", "Email header: “Halloween nights need firewood that lasts” with jack-o'-lanterns"),
                    ("email-47", "Email header: “Winter starts with the right firewood” with a gift-wrapped stack"),
                    ("email-52", "Email header: “Oak. Hickory. Mixed hardwood… here's how to choose.”"),
                    ("email-64", "Email header: “There's a flavor your grill has been missing”")]},
        {"folder": "ak", "title": "Holiday statics", "format": "Static posts", "status": "Scheduled · Nov 2026",
         "desc": "Single-image posts for Friendsgiving and gifting.",
         "slides": [("friendsgiving", "Static post: “Friendsgiving, by the fire.” friends at an outdoor table around a fire pit"),
                    ("gift-of-warmth", "Static post: “Give the gift of warmth.” a firewood tote with a red bow by the fire")]},
    ],
    "reels": [
        {"title": "Wood-fired stove cooking", "url": "https://www.instagram.com/reel/DRmqpCciF0i/", "eng": "686", "shares": "208", "saves": "162",
         "note": "Nov 28, 2025 · 7,011 accounts reached · 10,089 views. The account's top post in the period."},
        {"title": "Wood-fired hot tub", "url": "https://www.instagram.com/reel/DTslHZOjSfp/", "eng": "152", "shares": "26", "saves": "39",
         "note": "Jan 19, 2026 · 1,370 accounts reached · 2,214 views."},
        {"title": "Simple food over real fire", "url": "https://www.instagram.com/reel/DZ5F772CBvL/", "eng": "98", "shares": "35", "saves": "38",
         "note": "Jun 22, 2026 · 1,229 accounts reached · 1,424 views."},
    ],
}

NX = {
    "slug": "nxtdib", "file": "nxtdib.html", "name": "NxtDib",
    "kicker": "B2B marketplace · Editorial content",
    "meta": "NxtDib case study: an editorial B2B content system for a wholesale non-alcoholic and functional beverage marketplace, with original carousels for Instagram and LinkedIn.",
    "brand": {"bg": "#1a4a45", "ink": "#f5edd8", "accent": "#f5a623", "accent_on_paper": "#b26f00"},
    "headline": "Turning category shifts into <em>shelf decisions.</em>",
    "lede": "NxtDib is a wholesale marketplace for non-alcoholic, CBD and functional beverages. Its buyers are busy retailers and bar operators — so every post had to be something they could act on.",
    "facts": [("Role", "Content strategist &amp; designer"), ("Channels", "Instagram · LinkedIn · Facebook"),
              ("Tools", "Canva · ChatGPT image generation · Buffer · Sprout"), ("Period shown", "Sept 2025 – Nov 2026")],
    "card_title": "Turning category shifts into <em>shelf decisions.</em>",
    "card_text": "An editorial B2B content system for a wholesale beverage marketplace: buyer checklists, merchandising playbooks and seasonal stocking guides.",
    "kpis": [("114", "Feed posts"), ("58", "Carousels"), ("3", "Channels")],
    "chips": ["B2B content", "LinkedIn carousels", "Brand system", "AI-assisted production"],
    "cover_folder": "nxtdib", "cover": [("li-10-questions-01", "NxtDib LinkedIn carousel cover: “10 questions to ask before a first order”"),
                                         ("holiday-menu-01", "NxtDib carousel cover: “Plan your holiday drink menu now”"),
                                         ("li-cooler-door-01", "NxtDib LinkedIn carousel cover: “Same cooler door. New set.”")],
    "cs": {
        "challenge": {"h": "Busy buyers. A fast-moving <em>category.</em>",
            "body": """<p>Non-alcoholic and functional beverages change quickly — new formats, new occasions like Dry January, new rules for hemp-derived products. NxtDib needed to be useful to retail and hospitality buyers without turning every post into a sales pitch, on accounts that were still small.</p>"""},
        "strategy": {"h": "Be the buyer's <em>playbook.</em>",
            "body": """<ul>
<li><strong>Answer real buyer questions:</strong> what to stock, how to merchandise it, when to reorder, what to ask a brand before a first order.</li>
<li><strong>Plan around buying calendars:</strong> holiday menus in early November, Dry January stock lists before December shelves are set.</li>
<li><strong>Use one recognizable system:</strong> teal, warm orange and cream; 4:5 frames; a consistent “Stock what's next.” end slide.</li>
<li><strong>Write once, post twice:</strong> captions written to work on both Instagram and LinkedIn, plus LinkedIn-native carousels in a quieter editorial style.</li>
</ul>"""},
        "role": {"h": "From calendar to <em>caption.</em>",
            "body": """<ul><li>Built monthly content calendars and seasonal themes.</li>
<li>Wrote every carousel script, caption and CTA in a modern, industry-savvy voice.</li>
<li>Produced imagery with ChatGPT image generation, then designed and finished every slide in Canva.</li>
<li>Published to Instagram, LinkedIn and Facebook and tracked performance.</li></ul>
<div class="callout"><b>Verified:</b> all 114 NxtDib Instagram feed posts in the Sprout export list me as the sender.</div>"""},
        "execution": {"h": "A content system, not <em>one-off posts.</em>",
            "body": """<ul>
<li><strong>Instagram carousels</strong> for seasonal stocking: holiday drink menus, Thanksgiving hosting, Dry January, zero-proof merchandising.</li>
<li><strong>LinkedIn document carousels</strong> in a quieter editorial style: a 10-question first-order checklist, a cooler-door reset, a reorder-point formula.</li>
<li><strong>Statics</strong> that hold the calendar together between carousels.</li>
<li><strong>Volume with consistency:</strong> 114 feed posts in the period — 58 carousels, 52 photos and 4 Reels.</li></ul>"""},
        "results": {"h": "Honest numbers for an <em>early</em> channel.",
            "body": """<div class="metric-grid"><div><b>114</b><span>Feed posts published</span></div><div><b>58</b><span>Carousels</span></div><div><b>290</b><span>Engagements</span></div><div><b>9</b><span>Median accounts reached per post</span></div></div>
<p>The Instagram account was very small during this period — a median reach of nine accounts per post — so engagement rates would look impressive and mean little. I'm presenting NxtDib as proof of a consistent, high-quality B2B content system, not as an audience-growth story.</p>
<p class="small">Source: Sprout Social Instagram post-performance export, Sept 17, 2025 – Oct 26, 2026. LinkedIn and Facebook results are not included in this export.</p>"""},
        "takeaways": {"h": "What I'd carry <em>forward.</em>",
            "body": """<ol class="takeaways">
<li>In B2B, usefulness is the hook: checklists and formulas beat announcements.</li>
<li>A tight visual system lets AI-assisted production scale without the feed looking generated.</li>
<li>Small audiences deserve honest reporting; the next lever is distribution — LinkedIn and email to buyers — rather than more posts.</li>
</ol>"""},
    },
    "sets": [
        {"folder": "nxtdib", "title": "10 questions to ask before a first order", "format": "LinkedIn carousel · 8 slides",
         "desc": "A buyer checklist that positions NxtDib as the place to ask brands directly.",
         "slides": S("li-10-questions", ["Cover: “10 questions to ask before a first order” buyer checklist",
             "Questions 1–2: shelf life and case pack", "Questions 3–4: minimum advertised price and promo support",
             "Questions 5–6: reorder lead time and damaged-product policy",
             "Questions 7–8: sell-through in similar stores and hemp product compliance",
             "Questions 9–10: marketing assets and day-to-day contact", "First-order checklist summary with tick boxes",
             "End slide: “Ask brands directly” with “Create a buyer account” button"])},
        {"folder": "nxtdib", "title": "Plan your holiday drink menu", "format": "Carousel · 6 slides", "status": "Scheduled · Nov 2026",
         "desc": "Five menu moves for bars and restaurants ahead of the holidays.",
         "slides": S("holiday-menu", ["Cover: “Plan your holiday drink menu now” with cocktails on a bar",
             "“Lead with a zero-proof signature” — a garnished coupe cocktail",
             "“Pour alcohol-removed wine by the glass” — rosé being poured",
             "“Add a sparkling option for every table” — champagne bucket and coupes",
             "“Price zero-proof like a cocktail” — bartender finishing a drink",
             "End slide: “Stock what's next. Shop wholesale at nxtdib.com”"])},
        {"folder": "nxtdib", "title": "Same cooler door. New set.", "format": "LinkedIn carousel · 6 slides",
         "desc": "A before-and-after merchandising diagram that turns planogram logic into five rules.",
         "slides": S("li-cooler-door", ["Cover: “Same cooler door. New set.” merchandising carousel",
             "Before: a cooler door scattered by brand, shown as a color-coded grid",
             "After: the cooler door blocked by category",
             "Rules 1–3: block by category, newest category at eye level, tier by price",
             "Rules 4–5: hero item in the hot spot, leave one facing open",
             "Cooler door self-audit checklist"])},
        {"folder": "nxtdib", "title": "Your Dry January stock list", "format": "Carousel · 6 slides", "status": "Scheduled · Nov 2026",
         "desc": "Category-by-category guidance timed to when buyers set December shelves.",
         "slides": S("dry-january", ["Cover: “Your Dry January stock list” with bottles and cans",
             "“NA spirits” — amber bottles and a cocktail glass", "“Alcohol-removed wine and beer”",
             "“Functional sparkling” — cans on ice", "“Botanical and adaptogen drinks”",
             "End slide: “Stock what's next.”"])},
        {"folder": "nxtdib", "title": "Merchandise zero-proof like it matters", "format": "Carousel · 6 slides", "status": "Scheduled · Nov 2026",
         "desc": "Retail merchandising tips: eye-level space, cross-merch, gift bundles and staff storytelling.",
         "slides": S("merch-zero-proof", ["Cover: “Merchandise zero-proof like it matters” — a lit retail shelf",
             "“Give it eye-level space”", "“Cross-merch with mixers and glassware”", "“Build ready-to-gift bundles”",
             "“Teach your team the story” — staff pouring a sample", "End slide: “Stock what's next.”"])},
        {"folder": "nxtdib", "title": "Stop guessing when to reorder", "format": "LinkedIn carousel · 5 slides",
         "desc": "A reorder-point formula with a worked example for wholesale buyers.",
         "slides": S("li-reorder-point", ["Cover: “Stop guessing when to reorder. One formula. Three inputs.”",
             "The reorder-point formula: average weekly units × lead time + safety stock",
             "Worked example with illustrative numbers: reorder at 30 units",
             "Three ways to make it work: safety stock for peaks, protect top sellers, automate",
             "End slide: “Set it and restock on autopilot” with buyer-account button"])},
        {"folder": "nxtdib", "title": "What Thanksgiving hosts are buying", "format": "Carousel · 5 slides", "status": "Scheduled · Nov 2026",
         "desc": "Consumer demand translated into a retailer's stocking list.",
         "slides": S("thanksgiving-hosts", ["Cover: “What Thanksgiving hosts are buying” — a shopper at a beverage aisle",
             "“Alcohol-removed wine for the table”", "“NA spirits for the bar cart”",
             "“Sparkling botanicals for every age”", "End slide: “Stock what's next.”"])},
        {"folder": "nxtdib", "title": "Seasonal statics", "format": "Static posts", "status": "Scheduled · Nov 2026",
         "desc": "Single-image posts that keep the calendar moving between carousels.",
         "slides": [("holiday-shelves", "Static post: “Holiday shelves are built in November” beside a stocked wine wall"),
                    ("every-guest-toast", "Static post: “Every guest gets a toast” — glasses raised in a circle frame"),
                    ("dry-january-shelf", "Static post: “Dry January starts on your December shelf”"),
                    ("zero-proof-new-year", "Static post: “Ring in a zero-proof New Year” — a toast with sparklers")]},
    ],
}

EQ = {
    "slug": "equipio", "file": "equipio.html", "name": "Equipio",
    "kicker": "B2B marketplace · Niche community",
    "meta": "Equipio case study: social content for a film and TV equipment rental marketplace, combining curated creator Reels with RFQ-focused educational content. Verified Sprout Social results.",
    "brand": {"bg": "#141d26", "ink": "#e8edf1", "accent": "#7fb3d5", "accent_on_paper": "#2f5f80"},
    "headline": "Speaking the language of <em>film crews.</em>",
    "lede": "Equipio is a B2B marketplace where productions request quotes for film and TV equipment. Filmmakers care about craft and gear details — generic marketplace promotion doesn't earn their attention.",
    "facts": [("Role", "Social content strategist"), ("Channels", "Instagram · LinkedIn"),
              ("Tools", "Canva · Buffer · Sprout Social"), ("Period shown", "Sept 2025 – Oct 2026")],
    "card_title": "Speaking the language of <em>film crews.</em>",
    "card_text": "Gear breakdowns, rig curation and RFQ education for a film and TV equipment rental marketplace.",
    "kpis": [("3,685", "Engagements"), ("526", "Saves"), ("365", "Shares")],
    "chips": ["Creator curation", "Community content", "RFQ education", "LinkedIn"],
    "cover_label": "Case study · creative exports coming soon",
    "pending_note": "<b>Original Equipio creative is being exported from Canva</b> (RFQ explainer carousels and single-post templates) and will appear here. In the meantime, the curated Reels below are linked with their verified metrics.",
    "cs": {
        "challenge": {"h": "Relevance in a <em>technical</em> community.",
            "body": """<p>Equipio's audience is cinematographers, gaffers, producers and rental houses. They follow accounts that show interesting rigs and real productions. The challenge was to become part of that feed while still steering people to Equipio's value proposition: request a quote for the gear you need instead of hunting vendor by vendor.</p>"""},
        "strategy": {"h": "Earn the follow with craft, then <em>connect to the RFQ.</em>",
            "body": """<ul>
<li><strong>Craft-first curation:</strong> standout rig breakdowns and behind-the-scenes clips from working filmmakers, always credited.</li>
<li><strong>Original education:</strong> carousels that explain the rental and RFQ process in plain language.</li>
<li><strong>Channel discipline:</strong> Instagram can include credited reposts; LinkedIn gets original content only.</li>
<li><strong>One consistent CTA:</strong> “Skip the vendor hunt. Upload your RFQ at equipio.com.”</li>
</ul>"""},
        "role": {"h": "Curator, writer, <em>publisher.</em>",
            "body": """<ul><li>Planned Instagram and LinkedIn calendars (for example, 13 posts a month at three per week for June–August).</li>
<li>Found and credited creator content, wrote gear-literate captions and CTAs.</li>
<li>Designed original carousels and single-post templates in Canva.</li>
<li>Scheduled, published and reviewed performance.</li></ul>
<div class="callout"><b>Verified:</b> all 153 Equipio Instagram feed posts in the Sprout export list me as the sender.</div>"""},
        "execution": {"h": "Gear content with a <em>point.</em>",
            "body": """<ul>
<li><strong>Rig breakdowns</strong> like recreating the “Severance” camera look, gimbal and stabilizer setups, and precision crane moves.</li>
<li><strong>Captions that name the gear</strong> — cameras, lenses, rigs — because that's what this audience searches for and saves.</li>
<li><strong>RFQ explainers</strong> that show how renting through Equipio works.</li>
<li><strong>Mix:</strong> 103 Reels, 32 carousels and 18 photo posts in the period.</li></ul>"""},
        "results": {"h": "Strong attention, <em>honestly attributed.</em>",
            "body": """<div class="metric-grid"><div><b>153</b><span>Feed posts published</span></div><div><b>3,685</b><span>Engagements</span></div><div><b>526</b><span>Saves</span></div><div><b>365</b><span>Shares</span></div></div>
<ul>
<li>The highest engagement of any brand in the export, driven mainly by curated Reels: Reels averaged <strong>31.6</strong> engagements per post vs. <strong>8.5</strong> for carousels and <strong>8.9</strong> for photos.</li>
<li><strong>Top post:</strong> the “Severance” look gear breakdown (Nov 17, 2025) — <strong>282 engagements</strong>, 33 shares, 22 saves, 4,047 accounts reached.</li>
<li>These are engagement results, not bookings. Reach also varied a lot across the period, which I'd treat as a testing opportunity rather than a growth claim.</li>
</ul>
<p class="small">Source: Sprout Social Instagram post-performance export, Sept 17, 2025 – Oct 26, 2026. No RFQ, booking or revenue data is included in the export.</p>"""},
        "takeaways": {"h": "What I'd carry <em>forward.</em>",
            "body": """<ol class="takeaways">
<li>In a craft community, specificity is the strategy — name the gear, show the setup.</li>
<li>Curated content builds the audience; original RFQ content has to do the converting. Measure them separately.</li>
<li>Next step: tag RFQ links by post so social can be judged on quote requests.</li>
</ol>"""},
    },
    "sets": [],
    "reels": [
        {"title": "Recreating the “Severance” look", "url": "https://www.instagram.com/reel/DRKTZA-iqnH/", "eng": "282", "shares": "33", "saves": "22",
         "note": "Nov 17, 2025 · gear breakdown · 4,047 accounts reached · 5,220 views."},
        {"title": "Precision crane move", "url": "https://www.instagram.com/reel/DPo82GEACgj/", "eng": "239", "shares": "20", "saves": "3",
         "note": "Oct 10, 2025 · 3,948 accounts reached · 7,239 views."},
        {"title": "Whip-transition camera move", "url": "https://www.instagram.com/reel/DQCuE-5CgUM/", "eng": "136", "shares": "12", "saves": "20",
         "note": "Oct 20, 2025 · 2,437 accounts reached · 3,521 views."},
    ],
}

EW = {
    "slug": "every-window", "file": "every-window.html", "name": "Every Window",
    "kicker": "E-commerce · Buyer education",
    "meta": "Every Window case study: a buyer-education social content system for an online custom vinyl window brand, designed to match the website and drive people to design and price online.",
    "brand": {"bg": "#0f3f42", "ink": "#f1ede2", "accent": "#c9c08a", "accent_on_paper": "#5f6a1f"},
    "headline": "Windows, without the <em>sales visit.</em>",
    "lede": "Every Window lets homeowners and property managers design, price and order custom vinyl windows online. Most people have never bought windows without a salesperson — the content had to replace that conversation.",
    "facts": [("Role", "Social content lead"), ("Channels", "Instagram · Facebook · LinkedIn"),
              ("Tools", "Canva · AI image tools · Buffer"), ("Period shown", "Oct 28 – Nov 27, 2026")],
    "card_title": "Windows, without the <em>sales visit.</em>",
    "card_text": "A month-long buyer-education program — quote checklists, style comparisons and repair-or-replace guides — built to look and sound like the website.",
    "kpis": [("19", "Posts planned"), ("4/wk", "Cadence"), ("3", "Channels")],
    "chips": ["Content calendar", "Educational carousels", "Brand consistency", "LinkedIn documents"],
    "cover_folder": "every-window", "cover": [("how-it-works-01", "Every Window carousel cover: “Windows, without the sales visit”"),
                                               ("7-questions-01", "Every Window carousel cover: “7 questions to ask before you sign a window quote”"),
                                               ("single-vs-double-01", "Every Window carousel cover: “Single-hung vs. double-hung”")],
    "cs": {
        "challenge": {"h": "A considered purchase, <em>bought online.</em>",
            "body": """<p>Replacement windows are expensive, technical and usually sold in-home. Buyers worry about getting the measurements, styles and quote details wrong. To sell online, Every Window needed content that answers those questions before they become objections — and that looks unmistakably like the brand's own site.</p>"""},
        "strategy": {"h": "Answer the questions a salesperson <em>would.</em>",
            "body": """<ul>
<li><strong>Educate before selling:</strong> how quotes differ, single- vs. double-hung, repair vs. replace, condensation, U-factor and SHGC.</li>
<li><strong>Make the website the hero:</strong> every carousel ends on “Design &amp; price your windows” at everywindow.com.</li>
<li><strong>Match the site exactly:</strong> the deep-teal, cream and khaki palette, clean sans-serif type and the real Every Window logo.</li>
<li><strong>Serve two audiences:</strong> homeowners, plus landlords and maintenance teams (rental-turn and PRO Desk content).</li>
</ul>"""},
        "role": {"h": "Calendar, copy, design, <em>scheduling.</em>",
            "body": """<ul><li>Planned a four-posts-a-week calendar across Instagram, Facebook and LinkedIn.</li>
<li>Wrote every carousel and caption; designed all slides at 4:5 with AI-generated scene photography finished in the brand system.</li>
<li>Exported LinkedIn versions of each carousel as document posts.</li>
<li>Loaded the program into Buffer as drafts with channel-specific posting times.</li></ul>"""},
        "execution": {"h": "Nineteen posts, one <em>system.</em>",
            "body": """<ul>
<li><strong>Oct 28 – Nov 27, 2026:</strong> 19 posts — 9 carousels and 10 statics — each published to three channels.</li>
<li><strong>Repeatable series</strong> such as “Measure once” and “Price check” episodes that can run month after month.</li>
<li><strong>Carousel anatomy:</strong> a photographic cover, cream-background teaching slides with large numerals, and a teal CTA slide.</li></ul>"""},
        "results": {"h": "Launched — results to <em>come.</em>",
            "body": """<p>This program starts publishing on October 28, 2026, after the Sprout Social export used elsewhere on this site, so there is no performance data to report yet. I'm including it for the strategy and the creative system. Results will be added once the month completes.</p>
<div class="callout"><b>What I'll measure:</b> saves and shares per carousel, link clicks to the window designer, and which educational topics drive the most visits to pricing.</div>"""},
        "takeaways": {"h": "What I'd carry <em>forward.</em>",
            "body": """<ol class="takeaways">
<li>For considered purchases, content should remove one specific fear per post.</li>
<li>Designing to the website's system builds trust when people click through.</li>
<li>Series formats make a four-a-week cadence sustainable for a small team.</li>
</ol>"""},
    },
    "sets": [
        {"folder": "every-window", "title": "Windows, without the sales visit", "format": "Carousel · 5 slides", "status": "Scheduled · Oct 2026",
         "desc": "The brand's three-step promise: design, price, deliver.",
         "slides": S("how-it-works", ["Cover: “Windows, without the sales visit” — hands on a laptop",
             "Step 1 “Design”: choose replacement or new construction, then style, size and color online",
             "Step 2 “Price”: see your price instantly, no callbacks",
             "Step 3 “Deliver”: delivered to your home or jobsite",
             "End slide: “Design your windows in minutes” with PRO Desk note"])},
        {"folder": "every-window", "title": "7 questions to ask before you sign a window quote", "format": "Carousel · 10 slides", "status": "Scheduled · Nov 2026",
         "desc": "A quote-comparison checklist that builds trust by helping buyers shop smarter.",
         "slides": S("7-questions", ["Cover: “7 questions to ask before you sign a window quote” — clipboard and tape measure",
             "Intro: most quote differences come from what's included, not the window",
             "Question 1: is this price installed or product-only?", "Question 2: is removal and disposal included?",
             "Question 3: full-frame or insert replacement?", "Question 4: what glass package is included?",
             "Question 5: who handles trim, caulk and finish work?", "Question 6: what does the warranty cover, and who backs it?",
             "Question 7: how long from order to install?", "End slide: “Want a number you can compare?” with design-and-price button"])},
        {"folder": "every-window", "title": "4 signs it's time to replace, not repair", "format": "Carousel · 8 slides", "status": "Scheduled · Nov 2026",
         "desc": "A simple screen for homeowners, landlords and maintenance teams.",
         "slides": S("repair-vs-replace", ["Cover: “4 signs it's time to replace, not repair” — a weathered window frame",
             "Intro: not every drafty window needs replacing", "Sign 1: fog or moisture between the panes",
             "Sign 2: drafts around the sash, not just the trim", "Sign 3: windows that stick or won't lock",
             "Sign 4: soft, rotting or cracked frames", "Rule of thumb: one sign, maybe repair; two or more, price a replacement",
             "End slide: “See what a replacement actually costs”"])},
        {"folder": "every-window", "title": "Single-hung vs. double-hung", "format": "Carousel · 6 slides", "status": "Scheduled · Nov 2026",
         "desc": "Product education with simple line diagrams and a side-by-side comparison.",
         "slides": S("single-vs-double", ["Cover: “Single-hung vs. double-hung: which do you need?”",
             "Single-hung diagram: only the bottom sash moves", "Double-hung diagram: both sashes move",
             "Quick side-by-side comparison of both styles", "Rule of thumb: double-hung for cleaning access, single-hung for budget",
             "End slide: “Compare both styles” in the builder"])},
        {"folder": "every-window", "title": "Statics", "format": "Static posts", "status": "Scheduled · Nov 2026",
         "desc": "Single-image posts for pricing, engagement prompts and seasonal timing.",
         "slides": [("see-your-price", "Static post: “See your window price in minutes.” laptop by a sunny window"),
                    ("price-check", "Static post: “Price check” — comment a style and size to see a real price"),
                    ("window-prop", "Static post: “If your window needs a prop… it might be time.”"),
                    ("condensation", "Static post: “On the glass, or between the panes?” condensation explainer"),
                    ("order-now", "Static post: “Order now. Install when your crew is ready.”")]},
    ],
}

LEVO = {
    "slug": "levo-aero", "file": "levo-aero.html", "name": "Levo Aero",
    "kicker": "Aviation marketplace · Web + paid creative",
    "meta": "Levo Aero case study: Enterprise pricing landing pages and paid-social creative for a private aviation marketplace.",
    "brand": {"bg": "#0d1726", "ink": "#e9eef6", "accent": "#9fc3ff", "accent_on_paper": "#2c4f86"},
    "headline": "Making private aviation <em>pricing</em> clear.",
    "lede": "Levo Aero is a private aviation marketplace. My work there sits closer to the website and paid media: landing pages that explain pricing tiers, and ad creative for social channels.",
    "facts": [("Role", "Digital marketer"), ("Channels", "Website · LinkedIn · Instagram"),
              ("Tools", "CMS · Canva"), ("Status", "Case study in progress")],
    "card_title": "Making private aviation <em>pricing</em> clear.",
    "card_text": "Enterprise pricing landing pages built in the CMS, plus paid-social ad creative for LinkedIn and Instagram.",
    "kpis": [("4", "Enterprise pricing pages")],
    "chips": ["Landing pages", "CMS", "Pricing tiers", "Ad creative"],
    "cover_label": "Case study · creative exports coming soon",
    "pending_note": "<b>Levo ad creative is being exported from Canva</b> (LinkedIn and Instagram ad designs) and will appear here. No campaign performance data is reported for this project.",
    "cs": {
        "challenge": {"h": "A premium service needs a <em>clear</em> price story.",
            "body": """<p>Enterprise customers evaluating a private aviation platform need to understand what each tier includes and how to buy it. Those pages needed to exist as distinct, shareable URLs that sales conversations could point to.</p>"""},
        "strategy": {"h": "One page per tier, <em>one clear path.</em>",
            "body": """<ul><li>Give each Enterprise tier its own landing page and unique URL for customer-facing use.</li>
<li>Reuse proven page structures so the experience stays consistent with the rest of the site.</li>
<li>Support awareness with clean, on-brand ad creative sized for LinkedIn and Instagram.</li></ul>"""},
        "role": {"h": "Builder and <em>designer.</em>",
            "body": """<ul><li>Built four Enterprise pricing landing pages in the development CMS, starting from existing pages and adapting them to tiered pricing.</li>
<li>Designed paid-social ad creative in Canva for LinkedIn and Instagram placements.</li></ul>"""},
        "execution": {"h": "Pages first, <em>then promotion.</em>",
            "body": """<ul><li>Duplicated and restructured existing pages so all four tiers share a consistent layout.</li>
<li>Set up unique URLs per tier for direct customer use.</li>
<li>Produced ad layouts in feed, story and LinkedIn sizes.</li></ul>"""},
        "results": {"h": "Delivered — <em>no metrics claimed.</em>",
            "body": """<p>The four Enterprise pricing pages were delivered with unique, customer-facing URLs. Levo is not part of the Sprout Social export and I don't have campaign or conversion data for this work, so I'm not reporting any performance figures.</p>"""},
        "takeaways": {"h": "What I'd carry <em>forward.</em>",
            "body": """<ol class="takeaways"><li>Pricing pages are sales tools — one URL per tier makes them easy to share in a deal.</li>
<li>Next step: add analytics events to each tier page so marketing can see which tier gets the most interest.</li></ol>"""},
    },
    "sets": [],
}

PROJECTS = [AK, NX, EQ, EW, LEVO]
