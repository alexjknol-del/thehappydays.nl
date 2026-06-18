#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
The Happy Days — illustratie-kit.
Eén samenhangende, vriendelijke 'handgetekende' stijl: zachte ronde vormen,
warm palet, een terugkerend zonnetje. Alle visuals worden hier zelf getekend
(geen stockfoto's, geen copyrightmateriaal).
"""
import os

OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "assets", "img")
os.makedirs(OUT, exist_ok=True)

# ---- Palet (gelijk aan de CSS-tokens) ----
CREAM   = "#FBF6EE"
CREAM2  = "#F5ECDD"
PAPER   = "#FFFDF9"
INK     = "#38332D"
INKSOFT = "#6E665B"
SUN     = "#F2B544"
SUNDEEP = "#E29A18"
CORAL   = "#E98B6F"
CORALDP = "#D2694A"
BLUSH   = "#F8DCD0"
BLUSH2  = "#FCEAE2"
SAGE    = "#9FB291"
SAGESF  = "#E4EADD"
SKY     = "#BCD4DD"
SKYSF   = "#E2EEF1"
SKIN    = "#F0C49B"
SKINSH  = "#E3B083"
HAIR    = "#A9743F"
HAIRHI  = "#C49058"

SW = 3.4   # standaard lijndikte


def svg(w, h, body, vb=None):
    vb = vb or f"0 0 {w} {h}"
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" '
            f'width="{w}" height="{h}" role="img" fill="none" '
            f'stroke-linecap="round" stroke-linejoin="round">\n{body}\n</svg>\n')


def write(name, w, h, body, vb=None, title=None):
    t = f'<title>{title}</title>\n' if title else ''
    with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
        f.write(svg(w, h, t + body, vb))


def g(x, y, s, inner, rot=0):
    r = f" rotate({rot})" if rot else ""
    return f'<g transform="translate({x},{y}) scale({s}){r}">{inner}</g>'


# ============================================================
#  Kleine motieven / doodles
# ============================================================
def sun(cx, cy, r, color=SUN, rays=10, ray_len=None, sw=SW):
    """Zonnetje met stralen."""
    import math
    ray_len = ray_len or r * 0.55
    s = [f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{color}"/>']
    for i in range(rays):
        a = (2 * math.pi / rays) * i
        x1 = cx + math.cos(a) * (r + r * 0.30)
        y1 = cy + math.sin(a) * (r + r * 0.30)
        x2 = cx + math.cos(a) * (r + r * 0.30 + ray_len)
        y2 = cy + math.sin(a) * (r + r * 0.30 + ray_len)
        s.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
                 f'stroke="{color}" stroke-width="{sw}"/>')
    return "".join(s)


def heart(cx, cy, sz, color=CORAL, sw=0):
    """Klein hartje (gevuld)."""
    d = (f'M{cx},{cy+sz*0.32} '
         f'C{cx-sz*0.6},{cy-sz*0.25} {cx-sz*0.55},{cy-sz*0.75} {cx},{cy-sz*0.35} '
         f'C{cx+sz*0.55},{cy-sz*0.75} {cx+sz*0.6},{cy-sz*0.25} {cx},{cy+sz*0.32} Z')
    stroke = f' stroke="{INK}" stroke-width="{sw}"' if sw else ''
    return f'<path d="{d}" fill="{color}"{stroke}/>'


def sparkle(cx, cy, sz, color=SUN):
    d = (f'M{cx},{cy-sz} C{cx+sz*0.18},{cy-sz*0.18} {cx+sz*0.18},{cy-sz*0.18} {cx+sz},{cy} '
         f'C{cx+sz*0.18},{cy+sz*0.18} {cx+sz*0.18},{cy+sz*0.18} {cx},{cy+sz} '
         f'C{cx-sz*0.18},{cy+sz*0.18} {cx-sz*0.18},{cy+sz*0.18} {cx-sz},{cy} '
         f'C{cx-sz*0.18},{cy-sz*0.18} {cx-sz*0.18},{cy-sz*0.18} {cx},{cy-sz} Z')
    return f'<path d="{d}" fill="{color}"/>'


def dot(cx, cy, r, color=CORAL):
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{color}"/>'


def leaf(cx, cy, sz, color=SAGE, rot=0):
    d = (f'M{cx},{cy} C{cx-sz*0.5},{cy-sz*0.4} {cx-sz*0.4},{cy-sz} {cx},{cy-sz*1.2} '
         f'C{cx+sz*0.4},{cy-sz} {cx+sz*0.5},{cy-sz*0.4} {cx},{cy} Z')
    vein = f'<line x1="{cx}" y1="{cy}" x2="{cx}" y2="{cy-sz*1.05}" stroke="{INK}" stroke-width="1.6" opacity="0.5"/>'
    return f'<g transform="rotate({rot} {cx} {cy})"><path d="{d}" fill="{color}"/>{vein}</g>'


def steam(cx, cy, color=INKSOFT):
    """Twee dampkrullen."""
    p1 = f'<path d="M{cx-9},{cy} q-7,-9 0,-18 q7,-9 0,-18" stroke="{color}" stroke-width="2.6" opacity="0.55" fill="none"/>'
    p2 = f'<path d="M{cx+9},{cy} q7,-9 0,-18 q-7,-9 0,-18" stroke="{color}" stroke-width="2.6" opacity="0.55" fill="none"/>'
    return p1 + p2


def squiggle_path(w=120, color=SUN, sw=5):
    """Golvende onderstreping."""
    seg = w / 4
    d = f'M4,8 q{seg/2},-9 {seg},0 t{seg},0 t{seg},0 t{seg},0'
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w+8} 16" fill="none">'
            f'<path d="{d}" stroke="{color}" stroke-width="{sw}" stroke-linecap="round"/></svg>')


# ============================================================
#  Voorwerpen (lokale oorsprong, schaalbaar)
# ============================================================
def mug(fill=PAPER, drink=CORALDP):
    """Mok van opzij, ~ 0..90 breed."""
    body = (f'<path d="M14,30 Q14,26 18,26 L66,26 Q70,26 70,30 L66,74 '
            f'Q65,82 56,82 L24,82 Q15,82 14,74 Z" fill="{fill}" stroke="{INK}" stroke-width="{SW}"/>')
    drink_e = f'<ellipse cx="42" cy="30" rx="24" ry="5.5" fill="{drink}"/>'
    handle = f'<path d="M70,38 a15,15 0 0 1 0,28" fill="none" stroke="{INK}" stroke-width="{SW}"/>'
    saucer = f'<ellipse cx="42" cy="86" rx="40" ry="6.5" fill="{BLUSH}" stroke="{INK}" stroke-width="{SW}"/>'
    return saucer + body + handle + drink_e


def plant(pot=CORAL, foliage=SAGE):
    """Plant in pot, ~ 0..90 breed, 0..120 hoog (blad boven 0)."""
    leaves = (
        leaf(45, 60, 34, foliage, 0) +
        leaf(45, 64, 30, foliage, -42) +
        leaf(45, 64, 30, foliage, 42) +
        leaf(45, 66, 24, foliage, -78) +
        leaf(45, 66, 24, foliage, 78)
    )
    stem = f'<line x1="45" y1="64" x2="45" y2="92" stroke="{INK}" stroke-width="2.4" opacity="0.5"/>'
    pot_p = (f'<path d="M22,92 L68,92 L62,118 Q61,122 56,122 L34,122 Q29,122 28,118 Z" '
             f'fill="{pot}" stroke="{INK}" stroke-width="{SW}"/>')
    rim = f'<rect x="18" y="86" width="54" height="10" rx="5" fill="{pot}" stroke="{INK}" stroke-width="{SW}"/>'
    return leaves + stem + pot_p + rim


def journal(cover=CORAL):
    """Open dagboekje, ~ 0..150 breed."""
    base = (f'<path d="M12,30 Q75,18 138,30 L138,96 Q75,84 12,96 Z" '
            f'fill="{PAPER}" stroke="{INK}" stroke-width="{SW}"/>')
    spine = f'<line x1="75" y1="22" x2="75" y2="90" stroke="{INK}" stroke-width="2.4"/>'
    lines = ""
    for i, yy in enumerate((44, 56, 68)):
        lines += f'<line x1="20" y1="{yy}" x2="66" y2="{yy-2}" stroke="{INKSOFT}" stroke-width="2" opacity="0.45"/>'
        lines += f'<line x1="84" y1="{yy-2}" x2="130" y2="{yy}" stroke="{INKSOFT}" stroke-width="2" opacity="0.45"/>'
    ribbon = f'<path d="M118,18 l0,40 -8,-8 -8,8 0,-40 z" fill="{cover}" stroke="{INK}" stroke-width="2.6"/>'
    return base + spine + lines + ribbon


def pen(color=SUN):
    """Potlood/pen schuin, ~ 0..90."""
    body = (f'<g transform="rotate(38 45 50)">'
            f'<rect x="36" y="6" width="18" height="74" rx="4" fill="{color}" stroke="{INK}" stroke-width="{SW}"/>'
            f'<path d="M36,80 L54,80 L45,96 Z" fill="{INK}"/>'
            f'<rect x="36" y="6" width="18" height="9" rx="3" fill="{CORALDP}" stroke="{INK}" stroke-width="2.4"/>'
            f'</g>')
    return body


def candle(wax=BLUSH):
    """Brandende kaars, ~ 0..60 breed."""
    c = (f'<rect x="14" y="38" width="34" height="56" rx="6" fill="{wax}" stroke="{INK}" stroke-width="{SW}"/>'
         f'<ellipse cx="31" cy="38" rx="17" ry="5" fill="{PAPER}" stroke="{INK}" stroke-width="2.4"/>'
         f'<line x1="31" y1="34" x2="31" y2="26" stroke="{INK}" stroke-width="2.4"/>'
         f'<path d="M31,26 C26,20 26,12 31,4 C36,12 36,20 31,26 Z" fill="{SUN}"/>'
         f'<path d="M31,24 C28,20 28,15 31,9 C34,15 34,20 31,24 Z" fill="{CORALDP}" opacity="0.7"/>')
    return c


def armchair(fab=CORAL):
    """Fauteuil van voren, ~ 0..150 breed."""
    back = f'<path d="M22,30 Q24,12 44,12 L106,12 Q126,12 128,30 L128,70 L22,70 Z" fill="{fab}" stroke="{INK}" stroke-width="{SW}"/>'
    seat = f'<path d="M14,68 L136,68 L130,104 L20,104 Z" fill="{fab}" stroke="{INK}" stroke-width="{SW}"/>'
    cushion = f'<path d="M40,52 Q75,44 110,52 L108,70 L42,70 Z" fill="{BLUSH2}" stroke="{INK}" stroke-width="2.6"/>'
    arml = f'<rect x="10" y="58" width="20" height="48" rx="9" fill="{fab}" stroke="{INK}" stroke-width="{SW}"/>'
    armr = f'<rect x="120" y="58" width="20" height="48" rx="9" fill="{fab}" stroke="{INK}" stroke-width="{SW}"/>'
    legl = f'<line x1="30" y1="104" x2="26" y2="118" stroke="{INK}" stroke-width="{SW}"/>'
    legr = f'<line x1="120" y1="104" x2="124" y2="118" stroke="{INK}" stroke-width="{SW}"/>'
    return back + arml + armr + seat + cushion + legl + legr


def phone(face=INK, screen=SAGESF):
    """Telefoon liggend (scherm naar beneden) — 'leg ’m weg'."""
    body = f'<rect x="10" y="14" width="56" height="100" rx="14" fill="{face}" stroke="{INK}" stroke-width="{SW}"/>'
    cam = f'<circle cx="38" cy="26" r="3.2" fill="{SAGESF}"/>'
    z = (f'<text x="46" y="70" font-family="Caveat, cursive" font-size="34" fill="{SAGESF}" '
         f'opacity="0.9">z</text>')
    return body + cam


def basket(fill=SKY, band=PAPER):
    """Mand/opbergbox, ~ 0..110 breed."""
    b = (f'<path d="M14,40 L96,40 L88,104 Q87,108 82,108 L28,108 Q23,108 22,104 Z" '
         f'fill="{fill}" stroke="{INK}" stroke-width="{SW}"/>')
    rim = f'<rect x="8" y="32" width="94" height="12" rx="6" fill="{fill}" stroke="{INK}" stroke-width="{SW}"/>'
    weave = ""
    for xx in range(26, 92, 14):
        weave += f'<line x1="{xx}" y1="46" x2="{xx-4}" y2="104" stroke="{INK}" stroke-width="1.8" opacity="0.35"/>'
    return b + rim + weave


def glass_lemonade():
    """Glas limonade met citroenschijf, ~ 0..70 breed."""
    glass = (f'<path d="M16,18 L58,18 L52,96 Q51,102 45,102 L29,102 Q23,102 22,96 Z" '
             f'fill="{SKYSF}" stroke="{INK}" stroke-width="{SW}"/>')
    drink = f'<path d="M19,42 L55,42 L51,96 Q50,102 44,102 L30,102 Q24,102 23,96 Z" fill="{SUN}" opacity="0.85"/>'
    lemon = (f'<g transform="translate(50 24)"><circle r="13" fill="#FBE08A" stroke="{INK}" stroke-width="2.6"/>'
             f'<circle r="8" fill="#FCEFB6"/>'
             f'<line x1="-7" y1="0" x2="7" y2="0" stroke="{SUNDEEP}" stroke-width="1.6"/>'
             f'<line x1="0" y1="-7" x2="0" y2="7" stroke="{SUNDEEP}" stroke-width="1.6"/></g>')
    straw = f'<line x1="40" y1="14" x2="48" y2="-6" stroke="{CORAL}" stroke-width="5"/>'
    bubbles = "".join(dot(x, y, r, "#FCEFB6") for x, y, r in [(32, 60, 2.4), (40, 72, 2), (34, 84, 1.8)])
    return glass + drink + straw + lemon + bubbles


def moon(color="#F6E4B0"):
    """Wassende maan, ~ 0..90."""
    return (f'<path d="M64,12 A40,40 0 1 0 64,92 A30,30 0 1 1 64,12 Z" '
            f'fill="{color}" stroke="{INK}" stroke-width="{SW}"/>')


# ============================================================
#  Achtergrondpaneel
# ============================================================
def panel(w, h, fill, blob=None):
    rect = f'<rect x="0" y="0" width="{w}" height="{h}" rx="26" fill="{fill}"/>'
    b = ""
    if blob:
        bc, bx, by, br = blob
        b = f'<circle cx="{bx}" cy="{by}" r="{br}" fill="{bc}"/>'
    cid = f'cp{w}{h}{str(fill)[1:]}'
    defs = f'<defs><clipPath id="{cid}"><rect x="0" y="0" width="{w}" height="{h}" rx="26"/></clipPath></defs>'
    return rect, defs + f'<g clip-path="url(#{cid})">{b}</g>'


# ============================================================
#  ARTIKEL-ILLUSTRATIES (400 x 300)
# ============================================================
AW, AH = 400, 300


def art_morning():
    rect, clip = panel(AW, AH, BLUSH2, (SUN, 300, 70, 96))
    body = rect + clip
    body += g(150, 150, 1.7, mug(PAPER, "#8B5A38"))
    body += steam(150 + 1.7 * 42 - 0, 95)  # approx; redo precisely below
    # zon + doodles
    body += sun(78, 78, 22, SUN, rays=9)
    body += sparkle(330, 150, 9, CORAL)
    body += dot(300, 235, 5, CORAL)
    body += dot(70, 210, 4, SAGE)
    body += heart(345, 95, 12, CORAL)
    return body


def art_morning_v2():
    rect, clip = panel(AW, AH, BLUSH2, (SUN, 312, 64, 92))
    body = rect + clip
    body += sun(80, 76, 22, SUN, rays=9)
    # mok gecentreerd
    body += g(150, 150, 1.65, mug(PAPER, "#8B5A38") + steam(42, 22, INKSOFT))
    body += sparkle(330, 160, 9, CORAL)
    body += dot(304, 232, 5, CORAL)
    body += dot(64, 214, 4, SAGE)
    body += heart(348, 100, 12, CORAL)
    body += dot(120, 250, 3.4, SUNDEEP)
    return body


def art_digital():
    rect, clip = panel(AW, AH, SAGESF, (SAGE, 90, 240, 110))
    body = rect + clip
    body += g(150, 90, 1.5, phone())
    body += g(238, 150, 1.25, plant(CORAL, SAGE))
    body += sparkle(120, 80, 10, SUN)
    body += sparkle(300, 70, 7, CORAL)
    body += dot(320, 210, 5, SUN)
    # rustige 'pauze'-streepjes i.p.v. tekst (fonts erven niet in img-SVG)
    body += f'<g stroke="{SAGE}" stroke-width="5" stroke-linecap="round" opacity="0.9">'
    body += '<line x1="236" y1="64" x2="252" y2="64"/><line x1="240" y1="78" x2="256" y2="78"/>'
    body += '</g>'
    return body


def art_gratitude():
    rect, clip = panel(AW, AH, BLUSH, (BLUSH2, 320, 240, 110))
    body = rect + clip
    body += g(118, 120, 1.45, journal(CORAL))
    body += g(248, 150, 1.0, pen(SUN))
    body += heart(322, 86, 16, CORAL)
    body += heart(352, 120, 10, SUN)
    body += sparkle(80, 80, 9, SUN)
    body += dot(96, 244, 4.5, CORAL)
    body += dot(300, 238, 4, SAGE)
    return body


def art_habits():
    rect, clip = panel(AW, AH, SAGESF, (SAGE, 318, 72, 90))
    body = rect + clip
    body += sun(330, 78, 20, SUN, rays=9)
    # drie groeistadia
    body += g(70, 150, 0.7, plant(CORAL, SAGE))
    body += g(165, 130, 0.95, plant(CORALDP, SAGE))
    body += g(270, 110, 1.2, plant(CORAL, SAGE))
    body += dot(120, 250, 4, SUN)
    body += dot(225, 250, 4, CORAL)
    body += sparkle(60, 80, 8, CORAL)
    return body


def art_hygge():
    rect, clip = panel(AW, AH, BLUSH, (BLUSH2, 96, 96, 92))
    body = rect + clip
    body += g(118, 96, 1.25, armchair(CORAL))
    body += g(282, 120, 1.05, candle(BLUSH2))
    body += g(300, 196, 0.7, plant(SAGE, SAGE))
    body += sun(70, 74, 16, SUN, rays=8)
    body += heart(330, 86, 11, CORAL)
    body += dot(150, 256, 4, SAGE)
    return body


def art_declutter():
    rect, clip = panel(AW, AH, SKYSF, (SKY, 300, 230, 110))
    body = rect + clip
    body += g(96, 120, 1.15, basket(SKY))
    body += g(232, 150, 0.95, basket(CORAL))
    body += g(286, 96, 0.55, plant(SAGE, SAGE))
    body += sparkle(120, 86, 10, SUN)
    body += sparkle(330, 150, 7, CORAL)
    body += dot(86, 246, 4, CORAL)
    return body


def art_selfcare():
    rect, clip = panel(AW, AH, SKYSF, (SUN, 320, 64, 90))
    body = rect + clip
    body += sun(78, 74, 22, SUN, rays=9)
    body += g(160, 150, 1.45, glass_lemonade())
    body += leaf(300, 210, 26, SAGE, 20)
    body += leaf(330, 220, 22, SAGE, -30)
    body += sparkle(120, 90, 9, CORAL)
    body += heart(320, 110, 12, CORAL)
    body += dot(100, 250, 4, SUNDEEP)
    return body


def art_evening():
    rect, clip = panel(AW, AH, "#DFE3EE", ("#CBD2E6", 90, 80, 100))
    body = rect + clip
    body += g(250, 40, 1.0, moon())
    # sterren
    for x, y, s in [(120, 70, 8), (320, 150, 6), (90, 150, 5), (300, 60, 5)]:
        body += sparkle(x, y, s, "#F6E4B0")
    body += g(150, 150, 1.5, mug(PAPER, "#7E5A8E") + steam(42, 22, INKSOFT))
    body += g(300, 196, 0.7, candle(BLUSH2))
    body += dot(180, 256, 3.6, "#F6E4B0")
    return body


# ============================================================
#  HERO-ILLUSTRATIE (520 x 470)
# ============================================================
def hero_art():
    W, H = 520, 470
    rect, clip = panel(W, H, BLUSH2, (SUN, 410, 110, 150))
    body = rect + clip
    # grote zon
    body += sun(120, 110, 40, SUN, rays=11, ray_len=26)
    # mok groot
    body += g(70, 250, 2.1, mug(PAPER, "#8B5A38") + steam(42, 22, INKSOFT))
    # open dagboek + pen
    body += g(250, 250, 1.7, journal(CORAL))
    body += g(430, 286, 1.35, pen(SUN))
    # plant
    body += g(372, 150, 1.45, plant(SAGE, SAGE))
    # doodles
    body += heart(150, 360, 18, CORAL)
    body += heart(470, 130, 14, SUN)
    body += sparkle(300, 120, 12, CORAL)
    body += sparkle(60, 380, 10, SUN)
    body += dot(220, 420, 6, SAGE)
    body += dot(480, 360, 5, CORAL)
    body += dot(40, 180, 5, SUNDEEP)
    return svg(W, H, body, f"0 0 {W} {H}")


# ============================================================
#  CATEGORIE-ICONEN (lijnstijl, 48 x 48)
# ============================================================
def icon_wrap(inner, stroke=INK):
    return svg(48, 48, f'<g stroke="{stroke}" stroke-width="3" fill="none">{inner}</g>', "0 0 48 48")


def icon_mindful():
    # zon
    import math
    s = f'<circle cx="24" cy="24" r="8" fill="{SUN}" stroke="{INK}"/>'
    for i in range(8):
        a = math.pi * 2 / 8 * i
        s += (f'<line x1="{24+math.cos(a)*13:.1f}" y1="{24+math.sin(a)*13:.1f}" '
              f'x2="{24+math.cos(a)*18:.1f}" y2="{24+math.sin(a)*18:.1f}"/>')
    return icon_wrap(s)


def icon_growth():
    s = (f'<path d="M24,40 V20" />'
         f'<path d="M24,22 C16,22 13,15 13,11 C20,11 24,16 24,22 Z" fill="{SAGE}"/>'
         f'<path d="M24,26 C32,26 36,19 36,15 C29,15 24,20 24,26 Z" fill="{SAGE}"/>'
         f'<path d="M17,40 H31" />')
    return icon_wrap(s)


def icon_home():
    s = (f'<path d="M9,23 L24,10 L39,23" />'
         f'<path d="M13,21 V39 H35 V21" fill="{BLUSH}"/>'
         f'<path d="M20,39 V29 H28 V39" fill="{CORAL}"/>')
    return icon_wrap(s)


def icon_selfcare():
    s = (f'<path d="M24,38 C8,27 12,13 21,15 C23,15.5 24,17 24,18 '
         f'C24,17 25,15.5 27,15 C36,13 40,27 24,38 Z" fill="{CORAL}"/>')
    return icon_wrap(s)


# ============================================================
#  LOGO-MARK (zon + glimlach, 40 x 40)
# ============================================================
def logo_mark():
    import math
    body = [f'<circle cx="20" cy="20" r="11.5" fill="{SUN}"/>']
    for i in range(8):
        a = math.pi * 2 / 8 * i + 0.39
        body.append(f'<line x1="{20+math.cos(a)*14:.1f}" y1="{20+math.sin(a)*14:.1f}" '
                    f'x2="{20+math.cos(a)*18.5:.1f}" y2="{20+math.sin(a)*18.5:.1f}" '
                    f'stroke="{SUN}" stroke-width="2.6"/>')
    # glimlachje
    body.append(f'<circle cx="16" cy="18" r="1.7" fill="{INK}"/>')
    body.append(f'<circle cx="24" cy="18" r="1.7" fill="{INK}"/>')
    body.append(f'<path d="M14.5,22.5 Q20,27 25.5,22.5" stroke="{INK}" stroke-width="2.2" fill="none" stroke-linecap="round"/>')
    return svg(40, 40, "".join(body), "0 0 40 40")


# ============================================================
#  SCHRIJFSTER-AVATAR (memoji-stijl, 420 x 420)
# ============================================================
def avatar():
    W = 420
    parts = []
    # achtergrond cirkel
    parts.append(f'<circle cx="210" cy="210" r="206" fill="{BLUSH2}"/>')
    parts.append(f'<circle cx="210" cy="210" r="206" fill="none" stroke="{CORAL}" stroke-width="4" opacity="0.5"/>')
    # losse doodles in de achtergrond
    parts.append(sun(70, 80, 16, SUN, rays=8))
    parts.append(heart(350, 96, 14, CORAL))
    parts.append(sparkle(360, 300, 10, SUN))
    parts.append(dot(64, 320, 6, SAGE))

    # --- figuur (clip op cirkel zodat schouders netjes aflopen) ---
    fig = []
    # achterhaar
    fig.append(f'<path d="M104,196 C100,118 150,74 210,74 C270,74 320,118 316,196 '
               f'C314,232 312,260 300,300 L120,300 C108,260 106,232 104,196 Z" fill="{HAIR}"/>')
    # nek
    fig.append(f'<path d="M188,250 h44 v34 q-22,12 -44,0 z" fill="{SKINSH}"/>')
    # schouders / trui
    fig.append(f'<path d="M120,420 C120,338 162,300 210,300 C258,300 300,338 300,420 Z" fill="{CORAL}"/>')
    fig.append(f'<path d="M210,300 C232,302 250,312 262,330 L210,344 L158,330 C170,312 188,302 210,300 Z" '
               f'fill="{PAPER}" opacity="0.85"/>')  # kraagje
    # gezicht
    fig.append(f'<ellipse cx="210" cy="186" rx="74" ry="84" fill="{SKIN}"/>')
    # oren
    fig.append(f'<circle cx="138" cy="190" r="13" fill="{SKIN}"/>')
    fig.append(f'<circle cx="282" cy="190" r="13" fill="{SKIN}"/>')
    fig.append(f'<circle cx="282" cy="192" r="4.5" fill="{SUN}"/>')  # oorbel
    # voorhaar (pony + sluik langs gezicht)
    fig.append(f'<path d="M136,196 C128,120 158,78 210,78 C262,78 292,120 284,196 '
               f'C282,168 268,150 250,150 C236,150 232,140 210,140 C188,140 184,150 170,150 '
               f'C152,150 138,168 136,196 Z" fill="{HAIR}"/>')
    fig.append(f'<path d="M210,78 C176,80 150,104 144,150 C158,120 182,112 210,112 Z" fill="{HAIRHI}" opacity="0.55"/>')
    # bloemetje in het haar
    flower = []
    import math
    for i in range(5):
        a = math.pi * 2 / 5 * i
        flower.append(f'<ellipse cx="{162+math.cos(a)*11:.1f}" cy="{120+math.sin(a)*11:.1f}" rx="7" ry="10" '
                      f'fill="{SUN}" transform="rotate({i*72} {162+math.cos(a)*11:.1f} {120+math.sin(a)*11:.1f})"/>')
    fig.append("".join(flower) + f'<circle cx="162" cy="120" r="6" fill="{CORALDP}"/>')
    # wenkbrauwen
    fig.append(f'<path d="M170,162 q14,-7 26,-1" stroke="{INK}" stroke-width="4" fill="none" stroke-linecap="round"/>')
    fig.append(f'<path d="M224,161 q12,-6 26,1" stroke="{INK}" stroke-width="4" fill="none" stroke-linecap="round"/>')
    # ogen
    for ex in (183, 237):
        fig.append(f'<ellipse cx="{ex}" cy="184" rx="6.5" ry="8.5" fill="{INK}"/>')
        fig.append(f'<circle cx="{ex+2.2}" cy="181" r="2.2" fill="#fff"/>')
    # blosjes
    fig.append(f'<ellipse cx="166" cy="208" rx="14" ry="9" fill="{CORAL}" opacity="0.45"/>')
    fig.append(f'<ellipse cx="254" cy="208" rx="14" ry="9" fill="{CORAL}" opacity="0.45"/>')
    # neusje
    fig.append(f'<path d="M210,194 q4,8 -3,12" stroke="{SKINSH}" stroke-width="3.4" fill="none" stroke-linecap="round"/>')
    # sproetjes
    for fx, fy in [(180, 206), (188, 212), (196, 208), (224, 208), (232, 212), (240, 206)]:
        fig.append(f'<circle cx="{fx}" cy="{fy}" r="1.6" fill="{SKINSH}"/>')
    # glimlach
    fig.append(f'<path d="M186,224 Q210,246 234,224" stroke="{INK}" stroke-width="4.2" fill="none" stroke-linecap="round"/>')
    fig.append(f'<path d="M192,228 Q210,240 228,228 Q210,235 192,228 Z" fill="{CORALDP}"/>')

    clip = (f'<clipPath id="ava"><circle cx="210" cy="210" r="206"/></clipPath>')
    parts.append(f'<defs>{clip}</defs>')
    parts.append(f'<g clip-path="url(#ava)">{"".join(fig)}</g>')
    return svg(W, W, "".join(parts), f"0 0 {W} {W}")


# ============================================================
#  OG-IMAGE (1200 x 630) en favicon
# ============================================================
def og_image():
    W, H = 1200, 630
    b = [f'<rect width="{W}" height="{H}" fill="{CREAM}"/>']
    b.append(f'<rect width="{W}" height="{H}" fill="none"/>')
    # zachte hoekgloed
    b.append(f'<circle cx="120" cy="80" r="220" fill="{SUN}" opacity="0.16"/>')
    b.append(f'<circle cx="1120" cy="560" r="260" fill="{CORAL}" opacity="0.16"/>')
    # logo-mark groot links
    b.append(g(150, 250, 4.0, logo_mark_inner()))
    # tekst
    b.append(f'<text x="330" y="290" font-family="Fraunces, Georgia, serif" font-weight="600" '
             f'font-size="92" fill="{INK}">The Happy Days</text>')
    b.append(f'<text x="334" y="360" font-family="Mulish, sans-serif" font-weight="700" '
             f'font-size="34" fill="{INKSOFT}">Een Nederlandse leefstijlblog over alledaags geluk</text>')
    # zon + doodles
    b.append(sun(1040, 150, 50, SUN, rays=11, ray_len=30))
    b.append(heart(980, 470, 26, CORAL))
    b.append(sparkle(900, 120, 18, CORAL))
    b.append(dot(360, 430, 9, SAGE))
    # handgeschreven kicker
    b.append(f'<text x="332" y="470" font-family="Caveat, cursive" font-weight="700" '
             f'font-size="62" fill="{CORALDP}" transform="rotate(-3 332 470)">fijne dagen, elke dag</text>')
    return svg(W, H, "".join(b), f"0 0 {W} {H}")


def logo_mark_inner():
    """Logo zonder eigen svg-wrapper, voor hergebruik."""
    import math
    body = [f'<circle cx="20" cy="20" r="11.5" fill="{SUN}"/>']
    for i in range(8):
        a = math.pi * 2 / 8 * i + 0.39
        body.append(f'<line x1="{20+math.cos(a)*14:.1f}" y1="{20+math.sin(a)*14:.1f}" '
                    f'x2="{20+math.cos(a)*18.5:.1f}" y2="{20+math.sin(a)*18.5:.1f}" '
                    f'stroke="{SUN}" stroke-width="2.6"/>')
    body.append(f'<circle cx="16" cy="18" r="1.7" fill="{INK}"/>')
    body.append(f'<circle cx="24" cy="18" r="1.7" fill="{INK}"/>')
    body.append(f'<path d="M14.5,22.5 Q20,27 25.5,22.5" stroke="{INK}" stroke-width="2.2" fill="none" stroke-linecap="round"/>')
    return "".join(body)


def favicon():
    import math
    body = [f'<rect width="64" height="64" rx="16" fill="{CORAL}"/>']
    body.append(f'<circle cx="32" cy="32" r="15" fill="{SUN}"/>')
    for i in range(8):
        a = math.pi * 2 / 8 * i + 0.39
        body.append(f'<line x1="{32+math.cos(a)*19:.1f}" y1="{32+math.sin(a)*19:.1f}" '
                    f'x2="{32+math.cos(a)*25:.1f}" y2="{32+math.sin(a)*25:.1f}" '
                    f'stroke="{SUN}" stroke-width="4" stroke-linecap="round"/>')
    body.append(f'<circle cx="27" cy="30" r="2.4" fill="{INK}"/>')
    body.append(f'<circle cx="37" cy="30" r="2.4" fill="{INK}"/>')
    body.append(f'<path d="M25,35 Q32,42 39,35" stroke="{INK}" stroke-width="3" fill="none" stroke-linecap="round"/>')
    return svg(64, 64, "".join(body), "0 0 64 64")


# ============================================================
#  Schrijf alle bestanden
# ============================================================
def main():
    # artikel-illustraties
    arts = {
        "art-ochtendroutine.svg": art_morning_v2,
        "art-digitale-rust.svg": art_digital,
        "art-dankbaarheid.svg": art_gratitude,
        "art-gewoontes.svg": art_habits,
        "art-hygge.svg": art_hygge,
        "art-opruimen.svg": art_declutter,
        "art-zelfzorg.svg": art_selfcare,
        "art-avondroutine.svg": art_evening,
    }
    for name, fn in arts.items():
        write(name, AW, AH, fn(), title=name.replace("art-", "").replace(".svg", "").replace("-", " "))

    # hero
    with open(os.path.join(OUT, "hero.svg"), "w", encoding="utf-8") as f:
        f.write(hero_art())

    # categorie-iconen
    icons = {
        "ico-mindful.svg": icon_mindful,
        "ico-groei.svg": icon_growth,
        "ico-thuis.svg": icon_home,
        "ico-zelfzorg.svg": icon_selfcare,
    }
    for name, fn in icons.items():
        with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
            f.write(fn())

    # logo, avatar, favicon, og
    with open(os.path.join(OUT, "logo-mark.svg"), "w", encoding="utf-8") as f:
        f.write(logo_mark())
    with open(os.path.join(OUT, "avatar-saar.svg"), "w", encoding="utf-8") as f:
        f.write(avatar())
    with open(os.path.join(OUT, "favicon.svg"), "w", encoding="utf-8") as f:
        f.write(favicon())
    with open(os.path.join(OUT, "og-image.svg"), "w", encoding="utf-8") as f:
        f.write(og_image())

    # squiggle (klein, voor eventueel inline gebruik als bestand)
    with open(os.path.join(OUT, "squiggle.svg"), "w", encoding="utf-8") as f:
        f.write(squiggle_path(120, SUN, 5))

    print("SVG-bestanden geschreven naar", OUT)
    for n in sorted(os.listdir(OUT)):
        print("  ", n)


if __name__ == "__main__":
    main()
