# Wave 4 bonus — GPT-5.2 cover mockups (HTML + SVG → PDF)

This directory contains **working cover mockups** implemented as HTML/CSS with inline SVG (vector shapes), rendered to PDF using `wkhtmltopdf`.

## What’s here

- `cover-a-terminal.html`: **Typography-first** (“Terminal and the Cathedral” vibe)
- `cover-b-fracture-map.html`: **Minimalist fracture / map lines**
- `cover-c-mosaic-graph.html`: **Mosaic + graph overlay** (abstract, not a copyrighted image)
- `styles.css`: shared layout + print sizing
- `render.sh`: renders all HTML files to PDFs under `out/`

## Render PDFs

From repo root:

```bash
bash process/wave-4-faq-cover/mockups.gpt-5.2/render.sh
```

Outputs:
- `process/wave-4-faq-cover/mockups.gpt-5.2/out/cover-a-terminal.pdf`
- `process/wave-4-faq-cover/mockups.gpt-5.2/out/cover-b-fracture-map.pdf`
- `process/wave-4-faq-cover/mockups.gpt-5.2/out/cover-c-mosaic-graph.pdf`

## Notes / constraints

- **Trim + bleed**: these are set to a front-cover canvas of **6.25in × 9.25in** (6×9 plus 0.125in bleed on all sides).
- **Fonts**: uses system fonts only (no external downloads).
- **Purpose**: this is a “directional mock” to clarify composition, hierarchy, and vibe — not final production art.

