"""Insert the Season 3 ("Since July") band into every next/ page.
Idempotent: each band carries data-s3="<page>" and is skipped if present.
Facts come from after.html's receipts list (U.S. Soccer, ESPN, NBC, AP, Sky)."""
import pathlib, re
N = pathlib.Path(__file__).resolve().parent.parent / "next"

PERU = '''<div class="fixtures" style="max-width:420px"><div class="fixture" data-kick="2026-09-26T20:30:00Z"><div class="fixture__day">Sat · Sep 26 · Orlando</div><div class="fixture__opp">USA v Peru</div><div class="fixture__meta">Inter&amp;Co Stadium · 4:30 p.m. ET</div><div class="fixture__pt">1:30 p.m. Pacific</div><div class="fixture__cd"></div></div></div>'''

def band(page, tag, title, body):
    return f'''
<section class="s3" data-s3="{page}">
  <div class="container">
    <div class="s3__tag">{tag}</div>
    <h2 class="display display--l section__title">{title}</h2>
{body}
  </div>
</section>
'''

B = {}
B["index"] = ("after-hero", band("index", "Season 3 · the story kept going", 'The whistle in Seattle <span class="italic">was not the end.</span>', f'''
    <div class="led led-ticker" role="marquee" aria-label="Scoreboard ticker"><div class="led-ticker__track led__text led__text--m">POCHETTINO THROUGH 2030 &nbsp;·&nbsp; 28 CALLED FOR THE FALL &nbsp;·&nbsp; 13 NEVER CAPPED &nbsp;·&nbsp; SULLIVAN, 16 &nbsp;·&nbsp; PERU SEP 26 &nbsp;·&nbsp; CHILE SEP 29 &nbsp;·&nbsp; MEXICO OCT 3 &nbsp;·&nbsp; CANADA OCT 6</div></div>
    <p class="section__lede" style="margin-top:22px">The coach signed on through 2030. Reyna went to France, Berhalter to Middlesbrough, and a sixteen-year-old got his first senior call. The first match of the next cycle is Saturday, and it's on home soil again.</p>
    {PERU}
    <a class="btn-s3" href="after.html">Everything since July</a> <a class="btn-s3 btn-s3--ghost" href="arcade/belamini.html">Play the run</a>'''))

B["soccer-journey"] = ("before-door", band("soccer-journey", "Chapter after the last chapter · September 2026", 'The journey <span class="italic">has a next stop.</span>', '''
    <p class="section__lede">I ended this page in July thinking I was writing a finale. I was writing a halftime. On August 3 the coach who got us our first knockout win since 2002 signed on through 2030. On September 17 he called thirteen players who have never worn the senior shirt, one of them sixteen years old. I was twenty-three at the 1994 Draw. I will be fifty-nine in 2030. The kid Cavan Sullivan will be twenty. We are going to meet in the middle.</p>
    <div class="s3__grid">
      <div class="s3__card"><span class="when">1994 · Las Vegas</span><h3>The Draw</h3><p>Two friends from Harvard in the room where American soccer got its first real stage.</p></div>
      <div class="s3__card"><span class="when">2026 · SoFi</span><h3>The Board</h3><p>GORDON BELLAMY above PETE HINES. Fifty years in, finally inside a home World Cup.</p></div>
      <div class="s3__card"><span class="when">2030 · Spain, Portugal, Morocco</span><h3>The Next Room</h3><p>Four years, one coach, a squad averaging twenty-two. The planning starts with a text to Mike.</p></div>
    </div>
    <a class="btn-s3" href="after.html">Read Since July</a>'''))

B["run"] = ("before-door", band("run", "Match six has a date", 'The run ended July 6. <span class="italic">The next one starts Saturday.</span>', f'''
    <p class="section__lede">Twelve of the players on this page are in the fall camp: the Trusty who headed us in front at 3' against Türkiye, the Tillman who bent in both knockout free kicks, the Freeman who rose for the header in Seattle, the Reyna who flicked in the 90'+8 goal against Paraguay. Balogun and Pulisic are not called this time. Ricardo Pepi was called, then withdrawn injured on September 20.</p>
    {PERU}
    <a class="btn-s3" href="arcade/belamini.html">Play the run, 16-bit</a> <a class="btn-s3 btn-s3--ghost" href="after.html">What happened since</a>'''))

B["friends"] = ("before-main-end", band("friends", "Send it to them", 'Every friend gets <span class="italic">their name on the board.</span>', '''
    <p class="section__lede">On June 25 a videoboard put my name above Pete's. Now everyone on this page gets the same treatment: a card with their name in lights and one line from their chapter, and a link that opens right on it. Text it, and the card shows up in the preview.</p>
    <div class="s3__grid" id="sharecards">
@@SHARE@@
    </div>'''))

B["roster"] = ("before-main-end", band("roster", "Where they are now · September 2026", 'The 26, <span class="italic">seventy-eight days later.</span>', '''
    <p class="section__lede">Gold means called into the fall camp for Peru, Chile, Mexico and Canada. Clubs are listed only where a move is receipted.</p>
    <div class="squad">
@@ROSTER@@
    </div>
    <p class="s3__src">U.S. Soccer roster release, Sep 17, and update, Sep 20. Transfers: ESPN summer grades, Sep 2; AP on Reyna, Aug 4.</p>
    <a class="btn-s3" href="after.html#squad">See the full fall squad</a>'''))

B["strategy"] = ("before-main-end", band("strategy", "The 2030 brief", 'Same coach. <span class="italic">A younger team.</span>', '''
    <div class="s3__grid">
      <div class="s3__card"><span class="when">The mandate</span><h3>Bigger than the first team</h3><p>The new deal has Pochettino advising the youth national teams, the U-17 and U-20 World Cups, and the 2028 Olympic push, on top of the senior side.</p></div>
      <div class="s3__card"><span class="when">The numbers</span><h3>22 years, 9 months</h3><p>Average age of the fall squad. Twenty-eight called, thirteen of them never capped, average seventeen caps a man.</p></div>
      <div class="s3__card"><span class="when">Open question</span><h3>Who is the nine?</h3><p>Balogun is not called and Pepi is out injured. The forwards in camp: Damion Downs, Julian Hall, Justin Ellis, Cole Campbell and Cavan Sullivan.</p></div>
      <div class="s3__card"><span class="when">Open question</span><h3>Who is in goal?</h3><p>Matt Freese, 19 caps, is the only keeper with real minutes. Chris Brady has one. Diego Kochen and Brian Schwake have none.</p></div>
    </div>
    <p class="s3__src">U.S. Soccer, Aug 3 and Sep 17 and 20, 2026.</p>'''))

B["group-d"] = ("before-main-end", band("group-d", "Group D, graded one more time", 'Every American who scored in Group D, <span class="italic">and where he is now.</span>', '''
    <div class="s3__grid">
      <div class="s3__card"><span class="when">Paraguay · 31' and 45'+</span><h3>Folarin Balogun</h3><p>Still at Monaco after a deadline-day move to Everton fell apart. Not called this fall.</p></div>
      <div class="s3__card"><span class="when">Paraguay · 90'+8</span><h3>Gio Reyna</h3><p>Now at Strasbourg on a five-year deal. In the fall camp, 43 caps.</p></div>
      <div class="s3__card"><span class="when">Australia · 43'</span><h3>Alex Freeman</h3><p>In the fall camp, 22 caps, listed with Villarreal.</p></div>
      <div class="s3__card"><span class="when">Türkiye · 3'</span><h3>Auston Trusty</h3><p>The corner header. In the fall camp from Celtic.</p></div>
      <div class="s3__card"><span class="when">Türkiye · 49'</span><h3>Sebastian Berhalter</h3><p>Moved from Vancouver to Middlesbrough this summer. In the fall camp.</p></div>
    </div>
    <p class="s3__src">Plus two own goals, which I also count, emotionally. Sources on the <a href="after.html#sources">Since July</a> page.</p>'''))

B["r32"] = ("before-main-end", band("r32", "Postscript · the ten men, since", 'Balogun and Tillman, <span class="italic">two months on.</span>', '''
    <div class="s3__grid">
      <div class="s3__card"><span class="when">45' goal · 61' red</span><h3>Balogun</h3><p>The ban got suspended, and the summer kept the chaos going. On Premier League deadline day a move from Monaco to Everton was agreed and he went for the medical. Then he walked away after the deadline. Still a Monaco player. Not in the fall squad.</p></div>
      <div class="s3__card"><span class="when">82' free kick</span><h3>Tillman</h3><p>The man who shut the door is back in camp from Bayer Leverkusen, 35 caps and five goals, two of them the free kicks this site will never stop talking about.</p></div>
    </div>
    <a class="btn-s3" href="arcade/belamini.html">Play the ten-men level</a>'''))

B["r16"] = ("before-door", band("r16", "What the coach said, and what he did next", '"It wasn\'t our day." <span class="italic">Then he signed for four more years.</span>', '''
    <p class="section__lede">"I think we were not good enough, it wasn't our day," Pochettino said after Seattle, with his contract running out. Four weeks later, on August 3, he signed through 2030. Pulisic, who limped off at 52', was back in club action by September and was left out of the fall squad.</p>
    <div class="led led--red" style="margin-top:8px"><div class="led__text led__text--xl">61 SECONDS</div><div class="led__sub">Level with Belgium, 31' to 32'. Playable now, and just as unfair, in the arcade.</div></div>
    <a class="btn-s3" href="arcade/belamini.html">Play the 61 seconds</a>'''))

B["lore"] = ("before-main-end", band("lore", "New lore · summer and fall 2026", 'Three new entries <span class="italic">for the book.</span>', '''
    <div class="s3__grid">
      <div class="s3__card"><span class="when">August 2026</span><h3>Middlesbrough, America's club</h3><p>Berhalter from Vancouver, Arfsten from Columbus. In the English second tier, the Stars and Stripes found a home.</p></div>
      <div class="s3__card"><span class="when">Deadline day 2026</span><h3>The U-turn</h3><p>Balogun: the medical, the deal sheet, then the walk. The first man since Zidane to score and see red in the same knockout game also invented a new kind of transfer.</p></div>
      <div class="s3__card"><span class="when">September 17, 2026</span><h3>Sixteen</h3><p>Cavan Sullivan of the Philadelphia Union, called up to the senior team at sixteen, beside a seventeen-year-old from Greenville already playing for Dortmund.</p></div>
    </div>'''))

B["kits"] = ("before-main-end", band("kits", "The shirt, handed on", 'Thirteen players in camp <span class="italic">have never worn it.</span>', '''
    <p class="section__lede">This fall the senior shirt goes on thirteen players who have never worn it in a match, if they get the minutes. Twelve World Cup players are there to show them how it's done.</p>
    <div class="led led--white"><div class="led__text led__text--m">FIRST CALL-UPS: KOCHEN · SCHWAKE · MILLER · PIERRE · WESTFIELD · ALBERT · GOZO · MEHMETI · RAINES · C. CAMPBELL · ELLIS · HALL · SULLIVAN</div></div>
    <p class="s3__src">U.S. Soccer, Sep 17, 2026. Caps as listed at call-up.</p>'''))

B["meta"] = ("before-main-end", band("meta", "Season 3 · how this edition was made", 'September 22, <span class="italic">one night, one pass over everything.</span>', '''
    <div class="s3__grid">
      <div class="s3__card"><span class="when">Facts first</span><h3>Two sources a line</h3><p>Every item on Since July is backed by U.S. Soccer plus ESPN, NBC, AP, NPR, SI or Sky. Anything I could not confirm twice stayed off the page.</p></div>
      <div class="s3__card"><span class="when">The style</span><h3>The videoboard</h3><p>The new layer on every page speaks in the dot-matrix voice of the SoFi board from June 25. The old pages keep their own voices.</p></div>
      <div class="s3__card"><span class="when">The arcade</span><h3>Belamini, the full run</h3><p>The free-kick demo became four levels from the real tournament: Trusty's header, the ten men, Tillman's free kick, and the 61 seconds.</p></div>
      <div class="s3__card"><span class="when">The friends</span><h3>Name on the board</h3><p>A shareable card for every friend's chapter, built so the link preview is the gift.</p></div>
    </div>'''))

B["experience"] = ("before-footer", '''
<section class="s3" data-s3="experience" style="--rule:rgba(255,255,255,.14);--ink:#F7F8FB;--ink-dim:rgba(247,248,251,.72);--gold:#E8B23A;--bg:#0A1733;background:#0A1733;color:#F7F8FB">
  <div class="wrap" style="max-width:1100px;margin:0 auto;padding:0 20px">
    <div class="s3__tag">Next rooms · fall 2026</div>
    <h2 style="color:#F7F8FB;font-family:'Anton',Impact,sans-serif;font-size:clamp(2rem,6vw,3.2rem);line-height:1.05">Four more matchdays to be somewhere together.</h2>
    <p style="max-width:62ch;opacity:.8;margin-top:10px;line-height:1.6">All four on TNT, truTV or HBO Max, with Peacock too, and Telemundo or Universo in Spanish. Times in Pacific.</p>
    <div class="fixtures">
      <div class="fixture" data-kick="2026-09-26T20:30:00Z"><div class="fixture__day">Sat · Sep 26</div><div class="fixture__opp">Peru</div><div class="fixture__meta">Orlando</div><div class="fixture__pt">1:30 p.m. PT</div><div class="fixture__cd"></div></div>
      <div class="fixture" data-kick="2026-09-30T00:00:00Z"><div class="fixture__day">Tue · Sep 29</div><div class="fixture__opp">Chile</div><div class="fixture__meta">St. Louis</div><div class="fixture__pt">5:00 p.m. PT</div><div class="fixture__cd"></div></div>
      <div class="fixture" data-kick="2026-10-04T02:00:00Z"><div class="fixture__day">Sat · Oct 3</div><div class="fixture__opp">Mexico</div><div class="fixture__meta">Glendale, AZ</div><div class="fixture__pt">7:00 p.m. PT</div><div class="fixture__cd"></div></div>
      <div class="fixture" data-kick="2026-10-07T00:00:00Z"><div class="fixture__day">Tue · Oct 6</div><div class="fixture__opp">Canada</div><div class="fixture__meta">St. Paul</div><div class="fixture__pt">5:00 p.m. PT</div><div class="fixture__cd"></div></div>
    </div>
    <a class="btn-s3" href="fall-2026.ics" download>Add all four to your calendar</a> <a class="btn-s3 btn-s3--ghost" href="after.html" style="color:#F7F8FB">Since July</a>
  </div>
</section>
''')

def roster_markup():
    wc26 = ["Matt Freese","Matt Turner","Chris Brady","Chris Richards","Tim Ream","Antonee Robinson","Sergiño Dest","Joe Scally","Miles Robinson","Mark McKenzie","Auston Trusty","Alex Freeman","Max Arfsten","Tyler Adams","Weston McKennie","Sebastian Berhalter","Cristian Roldan","Malik Tillman","Alejandro Zendejas","Brenden Aaronson","Christian Pulisic","Folarin Balogun","Tim Weah","Gio Reyna","Ricardo Pepi","Haji Wright"]
    called = {"Matt Freese":"New York City FC","Chris Brady":"Chicago Fire","Chris Richards":"Crystal Palace","Antonee Robinson":"Fulham","Sergiño Dest":"PSV","Miles Robinson":"FC Cincinnati","Auston Trusty":"Celtic","Alex Freeman":"Villarreal","Tyler Adams":"Bournemouth","Sebastian Berhalter":"Middlesbrough, moved from Vancouver this summer","Malik Tillman":"Bayer Leverkusen","Gio Reyna":"Strasbourg, moved from Gladbach Aug 4"}
    notes = {"Ricardo Pepi":"Called, then withdrawn injured Sep 20","Max Arfsten":"Moved from Columbus to Middlesbrough this summer. Not called","Folarin Balogun":"Everton move collapsed on deadline day. Not called","Christian Pulisic":"Back in club action. Not called","Weston McKennie":"Not called this window"}
    assert len(wc26) == 26 and len(called) == 12
    out = []
    for n in wc26:
        if n in called: out.append(f'      <div class="squad__p wc"><b>{n}</b><span>In the fall camp · {called[n]}</span></div>')
        else: out.append(f'      <div class="squad__p"><b>{n}</b><span>{notes.get(n, "Not called this window")}</span></div>')
    return "\n".join(out)

FRIENDS = [("quinn","Quinn","Sixteen years and counting."),("pete","Pete","You are the friend who put me inside it."),("andy","Andy","You made my first one happen."),("mike","Mike","Here's to whatever room 2030 puts us in."),("francksens","The Francksens","You gave the middle of my World Cup a home."),("matt","Matt","MATCHDAY, always."),("mason","Mason","Every big thing in my life routes through you first."),("foster","Foster","The Cup came to your city and you gave it a birthday party."),("brennan","BrenBren","The strongest possible definition of family."),("joe","Joe","Love a dub. You are mine.")]
def share_markup():
    return "\n".join(f'      <a class="s3__card" href="for/{s}.html" style="text-decoration:none;display:block"><img src="og/{s}.jpg" alt="{n}\'s name on the board: {q}" loading="lazy" style="width:100%;border-radius:8px;display:block" /><span class="when" style="display:block;margin-top:10px">{n} · open the card</span></a>' for s,n,q in FRIENDS)

for page, (where, html) in B.items():
    p = N / f"{page}.html"; t = p.read_text()
    if f'data-s3="{page}"' in t: print("skip", page); continue
    html = html.replace("@@ROSTER@@", roster_markup()).replace("@@SHARE@@", share_markup())
    if where == "after-hero":
        i = t.index("</section>") + len("</section>"); t = t[:i] + html + t[i:]
    elif where == "before-door":
        i = t.index('<a class="door"'); j = t.rfind("<section", 0, i); t = t[:j] + html + t[j:]
    elif where == "before-main-end":
        i = t.index("</main>"); t = t[:i] + html + t[i:]
    elif where == "before-footer":
        i = t.index("<footer"); t = t[:i] + html + t[i:]
    if "season3.css" not in t:
        t = t.replace("</head>", '<link rel="stylesheet" href="season3.css">\n</head>', 1)
    if "season3.js" not in t:
        t = t.replace("</body>", '<script src="season3.js" defer></script>\n</body>', 1)
    p.write_text(t); print("band", page)
