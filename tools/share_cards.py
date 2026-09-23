"""Render one 1200x630 share card per friend chapter, plus next/for/<slug>.html
whose Open Graph image is that card. Style: the SoFi videoboard, the June 25
board that read GORDON BELLAMY / PETE HINES. Real photos only, full color."""
import pathlib, html, subprocess
from playwright.sync_api import sync_playwright
ROOT = pathlib.Path(__file__).resolve().parent.parent
NEXT = ROOT / "next"; BASE = "https://gordonusc.github.io/usmnt-2026-personal/next/"
F = [
 ("quinn","Quinn","Sixteen years and counting.","Opening weekend · Soccer House · SoFi","quinn-soccerhouse-0611.jpg"),
 ("pete","Pete","You are the friend who put me inside it.","June 25 · SoFi · on the board","board-0625.jpg"),
 ("andy","Andy","You made my first one happen.","June 18 · the Delphi box","andy-fanfest-0718.jpg"),
 ("mike","Mike","Here's to whatever room 2030 puts us in.","1994 draw · 2026 Lumen Field",None),
 ("francksens","The Francksens","You gave the middle of my World Cup a home.","Stoughton · the Dragon House",None),
 ("matt","Matt","MATCHDAY, always.","Every matchday, on time",None),
 ("mason","Mason","Every big thing in my life routes through you first.","June 17 · the night before",None),
 ("foster","Foster","The Cup came to your city and you gave it a birthday party.","NYC · Final week","foster-birthday-0718.jpg"),
 ("brennan","BrenBren","The strongest possible definition of family.","Final Sunday · New York","final-table-0719.jpg"),
 ("joe","Joe","Love a dub. You are mine.","The home front",None),
]
FONTS = (ROOT / "next" / "fonts-selfhosted.css").read_text().replace("url(../fonts/", "url(" + (ROOT / "fonts").as_uri() + "/")
def card(name, line, where, photo):
    ph = f'<div class="ph" style="background-image:url({(ROOT/"assets"/photo).as_uri()})"></div>' if photo else ""
    return f"""<!doctype html><html><head><meta charset=utf-8><style>{FONTS}
*{{margin:0;box-sizing:border-box}} body{{position:relative;width:1200px;height:630px;background:radial-gradient(ellipse at 80% 0%,rgba(255,205,0,.10),transparent 60%),#0B0E1A;display:flex;font-family:'Fraunces',serif;color:#F5F1E8;overflow:hidden}}
.ph{{width:430px;height:630px;background-size:cover;background-position:center;flex:none;box-shadow:inset -60px 0 80px -40px #0B0E1A}}
.r{{flex:1;padding:40px 56px 86px;display:flex;flex-direction:column;justify-content:center;gap:26px}}
.board{{position:relative;background:#04060d;border:2px solid rgba(255,205,0,.25);border-radius:14px;padding:26px 30px;overflow:hidden}}
.nw{{position:relative;display:inline-block}} .nw:after{{content:"";position:absolute;inset:0;background:radial-gradient(circle,transparent 48%,#04060d 64%) 0 0/4px 4px}}
.k{{font:700 20px/1 'JetBrains Mono',monospace;letter-spacing:.2em;color:#ff3b4f;text-shadow:0 0 10px #ff3b4f}}
.n{{font:700 {'104' if len(name)<9 else '72'}px/1.05 'JetBrains Mono',monospace;color:#FFCD00;text-transform:uppercase;margin-top:14px;text-shadow:0 0 10px rgba(255,205,0,.8),0 0 30px rgba(255,205,0,.4)}}
.q{{font-size:{'40' if len(line)<40 else '32'}px;line-height:1.2;font-style:italic}}
.w{{font:600 18px/1.3 'JetBrains Mono',monospace;color:rgba(245,241,232,.6);letter-spacing:.08em;text-transform:uppercase}}
.rib{{position:absolute;left:0;right:0;bottom:0;height:46px;background:#04060d;border-top:2px solid rgba(255,59,79,.4);font:700 20px/46px 'JetBrains Mono',monospace;letter-spacing:.2em;color:#ff3b4f;text-shadow:0 0 8px #ff3b4f;white-space:nowrap;overflow:hidden;padding-left:24px}}
.sig{{font:600 18px/1 'JetBrains Mono',monospace;color:#FFCD00;letter-spacing:.14em}}
</style></head><body>{ph}<div class=r><div class=board><div class=k>SUPER SUPPORTER · USA 26</div><div class=nw><div class=n>{html.escape(name)}</div></div></div>
<div class=q>"{html.escape(line)}"</div><div class=w>{html.escape(where)}</div><div class=sig>YOUR CHAPTER · FROM G</div></div><div class=rib>USA 26 · FRIENDS &amp; FAMILY · THE SUMMER, KEPT · USA 26 · FRIENDS &amp; FAMILY · THE SUMMER, KEPT</div></body></html>"""
def page(slug, name, line, where=""):
    img = f"{BASE}og/{slug}.jpg"; title = f"{name}: your chapter · USA 26 with Gordon"
    return f"""<!doctype html>
<html lang="en"><head>
<meta name="robots" content="noindex, nofollow, noarchive, noimageindex" />
<meta charset="utf-8" /><meta name="viewport" content="width=device-width,initial-scale=1" />
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(line)}" />
<meta property="og:type" content="website" /><meta property="og:title" content="{html.escape(title)}" />
<meta property="og:description" content="{html.escape(line)}" /><meta property="og:image" content="{img}" />
<meta property="og:image:width" content="1200" /><meta property="og:image:height" content="630" />
<meta property="og:url" content="{BASE}for/{slug}.html" /><meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:image" content="{img}" />
<link rel="stylesheet" href="../fonts-selfhosted.css" />
<style>body{{margin:0;min-height:100dvh;background:#0B0E1A;color:#F5F1E8;font-family:'General Sans',system-ui,sans-serif;display:grid;place-items:center;padding:24px 16px}}
main{{max-width:760px;width:100%;text-align:center}} img{{width:100%;height:auto;border-radius:14px;box-shadow:0 20px 60px rgba(0,0,0,.6)}}
a.go{{display:inline-block;margin-top:24px;background:#FFCD00;color:#0B0E1A;font-weight:800;padding:14px 26px;border-radius:999px;text-decoration:none;font-size:1.05rem}}
p{{opacity:.75;margin-top:12px;font-size:.95rem;line-height:1.5}}</style></head>
<body><main><img src="../og/{slug}.jpg" alt="{html.escape(name)}, in lights: {html.escape(line)}" width="1200" height="630" />
<h1 style="font-family:'Fraunces',serif;font-weight:400;font-style:italic;font-size:clamp(1.3rem,4vw,1.9rem);margin-top:26px;line-height:1.3">{html.escape(name)}: "{html.escape(line)}"</h1>
<p>{html.escape(where)}. This is one line from your chapter on The Friends, the page I wrote about the people who made my World Cup summer.</p>
<a class="go" href="../friends.html#{slug}">Read your chapter</a>
<p>USA 26 with Gordon · The Friends</p></main></body></html>
"""
(NEXT/"og").mkdir(exist_ok=True); (NEXT/"for").mkdir(exist_ok=True)
with sync_playwright() as pw:
    b = pw.chromium.launch(); pg = b.new_page(viewport={"width":1200,"height":630})
    for slug,name,line,where,photo in F:
        tmp = ROOT/"tools"/"cards"/f"_{slug}.html"; tmp.write_text(card(name,line,where,photo))
        pg.goto(tmp.as_uri()); pg.evaluate("document.fonts.ready")
        pg.wait_for_timeout(300)
        png = NEXT/"og"/f"{slug}.png"; pg.screenshot(path=str(png))
        subprocess.run(["sips","-s","format","jpeg","-s","formatOptions","82",str(png),"--out",str(NEXT/"og"/f"{slug}.jpg")],capture_output=True); png.unlink(); tmp.unlink()
        (NEXT/"for"/f"{slug}.html").write_text(page(slug,name,line,where)); print(slug)
    b.close()
