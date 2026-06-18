# The Happy Days

Een statische Nederlandse leefstijlblog voor **thehappydays.nl**, klaar voor GitHub Pages.
Alles is zelf opgebouwd: geen thema, geen build-tooling nodig om te publiceren, geen stockfoto's
(alle visuals zijn eigen SVG-tekeningen) en geen tracking.

---

## 🚀 Publiceren op GitHub Pages

1. Maak een nieuwe repository en plaats **de volledige inhoud van deze map** in de root van de repo
   (dus `index.html`, de mappen `assets/`, `over/`, `nieuws/` enz. komen direct in de root te staan).
2. Push naar de branch `main`.
3. Ga in de repo naar **Settings → Pages** en kies:
   - **Source:** *Deploy from a branch*
   - **Branch:** `main` / `/ (root)`
4. Het bestand **`CNAME`** zit er al in en bevat `thehappydays.nl`. Stel bij je domeinregistrar de DNS in:
   - **A-records** voor het hoofddomein (`@`) naar de GitHub Pages IP's:
     `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`
   - (optioneel) een **CNAME** voor `www` naar `<jouw-gebruikersnaam>.github.io`
5. Zet in **Settings → Pages** *Enforce HTTPS* aan zodra het certificaat klaar is.

> De links in de site zijn **root-absoluut** (`/over/`, `/assets/...`). Dat is precies goed voor een
> eigen domein. Wil je lokaal previewen? Start dan even een servertje in deze map in plaats van de
> HTML-bestanden direct te openen:
> ```bash
> python3 -m http.server 8000   # open daarna http://localhost:8000
> ```

---

## 📁 Structuur

```
.
├── index.html              Homepage
├── over/                   Over het platform
├── schrijfster/            Persona: Saar (met getekende "memoji")
├── partners/               Linkpartners (nu 2 toonaangevende NL-blogs)
├── nieuws/                 Blogoverzicht + 8 artikelen (elk een eigen map)
├── categorie/              4 themapagina's (mindful, groei, thuis & sfeer, zelfzorg)
├── contact/                Contact (mailto, geen formulier)
├── privacy/  cookies/      Juridische pagina's (gelinkt in de footer)
├── 404.html                Nette foutpagina
├── robots.txt  sitemap.xml SEO-basis
├── CNAME  .nojekyll        GitHub Pages-config
├── assets/
│   ├── css/style.css       Volledige huisstijl
│   ├── js/main.js          Menu, dropdown, cookiemelding (vanilla JS)
│   ├── fonts/              Self-hosted fonts (Fraunces, Mulish, Caveat) – privacyvriendelijk
│   └── img/                Alle eigen SVG-illustraties + iconen + OG-afbeeldingen
└── tools/                  (optioneel) Python-generator om de site te (her)bouwen
```

De map **`tools/`** wordt niet gebruikt door de gepubliceerde site en mag je laten staan of verwijderen.

---

## ✍️ Een nieuw artikel toevoegen

1. Open `tools/content.py` en voeg een blok toe aan de lijst `ARTICLES`
   (kopieer een bestaand blok; vul `slug`, `title`, `cat`, `date`, `excerpt`, `img` en `body` in).
2. Maak eventueel een passende illustratie aan in `tools/make_art.py`, of hergebruik een bestaande
   uit `assets/img/`.
3. Regenereer de site vanuit de **repo-root**:
   ```bash
   python3 tools/make_og.py    # social-share kaart voor het artikel
   python3 tools/build.py      # alle HTML + sitemap opnieuw genereren
   ```

Voor het opnieuw genereren van de afbeeldingen zijn twee Python-pakketten nodig
(zie `tools/requirements.txt`): `cairosvg` en `pillow`. Voor alleen `build.py` heb je niets extra's nodig.

---

## 🔧 Nog even doen

- **Social media-links:** in `tools/content.py` staan `instagram` en `pinterest` nu op `#`.
  Vervang die door je echte profiel-URL's en draai `tools/build.py` opnieuw
  (of pas ze handmatig aan in de HTML).

---

## 📝 Inhoud & rechten

Alle teksten en illustraties zijn origineel voor The Happy Days gemaakt — geen overgenomen
content, geen stockmateriaal. De gebruikte lettertypen (Fraunces, Mulish, Caveat) staan onder de
SIL Open Font License en worden vanaf je eigen server geladen.
