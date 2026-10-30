# -*- coding: utf-8 -*-
"""Portfolio content. Social post metrics use the Sprout Social export;
capability case studies identify their separate analytics presentation sources.
Historical reporting describes observations, not attributable campaign lift."""

SITE_URL = "https://polinayg.github.io/marketing-portfolio/"
VERSION = "2026-10-29"
DATE = "2026-10-29"
EMAIL = "polinayg99@gmail.com"
LINKEDIN = "https://www.linkedin.com/in/polina-gaydamachenko/"
RESUME_FILE = "assets/docs/Polina_Gaydamachenko_Resume.pdf?v=2026-10-29-aligned"

HOME_META = ("Portfolio of Polina Gaydamachenko, Multi-Brand Marketing Manager: social and email campaigns, "
             "website builds and redesigns, paid advertising and analytics across four B2C and B2B brands.")

JSONLD = {
    "@context": "https://schema.org", "@type": "Person", "name": "Polina Gaydamachenko",
    "jobTitle": "Multi-Brand Marketing Manager", "url": SITE_URL,
    "email": "mailto:" + EMAIL, "sameAs": [LINKEDIN, "https://github.com/polinayg"],
    "knowsAbout": ["Marketing strategy", "Social media marketing", "Email marketing", "Website design", "Paid advertising", "Google Analytics 4", "Content strategy"],
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
    "note": ("Source: Sprout Social Post Performance export, Sept 17, 2025 – Oct 26, 2026: 419 Instagram feed posts "
             "across @axeandkindle, @goequipio and @nxtdib (2 Stories excluded), all listing Polina Gaydamachenko as sender. "
             "Totals count post-level interactions, not unique people, and include original creative and curated Reels. "
             "Every Window is outside this export. These are content metrics, not revenue, conversion or follower-growth results."),
}

ABOUT = """<p class="lede">I'm the Multi-Brand Marketing Manager at NXT Companies, a vertical-AI venture studio, managing marketing across four B2C and B2B brands.</p>
<p>I connect planning with hands-on execution: social content and publishing, email campaigns in Drip, website builds and redesigns in the CMS, and Google and Meta advertising. My work spans consumer products, wholesale marketplaces, home improvement, and film equipment.</p>
<p>I use GA4, Google Search Console and Sprout Social to understand performance and turn findings into campaign and website recommendations. I adapt the message and visual system to each audience while keeping the work consistent across channels.</p>
<p>AI image generation and writing tools are part of my production workflow, with my editing, design decisions and brand review guiding the final work.</p>
<ul class="about-list">
<li>Multi-brand marketing strategy</li><li>Social content &amp; publishing</li>
<li>Email campaigns &amp; copywriting</li><li>Website builds &amp; redesigns</li>
<li>Google Ads &amp; Meta Ads</li><li>GA4 &amp; Search Console analysis</li>
<li>Creative design (Canva)</li><li>CMS page building</li>
<li>Reporting &amp; recommendations</li><li>AI-assisted production</li>
</ul>
<h3 style="margin-top:36px">My toolkit</h3>
<ul class="about-list" aria-label="Marketing toolkit by discipline">
<li><strong>Analytics &amp; reporting</strong><br>GA4 · Google Search Console · Looker Studio</li>
<li><strong>Paid advertising</strong><br>Google Ads · Meta Ads Manager</li>
<li><strong>Email &amp; CRM</strong><br>Drip · HubSpot</li>
<li><strong>Websites</strong><br>CMS builds · WordPress · HTML/CSS</li>
<li><strong>Creative</strong><br>Canva · Adobe Photoshop · Adobe Premiere Pro · CapCut · Figma</li>
<li><strong>Social &amp; workflow</strong><br>Sprout Social · Buffer · Monday.com</li>
</ul>
"""

HOME_CAPABILITIES = [
    {"file": "website-redesigns.html", "title": "Website Design & Builds", "scope": "CMS · Desktop + mobile",
     "description": "A website built from scratch, plus homepage, product, installation and blog redesigns. Explore six before-and-after comparisons and mobile examples.", "action": "Explore website work"},
    {"file": "email-marketing.html", "title": "Email Marketing", "scope": "Drip · Creative + copy",
     "description": "Seasonal campaigns, promotional creative and email messaging, with examples of how I connect the offer, imagery and call to action.", "action": "Explore email campaigns"},
    {"file": "paid-advertising.html", "title": "Paid Advertising", "scope": "Google Ads · Meta Ads · Growth planning",
     "description": "Account audits, campaign recommendations and a paid growth plan, with proposed actions clearly separated from implemented work.", "action": "Explore paid advertising"},
    {"file": "analytics-reporting.html", "title": "Analytics & Reporting", "scope": "GA4 · Search Console · Channel reporting",
     "description": "Performance analysis across web, search, social and email, translated into findings and practical next steps.", "action": "Explore analytics work"},
]

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
    "kpi_context": 'Instagram results · Sept 17, 2025 – Oct 26, 2026',
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
    "kpi_context": 'Instagram post counts · Sept 17, 2025 – Oct 26, 2026 · Publishing across 3 channels',
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
    "kpi_context": 'Instagram results · Sept 17, 2025 – Oct 26, 2026',
    "kpis": [("3,685", "Engagements"), ("526", "Saves"), ("365", "Shares")],
    "chips": ["Creator curation", "Community content", "RFQ education", "LinkedIn"],
    "cover_folder": "equipio", "cover": [("eq-car1-01", "Equipio carousel cover: “Renting gear, the smart way”"),
                                          ("eq-car2-01", "Equipio carousel cover: “How Equipio works — built on vendor trust”"),
                                          ("eq-tpl-01", "Equipio post: “Upload your RFQ. Get quotes. Fast.”")],
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
<li><strong>Template system:</strong> single-post formats for value props, tips and FAQs so original posts stay on-message between curated Reels.</li>
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
    "sets": [
        {"folder": "equipio", "title": "Renting gear, the smart way", "format": "Carousel · 6 slides",
         "desc": "The RFQ process told as a four-beat story: the problem, the first step, the magic, the win.",
         "slides": S("eq-car1", ["Cover: “Renting gear, the smart way” over a cinema camera rig",
             "“The problem: Need gear but don't want to chase quotes, call vendors, or email six times?”",
             "“The 1st step: Submit your gear list. Upload once. Just once.” over a laptop",
             "“The magic: Vendors quote you directly. Multiple offers. Transparent terms.”",
             "“The win: Pick your favorite. Book it. Done. No forms. No cold calls. Just gear.”",
             "End slide: “Your all-in-one RFQ platform for gear rentals” with equipio.com"])},
        {"folder": "equipio", "title": "How Equipio works — built on vendor trust", "format": "Carousel · 6 slides",
         "desc": "A trust-first version of the explainer, answering the producer's real question: can I trust who I'm renting from?",
         "slides": S("eq-car2", ["Cover: “How Equipio works — built on vendor trust” on a film set",
             "“The question: Can I trust who I'm renting from?”",
             "“Upload your list: Submit your RFQ. Get quotes directly from vetted, established vendors.”",
             "“Review real quotes: Compare quotes. Review vendors. Make the call.” over camera bodies",
             "“Book with confidence: The right gear from the right source. No mystery gear.”",
             "End slide: “Your all-in-one RFQ platform. Trusted vendors. Transparent terms.”"])},
        {"folder": "equipio", "title": "Single-post template system", "format": "Static posts · 7 shown",
         "desc": "Reusable single-image formats — value props, a pro tip and a producer FAQ — that keep the RFQ message consistent between curated Reels.",
         "slides": S("eq-tpl", ["“Upload your RFQ. Get quotes. Fast.” — one request, multiple vendors, compare side-by-side",
             "“We are here to solve a problem you forgot existed” — chasing gear quotes",
             "“Streamline your RFQ process with Equipio” — the platform on a laptop beside camera gear",
             "“New bids. New brands. New business.” — vendor-side message",
             "“You wouldn't list Google Ads as a pass-through. Equipio is the same — your sales engine, not your markup.”",
             "“Pro tip: Submit RFQ early to beat rental rush and get better rates.”",
             "Producer FAQ card: “Can I use my usual vendor?”"])},
    ],
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
    "kpi_context": 'Planned content program · Oct 28 – Nov 27, 2026',
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
              ("Tools", "CMS · Canva"), ("Performance data", "Not reported")],
    "card_title": "Making private aviation <em>pricing</em> clear.",
    "card_text": "Enterprise pricing landing pages built in the CMS, plus paid-social ad creative for LinkedIn and Instagram.",
    "kpi_context": 'Project deliverable · Enterprise pages built in the development CMS',
    "kpis": [("4", "Enterprise pricing pages")],
    "chips": ["Landing pages", "CMS", "Pricing tiers", "Ad creative"],
    "cover_folder": "levo", "cover": [("levo-story-01", "Levo story ad frame: “Your time.” over a private jet on a runway"),
                                       ("levo-ig-ad-01", "Levo Instagram ad: “Private Jet Charter. On Your Schedule.”"),
                                       ("levo-story-02", "Levo story ad frame: “Your schedule.” traveler in a jet cabin")],
    "cs": {
        "challenge": {"h": "A premium service needs a <em>clear</em> price story.",
            "body": """<p>Enterprise customers evaluating a private aviation platform need to understand what each tier includes and how to buy it. Those pages needed to exist as distinct, shareable URLs that sales conversations could point to.</p>"""},
        "strategy": {"h": "One page per tier, <em>one clear path.</em>",
            "body": """<ul><li>Give each Enterprise tier its own landing page and unique URL for customer-facing use.</li>
<li>Reuse proven page structures so the experience stays consistent with the rest of the site.</li>
<li>Support awareness with clean, on-brand ad creative sized for LinkedIn and Instagram.</li></ul>"""},
        "role": {"h": "Builder and <em>designer.</em>",
            "body": """<ul><li>Built four Enterprise pricing landing pages in the development CMS, starting from existing pages and adapting them to tiered pricing.</li>
<li>Designed paid-social ad concepts in Canva for LinkedIn, Instagram feed and Instagram Stories, plus a landing-page hero concept.</li></ul>"""},
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
    "sets": [
        {"folder": "levo", "title": "Instagram story sequence", "format": "Story ad · 3 frames", "status": "Ad concept", "ratio": "9/16",
         "desc": "A three-beat story built on the brand promise — your time, your schedule, your destination — ending on a single CTA.",
         "slides": S("levo-story", ["Story frame 1: “Your time.” over a private jet taxiing at sunset",
             "Story frame 2: “Your schedule.” a traveler looking out a jet window",
             "Story frame 3: “Your destination.” coastal landscape with a “Book now at Levo” button"])},
        {"folder": "levo", "title": "LinkedIn ads", "format": "LinkedIn feed ads", "status": "Ad concept", "ratio": "1200/627", "wide": True,
         "desc": "Two LinkedIn variants leading with a concrete route and a promise: instant quotes, vetted aircraft, no hidden fees.",
         "slides": [("levo-li-ad-01", "LinkedIn ad: “Private Jet NYC → Miami. Instant quotes. Vetted aircraft. No hidden fees.”"),
                    ("levo-li-ad-02", "LinkedIn ad variant: “Private Jet NYC → Miami” with a Get My Quote button")]},
        {"folder": "levo", "title": "Instagram feed ad", "format": "Instagram ad", "status": "Ad concept", "ratio": "1/1",
         "desc": "A square feed ad pairing an executive-travel moment with a single Book Now action.",
         "slides": [("levo-ig-ad-01", "Instagram ad: “Private Jet Charter. On Your Schedule.” with a Book Now button")]},
        {"folder": "levo", "title": "Landing page hero", "format": "Web design", "status": "Concept", "ratio": "16/10", "wide": True,
         "desc": "A hero section design pairing the headline with a single “Book flight” action.",
         "slides": [("levo-lp-01", "Landing page hero: “Private Jet Charter. On Your Schedule.” with a Book Flight button over a jet above clouds")]},
    ],
}

EMAIL_CS = {
    "slug": "email-marketing", "file": "email-marketing.html", "name": "Email Marketing",
    "kicker": "Capability · Email (Drip)",
    "meta": "Email marketing case study: Polina Gaydamachenko's Axe & Kindle email program in Drip — seasonal campaigns, seasonal header creative and historical email reporting.",
    "brand": {"bg": "#2a2118", "ink": "#f4ecdf", "accent": "#d9b36c", "accent_on_paper": "#8a5a1f"},
    "headline": "A weekly reason to <em>light a fire.</em>",
    "lede": "I plan, write, design and build Axe &amp; Kindle email campaigns in Drip, connecting seasonal firewood demand with relevant messages for homeowners and restaurant buyers.",
    "facts": [("Role", "Email marketer (end to end)"), ("Platform", "Drip"),
              ("Tools", "Drip · Canva · GA4"), ("Evidence", "Email creative + 2023–2025 reporting")],
    "card_title": "A weekly reason to <em>light a fire.</em>",
    "card_text": "Seasonal email campaigns planned, written and designed for Drip, with historical engagement and list-health reporting.",
    "kpis": [],
    "chips": ["Drip", "Campaign calendar", "Subject lines", "Email design"],
    "cover_folder": "ak-email", "cover": [("email-47", "Axe & Kindle email header: “Winter starts with the right firewood”"),
                                           ("email-42", "Axe & Kindle email header: “Halloween nights need firewood that lasts”"),
                                           ("email-36", "Axe & Kindle email header: “Perfectly smoked meats start with hickory firewood”")],
    "cs": {
        "challenge": {"h": "A seasonal product, a <em>year-round</em> list.",
            "body": """<p>Firewood demand spikes with the weather, but the email list doesn't take the summer off. The program needed a steady, recognizable cadence that stays relevant in every season — cook-outs, holidays, the first cold night — without wearing the list out.</p>"""},
        "strategy": {"h": "Timely moments, one clear <em>ask.</em>",
            "body": """<ul>
<li><strong>Calendar-driven subject lines</strong> tied to real moments: Labor Day fires, a Halloween fire-pit night, “October is one week away,” “How's the stack holding up?”</li>
<li><strong>Two audiences:</strong> homeowners, plus a restaurant angle (“Autumn service starts soon. Is your wood supply sorted?”).</li>
<li><strong>One CTA per email</strong> — shop or reorder kiln-dried firewood with free delivery.</li>
<li><strong>A recognizable look:</strong> a reusable header system so every send reads as Axe &amp; Kindle at a glance.</li>
</ul>"""},
        "role": {"h": "Every step, <em>every send.</em>",
            "body": """<ul><li>Plan the email calendar alongside the social calendar.</li>
<li>Write subject lines, preheaders and body copy.</li>
<li>Design headers and imagery in Canva for seasonal campaigns.</li>
<li>Build, schedule and send broadcasts in Drip; review results and list health.</li></ul>"""},
        "execution": {"h": "From calendar to <em>campaign.</em>",
            "body": """<ul>
<li><strong>Seasonal planning:</strong> connect email topics with holidays, cold-weather preparation and live-fire cooking.</li>
<li><strong>Creative production:</strong> write copy and design branded headers, then build and schedule broadcasts in Drip.</li>
<li><strong>Audience relevance:</strong> pair homeowner lifestyle messages with restaurant supply and reorder angles.</li>
<li><strong>Reporting:</strong> review sends, opens, clicks, unsubscribes and bounces to identify opportunities for the next campaign.</li>
</ul><p>The selected headers below show the creative work; the reporting slide provides a separate historical view of email performance.</p>"""},
        "results": {"h": "Read the results, <em>then prioritize.</em>",
            "body": """<p>The historical email analytics slide reports a 15% open rate and 0.41% click-through rate in 2023, compared with 10% and 0.29% in 2024. Over the same years, the reported unsubscribe rate declined from 0.33% to 0.13% and the bounce rate from 0.1% to 0.05%.</p>
<p>Lower unsubscribes and bounces sit alongside weaker opens and clicks: the opportunity is to improve message relevance and engagement. These are program-level observations, not proof that a particular design caused a change. No email-attributed revenue or conversion lift is claimed.</p>
<p class="small">Source: Email Analytics, slide 14 of my Axe &amp; Kindle + Every Window analytics presentation. The 2025 row is an interim snapshot from the 2025 review, not a full-year comparison. Historical figures are separate from the creative examples shown here.</p>"""},
        "takeaways": {"h": "What I'd carry <em>forward.</em>",
            "body": """<ol class="takeaways">
<li>Keep seasonal messaging specific to the customer's next use: a fireplace, a grill or a restaurant service.</li>
<li>Test subject lines and calls to action while monitoring clicks and list health together.</li>
<li>Prioritize segmentation, welcome and cart-recovery flows as future opportunities; measure their effect before claiming results.</li>
</ol>"""},
    },
    "sets": [
        {"folder": "ak-email", "title": "Email header library", "format": "Email headers · 12 examples", "square": True, "gallery_take": 0,
         "desc": "A year of seasonal and holiday headers designed for Drip campaigns.",
         "slides": [("email-01", "Email header: “Celebrate National Firewood Day — stock up on the best firewood!”"),
                    ("email-05", "Email header: “Winter is here — stock up on premium firewood”"),
                    ("email-09", "Email header: “Happy Thanksgiving from Axe & Kindle!”"),
                    ("email-12", "Email header: Valentine's Day — “Turn up the romance”"),
                    ("email-19", "Email header: “Maximize your firewood's performance with premium kiln-dried wood!”"),
                    ("email-24", "Email header: “Elevate every fire: why chefs and homeowners choose kiln-dried wood”"),
                    ("email-30", "Email header: “See why kitchens and campfires alike rely on Axe & Kindle”"),
                    ("email-36", "Email header: “Perfectly smoked meats start with hickory firewood”"),
                    ("email-42", "Email header: “Halloween nights need firewood that lasts”"),
                    ("email-47", "Email header: “Winter starts with the right firewood”"),
                    ("email-52", "Email header: “Oak. Hickory. Mixed hardwood… here's how to choose.”"),
                    ("email-64", "Email header: “There's a flavor your grill has been missing”")]},
        {"folder": "analytics", "title": "Email analytics, 2023–2025", "format": "Reporting slide", "ratio": "16/9", "wide": True, "gallery_take": 0,
         "desc": "From my analytics presentation: sends, open rate, click rate, unsubscribes and bounces by year.",
         "slides": [("deck-14", "Email analytics slide: sends, open rate, CTR, unsubscribe and bounce rate for 2023, 2024 and 2025")]},
    ],
}

ANALYTICS_CS = {
    "slug": "analytics-reporting", "file": "analytics-reporting.html", "name": "Analytics & Reporting",
    "kicker": "Capability · GA4 · Search Console · Social",
    "meta": "Analytics case study: Polina Gaydamachenko's cross-channel analysis for Axe & Kindle and Every Window using GA4, Google Search Console, Instagram Insights and Drip, with strategic recommendations.",
    "brand": {"bg": "#1f2e24", "ink": "#eef0e4", "accent": "#d9e58e", "accent_on_paper": "#4d6b22"},
    "headline": "Turning four data sources into <em>one story.</em>",
    "lede": "I built a 32-slide analytics review for Axe &amp; Kindle and Every Window — GA4, Google Search Console, Instagram Insights and Drip — and turned it into channel priorities for 2025.",
    "facts": [("Role", "Analyst &amp; author"), ("Sources", "GA4 · Search Console · Instagram Insights · Drip"),
              ("Deliverable", "32-slide deck + roadmap docs"), ("Date", "March–April 2025")],
    "card_title": "Turning four data sources into <em>one story.</em>",
    "card_text": "A cross-channel review of traffic, engagement, search, social and email for two brands — ending in clear, prioritized recommendations.",
    "kpis": [("4", "Data sources"), ("2", "Brands"), ("32", "Slides")],
    "chips": ["GA4", "Search Console", "Instagram Insights", "Channel strategy"],
    "cover_wide": True, "cover_folder": "analytics", "cover": [("deck-03", "Analytics slide: Axe & Kindle social media performance"),
                                            ("deck-15", "Analytics slide: engagement rate trends by channel"),
                                            ("deck-17", "Analytics slide: strategic recommendations for 2025")],
    "cs": {
        "challenge": {"h": "Lots of data, <em>no single picture.</em>",
            "body": """<p>Traffic, social, search and email data for Axe &amp; Kindle and Every Window lived in different tools. Leadership needed one view of what had changed since 2022, which channels were pulling their weight, and where to focus next.</p>"""},
        "strategy": {"h": "Same framework for <em>both brands.</em>",
            "body": """<ul>
<li><strong>One structure, two brands:</strong> audience → social performance → GA4 acquisition → organic search → Search Console → email → engagement → channel efficiency → recommendations.</li>
<li><strong>Quality over volume:</strong> look at engagement rate and revenue per channel, not just sessions.</li>
<li><strong>Call out measurement gaps:</strong> explain what GA4 can misattribute (untagged ads, dark social) so decisions aren't built on bad data.</li>
</ul>"""},
        "role": {"h": "Pulled it, analyzed it, <em>presented it.</em>",
            "body": """<ul><li>Pulled and reconciled data from GA4, Google Search Console, Instagram Insights and Drip for 2022–2025.</li>
<li>Designed the 32-slide presentation in Canva and wrote every takeaway.</li>
<li>Wrote supporting strategy documents, including a quarter-by-quarter roadmap.</li></ul>"""},
        "execution": {"h": "Findings that <em>drive decisions.</em>",
            "body": """<ul>
<li><strong>Engagement quality rose across channels:</strong> for Axe &amp; Kindle, organic engagement rate went from 20.8% to 47.2% and paid from 10.9% to 69.8% between 2022 and 2025.</li>
<li><strong>Channel roles became clear:</strong> organic search was the most efficient long-term channel, paid search a high-volume driver needing tighter ROI tracking, and email small but with best-in-class engagement.</li>
<li><strong>Social views were ad-assisted:</strong> Instagram Insights showed most recent views came from ads (79% for Axe &amp; Kindle, 98% for Every Window) — an honest read on what organic content was and wasn't doing.</li>
</ul>"""},
        "results": {"h": "What the review <em>showed.</em>",
            "body": """<div class="metric-grid"><div><b>~13,000</b><span>Axe &amp; Kindle Instagram followers gained (ad-assisted)</span></div><div><b>~1,200</b><span>Every Window followers gained (ad-assisted)</span></div><div><b>123,607</b><span>A&amp;K accounts reached, 90 days (+15.6%)</span></div><div><b>106,351</b><span>EW accounts reached, 90 days</span></div></div>
<p>Follower counts are approximate gains since I started managing each account, as reported in the deck; The deck attributes most views in that window to paid ads, so I present them as ad-assisted growth rather than organic. Company revenue figures from GA4 are part of the original analysis but are intentionally left off this public page.</p>
<p class="small">Source: my “AK &amp; EW Analytics Presentation, 2022–Present” (Canva), using GA4, Google Search Console, Instagram Insights and Drip data; prepared March–April 2025.</p>"""},
        "takeaways": {"h": "What I <em>recommended.</em>",
            "body": """<ol class="takeaways">
<li>Rebuild organic search: target top 2023 keywords, fix technical SEO, and strengthen category and product pages.</li>
<li>Scale email: grow the list, segment it, and add automations (welcome, cart and browse abandonment, win-back).</li>
<li>Measure paid search ROI: audit ROAS, trim low performers, shift to branded and bottom-funnel audiences.</li>
<li>Improve conversion paths: scroll-depth tracking, clearer CTAs, and user testing on key pages.</li>
</ol>"""},
    },
    "sets": [
        {"folder": "analytics", "title": "Axe & Kindle review", "format": "Presentation · 8 of 17 slides", "ratio": "16/9", "wide": True,
         "desc": "Audience, social performance, search, email, engagement trends, channel efficiency and recommendations. Revenue slides omitted.",
         "slides": [("deck-01", "Title slide: Axe & Kindle + Every Window Analytics, 2022–Present"),
                    ("deck-02", "Axe & Kindle social media audience: age, location and gender breakdown"),
                    ("deck-03", "Axe & Kindle social media performance: new followers, views, accounts reached and interactions"),
                    ("deck-13", "Google Search Console performance charts for Axe & Kindle"),
                    ("deck-14", "Email analytics: sends, open rate, click rate, unsubscribes and bounces by year"),
                    ("deck-15", "Engagement rate trends by channel, 2022–2025"),
                    ("deck-16", "Channel efficiency takeaways"),
                    ("deck-17", "Strategic recommendations for 2025")]},
        {"folder": "analytics", "title": "Every Window review", "format": "Presentation · 5 of 15 slides", "ratio": "16/9", "wide": True,
         "desc": "The same framework applied to Every Window, ending in a detailed 2025 roadmap. Revenue slides omitted.",
         "slides": [("deck-18", "Every Window social media audience: age, location and gender"),
                    ("deck-19", "Every Window social media performance since I started managing the account"),
                    ("deck-30", "Every Window engagement rate trends by channel"),
                    ("deck-31", "Every Window channel efficiency takeaways"),
                    ("deck-32", "Every Window strategic recommendations for 2025: organic, paid, email and conversion paths")]},
    ],
}

PAID_ADS_CS = {
    "slug": "paid-advertising", "file": "paid-advertising.html", "name": "Paid Advertising",
    "kicker": "Capability · Paid media analysis & strategy",
    "meta": "Paid advertising case study: Polina Gaydamachenko's Google Ads audits, campaign analysis for Axe & Kindle and Every Window. Recommendations distinguished from measured results.",
    "brand": {"bg": "#182d40", "ink": "#eff4f7", "accent": "#a8d8dd", "accent_on_paper": "#2c6170"},
    "headline": "Better decisions <em>before</em> more spend.",
    "lede": "I reviewed paid-search performance for Axe &amp; Kindle and Every Window. The work connects measurement, search intent, landing pages and campaign priorities.",
    "facts": [("Role", "Audit, analysis &amp; recommendations"),
              ("Channels", "Google Ads"),
              ("Inputs", "Google Ads · GA4 reports"),
              ("Period", "October 2026")],
    "cs": {
        "challenge": {"h": "A performance report needs <em>context.</em>",
            "body": """<p>These brands had different paid-media questions. Axe &amp; Kindle needed a review of account measurement and campaign efficiency. Every Window needed to connect campaign reports with its store and configurator funnel.</p><p>The shared challenge: decide what to fix or test before committing more media spend.</p>"""},
        "strategy": {"h": "Measurement, intent, <em>then investment.</em>",
            "body": """<ul><li><strong>Check the signal:</strong> review conversion definitions and value reporting before drawing conclusions about efficiency.</li><li><strong>Separate intent:</strong> distinguish branded, product, research and business-buyer searches.</li><li><strong>Follow the click:</strong> connect the ad message to a relevant product, configurator, quote or demo path.</li><li><strong>Make recommendations testable:</strong> specify the next action, required access and KPI for each priority.</li></ul>"""},
        "role": {"h": "Account review &amp; <em>reporting analysis.</em>",
            "body": """<ul><li><strong>Axe &amp; Kindle:</strong> conducted a view-only Google Ads audit covering tracking, campaign allocation, search terms, copy, landing pages and a proposed B2B lead campaign.</li><li><strong>Every Window:</strong> analyzed the GA4/Data Studio sales report and monthly performance sheet. I did not have direct Google Ads account access; search terms, bidding settings and conversion configuration remained items to verify.</li></ul>"""},
        "execution": {"h": "Two brands, <em>different next steps.</em>",
            "body": """<ul><li><strong>Axe &amp; Kindle:</strong> prioritized conversion-value validation and purchase/lead tracking, then recommended reviewing campaign allocation, search intent and product-page clarity.</li><li><strong>Every Window:</strong> flagged inconsistent conversion counts across reporting systems, recommended investigating branded-search efficiency and identified quote tracking and cart recovery as opportunities.</li></ul>"""},
        "results": {"h": "Delivered recommendations. <em>Impact to be measured.</em>",
            "body": """<p>The deliverables were an account audit and a reporting-based campaign analysis. Each identified priorities, dependencies and measures for evaluating the next step.</p><div class="callout"><b>Status at the time of these documents:</b> the Axe &amp; Kindle review was view-only, Every Window recommendations required account access and approval. These documents do not establish implementation or post-change results. No revenue lift, ROAS improvement, cost reduction or lead growth is claimed.</div><p class="small">Sources: my Axe &amp; Kindle Google Ads Audit (Oct 26, 2026; account period Sep 26–Oct 25); Every Window Google Ads Analysis (Oct 28, 2026; campaign period Sep 28–Oct 27, with separate funnel and monthly comparison periods). Historical findings describe those reviews, not the current state of the accounts or websites.</p>"""},
        "takeaways": {"h": "What I would <em>validate next.</em>",
            "body": """<ol class="takeaways"><li>Confirm that purchase, quote and lead events mean the same thing across the reports used to make decisions.</li><li>Review search terms and landing-page intent before treating a campaign label as evidence of buyer quality.</li><li>Use qualified leads and completed purchases to evaluate a test; do not substitute clicks for business outcomes.</li><li>Record a baseline, implement approved changes and compare equivalent periods before attributing an improvement.</li></ol>"""},
    },
    "work_heading": "From finding to <em>next action.</em>",
    "work_intro": "Portfolio summaries of my October 2026 recommendations. These are examples of analysis and planning, not a record of campaign improvements.",
    "work_examples": [
        {"id": "ak-measurement", "title": "Axe & Kindle · Validate the signal",
         "source": "Google Ads account audit · View-only · Oct 26, 2026",
         "finding": "Conversion-value adjustments and purchase-tracking warnings made reported efficiency a priority to validate. Business inquiries also needed a defined lead conversion.",
         "action": "Confirm whether value adjustments are intentional, review purchase event data and add contact-form lead measurement before testing a business-buyer campaign.",
         "measure": "Validated purchase values and event counts; successful test lead submissions; purchase efficiency and cost per qualified inquiry after approved changes."},
        {"id": "ew-intent", "title": "Every Window · Connect intent to the funnel",
         "source": "GA4/Data Studio report + monthly comparison sheet · Oct 28, 2026",
         "finding": "Campaign efficiency varied, while Google Ads, GA4 and store reports showed different conversion counts. Quote and configurator activity needed clearer measurement.",
         "action": "Request account access to inspect branded search, search terms and conversion settings; review lower-efficiency campaigns; connect quote, call and cart-recovery paths to reporting.",
         "measure": "Reconciled conversion definitions; branded CPC and conversion efficiency; qualified quotes and calls; cart-to-order rate. Account-level recommendations remain subject to verification."},
    ],
    "sets": [],
}

WEB_CS = {
    "slug": "website-redesigns", "file": "website-redesigns.html", "name": "Website Design & Builds",
    "kicker": "Capability · Website builds & redesigns",
    "meta": "Website portfolio by Polina Gaydamachenko: NxtDib built from scratch, plus before-and-after redesigns of homepages, product pages, an installation page and a blog page for Every Window and Axe & Kindle.",
    "brand": {"bg": "#173b3c", "ink": "#f3f0e5", "accent": "#d3cc96", "accent_on_paper": "#5b672d"},
    "headline": "Built for the <em>next step.</em>",
    "lede": "I built NxtDib’s website from scratch and redesigned pages across the Every Window and Axe &amp; Kindle sites: homepages, product pages, an installation page and a blog page. This selection pairs a complete website build with before-and-after examples of content hierarchy, visual presentation and customer actions.",
    "facts": [("Role", "Website build &amp; page redesigns"), ("Examples", "NxtDib · Every Window · Axe &amp; Kindle"),
              ("Tools", "CMS page builder"),
              ("Focus", "Content hierarchy · Visual consistency · Calls to action")],
    "cover_wide": True, "cover_folder": "web-redesigns",
    "cover": [("ew-current-preview", "Every Window current homepage desktop preview"),
              ("ak-current-preview", "Axe & Kindle current homepage desktop preview")],
    "head_extra": '<link rel="stylesheet" href="assets/css/web-redesigns.css?v=2026-10-29-mobile-2">\n',
    "cs": {
        "challenge": {"h": "Useful content needs a <em>clear hierarchy.</em>",
            "body": """<p>Each page had to introduce the brand, explain the offer and help visitors choose their next step. Every Window combines window selection, installation information and buyer education. Axe &amp; Kindle combines firewood shopping, live-fire cooking, delivery information, trust signals and a content library.</p><p>The earlier captures already contain substantial content. My redesign work focused on how that content is presented and organized.</p>"""},
        "strategy": {"h": "Keep the brand. Clarify the <em>journey.</em>",
            "body": """<ul><li><strong>Lead with the offer:</strong> use the opening section to establish the brand and a visible action.</li><li><strong>Group related decisions:</strong> bring product or style selection, installation guidance and supporting information into recognizable sections.</li><li><strong>Make trust easier to find:</strong> give customer reviews and supporting content a defined place in the page.</li><li><strong>Carry the visual system through:</strong> apply consistent brand colors, section treatments and footer presentation, and reuse them across page types.</li></ul>"""},
        "role": {"h": "The redesign, <em>shown in context.</em>",
            "body": """<p>I built <a href="https://www.nxtdib.com/" target="_blank" rel="noopener">nxtdib.com</a> from scratch as part of my multi-brand marketing work. I also redesigned the Every Window homepage, a product page and the installation page, and the Axe &amp; Kindle homepage, product pages and blog page. For Axe &amp; Kindle I redesigned every product page; the oak firewood page below is one example. My contribution covered page design, section hierarchy, imagery placement and calls to action, using the CMS page builder to assemble and refine pages. The supplied captures document these design decisions.</p><p>I also helped with the <a href="https://levo.aero/" target="_blank" rel="noopener">Levo Aero</a> website redesign.</p>"""},
        "execution": {"h": "Two brands, <em>two visual systems.</em>",
            "body": """<p><strong>Every Window:</strong> reorganized the installation introduction, changed the installation video from a full-width block to a text-and-video section, brought customer reviews higher into the homepage, and turned the style section into a visual selection grid. The product and installation pages follow the same teal, cream and olive-gold system, with image-led sections and clear calls to action. The redesigned footer uses a stronger deep-teal treatment.</p><p><strong>Axe &amp; Kindle:</strong> reduced the homepage partner-logo display, changed the customer-review grid into horizontal cards, rebuilt the product-page template with size selection and image-led supporting sections, and gave the blog an introduction, category tabs and a card layout. The existing signup and contact sections remain part of the homepage.</p>"""},
        "results": {"h": "The design change is <em>visible.</em>",
            "body": """<p>The NxtDib deliverable was a website built from scratch. For Every Window and Axe &amp; Kindle, the supplied before-and-after captures of homepages, product pages, an installation page and a blog page document changes in layout, content hierarchy and visual presentation.</p><p>These captures do not establish a change in conversion rate, revenue, page speed, accessibility or user satisfaction. No performance improvement is claimed without a comparable measurement period.</p><p class="small">Sources: my confirmed NxtDib website-build experience, plus the full-page before-and-after PDF captures supplied for each page shown below. The captures describe the supplied versions; the Every Window current-site detail is dated October 29, 2026. Mobile homepage PDFs are also included for both brands; the captures demonstrate the layouts shown, rather than cross-device testing results.</p>"""},
        "takeaways": {"h": "Design choices worth <em>testing.</em>",
            "body": """<ol class="takeaways"><li>A homepage can explain the offer, provide trust signals and guide a purchase without giving every section equal visual weight.</li><li>Buyer education works best when it supports a visible next action, such as selecting a style or size, exploring products or requesting help.</li><li>Before-and-after images demonstrate design decisions. To evaluate business impact, I would compare product/configurator clicks, form completions and purchases over equivalent periods.</li></ol>"""},
    },
    "work_feature": '<section class="set" aria-labelledby="nxtdib-build"><div class="set-head"><div><div class="badges"><span class="badge orig">Built from scratch</span></div><h3 id="nxtdib-build">NxtDib · A website built from scratch</h3><p>B2B wholesale beverage marketplace</p></div></div><div class="callout"><p><b>I built nxtdib.com from scratch.</b> This project demonstrates my website-building experience alongside the redesigns below.</p><p><a href="https://www.nxtdib.com/" target="_blank" rel="noopener">Visit the NxtDib website ↗</a></p></div></section>',
    "work_heading": "Website builds. <em>Thoughtful redesigns.</em>",
    "work_intro": "Explore the before-and-after captures and selected design details. Every pair is a full-page PDF capture, shown here as a scrollable preview. Open a PDF to zoom into the full-quality capture, or download it. Mobile homepage examples sit alongside the desktop comparisons for both brands. All source files are available to download.",
    "comparisons": [
        {"id": "every-window-redesign", "mobile": {'pdf': 'assets/docs/pdf/ew-home-mobile.pdf', 'preview': 'assets/img/web-redesigns/ew-home-mobile-preview.webp', 'description': 'The mobile capture shows window options, installation guidance and supporting content arranged for a narrow screen, carrying the deep-teal and cream visual system through the page.'}, "role": 'Homepage layout, section hierarchy, visual styling and placement of installation guidance, reviews and window styles.', "why": 'Visitors need to understand both the window offer and the installation option before choosing a next step. I grouped related information and gave product selection, guidance and customer feedback distinct places on the page.', "name": "Every Window", "heading": "Every Window · Homepage", "page": "homepage", "prefix": "ew-home",
         "detail": {"path": "assets/img/web-redesigns/ew-current-detail.png", "title": "A visual path to choosing a window style", "desc": "The current style grid groups six window types with labeled imagery and a Start Designing action."},
         "summary": "A more structured introduction to windows, installation and buyer education, using deep teal, cream and olive-gold accents.",
         "changes": [("Installation explanation", "The redesigned page pairs installation copy and a CTA with the video instead of using a full-width video block."),
                     ("Trust and selection", "Customer reviews appear higher on the page, and the style section becomes a visual grid of window options."),
                     ("Content and footer", "Recent posts, educational videos and the benefits section receive more defined layouts; the footer adopts a cohesive deep-teal treatment.")]},
        {"id": "every-window-product-redesign", "role": 'Single-hung product-page layout, product education, image-and-text sections and links to other window styles.', "why": 'A shopper may arrive knowing little about window types. I organized the page around understanding single-hung windows, assessing their benefits and comparing other styles before starting a design.', "name": "Every Window", "heading": "Every Window · Product page", "badge": "Product page redesign", "page": "single-hung product page", "prefix": "ew-product",
         "summary": "A category page that explains the product, answers common questions and routes visitors to the next style.",
         "changes": [("Opening section", "The page opens with a “What is a single-hung window?” panel beside a product image, followed by a contractor callout band."),
                     ("Alternating sections", "Benefits and “why choose” content alternate text with photography instead of running as long text blocks."),
                     ("Browse other styles", "Other window styles appear as image tiles, giving visitors a visual path to the next product page.")]},
        {"id": "every-window-installation-redesign", "role": 'Installation-page layout, process presentation, service checklist, benefit cards and CTA placement.', "why": 'Installation introduces questions about measurements, responsibilities and what the service includes. I broke that information into a visible sequence and focused sections to support the decision to request installation.', "name": "Every Window", "heading": "Every Window · Installation page", "badge": "Installation page redesign", "page": "installation page", "prefix": "ew-installation",
         "summary": "A page that explains what installation includes, shows the process and gives visitors a clear action at several points.",
         "changes": [("Process", "The three steps (place your order, confirm measurements, install) are shown as image cards next to an installation video card."),
                     ("What’s included", "The installation checklist moves from a dark full-width list into a titled card, organized under Replacement and New Construction."),
                     ("Reasons and CTA", "Four benefit cards and a closing “Ready for Professional Installation?” banner replace the earlier icon list and repeated buttons.")]},
        {"id": "axe-and-kindle-redesign", "mobile": {'pdf': 'assets/docs/pdf/ak-home-mobile.pdf', 'preview': 'assets/img/web-redesigns/ak-home-mobile-preview.webp', 'description': 'The mobile capture stacks product sections, customer reviews and supporting content in a single column, carrying the firewood brand’s colors and imagery through to the contact form and footer.'}, "role": 'Homepage layout, product presentation, partner-logo treatment and customer-review presentation.', "why": 'The homepage needs to balance product browsing with reasons to trust the brand. I made partner logos and reviews more compact so supporting proof fits alongside the shopping journey.', "name": "Axe & Kindle", "heading": "Axe & Kindle · Homepage", "page": "homepage", "prefix": "ak-home",
         "detail": {"path": "assets/img/web-redesigns/ak-review-pdf-detail.jpg", "badge": "Detail from the supplied after PDF", "title": "Customer reviews in a horizontal card layout", "desc": "The redesigned page presents customer feedback in a horizontal row with navigation controls, replacing the earlier grid."},
         "summary": "A more focused premium-firewood homepage with a more compact presentation of partner logos and customer reviews.",
         "changes": [("Partner proof", "The large collection of partner logos becomes a smaller, selected display."),
                     ("Customer reviews", "The earlier multi-row review grid becomes a horizontal row of cards with previous/next controls."),
                     ("Product browsing", "Oak, hickory, mixed hardwood and pizza-cut wood keep the same order, with a cleaner product-and-size presentation.")]},
        {"id": "axe-and-kindle-product-redesign", "role": 'Product-page design across every Axe & Kindle product, including purchase-area hierarchy, size navigation and supporting content. Oak firewood is the example shown.', "why": 'Firewood buyers need to understand the quantity, specifications and delivery details before ordering. I grouped the purchase information and gave size selection and supporting explanations clear sections within a consistent product-page design.', "name": "Axe & Kindle", "heading": "Axe & Kindle · Oak firewood product page", "badge": "Product page redesign", "page": "oak firewood product page", "prefix": "ak-product",
         "summary": "One example of the product-page template I redesigned for every Axe & Kindle product. The before and after captures show different oak size variants (face cord and 4-stack).",
         "changes": [("Purchase area", "Price, free-shipping note and add-to-cart sit beside the product gallery, with a “Why oak 4-stack?” summary and a “What’s included” grid."),
                     ("Choosing a size", "A “Shop other sizes” row lets visitors move between single stack, double stack and box."),
                     ("Supporting content", "Specifications, kiln-dried vs. seasoned, process, delivery and cooking sections each get their own image-led block.")]},
        {"id": "axe-and-kindle-blog-redesign", "role": 'Blog-index layout, introductory copy presentation, category navigation and article-card styling.', "why": 'Readers come for different reasons, from cooking advice to home-fireplace guidance. I added a clearer introduction and category navigation, with a consistent card layout to make relevant articles easier to scan.', "name": "Axe & Kindle", "heading": "Axe & Kindle · Blog page", "badge": "Blog page redesign", "page": "blog page", "prefix": "ak-blog",
         "summary": "A blog index that introduces the content and lets visitors scan guides, recipes and tips.",
         "changes": [("Introduction and filters", "A short intro line and category tabs (All, Cooking, Guides, Fireplaces & Fire Pits, Hospitality, Home & Lifestyle) sit above the posts."),
                     ("Post cards", "Posts appear as rounded cards with larger imagery and centered titles instead of bordered boxes."),
                     ("Page header", "The solid green banner is replaced by a quieter heading, so the posts start higher on the page.")]},
    ],
    "sets": [],
}

# Keep brand navigation, homepage cards and gallery stable. Capability pages
# are reached from the homepage analytics section and built with the same template.
# Levo source content and assets are retained for later restoration.
PROJECTS = [AK, NX, EQ, EW]
# Retain the published capability navigation while making the new study discoverable.
ANALYTICS_CS["next_case"] = "email-marketing"
PAID_ADS_CS["next_case"] = "email-marketing"
CAPABILITIES = [EMAIL_CS, ANALYTICS_CS, PAID_ADS_CS, WEB_CS]
CASE_STUDIES = PROJECTS + CAPABILITIES
