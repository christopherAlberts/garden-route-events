import json,os,time,urllib.parse,subprocess
CACHE=os.path.join(os.path.dirname(__file__),'geocache.json')
UA="GardenRouteEventsApp/0.1 (personal non-commercial events list; contact via github.com/christopherAlberts)"
_c=json.load(open(CACHE)) if os.path.exists(CACHE) else {}
_last=[0]
def geocode(q):
    if q in _c: return _c[q]
    wait=1.1-(time.time()-_last[0])
    if wait>0: time.sleep(wait)
    u="https://nominatim.openstreetmap.org/search?format=jsonv2&limit=1&countrycodes=za&q="+urllib.parse.quote(q)
    r=subprocess.run(["curl","-s","-m","30","-A",UA,u],capture_output=True,text=True).stdout
    _last[0]=time.time()
    try:
        d=json.loads(r); res=[float(d[0]['lat']),float(d[0]['lon']),d[0].get('display_name','')] if d else None
    except Exception: res=None
    _c[q]=res; json.dump(_c,open(CACHE,'w'),indent=0)
    return res
