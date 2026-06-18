#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
The Happy Days — statische sitegenerator.
Bouwt alle HTML-pagina's (kant-en-klaar voor GitHub Pages) uit content.py.
Pure Python, geen externe afhankelijkheden.
"""
import os
import html
import json
import datetime
from content import SITE, NAV, CATS, ARTICLES, cat, article
from make_art import logo_mark_inner

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # repo-root (ouder van tools/)


def esc(s):
    return html.escape(s, quote=True)


def write_page(path, content):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full) or ".", exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)


# ============================================================
#  Gedeelde SVG-iconen (origineel getekend, geen merklogo's)
# ============================================================
IC_MAIL = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" '
           'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
           '<rect x="3" y="5" width="18" height="14" rx="3"/><path d="M4 7l8 6 8-6"/></svg>')
IC_INSTA = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" '
            'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
            '<rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/>'
            '<circle cx="17.3" cy="6.7" r="1.1" fill="currentColor" stroke="none"/></svg>')
IC_PIN = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" '
          'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
          '<path d="M12 21s7-6.3 7-11a7 7 0 1 0-14 0c0 4.7 7 11 7 11z"/><circle cx="12" cy="10" r="2.5"/></svg>')
IC_ARROW = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" '
            'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
            '<path d="M5 12h14M13 6l6 6-6 6"/></svg>')
IC_EXT = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
          'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
          '<path d="M7 17 17 7M9 7h8v8"/></svg>')
IC_CHEV = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" '
           'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg>')
IC_CHECK = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" '
            'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 12l5 5L20 6"/></svg>')

SUN_DIVIDER = (
    '<div class="sun-row" aria-hidden="true">'
    '<svg viewBox="0 0 24 24" fill="currentColor"><circle cx="12" cy="12" r="5"/></svg>'
    '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 3c-1 4-1 4-5 5 4 1 4 1 5 5 1-4 1-4 5-5-4-1-4-1-5-5z"/></svg>'
    '<svg viewBox="0 0 24 24" fill="currentColor"><circle cx="12" cy="12" r="5"/></svg>'
    '</div>'
)


def squiggle(color="var(--sun)"):
    return (f'<svg class="squiggle" viewBox="0 0 128 16" fill="none" aria-hidden="true">'
            f'<path d="M4,8 q16,-9 32,0 t32,0 t32,0 t28,0" stroke="{color}" '
            f'stroke-width="5" stroke-linecap="round"/></svg>')


# ============================================================
#  <head>
# ============================================================
def head(title, desc, path, *, og_image=None, jsonld=None, article_meta=None):
    canonical = SITE["url"] + path
    og_image = og_image or "/assets/img/og-image.png"
    og_url = SITE["url"] + og_image
    full_title = title if title == SITE["name"] else f"{title} · {SITE['name']}"
    parts = [f'''<!DOCTYPE html>
<html lang="nl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(full_title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{esc(canonical)}">
<meta name="theme-color" content="#FBF6EE">
<meta name="author" content="{esc(SITE['author'])}">
<meta name="robots" content="index, follow">

<meta property="og:type" content="{'article' if article_meta else 'website'}">
<meta property="og:site_name" content="{esc(SITE['name'])}">
<meta property="og:locale" content="nl_NL">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{esc(canonical)}">
<meta property="og:image" content="{esc(og_url)}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(title)}">
<meta name="twitter:description" content="{esc(desc)}">
<meta name="twitter:image" content="{esc(og_url)}">''']

    if article_meta:
        parts.append(f'<meta property="article:published_time" content="{article_meta["date"]}">')
        parts.append(f'<meta property="article:author" content="{esc(SITE["author"])}">')
        parts.append(f'<meta property="article:section" content="{esc(article_meta["section"])}">')

    parts.append('''
<link rel="icon" href="/assets/img/favicon.svg" type="image/svg+xml">
<link rel="icon" href="/assets/img/favicon-32.png" sizes="32x32" type="image/png">
<link rel="apple-touch-icon" href="/assets/img/apple-touch-icon.png">

<link rel="preload" href="/assets/fonts/mulish-wght.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/assets/fonts/fraunces-wght.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/assets/css/style.css">''')

    if jsonld:
        if not isinstance(jsonld, list):
            jsonld = [jsonld]
        for block in jsonld:
            parts.append('<script type="application/ld+json">'
                         + json.dumps(block, ensure_ascii=False) + '</script>')

    parts.append('</head>\n<body>')
    parts.append('<a class="skip-link" href="#main">Naar de inhoud</a>')
    return "\n".join(parts)


# ============================================================
#  Header / navigatie
# ============================================================
def nav_html(active):
    items = []
    for it in NAV:
        is_active = (active == it["href"])
        cur = ' aria-current="page"' if is_active else ""
        if it.get("sub"):
            sub_links = [f'<a href="/nieuws/"><span class="dot" style="background:var(--ink)"></span>Alle artikelen</a>']
            for c in CATS:
                sub_links.append(
                    f'<a href="/categorie/{c["slug"]}/"><span class="dot" style="background:{c["dot"]}"></span>{esc(c["name"])}</a>')
            items.append(f'''<li class="has-sub">
<button class="nav__toggle-sub" aria-expanded="false" aria-haspopup="true">{esc(it["label"])} {IC_CHEV}</button>
<ul class="submenu">{"".join(sub_links)}</ul>
</li>''')
        else:
            items.append(f'<li><a class="nav__link" href="{it["href"]}"{cur}>{esc(it["label"])}</a></li>')

    return f'''<header class="site-header">
<nav class="nav wrap" aria-label="Hoofdmenu">
<a class="brand" href="/" aria-label="The Happy Days — naar de homepage">
<span class="brand__mark">{logo_mark_inner_svg()}</span>
<span class="brand__name">The Happy <b>Days</b></span>
</a>
<button class="nav__burger" aria-label="Menu openen of sluiten" aria-expanded="false" aria-controls="primary-nav"><span></span></button>
<ul class="nav__links" id="primary-nav">
{"".join(items)}
</ul>
</nav>
</header>'''


def logo_mark_inner_svg():
    return (f'<svg viewBox="0 0 40 40" fill="none" aria-hidden="true" '
            f'stroke-linecap="round" stroke-linejoin="round">{logo_mark_inner()}</svg>')


# ============================================================
#  Footer + cookiebar
# ============================================================
def social_block(cls):
    return f'''<div class="{cls}">
<a href="{SITE['instagram']}" aria-label="Instagram" rel="noopener">{IC_INSTA}</a>
<a href="{SITE['pinterest']}" aria-label="Pinterest" rel="noopener">{IC_PIN}</a>
<a href="mailto:{SITE['email']}" aria-label="E-mail">{IC_MAIL}</a>
</div>'''


def footer_html():
    cat_links = "".join(
        f'<li><a href="/categorie/{c["slug"]}/">{esc(c["name"])}</a></li>' for c in CATS)
    return f'''<footer class="site-footer">
<div class="wrap footer-top">
<div class="footer-col footer-brand">
<a class="brand" href="/" aria-label="The Happy Days">
<span class="brand__mark">{logo_mark_inner_svg()}</span>
<span class="brand__name">The Happy <b>Days</b></span>
</a>
<p>Een Nederlandse leefstijlblog over rust, aandacht en alledaags geluk. Fijne, gewone dagen — net iets mooier gemaakt.</p>
{social_block("footer-social")}
</div>
<div class="footer-col">
<h4>Ontdek</h4>
<ul>
<li><a href="/">Home</a></li>
<li><a href="/over/">Over</a></li>
<li><a href="/nieuws/">Nieuws</a></li>
<li><a href="/schrijfster/">Schrijfster</a></li>
<li><a href="/partners/">Partners</a></li>
<li><a href="/contact/">Contact</a></li>
</ul>
</div>
<div class="footer-col">
<h4>Thema's</h4>
<ul>{cat_links}</ul>
</div>
<div class="footer-col">
<h4>Contact</h4>
<ul>
<li><a href="mailto:{SITE['email']}">{SITE['email']}</a></li>
<li><a href="/contact/">Stuur een bericht</a></li>
<li><a href="/partners/">Samenwerken</a></li>
</ul>
</div>
</div>
<div class="wrap footer-bottom">
<p>© <span data-year>{datetime.date.today().year}</span> {esc(SITE['name'])}. Met aandacht gemaakt.</p>
<div class="footer-legal">
<a href="/privacy/">Privacybeleid</a>
<a href="/cookies/">Cookiebeleid</a>
</div>
</div>
</footer>

<div class="cookiebar" id="cookiebar" role="dialog" aria-live="polite" aria-label="Cookiemelding">
<p>We gebruiken alleen functionele cookies om de site goed te laten werken — geen tracking. Meer lezen in ons <a href="/cookies/">cookiebeleid</a>.</p>
<div class="actions">
<button class="btn btn--coral btn--sm" data-cookie-accept>Akkoord</button>
</div>
</div>

<script src="/assets/js/main.js" defer></script>
</body>
</html>'''


# ============================================================
#  Bouwstenen
# ============================================================
def card_html(a):
    c = cat(a["cat"])
    return f'''<a class="card" href="/nieuws/{a['slug']}/">
<span class="card__media"><img src="/assets/img/{a['img']}" alt="Illustratie bij: {esc(a['title'])}" loading="lazy" width="400" height="300"></span>
<span class="card__body">
<span class="tag"><span class="dot" style="background:{c['dot']}"></span>{esc(c['name'])}</span>
<span class="card__title">{esc(a['title'])}</span>
<span class="card__excerpt">{esc(a['excerpt'])}</span>
<span class="card__meta">{a['date_nl']}<span class="sep"></span>{a['read']} min lezen</span>
</span>
</a>'''


def posts_grid(items, extra=""):
    return f'<div class="posts {extra}">' + "".join(card_html(a) for a in items) + '</div>'


def head_block(kicker, title, sub=None, center=True):
    cls = "head-block center" if center else "head-block"
    h = f'<div class="{cls}"><span class="script">{esc(kicker)}</span><h2>{esc(title)}</h2>{squiggle()}'
    if sub:
        h += f'<p>{esc(sub)}</p>'
    return h + '</div>'


def page_head(kicker, title, sub=None, crumbs=None):
    cr = ""
    if crumbs:
        links = ' <span aria-hidden="true">›</span> '.join(
            (f'<a href="{href}">{esc(label)}</a>' if href else esc(label)) for label, href in crumbs)
        cr = f'<nav class="crumbs" aria-label="Kruimelpad">{links}</nav>'
    s = f'<p>{esc(sub)}</p>' if sub else ""
    return f'''<section class="page-head"><div class="wrap narrow">
{cr}<span class="script">{esc(kicker)}</span><h1>{esc(title)}</h1>{s}
</div></section>'''


def sorted_articles():
    return sorted(ARTICLES, key=lambda a: a["date"], reverse=True)


# ============================================================
#  JSON-LD
# ============================================================
def ld_website():
    return {
        "@context": "https://schema.org", "@type": "WebSite",
        "name": SITE["name"], "url": SITE["url"] + "/", "inLanguage": "nl-NL",
        "description": SITE["description"],
        "publisher": {"@type": "Organization", "name": SITE["name"],
                      "logo": {"@type": "ImageObject", "url": SITE["url"] + "/assets/img/favicon-192.png"}},
    }


def ld_breadcrumb(items):
    return {
        "@context": "https://schema.org", "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": name,
             "item": SITE["url"] + href}
            for i, (name, href) in enumerate(items)],
    }


def ld_article(a):
    c = cat(a["cat"])
    url = f"{SITE['url']}/nieuws/{a['slug']}/"
    return {
        "@context": "https://schema.org", "@type": "BlogPosting",
        "headline": a["title"], "description": a["excerpt"],
        "inLanguage": "nl-NL",
        "datePublished": a["date"], "dateModified": a["date"],
        "image": [f"{SITE['url']}/assets/img/og/{a['slug']}.png"],
        "articleSection": c["name"],
        "author": {"@type": "Person", "name": SITE["author"], "url": SITE["url"] + "/schrijfster/"},
        "publisher": {"@type": "Organization", "name": SITE["name"],
                      "logo": {"@type": "ImageObject", "url": SITE["url"] + "/assets/img/favicon-192.png"}},
        "mainEntityOfPage": {"@type": "WebPage", "@id": url},
    }


# ============================================================
#  PAGINA'S
# ============================================================
def build_home():
    recent = sorted_articles()[:6]
    cats_html = "".join(f'''<a class="cat" href="/categorie/{c['slug']}/">
<span class="cat__icon" style="background:{c['tint']}"><img src="/assets/img/{c['icon']}" alt="" width="48" height="48" aria-hidden="true"></span>
<span>{esc(c['name'])}</span><small>{esc(c['desc'])}</small>
</a>''' for c in CATS)

    body = f'''{nav_html("/")}
<main id="main">

<section class="hero">
<div class="wrap hero__grid">
<div class="hero__copy">
<span class="hero__kicker script">welkom!</span>
<h1>Fijne dagen zitten in de <em>kleine dingen</em></h1>
<p class="hero__text">The Happy Days is een Nederlandse leefstijlblog over rust, aandacht en alledaags geluk — met eerlijke verhalen en praktische tips.</p>
<div class="hero__cta">
<a class="btn btn--coral" href="/nieuws/">Lees de blog {IC_ARROW}</a>
<a class="btn btn--ghost" href="/over/">Over The Happy Days</a>
</div>
</div>
<div class="hero__art">
<img src="/assets/img/hero.svg" alt="Illustratie van een zonnige ochtend met een kop koffie, een open dagboek en een plantje" width="520" height="470">
</div>
</div>
<svg class="doodle doodle--1" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 3c-1 4-1 4-5 5 4 1 4 1 5 5 1-4 1-4 5-5-4-1-4-1-5-5z"/></svg>
<svg class="doodle doodle--2" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><circle cx="12" cy="12" r="6"/></svg>
</section>

<section class="section section--blush">
<div class="wrap narrow center stack">
{SUN_DIVIDER}
<h2 style="font-size:clamp(1.6rem,3.4vw,2.4rem)">The Happy Days gaat over alledaags geluk — niet over een perfect leven</h2>
<p class="lede">Geen toverwoorden, geen filters, geen leven dat altijd op rolletjes loopt. Wél eerlijke verhalen en kleine, haalbare ideeën die je gewone dagen net iets fijner maken. Want geluk zit zelden in de grote dingen, en juist heel vaak in de kleine.</p>
</div>
</section>

<section class="section">
<div class="wrap">
<div style="display:flex;align-items:flex-end;justify-content:space-between;gap:1rem;flex-wrap:wrap;margin-bottom:2rem">
{head_block("vers van de blog", "De nieuwste artikelen", center=False)}
<a class="btn btn--ghost btn--sm" href="/nieuws/">Alle artikelen {IC_ARROW}</a>
</div>
{posts_grid(recent)}
</div>
</section>

<section class="section section--cream2">
<div class="wrap">
{head_block("ontdek per thema", "Waar wil je over lezen?", "Vier rubrieken vol inspiratie voor fijnere, rustigere dagen.")}
<div class="cats" style="margin-top:2.4rem">{cats_html}</div>
</div>
</section>

<section class="section">
<div class="wrap writer">
<div class="writer__photo">
<div class="frame"><img src="/assets/img/avatar-saar.svg" alt="Tekening van Saar, de schrijfster van The Happy Days" width="360" height="360"></div>
</div>
<div class="writer__copy">
<span class="writer__sig">Hoi, ik ben Saar</span>
<h2>De vrouw achter The Happy Days</h2>
<p>Ik ben Saar, begin dertig, en ik geloof dat een fijn leven niet zit in grootse dingen, maar in de gewone momenten waar je even bij stilstaat. Op The Happy Days deel ik wat mij helpt om met meer rust en aandacht te leven — eerlijk, nuchter en zonder dat het perfect hoeft.</p>
<a class="btn btn--sun" href="/schrijfster/">Maak kennis met mij {IC_ARROW}</a>
</div>
</div>
</section>

<section class="section">
<div class="wrap">
<div class="follow">
<span class="script">blijf op de hoogte</span>
<h2>Zin in meer fijne dagen?</h2>
<p>Volg The Happy Days voor nieuwe artikelen en dagelijkse dosis goede zin, of stuur me gerust een berichtje. Ik vind het altijd leuk om van je te horen.</p>
{social_block("socials")}
</div>
</div>
</section>

</main>
{footer_html()}'''

    return head(SITE["name"],
                SITE["description"], "/",
                jsonld=[ld_website()]), body


def build_over():
    values = [
        ("ico-zelfzorg.svg", "Kleine dingen tellen",
         "Geluk zit zelden in grootse momenten. We vieren juist de gewone dingen: een kop koffie in de zon, een goed gesprek, een opgeruimde plek."),
        ("ico-mindful.svg", "Eerlijk en nuchter",
         "Geen perfecte plaatjes of onhaalbare idealen. Alles wat je hier leest, is down-to-earth en gewoon toe te passen in een druk leven."),
        ("ico-groei.svg", "Rust boven ruis",
         "De wereld is druk genoeg. The Happy Days is een rustige plek om even op adem te komen, met aandacht voor wat er echt toe doet."),
    ]
    vhtml = "".join(f'''<div class="value">
<img class="value__icon" src="/assets/img/{i}" alt="" aria-hidden="true" width="52" height="52">
<h3>{esc(t)}</h3><p>{esc(d)}</p></div>''' for i, t, d in values)
    cat_chips = "".join(
        f'<a class="btn btn--ghost btn--sm" href="/categorie/{c["slug"]}/">{esc(c["name"])}</a>' for c in CATS)

    body = f'''{nav_html("/over/")}
<main id="main">
{page_head("over ons", "Over The Happy Days", "Een rustige plek op internet over rust, aandacht en alledaags geluk.")}

<section class="section" style="padding-top:0">
<div class="wrap narrow prose">
<p class="lede">The Happy Days is een Nederlandse leefstijlblog die draait om één eenvoudig idee: een fijn leven maak je niet in de grote, bijzondere momenten, maar in de gewone dagen. In hoe je je ochtend begint, hoe je je huis inricht, en hoe vriendelijk je voor jezelf bent als het even tegenzit.</p>
<p>In een wereld die steeds drukker en sneller lijkt te gaan, willen we een tegenwicht bieden. Een plek waar je even op adem komt, inspiratie opdoet en het gevoel krijgt dat het ook rustiger mág. Niet met zweverige beloftes of perfecte plaatjes, maar met eerlijke verhalen en kleine, haalbare ideeën.</p>

<h2>Waar we in geloven</h2>
</div>
<div class="wrap" style="margin-top:1.6rem"><div class="values">{vhtml}</div></div>
</section>

<section class="section section--blush">
<div class="wrap narrow prose">
<h2>Wat je hier vindt</h2>
<p>Op The Happy Days schrijven we over de dingen die een gewone dag fijner maken, verdeeld over vier rubrieken:</p>
<ul>
<li><strong>Mindful leven</strong> — rust, aandacht en minder ruis in je dag.</li>
<li><strong>Persoonlijke groei</strong> — kleine stappen naar een leven dat bij je past.</li>
<li><strong>Thuis &amp; sfeer</strong> — een huis waar je tot rust komt.</li>
<li><strong>Zelfzorg</strong> — goed voor jezelf zorgen, met aandacht.</li>
</ul>
<p style="display:flex;flex-wrap:wrap;gap:.6rem;margin-top:1.4rem">{cat_chips}</p>
</div>
</section>

<section class="section">
<div class="wrap narrow center stack">
{SUN_DIVIDER}
<h2>Wie schrijft dit allemaal?</h2>
<p class="lede">Achter The Happy Days zit Saar — begin dertig, liefhebber van rustige ochtenden, goede koffie en de kleine momenten. Benieuwd naar het verhaal achter de blog?</p>
<p><a class="btn btn--coral" href="/schrijfster/">Maak kennis met Saar {IC_ARROW}</a></p>
</div>
</section>
</main>
{footer_html()}'''
    return head("Over The Happy Days",
                "Over The Happy Days: een Nederlandse leefstijlblog over rust, aandacht en alledaags geluk. Lees waar we in geloven en wat je hier vindt.",
                "/over/",
                jsonld=[ld_breadcrumb([("Home", "/"), ("Over", "/over/")])]), body


def build_partners():
    partners = [
        {"name": "Vaker Vrolijk", "url": "https://www.vakervrolijk.nl/", "initial": "V", "color": "#E98B6F",
         "desc": "De positieve blog van Romy met als motto ‘Jouw leven, jouw feestje.’ Op een eerlijke, "
                 "down-to-earth manier vol vrolijkheid, lifestyle, recepten en persoonlijke groei."},
        {"name": "Esmée Lifestyle", "url": "https://www.esmeelifestyle.nl/", "initial": "E", "color": "#F2B544",
         "desc": "De lifestyle blog vol geluk van Esmée, met wekelijks meerdere artikelen over geluk, "
                 "business en lifestyle — allemaal geschreven met een positieve twist."},
    ]
    phtml = "".join(f'''<div class="partner">
<div class="partner__badge" style="background:{p['color']}">{p['initial']}</div>
<div>
<h3>{esc(p['name'])}</h3>
<p>{esc(p['desc'])}</p>
<a class="ext" href="{p['url']}" target="_blank" rel="noopener">Bezoek {esc(p['name'])} {IC_EXT}</a>
</div>
</div>''' for p in partners)

    body = f'''{nav_html("/partners/")}
<main id="main">
{page_head("samen sterker", "Partners & samenwerkingen", "Mooie blogs en merken die passen bij The Happy Days.")}

<section class="section" style="padding-top:0">
<div class="wrap narrow prose" style="margin-bottom:2rem">
<p class="lede">Op deze plek komen binnenkort onze linkpartners en samenwerkingen te staan: blogs en merken die net als wij geloven in rust, aandacht en alledaags geluk.</p>
<p>Tot die tijd delen we graag twee toonaangevende Nederlandse leefstijlblogs die we zelf met veel plezier lezen. Ben je op zoek naar nog meer positiviteit en inspiratie? Neem zeker een kijkje.</p>
</div>
<div class="wrap"><div class="partner-list">{phtml}</div></div>

<div class="wrap"><div class="partner-cta">
<h3 style="font-size:1.35rem">Zelf samenwerken of linkpartner worden?</h3>
<p>Heb je een blog of merk dat past bij The Happy Days? Ik sta open voor leuke samenwerkingen en link-uitwisselingen.</p>
<p style="margin-top:1.2rem"><a class="btn btn--coral" href="mailto:{SITE['email']}">Mail naar {SITE['email']}</a></p>
</div></div>
</section>
</main>
{footer_html()}'''
    return head("Partners & samenwerkingen",
                "Partners van The Happy Days en twee toonaangevende Nederlandse leefstijlblogs die we aanraden: Vaker Vrolijk en Esmée Lifestyle.",
                "/partners/",
                jsonld=[ld_breadcrumb([("Home", "/"), ("Partners", "/partners/")])]), body


def build_nieuws():
    items = sorted_articles()
    chips = ['<a class="btn btn--coral btn--sm" href="/nieuws/">Alle</a>']
    for c in CATS:
        chips.append(f'<a class="btn btn--ghost btn--sm" href="/categorie/{c["slug"]}/">{esc(c["name"])}</a>')
    body = f'''{nav_html("/nieuws/")}
<main id="main">
{page_head("de blog", "Nieuws & artikelen", "Eerlijke verhalen en praktische tips voor fijne, gewone dagen.")}

<section class="section" style="padding-top:0">
<div class="wrap">
<div style="display:flex;flex-wrap:wrap;gap:.6rem;justify-content:center;margin-bottom:2.4rem">{"".join(chips)}</div>
{posts_grid(items)}
<p class="list-note">meer artikelen volgen — er komt elke week iets bij ♥</p>
</div>
</section>
</main>
{footer_html()}'''
    return head("Nieuws & artikelen",
                "Alle artikelen van The Happy Days over mindful leven, persoonlijke groei, thuis & sfeer en zelfzorg.",
                "/nieuws/",
                jsonld=[ld_breadcrumb([("Home", "/"), ("Nieuws", "/nieuws/")])]), body


def build_category(c):
    items = [a for a in sorted_articles() if a["cat"] == c["slug"]]
    grid = posts_grid(items) if items else '<p class="list-note">binnenkort de eerste artikelen ♥</p>'
    body = f'''{nav_html("/nieuws/")}
<main id="main">
{page_head(c["name"].lower(), c["name"], c["intro"], crumbs=[("Home", "/"), ("Nieuws", "/nieuws/"), (c["name"], None)])}

<section class="section" style="padding-top:0">
<div class="wrap">{grid}
<p style="text-align:center;margin-top:2.4rem"><a class="btn btn--ghost" href="/nieuws/">{IC_CHEV} Alle artikelen</a></p>
</div>
</section>
</main>
{footer_html()}'''
    return head(c["name"],
                f"{c['name']} op The Happy Days. {c['desc']}",
                f"/categorie/{c['slug']}/",
                jsonld=[ld_breadcrumb([("Home", "/"), ("Nieuws", "/nieuws/"), (c["name"], f"/categorie/{c['slug']}/")])]), body


def build_schrijfster():
    facts = [
        "Begin dertig en woont in Haarlem",
        "Drinkt haar koffie het liefst buiten in de ochtendzon",
        "Houdt van rustige zondagen, lange wandelingen en een goed boek",
        "Gelooft dat de kleine dingen het leven mooi maken",
    ]
    fhtml = "".join(f'<li>{IC_CHECK}<span>{esc(f)}</span></li>' for f in facts)
    fav = sorted_articles()[:3]
    body = f'''{nav_html("/schrijfster/")}
<main id="main">
{page_head("de schrijfster", "Hoi, ik ben Saar", crumbs=[("Home", "/"), ("Schrijfster", "/schrijfster/")])}

<section class="section" style="padding-top:0">
<div class="wrap writer">
<div class="writer__photo">
<div class="frame"><img src="/assets/img/avatar-saar.svg" alt="Tekening van Saar, de schrijfster van The Happy Days" width="360" height="360"></div>
</div>
<div class="writer__copy prose">
<p class="lede">Ik ben Saar, oprichter en schrijfster van The Happy Days. Begin dertig, geboren optimist, en groot liefhebber van de kleine momenten waar de meeste mensen aan voorbijlopen.</p>
<p>Een paar jaar geleden merkte ik dat mijn dagen op de automatische piloot voorbijvlogen. Altijd druk, altijd ‘aan’, en aan het eind van de week kon ik me amper herinneren waar de tijd was gebleven. Toen ik bewust kleine dingen anders ging doen — een rustige ochtend, mijn telefoon vaker weg, even tijd voor mezelf — veranderde er meer dan ik had verwacht. Niet mijn hele leven, maar wel hoe ik erin stond.</p>
<p>The Happy Days begon als mijn manier om die kleine ontdekkingen vast te leggen. Inmiddels is het een plek waar ik deel wat mij helpt om met meer rust en aandacht te leven, in de hoop dat het ook jou wat oplevert. Eerlijk en nuchter, want ik geloof niet in perfecte plaatjes — ik geloof in fijne, gewone dagen.</p>
<span class="writer__sig" style="font-size:3rem">Saar</span>
</div>
</div>
</section>

<section class="section section--blush">
<div class="wrap narrow">
{head_block("even voorstellen", "Saar in het kort")}
<ul class="facts" style="max-width:560px;margin:1.6rem auto 0">{fhtml}</ul>
</div>
</section>

<section class="section">
<div class="wrap">
{head_block("lees ook", "Mijn favoriete artikelen om mee te beginnen")}
<div style="margin-top:2.4rem">{posts_grid(fav)}</div>
</div>
</section>

<section class="section" style="padding-top:0">
<div class="wrap narrow center stack">
<h2>Even iets kwijt?</h2>
<p class="lede">Ik vind het altijd leuk om van lezers te horen — of je nou een tip hebt, een vraag, of gewoon hallo wilt zeggen.</p>
<p><a class="btn btn--coral" href="/contact/">Stuur me een berichtje {IC_ARROW}</a></p>
</div>
</section>
</main>
{footer_html()}'''
    person_ld = {
        "@context": "https://schema.org", "@type": "Person",
        "name": SITE["author"], "jobTitle": SITE["author_role"],
        "url": SITE["url"] + "/schrijfster/",
        "image": SITE["url"] + "/assets/img/avatar-saar.svg",
        "worksFor": {"@type": "Organization", "name": SITE["name"]},
        "homeLocation": {"@type": "Place", "name": SITE["city"]},
    }
    return head("De schrijfster — Saar",
                "Maak kennis met Saar, oprichter en schrijfster van The Happy Days. Lees het verhaal achter de blog.",
                "/schrijfster/",
                jsonld=[person_ld, ld_breadcrumb([("Home", "/"), ("Schrijfster", "/schrijfster/")])]), body


def build_contact():
    body = f'''{nav_html("/contact/")}
<main id="main">
{page_head("zeg hallo", "Contact", "Leuk dat je contact wilt opnemen — ik hoor graag van je.")}

<section class="section" style="padding-top:0">
<div class="wrap">
<div class="contact-card">
<div class="mail-ico">{IC_MAIL}</div>
<p class="eyebrow" style="color:var(--ink-soft)">Stuur een mailtje naar</p>
<p class="mail-big"><a href="mailto:{SITE['email']}">{SITE['email']}</a></p>
<p>Heb je een vraag, een tip of een idee voor een artikel? Of wil je samenwerken? Stuur me gerust een bericht. Ik probeer binnen een paar dagen te reageren.</p>
<a class="btn btn--coral" href="mailto:{SITE['email']}">Open je mailprogramma {IC_ARROW}</a>
</div>
<div class="wrap narrow center" style="margin-top:2rem">
<p style="color:var(--ink-soft)">Wil je samenwerken of linkpartner worden? Kijk dan ook even op de <a href="/partners/">partnerspagina</a>.</p>
</div>
</div>
</section>
</main>
{footer_html()}'''
    return head("Contact",
                f"Neem contact op met The Happy Days via {SITE['email']}. Vragen, tips of samenwerkingen zijn altijd welkom.",
                "/contact/",
                jsonld=[ld_breadcrumb([("Home", "/"), ("Contact", "/contact/")])]), body


def build_article(a):
    c = cat(a["cat"])
    og = f"/assets/img/og/{a['slug']}.png"
    related = [x for x in sorted_articles() if x["slug"] != a["slug"] and x["cat"] == a["cat"]]
    if len(related) < 3:
        related += [x for x in sorted_articles() if x["slug"] != a["slug"] and x not in related]
    related = related[:3]
    body = f'''{nav_html("/nieuws/")}
<main id="main">
<article>
<section class="article-hero">
<div class="wrap narrow center">
<nav class="crumbs" aria-label="Kruimelpad"><a href="/">Home</a> <span aria-hidden="true">›</span> <a href="/nieuws/">Nieuws</a> <span aria-hidden="true">›</span> <a href="/categorie/{c['slug']}/">{esc(c['name'])}</a></nav>
<span class="tag" style="margin:0 auto"><span class="dot" style="background:{c['dot']}"></span>{esc(c['name'])}</span>
<h1>{esc(a['title'])}</h1>
<div class="article-hero__meta">
<span>Door {esc(SITE['author'])}</span><span class="sep" style="width:4px;height:4px;border-radius:50%;background:var(--coral);display:inline-block"></span>
<time datetime="{a['date']}">{a['date_nl']}</time><span class="sep" style="width:4px;height:4px;border-radius:50%;background:var(--coral);display:inline-block"></span>
<span>{a['read']} min lezen</span>
</div>
</div>
</section>

<div class="wrap">
<figure class="article-figure">
<img src="/assets/img/{a['img']}" alt="Illustratie bij: {esc(a['title'])}" width="400" height="300" style="aspect-ratio:2/1;object-fit:cover;background:var(--blush-2)">
</figure>
</div>

<div class="wrap">
<div class="article-body prose">
{a['body'].strip()}

<div class="byline">
<img src="/assets/img/avatar-saar.svg" alt="Saar" width="64" height="64">
<div class="who">{esc(SITE['author'])}<small>{esc(SITE['author_role'])} van The Happy Days</small></div>
</div>
</div>
</div>
</article>

<section class="section section--cream2">
<div class="wrap">
{head_block("lees verder", "Misschien vind je dit ook fijn")}
<div style="margin-top:2.4rem">{posts_grid(related)}</div>
</div>
</section>
</main>
{footer_html()}'''
    return head(a["title"], a["excerpt"], f"/nieuws/{a['slug']}/",
                og_image=og,
                article_meta={"date": a["date"], "section": c["name"]},
                jsonld=[ld_article(a),
                        ld_breadcrumb([("Home", "/"), ("Nieuws", "/nieuws/"),
                                       (c["name"], f"/categorie/{c['slug']}/"),
                                       (a["title"], f"/nieuws/{a['slug']}/")])]), body


def legal_page(slug, kicker, title, intro, sections):
    blocks = f'<p class="lede">{esc(intro)}</p>'
    for h, paras in sections:
        blocks += f'<h2>{esc(h)}</h2>'
        for p in paras:
            blocks += p  # mag HTML bevatten
    updated = "15 juni 2026"
    body = f'''{nav_html("/" + slug + "/")}
<main id="main">
{page_head(kicker, title)}
<section class="section" style="padding-top:0">
<div class="wrap narrow prose">
<p style="color:var(--ink-soft);font-size:.92rem">Laatst bijgewerkt: {updated}</p>
{blocks}
</div>
</section>
</main>
{footer_html()}'''
    return head(title,
                f"{title} van The Happy Days.",
                f"/{slug}/",
                jsonld=[ld_breadcrumb([("Home", "/"), (title, f"/{slug}/")])]), body


def build_privacy():
    sec = [
        ("Wie zijn wij", [
            f"<p>The Happy Days ({esc(SITE['url'])}) is een Nederlandse leefstijlblog. "
            f"Heb je vragen over je privacy? Mail dan naar <a href=\"mailto:{SITE['email']}\">{SITE['email']}</a>.</p>"]),
        ("Welke gegevens we verzamelen", [
            "<p>The Happy Days is bewust een eenvoudige, statische website. We verzamelen <strong>geen</strong> "
            "persoonsgegevens via formulieren, want die hebben we niet. Er is geen account, geen nieuwsbrief-"
            "inschrijving en geen reactiemogelijkheid.</p>",
            "<p>We gebruiken <strong>geen</strong> trackingcookies, advertentienetwerken of analytische software "
            "die jou volgt. De lettertypen op deze site worden vanaf onze eigen server geladen, dus er gaan geen "
            "gegevens naar externe partijen zoals Google Fonts.</p>"]),
        ("Hosting en serverlogs", [
            "<p>Deze website wordt gehost via GitHub Pages. Net als bij vrijwel elke website kan de hostingpartij "
            "om technische en beveiligingsredenen standaard serverlogs bijhouden, waaronder IP-adressen. Wij hebben "
            "daar zelf geen inzage in en gebruiken deze gegevens niet. Meer informatie vind je in het privacybeleid "
            "van GitHub.</p>"]),
        ("Mail je ons?", [
            f"<p>Stuur je ons een e-mail via <a href=\"mailto:{SITE['email']}\">{SITE['email']}</a>, dan bewaren we "
            "die mail alleen om je vraag te kunnen beantwoorden. We gebruiken je gegevens nergens anders voor en "
            "delen ze niet met anderen.</p>"]),
        ("Externe links", [
            "<p>Op deze site staan links naar andere websites, zoals die van bevriende blogs. Wij zijn niet "
            "verantwoordelijk voor het privacybeleid of de inhoud van die externe sites. Lees daar zelf even hun "
            "voorwaarden door.</p>"]),
        ("Je rechten", [
            "<p>Je hebt het recht om te weten welke gegevens we van je hebben (in ons geval dus vrijwel niets), en "
            "om die in te zien of te laten verwijderen. Neem hiervoor gerust contact met ons op.</p>"]),
        ("Wijzigingen", [
            "<p>Mocht The Happy Days in de toekomst uitbreiden met bijvoorbeeld een nieuwsbrief of statistieken, "
            "dan passen we dit privacybeleid daarop aan. Kijk dus af en toe even of er iets is veranderd.</p>"]),
    ]
    return legal_page("privacy", "het kleine lettertype", "Privacybeleid",
                      "Je privacy is belangrijk. Hieronder lees je kort en duidelijk hoe The Happy Days met je gegevens omgaat — spoiler: we verzamelen er bijna geen.",
                      sec)


def build_cookies():
    sec = [
        ("Wat zijn cookies", [
            "<p>Cookies zijn kleine bestandjes die een website op je apparaat kan opslaan. Ze worden voor van alles "
            "gebruikt: van het onthouden van instellingen tot het volgen van je surfgedrag. Wij houden het bewust "
            "zo eenvoudig mogelijk.</p>"]),
        ("Welke cookies wij gebruiken", [
            "<p>The Happy Days gebruikt <strong>alleen functionele opslag</strong>. Concreet betekent dat: wanneer "
            "je onze cookiemelding wegklikt, onthouden we dat met een klein stukje opslag in je eigen browser "
            "(local storage), zodat de melding niet bij elk bezoek opnieuw verschijnt. Deze informatie blijft op "
            "jouw apparaat en wordt nergens naartoe gestuurd.</p>"]),
        ("Wat wij níét doen", [
            "<p>We gebruiken <strong>geen</strong> tracking- of advertentiecookies, en <strong>geen</strong> "
            "analytische cookies die je gedrag volgen. Er worden ook geen gegevens gedeeld met externe partijen. "
            "Onze lettertypen laden we vanaf onze eigen server, dus ook daarvoor zijn geen externe cookies nodig.</p>"]),
        ("Cookies beheren of verwijderen", [
            "<p>Omdat we geen tracking gebruiken, hoef je eigenlijk niets in te stellen. Wil je de functionele opslag "
            "toch wissen, dan kan dat altijd via de instellingen van je browser, bij het onderdeel ‘browsegegevens "
            "wissen’.</p>"]),
        ("Vragen", [
            f"<p>Heb je vragen over ons cookiebeleid? Mail dan naar "
            f"<a href=\"mailto:{SITE['email']}\">{SITE['email']}</a>. We leggen het graag uit.</p>"]),
    ]
    return legal_page("cookies", "het kleine lettertype", "Cookiebeleid",
                      "Kort en eerlijk: The Happy Days gebruikt geen trackingcookies. Alleen een klein beetje functionele opslag om de site prettig te laten werken.",
                      sec)


def build_404():
    body = f'''{nav_html("")}
<main id="main">
<section class="page-head" style="padding-block:clamp(60px,9vw,120px)">
<div class="wrap narrow center stack">
<span class="brand__mark" style="width:72px;height:72px;margin:0 auto">{logo_mark_inner_svg()}</span>
<span class="script" style="font-size:clamp(2rem,5vw,3rem);transform:rotate(-2deg)">oeps!</span>
<h1>Deze pagina is even zoek</h1>
<p class="lede">De pagina die je zoekt bestaat niet (meer). Geen zorgen — er is genoeg moois te lezen.</p>
<div style="display:flex;gap:.8rem;justify-content:center;flex-wrap:wrap;margin-top:1rem">
<a class="btn btn--coral" href="/">Naar de homepage {IC_ARROW}</a>
<a class="btn btn--ghost" href="/nieuws/">Bekijk de blog</a>
</div>
</div>
</section>
</main>
{footer_html()}'''
    return ('''<!DOCTYPE html>
<html lang="nl"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Pagina niet gevonden · The Happy Days</title>
<meta name="robots" content="noindex">
<meta name="theme-color" content="#FBF6EE">
<link rel="icon" href="/assets/img/favicon.svg" type="image/svg+xml">
<link rel="icon" href="/assets/img/favicon-32.png" sizes="32x32" type="image/png">
<link rel="apple-touch-icon" href="/assets/img/apple-touch-icon.png">
<link rel="stylesheet" href="/assets/css/style.css">
</head><body>
<a class="skip-link" href="#main">Naar de inhoud</a>''') + body


# ============================================================
#  Sitemap / robots / config
# ============================================================
def build_sitemap():
    urls = [("/", "1.0"), ("/nieuws/", "0.9"), ("/over/", "0.7"),
            ("/schrijfster/", "0.7"), ("/partners/", "0.6"), ("/contact/", "0.6"),
            ("/privacy/", "0.3"), ("/cookies/", "0.3")]
    urls += [(f"/categorie/{c['slug']}/", "0.6") for c in CATS]
    urls += [(f"/nieuws/{a['slug']}/", "0.8") for a in ARTICLES]
    today = datetime.date.today().isoformat()
    rows = ""
    for loc, prio in urls:
        lm = today
        if loc.startswith("/nieuws/") and loc != "/nieuws/":
            slug = loc.strip("/").split("/")[-1]
            lm = article(slug)["date"]
        rows += (f'  <url><loc>{SITE["url"]}{loc}</loc>'
                 f'<lastmod>{lm}</lastmod><priority>{prio}</priority></url>\n')
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
            f'{rows}</urlset>\n')


def build_robots():
    return (f"User-agent: *\nAllow: /\n\nSitemap: {SITE['url']}/sitemap.xml\n")


# ============================================================
#  Alles wegschrijven
# ============================================================
def main():
    pages = {
        "index.html": build_home(),
        "over/index.html": build_over(),
        "partners/index.html": build_partners(),
        "nieuws/index.html": build_nieuws(),
        "schrijfster/index.html": build_schrijfster(),
        "contact/index.html": build_contact(),
        "privacy/index.html": build_privacy(),
        "cookies/index.html": build_cookies(),
    }
    for c in CATS:
        pages[f"categorie/{c['slug']}/index.html"] = build_category(c)
    for a in ARTICLES:
        pages[f"nieuws/{a['slug']}/index.html"] = build_article(a)

    for path, (hd, body) in pages.items():
        write_page(path, hd + "\n" + body + "\n")

    # 404 (losse opbouw)
    write_page("404.html", build_404() + "\n")

    # config & SEO-bestanden
    write_page("sitemap.xml", build_sitemap())
    write_page("robots.txt", build_robots())
    write_page("CNAME", SITE["domain"] + "\n")
    write_page(".nojekyll", "")

    print(f"Gebouwd: {len(pages) + 1} HTML-pagina's + sitemap/robots/CNAME/.nojekyll")
    for p in sorted(pages):
        print("  ", p)


if __name__ == "__main__":
    main()
