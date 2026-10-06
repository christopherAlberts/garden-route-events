"""Detect event status (scheduled / postponed / cancelled / sold out).
Sources: title + notes keywords, schema.org eventStatus / offer availability on the
source & ticket pages, and visible page text near the event title. Writes tools/status_auto.json;
hand-checked overrides live in tools/status_overrides.json (they win)."""
import json,os,re,subprocess,hashlib,html
from concurrent.futures import ThreadPoolExecutor
H=os.path.dirname(os.path.abspath(__file__)); C=os.path.join(H,"..","raw","statuscache"); os.makedirs(C,exist_ok=True)
UA="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36"
def get(u):
    fn=os.path.join(C,hashlib.md5(u.encode()).hexdigest())
    if os.path.exists(fn): return open(fn,encoding="utf-8",errors="ignore").read()
    r=subprocess.run(["curl","-sL","-m","30","-A",UA,u],capture_output=True)
    s=r.stdout.decode("utf-8","ignore"); open(fn,"w").write(s); return s
KW=[("cancelled",r"\b(cancell?ed|cancell?ation of the event|gekanselleer|afgestel)\b"),
    ("postponed",r"\b(postponed|uitgestel|rescheduled|new date (to be|tba|tbc))\b"),
    ("sold out",r"\b(sold[\s-]?out|uitverkoop|fully booked|vol bespreek)\b")]
def kw(t):
    for st,p in KW:
        if re.search(p,t or "",re.I): return st
    return ""
def page_status(u):
    s=get(u); out=[]
    for j in re.findall(r'<script[^>]+ld\+json[^>]*>(.*?)</script>',s,re.S|re.I):
        try: o=json.loads(j)
        except Exception: continue
        L=o if isinstance(o,list) else o.get("@graph",[o])
        for x in L:
            if not isinstance(x,dict) or "Event" not in str(x.get("@type")): continue
            es=str(x.get("eventStatus",""))
            if "Cancelled" in es: out.append(("cancelled","schema eventStatus"))
            elif "Postponed" in es or "Rescheduled" in es: out.append(("postponed","schema eventStatus"))
            offs=x.get("offers") or []
            offs=offs if isinstance(offs,list) else [offs]
            av=[str(f.get("availability","")) for f in offs if isinstance(f,dict) and f.get("availability")]
            if av and all("SoldOut" in a for a in av): out.append(("sold out","all ticket types SoldOut (schema)"))
    # (headline/description keyword matching was dropped: too many false positives such as
    #  'last year sold out' or cancellation policies; those cases go to status_overrides.json)
    # explicit ticket-widget phrases
    body=html.unescape(re.sub(r"<[^>]+>"," ",s))
    m=re.search(r"\bthis event (?:has been|is) (cancell?ed|canceled|postponed|sold[- ]out)\b",body,re.I)
    if m:
        w=m.group(1).lower(); out.append(("cancelled" if "cancel" in w else "postponed" if "postpon" in w else "sold out","page text: '"+m.group(0)+"'"))
    return out
def check(e):
    res=[]
    k=kw(e["title"]+" "+e.get("notes",""))
    if k: res.append((k,"title/notes"))
    for u in {e.get("ticket_url",""),e.get("source_url","")}:
        if u and not re.search(r"\.pdf($|\?)",u,re.I):
            try: res+= [(a,b+" @ "+u) for a,b in page_status(u)]
            except Exception: pass
    return e["id"],res
if __name__=="__main__":
    D=json.load(open(os.path.join(H,"..","data","events.json")))
    with ThreadPoolExecutor(12) as ex: R=dict(ex.map(check,D))
    R={k:v for k,v in R.items() if v}
    json.dump(R,open(os.path.join(H,"status_auto.json"),"w"),indent=1)
    for k,v in R.items(): print(k,v)
