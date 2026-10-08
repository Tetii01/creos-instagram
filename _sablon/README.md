# Șablonul postărilor Creos

Reproduce stilul postărilor lui David (calibrat pixel cu pixel pe X Sweets și Extaz Padel, 9 oct. 2026).

- `build.py`: pagina 1080 × 1440 (HTML) randată în PNG cu Playwright. `project(...)` face postarea de tip proiect.
- `shader.py`: randează lumina roșie din `components/ui/LiquidShader.tsx` (repo-ul site-ului) în PNG.
- `assets/glow_project.png`: lumina folosită la postările de tip proiect (două cadre suprapuse, blur 26px, opacitate 0.62 în CSS).
- `assets/logo-shapes.json`: formele logo-ului, extrase din `components/brand/logo-shapes.ts`.
- Fonturile Geist (licență OFL, în `Geist-LICENSE.txt`).

Pornire: `pip install playwright && playwright install chromium`, apoi pui poza proiectului în `assets/` și apelezi `project(...)`.
