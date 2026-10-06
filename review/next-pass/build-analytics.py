"""Source-derived, unranked charts. SVG labels and a table also work without JS."""
from pathlib import Path
from html import escape as h
import json, statistics
root=Path(__file__).resolve().parents[2]
def roster_analytics(data):
 players=[p for p in data['players'] if 'camp' in p.get('cohort','camp').split()]
 assert len(players)==28 and sum(p['caps'] for p in players)==500
 colors={'GK':'#725534','DEF':'#276b61','MID':'#334f90','FWD':'#b3203c'}
 # Identical observations share one labelled circle. No fictitious jittered ages/caps.
 groups={}
 for p in players: groups.setdefault((p['age'],p['caps']),[]).append(p)
 marks=''
 for (age,caps),ps in groups.items():
  x=54+(age-16)/14*590;y=302-caps/70*250
  names='; '.join(p['name']+' ('+p['position']+')' for p in ps)
  marks+=f'<g class="scatter-group" data-members="{h(" ".join(p["id"] for p in ps))}"><circle cx="{x:.1f}" cy="{y:.1f}" r="{6 if len(ps)==1 else 11}" fill="{colors[ps[0]["position"]] if len(set(p["position"] for p in ps))==1 else "#55626c"}" stroke="#fffef8" stroke-width="2"><title>{h(names)} · age {age} · {caps} caps each</title></circle><text class="collision-count" x="{x:.1f}" y="{y+4:.1f}">{len(ps) if len(ps)>1 else ""}</text></g>'
 grid=''.join(f'<path d="M54 {302-n/70*250:.1f}H644" stroke="#bac5c3"/><text x="43" y="{307-n/70*250:.1f}" text-anchor="end">{n}</text>' for n in [0,10,30,50,70])
 ticks=''.join(f'<text x="{54+(n-16)/14*590:.1f}" y="330" text-anchor="middle">{n}</text>' for n in [16,18,20,22,24,26,28,30])
 opts=''.join(f'<option value="{p["id"]}">{h(p["name"])} · {p["age"]} years · {p["caps"]} caps</option>' for p in players)
 bars=''
 for label,test in [('0 caps',lambda n:n==0),('1–9',lambda n:0<n<10),('10–29',lambda n:10<=n<30),('30+',lambda n:n>=30)]:
  n=sum(test(p['caps']) for p in players)
  bars+=f'<div class="experience-row" data-bucket="{label}"><span>{label}</span><div><i style="width:{n/28*100:.2f}%"></i></div><b>{n}</b></div>'
 rows=''.join(f'<tr><th scope="row"><a href="#{p["id"]}">{h(p["name"])}</a></th><td>{p["position"]}</td><td>{p["age"]}</td><td>{p["caps"]}</td></tr>' for p in players)
 payload=json.dumps([{k:p[k] for k in ['id','name','age','caps','position']} for p in players]).replace('<','\\u003c')
 return f'''<noscript><style>.chart-tools,.chart-inspect,#chart-readout,#chart-profile{{display:none}}</style></noscript><section class="scout-section roster-analytics" id="experience"><p class="eyebrow">THE CURRENT 28 · DESCRIPTIVE ANALYSIS</p><h2>500 caps.<br>A median of three.</h2><p class="scout-intro">Experience is concentrated. Sixteen players have fewer than ten senior appearances; eight players hold 384 of the camp’s 500 caps. The five listed forwards have 15 caps combined. This describes international exposure, not player quality.</p><div class="chart-tools" role="group" aria-label="Chart position filter"><button data-chart-position="all" aria-pressed="true">All 28</button>{''.join(f'<button data-chart-position="{pos}" aria-pressed="false">{pos}</button>' for pos in colors)}</div><div class="analytics-grid"><figure class="experience-scatter"><figcaption><strong>Age × senior appearances</strong><span>Exact observations; a numbered dot contains coincident players.</span></figcaption><svg viewBox="0 0 680 352" role="img" aria-labelledby="scatter-title scatter-desc"><title id="scatter-title">Age and caps in the current U.S. camp</title><desc id="scatter-desc">Ages 17 to 29; caps zero to 61. The full data table and player selector follow this chart. Dots show exposure, not a rating.</desc><text x="54" y="24">SENIOR CAPS</text>{grid}{ticks}<text x="644" y="350" text-anchor="end">AGE · YEARS</text>{marks}</svg><label class="chart-inspect">Inspect the raw observation<select id="chart-player">{opts}</select></label><p id="chart-readout" role="status">Chris Brady · goalkeeper · age 22 · 2 senior caps.</p><a class="text-link" id="chart-profile" href="#chris-brady">Open this player’s profile →</a></figure><figure class="experience-bars"><figcaption><strong>How many players in each band?</strong><span>Players, not percentages. Scale: all 28 camp places.</span></figcaption><div class="experience-bar-data">{bars}</div><p id="chart-sample" class="fact-note">28 players · 500 career caps · median 3.</p><p class="fact-note">A young player’s low total is a small international sample, not evidence of low ability. Position groups follow the official camp list.</p></figure></div><p class="source-inline">Caps: <a href="{data['sources']['camp']['url']}">U.S. Soccer’s October 5 Canada preview ↗</a>. Ages checked October 6 in the official biographies linked below. Derived sums and median use only these 28 current players. No club minutes, per-90 rates or performance ratings are asserted.</p><details class="chart-data"><summary>All 28 observations &amp; chart limits</summary><p>Age runs horizontally and senior appearances vertically. Coincident points are grouped without shifting their coordinates. Choose a player above to highlight an exact observation; use a position filter to separate overlapping groups. Neither axis measures quality, selection probability or potential.</p><table><thead><tr><th>Player</th><th>Group</th><th>Age</th><th>Caps</th></tr></thead><tbody>{rows}</tbody></table></details><script type="application/json" id="roster-chart-data">{payload}</script></section>'''
if __name__=='__main__': print(roster_analytics(json.loads((root/'review/next-pass/squad-data.json').read_text())))
