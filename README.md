# Garden Route Events

A small static web app listing **real, upcoming concerts, festivals and musicals** on the
**Garden Route** (Mossel Bay, Hartenbos and Groot Brak through George, Oudtshoorn, Wilderness, Sedgefield,
Knysna and Plettenberg Bay to Nature's Valley and Tsitsikamma). It can also show the **rest of the coast**,
from Cape Town to Jeffreys Bay. The data covers **6 Oct 2026 – 28 Feb 2027** and was last checked on 6 Oct 2026.

**Live site:** [christopheralberts.github.io/garden-route-events](https://christopheralberts.github.io/garden-route-events/)

- **List view:** event cards. Garden Route events come first.
- **Calendar view:** a month grid. Multi-day events run across their days; click a day to see its events.
- **Map view:** OpenStreetMap via Leaflet, centred on the Garden Route. Garden Route pins are large and bright; wider-coast pins are small and grey.
- **Shared filters:** Garden Route / All coast toggle, town, category, month and free-text search. They apply to all three views, and the filter state is kept in the URL hash so you can share a filtered link.

Every event links to the page where its details were found (`source_url`), plus any other pages that list it (`alt_sources`).
Nothing is invented: if a detail was not on a source page, the field is left empty.

## How to open it

**Double-click `index.html`.** It works straight from disk (file://) because the data is embedded in `data/events.js`.
The map tiles and the Leaflet library load from the internet, so the map needs a connection. The list and calendar work offline.

Or serve it locally:

```bash
cd garden-route-events
python3 -m http.server 8000
# then open http://localhost:8000
```

When the app is served over http(s), it also fetches `data/events.json` and uses that copy if it differs from the embedded one.

It is a pure static site (no build step, relative paths only), so it runs as-is on GitHub Pages or any static host.
`.nojekyll` stops GitHub Pages from running Jekyll.

## Files

```
index.html          page shell (loads Leaflet from unpkg CDN)
css/style.css       styles (mobile-friendly)
js/app.js           app logic: filters, list, calendar, map
data/events.json    the dataset (array of events)
data/events.js      the same data as `window.EVENTS = [...]`, so file:// works
data/events.csv     the same data for spreadsheets (alt_sources joined with " | ")
tools/              build scripts used to assemble the dataset (see "Refreshing")
```

## Data structure

Each event in `data/events.json` has these fields:

| field | meaning |
|---|---|
| `id` | `YYYY-MM-DD-title-slug`, unique |
| `title` | event name as listed |
| `category` | `concert`, `festival` or `musical` |
| `start_date`, `end_date` | ISO dates; `end_date` is empty for single-day events |
| `time` | start time or time range as listed (SAST), may be empty |
| `town`, `region` | e.g. `Knysna` / `Garden Route`, `Hartenbos` / `Mossel Bay`, `Hermanus` / `Overberg` |
| `garden_route` | `true` for Garden Route events (Mossel Bay area to Tsitsikamma, plus Oudtshoorn) |
| `venue`, `venue_address` | as listed on the source page; may be empty |
| `lat`, `lng` | coordinates for the map |
| `geo_source` | `event page` (coordinates published on the ticket page), `nominatim` (venue geocoded with OpenStreetMap Nominatim), or `town centroid` (approximate, at the town centre) |
| `price_from` | cheapest listed price in rand (e.g. `150`), or text such as `Free entry`; may be empty |
| `ticket_url` | where to buy, if known |
| `source_url`, `source_name` | page where the details were seen |
| `alt_sources` | other pages listing the same event (duplicates merged) |
| `notes` | short context (line-up, caveats) |
| `last_checked` | date the listing was last verified |

## Refreshing the data

The dataset was compiled from ticketing platforms and tourism or venue calendars. These include Quicket, Webtickets, Howler,
iTickets, the Visit Mossel Bay calendar, Visit Knysna, Plett Tourism, On The Route's Garden Route event guide, Artscape, the Baxter
and official festival sites.

To refresh it:

1. Re-harvest the listings. The raw harvest (cached HTML/JSON from those sites) is **not** in this repo; the scripts expected it in `raw/`.
2. Update the hand-checked entries in `tools/manual.py` (festivals and shows found on tourism and official sites).
3. Run `python3 tools/build.py`. It dedupes, geocodes (Nominatim with a cache in `tools/geocache.json`, at most 1 request per second) and rewrites
   `data/events.json`, `data/events.js` and `data/events.csv`.

For a small change you can also edit `data/events.json` by hand. Then regenerate `data/events.js` with:

```bash
python3 -c "import json;d=json.load(open('data/events.json'));open('data/events.js','w').write('window.EVENTS = '+json.dumps(d,ensure_ascii=False)+';\n')"
```

Events whose dates have passed are hidden automatically in the list and on the map.

Dates and prices change, so always check the ticket or source page before you travel.
