#!/usr/bin/env python3
"""Ster-Kinekor Garden Route Mall (George) programme -> data/cinema.json + data/cinema.js

Source: www.sterkinekor.com only (Filmgrail/"Mars" platform). The site's own endpoints:
  * POST /api/GetBlockHtml  {blockName: ActualMovies | UpcomingMovies}  with cookie location=garden-route
      -> the "Now showing" / "Coming soon" poster grids, filtered to that cinema (same HTML the site shows)
  * POST /api/ExecuteApiMethod?blockName=QuickBuyWidget&methodName=getMovies  [26]
      -> JSON for every film bookable at Garden Route (location id 26): runtime, age rating, genres, per-cinema release date
  * GET  /f/<slug>/<id>  film page -> rating text, release date, duration, genres (for films not yet bookable)
If the fetch fails or returns nothing, the previous data/cinema.json is kept untouched (its fetched_at shows when it was last good).
"""
import json, re, html, sys, time, datetime, os, urllib.request

BASE = "https://www.sterkinekor.com"
LOC_ID, LOC_SLUG = 26, "garden-route"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data")
UA = {"User-Agent": "Mozilla/5.0 (GardenRouteEvents weekly build; +https://christopheralberts.github.io/garden-route-events/)"}
CINEMA = {"name": "Ster-Kinekor Garden Route Mall", "town": "George", "address": "Garden Route Mall, N2 Highway & Knysna Rd, George, 6529",
          "phone": "0861 668 437", "url": f"{BASE}/cinemas/{LOC_SLUG}", "location_id": LOC_ID}

def req(url, data=None, cookie=True, timeout=40):
    h = dict(UA)
    if data is not None:
        h.update({"Content-Type": "application/json;charset=UTF-8", "Accept": "application/json"})
        data = json.dumps(data).encode()
    if cookie: h["Cookie"] = "location=" + LOC_SLUG
    for i in range(3):
        try:
            return urllib.request.urlopen(urllib.request.Request(url, data=data, headers=h), timeout=timeout).read().decode("utf-8", "replace")
        except Exception as e:
            err = e; time.sleep(2 + 3 * i)
    raise err

def grid(block):
    body = {"_blockName": "ContainerWithLoadMore", "name": block, "blockName": block, "skip": 0, "take": 500, "step": 500,
            "isLoadAll": True, "hideMonths": True, "showButtonUnderPoster": True, "isOpenFromContentSwitcher": True, "props": {}}
    h = req(BASE + "/api/GetBlockHtml", body)
    out, seen = [], set()
    for chunk in re.split(r'<div class="card_item ', h)[1:]:
        m = re.search(r"goToNewQueryString\('(/f/([^/']+)/(\d+))'\)", chunk)
        if not m or m.group(3) in seen: continue
        seen.add(m.group(3))
        t = re.search(r'card_item__title[^>]*>(.*?)</div>', chunk, re.S)
        img = re.search(r'<img loading="lazy" src="(https://images\.filmgrail\.com/mediaserver/movies/[^"?]+)', chunk)
        lab = re.search(r'card_item__date[^>]*>\s*([^<]+?)\s*</div>', chunk)
        out.append({"id": int(m.group(3)), "slug": m.group(2), "url": BASE + m.group(1),
                    "title": html.unescape(t.group(1).strip()) if t else "",
                    "poster": (img.group(1) + "?optimizer=image&width=342") if img else "",
                    "date_label": lab.group(1).strip() if lab else "",
                    "buy": "Buy tickets" in chunk})
    return out

def bookable():
    qb = {"_blockName": "QuickBuyWidget", "isMobile": False, "children": None, "movies": []}
    j = json.loads(req(BASE + "/api/ExecuteApiMethod?blockName=QuickBuyWidget&methodName=getMovies", {"blockData": qb, "methodData": [LOC_ID]}))
    return {m["movieId"]: m for m in j} if isinstance(j, list) else {}

def page(url):
    t = req(url)
    x = re.sub(r"<script.*?</script>|<style.*?</style>", "", t, flags=re.S)
    x = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", x)))
    g = lambda pat: (re.search(pat, x).group(1).strip() if re.search(pat, x) else "")
    rd = g(r"Release date (\d{2}/\d{2}/\d{4})")
    return {"rating": g(r"\bRating (.+?) Release date"), "release": "-".join(reversed(rd.split("/"))) if rd else "",
            "duration": g(r"Duration (\d+h(?: \d+m)?|\d+m)"), "genres": g(r"Genres ([a-z ,\-]+?) (?:please|Director|Actors|OVERVIEW|Showtimes|Select)")}

def trailer_page(mid):
    """Ster-Kinekor's own trailer modal (/trailer-page?movieId=) embeds the film's trailer URL."""
    t = req(f"{BASE}/trailer-page?movieId={mid}")
    import urllib.parse
    u = urllib.parse.unquote(t)
    m = re.search(r'"trailer"\s*:\s*"(https?://[^"]+)"', u) or re.search(r'youtube\.com/embed/([A-Za-z0-9_-]{11})', u)
    if not m: return ""
    return m.group(1) if m.group(1).startswith("http") else "https://www.youtube.com/watch?v=" + m.group(1)

def details(mid):
    """Ster-Kinekor's trailer modal (/trailer-page?movieId=) embeds the full film record (movieDetails):
    overview, backdrop, director, cast, country, language, imdbId/tmdbId, trailer."""
    import urllib.parse
    t = req(f"{BASE}/trailer-page?movieId={mid}")
    for m in re.finditer(r'decodeURIComponent\("([^"]+)"\)', t):
        try: d = json.loads(urllib.parse.unquote(m.group(1)))
        except Exception: continue
        md = d.get("movieDetails") if isinstance(d, dict) else None
        if isinstance(md, dict) and str(md.get("movieId")) == str(mid): return md
    return {}

def clean_text(h):
    h = re.sub(r"<br\s*/?>|</p>", "\n", h or "", flags=re.I)
    h = html.unescape(re.sub(r"<[^>]+>", " ", h)).replace("\xa0", " ")
    paras = [re.sub(r"[ \t]+", " ", x).strip() for x in h.split("\n")]
    return "\n\n".join(x for x in paras if x)

def one_director(d):
    """Ster-Kinekor's director field often mixes in other crew (e.g. 'Chris Castaldi, ..., Anthony Russo, Joe Russo').
    Only keep it when it is a single name; otherwise omit rather than show the wrong person."""
    names = [x.strip() for x in re.split(r",|;|/| & ", d or "") if x.strip()]
    return names[0] if len(names) == 1 else ""

def clean_trailer(u):
    u = (u or "").strip()
    if not re.match(r"https?://(www\.)?(youtube\.com|youtu\.be|m\.youtube\.com|vimeo\.com)/", u): return ""
    return re.sub(r"[?&]si=[^&]*$", "", u)

def dur(mins):
    if not mins or mins <= 0: return ""
    return f"{mins//60}h {mins%60:02d}m" if mins >= 60 else f"{mins}m"

def main():
    today = datetime.date.today().isoformat()
    now, soon, meta = grid("ActualMovies"), grid("UpcomingMovies"), bookable()
    if not now and not soon:
        raise RuntimeError("Ster-Kinekor returned no films")
    films = []
    for kind, lst in (("now", now), ("soon", soon)):
        for f in lst:
            m = meta.get(f["id"], {})
            try: p = page(f["url"]); time.sleep(0.4)
            except Exception as e: p = {}; print("  film page failed", f["url"], e, file=sys.stderr)
            rel = ((m.get("releases") or {}).get(str(LOC_ID)) or {}).get("releaseDate") or m.get("releaseDate") or ""
            rel = rel[:10] or p.get("release", "")
            try: md = details(f["id"]); time.sleep(0.3)
            except Exception as e: md = {}; print("  details failed", f["id"], e, file=sys.stderr)
            tr = clean_trailer(m.get("trailer")) or clean_trailer(md.get("trailer"))
            cast = [c.get("name", "").strip() for c in (m.get("cast") or md.get("cast") or []) if isinstance(c, dict) and c.get("name")]
            bd = md.get("backdrop") or m.get("backdrop") or ""
            if bd and "filmgrail.com" in bd: bd = bd.split("?")[0] + "?optimizer=image&width=1200"
            genres = m.get("genres") or md.get("genres") or [s.strip() for s in p.get("genres", "").split(",") if s.strip()]
            films.append({"id": f["id"], "title": f["title"] or m.get("title", ""), "section": kind, "url": f["url"],
                          "poster": f["poster"] or m.get("poster", ""), "release_date": rel, "date_label": f["date_label"],
                          "age_rating": p.get("rating") or m.get("ratingName", ""), "age": m.get("ageRating") if (m.get("ageRating") or -1) > 0 else None,
                          "runtime": dur(m.get("runtime")) or p.get("duration", ""), "genres": genres,
                          "bookable": bool(m) or f["buy"], "trailer": tr,
                          "backdrop": bd, "synopsis": clean_text(m.get("overview") or md.get("overview")),
                          "director": one_director(m.get("director") or md.get("director")), "cast": cast[:10],
                          "language": md.get("language") or m.get("language") or "", "country": md.get("country") or m.get("country") or "",
                          "imdb_id": md.get("imdbId") or m.get("imdbId") or "", "tmdb_id": str(md.get("tmdbId") or m.get("tmdbId") or ""), "cinemas": [CINEMA["name"]]})
    films = [f for f in films if f["title"]]
    data = {"source": BASE, "source_note": "Ster-Kinekor website (sterkinekor.com), Garden Route Mall programme",
            "fetched_at": datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), "fetched_date": today, "cinema": CINEMA,
            "now_showing": sorted([f for f in films if f["section"] == "now"], key=lambda f: f["title"].lower()),
            "coming_soon": sorted([f for f in films if f["section"] == "soon"], key=lambda f: (f["release_date"] or "9999", f["title"].lower()))}
    json.dump(data, open(os.path.join(OUT, "cinema.json"), "w"), indent=1, ensure_ascii=False)
    with open(os.path.join(OUT, "cinema.js"), "w") as fh:
        fh.write("window.CINEMA=" + json.dumps(data, ensure_ascii=False, separators=(",", ":")) + ";\n")
    print(f"cinema: {len(data['now_showing'])} now showing, {len(data['coming_soon'])} coming soon at {CINEMA['name']}")
    return data

def fresh(hours=6):
    try:
        d = json.load(open(os.path.join(OUT, "cinema.json")))
        return datetime.datetime.now() - datetime.datetime.strptime(d["fetched_at"], "%Y-%m-%d %H:%M") < datetime.timedelta(hours=hours)
    except Exception: return False

if __name__ == "__main__":
    if "--force" not in sys.argv and fresh():
        print("cinema: data/cinema.json is under 6 h old, not refetching (use --force)"); sys.exit(0)
    try: main()
    except Exception as e:
        print("cinema: fetch failed, keeping last good data/cinema.json:", e, file=sys.stderr)
        sys.exit(0)
