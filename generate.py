import base64, os, json, urllib.request, textwrap, hashlib, html
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
def b64(p): return base64.b64encode(open(p,"rb").read()).decode()
I1=b64("assets/hunter.jpg"); I2=b64("assets/monarch.jpg")
USER=os.environ.get("GITHUB_REPOSITORY_OWNER") or "GIRRAJ2250"; NAME="GIRRAJ JANGID"; MAIL="ashujangid7688@gmail.com"; LI="linkedin.com/in/girraj-jangid-145132323"
SANS="Segoe UI,Arial,sans-serif"; MONO="Consolas,Courier New,monospace"
HEAD='<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="1000" height="%d" viewBox="0 0 1000 %d">'
DEFS='''<defs>
<linearGradient id="%(p)sbg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#0b0716"/><stop offset="1" stop-color="#05030c"/></linearGradient>
<linearGradient id="%(p)sbd" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#a78bfa"/><stop offset=".5" stop-color="#7c3aed" stop-opacity=".4"/><stop offset="1" stop-color="#22d3ee"/></linearGradient>
<linearGradient id="%(p)stx" x1="0" y1="0" x2="1" y2="0" spreadMethod="reflect"><stop offset="0" stop-color="#e9d5ff"/><stop offset=".5" stop-color="#a78bfa"/><stop offset="1" stop-color="#22d3ee"/><animateTransform attributeName="gradientTransform" type="translate" values="-0.6 0;0.6 0;-0.6 0" dur="7s" repeatCount="indefinite"/></linearGradient>
<linearGradient id="%(p)sfd" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#000"/><stop offset=".45" stop-color="#fff"/></linearGradient>
<linearGradient id="%(p)sfd2" x1="1" y1="0" x2="0" y2="0"><stop offset="0" stop-color="#000"/><stop offset=".55" stop-color="#fff"/></linearGradient>
<mask id="%(p)sm1"><rect width="1000" height="500" fill="url(#%(p)sfd)"/></mask>
<mask id="%(p)sm2"><rect width="1000" height="500" fill="url(#%(p)sfd2)"/></mask>
</defs>'''
def frame(p,h):
    return (DEFS%{'p':p})+f'<rect x="1" y="1" width="998" height="{h-2}" rx="22" fill="url(#{p}bg)"/>'+''.join(f'<circle cx="{(i*97)%980+10}" cy="{(i*53)%(h-20)+10}" r="1.3" fill="#a78bfa" opacity=".5"><animate attributeName="opacity" values=".1;.8;.1" dur="{3+i%4}s" repeatCount="indefinite"/></circle>' for i in range(30))
def end(p,h): return f'<rect x="1" y="1" width="998" height="{h-2}" rx="22" fill="none" stroke="url(#{p}bd)" stroke-width="1.5"/></svg>'
def t(x,y,s,txt,fill="#e5e7eb",w="400",f=SANS,extra=""):
    return f'<text x="{x}" y="{y}" font-family="{f}" font-size="{s}" font-weight="{w}" fill="{fill}" {extra}>{txt}</text>'

PINNED=[]   # optional: exact repo names to always show first, e.g. ["sales-dashboard","house-price"]. Empty = latest pushed repos
SHOW_RESUME_PROJECTS=True   # True: empty slots show resume projects. False: leave only real repos
RECORDS="97,000+"   # edit by hand: resume number
SKILLS=[("SQL","Joins • Aggregations • Cleaning • MySQL",.80),("POWER BI","Dashboards • KPIs • Slicers",.85),("EXCEL","Pivot • XLOOKUP • Power Query",.85),("PYTHON","Pandas • NumPy • Matplotlib • Seaborn",.72)]
CERTS="Deloitte Data Analytics Job Simulation (2025)   •   Data Visualization: Effective Insights (2025)   •   BCG X: Data for Decision Makers (2026)"
FALLBACK=[("QUEST 01 · CLEARED","Merchandise Sales Analytics","SQL • Power BI",["7,394+ transactions cleaned","5+ KPIs, slicers, customer","segmentation"]),
 ("QUEST 02 · CLEARED","House Price Analytics","Python • SQL • Power BI",["50,000+ housing records","price vs amenities trends,","dashboard with 5+ KPIs"]),
 ("QUEST 03 · CLEARED","Indian Job Market Analytics","Python • Pandas • Seaborn",["97,000+ job postings cleaned","EDA on roles, salary, cities","10+ visualizations"])]
def clean(x): return html.escape(''.join(c for c in (x or '') if ord(c)<0x2600 and c>=' '))
def fetch():
    if os.environ.get("MOCK_REPOS"): return json.load(open(os.environ["MOCK_REPOS"]))
    try:
        hd={"User-Agent":"profile-gen","Accept":"application/vnd.github+json"}
        if os.environ.get("GITHUB_TOKEN"): hd["Authorization"]="Bearer "+os.environ["GITHUB_TOKEN"]
        return json.load(urllib.request.urlopen(urllib.request.Request(f"https://api.github.com/users/{USER}/repos?per_page=100&sort=pushed",headers=hd),timeout=20))
    except Exception as e: print("fetch failed:",e); return []
repos=[r for r in fetch() if not r.get("fork") and not r.get("archived") and r["name"].lower()!=USER.lower()]
repos.sort(key=lambda r:r["pushed_at"],reverse=True)
cards=[]
print("repos found:",len(repos),[r["name"] for r in repos])
by={r["name"].lower():r for r in repos}
pick=[by[n.lower()] for n in PINNED if n.lower() in by]
pick+=[r for r in repos if r not in pick]
for r in pick[:3]:
    tech=" • ".join(([r["language"]] if r.get("language") else [])+[x.replace("-"," ") for x in r.get("topics",[])][:3]) or "Repository"
    desc=r.get("description") or "No description yet. Add one in the repo About section."
    nm=r["name"].replace("-"," ").replace("_"," ").title()
    cards.append((f"REPO · {r['pushed_at'][:10]} · ★ {r['stargazers_count']}",clean(nm if len(nm)<=27 else nm[:26]+'…'),clean(tech[:34]),[clean(l) for l in textwrap.wrap(desc,36)[:3]]))
live=len(cards)
cards+=FALLBACK[:3-len(cards)] if SHOW_RESUME_PROJECTS else []
stats=[(str(len(repos)),"PUBLIC REPOS"),(str(sum(r["stargazers_count"] for r in repos)),"TOTAL STARS"),(RECORDS,"RECORDS ANALYZED"),(repos[0]["pushed_at"][:10] if repos else "-","LAST PUSH")]

SK=" • "
# ---------- HERO ----------
h=440; s=HEAD%(h,h)+frame("h",h)
s+='<defs><clipPath id="hcl"><rect x="650" y="56" width="310" height="330" rx="14"/></clipPath></defs>'
s+='<rect x="50" y="34" width="560" height="30" rx="8" fill="#120b24" stroke="#a78bfa" stroke-opacity=".35"/><circle cx="68" cy="49" r="4" fill="#f87171"/><circle cx="84" cy="49" r="4" fill="#facc15"/><circle cx="100" cy="49" r="4" fill="#22c55e"/>'
s+=t(120,53,12,"girraj@github:~$ cat profile.md","#a78bfa","600",MONO)
s+=t(50,118,22,"Hi, I'm","#9ca3af","400",MONO)+t(50,186,64,NAME.title() if False else "Girraj Jangid","url(#htx)","800")
s+='<rect x="50" y="206" width="330" height="34" rx="17" fill="#7c3aed" fill-opacity=".2" stroke="#a78bfa"/>'+t(68,228,13,"DATA ANALYST  •  SQL  •  POWER BI","#e9d5ff","700",MONO)
s+=t(50,278,17,"Turning raw numbers into dashboards,","#d1d5db")+t(50,302,17,"and dashboards into decisions.","#d1d5db")
for i,(n,l) in enumerate([stats[0],stats[1],stats[2]]):
    x=50+i*170
    s+=f'<rect x="{x}" y="326" width="156" height="62" rx="12" fill="#7c3aed" fill-opacity=".08" stroke="#a78bfa" stroke-opacity=".5"/>'+t(x+14,354,22,n,"#e9d5ff","800")+t(x+14,376,10,l,"#9ca3af","600",MONO,'letter-spacing="1"')
s+='<circle cx="62" cy="412" r="5" fill="#22d3ee"><animate attributeName="opacity" values="1;.2;1" dur="2s" repeatCount="indefinite"/></circle>'+t(76,416,12,"OPEN TO WORK  ·  JAIPUR, INDIA","#22d3ee","700",MONO)
s+=f'<g clip-path="url(#hcl)"><image x="650" y="56" width="310" height="330" preserveAspectRatio="xMidYMin slice" xlink:href="data:image/jpeg;base64,{I1}"/></g>'
for bx,by,dx,dy in [(650,56,1,1),(960,56,-1,1),(650,386,1,-1),(960,386,-1,-1)]:
    s+=f'<path d="M{bx},{by+dy*26} L{bx},{by} L{bx+dx*26},{by}" fill="none" stroke="#22d3ee" stroke-width="3" stroke-linecap="round"/>'
s+='<circle cx="676" cy="82" r="5" fill="#f43f5e"><animate attributeName="opacity" values="1;0;1" dur="1.2s" repeatCount="indefinite"/></circle>'+t(688,86,11,"REC  hunter_01.mp4","#fff","700",MONO)
s+='<rect x="670" y="368" width="270" height="4" rx="2" fill="#fff" fill-opacity=".25"/><rect x="670" y="368" width="60" height="4" rx="2" fill="#22d3ee"><animate attributeName="width" values="10;270;10" dur="6s" repeatCount="indefinite"/></rect>'
open("hero.svg","w").write(s+end("h",h))

# ---------- ABOUT ----------
h=470; s=HEAD%(h,h)+frame("a",h)
s+='<defs><clipPath id="acl"><rect x="40" y="40" width="300" height="390" rx="16"/></clipPath></defs>'
s+=f'<g clip-path="url(#acl)"><image x="40" y="40" width="300" height="390" preserveAspectRatio="xMidYMin slice" xlink:href="data:image/jpeg;base64,{I2}"/></g><rect x="40" y="40" width="300" height="390" rx="16" fill="none" stroke="#a78bfa" stroke-opacity=".6"/>'
s+=t(380,66,12,"// BY NIGHT, A DATA ANALYST","#22d3ee","700",MONO,'letter-spacing="2"')+t(380,112,36,"Believe it — then ship it.","#f3e8ff","800")
s+=t(380,140,14,"Data Analyst in training. BCA (Data Science), Suresh Gyan Vihar University.","#9ca3af")
rows=[("Dashboards that explain themselves","Power BI with 5+ KPIs, slicers and clean visuals.","#22d3ee"),("SQL that stays clean","7,394+ transactions cleaned with joins and aggregations.","#a78bfa"),("Python for the heavy lifting","97,000+ job postings explored with Pandas, NumPy, Seaborn.","#f472b6")]
for i,(a_,b_,c) in enumerate(rows):
    y=170+i*70
    s+=f'<rect x="380" y="{y}" width="580" height="58" rx="12" fill="#7c3aed" fill-opacity=".07" stroke="{c}" stroke-opacity=".5"/><rect x="394" y="{y+13}" width="32" height="32" rx="9" fill="{c}" fill-opacity=".2" stroke="{c}"/>'+t(410,y+35,15,str(i+1),c,"800",MONO,'text-anchor="middle"')
    s+=t(442,y+25,16,a_,"#f3e8ff","700")+t(442,y+46,13,b_,"#9ca3af")
s+='<rect x="380" y="385" width="580" height="44" rx="10" fill="#0f0a1f" stroke="#22d3ee" stroke-opacity=".5"/>'+t(398,413,15,"\u201cI don\u2019t guess. I query.\u201d","#e5e7eb","600",MONO)+t(940,413,11,"GIRRAJ  ·  2026","#22d3ee","700",MONO,'text-anchor="end"')
open("about.svg","w").write(s+end("a",h))

# ---------- STACK (chip grid) ----------
h=380; s=HEAD%(h,h)+frame("k",h)
s+='<defs><clipPath id="kcl"><rect x="40" y="40" width="230" height="300" rx="16"/></clipPath></defs>'
s+=f'<g clip-path="url(#kcl)"><image x="40" y="40" width="230" height="300" preserveAspectRatio="xMidYMin slice" xlink:href="data:image/jpeg;base64,{I1}"/></g><rect x="40" y="40" width="230" height="300" rx="16" fill="none" stroke="#a78bfa" stroke-opacity=".6"/>'
s+=t(310,66,12,"// JUTSU ARSENAL","#22d3ee","700",MONO,'letter-spacing="2"')+t(310,108,34,"Tools I fight with","#f3e8ff","800")
chips=[("SQL","#22d3ee"),("MySQL","#38bdf8"),("Power BI","#facc15"),("Excel","#22c55e"),("Power Query","#4ade80"),("Python","#60a5fa"),("Pandas","#a78bfa"),("NumPy","#818cf8"),("Matplotlib","#f472b6"),("Seaborn","#2dd4bf"),("Jupyter","#fb923c"),("Colab","#fbbf24"),("Petpooja","#f87171"),("GitHub","#e5e7eb")]
x,y=310,134
for i,(n,c) in enumerate(chips):
    w=len(n)*9+38
    if x+w>960: x=310; y+=54
    s+=f'<rect x="{x}" y="{y}" width="{w}" height="38" rx="10" fill="{c}" fill-opacity=".08" stroke="{c}"><animate attributeName="stroke-opacity" values=".35;1;.35" dur="5s" begin="{i*.35:.2f}s" repeatCount="indefinite"/></rect><circle cx="{x+16}" cy="{y+19}" r="4" fill="{c}"/>'+t(x+28,y+24,14,n,"#f3e8ff","600")
    x+=w+12
for j,l in enumerate(textwrap.wrap("CERTIFIED:  "+CERTS.replace("   •   ","  /  "),78)[:2]): s+=t(310,312+j*20,12,clean(l),"#9ca3af","400",MONO)
open("stack.svg","w").write(s+end("k",h))

# ---------- MISSION DASHBOARD ----------
from collections import Counter
h=500; s=HEAD%(h,h)+frame("d",h)
s+='<defs><clipPath id="dcl"><rect x="112" y="108" width="156" height="170" rx="12"/></clipPath></defs>'
s+=t(340,34,12,"// MISSION DASHBOARD","#22d3ee","700",MONO,'letter-spacing="2"')
s+='<g><animateTransform attributeName="transform" type="rotate" values="-3 190 0;3 190 0;-3 190 0" dur="5s" repeatCount="indefinite"/>'
s+='<rect x="184" y="0" width="12" height="80" fill="#7c3aed"/><rect x="178" y="74" width="24" height="14" rx="4" fill="#9ca3af"/><rect x="90" y="88" width="200" height="350" rx="16" fill="#0f0a1f" stroke="#a78bfa" stroke-width="1.5"/>'
s+=t(112,102,9,"DATA ANALYST · ID CARD","#22d3ee","700",MONO)+f'<g clip-path="url(#dcl)"><image x="112" y="108" width="156" height="170" preserveAspectRatio="xMidYMin slice" xlink:href="data:image/jpeg;base64,{I1}"/></g>'
s+='<rect x="112" y="108" width="156" height="170" rx="12" fill="none" stroke="#a78bfa"><animate attributeName="stroke-opacity" values=".3;1;.3" dur="3s" repeatCount="indefinite"/></rect>'
s+=t(190,308,18,NAME.title(),"#f3e8ff","800",SANS,'text-anchor="middle"')+t(190,328,10,"SHADOW ANALYST · JAIPUR","#a78bfa","700",MONO,'text-anchor="middle" letter-spacing="1"')
s+=''.join(f'<rect x="{112+i*4}" y="356" width="{1+i%3}" height="42" fill="#e5e7eb" opacity=".75"/>' for i in range(39))+'</g>'
kp=[stats[0],stats[1],(str(sum(r.get("forks_count",0) for r in repos)),"FORKS"),stats[3]]
for i,(n,l) in enumerate(kp):
    x=340+i*160
    s+=f'<rect x="{x}" y="50" width="148" height="80" rx="12" fill="#7c3aed" fill-opacity=".08" stroke="#a78bfa" stroke-opacity=".5"/>'+t(x+16,92,24 if len(n)<9 else 18,n,"#e9d5ff","800")+t(x+16,114,10,l,"#9ca3af","600",MONO,'letter-spacing="1"')
s+='<rect x="340" y="150" width="340" height="320" rx="14" fill="#0f0a1f" stroke="#7c3aed" stroke-opacity=".6"/>'+t(358,178,11,"[ TOP MISSIONS ]","#22d3ee","700",MONO,'letter-spacing="2"')
ms=[(clean(r["name"] if len(r["name"])<=22 else r["name"][:21]+"…"),r.get("size",0)+1,f'{r.get("size",0)} KB') for r in pick[:5]]
if len(ms)<3 and SHOW_RESUME_PROJECTS: ms+=[("Merchandise Sales",7394,"7,394 rows"),("House Price",50000,"50,000 rows"),("Job Market",97000,"97,000 rows")][:5-len(ms)]
mx=max(m[1] for m in ms)
for i,(n,v_,lb) in enumerate(ms):
    y=200+i*50; W=max(8,int(300*v_/mx))
    s+=t(358,y+14,13,n,"#e5e7eb","600")+t(662,y+14,11,lb,"#a78bfa","600",MONO,'text-anchor="end"')+f'<rect x="358" y="{y+22}" width="300" height="8" rx="4" fill="#1f1535"/><rect x="358" y="{y+22}" width="{W}" height="8" rx="4" fill="#22d3ee"><animate attributeName="width" values="0;{W}" dur="1.4s" begin="0s" fill="freeze"/></rect>'
s+='<rect x="700" y="150" width="260" height="320" rx="14" fill="#0f0a1f" stroke="#7c3aed" stroke-opacity=".6"/>'+t(718,178,11,"[ NOW ]  LATEST PUSH","#22d3ee","700",MONO,'letter-spacing="2"')
if repos:
    r=repos[0]; s+=t(718,212,15,clean(r["name"] if len(r["name"])<=24 else r["name"][:23]+"…"),"#f3e8ff","700")+t(718,234,11,"pushed "+r["pushed_at"][:10],"#a78bfa","600",MONO)
    for j,l in enumerate(textwrap.wrap(r.get("description") or "No description yet.",28)[:6]): s+=t(718,268+j*24,13,clean(l),"#d1d5db")
else: s+=t(718,220,13,"Waiting for first repo","#9ca3af")
open("dashboard.svg","w").write(s+end("d",h))

# ---------- VILLAGE ----------
import math
h=260; s=HEAD%(h,h)+frame("v",h)
s+=t(50,60,12,"// CONTRIBUTION VILLAGE","#22d3ee","700",MONO,'letter-spacing="2"')+t(50,104,32,"My contribution village","#f3e8ff","800")+t(50,136,14,"Every commit raises another building, rebuilt automatically every day.","#9ca3af")
s+=t(50,190,13,"Built by GitHub Actions from my real contribution history.","#a78bfa","500",MONO)
langs=Counter((r.get("language") or "Other") for r in repos).most_common(5); tot=sum(c for _,c in langs); C=2*math.pi*55
s+='<g transform="translate(680,130) rotate(-90)"><circle r="55" fill="none" stroke="#1f1535" stroke-width="22"/>'
cum=0
for i,(lg,c) in enumerate(langs):
    col=["#22d3ee","#a78bfa","#f472b6","#facc15","#4ade80"][i]; s+=f'<circle r="55" fill="none" stroke="{col}" stroke-width="22" stroke-dasharray="{C*c/tot:.1f} {C:.1f}" stroke-dashoffset="{-C*cum/tot:.1f}"/>'; cum+=c
s+='</g>'+t(680,136,14,str(len(repos)),"#e9d5ff","800",SANS,'text-anchor="middle"')
for i,(lg,c) in enumerate(langs):
    col=["#22d3ee","#a78bfa","#f472b6","#facc15","#4ade80"][i]; s+=f'<rect x="780" y="{82+i*26}" width="12" height="12" rx="3" fill="{col}"/>'+t(800,93+i*26,13,clean(lg),"#e5e7eb","500")
if not langs: s+=t(780,120,13,"Push a repo to fill this","#9ca3af")
open("village.svg","w").write(s+end("v",h))

# ---------- CONNECT ----------
h=380; s=HEAD%(h,h)+frame("c",h)
s+=f'<g mask="url(#cm2)"><image x="0" y="0" width="380" height="{h}" preserveAspectRatio="xMidYMin slice" xlink:href="data:image/jpeg;base64,{I2}"/></g>'
s+='<rect x="0" width="380" height="380" fill="#7c3aed" opacity=".10"/>'
s+=t(400,70,13,"[ ARISE ]","#a78bfa","700",MONO,'letter-spacing="3"')+t(400,125,40,"Let's build something","url(#ctx)","800")+t(400,170,40,"legendary.","url(#ctx)","800")
for i,(k,v) in enumerate([("GITHUB","github.com/"+USER),("LINKEDIN",LI),("EMAIL",MAIL)]):
    y=200+i*55
    s+=f'<rect x="400" y="{y}" width="560" height="44" rx="12" fill="#7c3aed" fill-opacity=".08" stroke="#a78bfa" stroke-opacity=".45"/>'
    s+=f'<rect x="412" y="{y+8}" width="28" height="28" rx="8" fill="#7c3aed"/>'+t(426,y+28,14,k[0],"#fff","800",SANS,'text-anchor="middle"')
    s+=t(454,y+19,10,k,"#a78bfa","700",MONO,'letter-spacing="2"')+t(454,y+35,14,v,"#e5e7eb","500")
    s+=f'<text x="935" y="{y+29}" font-family="{SANS}" font-size="18" fill="#22d3ee">→<animateTransform attributeName="transform" type="translate" values="0 0;6 0;0 0" dur="1.6s" repeatCount="indefinite"/></text>'
open("connect.svg","w").write(s+end("c",h))

# ---------- README ----------
def v(f): return hashlib.sha1(open(f,"rb").read()).hexdigest()[:8]
open("README.md","w").write(f"""<div align="center">

<img src="hero.svg?v={v('hero.svg')}" alt="Hero" width="100%"/>

<img src="about.svg?v={v('about.svg')}" alt="About" width="100%"/>

<img src="stack.svg?v={v('stack.svg')}" alt="Tools" width="100%"/>

<img src="dashboard.svg?v={v('dashboard.svg')}" alt="Dashboard" width="100%"/>

<img src="village.svg?v={v('village.svg')}" alt="Village" width="100%"/>

<img src="./profile-3d-contrib/profile-night-view.svg" alt="Contribution city" width="100%"/>

<img src="connect.svg?v={v('connect.svg')}" alt="Connect" width="100%"/>

<a href="https://github.com/{USER}"><img src="https://img.shields.io/badge/GitHub-{USER}-7c3aed?style=for-the-badge&logo=github&logoColor=white"/></a>
<a href="https://{LI}"><img src="https://img.shields.io/badge/LinkedIn-Girraj%20Jangid-0a66c2?style=for-the-badge&logo=linkedin&logoColor=white"/></a>
<a href="mailto:{MAIL}"><img src="https://img.shields.io/badge/Email-Contact-ea4335?style=for-the-badge&logo=gmail&logoColor=white"/></a>

</div>
""")
