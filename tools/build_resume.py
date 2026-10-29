#!/usr/bin/env python3
"""Rebuild the portfolio resume: python3 tools/build_resume.py (requires reportlab)."""
from pathlib import Path
import os
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.pagesizes import letter

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / 'assets/docs/Polina_Gaydamachenko_Resume.pdf'
# Embed fonts when available; pass RESUME_FONT_DIR on other machines.
font_dir = Path(os.environ.get('RESUME_FONT_DIR',
    str(Path(os.environ.get('CODEX_PRIMARY_RUNTIME_ROOT', '/opt/codex/runtimes/codex-primary-runtime')) /
        'dependencies/native/libreoffice-headless/libreoffice/share/fonts/truetype')))
if (font_dir / 'LiberationSans-Regular.ttf').exists():
    pdfmetrics.registerFont(TTFont('ResumeSans', str(font_dir / 'LiberationSans-Regular.ttf')))
    pdfmetrics.registerFont(TTFont('ResumeSans-Bold', str(font_dir / 'LiberationSans-Bold.ttf')))
    pdfmetrics.registerFontFamily('ResumeSans', normal='ResumeSans', bold='ResumeSans-Bold')
    FONT, BOLD = 'ResumeSans', 'ResumeSans-Bold'
else:
    FONT, BOLD = 'Helvetica', 'Helvetica-Bold'
INK = colors.HexColor('#24333b')
ACCENT = colors.HexColor('#174957')
STYLE = ParagraphStyle('body', fontName=FONT, fontSize=9.3, leading=10.6,
                       textColor=INK, spaceAfter=1)
BULLET = ParagraphStyle('bullet', parent=STYLE, leftIndent=9, firstLineIndent=-7, spaceAfter=1)
SECTION = ParagraphStyle('section', parent=STYLE, fontName=BOLD, fontSize=9.8,
                        leading=12, textColor=ACCENT, spaceBefore=5, spaceAfter=2, keepWithNext=True)
ROLE = ParagraphStyle('role', parent=STYLE, fontName=BOLD, spaceBefore=3,
                     spaceAfter=2, keepWithNext=True)
NAME = ParagraphStyle('name', parent=STYLE, fontName=BOLD, fontSize=20,
                     leading=24, textColor=ACCENT, alignment=TA_CENTER, spaceAfter=4)
TITLE = ParagraphStyle('title', parent=STYLE, fontName=BOLD, fontSize=9.1,
                      leading=12, alignment=TA_CENTER, spaceAfter=4)
CONTACT = ParagraphStyle('contact', parent=STYLE, alignment=TA_CENTER, fontSize=9, leading=12)


def link(url, label):
    return f'<a href="{url}" color="#174957">{label}</a>'


def build():
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    story = []
    def para(text, style=STYLE): story.append(Paragraph(text, style))
    def section(text): para(text, SECTION)
    def bullet(text): para('• ' + text, BULLET)
    para('POLINA GAYDAMACHENKO', NAME)
    para('MULTI-BRAND MARKETING MANAGER | DIGITAL &amp; SOCIAL MEDIA STRATEGY', TITLE)
    para('Brentwood, TN | ' + link('tel:+16158300088', '(615) 830-0088') + ' | ' +
         link('mailto:polinayg99@gmail.com', 'polinayg99@gmail.com') + ' | ' +
         link('https://www.linkedin.com/in/polina-gaydamachenko/', 'LinkedIn') + ' | ' +
         link('https://polinayg.github.io/marketing-portfolio/', 'Portfolio'), CONTACT)

    section('PROFESSIONAL PROFILE')
    para('Digital marketing professional with 4+ years of experience leading multi-channel initiatives across e-commerce, B2B, technology, and marketplace brands. Combines social media strategy, UGC and short-form video production, paid advertising, email automation, SEO, website optimization, and analytics. Experienced managing campaigns from concept through launch, collaborating with developers and stakeholders, and translating performance insights into actionable improvements.')

    section('CORE SKILLS')
    para('Social Media Strategy &amp; Community Management | Content Calendars &amp; Creative Direction | UGC &amp; Short-Form Video | Meta Ads &amp; Google Ads | Email Marketing &amp; Automation | SEO &amp; Website Optimization | GA4 &amp; Reporting | AI-Assisted Content &amp; Prompt Engineering | AI Workflow Automation')

    section('PROFESSIONAL EXPERIENCE')
    para('NXT COMPANIES | Franklin, TN', ROLE)
    para('<b>Multi-Brand Marketing Manager</b> | Jun 2026-Present', ROLE)
    bullet('Lead integrated marketing execution for five brands - Axe &amp; Kindle, Every Window, NxtDib, Levo Aero, and Equipio - serving distinct consumer, wholesale, and technology audiences.')
    bullet('Own cross-channel campaigns from positioning, briefs, content calendars, and creative production through landing pages, email deployment, stakeholder approvals, and launch QA.')
    bullet('Develop social content, UGC-style assets, graphics, short-form video, and audience-specific messaging to support awareness, engagement, and lead generation.')
    bullet('Plan and evaluate Meta and Google Ads initiatives; use GA4, Looker Studio, and platform data to identify improvements in targeting, creative, traffic quality, and conversion paths.')
    bullet('Partner with developers and leadership on website UX, SEO content, product launches, CMS updates, and conversion-focused calls to action; coordinate dependencies in Monday.com.')
    para('<b>Digital Marketing Coordinator</b> | May 2023-May 2026', ROLE)
    bullet('Executed social media, email, paid media, and website initiatives across multiple brands, adapting channel strategies and creative to different customer segments.')
    bullet('Built and deployed promotional and segmented email campaigns using Drip and HubSpot, coordinating copy, HTML layouts, assets, timing, and audience targeting.')
    bullet('Maintained SEO-focused website content and landing pages; monitored acquisition and engagement trends and prepared performance reporting and optimization recommendations.')
    para('OMNICOMMANDER | Social Media Manager | Sep 2022-Apr 2023', ROLE)
    bullet('Created and scheduled platform-specific social media content for client accounts, maintaining brand voice and visual consistency.')
    bullet('Produced campaign creative, tracked engagement and KPIs, and collaborated with internal teams on content planning and performance improvements.')

    section('SELECTED BRAND EXPERIENCE')
    para(link('https://axeandkindle.com/', '<b>Axe &amp; Kindle:</b>') + ' E-commerce product launches, seasonal email campaigns, Meta advertising, SEO content, and social media content and campaigns.')
    para(link('https://everywindow.com/', '<b>Every Window:</b>') + ' Website UX and SEO, Google Ads analysis, lead-generation content, and homeowner/contractor messaging.')
    para(link('https://nxtdib.com/', '<b>NxtDib:</b>') + ' B2B buyer-focused social campaigns and creative direction for a wholesale beverage marketplace.')
    para(link('https://levo.aero/', '<b>Levo Aero</b>') + ' &amp; ' + link('https://equipio.com/', '<b>Equipio:</b>') + ' Landing-page messaging, campaign planning, and content for aviation and equipment marketplaces.')

    section('TOOLS &amp; PLATFORMS')
    para('Google Ads, Meta Ads Manager, GA4, Looker Studio, Google Search Console, Hotjar, Mixpanel, Drip, HubSpot, Adobe Photoshop, Premiere Pro, Final Cut Pro, Canva, Figma, WordPress, HTML/CSS, Monday.com, Sprout Social, Buffer, Meta Business Suite, Shopify, ChatGPT, Claude')

    section('EDUCATION &amp; CERTIFICATIONS')
    para('<b>University of Tennessee at Chattanooga</b> | Bachelor of Science (B.S.), Business Administration and Management | Aug 2019-Dec 2022')
    para('<b>Vanderbilt University</b> | Certificate, Digital Marketing Bootcamp | Dec 2021-Apr 2022 | Grade: A+<br/>18-week intensive program in digital marketing strategy, campaign development and optimization, digital advertising, analytics, and reporting.')
    para('<b>Google (2026)</b> | Stay Ahead of the AI Curve; Introduction to AI; Discover the Art of Prompting; Maximize Productivity With AI Tools; Use AI Responsibly')
    para('<b>Advancing Women in Tech / Anthropic (2026)</b> | AI Fundamentals with Claude; AI Collaboration with Claude; AI Automation with Claude')
    para('<b>Coursera (2026)</b> | AI Enablement I; AI Productivity II')

    doc = SimpleDocTemplate(str(OUTPUT), pagesize=letter, rightMargin=34, leftMargin=34,
                            topMargin=28, bottomMargin=27, title='Polina Gaydamachenko | Multi-Brand Marketing Manager',
                            author='Polina Gaydamachenko')
    doc.build(story)
    print(OUTPUT)


if __name__ == '__main__':
    build()
