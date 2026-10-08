import json, sys
from pathlib import Path
from playwright.sync_api import sync_playwright
ROOT=Path(__file__).resolve().parent
L=json.loads((ROOT/'assets/logo-shapes.json').read_text())
def logo_svg(h):
    vb=L['logoViewBox']; w=h*vb['width']/vb['height']
    paths=''.join(f'<path d="{d}" fill="#ffffff"/>' for d in L['logoWordmarkShapes'])+''.join(f'<path d="{d}" fill="#ff3b4e"/>' for d in L['logoSymbolShapes'])
    return f'<svg width="{w:.1f}" height="{h}" viewBox="0 0 {vb["width"]} {vb["height"]}">{paths}</svg>'
CSS="""
@font-face{font-family:Geist;src:url(assets/Geist-Regular.woff2);font-weight:400}
@font-face{font-family:Geist;src:url(assets/Geist-Medium.woff2);font-weight:500}
@font-face{font-family:Geist;src:url(assets/Geist-SemiBold.woff2);font-weight:600}
@font-face{font-family:Geist;src:url(assets/Geist-Bold.woff2);font-weight:700}
*{box-sizing:border-box;margin:0;padding:0}
body{width:1080px;height:1440px;font-family:Geist,sans-serif;color:#fff;-webkit-font-smoothing:antialiased;position:relative;overflow:hidden;
 background:radial-gradient(ellipse 110% 38% at 50% 71%, rgb(28,14,18) 0%, rgba(11,11,13,0) 100%), #0b0b0d}
.glow{position:absolute;left:0;top:0;width:1080px;height:1440px;filter:blur(26px);opacity:.62}
.logo{position:absolute;top:86px;left:88px}
.card{position:absolute;left:88px;right:88px;top:183px;height:747px;border-radius:36px;border:1.5px solid transparent;overflow:hidden;
 box-shadow:0 30px 70px rgba(0,0,0,.55);
 background:linear-gradient(120deg,#191919 0%,#0b0b0b 90%) padding-box,linear-gradient(140deg,rgba(255,255,255,.3) 0%,rgba(31,31,31,.8) 22%,rgba(255,255,255,.08) 50%,rgba(255,255,255,.22) 78%,rgba(31,31,31,0) 100%) border-box}
.card img{display:block;width:100%;height:100%;object-fit:cover;border-radius:34px}
.text{position:absolute;left:88px;right:88px;top:992px}
.label{font-size:28px;font-weight:500;color:#ff3b4e;line-height:1.2;letter-spacing:-0.005em}
.title{font-size:88px;font-weight:700;letter-spacing:-0.05em;line-height:1.04;padding-bottom:.06em;margin-top:18px;
 background-image:linear-gradient(180deg,#fff 0%,rgba(255,255,255,.62) 100%);-webkit-background-clip:text;background-clip:text;color:transparent}
.desc{font-size:32px;line-height:1.47;color:#b4b3b7;margin-top:20px;max-width:840px;letter-spacing:-0.005em}
"""
def page(body): return f'<!doctype html><html lang="ro"><head><meta charset="utf-8"><style>{CSS}</style></head><body>{body}</body></html>'
def render(html, out):
    p=ROOT/'_tmp.html'; p.write_text(html,encoding='utf-8')
    with sync_playwright() as pw:
        b=pw.chromium.launch(); pg=b.new_page(viewport={'width':1080,'height':1440},device_scale_factor=1)
        pg.goto(p.as_uri()); pg.evaluate('document.fonts.ready'); pg.wait_for_timeout(300)
        pg.screenshot(path=str(out),full_page=False); b.close()
def project(glow, img, label, title, desc, out, objpos='center'):
    body=f"""<img class="glow" src="{glow}">
<div class="logo">{logo_svg(40)}</div>
<div class="card"><img src="{img}" style="object-position:{objpos}"></div>
<div class="text"><div class="label">{label}</div><div class="title">{title}</div><div class="desc">{desc}</div></div>"""
    render(page(body), out)
if __name__=='__main__':
    # calibrare pe X Sweets, ca să compar cu postarea lui David
    out=ROOT/'out'; out.mkdir(exist_ok=True)
    project('assets/glowhero_t11.png','assets/x-sweets.webp','Website + chatboți AI','X Sweets<br>and Coffee',
            'Site nou pentru restaurant, cu chatboți AI integrați care răspund clienților pe loc.', out/'calib_xsweets.png')
