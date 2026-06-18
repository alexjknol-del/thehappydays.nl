#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genereer per-artikel social-share kaarten (1200x630 PNG)."""
import os, re, textwrap
import cairosvg
from content import ARTICLES, cat, SITE
from make_art import logo_mark_inner

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # repo-root (ouder van tools/)
IMG = os.path.join(ROOT, "assets", "img")
OGD = os.path.join(IMG, "og")
os.makedirs(OGD, exist_ok=True)

CREAM, INK, INKSOFT, SUN, CORAL, CORALDP = "#FBF6EE", "#38332D", "#6E665B", "#F2B544", "#E98B6F", "#D2694A"


def inline_svg(path, x, y, scale):
    """Lees een SVG-bestand en plaats de inhoud als <g> (geschaald/verplaatst)."""
    with open(path, encoding="utf-8") as f:
        s = f.read()
    inner = s[s.index(">", s.index("<svg")) + 1: s.rindex("</svg>")]
    inner = re.sub(r"<title>.*?</title>", "", inner, flags=re.S)
    return (f'<g transform="translate({x},{y}) scale({scale})" '
            f'stroke-linecap="round" stroke-linejoin="round">{inner}</g>')


def wrap_title(title):
    if len(title) <= 84:
        size, lh, width = 56, 66, 20
    else:
        size, lh, width = 47, 56, 24
    lines = textwrap.wrap(title, width=width)
    return size, lh, lines


def og_card(a):
    c = cat(a["cat"])
    W, H = 1200, 630
    size, lh, lines = wrap_title(a["title"])
    b = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" fill="none">']
    b.append(f'<rect width="{W}" height="{H}" fill="{CREAM}"/>')
    b.append(f'<circle cx="60" cy="40" r="200" fill="{SUN}" opacity="0.13"/>')
    b.append(f'<circle cx="1180" cy="600" r="230" fill="{CORAL}" opacity="0.13"/>')

    # rechter kaart met de artikel-illustratie
    b.append(f'<rect x="688" y="150" width="430" height="330" rx="28" fill="#FFFDF9" '
             f'stroke="rgba(56,51,45,0.08)"/>')
    art = os.path.join(IMG, a["img"])
    # illustratie 400x300 -> ~398 breed in kaart
    b.append(inline_svg(art, 704, 165, 0.745))

    # logo-mark + merknaam
    b.append(f'<g transform="translate(80,64) scale(1.5)" stroke-linecap="round" stroke-linejoin="round">'
             f'{logo_mark_inner()}</g>')
    b.append(f'<text x="152" y="98" font-family="Fraunces" font-weight="600" font-size="34" '
             f'fill="{INK}">The Happy Days</text>')

    # eyebrow (categorie)
    b.append(f'<text x="80" y="232" font-family="Mulish" font-weight="800" font-size="22" '
             f'letter-spacing="3" fill="{CORALDP}">{escape(c["name"].upper())}</text>')

    # titel (meerdere regels)
    y = 290
    b.append(f'<text x="80" font-family="Fraunces" font-weight="600" font-size="{size}" fill="{INK}">')
    for ln in lines:
        b.append(f'<tspan x="80" y="{y}">{escape(ln)}</tspan>')
        y += lh
    b.append('</text>')

    # tagline onderaan
    b.append(f'<text x="80" y="540" font-family="Mulish" font-weight="600" font-size="24" '
             f'fill="{INKSOFT}">{a["read"]} min lezen  ·  thehappydays.nl</text>')
    b.append('</svg>')
    return "".join(b)


def escape(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def main():
    for a in ARTICLES:
        svg = og_card(a)
        out = os.path.join(OGD, a["slug"] + ".png")
        cairosvg.svg2png(bytestring=svg.encode("utf-8"), write_to=out,
                         output_width=1200, output_height=630)
        print("  og/", a["slug"] + ".png")
    print("Klaar:", len(ARTICLES), "share-kaarten")


if __name__ == "__main__":
    main()
