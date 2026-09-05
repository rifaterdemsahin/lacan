# Lacan Concepts

A static site that turns a folder of Lacanian teaching charts into a readable, searchable map.

**Live site:** [https://rifaterdemsahin.github.io/lacan/](https://rifaterdemsahin.github.io/lacan/)

GitHub Pages is served from `main` `/`. Locally, open `index.html` or run the server below.

## Rationale

The repo started as WhatsApp image exports with timestamps for names. The images already contained a full curriculum:

- a six-step cycle (meaning → proof → trauma → symptom → formula → sinthome)
- four clinical structures plus an ethical / sinthomatic row
- object attachment (objet petit a), parental over-attachment
- jouissance vs drive vs desire
- a careful *non-identity* with dopamine
- UML drafts of the same process

This site exists so those charts can be **named, explained, compared, and searched**, without pretending they are diagnostic labels.

## What changed

- Images moved to `images/` and renamed to semantic filenames (`01-cycle-overview-…`, `21-jouissance-drive-desire.jpg`, …).
- One exact duplicate WhatsApp export was removed.
- HTML pages explain each concept with the original visuals plus simple CSS diagrams.
- Shared top menu (Concepts, Structures, Clinic, Maps) and a header search (`/` to focus).

## Source

Charts attributed to **Kaya Şahin, Lacancı Psikanaliz**. Teaching maps, not a substitute for clinical training.

## Local

Open `index.html` in a browser, or:

```bash
python3 -m http.server 8000
```
