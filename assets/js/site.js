const PAGES = [
  { href: "index.html", title: "Home", group: "Start",
    keywords: "hub overview lacan archive charts kaya sahin cycle structures",
    excerpt: "Hub for the six-step cycle, clinical structures, and Lacanian maps." },
  { href: "three-registers.html", title: "Three Registers", group: "Concepts",
    keywords: "rsi imaginary symbolic real borromean rings imgesel simgesel gercek",
    excerpt: "Imaginary, Symbolic, and Real: the three orders that knot a subject." },
  { href: "cycle.html", title: "Six-Step Cycle", group: "Concepts",
    keywords: "anlam ispat travma semptom formul sinthome meaning proof trauma symptom formula",
    excerpt: "Meaning → Proof → Trauma → Symptom → Formula → Sinthome." },
  { href: "desire-and-drive.html", title: "Desire and Drive", group: "Concepts",
    keywords: "desir trieb drive objet petit a lack manque arzu durtu",
    excerpt: "Drive circles lack; desire aims at the Other's desire." },
  { href: "jouissance.html", title: "Jouissance", group: "Concepts",
    keywords: "jouissance goce pleasure pain surplus enjoyment haz aci",
    excerpt: "Enjoyment beyond the pleasure principle: surplus that both pulls and destroys." },
  { href: "objet-petit-a.html", title: "Objet petit a", group: "Concepts",
    keywords: "objet petit a object cause of desire leftover object attachment key heart fetish",
    excerpt: "The object-cause of desire and how each structure binds to a different object." },
  { href: "big-other.html", title: "The Big Other", group: "Concepts",
    keywords: "big other grand autre name of the father nom du pere law language oteki",
    excerpt: "The locus of language, law, and the Other's desire." },
  { href: "formula.html", title: "Formula", group: "Concepts",
    keywords: "formula formul life strategy repetition f(x) ritual",
    excerpt: "The personal algorithm that repeats a symptom as a way of living." },
  { href: "sinthome.html", title: "Sinthome", group: "Concepts",
    keywords: "sinthome joyce knot creative knotting fourth ring",
    excerpt: "A singular knot that lets the subject live with lack instead of fleeing it." },
  { href: "structures.html", title: "Clinical Structures", group: "Structures",
    keywords: "obsessive hysteric perverse psychotic ethical subject nevroz psikoz sapkin",
    excerpt: "Four clinical structures plus the ethical / sinthomatic subject." },
  { href: "obsessive.html", title: "Obsessive", group: "Structures",
    keywords: "obsessive obsessional neurosis control delay guilt ritual obsesif",
    excerpt: "Avoids the Real through rules, doubt, delay, and control." },
  { href: "hysteric.html", title: "Hysteric", group: "Structures",
    keywords: "hysteric hysteria question desire of the other histerik",
    excerpt: "Keeps the Other's desire alive by questioning: what am I for you?" },
  { href: "perverse.html", title: "Perverse", group: "Structures",
    keywords: "perverse perversion fetish staging jouissance of the other sapkin",
    excerpt: "Organizes the Other's jouissance through staging, law, and fetish." },
  { href: "psychotic.html", title: "Psychotic", group: "Structures",
    keywords: "psychotic foreclosure name of the father hallucination psikotik",
    excerpt: "When the Name-of-the-Father is foreclosed, the Real invades." },
  { href: "ethical-subject.html", title: "Ethical Subject", group: "Structures",
    keywords: "ethical subject sinthomatic etik ozne desire responsibility",
    excerpt: "A subject loyal to their own desire, turning lack into a creative knot." },
  { href: "object-attachment.html", title: "Object Attachment", group: "Clinic",
    keywords: "object attachment control gaze fetish stabilization sinthome object",
    excerpt: "Which object each structure clings to, and why." },
  { href: "parental-attachment.html", title: "Parental Attachment", group: "Clinic",
    keywords: "parents over-attachment family ebeveyn baglanma",
    excerpt: "How parental figures become the first Big Other for each structure." },
  { href: "dopamine.html", title: "Lacan and Dopamine", group: "Clinic",
    keywords: "dopamine neuroscience craving reward wanting vs jouissance",
    excerpt: "Parallel, not identity: dopamine is not jouissance." },
  { href: "uml-model.html", title: "UML Model", group: "Maps",
    keywords: "uml class interface realization trauma meaning proof symptom",
    excerpt: "An abstract software-style map of structures realizing the same interface." },
  { href: "glossary.html", title: "Glossary", group: "Maps",
    keywords: "glossary dictionary terms definitions lacanian vocabulary",
    excerpt: "A working dictionary of the terms used across these charts." },
  { href: "about.html", title: "About & Rationale", group: "Maps",
    keywords: "about rationale source kaya sahin credits method",
    excerpt: "Why this site exists, how files were renamed, and how to read the charts." }
];

const GROUPS = [
  { name: "Concepts", items: ["three-registers.html","cycle.html","desire-and-drive.html","jouissance.html","objet-petit-a.html","big-other.html","formula.html","sinthome.html"] },
  { name: "Structures", items: ["structures.html","obsessive.html","hysteric.html","perverse.html","psychotic.html","ethical-subject.html"] },
  { name: "Clinic", items: ["object-attachment.html","parental-attachment.html","dopamine.html"] },
  { name: "Maps", items: ["uml-model.html","glossary.html","about.html"] }
];

function pageByHref(href) {
  return PAGES.find((p) => p.href === href);
}

function currentFile() {
  const path = location.pathname.split("/").pop();
  return path && path.endsWith(".html") ? path : "index.html";
}

function headerHTML() {
  const current = currentFile();
  const groupMenus = GROUPS.map((g) => {
    const links = g.items.map((href) => {
      const p = pageByHref(href);
      const cur = href === current ? ' aria-current="page"' : "";
      return `<a href="${href}"${cur}>${p.title}</a>`;
    }).join("");
    return `<details class="nav-drop"><summary>${g.name}</summary><div class="nav-panel">${links}</div></details>`;
  }).join("");

  return `
    <header class="site-header">
      <div class="wrap header-inner">
        <a class="brand" href="index.html">
          <span class="brand-mark">LACAN</span>
          <span class="brand-sub">Concepts</span>
        </a>
        <nav class="nav" id="site-nav">
          <a href="index.html"${current === "index.html" ? ' aria-current="page"' : ""}>Home</a>
          ${groupMenus}
        </nav>
        <div class="search-wrap">
          <label class="visually-hidden" for="site-search" style="position:absolute;left:-9999px">Search</label>
          <input id="site-search" type="search" placeholder="Search concepts…" autocomplete="off" />
          <div class="search-results" id="search-results" role="listbox"></div>
        </div>
        <button class="menu-btn" id="menu-btn" type="button" aria-expanded="false">Menu</button>
      </div>
    </header>`;
}

function footerHTML() {
  return `
    <footer class="site-footer">
      <div class="wrap footer-grid">
        <div>
          <strong>Lacan Concepts</strong>
          <p>A reading site built from the original Turkish / English teaching charts. Clinical maps, not diagnoses. Press <span class="kbd">/</span> to search.</p>
        </div>
        <div>
          <strong>Start here</strong><br>
          <a href="cycle.html">Six-step cycle</a><br>
          <a href="structures.html">Clinical structures</a><br>
          <a href="glossary.html">Glossary</a>
        </div>
        <div>
          <strong>Source</strong><br>
          Charts attributed to Kaya Şahin, Lacancı Psikanaliz.<br>
          <a href="about.html">About & rationale</a>
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
  return PAGES.map((p) => {
    const hay = normalize([p.title, p.group, p.keywords, p.excerpt].join(" "));
    const score = terms.reduce((acc, t) => acc + (hay.includes(t) ? 1 : 0), 0);
    return { p, score };
  }).filter((x) => x.score > 0)
    .sort((a, b) => b.score - a.score || a.p.title.localeCompare(b.p.title))
    .map((x) => x.p);
}

function renderResults(items, q) {
  const box = document.getElementById("search-results");
  if (!q.trim()) {
    box.classList.remove("open");
    box.innerHTML = "";
    return;
  }
  if (!items.length) {
    box.classList.add("open");
    box.innerHTML = `<div class="search-empty">No pages match “${q}”.</div>`;
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
  let hits = [];

  input.addEventListener("input", () => {
    hits = searchPages(input.value);
    renderResults(hits, input.value);
  });
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
