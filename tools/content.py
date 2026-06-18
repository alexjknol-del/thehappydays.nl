# -*- coding: utf-8 -*-
"""Inhoud & configuratie voor The Happy Days (gedeeld door build.py en make_og.py)."""

SITE = {
    "name": "The Happy Days",
    "domain": "thehappydays.nl",
    "url": "https://thehappydays.nl",
    "email": "info@thehappydays.nl",
    "tagline": "Een Nederlandse leefstijlblog over alledaags geluk",
    "description": ("The Happy Days is een Nederlandse leefstijlblog over rust, aandacht en "
                    "alledaags geluk — met eerlijke verhalen en praktische tips voor fijne, gewone dagen."),
    "author": "Saar Brouwer",
    "author_role": "Oprichter & schrijfster",
    "founded": "2026",
    "city": "Haarlem",
    # Vervang '#' door je echte profiel-URL zodra je accounts hebt.
    "instagram": "#",
    "pinterest": "#",
}

# Hoofdmenu — structuur + leefstijlthema's (Nieuws klapt de thema's uit)
NAV = [
    {"label": "Home", "href": "/"},
    {"label": "Over", "href": "/over/"},
    {"label": "Nieuws", "href": "/nieuws/", "sub": True},
    {"label": "Schrijfster", "href": "/schrijfster/"},
    {"label": "Partners", "href": "/partners/"},
    {"label": "Contact", "href": "/contact/"},
]

CATS = [
    {"slug": "mindful-leven", "name": "Mindful leven", "icon": "ico-mindful.svg",
     "dot": "#9FB291", "tint": "#E4EADD",
     "desc": "Rust, aandacht en minder ruis in je dag.",
     "intro": "Mindful leven gaat niet over uren mediteren, maar over aandacht in de gewone momenten. "
              "Hier vind je rustige routines en manieren om de drukte even zachter te zetten."},
    {"slug": "persoonlijke-groei", "name": "Persoonlijke groei", "icon": "ico-groei.svg",
     "dot": "#E98B6F", "tint": "#FCEAE2",
     "desc": "Kleine stappen naar een leven dat bij je past.",
     "intro": "Groeien hoeft geen grote ommezwaai te zijn. Met kleine, haalbare gewoontes kom je verder "
              "dan met goede voornemens die te groot zijn. Lees mee over stap voor stap vooruit."},
    {"slug": "thuis-en-sfeer", "name": "Thuis & sfeer", "icon": "ico-thuis.svg",
     "dot": "#F2B544", "tint": "#FCEFCB",
     "desc": "Een huis waar je tot rust komt.",
     "intro": "Je huis mag een plek zijn waar je opademt. In deze rubriek draait het om warmte, "
              "gezelligheid en een opgeruimde plek die rust geeft — zonder dat het perfect hoeft te zijn."},
    {"slug": "zelfzorg", "name": "Zelfzorg", "icon": "ico-zelfzorg.svg",
     "dot": "#E5879E", "tint": "#FBE3E8",
     "desc": "Goed voor jezelf zorgen, met aandacht.",
     "intro": "Zelfzorg is geen luxe, maar onderhoud. Kleine momenten voor jezelf maken een groot verschil "
              "in hoe je je voelt. Hier lees je hoe je vriendelijk voor jezelf blijft, ook op drukke dagen."},
]


def cat(slug):
    return next(c for c in CATS if c["slug"] == slug)


# ============================================================
#  ARTIKELEN
# ============================================================
ARTICLES = [
    {
        "slug": "rustige-ochtendroutine-kleine-gewoontes",
        "title": "Een rustige ochtendroutine: 7 kleine gewoontes voor een fijne start",
        "cat": "mindful-leven",
        "date": "2026-06-12", "date_nl": "12 juni 2026", "read": 5,
        "img": "art-ochtendroutine.svg",
        "excerpt": "Hoe je je dag begint, kleurt vaak de rest. Met deze zeven kleine ochtendgewoontes start je rustiger — zonder dat je een uur eerder hoeft op te staan.",
        "body": """
<p>Hoe je je ochtend begint, zet vaak de toon voor de rest van je dag. Begin je met haasten, je telefoon en een halfopgegeten boterham in de auto, dan voelt de dag al gejaagd voordat hij goed en wel begonnen is. Maar een rustige ochtend hoeft geen ingewikkeld ochtendritueel van twee uur te zijn. Het zit 'm juist in een paar kleine gewoontes die je met aandacht doet.</p>
<p>Hieronder deel ik zeven kleine dingen die mijn ochtenden zachter maakten. Kies er eentje uit om mee te beginnen — niet alles tegelijk.</p>

<h2>1. Begin niet met je telefoon</h2>
<p>De verleiding is groot om als eerste je telefoon te pakken. Maar daarmee start je je dag met de prikkels en zorgen van de hele wereld, nog voor je goed wakker bent. Leg je telefoon 's avonds buiten handbereik en gun jezelf de eerste twintig minuten zonder scherm.</p>

<h2>2. Drink een glas water</h2>
<p>Na een nacht slapen is je lichaam toe aan vocht. Een glas water voordat je koffie of thee zet, is een klein gebaar van goede zorg. Zet het glas de avond ervoor al klaar, dan hoef je er 's ochtends niet over na te denken.</p>

<h2>3. Open de gordijnen en laat licht binnen</h2>
<p>Daglicht helpt je lichaam wakker te worden en zet je interne klok goed. Schuif de gordijnen open zodra je opstaat. Sta even bij het raam, kijk naar buiten en haal een paar keer rustig adem.</p>

<h2>4. Maak je bed op</h2>
<p>Een opgemaakt bed is een mini-overwinning waarmee je de dag begint. Het kost een minuut en geeft meteen een opgeruimd gevoel. En 's avonds stap je in een bed dat er fijn bij ligt.</p>

<blockquote><p>Een rustige ochtend is geen kwestie van vroeg opstaan, maar van met aandacht beginnen.</p></blockquote>

<h2>5. Beweeg even, hoe klein ook</h2>
<p>Je hoeft niet meteen te gaan hardlopen. Een paar minuten rekken, een korte wandeling om het blok of even de trap op en af brengt je lichaam zachtjes op gang. Beweging maakt je hoofd helderder dan welke koffie ook.</p>

<h2>6. Eet rustig je ontbijt</h2>
<p>Probeer je ontbijt niet staand of onderweg naar binnen te werken, maar ga er even voor zitten. Proef wat je eet. Tien minuten echt pauze maken aan het begin van de dag voelt als een klein cadeautje aan jezelf.</p>

<h2>7. Bedenk één ding waar je naar uitkijkt</h2>
<p>Voordat de dag op stoom komt: bedenk één klein moment waar je je op kunt verheugen. Een kop thee in de zon, een wandeling tussen de middag, een appje naar een vriendin. Iets om naar uit te kijken maakt zelfs een drukke dag lichter.</p>

<div class="callout"><p><strong>Begin klein.</strong> Pak niet alle zeven gewoontes tegelijk op — dan wordt je rustige ochtend juist een opgave. Kies er deze week eentje uit. Als die vanzelf gaat, voeg je de volgende toe.</p></div>

<p>Een fijne dag begint vaak met een fijne ochtend. En een fijne ochtend begint met aandacht voor de kleine dingen. Welke gewoonte ga jij morgen proberen?</p>
""",
    },
    {
        "slug": "minder-schermtijd-meer-aandacht-digitale-rust",
        "title": "Minder schermtijd, meer aandacht: zo vind je digitale rust",
        "cat": "mindful-leven",
        "date": "2026-06-09", "date_nl": "9 juni 2026", "read": 5,
        "img": "art-digitale-rust.svg",
        "excerpt": "Constant online zijn is vermoeiender dan we denken. Met een paar eenvoudige grenzen geef je je hoofd weer ruimte om te ademen.",
        "body": """
<p>We pakken onze telefoon gemiddeld tientallen keren per dag, vaak zonder er erg in te hebben. In de rij, op de bank, zelfs op het moment dat we eigenlijk even niets hoeven te doen. En hoewel je scherm je verbindt met van alles, kost dat constante stroompje informatie meer energie dan je merkt. Digitale rust is geen kwestie van je telefoon wegdoen, maar van bewuster kiezen wanneer je wél en niet online bent.</p>

<h2>Waarom eindeloos scrollen zo moe maakt</h2>
<p>Elke melding, elk nieuwtje en elk filmpje vraagt een klein beetje van je aandacht. Doe je dat de hele dag door, dan krijgt je hoofd nooit echt rust. Je voelt je drukker dan je bent, en concentreren wordt lastiger. Het mooie nieuws: je hoeft niet radicaal te minderen om verschil te merken. Een paar bewuste grenzen zijn vaak al genoeg.</p>

<h2>Maak schermvrije zones in huis</h2>
<p>Spreek met jezelf af dat sommige plekken telefoonvrij zijn. De eettafel bijvoorbeeld, of de slaapkamer. Door je telefoon niet mee naar bed te nemen, slaap je beter én begin je je ochtend rustiger. Leg een oplader op een vaste plek buiten de slaapkamer, dan wordt het vanzelf een gewoonte.</p>

<h2>Zet je meldingen op dieet</h2>
<p>De meeste meldingen zijn niet urgent. Ze onderbreken je alleen maar. Loop eens door je instellingen en zet alle meldingen uit die niet echt nodig zijn. Wat overblijft, mag je bewust aandacht geven. Je bepaalt zelf wanneer je je apps opent, in plaats van dat ze jou de hele dag aantikken.</p>

<blockquote><p>Je telefoon is een prima gereedschap, maar een slechte baas.</p></blockquote>

<h2>Bouw één offline moment per dag in</h2>
<p>Kies een vast moment waarop je je telefoon bewust weglegt. Tijdens het avondeten, het laatste uur voor je gaat slapen, of een wandeling zonder oortjes. In het begin voelt het misschien onwennig, maar al snel merk je hoe fijn het is om even nergens bereikbaar te zijn.</p>

<h2>Maak het jezelf gemakkelijk</h2>
<ul>
<li><strong>Zet je scherm op grijstinten.</strong> Zonder felle kleuren is je telefoon een stuk minder verleidelijk.</li>
<li><strong>Ruim je beginscherm op.</strong> Haal de apps die je het meest opslokken van je startpagina af.</li>
<li><strong>Leg iets anders binnen handbereik.</strong> Een boek op de salontafel pak je sneller dan je denkt als je telefoon niet vlakbij ligt.</li>
</ul>

<div class="callout"><p><strong>Wees mild voor jezelf.</strong> Digitale rust is geen wedstrijd en je hoeft niet in één keer perfect te zijn. Eén schermvrij moment per dag is al een mooi begin.</p></div>

<p>Minder schermtijd betekent niet minder leven — eerder andersom. De momenten die je offline doorbrengt, beleef je vaak net wat intenser. En dat is precies waar fijne dagen van gemaakt zijn.</p>
""",
    },
    {
        "slug": "dankbaarheidsdagboek-bijhouden",
        "title": "Een dankbaarheidsdagboek bijhouden: zo verandert het je dag",
        "cat": "persoonlijke-groei",
        "date": "2026-06-05", "date_nl": "5 juni 2026", "read": 4,
        "img": "art-dankbaarheid.svg",
        "excerpt": "Elke dag drie dingen opschrijven waar je dankbaar voor bent klinkt simpel — en juist die eenvoud maakt het zo krachtig.",
        "body": """
<p>Sommige gewoontes zijn zo simpel dat je je afvraagt of ze wel werken. Een dankbaarheidsdagboek is daar een mooi voorbeeld van. Je schrijft elke dag een paar dingen op waar je dankbaar voor bent — meer is het niet. En toch is het een van de eenvoudigste manieren om wat positiever in je dag te staan.</p>

<h2>Wat dankbaarheid met je doet</h2>
<p>Ons hoofd heeft van nature de neiging om vooral te letten op wat er misgaat of nog moet gebeuren. Dat is handig om problemen op te lossen, maar minder fijn voor je humeur. Door bewust stil te staan bij wat er wél goed gaat, train je je aandacht om de fijne dingen vaker op te merken. Niet omdat de moeilijke dingen verdwijnen, maar omdat je ze niet langer als enige ziet.</p>

<h2>Zo begin je</h2>
<p>Je hebt er weinig voor nodig: een schriftje en een paar minuten. Schrijf elke dag drie dingen op waar je dankbaar voor bent. Dat mogen grote dingen zijn, maar juist de kleine werken vaak het best.</p>
<ul>
<li>De eerste kop koffie van de dag.</li>
<li>Een onverwacht berichtje van een vriend.</li>
<li>Het zonnetje dat door het raam scheen.</li>
</ul>

<h2>Wees zo concreet mogelijk</h2>
<p>"Mijn gezin" is mooi, maar "dat mijn dochter vanmorgen spontaan een grapje maakte" raakt je net wat meer. Hoe specifieker je opschrijft, hoe sterker je het moment opnieuw voelt. Schrijf daarom niet alleen wát, maar af en toe ook waaróm je er dankbaar voor bent.</p>

<blockquote><p>Dankbaarheid verandert niet wat je hebt, maar hoe je ernaar kijkt.</p></blockquote>

<h2>Maak er een vast moment van</h2>
<p>Koppel het schrijven aan iets wat je toch al doet, dan vergeet je het minder snel. Veel mensen vinden de avond fijn: vlak voor het slapengaan terugkijken op de dag is een rustige manier om af te sluiten. Voel je je 's ochtends frisser? Begin dan juist de dag ermee.</p>

<h2>Vastgelopen? Gebruik een vraag</h2>
<p>Op sommige dagen lukt het niet zo makkelijk. Een klein zetje helpt dan:</p>
<ul>
<li>Wie heeft me vandaag geholpen of aan het lachen gemaakt?</li>
<li>Wat ging er beter dan ik had verwacht?</li>
<li>Welk klein moment wil ik onthouden?</li>
</ul>

<div class="callout"><p><strong>Geen perfectie nodig.</strong> Sla je een dag over? Geen ramp. Een dankbaarheidsdagboek is geen verplichting maar een cadeautje aan jezelf. Pak het de volgende dag gewoon weer op.</p></div>

<p>Geef het een week of twee de tijd. Grote kans dat je jezelf vanzelf vaker betrapt op het opmerken van fijne dingen — ook op momenten dat je je schriftje er niet bij hebt. En dat is precies het idee.</p>
""",
    },
    {
        "slug": "kleine-gewoontes-nieuwe-routine-opbouwen",
        "title": "Kleine gewoontes, groot verschil: zo bouw je een nieuwe routine op",
        "cat": "persoonlijke-groei",
        "date": "2026-05-28", "date_nl": "28 mei 2026", "read": 5,
        "img": "art-gewoontes.svg",
        "excerpt": "Nieuwe gewoontes mislukken niet omdat we lui zijn, maar omdat we te groot beginnen. Zo maak je verandering juist makkelijk.",
        "body": """
<p>We kennen het allemaal: vol goede moed beginnen we aan een nieuwe gewoonte, en na twee weken is het stilletjes verwaterd. Dat ligt zelden aan een gebrek aan wilskracht. Veel vaker beginnen we simpelweg te groot. De truc om een gewoonte te laten beklijven is niet meer discipline, maar een slimmer begin.</p>

<h2>Waarom kleine gewoontes blijven plakken</h2>
<p>Een gewoonte die maar twee minuten kost, kun je bijna niet overslaan. Geen tijd of zin als excuus, want twee minuten heb je altijd. En juist door klein te beginnen, bouw je iets veel waardevollers op: het gevoel dat je iemand bent die zich aan z'n afspraken houdt. Dat vertrouwen is de echte motor onder elke verandering.</p>

<h2>Knoop het vast aan iets wat je al doet</h2>
<p>De makkelijkste manier om een gewoonte te onthouden, is hem koppelen aan iets wat al vastligt in je dag. Dat heet 'habit stacking':</p>
<ul>
<li>Na het tandenpoetsen doe ik twee minuten rekoefeningen.</li>
<li>Terwijl de koffie doorloopt, schrijf ik drie dingen op waar ik dankbaar voor ben.</li>
<li>Zodra ik thuiskom, leg ik mijn telefoon op een vaste plek.</li>
</ul>
<p>Je bestaande routine wordt zo het geheugensteuntje voor de nieuwe gewoonte.</p>

<h2>Maak het belachelijk makkelijk</h2>
<p>Wil je meer lezen? Begin met één bladzijde. Meer bewegen? Begin met de schoenen aandoen. Het doel is niet om groots uit te pakken, maar om de drempel zó laag te maken dat beginnen vanzelfsprekend wordt. Eenmaal bezig doe je vaak vanzelf wat meer — maar dat hoeft niet.</p>

<blockquote><p>Het gaat er niet om wat je één keer doet, maar om wat je elke dag een beetje doet.</p></blockquote>

<h2>Houd het zichtbaar bij</h2>
<p>Een streepje op de kalender, een vinkje in een schriftje: het zien van je reeks geeft een verrassend goed gevoel en motiveert om door te gaan. Mis je een dag? Probeer dan vooral niet twee keer achter elkaar over te slaan. Eén keer missen is een uitzondering, twee keer wordt het nieuwe patroon.</p>

<h2>Wees geduldig met jezelf</h2>
<p>Een nieuwe gewoonte voelt in het begin onwennig en dat hoort erbij. Het duurt even voordat iets echt vanzelf gaat. Verwacht geen wonderen in een week, maar kijk eens terug na een maand. De optelsom van al die kleine dagen verbaast je waarschijnlijk.</p>

<div class="callout"><p><strong>Eén gewoonte tegelijk.</strong> De verleiding is groot om je hele leven in één keer om te gooien. Maar je maakt veel meer kans als je je op één kleine gewoonte richt en die echt vastzet voordat je de volgende toevoegt.</p></div>

<p>Grote veranderingen beginnen zelden groot. Ze beginnen met iets kleins, dat je zo vaak herhaalt dat het bij je gaat horen. Welke kleine gewoonte zou jij willen opbouwen?</p>
""",
    },
    {
        "slug": "hygge-in-huis-warm-en-gezellig",
        "title": "Hygge in huis: zo maak je het warm en gezellig",
        "cat": "thuis-en-sfeer",
        "date": "2026-05-22", "date_nl": "22 mei 2026", "read": 4,
        "img": "art-hygge.svg",
        "excerpt": "Het Deense 'hygge' draait om warmte, geborgenheid en samen genieten van kleine momenten. Zo breng je dat gevoel je eigen huis binnen.",
        "body": """
<p>De Denen staan al jaren bekend als een van de gelukkigste volkeren ter wereld, en één woord duikt in dat verband steeds weer op: <em>hygge</em>. Het laat zich lastig precies vertalen, maar het komt neer op een gevoel van warmte, geborgenheid en samen genieten van kleine momenten. Het mooie is: je hebt er geen Scandinavisch interieur voor nodig. Hygge zit vooral in sfeer en aandacht.</p>

<h2>Wat hygge eigenlijk is</h2>
<p>Hygge is geen stijl die je koopt, maar een gevoel dat je creëert. Denk aan een regenachtige zondag onder een dekentje met een kop thee en een goed boek. Of een avond met vrienden waarbij niemand op z'n telefoon kijkt. Het draait niet om perfectie, maar om je behaaglijk en op je gemak voelen.</p>

<h2>Zacht licht doet wonderen</h2>
<p>Niets bepaalt de sfeer in een kamer zo sterk als licht. Felle plafondlampen voelen al snel kil. Kies in de avond voor meerdere kleine lichtbronnen: een schemerlampje, een lichtslinger, en natuurlijk kaarsen. Dat warme, lage licht maakt een ruimte meteen knus.</p>

<h2>Omring je met zachte materialen</h2>
<p>Hygge is letterlijk om je heen te voelen. Een wollen plaid over de bank, een paar extra kussens, een zacht kleed onder je voeten. Stapel verschillende texturen op elkaar — het nodigt uit om lekker weg te kruipen en geeft een kamer direct iets warms.</p>

<blockquote><p>Hygge koop je niet, hygge maak je — met licht, warmte en aandacht.</p></blockquote>

<h2>Maak ruimte voor langzame momenten</h2>
<p>Sfeer is niet alleen wat je ziet, maar ook wat je doet. Hygge is een kop warme chocolademelk zonder haast, een spelletje aan tafel, of samen koken zonder dat het af hoeft te zijn op een bepaald tijdstip. Plan bewust momenten in waarop niets moet en je gewoon mag genieten.</p>

<h2>Richt een knus hoekje in</h2>
<p>Je hoeft niet je hele huis om te gooien. Kies één plekje uit en maak het extra behaaglijk: een fijne stoel bij het raam, een zacht kleed, een lampje en een stapel boeken binnen handbereik. Een vaste plek om tot rust te komen, nodigt vanzelf uit om dat ook echt te doen.</p>

<div class="callout"><p><strong>Sfeer boven spullen.</strong> Hygge gaat niet over nóg meer kopen. Vaak maakt het juist méér uit dat je het rustig houdt: een opgeruimde plek, zacht licht en de tijd om ervan te genieten.</p></div>

<p>Warmte en gezelligheid hoeven niet duur of ingewikkeld te zijn. Een kaarsje aan, een dekentje erbij en even nergens heen hoeven — soms is dat alles wat een avond fijn maakt.</p>
""",
    },
    {
        "slug": "opgeruimd-huis-rustig-hoofd-beginnen-met-opruimen",
        "title": "Een opgeruimd huis, een rustig hoofd: licht beginnen met opruimen",
        "cat": "thuis-en-sfeer",
        "date": "2026-05-16", "date_nl": "16 mei 2026", "read": 5,
        "img": "art-opruimen.svg",
        "excerpt": "Opruimen voelt vaak als een berg waar je niet aan durft te beginnen. Met deze rustige aanpak maak je het juist klein en behapbaar.",
        "body": """
<p>Een opgeruimd huis geeft een opgeruimd gevoel — dat klinkt logisch, en toch komt het er vaak niet van. De rommel groeit, de drempel om te beginnen wordt hoger, en op een gegeven moment voelt opruimen als een onmogelijke klus. Goed nieuws: je hoeft niet in één weekend je hele huis te kantelen. Klein en rustig beginnen werkt veel beter, en blijft ook nog eens langer hangen.</p>

<h2>Waarom rommel je hoofd vermoeit</h2>
<p>Alles wat rondslingert, vraagt ergens een klein beetje aandacht. Onbewust registreer je elke stapel post, elke volle stoel, elk ding dat 'nog ergens heen moet'. Bij elkaar opgeteld geeft dat een gevoel van onrust, zonder dat je precies de vinger erop kunt leggen. Opruimen is daarom niet alleen praktisch — het geeft je hoofd letterlijk wat lucht.</p>

<h2>Begin met één la</h2>
<p>De grootste fout is te groot beginnen. Je neemt je voor de hele zolder te doen, raakt halverwege ontmoedigd en stopt. Kies daarom iets kleins en afgebakends: één la, één plank, één hoekje van het aanrecht. Klaar binnen tien minuten, en met een resultaat dat je meteen ziet. Dat kleine succes geeft zin in de volgende.</p>

<h2>Geef alles een vaste plek</h2>
<p>Rommel ontstaat vaak doordat dingen geen eigen plek hebben. Als iets nergens 'thuishoort', blijft het rondzwerven. Bepaal voor de spullen die je het meest gebruikt een vaste plaats. Opruimen wordt dan een kwestie van even terugleggen, in plaats van elke keer opnieuw bedenken waar iets heen moet.</p>

<blockquote><p>Je hoeft niet alles in één keer op te ruimen. Je hoeft alleen ergens te beginnen.</p></blockquote>

<h2>Eén erbij, één eruit</h2>
<p>Wil je voorkomen dat de rommel zich weer opstapelt? Hanteer dan een eenvoudige regel: komt er iets nieuws binnen, dan mag er ook iets weg. Een nieuwe trui, een oude trui de deur uit. Zo blijft de hoeveelheid spullen vanzelf in balans, zonder grote opruimacties.</p>

<h2>Maak het jezelf aangenaam</h2>
<ul>
<li><strong>Zet een timer op tien minuten.</strong> Tien minuten opruimen voelt te doen, en vaak ga je daarna vanzelf nog even door.</li>
<li><strong>Zet muziek op.</strong> Met een fijn lijstje wordt opruimen ineens een stuk minder een klus.</li>
<li><strong>Houd één doos voor 'weg'.</strong> Twijfel je over iets? In de doos. Pak je het een maand niet, dan mag het echt weg.</li>
</ul>

<div class="callout"><p><strong>Klaar is nooit.</strong> Een huis raakt nu eenmaal weer rommelig, en dat is helemaal goed. Het doel is geen showroom, maar een plek waar jij je prettig voelt. Een beetje leven mag.</p></div>

<p>Begin vandaag met dat ene laatje. Grote kans dat het verrassend bevredigend is — en dat je morgen vanzelf zin hebt in de volgende.</p>
""",
    },
    {
        "slug": "zomerse-zelfzorg-kleine-momenten-voor-jezelf",
        "title": "Zomerse zelfzorg: kleine momenten voor jezelf",
        "cat": "zelfzorg",
        "date": "2026-06-02", "date_nl": "2 juni 2026", "read": 4,
        "img": "art-zelfzorg.svg",
        "excerpt": "Zelfzorg hoeft geen dure wellnessdag te zijn. In de zomer liggen de fijnste momenten voor het oprapen — als je ze maar even pakt.",
        "body": """
<p>Als de dagen langer worden en de zon vaker schijnt, komt er vanzelf iets luchtigs over ons. Toch vergeten we juist in drukke zomerweken weleens om goed voor onszelf te zorgen. Terwijl zelfzorg helemaal geen dure wellnessdag hoeft te zijn. Het zit 'm in de kleine momenten die je bewust voor jezelf neemt — en in de zomer liggen die voor het oprapen.</p>

<h2>Zelfzorg is geen luxe</h2>
<p>Soms voelt tijd voor jezelf nemen een beetje als egoïsme. Maar goed voor jezelf zorgen is geen luxe, het is onderhoud. Net zoals je telefoon af en toe moet opladen, heb jij momenten van rust nodig om opgeladen te blijven. En hoe beter jij in je vel zit, hoe meer je ook voor anderen kunt betekenen.</p>

<h2>Begin je dag buiten</h2>
<p>Een korte ochtendwandeling voor je aan de dag begint, doet wonderen. Het frisse licht, de buitenlucht en even bewegen voordat de drukte losbarst: je merkt het de hele dag. Geen tijd voor een wandeling? Drink je koffie dan eens buiten in de ochtendzon.</p>

<h2>Drink genoeg en eet wat lichter</h2>
<p>Met de warmte vergeten we makkelijk om genoeg te drinken. Zet 's ochtends een mooie kan water of thee klaar met wat schijfjes citroen of komkommer. En geniet van wat de zomer aan tafel brengt: vers fruit, frisse salades, dingen die je een licht en energiek gevoel geven.</p>

<blockquote><p>Goed voor jezelf zorgen is geen egoïsme, maar de basis om er ook voor anderen te kunnen zijn.</p></blockquote>

<h2>Geniet van de lange avonden</h2>
<p>De zomeravonden zijn er om van te genieten. Leg je telefoon weg en zit eens buiten tot de zon ondergaat. Een avondwandeling, een boek in de tuin of op het balkon, of gewoon even niets — die rustige avonden zijn balsem voor je hoofd.</p>

<h2>Plan een langzaam weekend</h2>
<p>Niet elk weekend hoeft volgepland te zijn met uitjes en afspraken. Plan er deze zomer bewust eentje in waarin niets moet. Slaap uit, ontbijt uitgebreid, doe waar je zin in hebt. Een leeg weekend is geen verloren tijd — het is precies wat je soms nodig hebt.</p>

<div class="callout"><p><strong>Klein telt ook.</strong> Zelfzorg hoeft geen uur te duren. Vijf minuten met je ogen dicht in de zon, een glas water met aandacht, even diep ademhalen — ook die kleine momenten laden je op.</p></div>

<p>De zomer is een uitnodiging om het wat rustiger aan te doen. Pak die uitnodiging aan, en gun jezelf de kleine momenten die een gewone dag een fijne dag maken.</p>
""",
    },
    {
        "slug": "fijne-avondroutine-betere-nachtrust",
        "title": "Een fijne avondroutine voor een betere nachtrust",
        "cat": "zelfzorg",
        "date": "2026-05-12", "date_nl": "12 mei 2026", "read": 5,
        "img": "art-avondroutine.svg",
        "excerpt": "Hoe je je avond afsluit, bepaalt hoe je slaapt. Met een rustig avondritueel kom je makkelijker tot rust — en word je uitgeruster wakker.",
        "body": """
<p>We denken vaak na over onze ochtendroutine, maar hoe je je avond doorbrengt is minstens zo belangrijk. Sterker nog: een goede nachtrust begint al uren voordat je je hoofd op het kussen legt. Met een rustig avondritueel geef je je lichaam en hoofd het signaal dat de dag erop zit — en val je makkelijker en dieper in slaap.</p>

<h2>Bouw de dag rustig af</h2>
<p>Je kunt niet van honderd naar nul in vijf minuten. Probeer het laatste uur van de dag bewust kalmer aan te doen. Dim het licht, zet drukke series of nieuws uit, en kies voor iets rustigs: lezen, een warme douche, of gewoon wat opruimen. Zo geef je jezelf de tijd om af te schakelen.</p>

<h2>Leg je telefoon op tijd weg</h2>
<p>Het felle, blauwe licht van schermen houdt je wakkerder dan je denkt, en het eindeloze scrollen houdt je hoofd actief. Spreek met jezelf af dat je je telefoon een half uur voor het slapen weglegt. Laad hem op buiten de slaapkamer, dan is de verleiding meteen weg.</p>

<h2>Maak er een klein ritueel van</h2>
<p>Een vast avondritueel werkt als een schakelaar voor je hoofd. Het hoeft niets ingewikkelds te zijn:</p>
<ul>
<li>Een kop kruidenthee zonder cafeïne.</li>
<li>Een paar minuten rustig rekken of ademhalen.</li>
<li>Drie dingen opschrijven die fijn waren vandaag.</li>
</ul>
<p>Doe je dit elke avond, dan gaat je lichaam het herkennen als 'tijd om tot rust te komen'.</p>

<blockquote><p>Een goede nacht begint niet in bed, maar in het uur ervoor.</p></blockquote>

<h2>Zet morgen alvast klaar</h2>
<p>Lig je vaak te malen over wat je morgen allemaal moet? Schrijf het dan voor het slapen even op. Door je to-do's en gedachten op papier te zetten, hoef je ze niet de hele nacht vast te houden. Leg ook praktisch alvast klaar wat je morgen nodig hebt — dat scheelt ochtendstress.</p>

<h2>Zorg voor een fijne slaapkamer</h2>
<p>Je omgeving doet veel. Een opgeruimde, donkere en niet te warme slaapkamer nodigt uit tot slapen. Lucht de kamer even voor je naar bed gaat, en houd 'm zo veel mogelijk vrij van schermen en werk. Je slaapkamer mag een plek van rust zijn.</p>

<div class="callout"><p><strong>Wees niet te streng.</strong> Lukt het op een avond niet om alles te volgen? Geen probleem. Een avondroutine is bedoeld om je te helpen ontspannen, niet om er een nieuwe verplichting bij te krijgen.</p></div>

<p>Een fijne dag verdient een rustige afsluiting. Geef jezelf die zachte landing aan het eind van de dag — je wordt er morgen een stuk fijner wakker van.</p>
""",
    },
]


def article(slug):
    return next(a for a in ARTICLES if a["slug"] == slug)
