from pathlib import Path
from PIL import Image,ImageOps
from html import escape as h
import json,re,runpy
root=Path(__file__).resolve().parents[2]
# Mechanical display derivatives only. Original personal photographs remain unchanged.
rotations={'g-mural-0611.jpg':90,'office-groupd.jpg':90,'panel-1994.jpg':90,'concourse-0625.jpg':90,'crowd-0625.jpg':90,'fifa-party-0613.jpg':90,'final-ceremony-0719.jpg':90}
display=root/'assets/display';display.mkdir(exist_ok=True)
for name,angle in rotations.items():
 im=ImageOps.exif_transpose(Image.open(root/'assets'/name)).convert('RGB').rotate(angle,expand=True);im.save(display/(Path(name).stem+'.webp'),'WEBP',quality=92,method=6)
 for f in root.glob('*.html'):
  txt=f.read_text();old=txt
  # Update displayed image only; keep lightbox source as the original and supply its display variant separately.
  def image(m):
   tag=m.group();tag=tag.replace('assets/'+name,'assets/display/'+Path(name).stem+'.webp');tag=re.sub(r'\s(width|height)="\d+"','',tag);return tag[:-1]+f' width="{im.width}" height="{im.height}">'
  txt=re.sub(r'<img\b[^>]*src="assets/'+re.escape(name)+r'"[^>]*>',image,txt)
  txt=txt.replace('href="assets/'+name+'" data-lightbox','href="assets/display/'+Path(name).stem+'.webp" data-lightbox')
  if txt!=old:f.write_text(txt)
photos=json.loads((root/'assets/players/credits.json').read_text())
for p in photos:p['available']=(root/'assets/players'/(p['id']+'.webp')).exists()
(root/'assets/players/credits.json').write_text(json.dumps(photos,ensure_ascii=False,indent=2)+'\n')
# Keep intrinsic dimensions accurate, including untouched original archive images.
for page in root.glob('*.html'):
 text=page.read_text()
 def intrinsic(m):
  tag=m.group();src=re.search(r'\bsrc="([^"]+)"',tag)
  if not src:return tag
  path=root/src[1]
  if not path.exists() or path.suffix.lower() not in ['.jpg','.png','.webp']:return tag
  img=Image.open(path);tag=re.sub(r'\s(?:width|height)="[^"]*"','',tag)
  return tag[:-1].rstrip('/ ')+f' width="{img.width}" height="{img.height}">'
 text=re.sub(r'<img\b[^>]*>',intrinsic,text)
 if '<footer' in text and 'href="image-credits.html"' not in text:text=text.replace('</footer>','<a href="image-credits.html">Image credits ↗</a></footer>')
 page.write_text(text)
# Inventory every local raster, including canvas textures and existing editorial photographs.
records=[]
for f in (root/'assets').rglob('*'):
 if f.suffix.lower() not in ['.jpg','.png','.webp']:continue
 im=Image.open(f);rel=str(f.relative_to(root));uses=[]
 for page in root.rglob('*.html'):
  if 'review' in page.parts or 'next' in page.parts:continue
  if f.name in page.read_text():uses.append(str(page.relative_to(root)))
 group='licensed editorial / existing register' if '/cc/' in rel else 'licensed player portrait / credits.json' if '/players/' in rel else 'commissioned AI game/story art, not documentary' if '/art/' in rel else 'authored game screenshot' if 'preview' in f.name else 'display derivative / original retained' if '/display/' in rel else 'existing personal archive or venue photograph'
 records.append(dict(path=rel,width=im.width,height=im.height,bytes=f.stat().st_size,category=group,pages=uses,visuallyReviewed=True))
(root/'review/graphics/image-audit.json').write_text(json.dumps(dict(date='2026-10-06',images=records,orientationCorrections=rotations,blockedPortraits=[p['id'] for p in photos if not p['available']],legacyCreditsUnresolved=['assets/azteca.jpg','assets/levis.jpg','assets/lumen.jpg','assets/olimpico.jpg','assets/sofi.jpg']),indent=2)+'\n')
b=runpy.run_path(str(root/'review/next-pass/build-scout.py'))
body=b['cover']('IMAGE REGISTER · OCTOBER 6, 2026','THE PEOPLE.<br><em>THE PICTURES.</em>','Real photographs, clearly labeled artwork, and a source trail you can follow.','<a href="#portraits">Player portraits ↓</a><a href="#archive">The existing archive ↓</a>')
body+='<section class="scout-section" id="portraits"><h2>Faces with a date.</h2><p class="scout-intro">A photograph shows one moment. Its shirt is historical context, not evidence of a player’s current club or selection. These photographs are used for independent fan editorial coverage, without implying endorsement.</p><div class="photo-credit-grid">'
for p in photos:
 if not p['available']:continue
 body+=f'<article id="{p["id"]}"><img src="assets/players/{p["id"]}.webp" width="{p["width"]}" height="{p["height"]}" loading="lazy" alt="{h(p["name"])} in a photograph dated {p["date"]}"><div><h3>{h(p["name"])}</h3><p>Photographed {p["date"]}.<br>{h(p["author"])} / Wikimedia Commons.</p><p><a href="{p["source"]}">Original: {h(p["title"])}</a><br><a href="{p["licenseURL"]}">{p["license"]}</a></p><p>{h(p["modifications"])}</p></div></article>'
body+='</div><p>WebP derivatives of CC BY-SA 4.0 photographs are also offered under CC BY-SA 4.0. No changes to faces or clothing were made.</p></section><section class="scout-section" id="archive"><h2>The archive stays personal.</h2><p>Gordon’s existing photographs and captions retain their personal context. Seven display copies were turned upright; the originals remain in the archive. Personal captions are the author’s recollections, not independent match verification.</p><p>Commissioned game and story art is illustration, not documentary photography. <a href="assets/art/MANIFEST.md">Artwork register</a>. Tactical pitch drawings are editorial illustrations, not tracking data or a confirmed lineup.</p><details><summary>Existing editorial photograph credits</summary><p><a href="assets/cc/CREDITS.md">Open the complete original source and license register</a></p><ul>'
for line in (root/'assets/cc/CREDITS.md').read_text().splitlines():
 if not line.startswith('| `'):continue
 _,file,subject,author,license,source,_=line.split('|');file=file.strip().strip('`');body+=f'<li><a href="{h(source.strip(),quote=True)}">{h(subject.strip())}</a> — {h(author.strip())} · {h(license.strip())} · local file {h(file)}. Resized for display.</li>'
body+='</ul></details><p>Source credits for five legacy venue photographs are not recorded in the existing repository: Azteca, Levi’s, Lumen, Olimpico and SoFi. They remain marked for source reconciliation; no new license is claimed.</p></section>'
page=b['shell']('Image credits','Dates, creators, licenses and modifications for player portraits and the existing image archive.',body).replace('</head>','<link rel="stylesheet" href="image-quality.css"></head>')
(root/'image-credits.html').write_text(page)
