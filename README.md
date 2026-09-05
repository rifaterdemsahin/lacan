# 🪢 Lacan Concepts · Kavramlar

🌐 Two editions of the same clinic:

- 🇹🇷 **Türkçe (çizelgeler):** [https://rifaterdemsahin.github.io/lacan/tr/](https://rifaterdemsahin.github.io/lacan/tr/)
- 🇬🇧 **English (SVG):** [https://rifaterdemsahin.github.io/lacan/en/](https://rifaterdemsahin.github.io/lacan/en/)

**Language gate:** [https://rifaterdemsahin.github.io/lacan/](https://rifaterdemsahin.github.io/lacan/)

Turkish pages keep the original teaching photographs. English pages redraw the same ideas as SVG diagrams (no photo-charts). Both have a top menu, emoji labels, and search (`/`).

GitHub Pages is served from `main` `/`.

## Rationale

The repo started as WhatsApp image exports with timestamps for names. The images already contained a full curriculum:

- a six-step cycle (meaning → proof → trauma → symptom → formula → sinthome)
- four clinical structures plus an ethical / sinthomatic row
- object attachment (objet petit a), parental over-attachment
- jouissance vs drive vs desire
- a careful *non-identity* with dopamine
- UML drafts of the same process

This site exists so those charts can be **named, explained, compared, and searched**, without pretending they are diagnostic labels. English readers get SVG maps so they do not have to parse dense Turkish infographics; Turkish readers keep the source charts.

## What changed

- Images moved to `images/` and renamed to semantic filenames (`01-cycle-overview-…`, `21-jouissance-drive-desire.jpg`, …).
- One exact duplicate WhatsApp export was removed.
- `tr/` = original visuals. `en/` = SVG concept diagrams in `assets/svg/`.
- Shared top menu (Concepts / Kavramlar, Structures / Yapılar, Clinic / Klinik, Maps / Haritalar) and header search.
- `favicon.ico` (three-register knot).

## Source

Charts attributed to **Kaya Şahin, Lacancı Psikanaliz**. Teaching maps, not a substitute for clinical training.

## Local

```bash
python3 -m http.server 8000
```

Then open http://127.0.0.1:8000/
