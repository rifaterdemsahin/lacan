#!/usr/bin/env python3
"""Build TR (chart images) + EN (SVG) pages, language gate, redirects, favicon."""
from pathlib import Path
from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parents[1]
SVG = ROOT / "assets" / "svg"
TR = ROOT / "tr"
EN = ROOT / "en"
for p in (SVG, TR, EN):
    p.mkdir(parents=True, exist_ok=True)

C = {
    "blue": "#2c4a7c", "green": "#2f6a45", "red": "#7a2436",
    "purple": "#5a3d7a", "teal": "#2a5f62", "gold": "#b68a3a",
    "ink": "#1c1420", "soft": "#3a3040", "paper": "#fffdf8",
    "line": "#d8cbb6",
}

def svg_doc(w, h, inner, title=""):
    t = f'<title>{title}</title>' if title else ""
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img" aria-label="{title}">
{t}
<rect width="{w}" height="{h}" fill="{C["paper"]}"/>
{inner}
</svg>
'''

def flow_svg(name, title, steps):
    n = len(steps)
    w, h = 1100, 260
    gap = 14
    left = 24
    box_w = (w - left * 2 - gap * (n - 1)) / n
    parts = [f'<text x="24" y="32" font-family="Georgia, serif" font-size="20" fill="{C["ink"]}">{title}</text>']
    for i, (color, emoji, label, sub) in enumerate(steps):
        x = left + i * (box_w + gap)
        y = 52
        parts.append(f'<rect x="{x}" y="{y}" width="{box_w}" height="180" rx="8" fill="#fff" stroke="{color}" stroke-width="2"/>')
        parts.append(f'<text x="{x + 12}" y="{y + 28}" font-size="13" fill="{color}" font-family="sans-serif">{i+1}  {emoji}</text>')
        parts.append(f'<text x="{x + 12}" y="{y + 58}" font-size="16" font-weight="700" fill="{C["ink"]}" font-family="Georgia, serif">{label}</text>')
        # wrap sub roughly
        words = sub.split()
        line, lines, y0 = "", [], y + 82
        for word in words:
            trial = (line + " " + word).strip()
            if len(trial) > 18:
                lines.append(line)
                line = word
            else:
                line = trial
        if line:
            lines.append(line)
        for j, ln in enumerate(lines[:5]):
            parts.append(f'<text x="{x + 12}" y="{y0 + j*18}" font-size="12" fill="{C["soft"]}" font-family="sans-serif">{ln}</text>')
        if i < n - 1:
            ax = x + box_w + 2
            parts.append(f'<text x="{ax}" y="{y + 90}" font-size="16" fill="{C["gold"]}">→</text>')
    (SVG / f"{name}.svg").write_text(svg_doc(w, h, "\n".join(parts), title), encoding="utf-8")

def rings_svg():
    inner = f'''
    <text x="24" y="36" font-family="Georgia, serif" font-size="22" fill="{C["ink"]}">RSI · three registers</text>
    <circle cx="280" cy="175" r="88" fill="none" stroke="{C["green"]}" stroke-width="14"/>
    <circle cx="360" cy="230" r="88" fill="none" stroke="{C["blue"]}" stroke-width="14"/>
    <circle cx="440" cy="175" r="88" fill="none" stroke="{C["red"]}" stroke-width="14"/>
    <circle cx="800" cy="200" r="70" fill="none" stroke="{C["gold"]}" stroke-width="10" stroke-dasharray="8 6"/>
    <text x="230" y="90" fill="{C["green"]}" font-size="16">🟢 Imaginary</text>
    <text x="430" y="90" fill="{C["red"]}" font-size="16">🔴 Real</text>
    <text x="318" y="340" fill="{C["blue"]}" font-size="16">🔵 Symbolic</text>
    <text x="730" y="110" fill="{C["gold"]}" font-size="16">🪢 Sinthome</text>
    <text x="720" y="300" font-size="13" fill="{C["soft"]}" font-family="sans-serif">Fourth ring</text>
    <text x="24" y="370" font-size="13" fill="{C["soft"]}" font-family="sans-serif">Cut one ring and the knot falls. The sinthome can hold what the paternal metaphor did not.</text>
    '''
    (SVG / "rsi.svg").write_text(svg_doc(1100, 400, inner, "Three registers"), encoding="utf-8")

def columns_svg(name, title, cols):
    n = len(cols)
    w, h = 1100, 340
    gap = 16
    left = 24
    box_w = (w - left * 2 - gap * (n - 1)) / n
    parts = [f'<text x="24" y="32" font-family="Georgia, serif" font-size="20" fill="{C["ink"]}">{title}</text>']
    for i, (color, emoji, label, lines) in enumerate(cols):
        x = left + i * (box_w + gap)
        parts.append(f'<rect x="{x}" y="50" width="{box_w}" height="270" rx="8" fill="#fff" stroke="{color}" stroke-width="2"/>')
        parts.append(f'<rect x="{x}" y="50" width="{box_w}" height="8" rx="4" fill="{color}"/>')
        parts.append(f'<text x="{x + 14}" y="90" font-size="22">{emoji}</text>')
        parts.append(f'<text x="{x + 14}" y="120" font-size="16" font-weight="700" font-family="Georgia, serif" fill="{C["ink"]}">{label}</text>')
        for j, ln in enumerate(lines):
            parts.append(f'<text x="{x + 14}" y="{150 + j*22}" font-size="13" fill="{C["soft"]}" font-family="sans-serif">{ln}</text>')
    (SVG / f"{name}.svg").write_text(svg_doc(w, h, "\n".join(parts), title), encoding="utf-8")

def loop_svg():
    labels = [
        (80, 200, "1 👁️", "Other's lack"),
        (250, 80, "2 🔁", "Drive"),
        (520, 60, "3 ❤️", "Desire"),
        (780, 80, "4 🔥", "Jouissance"),
        (930, 200, "5 ○", "Lack returns"),
        (520, 320, "6 🌀", "New orbit"),
    ]
    parts = [f'<text x="24" y="32" font-family="Georgia, serif" font-size="20" fill="{C["ink"]}">Jouissance is a loop, not a prize</text>']
    parts.append(f'<ellipse cx="550" cy="200" rx="360" ry="130" fill="none" stroke="{C["gold"]}" stroke-width="2" stroke-dasharray="6 6"/>')
    for x, y, e, t in labels:
        parts.append(f'<rect x="{x}" y="{y}" width="160" height="54" rx="8" fill="#fff" stroke="{C["line"]}"/>')
        parts.append(f'<text x="{x+10}" y="{y+22}" font-size="13">{e}</text>')
        parts.append(f'<text x="{x+10}" y="{y+42}" font-size="13" fill="{C["soft"]}" font-family="sans-serif">{t}</text>')
    (SVG / "jouissance.svg").write_text(svg_doc(1100, 400, "\n".join(parts), "Jouissance loop"), encoding="utf-8")

def uml_svg():
    inner = f'''
    <text x="24" y="32" font-family="Georgia, serif" font-size="20" fill="{C["ink"]}">«interface» Subjectivation</text>
    <rect x="40" y="50" width="1020" height="70" rx="8" fill="#fff" stroke="{C["ink"]}" stroke-width="1.5"/>
    <text x="60" y="80" font-size="14" font-family="sans-serif">⚡ Trauma (Real)  →  📘 Meaning (Symbolic)  →  🪞 Proof (Imaginary)  →  💜 Symptom  →  🎯 Existence</text>
    <text x="60" y="102" font-size="12" fill="{C["soft"]}" font-family="sans-serif">Every structure must realize this interface in its own idiom.</text>
    '''
    boxes = [
        (40, "🔒 Obsessive", C["blue"], "rules / delay"),
        (300, "❓ Hysteric", C["red"], "question / gaze"),
        (560, "🎭 Perverse", C["green"], "scene / fetish"),
        (820, "⚡ Psychotic", C["purple"], "homemade order"),
    ]
    for x, title, color, sub in boxes:
        inner += f'<rect x="{x}" y="160" width="240" height="140" rx="8" fill="#fff" stroke="{color}" stroke-width="2"/>'
        inner += f'<text x="{x+16}" y="198" font-size="16" font-family="Georgia, serif" fill="{C["ink"]}">{title}</text>'
        inner += f'<text x="{x+16}" y="228" font-size="13" fill="{C["soft"]}" font-family="sans-serif">«structure»</text>'
        inner += f'<text x="{x+16}" y="258" font-size="13" fill="{C["soft"]}" font-family="sans-serif">{sub}</text>'
        inner += f'<line x1="{x+120}" y1="160" x2="550" y2="120" stroke="{C["gold"]}" stroke-dasharray="4 4"/>'
    (SVG / "uml.svg").write_text(svg_doc(1100, 340, inner, "UML model"), encoding="utf-8")

def dopamine_svg():
    inner = f'''
    <text x="24" y="32" font-family="Georgia, serif" font-size="20" fill="{C["ink"]}">Parallel, not identical</text>
    <rect x="40" y="60" width="420" height="240" rx="8" fill="#fff" stroke="{C["blue"]}" stroke-width="2"/>
    <text x="60" y="95" font-size="18" fill="{C["blue"]}"> Lacan</text>
    <text x="60" y="130" font-size="14" font-family="sans-serif">lack · Other · objet a</text>
    <text x="60" y="155" font-size="14" font-family="sans-serif">desire · drive · symptom</text>
    <text x="60" y="180" font-size="14" font-family="sans-serif">🔥 jouissance (structural)</text>
    <rect x="640" y="60" width="420" height="240" rx="8" fill="#fff" stroke="{C["teal"]}" stroke-width="2"/>
    <text x="660" y="95" font-size="18" fill="{C["teal"]}">🧠 Dopamine system</text>
    <text x="660" y="130" font-size="14" font-family="sans-serif">cue · craving · action</text>
    <text x="660" y="155" font-size="14" font-family="sans-serif">dip · search again</text>
    <text x="660" y="180" font-size="14" font-family="sans-serif">chemical motor of wanting</text>
    <text x="500" y="190" font-size="28" fill="{C["red"]}" font-weight="700">≠</text>
    <text x="40" y="330" font-size="13" fill="{C["soft"]}" font-family="sans-serif">Dopamine can accompany desire. It is not jouissance.</text>
    '''
    (SVG / "dopamine.svg").write_text(svg_doc(1100, 360, inner, "Lacan and dopamine"), encoding="utf-8")

# --- generate SVGs ---
flow_svg("cycle", "Six-step cycle", [
    (C["blue"], "📘", "Meaning", "Symbolic: what am I in language?"),
    (C["green"], "🪞", "Proof", "Imaginary: confirm value in a gaze"),
    (C["red"], "⚡", "Trauma", "Real: lack, loss, the impossible"),
    (C["purple"], "💜", "Symptom", "A costly original reply"),
    (C["teal"], "ƒ", "Formula", "The reply becomes an algorithm"),
    (C["gold"], "🪢", "Sinthome", "A knot one can live"),
])
rings_svg()
columns_svg("structures", "Clinical structures · positions, not types", [
    (C["blue"], "🔒", "Obsessive", ["Avoids Real via rules", "Proof: I do it right", "Object: control"]),
    (C["red"], "❓", "Hysteric", ["Avoids Real via questions", "Proof: I am wanted", "Object: gaze"]),
    (C["green"], "🎭", "Perverse", ["Stages Other's jouissance", "Proof: I run the scene", "Object: fetish"]),
    (C["purple"], "⚡", "Psychotic", ["Homemade Symbolic", "Proof: my world is true", "Object: stabilizer"]),
    (C["gold"], "⭐", "Ethical", ["Admits lack", "Loyal to own desire", "Object: sinthome"]),
])
columns_svg("objet-a", "Objet petit a · what each structure holds", [
    (C["blue"], "🔑", "Control", ["ritual, work, plan", "limit jouissance"]),
    (C["red"], "👀", "Gaze", ["look, like, chosen", "keep desire alive"]),
    (C["green"], "🎭", "Fetish", ["thing / scene / tech", "cover castration"]),
    (C["purple"], "🎧", "Stabilizer", ["system, number, voice", "hold the world"]),
    (C["gold"], "⭐", "Sinthome", ["craft, writing, practice", "knot lack"]),
])
columns_svg("desire-drive", "Not synonyms", [
    (C["teal"], "🔁", "Drive (Trieb)", ["circles the hole", "satisfaction in the loop", "not a GPS to an object"]),
    (C["red"], "💫", "Desire (Désir)", ["aims at the missing", "desire of the Other", "never fully filled"]),
    (C["purple"], "🔥", "Jouissance", ["surplus beyond pleasure", "pain mixed in", "reproduces lack"]),
])
columns_svg("big-other", "Other vs other", [
    (C["green"], "🪞", "other (imaginary)", ["counterpart, rival, peer", "the image I compare", "proof lives here"]),
    (C["blue"], "👁️", "Other (symbolic)", ["law, language, A", "treasury of signifiers", "meaning lives here"]),
    (C["gold"], "📛", "Name-of-the-Father", ["a function, not a dad", "installs a limit", "foreclosed in psychosis"]),
])
flow_svg("formula", "A formula is a life-algorithm", [
    (C["blue"], "🔒", "Obsessive", "If I control, I am safe"),
    (C["red"], "❓", "Hysteric", "If you keep wanting, I exist"),
    (C["green"], "🎭", "Perverse", "If I run the scene, lack hides"),
    (C["purple"], "⚡", "Psychotic", "My system holds the world"),
])
flow_svg("attachment", "From trauma to an object", [
    (C["red"], "⚡", "Trauma", "Encounter with lack"),
    (C["gold"], "😰", "Anxiety", "Pressure around the hole"),
    (C["purple"], "💜", "Symptom", "A defense / enjoyment"),
    (C["teal"], "🧲", "Object bind", "Regulates anxiety a while"),
    (C["blue"], "➡️", "Fork", "Freeze or sinthome"),
])
flow_svg("parental", "Parents as first Big Other", [
    (C["blue"], "⚖️", "Law", "Obsessive: judge of right"),
    (C["red"], "❤️", "Love-gaze", "Hysteric: the one who chooses"),
    (C["green"], "👑", "Power", "Perverse: throne to use"),
    (C["purple"], "🌍", "World-hold", "Psychotic: guarantor of reality"),
    (C["gold"], "⭐", "Ethical", "Love without fusion"),
])
loop_svg()
uml_svg()
dopamine_svg()
columns_svg("obsessive", "Obsessive position", [
    (C["blue"], "📘", "Meaning", ["rules, knowledge, order", "ambiguity feels like insult"]),
    (C["green"], "🪞", "Proof", ["competence, the good child", "never quite enough"]),
    (C["red"], "⚡", "Trauma", ["loss of control", "guilt without a named act"]),
    (C["purple"], "💜", "Symptom", ["checking, delay, ritual", "shield against the Real"]),
])
columns_svg("hysteric", "Hysteric position", [
    (C["red"], "❓", "Question", ["Che vuoi? What do you want?", "being referred to Other"]),
    (C["green"], "👀", "Proof", ["am I the special object?", "keep desire open"]),
    (C["purple"], "💜", "Symptom", ["complaint, conversion, riddle", "Other's desire stays in play"]),
    (C["gold"], "⭐", "Ethical turn", ["produce meaning from inside", "a form that can stand alone"]),
])
columns_svg("perverse", "Perverse position", [
    (C["green"], "🎭", "Scene", ["law used as a tool", "others as functions"]),
    (C["gold"], "🧩", "Fetish", ["I know, but even so", "plug for castration"]),
    (C["red"], "⚡", "Trauma", ["lack denied or dumped", "onto someone else's body"]),
    (C["teal"], "⭐", "Ethical turn", ["same gifts, not as traps", "making without props"]),
])
columns_svg("psychotic", "Psychotic position", [
    (C["purple"], "📛", "Foreclosure", ["Name-of-the-Father missing", "Real may invade"]),
    (C["blue"], "🏗️", "Homemade order", ["delusion as stabilization", "a world that must be true"]),
    (C["teal"], "🎧", "Stabilizer", ["voice, number, system, faith", "holds meaning together"]),
    (C["gold"], "🪢", "Sinthome", ["Joyce's writing as knot", "practice instead of demolition"]),
])
columns_svg("ethical", "Ethical / sinthomatic subject", [
    (C["gold"], "📘", "Meaning", ["kept open", "not a weapon or a cage"]),
    (C["gold"], "🪞", "Proof", ["a style offered", "not a verdict begged"]),
    (C["gold"], "⚡", "Trauma", ["lack admitted", "neither denied nor worshipped"]),
    (C["gold"], "🪢", "Knot", ["I am the agent of my desire", "a practice, not a trophy"]),
])
columns_svg("sinthome", "Symptom vs sinthome", [
    (C["purple"], "💜", "Symptom", ["repeats and hurts", "protects and enjoys", "hidden from the official story"]),
    (C["gold"], "🪢", "Sinthome", ["repetition as a style", "holds RSI together", "lack becomes livable"]),
    (C["blue"], "✍️", "Practice", ["writing, craft, love, discipline", "idiosyncratic on purpose", "must be fed or it tires"]),
])

print("svgs", len(list(SVG.glob("*.svg"))))

def wrap(lang, title, desc, kicker, h1, lede, body):
    return f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <link rel="icon" href="../favicon.ico" type="image/x-icon">
  <link rel="apple-touch-icon" href="../apple-touch-icon.png">
  <link rel="stylesheet" href="../assets/css/style.css">
</head>
<body data-base="../" data-lang="{lang}">
  <main class="wrap">
    <section class="hero">
      <p class="kicker">{kicker}</p>
      <h1>{h1}</h1>
      <p class="lede">{lede}</p>
    </section>
    {body}
  </main>
  <script src="../assets/js/site.js"></script>
</body>
</html>
'''

def img(src, alt, cap):
    return f'<figure class="visual"><img src="../images/{src}" alt="{alt}"><figcaption>{cap}</figcaption></figure>'

def svg(name, cap):
    return f'<figure class="visual"><img src="../assets/svg/{name}.svg" alt="{cap}"><figcaption>{cap}</figcaption></figure>'

def flow_html(items):
    out = ['<div class="flow">']
    tones = ["tone-blue","tone-green","tone-red","tone-purple","tone-teal","tone-gold"]
    for i, (emoji, title, text) in enumerate(items):
        tone = tones[i % 6]
        out.append(f'<article class="step {tone}"><div class="n">{i+1} · {emoji}</div><h3>{title}</h3><p>{text}</p></article>')
    out.append("</div>")
    return "\n".join(out)

# Each slug: {en: (title,desc,kicker,h1,lede,body), tr: ...}
def cards(items):
    grid = "grid-3" if len(items) >= 3 else "grid-2"
    out = [f'<div class="grid {grid}">']
    for tone, chip, h, p, href in items:
        more = f'<a class="more" href="{href}">→</a>' if href else ""
        out.append(f'<article class="card {tone}"><span class="chip">{chip}</span><h3>{h}</h3><p>{p}</p>{more}</article>')
    out.append("</div>")
    return "\n".join(out)

PAGES = {}

PAGES["index.html"] = {
"en": (
"🏠 Lacan Concepts",
"Visual encyclopedia of Lacanian structures, in English with SVG maps.",
"Choose a map · SVG edition",
"How a subject makes meaning, proves itself, meets lack, and knots a life.",
"English pages draw the concepts in SVG. The original photo-charts live on the Turkish side. These are clinical maps, not diagnoses.",
flow_html([
    ("📘","Meaning","The subject asks what the world, and their own being, could mean."),
    ("🪞","Proof","They try to confirm their value in the gaze of the Other."),
    ("⚡","Trauma","Lack, loss, and the impossible show through the story."),
    ("💜","Symptom","A painful but original reply to that encounter."),
    ("ƒ","Formula","The symptom hardens into a repeated life algorithm."),
    ("🪢","Sinthome","A singular way of living with lack, rather than fleeing it."),
]) + svg("cycle", "SVG: the six-step cycle") +
"<h2>🧩 Clinical structures</h2><p>Positions toward the Symbolic, the Imaginary, the Real, and the desire of the Other — not personality types.</p>" +
cards([
    ("tone-blue","🔒 Neurosis","Obsessive","Avoids the Real through rules, delay, guilt, and control.","obsessive.html"),
    ("tone-red","❓ Neurosis","Hysteric","Avoids the Real by questioning. Proof is being wanted.","hysteric.html"),
    ("tone-green","🎭 Perversion","Perverse","Organizes the Other’s jouissance: staging, fetish, law as a tool.","perverse.html"),
    ("tone-purple","⚡ Psychosis","Psychotic","The Name-of-the-Father is foreclosed. Meaning is self-built.","psychotic.html"),
    ("tone-gold","⭐ Ethic","Ethical subject","Accepts lack and stays loyal to a chosen desire.","ethical-subject.html"),
    ("tone-teal","🪢 Knot","Sinthome","A fourth ring that holds RSI together.","sinthome.html"),
]) + svg("structures", "SVG: five positions") +
'<p class="note">⚠️ Teaching tools, not diagnostic labels. Each subject is singular.</p>'
),
"tr": (
"🏠 Lacan Kavramları",
"Lacancı yapıların görsel ansiklopedisi — orijinal çizelgelerle.",
"Harita seç · çizelge baskısı",
"Özne nasıl anlam üretir, kendini ispatlar, eksikle karşılaşır ve bir yaşam düğümler.",
"Türkçe sayfalar orijinal öğretim çizelgelerini gösterir. İngilizce tarafta aynı kavramlar SVG ile çizilir. Klinik harita, tanı değil.",
flow_html([
    ("📘","Anlam","Özne dünyanın ve kendi varlığının ne anlama geldiğini sorar."),
    ("🪞","İspat","Değerini Öteki'nin bakışında doğrulamaya çalışır."),
    ("⚡","Travma","Eksiklik, kayıp ve imkânsız hikâyeden sızar."),
    ("💜","Semptom","Bu karşılaşmaya acılı ama özgün bir yanıttır."),
    ("ƒ","Formül","Semptom tekrar eden bir yaşam algoritmasına sertleşir."),
    ("🪢","Sinthome","Eksiklikten kaçmadan onunla yaşamanın tekil yolu."),
]) + img("01-cycle-overview-all-structures.jpg", "Tüm yapılarda anlam-ispat-travma-semptom-formül-sinthome tablosu", "Ana çizelge: her yapı, her adım. 24 Temmuz 2026 tarihli WhatsApp dışa aktarımı, yeniden adlandırıldı.") +
"<h2>🧩 Klinik yapılar</h2><p>Simgesel, İmgesel, Gerçek ve Öteki'nin arzusu karşısında konumlar — kişilik tipleri değil.</p>" +
cards([
    ("tone-blue","🔒 Nevroz","Obsesif","Gerçek'ten kural, erteleme, suçluluk ve kontrol ile kaçar.","obsessive.html"),
    ("tone-red","❓ Nevroz","Histerik","Gerçek'ten soru sorarak kaçar. İspat: isteniyor olmak.","hysteric.html"),
    ("tone-green","🎭 Sapkınlık","Sapkın","Öteki'nin jouissance'ını sahne, fetiş ve yasa aleti ile düzenler.","perverse.html"),
    ("tone-purple","⚡ Psikoz","Psikotik","Baba-Adı forklüze edilmiştir. Anlam evde kurulur.","psychotic.html"),
    ("tone-gold","⭐ Etik","Etik özne","Eksikliği kabul eder; seçtiği arzuya sadık kalır.","ethical-subject.html"),
    ("tone-teal","🪢 Düğüm","Sinthome","RSI'yi tutan dördüncü halka.","sinthome.html"),
]) +
'<p class="note">⚠️ Öğretim aracı, tanı etiketi değil. Her özne tekildir.</p>'
)
}

PAGES["cycle.html"] = {
"en": (
"🔄 Six-step cycle", "Meaning, proof, trauma, symptom, formula, sinthome.",
"Anlam · İspat · Travma · Semptom · Formül · Sinthome",
"The six-step cycle",
"Every map in this archive is a variation on one sequence. English pages draw it in SVG.",
flow_html([("📘","Meaning","Symbolic. Who am I?"),("🪞","Proof","Imaginary. Confirm I count."),("⚡","Trauma","Real. Lack shows through."),("💜","Symptom","A costly reply."),("ƒ","Formula","A repeated strategy."),("🪢","Sinthome","A livable knot.")])
+ svg("cycle", "SVG map of the cycle")
+ "<h2>📘 1. Meaning</h2><p>The subject is thrown into language. Meaning is borrowed from the Other’s store of signifiers. If meaning must be complete, ambiguity panics the subject. The ethical move is to leave a place for the unknown.</p>"
+ "<h2>🪞 2. Proof</h2><p>Proof is the demand to be seen. Gaze, comparison, performance. A trap if it depends only on the Other’s stamp.</p>"
+ "<h2>⚡ 3. Trauma</h2><p>Not only an event: the encounter with lack. What does not fit the story. Structures differ by how they meet it.</p>"
+ "<h2>💜 4. Symptom</h2><p>Already a solution — a costly one. How jouissance is bound. A message and a mode of enjoyment.</p>"
+ "<h2>ƒ 5. Formula</h2><p>The symptom becomes an algorithm: if I control / if I keep asking / if I stage the scene. Frozen, it cages; living, it can be revised.</p>"
+ "<h2>🪢 6. Sinthome</h2><p>Not the absence of a symptom. The symptom reworked as a knot: a practice that holds Imaginary, Symbolic, and Real together.</p>"
),
"tr": (
"🔄 Altı adımlı döngü", "Anlam, ispat, travma, semptom, formül, sinthome.",
"Anlam · İspat · Travma · Semptom · Formül · Sinthome",
"Altı adımlı döngü",
"Arşivdeki her çizelge aynı dizinin bir çeşitlemesidir. Türkçe sayfa orijinal tabloyu gösterir.",
flow_html([("📘","Anlam","Simgesel. Ben kimim?"),("🪞","İspat","İmgesel. Sayılıyor muyum?"),("⚡","Travma","Gerçek. Eksik sızar."),("💜","Semptom","Pahalı bir yanıt."),("ƒ","Formül","Tekrar eden strateji."),("🪢","Sinthome","Yaşanabilir düğüm.")])
+ img("01-cycle-overview-all-structures.jpg", "Altı adımlı döngünün tüm yapılar üzerindeki ana tablosu", "Ana tablo: her yapının sorunu, çözümü ve çözülmezse ne olduğu.")
+ "<h2>📘 1. Anlam</h2><p>Özne dile atılır. Anlam, Öteki'nin gösteren deposundan ödünç alınır. Anlam tam olmak zorundaysa belirsizlik panik üretir. Etik hamle, bilinmeyene yer bırakmaktır.</p>"
+ "<h2>🪞 2. İspat</h2><p>İspat, görülme talebidir. Bakış, kıyas, performans. Yalnızca Öteki'nin damgasına bağlıysa tuzaktır.</p>"
+ "<h2>⚡ 3. Travma</h2><p>Yalnızca bir olay değil: eksiklikle karşılaşma. Hikâyeye sığmayan. Yapılar bunu karşılama biçimleriyle ayrılır.</p>"
+ "<h2>💜 4. Semptom</h2><p>Zaten bir çözümdür — pahalı bir çözüm. Jouissance'ın bağlanma biçimi. Hem mesaj hem keyif kipi.</p>"
+ "<h2>ƒ 5. Formül</h2><p>Semptom algoritma olur: kontrol edersem / sormaya devam edersem / sahneyi kurarsam. Donarsa kafes; yaşarsa mevsimlik olabilir.</p>"
+ "<h2>🪢 6. Sinthome</h2><p>Semptomun yokluğu değil. Semptomun düğüm olarak yeniden işlenmesi: İmgesel, Simgesel ve Gerçek'i tutan bir pratik.</p>"
)
}

PAGES["three-registers.html"] = {
"en": ("🟣 Three registers", "Imaginary, Symbolic, Real.", "RSI · Borromean knot",
"Imaginary, Symbolic, Real",
"Not layers of a mind: three ways experience is ordered. Meaning is Symbolic, proof Imaginary, trauma Real. The sinthome can be a fourth ring.",
svg("rsi", "SVG: three rings and a fourth")
+ "<h2>🟢 Imaginary</h2><p>Images, identification, the ego, the gaze, rivalry. Where the subject looks for proof.</p>"
+ "<h2>🔵 Symbolic</h2><p>Language, law, kinship, the Name-of-the-Father, the Big Other. Where the subject looks for meaning.</p>"
+ "<h2>🔴 Real</h2><p>What will not be imaged or said. Lack, jouissance, leftover. Where the cycle meets the impossible.</p>"
+ "<p>A Borromean knot: cut one ring and all three fall. Psychosis is a failure of the Symbolic knot. A sinthome can restitch what the paternal metaphor did not hold.</p>"
),
"tr": ("🟣 Üç düzen", "İmgesel, Simgesel, Gerçek.", "RSI · Borromean düğüm",
"İmgesel, Simgesel, Gerçek",
"Zihnin katmanları değil: deneyimin düzenlendiği üç yol. Anlam Simgesel, ispat İmgesel, travma Gerçek. Sinthome dördüncü halka olabilir.",
img("16-trauma-meaning-proof-symptom-tr.jpg", "Travma anlam ispat semptom sürecinin Türkçe tablosu", "Süreç tablosu RSI'yi sütunlara yazar: Gerçek → Simgesel → İmgesel → jouissance.")
+ "<h2>🟢 İmgesel</h2><p>İmgeler, özdeşleşme, ego, bakış, rekabet. Öznenin ispat aradığı yer.</p>"
+ "<h2>🔵 Simgesel</h2><p>Dil, yasa, akrabalık, Baba-Adı, Büyük Öteki. Anlamın arandığı yer.</p>"
+ "<h2>🔴 Gerçek</h2><p>İmgeye ve söze girmeyen. Eksiklik, jouissance, artık. Döngünün imkânsızla karşılaştığı yer.</p>"
+ "<p>Borromean düğüm: bir halka kesilirse üçü de düşer. Psikoz, Simgesel düğümün tutmamasıdır. Sinthome, baba metaforunun tutmadığı yeri yeniden dikebilir.</p>"
)
}

def pair(en_t, tr_t, en_body, tr_body, en_svg, tr_imgs, extra_en="", extra_tr=""):
    title_en, desc_en, kick_en, h1_en, lede_en = en_t
    title_tr, desc_tr, kick_tr, h1_tr, lede_tr = tr_t
    return {
        "en": (title_en, desc_en, kick_en, h1_en, lede_en, en_body + svg(en_svg, title_en) + extra_en),
        "tr": (title_tr, desc_tr, kick_tr, h1_tr, lede_tr, tr_body + "".join(tr_imgs) + extra_tr),
    }

PAGES["structures.html"] = pair(
    ("🧩 Clinical structures", "Four structures plus the ethical subject.", "Position, not personality", "Clinical structures", "Obsession and hysteria are neuroses. Perversion is another relation to the law. Psychosis is another relation to the Symbolic. The fifth row is an ethic of desire."),
    ("🧩 Klinik yapılar", "Dört yapı ve etik özne.", "Konum, kişilik değil", "Klinik yapılar", "Obsesyon ve histeri nevroza aittir. Sapkınlık yasayla başka bir ilişkidir. Psikoz Simgesel'le başka bir ilişkidir. Beşinci satır arzu etiğidir."),
    "<p>The UML idea: subjectivation is an interface every structure must implement.</p>",
    "<p>UML fikri: özneleşme, her yapının gerçekleştirmek zorunda olduğu bir arayüzdür.</p>",
    "structures",
    [img("16-trauma-meaning-proof-symptom-tr.jpg", "Yapılara göre travma-anlam-ispat-semptom tablosu", "Türkçe süreç tablosu: her yapının Gerçek'ten varoluşa yolu.")],
)

PAGES["obsessive.html"] = pair(
    ("🔒 Obsessive", "Rules, delay, guilt, control.", "Neurosis · control", "The obsessive subject", "Meets the Big Other as comply-or-be-wrong. Safety is sought in rules, thought, and postponement."),
    ("🔒 Obsesif", "Kural, erteleme, suçluluk, kontrol.", "Nevroz · kontrol", "Obsesif özne", "Büyük Öteki'yi uy-ya da-yanlış-ol olarak karşılar. Güvenlik kural, düşünce ve ertelemede aranır."),
    "<p>Meaning from rules. Proof as competence. Trauma as loss of control. Symptom as ritual and rumination.</p>" + svg("obsessive", "SVG: obsessive position"),
    "<p>Anlam kurallardan. İspat yetkinlik. Travma kontrol kaybı. Semptom ritüel ve ruminasyon.</p>",
    "formula",
    [img("02-cycle-obsessive-smart-vs-average.jpg", "Zeki bilgili ve vasat obsesif öznelerin döngü tablosu", "İki satır, aynı yapı: bilgi-ağır ve kural-izleyen."),
     img("05-cycle-obsessive-to-ethical.jpg", "Obsesiften etik özneye", "Kontrol döngüsü ile yaratıcı döngü.")],
)

PAGES["hysteric.html"] = pair(
    ("❓ Hysteric", "The question to the Other's desire.", "Neurosis · Che vuoi?", "The hysteric subject", "Organized around: what do you want? What am I for you? Desire stays alive by not closing the answer."),
    ("❓ Histerik", "Öteki'nin arzusuna soru.", "Nevroz · Che vuoi?", "Histerik özne", "Ne istiyorsun? Senin için neyim? Cevabı kapatmamak arzuyu canlı tutar."),
    "<p>Not a theatrical personality. Being is referred to the Other’s desire. The gaze object is typical.</p>" + svg("hysteric", "SVG: hysteric position"),
    "<p>Tiyatro kişiliği değil. Varlık Öteki'nin arzusuna gönderilir. Tipik nesne bakış nesnesidir.</p>",
    "hysteric",
    [img("03-cycle-hysteric.jpg", "Histerik döngü tablosu", "Sorgulayan döngü ve etik karşılığı."),
     img("07-cycle-hysteric-to-ethical.jpg", "Histerikten etik özneye", "Soru döngüsü / yaratıcı döngü.")],
)

PAGES["perverse.html"] = pair(
    ("🎭 Perverse", "Staging, fetish, disavowal.", "Disavowal · scene", "The perverse subject", "Not a moral insult: a position that disavows lack and tries to be the instrument of the Other's jouissance."),
    ("🎭 Sapkın", "Sahne, fetiş, yadsıma.", "Yadsıma · sahne", "Sapkın özne", "Ahlaki hakaret değil: eksikliği yadsıyan ve Öteki'nin jouissance'ının aleti olmaya çalışan bir konum."),
    "<p>Freud’s fetishist knows very well, but even so. The fetish plugs castration. The ethical turn keeps the gifts — scene-making, intensity — without turning people into props.</p>" + svg("perverse", "SVG: perverse position"),
    "<p>Freud'un fetişisti pekâlâ bilir, yine de. Fetiş hadım edilmeyi tıkar. Etik dönüş, sahne kurma yeteneğini insanları aksesuar etmeden kullanır.</p>",
    "perverse",
    [img("06-cycle-perverse.jpg", "Sapkın döngü tablosu", "Manipülatif döngü ve yaratıcı döngü."),
     img("08-cycle-perverse-to-ethical.jpg", "Sapkından etik özneye", "Öteki'nin jouissance'ını düzenlemek / kendi düğümünü kurmak.")],
)

PAGES["psychotic.html"] = pair(
    ("⚡ Psychotic", "Foreclosure of the Name-of-the-Father.", "Foreclosure · homemade Symbolic", "The psychotic subject", "Not more neurosis: a different knot. What neurosis represses, psychosis may meet as invasion."),
    ("⚡ Psikotik", "Baba-Adı'nın forklüzyonu.", "Forklüzyon · ev yapımı Simgesel", "Psikotik özne", "Daha fazla nevroz değil: başka bir düğüm. Nevrozun bastırdığını psikoz istila olarak karşılayabilir."),
    "<p>A private order (delusion, system) is already an attempt to stabilize the Real. Late Lacan reads Joyce’s writing as a sinthome. Help find a knot — music, craft, rhythm — rather than only tearing the private order down.</p>" + svg("psychotic", "SVG: psychotic position"),
    "<p>Özel bir düzen (hezeyan, sistem) Gerçek'i sabitleme çabasıdır. Geç Lacan Joyce'un yazısını sinthome olarak okur. Yalnızca özel düzeni yıkmak yerine bir düğüm — müzik, zanaat, ritim — bulunmasına yardım.</p>",
    "psychotic",
    [img("04-cycle-psychotic.jpg", "Psikotik döngü tablosu", "Kırılgan anlam ve tutan düğüm."),
     img("09-cycle-psychotic-to-ethical.jpg", "Psikotikten etik özneye", "Kırılgan ev-yapımı dünyadan yaşanabilir düğüme.")],
)

PAGES["ethical-subject.html"] = pair(
    ("⭐ Ethical subject", "Loyalty to a chosen desire.", "Sinthomatic subject", "The ethical subject", "Not a fifth pathology. Accept lack, stop using the Other as a guarantee, take responsibility for unconscious desire."),
    ("⭐ Etik özne", "Seçilmiş arzuya sadakat.", "Sinthomatik özne", "Etik özne", "Beşinci bir patoloji değil. Eksikliği kabul et, Öteki'yi garanti olarak kullanmayı bırak, bilinçdışı arzunun sorumluluğunu al."),
    "<p>Not moralism. An ethic of desire: I will not outsource my being, nor cover lack by making someone else into a scene, nor freeze life into a perfect rule.</p>" + svg("ethical", "SVG: ethical / sinthomatic subject"),
    "<p>Ahlakçılık değil. Arzu etiği: varlığımı dışarıya ihale etmem; eksikliği başkasını sahne ederek örtmem; hayatı mükemmel kurala dondurmam.</p>",
    "ethical",
    [img("13-choosing-unconscious-desire.jpg", "Bilinçdışı arzuyu seçme koşulları", "Kısa tablo."),
     img("14-choosing-unconscious-desire-detailed.jpg", "Objet a, semblant, jouissance ve dürtü ile ayrıntılı tablo", "Son hücre: Arzunun faili benim.")],
)

PAGES["sinthome.html"] = pair(
    ("🪢 Sinthome", "Fourth ring, Seminar XXIII.", "Fourth ring", "Sinthome", "Lacan respells symptôme as sinthome: not a coded message to delete, but a singular know-how that knots a life."),
    ("🪢 Sinthome", "Dördüncü halka, Seminer XXIII.", "Dördüncü halka", "Sinthome", "Lacan symptôme'u sinthome diye yeniden heceler: silinecek şifreli mesaj değil, yaşamı düğümleyen tekil bir know-how."),
    "<p>Joyce is the literary case. The charts translate that into ordinary clinic: a practice that holds RSI. A knot is a practice, not a trophy — if unfed it becomes a tired duty.</p>" + svg("sinthome", "SVG: symptom vs sinthome") + svg("rsi", "SVG: fourth ring around RSI"),
    "<p>Joyce edebi örnektir. Çizelgeler bunu sıradan kliniğe çevirir: RSI'yi tutan bir pratik. Düğüm kupa değil pratiktir — beslenmezse yorgun bir vazife olur.</p>",
    "sinthome",
    [img("01-cycle-overview-all-structures.jpg", "Sinthome hedefi içeren ana döngü tablosu", "Neredeyse her çizelge aynı kutuyu basar: üç düzeni düğümle, eksiklikle barış, tekil bir yaşam sür.")],
)

PAGES["objet-petit-a.html"] = pair(
    ("🎯 Objet petit a", "Object-cause of desire.", "Leftover that makes us want", "Objet petit a", "Not an object we have: the leftover that makes us want. Gaze, voice, a scene, a nothing that glows."),
    ("🎯 Objet petit a", "Arzunun nesne-nedeni.", "İstememizi sağlayan artık", "Objet petit a", "Sahip olduğumuz nesne değil: istememizi sağlayan artık. Bakış, ses, bir sahne, parlayan bir hiç."),
    "<p>After trauma, anxiety rises. Binding to an object is already a small solution. It can freeze as symptom or be reworked as sinthome.</p>" + svg("objet-a", "SVG: five typical objects"),
    "<p>Travmadan sonra kaygı yükselir. Bir nesneye bağlanmak zaten küçük bir çözümdür. Semptomda donabilir veya sinthome olarak işlenebilir.</p>",
    "objet-a",
    [img("10-object-attachment-objet-petit-a.jpg", "Yapılara göre objet petit a bağlanması", "Hangi nesne, hangi iş için."),
     img("11-object-attachment-stages-and-reasons.jpg", "Aşama aşama bağlanma nedenleri", "İhtiyaç, korku ve eksiklik her adımda nesneyi zorunlu kılar.")],
)

PAGES["object-attachment.html"] = pair(
    ("🧲 Object attachment", "Which object, why, at which step.", "Clinic of objet petit a", "How structures bind to objects", "Not a shopping list of hobbies: a logic of anxiety."),
    ("🧲 Nesne bağlanması", "Hangi nesne, neden, hangi adımda.", "Objet petit a kliniği", "Yapılar nesnelere nasıl bağlanır", "Hobi listesi değil: kaygının mantığı."),
    flow_html([("⚡","Trauma","Lack / jouissance"),("😰","Anxiety","Pressure"),("💜","Symptom","Defense"),("🧲","Bind","Object regulates"),("🪢","Fork","Freeze or knot")])
    + svg("attachment", "SVG: trauma to object"),
    flow_html([("⚡","Travma","Eksik / jouissance"),("😰","Kaygı","Basınç"),("💜","Semptom","Savunma"),("🧲","Bağ","Nesne düzenler"),("🪢","Çatal","Donma veya düğüm")]),
    "attachment",
    [img("10-object-attachment-objet-petit-a.jpg", "Nesne bağlanma tablosu", "Her yapının tuttuğu nesne."),
     img("11-object-attachment-stages-and-reasons.jpg", "Nedenleriyle bağlanma", "Altın kutu: bazıları semptomda kalır, bazıları sinthome'a çevirir.")],
)

PAGES["parental-attachment.html"] = pair(
    ("👨‍👩‍👧 Parental attachment", "Parents as first Big Other.", "The first Other", "Over-attachment to parental figures", "Parents often occupy the place of law, love, gaze — the one who seems to know."),
    ("👨‍👩‍👧 Ebeveyn bağlanması", "Ebeveynler ilk Büyük Öteki.", "İlk Öteki", "Ebeveyn figürlerine aşırı bağlanma", "Ebeveynler sık sık yasa, sevgi, bakış yerini — bilen yeri — tutar."),
    svg("parental", "SVG: how each structure uses the parent"),
    "<p>Sevgi, onay, aidiyet talebi çocukça değildir. Ebeveyn anlamın, ispatın ve sakinliğin tek garantisi kaldığında donar.</p>",
    "parental",
    [img("12-parental-over-attachment.jpg", "Ebeveynlere aşırı bağlanma tablosu", "Her adımda ebeveynin işlevi; etik satır kaynaşmasız sevgiyi yazar.")],
)

PAGES["jouissance.html"] = pair(
    ("🔥 Jouissance", "Beyond the pleasure principle.", "Surplus enjoyment", "Jouissance", "Not happiness. Surplus enjoyment: pleasure pushed past the limit, mixed with pain. What the symptom secretly serves."),
    ("🔥 Jouissance", "Haz ilkesinin ötesi.", "Fazla tatmin", "Jouissance", "Mutluluk değil. Fazla tatmin: hazzın sınırın ötesine itilmesi, acıyla karışması. Semptomun gizlice hizmet ettiği şey."),
    flow_html([("👁️","Other's lack","Something missing in the Other — and in me"),("🔁","Drive","Circles the hole"),("❤️","Desire","The circling is read as a wish"),("🔥","Jouissance","The circling itself produces surplus"),("○","Lack returns","It does not seal the hole"),("🌀","New desire","Another orbit")])
    + svg("jouissance", "SVG: jouissance as a loop") + svg("desire-drive", "SVG: drive, desire, jouissance"),
    flow_html([("👁️","Öteki'nin eksiği","Öteki'nde — ve bende — bir şey yok"),("🔁","Dürtü","Deliğin etrafında döner"),("❤️","Arzu","Dönüş bir dilek olarak okunur"),("🔥","Jouissance","Dönüşün kendisi fazlalık üretir"),("○","Eksik döner","Deliği kapatmaz"),("🌀","Yeni arzu","Yeni yörünge")]),
    "jouissance",
    [img("21-jouissance-drive-desire.jpg", "Jouissance süreci ve dürtü-arzu-jouissance karşılaştırması", "Döngü ve karşılaştırma tablosu.")],
)

PAGES["desire-and-drive.html"] = pair(
    ("💫 Desire and drive", "Désir, Trieb, manque.", "Not a need, not an instinct", "Desire and drive", "Need can be satisfied. Demand is spoken to the Other. Desire is what is left. Drive is the repetitive push around a hole."),
    ("💫 Arzu ve dürtü", "Désir, Trieb, manque.", "İhtiyaç değil, içgüdü değil", "Arzu ve dürtü", "İhtiyaç doyurulabilir. Talep Öteki'ye söylenir. Arzu artandır. Dürtü deliğin etrafındaki tekrarlı itkidir."),
    "<p>Desire is the desire of the Other: I want to be wanted, and my want is formatted by the Other’s signifiers. Drive does not arrive; satisfaction is in the circuit. That is why “just stop” is not a theory of change.</p>" + svg("desire-drive", "SVG: three terms"),
    "<p>Arzu Öteki'nin arzusudur: istenmek isterim ve isteğim Öteki'nin gösterenleriyle biçimlenir. Dürtü varmaz; tatmin devrededir. Bu yüzden “sadece bırak” bir değişim kuramı değildir.</p>",
    "desire-drive",
    [img("21-jouissance-drive-desire.jpg", "Dürtü, arzu ve jouissance tablosu", "Üç terimin görsel sözlüğü.")],
)

PAGES["big-other.html"] = pair(
    ("👁️ The Big Other", "Grand Autre, Name-of-the-Father.", "A, not a person", "The Big Other", "Not a person. The place of language, law, and presumed knowledge. We are spoken before we speak."),
    ("👁️ Büyük Öteki", "Grand Autre, Baba-Adı.", "A, bir kişi değil", "Büyük Öteki", "Bir kişi değil. Dil, yasa ve varsayılan bilginin yeri. Konuşmadan önce konuşuluruz."),
    svg("big-other", "SVG: other / Other / Name-of-the-Father"),
    "<p>Küçük öteki imgesel karşıktır. Büyük Öteki simgesel yasadır. Baba-Adı bir işlevdir, baba değil.</p>",
    "big-other",
    [img("12-parental-over-attachment.jpg", "Ebeveynlerin ilk Öteki olarak kullanımı", "İlk işgalciler çoğu zaman ebeveyn figürleridir."),
     img("16-trauma-meaning-proof-symptom-tr.jpg", "Yapıların Büyük Öteki ile ilişkisi", "Her yapı Öteki ile farklı bir sözleşme yapar.")],
)

PAGES["formula.html"] = pair(
    ("ƒ Formula", "Life strategy, f(x).", "Symptom as algorithm", "The formula", "Step five: the subject no longer only suffers a reply; they live by it."),
    ("ƒ Formül", "Yaşam stratejisi, f(x).", "Algoritma olarak semptom", "Formül", "Beşinci adım: özne yanıtı yalnızca çekmez; onunla yaşar."),
    svg("formula", "SVG: four typical formulas"),
    "<p>Donmuş formül esnekliği öldürür. Terapi formülü silmek değil; onu mevsimlik, paylaşılır ve bir arzuya sadık kılmaktır.</p>",
    "formula",
    [img("01-cycle-overview-all-structures.jpg", "Formül sütununu içeren ana tablo", "Beşinci sütun: yaşam stratejisi.")],
)

PAGES["dopamine.html"] = pair(
    ("🧠 Lacan and dopamine", "Parallel, not identical.", "Jouissance ≠ dopamine", "Lacan and dopamine", "Dopamine may accompany wanting. Jouissance is structural enjoyment knotted through lack, the Other, and repetition."),
    ("🧠 Lacan ve dopamin", "Paralel, özdeş değil.", "Jouissance ≠ dopamin", "Lacan ve dopamin", "Dopamin istemeye eşlik edebilir. Jouissance, eksiklik, Öteki ve tekrar üzerinden düğümlenen yapısal bir keyiftir."),
    svg("dopamine", "SVG: two languages, one subject, not one substance"),
    "<p>Çizelgenin uyarısı tezdir: jouissance dopamin değildir. Obsesif erteleme, histerik tanınma arayışı, sapkın sahne, psikotik kesinlik — hepsinde jouissance vardır ve hiçbiri tek bir ileticiye inmez.</p>",
    "dopamine",
    [img("15-lacan-and-dopamine.jpg", "Lacan ve dopamin yapısal paralellikler tablosu", "Daha doğru formül: dopamin arzunun biyolojik motorlarından biri olabilir; jouissance yapısal tatmin biçimidir.")],
)

PAGES["uml-model.html"] = pair(
    ("📐 UML model", "Interface, class, realization.", "Software-style map", "A software-style map of the same clinic", "Subjectivation is an interface. Obsessive, hysteric, perverse, psychotic are classes that realize it in different code. English pages draw that in SVG, not photographs."),
    ("📐 UML modeli", "Arayüz, sınıf, gerçekleştirme.", "Yazılım tarzı harita", "Aynı kliniğin yazılım tarzı haritası", "Özneleşme bir arayüzdür. Obsesif, histerik, sapkın, psikotik bunu farklı kodda gerçekleştiren sınıflardır."),
    svg("uml", "SVG: shared interface, four realizations") + svg("cycle", "SVG: the process those classes implement"),
    "<p>Ağustos çizimleri aynı fikri üç taslakta netleştirir. Öğretim diyagramıdır; ruhun Java programı olduğu iddiası değil.</p>",
    "uml",
    [img("16-trauma-meaning-proof-symptom-tr.jpg", "Türkçe süreç tablosu", "UML fikrinin sözel hali."),
     img("17-trauma-meaning-proof-symptom-en.jpg", "İngilizce süreç tablosu", "Türkçe terimlerin İngilizce eşi — yine de fotoğraf yalnızca TR tarafta."),
     img("18-uml-structures-v1.jpg", "UML taslak 1", "İlk soyut geçiş."),
     img("19-uml-structures-v2.jpg", "UML taslak 2", "Aktörler ve kırık Simgesel."),
     img("20-uml-structures-v3.jpg", "UML taslak 3", "En dolu lejant.")],
)

GLOSS_ROWS = [
    ("Anlam / Meaning", "Symbolic work of making world and I readable.", "Dünyayı ve ben'i okunur kılan Simgesel iş."),
    ("İspat / Proof", "Imaginary work of confirming value.", "Değeri doğrulayan İmgesel iş."),
    ("Travma / Trauma", "Encounter with the Real.", "Gerçek'le karşılaşma."),
    ("Semptom / Symptom", "Costly reply that binds jouissance.", "Jouissance'ı bağlayan pahalı yanıt."),
    ("Formül / Formula", "Symptom as life-algorithm.", "Yaşam algoritması olarak semptom."),
    ("Sinthome", "Singular knot; livable style.", "Tekil düğüm; yaşanabilir üslup."),
    ("Imaginary / İmgesel", "Images, ego, gaze.", "İmge, ego, bakış."),
    ("Symbolic / Simgesel", "Language, law, Other.", "Dil, yasa, Öteki."),
    ("Real / Gerçek", "What will not go into signifier.", "Gösterene girmeyen."),
    ("Big Other / Büyük Öteki", "Place of law and speech.", "Yasa ve sözün yeri."),
    ("Name-of-the-Father / Baba-Adı", "Signifier that installs a limit.", "Sınır koyan gösteren."),
    ("Objet petit a", "Object-cause of desire.", "Arzunun nesne-nedeni."),
    ("Desire / Arzu", "Want structured by the Other's want.", "Öteki'nin isteğiyle biçimlenen istek."),
    ("Drive / Dürtü", "Repeating push around a hole.", "Deliğin etrafındaki tekrarlı itki."),
    ("Jouissance", "Surplus enjoyment mixed with pain.", "Acıyla karışık fazla tatmin."),
    ("Manque / Lack", "Structural missingness.", "Yapısal eksiklik."),
    ("Foreclosure / Forklüzyon", "Signifier never inscribed.", "Hiç yazılmamış gösteren."),
    ("Disavowal / Yadsıma", "I know, but even so.", "Biliyorum, yine de."),
]
gloss_en = "<div class='table-wrap'><table><thead><tr><th>Term</th><th>On these pages</th></tr></thead><tbody>" + "".join(
    f"<tr><td><strong>{a}</strong></td><td>{b}</td></tr>" for a,b,_ in GLOSS_ROWS) + "</tbody></table></div>"
gloss_tr = "<div class='table-wrap'><table><thead><tr><th>Terim</th><th>Bu sayfalarda</th></tr></thead><tbody>" + "".join(
    f"<tr><td><strong>{a}</strong></td><td>{c}</td></tr>" for a,_,c in GLOSS_ROWS) + "</tbody></table></div>"

PAGES["glossary.html"] = {
"en": ("📚 Glossary", "Working dictionary.", "Terms", "Glossary", "As used on these maps.", gloss_en),
"tr": ("📚 Sözlük", "Çalışma sözlüğü.", "Terimler", "Sözlük", "Bu haritalarda kullanıldığı biçimiyle.", gloss_tr),
}

PAGES["about.html"] = {
"en": ("ℹ️ About", "Rationale and language split.", "Why two editions", "About and rationale",
"The repository began as WhatsApp exports. This site names them, explains them, and splits the reading: photographs in Turkish, SVG in English.",
"<ol>"
"<li>🇹🇷 <strong>Turkish edition</strong> keeps the original teaching charts — they are the primary text.</li>"
"<li>🇬🇧 <strong>English edition</strong> redraws the same logic as SVG so the concepts are readable without requiring the Turkish infographic.</li>"
"<li>🔍 Search and a top menu sit on both sides. 🌐 switches language on the same slug.</li>"
"<li>⚠️ Maps, not diagnoses. The charts already print that warning.</li>"
"</ol>"
"<p>Charts: <strong>Kaya Şahin — Lacancı Psikanaliz</strong>. Favicon: three-register knot.</p>"
+ svg("rsi", "SVG mark used across the English edition")
),
"tr": ("ℹ️ Hakkında", "Gerekçe ve dil ayrımı.", "Neden iki baskı", "Hakkında ve gerekçe",
"Depo WhatsApp dışa aktarımlarıyla başladı. Bu site onları adlandırır, açıklar ve okumayı ayırır: fotoğraflar Türkçe tarafta, SVG İngilizce tarafta.",
"<ol>"
"<li>🇹🇷 <strong>Türkçe baskı</strong> orijinal öğretim çizelgelerini tutar — asıl metin onlardır.</li>"
"<li>🇬🇧 <strong>İngilizce baskı</strong> aynı mantığı SVG olarak çizer; Türkçe infografiğe ihtiyaç duymadan kavram okunur.</li>"
"<li>🔍 Arama ve üst menü iki tarafta da vardır. 🌐 aynı sayfa adında dili değiştirir.</li>"
"<li>⚠️ Harita, tanı değil. Çizelgeler zaten bu uyarıyı basar.</li>"
"</ol>"
"<p>Çizelgeler: <strong>Kaya Şahin — Lacancı Psikanaliz</strong>. Favicon: üç düzen düğümü.</p>"
+ img("01-cycle-overview-all-structures.jpg", "Ana çizelge", "Türkçe baskının kaynak görseli.")
)
}

# write pages
for slug, langs in PAGES.items():
    for lang, tup in langs.items():
        title, desc, kicker, h1, lede, body = tup
        html = wrap(lang, title, desc, kicker, h1, lede, body)
        folder = TR if lang == "tr" else EN
        (folder / slug).write_text(html, encoding="utf-8")

# language gate
gate = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Lacan · 🇹🇷 Türkçe / 🇬🇧 English</title>
  <meta name="description" content="Choose Turkish charts or English SVG maps of Lacanian concepts.">
  <link rel="icon" href="favicon.ico" type="image/x-icon">
  <link rel="apple-touch-icon" href="apple-touch-icon.png">
  <link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
  <main class="gate">
    <div class="gate-inner">
      <div class="gate-brand">
        <div class="mark">🪢 LACAN</div>
        <h1>Concepts · Kavramlar</h1>
        <p class="lede" style="margin:0.4rem auto 0;text-align:center">Two editions of the same clinic. Pick a language.</p>
      </div>
      <div class="lang-choice">
        <a class="lang-card" href="tr/index.html">
          <span class="flag">🇹🇷</span>
          <h2>Türkçe</h2>
          <p>Orijinal öğretim çizelgeleri — fotoğraf olarak. Anlam, ispat, travma, semptom, formül, sinthome.</p>
        </a>
        <a class="lang-card" href="en/index.html">
          <span class="flag">🇬🇧</span>
          <h2>English</h2>
          <p>Same concepts drawn as SVG diagrams — no photo-charts. Search and menu still on top.</p>
        </a>
      </div>
      <p style="text-align:center;margin-top:1.4rem;color:var(--ink-soft);font-size:0.88rem">
        🔍 Search is on every inner page · ⚠️ maps, not diagnoses · Kaya Şahin
      </p>
    </div>
  </main>
</body>
</html>
'''
(ROOT / "index.html").write_text(gate, encoding="utf-8")

# redirects for old root pages
old = [
    "about.html","big-other.html","cycle.html","desire-and-drive.html","dopamine.html",
    "ethical-subject.html","formula.html","glossary.html","hysteric.html","jouissance.html",
    "object-attachment.html","objet-petit-a.html","obsessive.html","parental-attachment.html",
    "perverse.html","psychotic.html","sinthome.html","structures.html","three-registers.html",
    "uml-model.html",
]
for slug in old:
    (ROOT / slug).write_text(f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta http-equiv="refresh" content="0; url=en/{slug}">
  <link rel="canonical" href="en/{slug}">
  <link rel="icon" href="favicon.ico" type="image/x-icon">
  <title>Redirect · Lacan</title>
</head>
<body>
  <p>🌐 <a href="en/{slug}">English (SVG)</a> · <a href="tr/{slug}">Türkçe (çizelgeler)</a></p>
</body>
</html>
''', encoding="utf-8")

# favicon.ico — three register rings
def make_icon(size):
    img = Image.new("RGBA", (size, size), (247, 241, 230, 255))
    d = ImageDraw.Draw(img)
    m = max(2, size // 16)
    # three overlapping ellipses
    d.ellipse((m, size*0.18, size*0.62, size*0.82), outline=(47, 106, 69, 255), width=max(2, size//10))
    d.ellipse((size*0.18, size*0.32, size*0.82, size*0.96), outline=(44, 74, 124, 255), width=max(2, size//10))
    d.ellipse((size*0.38, size*0.18, size-m, size*0.82), outline=(122, 36, 54, 255), width=max(2, size//10))
    return img

ico16, ico32, ico48 = make_icon(16), make_icon(32), make_icon(48)
ico48.save(ROOT / "favicon.ico", format="ICO", sizes=[(16, 16), (32, 32), (48, 48)])
make_icon(180).save(ROOT / "apple-touch-icon.png", format="PNG")
print("wrote pages", len(list(TR.glob("*.html"))), len(list(EN.glob("*.html"))))
print("favicon", (ROOT / "favicon.ico").stat().st_size)
