import json,re,html,csv,math,datetime,sys,os,unicodedata
sys.path.insert(0,os.path.dirname(__file__))
from towns import TOWNS
from geo import geocode
import manual
import os; _H=os.path.dirname(os.path.abspath(__file__)); RAW=os.path.join(_H,"..","raw"); OUT=os.path.join(_H,"..","data")
_T=datetime.date.today()
TODAY=os.environ.get("EVENTS_TODAY",_T.isoformat()); END=(datetime.date.fromisoformat(TODAY)+datetime.timedelta(days=730)).isoformat(); CHECKED=TODAY
TZ=datetime.timezone(datetime.timedelta(hours=2))
EV=[]
def hav(a,b):
    R=6371;la1,lo1,la2,lo2=map(math.radians,[a[0],a[1],b[0],b[1]])
    h=math.sin((la2-la1)/2)**2+math.cos(la1)*math.cos(la2)*math.sin((lo2-lo1)/2)**2
    return 2*R*math.asin(math.sqrt(h))
CENT={t:geocode(q)[:2] for t,(q,r,g) in TOWNS.items()}
# Towns used only for hand-checked entries (Running Guy PE / Winelands races). Keep them out of
# automatic Quicket/Webtickets geocoding so the coast stays Cape Town–Jeffreys Bay.
MANUAL_ONLY_TOWNS={"Gqeberha","Stellenbosch","Swellendam","Ladismith"}
AUTO_CENT={t:ll for t,ll in CENT.items() if t not in MANUAL_ONLY_TOWNS}
EXCL={"Stellenbosch":(-33.934,18.86,12),"Paarl":(-33.73,18.96,14),"Franschhoek":(-33.91,19.12,10),"Grabouw":(-34.15,19.02,10),"Caledon":(-34.23,19.43,10),"Wolseley":(-33.52,19.2,15),"Malmesbury":(-33.46,18.73,15),"Darling":(-33.38,18.38,10),"Ladismith/Karoo62":(-33.49,21.27,25),"Robertson":(-33.8,19.88,25),"Gqeberha":(-33.96,25.62,40)}
def town_from_geo(lat,lng):
    for n,(a,b,r) in EXCL.items():
        if hav((lat,lng),(a,b))<r: return None
    best=min(AUTO_CENT,key=lambda t:hav((lat,lng),AUTO_CENT[t]))
    d=hav((lat,lng),AUTO_CENT[best])
    lim=45 if best in("Cape Town","Somerset West") else 30
    return best if d<lim else None
MUSICAL=re.compile(r"\bmusical\b|pantomime|\bpanto\b",re.I)
MUSICAL_STRICT=re.compile(r"(?<!spectacular )\bmusical\b(?! (theatre academy|direction|director|experience|journey|celebration|evening|tribute|programme|feast|delight|accompaniment))|pantomime|\bpanto\b",re.I)
OPERA=re.compile(r"rom[ée]o et juliette|don giovanni|la boh[eè]me|\bcarmen\b|\btosca\b|traviata|madama butterfly|magic flute",re.I)
BADVEN=re.compile(r"defected studio|the address club|cashmere premium lounge|colorbox studios",re.I)
FEST=re.compile(r"festival|\bfest\b|fees\b|oktoberfest|octoberfest",re.I)
EXCL_KW=re.compile(r"open mic|karaoke|workshop|\bclass(es)?\b|lesson|course|quiz|comedy|stand-?up|improv|masterclass|retreat|yoga|meditation|sound ?bath|breathwork|cacao|ecstatic|movie|\bfilm\b|screening|party|\bclub\b|rave\b|afterparty|lecture|ballet|dance (show|school|academy|studio|showcase)|illusion|gala dinner|auditions?|exam|postponed|cancelled|expo|market|wine tasting|tour of|run\b|walk\b|golf|seminar|conference|networking|speed dating|bingo|kids party|silent disco|rehearsal|december season|walking tour|halloween|\bdj\b|graduation|wellness|erotika|birthday celebration",re.I)
MUSIC_KW=re.compile(r"concert|orchestra|choir|symphon|philharmonic|jazz|live\b|tribute|band|quartet|trio|recital|gospel|worship|carols?|hymns|songs|music|unplugged|acoustic|festival|fest\b|singer|piano|guitar",re.I)
def cat_for(title,about,base):
    t=title+" "+(about or "")
    if MUSICAL.search(title) or (base=="theatre" and MUSICAL_STRICT.search(t)): return "musical"
    if FEST.search(title): return "festival"
    return "concert"
def ev(**k):
    k.setdefault("end_date",""); k.setdefault("alt_sources",[]); k.setdefault("notes",""); k.setdefault("venue_address","")
    k.setdefault("time",""); k.setdefault("price_from",""); k.setdefault("ticket_url",""); k.setdefault("lat",None); k.setdefault("lng",None); k.setdefault("geo_source",""); k.setdefault("recurrence",""); k.setdefault("occurrences",[]); k.setdefault("_img","")
    EV.append(k)
# ---------- Quicket (geo search JSON, same data as quicket.co.za search) ----------
Q=json.load(open(f"{RAW}/quicket/algolia_coast_v2.json"))
GRQ={ # id: category  (hand-reviewed Garden Route Quicket listings)
"393493":"festival","391548":"concert","395253":"musical","401035":"concert","392372":"concert","392375":"concert","392382":"concert","392377":"concert",
"397115":"concert","399259":"concert","399044":"festival","397024":"concert","383601":"concert","396377":"concert","397935":"festival","401094":"concert",
"393772":"concert","390041":"concert","400669":"concert","389748":"concert","396754":"concert","392031":"concert","399055":"concert","388199":"concert",
"400050":"concert","400973":"concert","398527":"concert","398838":"concert","399108":"concert","399396":"concert","399888":"concert","398219":"concert",
"398190":"concert","349754":"concert","387081":"festival","398452":"concert","399906":"concert","399904":"concert","399672":"concert","398221":"concert",
"390180":"concert","401267":"concert","389550":"concert","396731":"festival","392725":"festival","375254":"market"}
QNOTES={"396731":"Book/stories festival (Grootbrak Boekeblaf).","392725":"Birding festival (not music).","395253":"Forest Edge Schools musical production.","387081":"Afrikaans music festival on the farm.","397935":"Boutique jazz festival: day & night jazz club shows.","399044":"Oktoberfest beer festival with music.","393493":"Colour festival with music."}
Q_SKIP={"397388"}
FUNQ={ # hand-reviewed community fun runs / charity walks on Quicket (id: note)
"361367":"4.5 km community walk for breast cancer awareness.","400477":"Charity forest cycle & walk for I Love Boobies.","400264":"Charity walk for CANSA.",
"395180":"Charity run on World Homeless Day.","394744":"Charity walk.","399994":"Spring fun run at a wine farm.","398041":"Hospice charity fun run.",
"398261":"5 km birthday charity walk on the Sea Point Promenade.","396776":"Sunset fundraiser walk.","390242":"School fun run.","383490":"Community walk.",
"401426":"Colour fun walk.","384905":"Costumed Halloween zombie walk through the city.","391873":"Charity fun run."}
QTOWN={"Simola Golf and Country Estate":"Knysna","Still Bay":"Stilbaai","Stormsrivier":"Storms River","Keurboomstrand":"Plettenberg Bay","Brenton-on-Sea":"Knysna","Groot-Brakrivier":"Groot Brak","Riversdale":"Riversdale","Saint Francis Bay":"St Francis Bay","St Francis Bay":"St Francis Bay","Sandbaai":"Hermanus","Onrus":"Hermanus"}
def qtime(ts): return datetime.datetime.fromtimestamp(ts,TZ)
for oid,h in Q.items():
    s=qtime(h["DateFrom"]); e=qtime(h["DateTo"]) if h.get("DateTo") else None
    sd=s.strftime("%Y-%m-%d"); ed=e.strftime("%Y-%m-%d") if e else ""
    dl=sorted(qtime(x) for x in (h.get("Dates") or []) if TODAY<=qtime(x).strftime("%Y-%m-%d")<=END)
    if len(h.get("Dates") or [])>1 and dl:
        s=dl[0]; sd=s.strftime("%Y-%m-%d"); ed=max(dl[-1].strftime("%Y-%m-%d"),ed if (e and len(dl)==len(h["Dates"])) else "")
        if ed>END: ed=dl[-1].strftime("%Y-%m-%d")
    if (ed or sd)<TODAY or sd>END: continue
    city=(h.get("City") or "").strip(); geo=h.get("_geoloc") or {}
    lat,lng=geo.get("lat"),geo.get("lng")
    title=html.unescape(h["ProductName"]).strip()
    url="https://www.quicket.co.za"+h["ProductUrl"]
    if oid in FUNQ:
        cat="funrun"; town=QTOWN.get(city,city)
        if town not in TOWNS: town=town_from_geo(lat,lng) if lat else None
        if not town or sd<TODAY: continue
        notes=FUNQ[oid]
    elif h["_box"]=="garden_route":
        if oid not in GRQ: continue
        cat=GRQ[oid]; town=QTOWN.get(city,city)
        if town not in TOWNS: town=town_from_geo(lat,lng) if lat else None
        if not town: continue
        notes=QNOTES.get(oid,"")
    else:
        cats=h.get("Categories") or []
        if len(h.get("Dates") or [])>6 or oid in Q_SKIP: continue
        if sd<TODAY or oid in Q_SKIP: continue
        if EXCL_KW.search(title) or BADVEN.search(h.get("VenueName","")): continue
        if "Music" not in cats and not ("Arts & Culture" in cats and (MUSICAL.search(title) or MUSIC_KW.search(title))) and not FEST.search(title): continue
        if FEST.search(title) and "Music" not in cats and not MUSIC_KW.search(title) and not re.search(r"oktober|beer|wine|food",title,re.I): continue
        if not lat: continue
        town=town_from_geo(lat,lng)
        if not town or TOWNS[town][2]: continue  # wider coast only here
        cat=cat_for(title,"", "music")
        notes="Quicket category: "+", ".join(c for c in cats if c)
    ev(title=title,category=cat,start_date=sd,end_date=ed if ed!=sd else "",time=s.strftime("%H:%M"),town=town,venue=h.get("VenueName","").strip(),
       venue_address=h.get("AddressFormatted",""),ticket_url=url+"#tickets",source_url=url,source_name="Quicket",notes=notes,lat=lat,lng=lng,geo_source="event page" if lat else "",_img=("https:"+h["ImageUrl"]) if h.get("ImageUrl","").startswith("//") else h.get("ImageUrl",""),_prio=1)
# dedupe duplicate Quicket listing of CSNY Plett (398526 == 392377) handled by dedupe below
# ---------- Webtickets ----------
W=json.load(open(f"{RAW}/wt/all_ev.json"))
MON={m:i for i,m in enumerate("JAN FEB MAR APR MAY JUN JUL AUG SEP OCT NOV DEC".split(),1)}
WT_SKIP={"1598588884","1601652195"}
WT_END={"1602663500":"2026-12-19","1601853362":"2026-11-14"}
WT_ALT={"1601853362":["https://www.broadwayworld.com/south-africa/article/INTO-THE-WOODS-Will-Open-at-Theatre-on-Bay-in-October-20260924"]}
WT_NOTE={"1602663500":"Pantomime. Shows 5, 9-11 and 16-19 Dec (per Webtickets calendar)."}  # flamenco dance show
for k,e in W.items():
    if k in WT_SKIP: continue
    s=open(f"{RAW}/wt/ev/{k}.html").read()
    ds=sorted(set((int(y),MON[m],int(d)) for d,m,y in re.findall(r"\b(\d{2})-(JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEP|OCT|NOV|DEC)-(20\d\d) \d{2}:\d{2}",s)))
    tm=re.findall(r"\b\d{2}-(?:JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEP|OCT|NOV|DEC)-20\d\d (\d{2}:\d{2})",s)
    if not ds:
        m=re.search(r"(\d{1,2}) (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]* (20\d\d)",e["meta"])
        if not m: continue
        ds=[(int(m.group(3)),MON[m.group(2).upper()],int(m.group(1)))]
    ds=[d for d in ds if "%04d-%02d-%02d"%d>=TODAY and "%04d-%02d-%02d"%d<=END]
    if not ds: continue
    sd="%04d-%02d-%02d"%ds[0]; ed=WT_END.get(k,"%04d-%02d-%02d"%ds[-1])
    g=e["geo"]
    if not g or not e["venue_full"]: continue
    town=town_from_geo(*g)
    if not town: continue
    title=e["title"]; about=e["about"]
    cats=e["cats"]
    if OPERA.search(title) or EXCL_KW.search(title) or "Postponed" in e["meta"] or "POSTPONED" in title: continue
    if cats==["Theatre"] or set(cats)<= {"Theatre","Christmas"}:
        if not MUSICAL_STRICT.search(title+" "+about[:400]): continue
        cat="musical"
    elif "Festival" in cats and "Music" not in cats:
        if not FEST.search(title): continue
        cat="festival"
    elif "Wine Festival" in cats and "Music" not in cats:
        if not FEST.search(title): continue
        cat="festival"
    elif "Music" in cats:
        if re.search(r"opera\b|don giovanni|stabat",title,re.I) and not MUSICAL.search(title): cat="concert"
        cat=cat_for(title,about[:400],"theatre" if "Theatre" in cats else "music")
        if cat=="musical" and not MUSICAL_STRICT.search(title+" "+about[:300]): cat="concert"
    else: continue
    if re.search(r"dance|ballet",title+" "+about[:200],re.I) and cat!="festival" and not re.search(r"concert|music",title,re.I): continue
    ev(title=title,category=cat,start_date=sd,end_date=ed if ed!=sd else "",time=(tm[0] if tm else ""),town=town,venue=e["venue_full"].split(",")[0],venue_address=e["venue_full"],
       price_from=e["price"],ticket_url=e["url"],source_url=e["url"],source_name="Webtickets",notes=WT_NOTE.get(k,"Webtickets category: "+", ".join(cats)),lat=g[0],lng=g[1],geo_source="event page",alt_sources=WT_ALT.get(k,[]),_img=(re.search(r'property="og:image" content="([^"]+)"',s) or [None,""])[1],_prio=1)
# ---------- Howler (wider coast; GR Howler items are in manual.py) ----------
HW=json.load(open(f"{RAW}/howler/search.json"))
HSEL={ # url: (category, town, venue_address)
"https://www.howler.co.za/GLSHermanus":("concert","Hermanus",""),
"https://oppipanne.howler.co.za/herman":("concert","Hermanus",""),
"https://fatboyslim.howler.co.za/fatboycpt26":("concert","Cape Town",""),
"https://fatboyslim.howler.co.za/fatboycpt26second":("concert","Cape Town",""),
"https://wavglobal.howler.co.za/wavct":("festival","Cape Town","Green Point Track, Cape Town"),
"https://musicpeople.howler.co.za/ll19dec26":("festival","Cape Town",""),
"https://www.howler.co.za/RnBFestCT":("festival","Cape Town",""),
"https://www.howler.co.za/IndieByDayCPT":("festival","Cape Town",""),
"https://musicpeople.howler.co.za/mp18dec26":("concert","Cape Town",""),
"https://www.howler.co.za/mitchellsplainfestival":("festival","Cape Town","Westridge Gardens, Mitchells Plain"),
"https://www.howler.co.za/organicgroovescpt":("festival","Cape Town",""),
}
for u,h in HW.items():
    if "Jbay" in u or "jbay" in u.lower():
        if "all-show-pass" in u: continue
        HSEL[u]=("concert","Jeffreys Bay","")
MONS={m:i for i,m in enumerate("Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split(),1)}
def hdate(s):
    m=re.findall(r"(\d{1,2}) (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)(?: (20\d\d))?",s)
    out=[]
    for d,mo,y in m:
        _ty,_tm=int(TODAY[:4]),int(TODAY[5:7]); y=int(y) if y else (_ty if MONS[mo]>=_tm else _ty+1)
        out.append("%04d-%02d-%02d"%(y,MONS[mo],int(d)))
    return out
for u,(cat,town,addr) in HSEL.items():
    h=HW[u]; ds=hdate(h["date"])
    if not ds: continue
    sd=ds[0]; ed=ds[-1] if len(ds)>1 else ""
    if sd>END or (ed or sd)<TODAY: continue
    # overnight events (e.g. 15 Dec - 16 Dec) are single nights
    if ed and (datetime.date.fromisoformat(ed)-datetime.date.fromisoformat(sd)).days==1 and cat=="concert": ed=""
    pr=re.sub(r"^(From|Tickets)\s*","",h["price"]).strip()
    ven=h["venue"]; m=re.search(r"(-?\d+\.\d+),\s*(-?\d+\.\d+)",ven)
    ev(title=h["title"],category=cat,start_date=sd,end_date=ed,town=town,venue=ven,venue_address=addr,price_from=pr,ticket_url=u,source_url=u,source_name="Howler",notes="",_prio=1)
# ---------- iTickets: Heroes Live (Cape Town) concerts ----------
IT_OK="486126 486127 486144 486145 486248 486285 486310 486320 486330 486396 486482 486623 486774 486779 486798 486809 486895 486897 486898 486899 487082 487170 487171 487357 487501".split()
for line in open(f"{RAW}/itix/all.txt"):
    p=[x.strip() for x in line.split("|")]
    iid=p[0].rsplit("/",1)[1]
    if iid not in IT_OK: continue
    m=re.search(r"(\w{3}) (\d{2}), (20\d\d) ∙ ([\d:]+ [ap]m)",p[1])
    mo={v:k for k,v in MONS.items()}; 
    sd="%s-%02d-%s"%(m.group(3),MONS[m.group(1)],m.group(2))
    t=datetime.datetime.strptime(m.group(4),"%I:%M %p").strftime("%H:%M")
    title=p[2].replace("| Heroes Live","").strip()
    ev(title=title+" – Heroes Live",category="concert",start_date=sd,time=t,town="Cape Town",venue="Heroes Live",venue_address="",ticket_url=p[0],source_url=p[0],source_name="iTickets",notes="",_prio=1)
# ---------- Artscape (venue calendar) ----------
A=json.load(open(f"{RAW}/tribe/www.artscape.co.za.json"))
ASEL={"danger-in-the-dark":"musical","voices-of-the-ages-louis-mhlanga-living-for-the-living":"concert","voices-of-the-ages-internet-athi-polymorphism-love-in-all-its-forms":"concert","voices-of-the-ages-zolani-mahola-people-power":"concert","poetry-and-jazz-sunset-session-2":"concert","umngqungqo-orchestral-experience":"concert","nataniel-sooibrand":"concert","swing-with-the-king-3":"concert","boogie-time-baby":"concert","from-hanover-street-a-concert-commemorating-60-years-2":"concert","oliver-cpt":"musical"}
for e in A:
    slug=e["url"].rstrip("/").rsplit("/",1)[1]
    if slug not in ASEL: continue
    sd=e["start_date"][:10]; ed=e["end_date"][:10]
    t=e["start_date"][11:16]; t="" if t in("00:00","08:00") else t
    ev(title=html.unescape(e["title"]),category=ASEL[slug],start_date=sd,end_date=ed if ed!=sd else "",time=t,town="Cape Town",venue="Artscape Theatre Centre",venue_address="D.F. Malan Street, Foreshore, Cape Town",
       ticket_url=e["url"],source_url=e["url"],source_name="Artscape (venue calendar)",notes="",_img=((e.get("image") or {}).get("url","") if isinstance(e.get("image"),dict) else ""),_prio=2)
# ---------- Manual ----------
TRIBE_IMG={}
for _f in ("visitmosselbay.co.za","www.artscape.co.za"):
    try:
        for _e in json.load(open(f"{RAW}/tribe/{_f}.json")):
            _im=(_e.get("image") or {}).get("url","") if isinstance(_e.get("image"),dict) else ""
            if _im: TRIBE_IMG[re.sub(r"/\d{4}-\d\d-\d\d/(\d+/)?$","/",_e["url"])]=_im
    except Exception: pass
def tribe_img(u): return TRIBE_IMG.get(re.sub(r"/\d{4}-\d\d-\d\d/(\d+/)?$","/",u or ""),"")
for m in manual.M:
    m=dict(m); m["_prio"]=1 if m["source_name"] in("Quicket","Webtickets","Howler","iTickets") else 2
    if not m.get("_img"):
        for _u in [m.get("source_url","")]+list(m.get("alt_sources",[])):
            if tribe_img(_u): m["_img"]=tribe_img(_u); break
    ev(**m)
# Cape Town manual extras
ev(title="Cinderella & FrikaDella (pantomime)",category="musical",start_date="2026-12-05",end_date="2026-12-19",town="Cape Town",venue="Baxter Theatre Centre",venue_address="Main Road, Rondebosch, Cape Town",ticket_url="https://baxter.uct.ac.za/events/cinderella-frikadella",source_url="https://baxter.uct.ac.za/events/cinderella-frikadella",source_name="Baxter Theatre Centre",notes="",_prio=2)
# ---------- filter window, normalise ----------
EV=[e for e in EV if e["start_date"]<=END and (e["end_date"] or e["start_date"])>=TODAY]
def norm(t):
    t=unicodedata.normalize("NFKD",t).encode("ascii","ignore").decode().lower()
    t=re.sub(r"\b(live|in|at|the|and|of|a|ft|feat|presents|tribute|to|experience|2026|2027|concert|edition|show|tour|with)\b"," ",t)
    return set(w for w in re.findall(r"[a-z0-9]+",t) if len(w)>2)
SRC_RANK={"Quicket":1,"Webtickets":1,"Howler":1,"iTickets":1}
EV.sort(key=lambda e:(e["_prio"],SRC_RANK.get(e["source_name"],3)))
kept=[]
for e in EV:
    dup=None
    for k in kept:
        if k["start_date"]==e["start_date"] and k["town"]==e["town"] and (k["category"]==e["category"] or not ({k["category"],e["category"]}&{"funrun","market","community","arts","quiz","festive","nature","sport"})) and not (e["category"] in ("quiz","festive") and (k["venue"]!=e["venue"] or k["title"]!=e["title"])):
            a,b=norm(k["title"]),norm(e["title"])
            if a and b and len(a&b)/min(len(a),len(b))>=0.6: dup=k;break
    if dup:
        for u in [e["source_url"]]+e["alt_sources"]:
            if u!=dup["source_url"] and u not in dup["alt_sources"]: dup["alt_sources"].append(u)
        for f in ("price_from","time","venue_address","ticket_url","end_date"):
            if not dup[f] and e[f]: dup[f]=e[f]
        if not dup["lat"] and e["lat"]: dup["lat"],dup["lng"],dup["geo_source"]=e["lat"],e["lng"],e["geo_source"]
        if e["notes"] and e["notes"] not in dup["notes"] and not e["notes"].startswith(("Quicket category","Webtickets category")): dup["notes"]=(dup["notes"]+" "+e["notes"]).strip()
        continue
    kept.append(e)
EV=kept
# ---------- geo ----------
for e in EV:
    town=e["town"]; c=CENT[town]
    if e["lat"] and hav((e["lat"],e["lng"]),c)>60: e["lat"]=None
    if not e["lat"]:
        qs=[]
        tq=TOWNS[town][0]
        if e["venue_address"]: qs.append(e["venue_address"] if town.split()[0].lower() in e["venue_address"].lower() else e["venue_address"]+", "+tq)
        qs.append(e["venue"].split("(")[0].split("&")[0].strip()+", "+tq)
        for q in qs:
            r=geocode(q)
            if r and hav(r[:2],c)<35 and not (abs(r[0]-c[0])<1e-4 and abs(r[1]-c[1])<1e-4):
                e["lat"],e["lng"],e["geo_source"]=round(r[0],6),round(r[1],6),"nominatim";break
    if not e["lat"]:
        e["lat"],e["lng"],e["geo_source"]=round(c[0],6),round(c[1],6),"town centroid"
    e["lat"]=round(e["lat"],6); e["lng"]=round(e["lng"],6)
# ---------- finalise ----------
EV.sort(key=lambda e:(not TOWNS[e["town"]][2],e["start_date"],e["time"] or "",e["title"]))
FIELDS=["id","title","category","status","status_note","start_date","end_date","time","recurrence","occurrences","nye","xmas","town","region","garden_route","venue","venue_address","lat","lng","geo_source","price_from","ticket_url","source_url","source_name","alt_sources","image","notes","last_checked"]
IMGDIR=os.path.join(_H,"..","images"); CAND={}
def _lj(n):
    try: return json.load(open(os.path.join(_H,n)))
    except Exception: return {}
ST_AUTO=_lj("status_auto.json"); ST_OVR=_lj("status_overrides.json")
out=[]
seen=set()
for e in EV:
    slug=re.sub(r"[^a-z0-9]+","-",unicodedata.normalize("NFKD",e["title"]).encode("ascii","ignore").decode().lower()).strip("-")[:50]
    i=f"{e['start_date']}-{slug}"; n=2
    while i in seen: i=f"{e['start_date']}-{slug}-{n}"; n+=1
    seen.add(i)
    r={"id":i,"region":TOWNS[e["town"]][1],"garden_route":TOWNS[e["town"]][2],"last_checked":CHECKED}
    for f in FIELDS:
        if f in r: continue
        r[f]=e.get(f,"")
    r["title"]=re.sub(r"\s+"," ",r["title"]).strip()
    r["status"],r["status_note"]="scheduled",""
    if ST_AUTO.get(i):
        st,why=ST_AUTO[i][0]; r["status"]=st
        r["status_note"]={"sold out":"Sold out","postponed":"Postponed","cancelled":"Cancelled"}[st]+" per "+("the ticketing page's ticket availability" if "schema" in why else "the ticketing page")+" (checked "+TODAY+")."
    if i in ST_OVR: r.update({k:v for k,v in ST_OVR[i].items() if k in("status","status_note")})
    r["image"]=f"images/{i}.webp" if os.path.exists(os.path.join(IMGDIR,i+".webp")) else ""
    r["occurrences"]=[d for d in (e.get("occurrences") or []) if TODAY<=d<=END]
    CAND[i]={"img":e.get("_img",""),"pages":[u for u in [e.get("ticket_url",""),e["source_url"]]+e["alt_sources"] if u]}
    # New Year's Eve tag (31 Dec of any year); keeps the event's real category
    _sd,_ed=r["start_date"],r["end_date"] or r["start_date"]; _ny=bool(re.search(r"new year|\bnye\b|oujaar|countdown",r["title"],re.I))
    _nyes=[f"{y}-12-31" for y in range(int(_sd[:4]),int(_ed[:4])+1)]
    if r["occurrences"]: r["nye"]=any(d[5:]=="12-31" for d in r["occurrences"]) and _ny
    else:
        _span=(datetime.date.fromisoformat(_ed)-datetime.date.fromisoformat(_sd)).days
        r["nye"]=_sd[5:]=="12-31" or any(_sd<=n<=_ed for n in _nyes) and (_ny or (_span<=6 and r["category"] in("festival","concert")))
    # Christmas tag (carols, Christmas concerts/shows, lights switch-ons, Christmas markets, Christmas lunches/dinners); keeps the real category
    _xm=bool(re.search(r"carol|christmas|kersfees|kersmark|kersliedere|kerskonsert|kerslig|xmas|nativity|heilige nag|lights festival|festive lights|lights switch|father christmas|gift market|gift fair|\bsanta\b",r["title"],re.I))
    if r["occurrences"]: r["xmas"]=_xm and any("11-01"<=d[5:]<="12-26" for d in r["occurrences"])
    else: r["xmas"]=_xm and any(_sd<=f"{y}-12-26" and _ed>=f"{y}-11-01" for y in range(int(_sd[:4]),int(_ed[:4])+1))
    out.append({f:r[f] for f in FIELDS})
os.makedirs(OUT,exist_ok=True)
json.dump(out,open(f"{OUT}/events.json","w"),indent=1,ensure_ascii=False)
with open(f"{OUT}/events.js","w") as f:
    f.write("// Auto-generated by tools/build.py – lets index.html work when opened directly from disk (file://).\nwindow.EVENTS = ")
    json.dump(out,f,ensure_ascii=False); f.write(";\nwindow.EVENTS_BUILT = %s;\n"%json.dumps(CHECKED))
with open(f"{OUT}/events.csv","w",newline="") as f:
    w=csv.DictWriter(f,fieldnames=FIELDS); w.writeheader()
    for r in out: w.writerow({**r,"alt_sources":" | ".join(r["alt_sources"]),"occurrences":" | ".join(r["occurrences"])})
json.dump(CAND,open(os.path.join(_H,"img_candidates.json"),"w"),indent=0)
from collections import Counter
print("total",len(out))
print("GR",sum(r["garden_route"] for r in out))
print(Counter(r["category"] for r in out))
print(Counter(r["region"] for r in out))
print(Counter((r["region"],r["category"]) for r in out if r["garden_route"]))
print(Counter(r["geo_source"] for r in out))
print(Counter(r["source_name"] for r in out))
