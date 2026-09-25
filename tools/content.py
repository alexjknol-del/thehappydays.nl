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
        "slug": "zo-houd-je-aandacht-voor-elkaar-in-een-lange-relatie",
        "title": "Zo houd je aandacht voor elkaar in een lange relatie",
        "meta_title": "Relatietips voor een gezonde relatie die echt verschil maken?",
        "meta_desc": "Relatietips voor meer aandacht en verbinding ✓ Ontdek hoe communicatie, waardering en ruimte voor jezelf bijdragen aan een gezonde relatie ✓",
        "cat": "persoonlijke-groei",
        "date": "2026-09-22", "date_nl": "22 september 2026", "read": 4,
        "img": "art-relatie.svg",
        "excerpt": "In het begin van een relatie gaat aandacht voor elkaar bijna vanzelf. Je zoekt elkaar op, praat urenlang en maakt bewust tijd vrij om samen te zijn.",
        "body": """
<p>In het begin van een relatie gaat aandacht voor elkaar bijna vanzelf. Je zoekt elkaar op, praat urenlang en maakt bewust tijd vrij om samen te zijn. Naarmate je langer samen bent, krijgt het dagelijks leven steeds meer ruimte. Werk, sociale afspraken en andere verplichtingen komen op de voorgrond. Juist dan is het waardevol om bewust te blijven investeren in de band met je partner. Dat hoeft echt niet ingewikkeld te zijn. Kleine, regelmatige gewoontes kunnen al meer verschil maken dan je zou denken.</p>
<h2>Blijf met elkaar in gesprek</h2>
<p>Goede communicatie betekent niet alleen praten wanneer er iets misgaat. Vertel elkaar ook wat je bezighoudt, waar je naar uitkijkt en wat je nodig hebt. Verwacht niet automatisch dat je partner weet wat je denkt of voelt: zelfs mensen die jarenlang samenleven hebben dat niet altijd door. Een praktische <a href="https://www.online-relatietherapie.nl/10-relatietips/" target="_blank" rel="noopener">relatietip</a> is om regelmatig bewust tijd te maken voor een gesprek zonder afleiding van telefoons, televisie of anderen. Luister daarbij niet alleen om te kunnen antwoorden, maar probeer werkelijk te begrijpen wat de ander bedoelt. Dat voorkomt dat kleine irritaties zich onnodig opstapelen.</p>
<h2>Houd ruimte voor jezelf</h2>
<p>Een sterke relatie betekent niet dat je alles samen moet doen. Eigen hobby's, vriendschappen en interesses blijven belangrijk, ook als je lang samen bent. Ze geven je ruimte om jezelf te blijven ontwikkelen en zorgen voor nieuwe ervaringen die je met je partner kunt delen. Verschillen tussen partners hoeven dan ook geen obstakel te zijn. Het is zelden nodig om de ander te veranderen. Respect voor elkaars karakter en voorkeuren draagt juist bij aan een prettige balans tussen verbondenheid en zelfstandigheid, en voorkomt dat je in een relatie jezelf kwijtraakt.</p>
<h2>Laat waardering niet vanzelfsprekend worden</h2>
<p>Wanneer je lang samen bent, raak je gemakkelijk gewend aan wat de ander allemaal doet. Een maaltijd koken, iets regelen of gewoon luisteren na een drukke dag kan daardoor ongemerkt vanzelfsprekend gaan aanvoelen. Spreek je waardering daarom uit, ook als het om kleine dingen gaat. Een oprecht compliment of een eenvoudig bedankje laat zien dat je de ander nog steeds bewust ziet en waardeert. Hetzelfde geldt voor samen tijd doorbrengen. Een avond zonder afleiding, een wandeling of rustig koffie drinken samen kan genoeg zijn om opnieuw echt contact te hebben.</p>
<h2>Bespreek wat je dwarszit</h2>
<p>Gevoelens opkroppen zorgt er bijna altijd voor dat frustraties zich opstapelen totdat ze op het verkeerde moment naar buiten komen. Eerlijk vertellen wat je raakt of waar je onzeker over bent, maakt het mogelijk om samen naar een oplossing te zoeken in plaats van langs elkaar heen te werken. Daarbij hoort ook verantwoordelijkheid nemen wanneer je zelf iets niet handig hebt aangepakt. Excuses aanbieden en echt luisteren naar de ervaring van je partner kunnen helpen om na een conflict weer nader tot elkaar te komen zonder dat oude kwesties blijven smeulen.</p>
<p>Soms blijven bepaalde patronen ondanks gesprekken terugkomen. Dan kan <a href="https://www.online-relatietherapie.nl/" target="_blank" rel="noopener">online relatietherapie</a> een waardevolle stap zijn om samen of individueel naar communicatie, gedrag en verwachtingen te kijken. Een therapeut begeleidt het gesprek en helpt om patronen te herkennen die vanuit de relatie zelf moeilijk zichtbaar zijn. Ook stellen zonder grote problemen kunnen er baat bij hebben om bewust stil te staan bij hoe ze met elkaar omgaan.</p>
<h2>Aandacht blijft de basis</h2>
<p>Een gezonde relatie vraagt niet om voortdurende romantische gebaren of grote inspanningen. Vaak zit verbinding juist in dagelijkse aandacht, eerlijkheid en oprechte interesse in elkaar. Door te blijven praten, ruimte te geven en waardering uit te spreken, voorkom je dat samenzijn alleen een gewoonte wordt. Zo blijft er plaats voor zowel je eigen ontwikkeling als de band die jullie samen hebben opgebouwd.</p>
<h2>Veelgestelde vragen</h2>
<h3>Hoe voorkom je dat je als stel langs elkaar heen gaat leven?</h3>
<p>Maak bewust momenten vrij waarop jullie zonder afleiding samen zijn en met elkaar praten. Regelmaat is daarbij vaak belangrijker dan de duur van zo'n moment.</p>
<h3>Moet je als stel alles samen doen?</h3>
<p>Nee. Eigen hobby's, vrienden en activiteiten dragen juist bij aan een gezonde relatie. Je houdt zo ruimte voor je eigen identiteit en brengt nieuwe ervaringen mee naar huis.</p>
<h3>Wanneer kan relatietherapie zinvol zijn?</h3>
<p>Relatietherapie kan worden overwogen wanneer conflicten of communicatieproblemen blijven terugkomen. Ook stellen zonder grote problemen kunnen er baat bij hebben om bewuster naar hun relatie en onderlinge patronen te kijken.</p>
""",
    },
    {
        "slug": "meer-vertrouwen-in-jezelf",
        "title": "Meer vertrouwen in jezelf begint bij hoe je naar jezelf kijkt",
        "meta_title": "Zelfvertrouwen vergroten door anders naar jezelf te kijken?",
        "meta_desc": "Zelfvertrouwen vergroten? ✓ Ontdek hoe gedachten en ervaringen je zelfbeeld beïnvloeden ✓ Lees hoe kleine veranderingen meer vertrouwen kunnen geven.",
        "cat": "persoonlijke-groei",
        "date": "2026-09-23", "date_nl": "23 september 2026", "read": 3,
        "img": "art-zelfvertrouwen.svg",
        "excerpt": "Zelfvertrouwen lijkt soms iets wat je hebt of niet hebt. In werkelijkheid verandert het door de jaren heen, soms zonder dat je het direct doorhebt.",
        "body": """
<p>Zelfvertrouwen lijkt soms iets wat je hebt of niet hebt. In werkelijkheid verandert het door de jaren heen, soms zonder dat je het direct doorhebt. Ervaringen, reacties van anderen en de manier waarop je over jezelf bent gaan denken, spelen allemaal een rol. Een kritische opmerking kan verrassend lang blijven hangen. Positieve ervaringen laten dan juist zien dat je meer kunt dan je dacht. Wie onzekerheid beter leert begrijpen, ontdekt ook waar ruimte voor verandering zit.</p>
<h2>Hoe je zelfbeeld zich ontwikkelt</h2>
<p>Je zelfbeeld ontstaat niet op één moment. Als kind krijg je voortdurend signalen over wat anderen van je vinden. Ouders, leraren, vrienden en klasgenoten laten allemaal hun sporen na in hoe je naar jezelf kijkt. Ook ervaringen op latere leeftijd tellen mee. Een negatieve ervaring hoeft op zichzelf niet bepalend te zijn, maar bepaalde opmerkingen of gebeurtenissen kunnen zich vastzetten. Je gaat geloven dat je niet slim genoeg bent, of dat je altijd fouten maakt. Wanneer zulke gedachten regelmatig terugkomen, gaan ze vanzelfsprekender voelen dan ze in werkelijkheid zijn.</p>
<h2>Wanneer onzekerheid je keuzes bepaalt</h2>
<p>Iedereen twijfelt weleens aan zichzelf. Dat wordt lastig als onzekerheid bepaalt wat je wel en niet durft te doen. Misschien spreek je tijdens een vergadering liever niet, terwijl je wel een goed idee hebt. Of je vermijdt nieuwe activiteiten omdat je vooraf al verwacht te falen. Door situaties steeds te omzeilen, krijg je minder kansen om te ervaren dat je ze misschien wél aankunt. Wie bewust wil werken aan <a href="https://www.internettherapeut.nl/hulp-bij-zelfvertrouwen/" target="_blank" rel="noopener">zelfvertrouwen vergroten</a>, doet er goed aan om naar zowel gedachten als gedrag te kijken. Juist die combinatie helpt om oude overtuigingen opnieuw te onderzoeken en stap voor stap te verzwakken.</p>
<h2>Anders leren kijken naar kritische gedachten</h2>
<p>Een negatieve gedachte over jezelf is niet automatisch een feit, ook al klinkt ze overtuigend. Je maakt één fout en denkt meteen dat je nergens goed in bent. Iemand reageert kortaf en je concludeert dat jij iets verkeerd hebt gedaan. Het helpt om zulke gedachten bewust op te merken in plaats van ze zomaar te accepteren. Vraag jezelf af waarop je conclusie is gebaseerd en welke informatie je misschien over het hoofd ziet. Denk ook aan momenten waarop iets juist goed ging. Het doel is niet om alles positief te maken, maar om realistischer naar jezelf en je mogelijkheden te leren kijken.</p>
<h2>Kleine ervaringen kunnen verschil maken</h2>
<p>Zelfvertrouwen groeit niet alleen door anders te denken. Gedrag speelt een minstens even grote rol. Iets doen wat je spannend vindt, levert nieuwe informatie op die je verwachtingen kan corrigeren. Stel die vraag toch, ga alleen naar die activiteit, geef duidelijk je mening. Begin bij een uitdaging die haalbaar voelt, zodat je kunt ervaren wat er werkelijk gebeurt in plaats van alleen af te gaan op wat je vreesde. Als onzekerheid hardnekkig is en je dagelijks leven structureel beperkt, kan begeleiding door een psycholoog helpen. Ook online gesprekken via <a href="https://www.internettherapeut.nl/" target="_blank" rel="noopener">internettherapeut.nl</a> bieden de mogelijkheid om gedachten en gedrag samen te onderzoeken, zonder wachtlijst en vanuit een vertrouwde omgeving.</p>
<h2>Zelfvertrouwen hoeft niet perfect te zijn</h2>
<p>Meer vertrouwen in jezelf betekent niet dat onzekerheid volledig verdwijnt. Twijfel hoort bij nieuwe situaties en moeilijke keuzes, dat is gewoon menselijk. Het verschil zit vooral in de ruimte die je die twijfel geeft. Wanneer je jezelf niet voortdurend langs een onhaalbare meetlat legt, ontstaat er meer vrijheid om te proberen, te leren en soms fouten te maken zonder dat dat meteen iets zegt over wie je bent.</p>
<h2>Veelgestelde vragen</h2>
<h3>Kun je zelfvertrouwen echt ontwikkelen?</h3>
<p>Ja. Zelfvertrouwen kan veranderen door nieuwe ervaringen en door bewuster om te gaan met negatieve overtuigingen over jezelf. Cognitieve gedragstherapie is een bewezen effectieve methode om daarmee aan de slag te gaan.</p>
<h3>Wat is het verschil tussen zelfvertrouwen en zelfbeeld?</h3>
<p>Zelfbeeld gaat over hoe je jezelf als persoon ziet. Zelfvertrouwen heeft meer te maken met het vertrouwen dat je hebt in je eigen mogelijkheden. Beide beïnvloeden elkaar en kunnen allebei worden versterkt.</p>
<h3>Wanneer kan professionele hulp zinvol zijn?</h3>
<p>Als onzekerheid je dagelijks functioneren beperkt, bijvoorbeeld doordat je sociale situaties, werk of nieuwe activiteiten structureel vermijdt, is het zinvol om dit met een psycholoog te bespreken.</p>
""",
    },
    {
        "slug": "welke-therapievorm-past-bij-trauma-verwerken",
        "title": "Welke therapievorm past bij het verwerken van trauma?",
        "meta_title": "Trauma therapie kiezen die past bij jouw klachten?",
        "meta_desc": "Welke trauma therapie past bij je? ✓ Lees over EMDR, CGT, schematherapie en NET ✓ Ontdek waarom een persoonlijke aanpak belangrijk is.",
        "cat": "zelfzorg",
        "date": "2026-09-24", "date_nl": "24 september 2026", "read": 3,
        "img": "art-verwerken.svg",
        "excerpt": "Een ingrijpende ervaring kan lang doorwerken, ook als het er op het eerste gezicht niet zo uitziet. Soms merk je het aan terugkerende beelden of nachtmerries.",
        "body": """
<p>Een ingrijpende ervaring kan lang doorwerken, ook als het er op het eerste gezicht niet zo uitziet. Soms merk je het aan terugkerende beelden of nachtmerries. Soms aan een aanhoudend gevoel van onrust, de neiging om bepaalde situaties te vermijden of gedachten over jezelf die steeds terugkomen. Trauma heeft veel gezichten, en gelukkig zijn er ook verschillende manieren om ermee aan de slag te gaan. Welke therapievorm het beste past, hangt af van je ervaringen, je klachten en wat je op dat moment aankunt.</p>
<h2>Waarom er niet één aanpak bestaat</h2>
<p>Trauma is geen vastomlijnde klacht die altijd op dezelfde manier wordt behandeld. Een eenmalige schokkende gebeurtenis kan andere gevolgen hebben dan langdurige onveiligheid vroeg in het leven. Ook maakt het uit of bepaalde herinneringen de meeste spanning veroorzaken, of dat er diepgewortelde patronen zijn ontstaan die al jaren doorwerken in hoe je denkt, voelt en reageert. Juist daarom bestaat <a href="https://www.trauma-therapie.nl/therapieen/" target="_blank" rel="noopener">trauma therapie</a> uit verschillende behandelvormen, elk met een eigen insteek en werkwijze. Een psycholoog kan samen met jou onderzoeken wat er speelt en welke aanpak daarbij het beste aansluit.</p>
<h2>EMDR bij belastende herinneringen</h2>
<p>EMDR staat voor Eye Movement Desensitization and Reprocessing. Bij deze behandeling denk je onder begeleiding terug aan een belastende herinnering, terwijl je tegelijkertijd een afleidende taak uitvoert zoals het volgen van bewegingen met je ogen. Het doel is niet om de herinnering te wissen, maar om de emotionele lading ervan te verminderen. Zo kun je aan de ervaring terugdenken zonder dat dezelfde intense spanning telkens opnieuw wordt opgeroepen. EMDR wordt veel ingezet bij enkelvoudig trauma en posttraumatische stressklachten en is een van de meest onderzochte methoden op dit gebied.</p>
<h2>Gedachten en patronen doorbreken</h2>
<p>Bij cognitieve gedragstherapie staat de wisselwerking tussen gedachten, gevoelens en gedrag centraal. Na een ingrijpende ervaring kunnen overtuigingen ontstaan die je dagelijks leven stilletjes beïnvloeden, zoals het idee dat de wereld onveilig is of dat je zelf tekortschiet. Tijdens de behandeling onderzoek je die overtuigingen en leer je er anders mee om te gaan. Schematherapie gaat een stap verder en richt zich op patronen die vaak al vroeg in het leven zijn ontstaan. Denk aan wantrouwen, verlatingsangst of een negatief zelfbeeld. Deze methode is met name waardevol bij complex trauma of wanneer vroegere ervaringen nog steeds doorwerken in relaties en zelfbeleving.</p>
<h2>Een levensverhaal opnieuw ordenen</h2>
<p>Narratieve Exposure Therapie, afgekort NET, is ontwikkeld voor mensen die meerdere traumatische gebeurtenissen hebben meegemaakt. Samen met een behandelaar breng je belangrijke ervaringen in chronologische volgorde, waarbij ook positieve en betekenisvolle momenten een plek krijgen naast de moeilijke. Zo kan er meer samenhang ontstaan tussen herinneringen die eerder versnipperd of overweldigend aanvoelden. NET wordt onder meer ingezet bij langdurig misbruik, oorlogservaringen of vluchtelingenachtergronden.</p>
<h2>Online hulp als toegankelijke optie</h2>
<p>De keuze voor een therapievorm hangt niet alleen af van de methode zelf. Ook praktische factoren spelen mee. Voor wie vanuit een vertrouwde omgeving wil starten, biedt <a href="https://www.trauma-therapie.nl/" target="_blank" rel="noopener">Online Trauma Therapie</a> de mogelijkheid om via beveiligd videobellen met een gespecialiseerde psycholoog te werken, zonder wachtlijst en met flexibele afspraken. Of online behandeling bij jouw situatie past, wordt tijdens een professionele intake beoordeeld. De eerste kennismaking is gratis, wat de drempel om te beginnen zo laag mogelijk maakt.</p>
<h2>Ruimte voor een persoonlijke aanpak</h2>
<p>Traumaverwerking volgt geen standaardroute. Soms is één methode precies wat iemand nodig heeft. In andere gevallen worden behandelvormen gecombineerd of aangepast naarmate het traject vordert. Wat het meeste oplevert, hangt af van jouw verhaal, je klachten en wat je op dat moment aankunt. Een behandelplan dat daarin meeverandert, geeft ruimte voor echte vooruitgang in plaats van een vaststaand protocol.</p>
<h2>Veelgestelde vragen</h2>
<h3>Welke therapie wordt vaak gebruikt bij trauma?</h3>
<p>EMDR en traumagerichte cognitieve gedragstherapie worden veel ingezet bij traumagerelateerde klachten. Ook NET en schematherapie kunnen passend zijn, afhankelijk van de situatie en de achtergrond van de klachten.</p>
<h3>Is EMDR geschikt voor ieder trauma?</h3>
<p>Niet automatisch. Of EMDR passend is, hangt af van je klachten, ervaringen en persoonlijke omstandigheden. Een behandelaar kan dit samen met jou beoordelen tijdens een intake.</p>
<h3>Kunnen verschillende traumatherapieën worden gecombineerd?</h3>
<p>Ja, dat is mogelijk en soms zelfs de sterkste aanpak. Verschillende behandelmethoden kunnen na elkaar of naast elkaar worden gebruikt, afhankelijk van de behandeldoelen en het verloop van het traject.</p>
""",
    },
    {
        "slug": "knopen-met-koord-handwerk-als-rustmoment",
        "title": "Knopen met koord: handwerk als rustmoment",
        "cat": "mindful-leven",
        "date": "2026-09-11", "date_nl": "11 september 2026", "read": 5,
        "img": "art-knopen.svg",
        "excerpt": "Iets maken met de handen vraagt precies genoeg aandacht om het hoofd stil te krijgen. Knopen met koord is daar een van de eenvoudigste vormen van, en er is bijna niets voor nodig.",
        "body": """
<p>Er zijn avonden waarop niets helpt. De telefoon blijft trekken, een boek blijft na twee bladzijden liggen en televisie kijken voelt als wachten. Op zulke momenten werkt iets doen met de handen vaak beter dan proberen te ontspannen. Knopen met koord is daar een van de toegankelijkste vormen van: geen cursus, geen machine, geen werkkamer.</p>

<h2>Waarom herhaling het hoofd stil krijgt</h2>
<p>Een knoop bestaat uit een handeling die telkens terugkomt. Die herhaling vraagt genoeg aandacht om niet af te dwalen, maar te weinig om in te spannen. Dat is dezelfde reden waarom breien, haken en tekenen zo vaak worden genoemd als rustgevend. Het verschil met scrollen is dat er na een half uur iets ligt dat er eerst niet was.</p>

<h2>Wat er nodig is om te beginnen</h2>
<p>De basis is een paar meter koord, een sluiting en een schaar. Wie niet los wil uitzoeken, begint met een kant en klaar setje. Bij <a href="https://www.123paracord.nl/diy-sets/armbandsetjes/">123Paracord</a> gaat het om setjes voor een armband rond zes euro, waarin koord, sluiting en beschrijving al bij elkaar zitten. Voor een eerste avond is dat genoeg, en het voorkomt dat er halverwege iets ontbreekt.</p>

<blockquote><p>Beginnen met een compleet setje scheelt de teleurstelling van een halve avond zoeken naar het juiste onderdeel.</p></blockquote>

<h2>Twee knopen zijn een begin</h2>
<p>De platte knoop en de slangenknoop dekken samen het meeste af. De eerste geeft een breed, regelmatig bandje, de tweede een ronde streng die strakker aanvoelt. Beide zijn in een kwartier onder de knie. Wie liever iets ronds maakt, gebruikt een schijf: op de pagina met knoopschijven van <a href="https://www.123paracord.nl/paracord-accessoires/kumihimo-schijf/">123paracord.nl</a> staan de ronde exemplaren van ongeveer drie euro, waarmee acht draden zich vanzelf tot een vlecht ordenen zonder dat er geteld hoeft te worden.</p>

<h2>Klein beginnen loont</h2>
<p>Een armband of een sleutelhanger is in een avond af. Een riem of een tas is dat niet, en juist daar loopt het vaak stuk: een project dat weken duurt, verandert van rustmoment in een verplichting die ligt te wachten. De regel die het langst standhoudt, is dat een project binnen twee avonden af moet kunnen zijn.</p>

<h2>Een vaste plek voor het materiaal</h2>
<p>Handwerk sterft een stille dood in een la waar alles doorheen ligt. Een mandje of een doos waarin koord, schaar en sluitingen samen blijven, maakt het verschil tussen een hobby die doorloopt en een die na drie keer stopt. Alles binnen handbereik betekent dat het aanzetten geen moeite kost.</p>

<h2>Wat het oplevert naast het bandje</h2>
<p>Het resultaat is bescheiden en dat is precies goed. Een gevlochten bandje om de pols, een sleutelhanger aan een tas, iets dat weggegeven kan worden. Wat blijft hangen is niet zozeer het voorwerp, maar het half uur waarin de gedachten een andere kant op gingen. Dat is een klein ding, en kleine dingen zijn nou juist waar fijne dagen uit bestaan.</p>
""",
    },
    {
        "slug": "microdosering-waar-de-term-vandaan-komt",
        "title": "Microdosering: waar die term vandaan komt en wat er precies mee bedoeld wordt",
        "cat": "mindful-leven",
        "date": "2026-09-06", "date_nl": "6 september 2026", "read": 6,
        "img": "art-microdosering.svg",
        "excerpt": "De term duikt overal op, van podcasts tot verjaardagen, maar wat er nou eigenlijk mee bedoeld wordt blijft vaag. Een rustige uitleg van de herkomst, zonder beloftes.",
        "body": """
<p>Sommige woorden verschijnen zomaar in het dagelijks taalgebruik. Microdosering is er zo een. Het valt in podcasts, in reportages en aan de keukentafel, meestal zonder dat iemand uitlegt waar de term vandaan komt. Dit artikel doet dat wel, en houdt het bij de herkomst en de feiten. Over werking of resultaat staat hier bewust niets, want daarover mag in Nederland niets beweerd worden.</p>

<h2>Een woord uit de jaren tien</h2>
<p>De term raakte rond 2015 in omloop, nadat een Amerikaanse onderzoeker begon met het verzamelen van ervaringsverslagen. Daarvoor bestond het woord nauwelijks. Wat er sindsdien omheen is ontstaan, is vooral een verhaal: over technologiebedrijven, over creativiteit, over prestatie. Dat verhaal is groter geworden dan de kennis waarop het rust.</p>

<p>Dat is op zichzelf een bekend patroon. Een term wordt opgepikt, herhaald, en gaat na verloop van tijd een eigen leven leiden. Wie er iets over wil weten, komt daardoor eerder anekdotes tegen dan feiten.</p>

<h2>Wat het woord aanduidt</h2>
<p>Letterlijk gaat het om een verhouding: een fractie van wat als gebruikelijke hoeveelheid geldt, doorgaans genoemd als een tiende tot een twintigste. Meer dan dat zegt de term niet. Er bestaat geen wettelijke definitie, geen genormeerde hoeveelheid en geen erkende methode. Twee mensen die het woord gebruiken, bedoelen dus niet per se hetzelfde.</p>

<blockquote><p>Een populaire term is nog geen omschreven begrip. Wie iets wil begrijpen, begint bij de herkomst en niet bij de verhalen eromheen.</p></blockquote>

<h2>Paddenstoelen en truffels: niet hetzelfde</h2>
<p>In gesprekken lopen twee producten voortdurend door elkaar. Sinds 2008 staan paddenstoelen met psilocybine in Nederland op lijst II van de Opiumwet. Sclerotia, in de handel truffels genoemd, vielen buiten die aanwijzing en bleven legaal verkrijgbaar. Botanisch zijn het verschillende delen van hetzelfde organisme: het ene groeit onder de grond, het andere erboven.</p>

<p>Die scheiding verklaart waarom het ene product in een winkel ligt en het andere niet. Buiten Nederland gelden weer andere regels, ook binnen Europa, dus meenemen op reis is meestal niet toegestaan. Achtergrond over het onderscheid staat op <a href="https://www.cosmictruffles.nl/microdosering-truffels/">https://www.cosmictruffles.nl/microdosering-truffels/</a>.</p>

<h2>Waarom aanbieders zo weinig zeggen</h2>
<p>Wie webshops in dit segment bekijkt, valt het op: veel productinformatie, bewaaradvies en een aparte disclaimerpagina, en vrijwel geen tekst over wat er te verwachten valt. Dat is geen terughoudendheid uit bescheidenheid maar een wettelijke verplichting. Uitspraken die suggereren dat iets een aandoening voorkomt, behandelt of geneest, zijn verboden. Ook een winkel als <a href="https://www.cosmictruffles.nl/magic-truffels/">Cosmic Truffles</a> werkt binnen die grens.</p>

<div class="callout"><p><strong>Rustig lezen.</strong> Komt er ergens een stellige belofte langs over een middel, dan is dat het moment om even te vertragen. De vraag is dan niet of het klinkt als iets moois, maar wie het zegt en waarop het gebaseerd is.</p></div>

<h2>Wat er over onderzoek te zeggen valt</h2>
<p>Er loopt wetenschappelijk onderzoek naar deze stoffen, maar het aantal gecontroleerde studies naar lage hoeveelheden is klein en de uitkomsten lopen uiteen. Bij berichten die iets als aangetoond presenteren, helpen drie vragen: om welk onderzoek gaat het, hoeveel deelnemers waren er, en was er een controlegroep? Zonder die drie blijft er weinig over om op te bouwen.</p>

<h2>Het grotere plaatje</h2>
<p>Achter de populariteit van dit soort termen zit vaak dezelfde wens: dat er ergens een kortere route bestaat naar meer rust of meer helderheid. Die wens is invoelbaar. Tegelijk is er tot nu toe weinig dat het bestaan van zo een route bevestigt, en dat is precies de reden om nieuwsgierig te blijven maar niet goedgelovig.</p>

<p>Wie medicatie gebruikt of twijfelt, legt de vraag voor aan een arts of apotheker. En verder geldt wat voor de meeste onderwerpen op deze site opgaat: kleine, saaie gewoontes doen op de lange termijn meestal meer dan welke nieuwe term dan ook.</p>
""",
    },
    {
        "slug": "dames-huispakken-comfortabel-thuis",
        "title": "Dames huispakken: lekker warm en comfortabel thuis",
        "cat": "thuis-en-sfeer",
        "date": "2026-07-18", "date_nl": "18 juli 2026", "read": 4,
        "img": "art-huispakken.svg",
        "excerpt": "Weinig is zo fijn als thuiskomen en in iets zachts en warms wegkruipen. Een goed huispak maakt van je avond meteen een klein moment van rust.",
        "body": """
<p>Er is een moment op de dag dat je thuiskomt, je jas ophangt en het liefst meteen in iets zachts wilt wegkruipen. Je dagkleren uit, je huispak aan. Dat kleine ritueel is het startsein voor ontspanning: je lichaam merkt dat er even niets meer moet.</p>

<h2>Waarom een huispak zo fijn is</h2>
<p>Een huispak is meer dan losse kleding om in rond te lopen. Het is een signaal aan jezelf dat de dag erop zit. Zachte stof tegen je huid, een ruime pasvorm die nergens knelt, en niets wat je hoeft in te houden. Juist die eenvoud maakt dat je sneller tot rust komt dan in een spijkerbroek die de hele dag om je heen zat.</p>

<h2>Waar je op let bij het kiezen</h2>
<p>Niet elk huispak voelt hetzelfde, en de stof maakt het grootste verschil. Katoen ademt fijn en blijft het hele jaar door prettig, badstof en velours voelen extra warm en zacht in de koudere maanden, en een lichte tricot is heerlijk in de zomer. Let daarnaast op de pasvorm: een goed huispak zit ruim zonder vormeloos te worden, met een tailleband die niet in je vel snijdt.</p>
<ul>
<li><strong>Zomer:</strong> lichte katoen of tricot, korte mouwen of een dunne broek.</li>
<li><strong>Winter:</strong> badstof, velours of een gebreide kwaliteit die de warmte vasthoudt.</li>
<li><strong>Tussenseizoen:</strong> een setje in laagjes dat je makkelijk aan- en uittrekt.</li>
</ul>

<blockquote><p>Comfort is geen luxe maar een vorm van zelfzorg — thuis mag alles even zachter.</p></blockquote>

<h2>Van ochtend tot avond</h2>
<p>Een huispak hoeft niet alleen voor 's avonds op de bank. Een rustige zondagochtend met koffie en de krant, een dag thuiswerken zonder afspraken, of dat uurtje na het douchen voor het slapengaan: het zijn precies de momenten waarop iets comfortabels je dag zachter maakt. Kies een setje dat er ook nog eens verzorgd uitziet, dan voel je je er zelfs bij een onverwachte videobelafspraak prettig in.</p>

<div class="callout"><p><strong>Kleine tip.</strong> Heb je twee huispakken, dan hoef je nooit te wachten op de was. Eentje aan, eentje in de kast, zo blijft dat fijne gevoel altijd binnen handbereik.</p></div>

<h2>Een mooi huispak vinden</h2>
<p>Op zoek naar een nieuw exemplaar? Er zijn webshops die zich helemaal richten op <a href="https://loungeweare.com/">dames huispakken</a>, met modellen in verschillende stoffen, kleuren en pasvormen. Zo vind je makkelijker een setje dat bij jou past, bij het seizoen en bij de manier waarop jij het liefst thuis ontspant.</p>

<p>Uiteindelijk draait het om dat ene simpele gevoel: thuiskomen, iets zachts aantrekken en merken dat je schouders zakken. Een goed huispak helpt je daarbij, elke dag opnieuw.</p>
""",
    },
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
