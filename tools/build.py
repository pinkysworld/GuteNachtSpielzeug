#!/usr/bin/env python3
"""Generates the static DE/EN pages. Run: python3 tools/build.py"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BASE = "/GuteNachtSpielzeug/"
SITE = "https://minh.systems" + BASE

T = {
 "de": dict(
  name="Gute Nacht, Spielzeug", pre="", other="en", other_label="English",
  nav=[("#so-gehts", "So geht's"), ("#buecher", "Bücher"), ("#eltern", "Für Eltern"), ("support/", "Hilfe")],
  soon_small="Bald im", soon_big="App Store",
  support="Support", privacy="Datenschutz (App)", impressum="Impressum", dsgvo="Datenschutz",
  rights="© 2026 Minh Nguyen Studios. Alle Rechte vorbehalten.",
  skip="Zum Inhalt springen", tm="Apple, iPhone, iPad und App Store sind Marken der Apple Inc.", mailfb="mip [at] gmx.biz",
 ),
 "en": dict(
  name="Good Night, Toys", pre="en/", other="de", other_label="Deutsch",
  nav=[("#how", "How it works"), ("#books", "Books"), ("#parents", "For parents"), ("support/", "Help")],
  soon_small="Coming soon to the", soon_big="App Store",
  support="Support", privacy="Privacy (app)", impressum="Imprint", dsgvo="Privacy (website)",
  rights="© 2026 Minh Nguyen Studios. All rights reserved.",
  skip="Skip to content", tm="Apple, iPhone, iPad and App Store are trademarks of Apple Inc.", mailfb="mip [at] gmx.biz",
 ),
}

BOOKS = [
 ("kinderzimmer", "Kinderzimmer", "Kids' Room", "Bo, der Bär, und die kleine Eisenbahn", "Bo the bear and the little train", True),
 ("hof", "Bauernhof", "Farm", "Schaf, Huhn und Pferd", "Sheep, hen and horse", True),
 ("werkstatt", "Werkstatt", "Workshop", "Holzspielzeug zwischen Hobelspänen", "Wooden toys among the shavings", False),
 ("bad", "Badezimmer", "Bathroom", "Quak, die Ente, und das Boot", "Quak the duck and the boat", False),
 ("musik", "Musikzimmer", "Music Room", "Trommel, Spieluhr und Trompete", "Drum, music box and trumpet", False),
 ("kita", "Kindergarten", "Kindergarten", "Lotta, die Puppe, und ihre Freunde", "Lotta the doll and friends", False),
 ("kitagarten", "Kita-Garten", "Playground", "Draußen auf dem Spielplatz", "Out on the playground", False),
 ("garten", "Garten", "Backyard", "Unter Lichterketten im Garten", "Under fairy lights in the yard", False),
 ("hoehle", "Kuschelhöhle", "Blanket Fort", "Wuffel, der Hund, und Olli, die Eule", "Wuffel the dog and Olli the owl", False),
]

LANGS_DE = "Deutsch, Englisch, Französisch, Spanisch, Italienisch, Niederländisch, Portugiesisch, Schwedisch, Dänisch, Norwegisch, Japanisch, Koreanisch und Chinesisch"
LANGS_EN = "German, English, French, Spanish, Italian, Dutch, Portuguese, Swedish, Danish, Norwegian, Japanese, Korean and Chinese"


def appstore(t):
    return (f'<span class="appstore is-soon" data-appstore role="note">'
            f'<span class="as-small">{t["soon_small"]}</span><span class="as-big">{t["soon_big"]}</span></span>')


def mail(t, subject=""):
    return f'<span data-mail="{subject}"><noscript>{t["mailfb"]}</noscript></span>'


def layout(lang, path, title, desc, body, home=False):
    t = T[lang]
    home_url = BASE + t["pre"]
    other_pre = T[t["other"]]["pre"]
    other_url = BASE + other_pre + path
    nav = "".join(
        f'<a class="hide-sm" href="{h if (home and h.startswith("#")) else home_url + h}">{l}</a>'
        for h, l in t["nav"])
    alt_de = SITE + T["de"]["pre"] + path
    alt_en = SITE + T["en"]["pre"] + path
    canon = SITE + t["pre"] + path
    return f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="apple-itunes-app" content="app-id=6824285939">
<meta name="theme-color" content="#f7f0e2">
<link rel="canonical" href="{canon}">
<link rel="alternate" hreflang="de" href="{alt_de}">
<link rel="alternate" hreflang="en" href="{alt_en}">
<link rel="alternate" hreflang="x-default" href="{alt_de}">
<link rel="icon" type="image/png" href="{BASE}favicon.png">
<link rel="apple-touch-icon" href="{BASE}apple-touch-icon.png">
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canon}">
<meta property="og:image" content="{SITE}assets/img/og.jpg">
<meta property="og:locale" content="{'de_DE' if lang == 'de' else 'en_US'}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="{SITE}assets/img/og.jpg">
<link rel="stylesheet" href="{BASE}assets/site.css?v=2">
<script src="{BASE}assets/site.js?v=2" defer></script>
</head>
<body>
<a class="skip" href="#main">{t["skip"]}</a>
<header class="top"><div class="wrap">
<a class="brand" href="{home_url}"><img src="{BASE}assets/img/icon.webp" alt="" width="38" height="38">{t["name"]}</a>
<nav class="nav" aria-label="Menu">{nav}<a class="lang" href="{other_url}" hreflang="{t["other"]}" lang="{t["other"]}">{t["other_label"]}</a></nav>
</div></header>
<main id="main">
{body}
</main>
<footer><div class="wrap">
<a href="https://minh.systems/"><img class="wm" src="{BASE}assets/img/minh-wordmark.svg" alt="minh.studios – Minh Nguyen Studios" width="200" height="50"></a>
<nav aria-label="Footer">
<a href="{home_url}support/">{t["support"]}</a>
<a href="{home_url}privacy/">{t["privacy"]}</a>
<a href="https://minh.systems/impressum/">{t["impressum"]}</a>
<a href="https://minh.systems/datenschutz/">{t["dsgvo"]}</a>
</nav>
<small>{t["rights"]} {t["tm"]}</small>
</div></footer>
</body>
</html>
"""


def img(name, alt, w=1184, h=648, cls="shot", lazy=True):
    return (f'<img class="{cls}" src="{BASE}assets/img/{name}.webp" '
            f'srcset="{BASE}assets/img/{name}-sm.webp 592w, {BASE}assets/img/{name}.webp 1184w" '
            f'sizes="(max-width:860px) 100vw, 600px" width="{w}" height="{h}" alt="{alt}"'
            f'{" loading=\"lazy\"" if lazy else ""} decoding="async">')


def books(lang):
    out = []
    for key, de, en, sd, se, free in BOOKS:
        name = de if lang == "de" else en
        sub = sd if lang == "de" else se
        tag = (f'<em class="tag">{"Gratis" if lang == "de" else "Free"}</em>' if free else "")
        out.append(f'<li><img src="{BASE}assets/img/book_{key}.webp" width="320" height="440" loading="lazy" '
                   f'alt="{"Buchcover" if lang == "de" else "Book cover"} „{name}“"><strong>{name}</strong><span>{sub}</span>{tag}</li>')
    return '<ul class="books">' + "".join(out) + "</ul>"


def home_de():
    t = T["de"]
    return f"""
<section class="hero"><div class="wrap">
<div>
<span class="pill">Für Kinder von 3 bis 6 · iPhone &amp; iPad</span>
<h1>Gute Nacht, Spielzeug</h1>
<p class="lead">Ein interaktives Gute-Nacht-Bilderbuch: Dein Kind bringt die Spielsachen ins Bett, macht das Licht aus und hängt den Mond ins Fenster. Dann wird es dunkel, das Schlaflied wird leiser – und das Buch klappt zu.</p>
<div class="ctas">{appstore(t)}<a class="btn2" href="#so-gehts">So geht's</a></div>
<ul class="facts"><li>Ohne Lesen</li><li>Ohne Werbung</li><li>Ohne Datensammlung</li><li>Offline</li></ul>
</div>
<div class="hero-art">
{img("hero", "Kinderzimmer im Spiel: Bett, Hundehütte und Spielsachen in Filz- und Holzoptik, Bo der Bär und die kleine Eisenbahn auf dem Teppich", lazy=False)}
<img class="shelf shot" src="{BASE}assets/img/shelf-sm.webp" width="592" height="324" alt="Das Bücherregal mit den Zimmer-Büchern">
</div>
</div></section>

<section id="so-gehts" class="center"><div class="wrap">
<h2>So geht der Abend</h2>
<p class="lead">Ruhig, ohne Zeitdruck, ohne Punkte, ohne Verlieren. Einfach tippen und ziehen – auch für Kinder, die noch nicht lesen.</p>
<div class="steps">
<div class="step">{img("step1", "Spielzeug liegt zugedeckt in seinen Schlafplätzen")}<h3>Spielzeug ins Bett</h3><p>Jedes Spielzeug hat seinen Schlafplatz – mit Kissen, Decke und allem, was dazugehört.</p></div>
<div class="step">{img("step2", "Das Zimmer mit ausgeschaltetem Licht, alle Spielsachen schlafen")}<h3>Licht aus</h3><p>Wenn alle liegen, knipst dein Kind das Licht aus. Das Zimmer wird still.</p></div>
<div class="step">{img("step3", "Der Mond hängt im Fenster des dunklen Kinderzimmers")}<h3>Mond ins Fenster</h3><p>Zum Schluss kommt der Mond ins Fenster, das Schlaflied wird leiser und das Buch klappt zu.</p></div>
</div>
</div></section>

<section id="buecher" class="night"><div class="wrap center">
<h2>Neun Bücher im Regal</h2>
<p class="lead">Jedes Zimmer ist ein Buch mit eigenen Spielsachen, eigenen Schlafplätzen und eigener Musik. Kinderzimmer und Bauernhof sind gratis.</p>
{books("de")}
</div></section>

<section><div class="wrap">
<h2 class="center">Handgemacht aussehende Welten</h2>
<p class="lead center" style="margin:0 auto">Filz, Holz und warmes Licht – und Schlaflieder, die beim Spielen immer sanfter werden.</p>
<div class="gallery">
<figure>{img("kita", "Der Kindergarten mit Puppenwagen, Bettchen und Lotta, der Puppe")}<figcaption>Kindergarten</figcaption></figure>
<figure>{img("hoehle", "Die Kuschelhöhle aus Decken, darin schlafen die Spielsachen")}<figcaption>Kuschelhöhle</figcaption></figure>
<figure>{img("garten", "Der Garten am Abend mit Lichterketten")}<figcaption>Garten</figcaption></figure>
<figure>{img("kitagarten", "Der Kita-Garten bei Nacht, alle Spielsachen schlafen")}<figcaption>Kita-Garten</figcaption></figure>
</div>
</div></section>

<section id="eltern" class="night"><div class="wrap">
<h2>Für Eltern</h2>
<p class="lead">Gemacht als ruhiges Abendritual – nicht als App, die Kinder wach hält.</p>
<div class="cards">
<div class="card" style="color:var(--ink)"><div class="ico" aria-hidden="true">🌙</div><h3>Keine Werbung, kein Tracking</h3><p>Keine Werbung, keine Analyse, kein Konto. Die App sammelt keinerlei Daten und funktioniert komplett offline.</p></div>
<div class="card" style="color:var(--ink)"><div class="ico" aria-hidden="true">🔒</div><h3>Elternbereich mit Sperre</h3><p>Zahnrad 1,5 Sekunden halten, dann die als Wort geschriebene Zahl antippen. Dort: Spielzeug pro Runde, Hilfestufe, Lautstärke, „nur eine Runde“, Sprache.</p></div>
<div class="card" style="color:var(--ink)"><div class="ico" aria-hidden="true">📚</div><h3>Ein einziger Kauf</h3><p>Kinderzimmer und Bauernhof sind gratis. Ein Kauf „Alle Bücher“ (3,99 € in Deutschland) schaltet alle Zimmer für immer frei – auch künftige. Kein Abo. Familienfreigabe inklusive.</p></div>
<div class="card" style="color:var(--ink)"><div class="ico" aria-hidden="true">🌍</div><h3>13 Sprachen</h3><p>{LANGS_DE} – weitere folgen. Für iPhone und iPad im Querformat.</p></div>
</div>
</div></section>

<section><div class="wrap" style="max-width:780px">
<h2>Häufige Fragen</h2>
<details><summary>Muss mein Kind lesen können?</summary><p>Nein. Alles funktioniert mit Bildern, Gesten und Klängen.</p></details>
<details><summary>Was kostet die App?</summary><p>Laden und die Bücher Kinderzimmer und Bauernhof sind gratis. Alle weiteren Bücher gibt es mit einem einmaligen Kauf „Alle Bücher“ – ohne Abo.</p></details>
<details><summary>Sammelt die App Daten?</summary><p>Nein. Keine Konten, keine Analyse, keine Werbung, keine Netzwerkverbindungen. Mehr in der <a href="privacy/">Datenschutzerklärung der App</a>.</p></details>
<p><a href="support/">Alle Fragen &amp; Kontakt →</a></p>
</div></section>
"""


def home_en():
    t = T["en"]
    return f"""
<section class="hero"><div class="wrap">
<div>
<span class="pill">For ages 3 to 6 · iPhone &amp; iPad</span>
<h1>Good Night, Toys</h1>
<p class="lead">An interactive bedtime picture book: your child puts the toys to bed, switches off the light and hangs the moon in the window. Then it gets dark, the lullaby grows quieter – and the book closes.</p>
<div class="ctas">{appstore(t)}<a class="btn2" href="#how">How it works</a></div>
<ul class="facts"><li>No reading needed</li><li>No ads</li><li>No data collection</li><li>Works offline</li></ul>
</div>
<div class="hero-art">
{img("hero", "The kids' room in the game: bed, dog house and felt-and-wood toys, Bo the bear and the little train on the rug", lazy=False)}
<img class="shelf shot" src="{BASE}assets/img/shelf-sm.webp" width="592" height="324" alt="The bookshelf with the room books">
</div>
</div></section>

<section id="how" class="center"><div class="wrap">
<h2>How bedtime goes</h2>
<p class="lead">Calm, with no time pressure, no points and no failing. Just tap and drag – made for children who can't read yet.</p>
<div class="steps">
<div class="step">{img("step1", "Toys tucked into their sleeping places")}<h3>Toys to bed</h3><p>Every toy has its own sleeping place – with pillow, blanket and everything that belongs.</p></div>
<div class="step">{img("step2", "The room with the light switched off, all toys asleep")}<h3>Light off</h3><p>When everyone is lying down, your child switches off the light. The room goes quiet.</p></div>
<div class="step">{img("step3", "The moon hangs in the window of the dark kids' room")}<h3>Moon in the window</h3><p>Finally the moon goes in the window, the lullaby fades and the book closes.</p></div>
</div>
</div></section>

<section id="books" class="night"><div class="wrap center">
<h2>Nine books on the shelf</h2>
<p class="lead">Every room is a book with its own toys, sleeping places and music. The Kids' Room and the Farm are free.</p>
{books("en")}
</div></section>

<section><div class="wrap">
<h2 class="center">Worlds that look handmade</h2>
<p class="lead center" style="margin:0 auto">Felt, wood and warm light – with lullabies that grow softer as play goes on.</p>
<div class="gallery">
<figure>{img("kita", "The kindergarten with doll's pram, little bed and Lotta the doll")}<figcaption>Kindergarten</figcaption></figure>
<figure>{img("hoehle", "The blanket fort with the toys asleep inside")}<figcaption>Blanket Fort</figcaption></figure>
<figure>{img("garten", "The backyard in the evening with fairy lights")}<figcaption>Backyard</figcaption></figure>
<figure>{img("kitagarten", "The playground at night, all toys asleep")}<figcaption>Playground</figcaption></figure>
</div>
</div></section>

<section id="parents" class="night"><div class="wrap">
<h2>For parents</h2>
<p class="lead">Made as a calm evening ritual – not as an app that keeps kids awake.</p>
<div class="cards">
<div class="card" style="color:var(--ink)"><div class="ico" aria-hidden="true">🌙</div><h3>No ads, no tracking</h3><p>No ads, no analytics, no account. The app collects no data at all and works fully offline.</p></div>
<div class="card" style="color:var(--ink)"><div class="ico" aria-hidden="true">🔒</div><h3>Parent area behind a gate</h3><p>Hold the gear for 1.5 seconds, then tap the number written as a word. Inside: toys per round, help level, volume, “only one round”, language.</p></div>
<div class="card" style="color:var(--ink)"><div class="ico" aria-hidden="true">📚</div><h3>One single purchase</h3><p>The Kids' Room and the Farm are free. One “All Books” purchase (€3.99 in Germany, adjusted by country) unlocks every room forever – including future ones. No subscription. Family Sharing included.</p></div>
<div class="card" style="color:var(--ink)"><div class="ico" aria-hidden="true">🌍</div><h3>13 languages</h3><p>{LANGS_EN} – more coming. For iPhone and iPad in landscape.</p></div>
</div>
</div></section>

<section><div class="wrap" style="max-width:780px">
<h2>Frequently asked</h2>
<details><summary>Does my child need to read?</summary><p>No. Everything works with pictures, gestures and sounds.</p></details>
<details><summary>What does it cost?</summary><p>The download and the Kids' Room and Farm books are free. All other books come with one single “All Books” purchase – no subscription.</p></details>
<details><summary>Does the app collect data?</summary><p>No. No accounts, no analytics, no ads, no network connections. See the <a href="privacy/">app privacy policy</a>.</p></details>
<p><a href="support/">All questions &amp; contact →</a></p>
</div></section>
"""


def support(lang):
    t = T[lang]
    if lang == "de":
        return f"""<div class="page"><div class="wrap">
<h1>Hilfe &amp; Support</h1>
<p class="lead">Fragen, Probleme oder Ideen zu „Gute Nacht, Spielzeug“? Schreib uns – wir antworten in der Regel innerhalb weniger Tage.</p>
<div class="box"><strong>E-Mail:</strong> {mail(t, "Gute Nacht, Spielzeug")}</div>
<h2>Häufige Fragen</h2>
<details open><summary>Wie stelle ich meinen Kauf wieder her?</summary><p>Öffne den Elternbereich (siehe unten) und tippe auf „Kauf wiederherstellen“. Melde dich vorher mit derselben Apple-ID an, mit der „Alle Bücher“ gekauft wurde.</p></details>
<details><summary>Wie komme ich in den Elternbereich?</summary><p>Halte das Zahnrad oben links 1,5 Sekunden gedrückt. Dann erscheint eine Zahl als Wort (z. B. „sieben“) – tippe die passende Ziffer an. Im Elternbereich stellst du Spielzeug pro Runde, Hilfestufe, Musik- und Geräuschlautstärke, „nur eine Runde pro Sitzung“ und die Sprache ein, stellst Käufe wieder her und findest die Credits.</p></details>
<details><summary>Funktioniert die Familienfreigabe?</summary><p>Ja. „Alle Bücher“ ist für die Familienfreigabe aktiviert. Familienmitglieder tippen im Elternbereich auf „Kauf wiederherstellen“.</p></details>
<details><summary>Welche Sprachen gibt es?</summary><p>{LANGS_DE}. Weitere Sprachen folgen. Die Sprache kann im Elternbereich gewechselt werden.</p></details>
<details><summary>Welche Daten sammelt die App?</summary><p>Keine. Kein Konto, keine Analyse, keine Werbung, keine Netzwerkverbindungen. Einstellungen bleiben nur auf dem Gerät. Details in der <a href="../privacy/">Datenschutzerklärung der App</a>.</p></details>
<details><summary>Wie setze ich die App zurück bzw. lösche alle Daten?</summary><p>Lösche einfach die App vom Gerät – damit sind alle Einstellungen und Spielstände entfernt. Den Kauf kannst du nach einer Neuinstallation jederzeit kostenlos wiederherstellen.</p></details>
<details><summary>Was kostet die App?</summary><p>Laden sowie Kinderzimmer und Bauernhof sind gratis. Ein einmaliger Kauf „Alle Bücher“ (3,99 € in Deutschland, in anderen Ländern angepasst) schaltet alle Zimmer dauerhaft frei – auch künftige. Kein Abo, keine Werbung.</p></details>
<h2>Kontakt</h2>
<p>Minh Nguyen Studios · E-Mail: {mail(t, "Gute Nacht, Spielzeug")}<br>Anbieterkennzeichnung: <a href="https://minh.systems/impressum/">Impressum</a></p>
</div></div>"""
    return f"""<div class="page"><div class="wrap">
<h1>Help &amp; Support</h1>
<p class="lead">Questions, problems or ideas about “Good Night, Toys”? Write to us – we usually reply within a few days.</p>
<div class="box"><strong>Email:</strong> {mail(t, "Good Night, Toys")}</div>
<h2>Frequently asked questions</h2>
<details open><summary>How do I restore my purchase?</summary><p>Open the parent area (see below) and tap “Restore purchase”. Make sure you are signed in with the same Apple ID that bought “All Books”.</p></details>
<details><summary>How do I open the parent area?</summary><p>Press and hold the gear in the top-left corner for 1.5 seconds. A number appears written as a word (e.g. “seven”) – tap the matching digit. In the parent area you can set toys per round, help level, music and sound volume, “only one round this session” and the language, restore purchases and see the credits.</p></details>
<details><summary>Does Family Sharing work?</summary><p>Yes. “All Books” supports Family Sharing. Family members tap “Restore purchase” in the parent area.</p></details>
<details><summary>Which languages are available?</summary><p>{LANGS_EN}. More languages are coming. You can switch the language in the parent area.</p></details>
<details><summary>What data does the app collect?</summary><p>None. No account, no analytics, no ads, no network connections. Settings stay on the device only. Details in the <a href="../privacy/">app privacy policy</a>.</p></details>
<details><summary>How do I reset the app or delete all data?</summary><p>Simply delete the app from your device – that removes all settings and progress. You can restore your purchase for free at any time after reinstalling.</p></details>
<details><summary>What does it cost?</summary><p>The download, the Kids' Room and the Farm are free. One single “All Books” purchase (€3.99 in Germany, adjusted by country) unlocks every room forever – including future ones. No subscription, no ads.</p></details>
<h2>Contact</h2>
<p>Minh Nguyen Studios · Email: {mail(t, "Good Night, Toys")}<br>Legal notice: <a href="https://minh.systems/impressum/">Imprint</a></p>
</div></div>"""


def privacy(lang):
    t = T[lang]
    if lang == "de":
        return f"""<div class="page"><div class="wrap">
<h1>Datenschutzerklärung der App</h1>
<p class="lead">„Gute Nacht, Spielzeug“ (iPhone &amp; iPad) – Stand: Oktober 2026</p>
<div class="box"><strong>Kurz gesagt:</strong> Die App erhebt, speichert oder übermittelt keinerlei personenbezogene Daten. Keine Werbung, keine Analyse, kein Tracking, kein Konto, keine Netzwerkverbindungen.</div>
<h2>1. Verantwortlicher</h2>
<p>Minh Nguyen Studios. Vollständige Anbieterangaben und Anschrift: <a href="https://minh.systems/impressum/">minh.systems/impressum</a>. Kontakt zum Datenschutz: {mail(t, "Datenschutz Gute Nacht, Spielzeug")}</p>
<h2>2. Keine Datenerhebung</h2>
<ul>
<li>Die App erhebt keine personenbezogenen Daten – weder von Kindern noch von Eltern.</li>
<li>Es gibt keine Analyse- oder Statistikdienste, keine Werbung, keine Tracking- oder Drittanbieter-SDKs.</li>
<li>Die App baut keine Netzwerkverbindungen auf und funktioniert vollständig offline.</li>
<li>Es gibt kein Benutzerkonto und keine Möglichkeit, Inhalte zu teilen oder mit anderen zu kommunizieren.</li>
</ul>
<h2>3. Speicherung auf dem Gerät</h2>
<p>Einstellungen (z. B. Lautstärke, Sprache, Hilfestufe) und der Spielfortschritt werden ausschließlich lokal auf deinem Gerät gespeichert und nie an uns übertragen. Wenn du die App löschst, werden diese Daten entfernt.</p>
<h2>4. In-App-Kauf</h2>
<p>Der Kauf „Alle Bücher“ wird vollständig von Apple über den App Store (StoreKit) abgewickelt. Wir erhalten keine Zahlungsdaten, keine Apple-ID und keine sonstigen persönlichen Daten. Es gilt die <a href="https://www.apple.com/de/legal/privacy/">Datenschutzrichtlinie von Apple</a>. Der Kaufbereich liegt hinter einer Elternsperre.</p>
<h2>5. Kinder</h2>
<p>Die App richtet sich an Kinder von 3 bis 6 Jahren und erfüllt die Anforderungen der Kategorie „Kinder“ im App Store. Da wir keinerlei Daten erheben, werden auch keine Daten von Kindern im Sinne von COPPA (USA) oder Art. 8 DSGVO verarbeitet. Links nach außen, Käufe und Einstellungen sind nur über die Elternsperre erreichbar.</p>
<h2>6. Deine Rechte</h2>
<p>Da wir keine personenbezogenen Daten über dich oder dein Kind verarbeiten, gibt es nichts, was wir beauskunften, berichtigen oder löschen könnten. Bei Fragen kannst du dich jederzeit an uns wenden. Du hast außerdem das Recht, dich bei einer Datenschutz-Aufsichtsbehörde zu beschweren.</p>
<h2>7. Diese Website</h2>
<p>Diese Website wird über GitHub Pages (GitHub, Inc.) bereitgestellt. GitHub kann beim Aufruf technisch notwendige Daten wie die IP-Adresse zu Sicherheitszwecken protokollieren; siehe <a href="https://docs.github.com/de/site-policy/privacy-policies/github-general-privacy-statement">Datenschutzerklärung von GitHub</a>. Die Website verwendet keine Cookies, keine Analyse und lädt keine externen Schriften oder Inhalte von Drittservern. Weitere Informationen: <a href="https://minh.systems/datenschutz/">Datenschutzerklärung von Minh Nguyen Studios</a>.</p>
<h2>8. Änderungen</h2>
<p>Ändert sich die App so, dass dies den Datenschutz betrifft, aktualisieren wir diese Erklärung vorher.</p>
</div></div>"""
    return f"""<div class="page"><div class="wrap">
<h1>App Privacy Policy</h1>
<p class="lead">“Good Night, Toys” (iPhone &amp; iPad) – last updated October 2026</p>
<div class="box"><strong>In short:</strong> The app does not collect, store or transmit any personal data. No ads, no analytics, no tracking, no account, no network connections.</div>
<h2>1. Controller</h2>
<p>Minh Nguyen Studios. Full company details and address: <a href="https://minh.systems/impressum/">minh.systems/impressum</a>. Privacy contact: {mail(t, "Privacy Good Night, Toys")}</p>
<h2>2. No data collection</h2>
<ul>
<li>The app collects no personal data – neither from children nor from parents.</li>
<li>There are no analytics or statistics services, no advertising, no tracking or third-party SDKs.</li>
<li>The app makes no network requests and works completely offline.</li>
<li>There is no user account and no way to share content or communicate with others.</li>
</ul>
<h2>3. Storage on the device</h2>
<p>Settings (e.g. volume, language, help level) and progress are stored only locally on your device and are never sent to us. Deleting the app removes this data.</p>
<h2>4. In-app purchase</h2>
<p>The “All Books” purchase is handled entirely by Apple through the App Store (StoreKit). We never receive payment details, your Apple ID or any other personal data. <a href="https://www.apple.com/legal/privacy/">Apple's privacy policy</a> applies. The purchase area is behind a parental gate.</p>
<h2>5. Children</h2>
<p>The app is designed for children aged 3 to 6 and meets the requirements of the App Store Kids category. Because we collect no data at all, no children's data is processed within the meaning of COPPA (USA) or Art. 8 GDPR (GDPR-K). External links, purchases and settings are only reachable through the parental gate.</p>
<h2>6. Your rights</h2>
<p>As we do not process any personal data about you or your child, there is nothing we could disclose, correct or delete. You can contact us with any questions at any time. You also have the right to lodge a complaint with a data protection supervisory authority.</p>
<h2>7. This website</h2>
<p>This website is hosted on GitHub Pages (GitHub, Inc.). GitHub may log technical data such as IP addresses for security purposes; see the <a href="https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement">GitHub Privacy Statement</a>. The website uses no cookies, no analytics and loads no external fonts or content from third-party servers. More: <a href="https://minh.systems/datenschutz/">Minh Nguyen Studios privacy policy</a>.</p>
<h2>8. Changes</h2>
<p>If the app ever changes in a way that affects privacy, we will update this policy beforehand.</p>
</div></div>"""


PAGES = [
 ("de", "", "Gute Nacht, Spielzeug – das ruhige Gute-Nacht-Bilderbuch für iPhone & iPad",
  "Interaktives Gute-Nacht-Bilderbuch für Kinder von 3–6: Spielzeug ins Bett bringen, Licht aus, Mond ins Fenster. Ohne Lesen, ohne Werbung, ohne Datensammlung.", home_de, True),
 ("en", "", "Good Night, Toys – the calm bedtime picture book for iPhone & iPad",
  "Interactive bedtime picture book for ages 3–6: put the toys to bed, switch off the light, hang the moon in the window. No reading, no ads, no data collection.", home_en, True),
 ("de", "support/", "Hilfe & Support – Gute Nacht, Spielzeug", "Antworten zu Kauf wiederherstellen, Elternbereich, Familienfreigabe und Sprachen – und Kontakt zum Support.", lambda: support("de"), False),
 ("en", "support/", "Help & Support – Good Night, Toys", "Answers about restoring purchases, the parent area, Family Sharing and languages – plus support contact.", lambda: support("en"), False),
 ("de", "privacy/", "Datenschutzerklärung der App – Gute Nacht, Spielzeug", "Die App Gute Nacht, Spielzeug erhebt keine Daten: keine Werbung, keine Analyse, kein Tracking, keine Netzwerkverbindungen.", lambda: privacy("de"), False),
 ("en", "privacy/", "App Privacy Policy – Good Night, Toys", "Good Night, Toys collects no data: no ads, no analytics, no tracking, no network requests.", lambda: privacy("en"), False),
]

for lang, path, title, desc, fn, home in PAGES:
    out = ROOT / T[lang]["pre"] / path / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(layout(lang, path, title, desc, fn(), home), encoding="utf-8")

urls = "".join(f"<url><loc>{SITE}{T[l]['pre']}{p}</loc></url>" for l, p, *_ in PAGES)
(ROOT / "sitemap.xml").write_text(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>\n')
print("ok")
