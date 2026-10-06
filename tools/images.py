"""Fetch each event's real image (Quicket ImageUrl, og:image on the event/ticket page), resize to <=600px WebP into images/<id>.webp.
Run after build.py, then run build.py again so the `image` field is filled in. Pages are cached in raw/imgcache (not committed)."""
import json,os,re,html,hashlib,subprocess,io,sys
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urljoin
from PIL import Image
H=os.path.dirname(os.path.abspath(__file__)); ROOT=os.path.join(H,"..")
IMG=os.path.join(ROOT,"images"); CACHE=os.path.join(ROOT,"raw","imgcache"); os.makedirs(IMG,exist_ok=True); os.makedirs(CACHE,exist_ok=True)
UA="GardenRouteEventsApp/0.2 (+https://christopheralberts.github.io/garden-route-events/)"
BUA="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36"
SKIP_PAGE=re.compile(r"\.pdf$|georgeherald\.com/Whatson|ontheroute\.co\.za/your-garden-route|carpemusicam\.co\.za/?$|#tickets$",re.I)
BAD_IMG=re.compile(r"logo|favicon|placeholder|default|blank|sprite|icon|avatar|/wt_social|howler-og|share-image|mosselbay-regions|wp-content/uploads/2024/04/|quicket\.co\.za/Q\d+[._]|total-energies|P9042457|Zn8EsOb8s9kSq5woDRdMS2mYlNuPkhET2d2QtgCb",re.I)
def fetch(u,binary=False,timeout=30):
    fn=os.path.join(CACHE,hashlib.md5(u.encode()).hexdigest())
    if os.path.exists(fn): return open(fn,"rb").read()
    for ua in (BUA,UA):
        r=subprocess.run(["curl","-sL","-m",str(timeout),"-A",ua,"-o","-","-w","\n%{http_code}",u],capture_output=True)
        body,_,code=r.stdout.rpartition(b"\n")
        if code.strip()==b"200" and body: open(fn,"wb").write(body); return body
    return b""
def og(page_url):
    if SKIP_PAGE.search(page_url): return ""
    s=fetch(page_url).decode("utf-8","ignore")
    for pat in [r'<meta[^>]+property=["\']og:image(?::secure_url)?["\'][^>]+content=["\']([^"\']+)',r'<meta[^>]+content=["\']([^"\']+)["\'][^>]+property=["\']og:image',
                r'<meta[^>]+name=["\']twitter:image["\'][^>]+content=["\']([^"\']+)']:
        m=re.search(pat,s,re.I)
        if m:
            u=urljoin(page_url,html.unescape(m.group(1)).strip())
            if not BAD_IMG.search(u): return u
    return ""
def save(i,url):
    b=fetch(url,True,40)
    if len(b)<3000: return False
    try:
        im=Image.open(io.BytesIO(b)); im.load()
        if im.width<200 or im.height<150: return False
        im=im.convert("RGB"); im.thumbnail((600,600),Image.LANCZOS)
        im.save(os.path.join(IMG,i+".webp"),"WEBP",quality=62,method=6); return True
    except Exception as ex: return False
C=json.load(open(os.path.join(H,"img_candidates.json")))
def work(item):
    i,c=item
    if os.path.exists(os.path.join(IMG,i+".webp")): return i,"have",""
    urls=[c["img"]] if c["img"] and not BAD_IMG.search(c["img"]) else []
    for p in c["pages"]:
        if len(urls)>=3: break
        u=og(p)
        if u and u not in urls: urls.append(u)
    for u in urls:
        if save(i,u): return i,"ok",u
    return i,"none",""
res={}
with ThreadPoolExecutor(16) as ex:
    for i,st,u in ex.map(work,C.items()):
        res[i]=(st,u); print(st,i,u[:90],flush=True)
log=os.path.join(H,"image_sources.json")
old=json.load(open(log)) if os.path.exists(log) else {}
for i,(st,u) in res.items():
    if st=="ok": old[i]=u
old={i:u for i,u in old.items() if i in C}
json.dump(old,open(log,"w"),indent=0)
print("done",sum(1 for s,_ in res.values() if s in("ok","have")),"/",len(res))
