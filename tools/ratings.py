#!/usr/bin/env python3
"""IMDb + Rotten Tomatoes scores for the Cinema tab.

tools/ratings_snapshot.json holds real scores keyed by IMDb ID (title, sk_movie_id, imdb, rt, source, date).
* If env OMDB_API_KEY is set, every film in data/cinema.json (now showing + coming soon) that has an IMDb ID is
  looked up on OMDb (www.omdbapi.com/?i=<imdb id>) and the snapshot entry is overwritten/extended with the IMDb rating
  and the Rotten Tomatoes value OMDb returns. Missing values ("N/A") are never filled in.
* Without the key, the snapshot is kept as-is.
merge(data) then adds f["ratings"] = [{"source":"IMDb","value":"8.4"},{"source":"Rotten Tomatoes","value":"94%"}]
to each film whose IMDb ID (or Ster-Kinekor movie id) is in the snapshot. Run standalone to update data/cinema.json/js.
"""
import json, os, sys, datetime, urllib.request, urllib.parse

H = os.path.dirname(os.path.abspath(__file__))
SNAP = os.path.join(H, "ratings_snapshot.json")
OUT = os.path.join(H, "..", "data")

def load():
    try: return json.load(open(SNAP))
    except Exception: return {"films": {}}

def omdb_update(data, snap, key):
    films = (data.get("now_showing") or []) + (data.get("coming_soon") or [])
    n = 0
    for f in films:
        iid = f.get("imdb_id") or next((k for k, v in snap["films"].items() if v.get("sk_movie_id") == f.get("id")), "")
        if not iid: continue
        try:
            j = json.loads(urllib.request.urlopen("https://www.omdbapi.com/?" + urllib.parse.urlencode({"i": iid, "apikey": key}), timeout=20).read())
        except Exception as e:
            print("  omdb failed", iid, e, file=sys.stderr); continue
        if j.get("Response") != "True": continue
        im = j.get("imdbRating") if j.get("imdbRating") not in (None, "", "N/A") else ""
        rt = next((r["Value"] for r in j.get("Ratings", []) if r.get("Source") == "Rotten Tomatoes"), "")
        if not im and not rt: continue
        e = snap["films"].get(iid, {})
        e.update({"title": f.get("title") or e.get("title", ""), "sk_movie_id": f.get("id"), "source": "OMDb (IMDb rating, Rotten Tomatoes)",
                  "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M")})
        if im: e["imdb"] = im
        if rt: e["rt"] = rt
        snap["films"][iid] = e; n += 1
    json.dump(snap, open(SNAP, "w"), indent=1, ensure_ascii=False)
    print(f"ratings: OMDb updated {n} films")

def merge(data, snap=None):
    snap = snap or load()
    byid = {v.get("sk_movie_id"): (k, v) for k, v in snap.get("films", {}).items()}
    for f in (data.get("now_showing") or []) + (data.get("coming_soon") or []):
        k, v = (f.get("imdb_id"), snap["films"][f["imdb_id"]]) if f.get("imdb_id") in snap.get("films", {}) else byid.get(f.get("id"), (None, None))
        f.pop("ratings", None)
        if not v: continue
        r = []
        if v.get("imdb"): r.append({"source": "IMDb", "value": v["imdb"]})
        if v.get("rt"): r.append({"source": "Rotten Tomatoes", "value": v["rt"]})
        if r:
            f["ratings"] = r; f["ratings_source"] = f"{v.get('source','')}, {v.get('date','')}"
            if not f.get("imdb_id"): f["imdb_id"] = k
    return data

def main():
    p = os.path.join(OUT, "cinema.json")
    data = json.load(open(p)); snap = load()
    key = os.environ.get("OMDB_API_KEY", "").strip()
    if key: omdb_update(data, snap, key)
    merge(data, snap)
    json.dump(data, open(p, "w"), indent=1, ensure_ascii=False)
    with open(os.path.join(OUT, "cinema.js"), "w") as fh:
        fh.write("window.CINEMA=" + json.dumps(data, ensure_ascii=False, separators=(",", ":")) + ";\n")
    A = data["now_showing"] + data["coming_soon"]
    print(f"ratings: {sum(1 for f in A if f.get('ratings'))} of {len(A)} films have scores" + ("" if key else " (snapshot; no OMDB_API_KEY)"))

if __name__ == "__main__":
    main()
