# Șablonul postărilor Creos

Reproduce stilul postărilor lui David (calibrat pixel cu pixel pe X Sweets și Extaz Padel, 9 oct. 2026).

- `build.py`: pagina 1080 × 1440 (HTML) randată în PNG cu Playwright. `project(...)` face postarea de tip proiect.
- `shader.py`: randează lumina roșie din `components/ui/LiquidShader.tsx` (repo-ul site-ului) în PNG.
- `assets/glow_project.png`: lumina folosită la postările de tip proiect (două cadre suprapuse, blur 26px, opacitate 0.62 în CSS).
- `assets/logo-shapes.json`: formele logo-ului, extrase din `components/brand/logo-shapes.ts`.
- Fonturile Geist (licență OFL, în `Geist-LICENSE.txt`).

Pornire: `pip install playwright && playwright install chromium`, apoi pui poza proiectului în `assets/` și apelezi `project(...)`.

## Fundalul (important)

`assets/bg_project.png` e fundalul real din exportul original al postării Extaz Padel a lui David (lumina de sus, marginile, umbra de sub card, pata vișinie de jos), fără logo și fără text. Diferența față de originalul lui, în afara cardului și a textului: maxim 2 din 255. La postările de tip proiect se folosește el (`bg=`), nu lumina randată din shader, ca toate să arate la fel.

Capturile de ecran de pe iPhone sunt în spațiul de culoare Display P3. Înainte să compari culori cu o postare de-a lui David, convertește captura în sRGB (PIL `ImageCms.profileToProfile`), altfel roșul pare mai stins decât e.

## Valori măsurate pe exportul original (postare de tip proiect)

Logo: top 88, stânga 88, înălțime 40. Card: 88-992 × 183-930, colțuri 36. Text de la top 995: eticheta 28px Medium #ff3b4e; titlul 88px Bold, letter-spacing -0.025em, metalic, margin-top 16; descrierea 33px Regular, line-height 47px, #909099, letter-spacing 0.004em, max-width 845, margin-top 22. Verificat pe Extaz Padel: lățimile titlului și ale rândurilor de descriere ies la ±2 px.
