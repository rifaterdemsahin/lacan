const UI = {
  en: {
    home: "🏠 Home",
    search: "🔍 Search concepts…",
    searchEmpty: (q) => `😕 No pages match “${q}”.`,
    menu: "☰ Menu",
    brandSub: "🪢 Concepts",
    footerBlurb: "🌐 Bilingual site. 🇬🇧 English = 🖼️ SVG maps · 🇹🇷 Turkish = 📷 original charts. ⚠️ Clinical maps, not diagnoses. Press / to search.",
    start: "🚀 Start here",
    source: "📎 Source",
    sourceLine: "📷 Charts: Kaya Şahin, Lacancı Psikanaliz.",
    groups: { Concepts: "📖 Concepts", Structures: "🧩 Structures", Clinic: "🩺 Clinic", Maps: "🗺️ Maps" }
  },
  tr: {
    home: "🏠 Ana sayfa",
    search: "🔍 Kavram ara…",
    searchEmpty: (q) => `😕 “${q}” ile eşleşen sayfa yok.`,
    menu: "☰ Menü",
    brandSub: "🪢 Kavramlar",
    footerBlurb: "🌐 İki dilli site. 🇹🇷 Türkçe = orijinal çizelgeler · 🇬🇧 İngilizce = SVG. ⚠️ Klinik harita, tanı değil. Aramak için /.",
    start: "🚀 Buradan başla",
    source: "📎 Kaynak",
    sourceLine: "📷 Çizelgeler: Kaya Şahin, Lacancı Psikanaliz.",
    groups: { Concepts: "📖 Kavramlar", Structures: "🧩 Yapılar", Clinic: "🩺 Klinik", Maps: "🗺️ Haritalar" }
  }
};

const PAGE_META = {
  "index.html": {
    en: { title: "🏠 Home", excerpt: "Hub for the six-step cycle, clinical structures, and Lacanian maps.", keywords: "home hub cycle structures" },
    tr: { title: "🏠 Ana sayfa", excerpt: "Altı adımlı döngü, klinik yapılar ve Lacancı haritaların kapısı.", keywords: "ana sayfa dongu yapilar" }
  },
  "three-registers.html": {
    en: { title: "🟣 Three Registers", excerpt: "Imaginary, Symbolic, and Real: the three orders that knot a subject.", keywords: "rsi imaginary symbolic real borromean" },
    tr: { title: "🟣 Üç Düzen", excerpt: "İmgesel, Simgesel ve Gerçek: özneyi düğümleyen üç düzen.", keywords: "rsi imgesel simgesel gercek borromean" }
  },
  "cycle.html": {
    en: { title: "🔄 Six-Step Cycle", excerpt: "Meaning → Proof → Trauma → Symptom → Formula → Sinthome.", keywords: "cycle meaning proof trauma symptom formula sinthome" },
    tr: { title: "🔄 Altı Adımlı Döngü", excerpt: "Anlam → İspat → Travma → Semptom → Formül → Sinthome.", keywords: "dongu anlam ispat travma semptom formul sinthome" }
  },
  "desire-and-drive.html": {
    en: { title: "💫 Desire and Drive", excerpt: "Drive circles lack; desire aims at the Other's desire.", keywords: "desire drive trieb desir objet petit a" },
    tr: { title: "💫 Arzu ve Dürtü", excerpt: "Dürtü eksikliğin etrafında döner; arzu Öteki'nin arzusuna yönelir.", keywords: "arzu durtu desir trieb" }
  },
  "jouissance.html": {
    en: { title: "🔥 Jouissance", excerpt: "Enjoyment beyond the pleasure principle: surplus that both pulls and destroys.", keywords: "jouissance goce pleasure pain surplus" },
    tr: { title: "🔥 Jouissance", excerpt: "Haz ilkesinin ötesinde tatmin: hem çeken hem yıkan fazlalık.", keywords: "jouissance haz aci fazlalik" }
  },
  "objet-petit-a.html": {
    en: { title: "🎯 Objet petit a", excerpt: "The object-cause of desire and how each structure binds to a different object.", keywords: "objet petit a object cause desire" },
    tr: { title: "🎯 Objet petit a", excerpt: "Arzunun nesne-nedeni; her yapının bağlandığı farklı nesne.", keywords: "objet petit a nesne arzu" }
  },
  "big-other.html": {
    en: { title: "👁️ The Big Other", excerpt: "The locus of language, law, and the Other's desire.", keywords: "big other grand autre name of the father" },
    tr: { title: "👁️ Büyük Öteki", excerpt: "Dil, yasa ve Öteki'nin arzusunun yeri.", keywords: "buyuk oteki nom du pere yasa dil" }
  },
  "formula.html": {
    en: { title: "🧮 Formula", excerpt: "The personal algorithm that repeats a symptom as a way of living.", keywords: "formula life strategy repetition" },
    tr: { title: "🧮 Formül", excerpt: "Semptomu bir yaşam algoritmasına çeviren kişisel strateji.", keywords: "formul yasam stratejisi tekrar" }
  },
  "sinthome.html": {
    en: { title: "🪢 Sinthome", excerpt: "A singular knot that lets the subject live with lack instead of fleeing it.", keywords: "sinthome joyce fourth ring knot" },
    tr: { title: "🪢 Sinthome", excerpt: "Eksiklikle kaçmadan yaşamayı sağlayan tekil düğüm.", keywords: "sinthome joyce dorduncu halka" }
  },
  "structures.html": {
    en: { title: "🧩 Clinical Structures", excerpt: "Four clinical structures plus the ethical / sinthomatic subject.", keywords: "obsessive hysteric perverse psychotic ethical" },
    tr: { title: "🧩 Klinik Yapılar", excerpt: "Dört klinik yapı ve etik / sinthomatik özne.", keywords: "obsesif histerik sapkin psikotik etik" }
  },
  "obsessive.html": {
    en: { title: "🔒 Obsessive", excerpt: "Avoids the Real through rules, doubt, delay, and control.", keywords: "obsessive control delay guilt ritual" },
    tr: { title: "🔒 Obsesif", excerpt: "Gerçek'ten kural, kuşku, erteleme ve kontrol ile kaçar.", keywords: "obsesif kontrol erteleme suc ritüel" }
  },
  "hysteric.html": {
    en: { title: "❓ Hysteric", excerpt: "Keeps the Other's desire alive by questioning: what am I for you?", keywords: "hysteric question desire of the other" },
    tr: { title: "❓ Histerik", excerpt: "Soru sorarak Öteki'nin arzusunu canlı tutar: senin için neyim?", keywords: "histerik soru otekinin arzusu" }
  },
  "perverse.html": {
    en: { title: "🎭 Perverse", excerpt: "Organizes the Other's jouissance through staging, law, and fetish.", keywords: "perverse fetish staging jouissance" },
    tr: { title: "🎭 Sapkın", excerpt: "Sahne, yasa ve fetiş ile Öteki'nin jouissance'ını düzenler.", keywords: "sapkin fetis sahne jouissance" }
  },
  "psychotic.html": {
    en: { title: "⚡ Psychotic", excerpt: "When the Name-of-the-Father is foreclosed, the Real invades.", keywords: "psychotic foreclosure name of the father" },
    tr: { title: "⚡ Psikotik", excerpt: "Baba-Adı forklüze edildiğinde Gerçek istila eder.", keywords: "psikotik forklüzyon baba adi" }
  },
  "ethical-subject.html": {
    en: { title: "⭐ Ethical Subject", excerpt: "A subject loyal to their own desire, turning lack into a creative knot.", keywords: "ethical subject sinthomatic desire" },
    tr: { title: "⭐ Etik Özne", excerpt: "Kendi arzusuna sadık özne; eksikliği yaratıcı düğüme çevirir.", keywords: "etik ozne sinthomatik arzu" }
  },
  "object-attachment.html": {
    en: { title: "🧲 Object Attachment", excerpt: "Which object each structure clings to, and why.", keywords: "object attachment control gaze fetish" },
    tr: { title: "🧲 Nesne Bağlanması", excerpt: "Her yapının hangi nesneye neden sarıldığı.", keywords: "nesne baglanma bakis fetis kontrol" }
  },
  "parental-attachment.html": {
    en: { title: "👨‍👩‍👧 Parental Attachment", excerpt: "How parental figures become the first Big Other for each structure.", keywords: "parents over-attachment family" },
    tr: { title: "👨‍👩‍👧 Ebeveyn Bağlanması", excerpt: "Ebeveyn figürlerinin her yapı için ilk Büyük Öteki oluşu.", keywords: "ebeveyn asiri baglanma aile" }
  },
  "dopamine.html": {
    en: { title: "🧠 Lacan and Dopamine", excerpt: "Parallel, not identity: dopamine is not jouissance.", keywords: "dopamine neuroscience craving jouissance" },
    tr: { title: "🧠 Lacan ve Dopamin", excerpt: "Paralel, özdeş değil: dopamin jouissance değildir.", keywords: "dopamin norobilim jouissance" }
  },
  "uml-model.html": {
    en: { title: "📐 UML Model", excerpt: "An abstract map of structures realizing the same subjectivation interface.", keywords: "uml interface class trauma meaning proof" },
    tr: { title: "📐 UML Modeli", excerpt: "Aynı özneleşme arayüzünü gerçekleştiren yapıların soyut haritası.", keywords: "uml arayuz sinif travma anlam ispat" }
  },
  "glossary.html": {
    en: { title: "📚 Glossary", excerpt: "A working dictionary of the terms used across these maps.", keywords: "glossary dictionary terms" },
    tr: { title: "📚 Sözlük", excerpt: "Bu haritalardaki terimlerin çalışma sözlüğü.", keywords: "sozluk terimler tanimlar" }
  },
  "about.html": {
    en: { title: "ℹ️ About", excerpt: "Why this site exists, language split, and how to read the charts.", keywords: "about rationale source kaya sahin" },
    tr: { title: "ℹ️ Hakkında", excerpt: "Bu sitenin gerekçesi, dil ayrımı ve çizelgeleri okuma biçimi.", keywords: "hakkinda gerekce kaynak kaya sahin" }
  }
};

const GROUP_ITEMS = {
  Concepts: ["three-registers.html","cycle.html","desire-and-drive.html","jouissance.html","objet-petit-a.html","big-other.html","formula.html","sinthome.html"],
  Structures: ["structures.html","obsessive.html","hysteric.html","perverse.html","psychotic.html","ethical-subject.html"],
  Clinic: ["object-attachment.html","parental-attachment.html","dopamine.html"],
  Maps: ["uml-model.html","glossary.html","about.html"]
};

function langOf() {
  return document.documentElement.lang === "tr" ? "tr" : "en";
}
function baseOf() {
  return document.body.dataset.base || "../";
}
function currentFile() {
  const path = location.pathname.split("/").pop();
  return path && path.endsWith(".html") ? path : "index.html";
}
function pagesFor(lang) {
  return Object.entries(PAGE_META).map(([href, meta]) => ({
    href,
    group: Object.keys(GROUP_ITEMS).find((g) => GROUP_ITEMS[g].includes(href)) || "Start",
    ...meta[lang]
  }));
}

function headerHTML() {
  const lang = langOf();
  const ui = UI[lang];
  const current = currentFile();
  const other = lang === "tr" ? "en" : "tr";
  const base = baseOf();
  const groupMenus = Object.entries(GROUP_ITEMS).map(([g, items]) => {
    const links = items.map((href) => {
      const p = PAGE_META[href][lang];
      const cur = href === current ? ' aria-current="page"' : "";
      return `<a href="${href}"${cur}>${p.title}</a>`;
    }).join("");
    return `<details class="nav-drop"><summary>${ui.groups[g]}</summary><div class="nav-panel">${links}</div></details>`;
  }).join("");

  return `
    <header class="site-header">
      <div class="wrap header-inner">
        <a class="brand" href="index.html">
          <span class="brand-mark">LACAN</span>
          <span class="brand-sub">${ui.brandSub}</span>
        </a>
        <nav class="nav" id="site-nav">
          <a href="index.html"${current === "index.html" ? ' aria-current="page"' : ""}>${ui.home}</a>
          ${groupMenus}
        </nav>
        <div class="search-wrap">
          <label class="visually-hidden" for="site-search" style="position:absolute;left:-9999px">${ui.search}</label>
          <input id="site-search" type="search" placeholder="${ui.search}" autocomplete="off" />
          <div class="search-results" id="search-results" role="listbox"></div>
        </div>
        <nav class="lang-switch" aria-label="Language">
          <a href="${base}tr/${current}"${lang === "tr" ? ' aria-current="true"' : ""}>🇹🇷 TR</a>
          <a href="${base}en/${current}"${lang === "en" ? ' aria-current="true"' : ""}>🇬🇧 EN</a>
        </nav>
        <button class="menu-btn" id="menu-btn" type="button" aria-expanded="false">${ui.menu}</button>
      </div>
    </header>`;
}

function footerHTML() {
  const lang = langOf();
  const ui = UI[lang];
  const cycle = PAGE_META["cycle.html"][lang].title;
  const structures = PAGE_META["structures.html"][lang].title;
  const glossary = PAGE_META["glossary.html"][lang].title;
  const about = PAGE_META["about.html"][lang].title;
  return `
    <footer class="site-footer">
      <div class="wrap footer-grid">
        <div>
          <strong>Lacan ${ui.brandSub}</strong>
          <p>${ui.footerBlurb}</p>
        </div>
        <div>
          <strong>${ui.start}</strong><br>
          <a href="cycle.html">${cycle}</a><br>
          <a href="structures.html">${structures}</a><br>
          <a href="glossary.html">${glossary}</a>
        </div>
        <div>
          <strong>${ui.source}</strong><br>
          ${ui.sourceLine}<br>
          <a href="about.html">${about}</a>
          · <a href="${baseOf()}index.html">${lang === "tr" ? "🌐 Dil seç" : "🌐 Languages"}</a>
        </div>
      </div>
    </footer>`;
}

function normalize(s) {
  return s.toLowerCase()
    .normalize("NFD")
    .replace(/[\u0300-\u036f]/g, "")
    .replace(/ı/g, "i")
    .replace(/ş/g, "s")
    .replace(/ğ/g, "g")
    .replace(/ü/g, "u")
    .replace(/ö/g, "o")
    .replace(/ç/g, "c");
}

function searchPages(q) {
  const query = normalize(q.trim());
  if (!query) return [];
  const terms = query.split(/\s+/).filter(Boolean);
  const lang = langOf();
  return pagesFor(lang).map((p) => {
    const hay = normalize([p.title, p.group, p.keywords, p.excerpt].join(" "));
    const score = terms.reduce((acc, t) => acc + (hay.includes(t) ? 1 : 0), 0);
    return { p, score };
  }).filter((x) => x.score > 0)
    .sort((a, b) => b.score - a.score || a.p.title.localeCompare(b.p.title))
    .map((x) => x.p);
}

function renderResults(items, q) {
  const box = document.getElementById("search-results");
  const lang = langOf();
  if (!q.trim()) {
    box.classList.remove("open");
    box.innerHTML = "";
    return;
  }
  if (!items.length) {
    box.classList.add("open");
    box.innerHTML = `<div class="search-empty">${UI[lang].searchEmpty(q)}</div>`;
    return;
  }
  box.classList.add("open");
  box.innerHTML = items.map((p, i) =>
    `<a class="search-hit${i === 0 ? " active" : ""}" href="${p.href}" data-i="${i}">
      <strong>${p.title}</strong>
      <span>${p.excerpt}</span>
    </a>`
  ).join("");
}

function bindSearch() {
  const input = document.getElementById("site-search");
  const box = document.getElementById("search-results");
  input.addEventListener("input", () => renderResults(searchPages(input.value), input.value));
  input.addEventListener("keydown", (e) => {
    const active = box.querySelector(".search-hit.active");
    const list = [...box.querySelectorAll(".search-hit")];
    if (e.key === "Escape") {
      box.classList.remove("open");
      input.blur();
    } else if (e.key === "Enter" && active) {
      e.preventDefault();
      location.href = active.getAttribute("href");
    } else if (e.key === "ArrowDown" && list.length) {
      e.preventDefault();
      const i = Math.min(list.length - 1, list.indexOf(active) + 1);
      list.forEach((el) => el.classList.remove("active"));
      list[i].classList.add("active");
      list[i].scrollIntoView({ block: "nearest" });
    } else if (e.key === "ArrowUp" && list.length) {
      e.preventDefault();
      const i = Math.max(0, list.indexOf(active) - 1);
      list.forEach((el) => el.classList.remove("active"));
      list[i].classList.add("active");
    }
  });
  document.addEventListener("click", (e) => {
    if (!e.target.closest(".search-wrap")) box.classList.remove("open");
  });
  document.addEventListener("keydown", (e) => {
    if (e.key === "/" && document.activeElement !== input && !e.metaKey && !e.ctrlKey) {
      const tag = document.activeElement && document.activeElement.tagName;
      if (tag === "INPUT" || tag === "TEXTAREA") return;
      e.preventDefault();
      input.focus();
    }
  });
}

function bindNav() {
  const btn = document.getElementById("menu-btn");
  const nav = document.getElementById("site-nav");
  btn.addEventListener("click", () => {
    const open = nav.classList.toggle("open");
    btn.setAttribute("aria-expanded", String(open));
  });
  document.querySelectorAll(".nav-drop").forEach((d) => {
    d.addEventListener("toggle", () => {
      if (d.open) {
        document.querySelectorAll(".nav-drop").forEach((other) => {
          if (other !== d) other.removeAttribute("open");
        });
      }
    });
  });
}

document.body.insertAdjacentHTML("afterbegin", headerHTML());
document.body.insertAdjacentHTML("beforeend", footerHTML());
bindSearch();
bindNav();
