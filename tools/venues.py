"""Build tools/venues.csv: one row per venue from data/events.json + data/restaurants.json."""
import json,re,csv,os,collections,sys
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from towns import TOWNS as _TW
R0=os.path.join(os.path.dirname(os.path.abspath(__file__)),"..")
E=json.load(open(f"{R0}/data/events.json"));RS=json.load(open(f"{R0}/data/restaurants.json"))
GR_REG={"Garden Route","Mossel Bay","Hessequa (Stilbaai)"}
ALIAS={"moedergemeente church":"ng moeder","mossel bay town hall":"mossel bay stadsaal","beach house bar":"wilderness beach house","beacon island resort":"beacon isle resort","southern sun beacon island":"beacon isle resort",
 "simola hotel country club spa":"simola","simola golf and country estate":"simola","simola country hotel spa":"simola",
 "knysna gin distillery cocktail bar":"knysna gin","34 waenhout live venue":"34 waenhout","34 waenhout live venue knysna":"34 waenhout",
 "blend country restaurant pub":"blend","slops plett":"slops","hope church hope family":"hope church",
 "fairy knowe hotel venues across the village":"fairy knowe hotel","fairy knowe hotel wilderness":"fairy knowe hotel",
 "beach house bar kitchen wilderness beach house backpackers":"wilderness beach house","beach house bar kitchen":"wilderness beach house",
 "cula restaurant bar":"cula","tapas oysters thesen island":"tapas oysters","the pottery george":"pottery","red bridge brewing co":"red bridge brewing",
 "fancourt hotel":"fancourt","fancourt":"fancourt"}
def key(n):
    n=re.sub(r"\(.*?\)","",n.lower()); n=n.split(",")[0]
    n=re.sub(r"[’'`]s\b","s",n); n=re.sub(r"[^a-z0-9 ]"," ",n); n=re.sub(r"\b(the|at)\b"," ",n); n=re.sub(r"\s+"," ",n).strip()
    n=ALIAS.get(n,n)
    for pre in PREFIX:
        if n.startswith(pre): return pre
    return n
PREFIX=["fancourt","simola","knysna gin","kingswood","fairy knowe hotel","beach house bar","wilderness beach house","atkv","rijk","ng moeder","mossel bay stadsaal","mossel bay town hall","garden route botanical","herold","loerie park","34 waenhout","hennies george"]
SKIP=re.compile(r"^(george|plettenberg bay|hartenbos|great brak river|venue to be confirmed|various venues.*|secret beach.*|anywhere in.*|tba|tbc|online|)$")
rows={}
def put(name,town,region,gr,typ,urls,note=""):
    k=(key(name),town)
    if SKIP.match(k[0]) or SKIP.match(name.lower()): return
    r=rows.setdefault(k,dict(name=name,town=town,region=region,garden_route=gr,types=set(),urls=set(),events=0,notes=set()))
    if len(name)<len(r["name"]): r["name"]=name
    r["types"].add(typ); r["urls"].update(u for u in urls if u); 
    if note: r["notes"].add(note)
    if typ=="event venue": r["events"]+=1
for e in E:
    put(e["venue"],e["town"],e["region"],bool(e.get("garden_route")) or e["region"] in GR_REG,"event venue",[e.get("source_url")])
for r in RS:
    put(r["name"],r["town"],r.get("region",""),bool(r.get("garden_route")) or r.get("region") in GR_REG or r["town"] in("George","Knysna","Wilderness","Plettenberg Bay","Mossel Bay","Sedgefield"),"restaurant card",[r.get("website")]+[s["url"] for s in r.get("sources",[])],r.get("notes",""))
# Venues discussed but with no listing yet
for n,t,u,note in [("Bossa George","George","https://bossagoodtimes.com/branches/george/","Heard as 'Borsa'. No events/specials found 7 Oct 2026."),
 ("Polpetta George","George","https://visitgeorge.co.za/directory/polpetta-george/","Heard as 'Palpetta'. No events/specials found 7 Oct 2026."),
 ("Outeniqua Transport Museum","George","https://www.georgeherald.com/News/Article/Local-News/transport-museum-opens-temporarily-202607010954","Closed after May 2026 storm damage; only temporarily reopened 27 Jun-12 Jul 2026 for The Market. No reopening date or 2026 events confirmed (Oct 2026). Annual December market venue uncertain."),
 ("Old Nick Village","Plettenberg Bay","https://oldnickvillage.co.za/","Plettenberg Bay (N2, 3 km east of town), not Wilderness. Weekly Wednesday Market listed; past years had Christmas Eve and Easter markets."),
 ("Victoria Bay (surf contests)","George","https://surfingsouthafrica.co.za/2025contestcalendar/category/competitions/2026-contest-calendar/","Surf break; contests run by Surfing South Africa / WSL Africa / Eden Surfriders. 2026 contests (Vic Bay Quad 12-14 Jun, Rip Curl Vic Bay Surf Pro 19-21 Jun, Billabong Junior SAST #6 25-27 Sep) are past; nothing upcoming as of 7 Oct 2026. Also watch worldsurfleague.com (Africa QS) and visitgeorge.co.za."),
 ("George Showgrounds","George","https://georgelandbouskou.co.za/","R102, Groeneweide Park. George Agricultural Show (Aug 2027: 26-28 Aug); George Motor Club stock car oval (https://georgemotorclub.racing/race-calendar/, MSA https://www.motorsport.co.za/venue/george-showgrounds-george/)."),
 ("George Motor Club oval track (George Showgrounds)","George","https://georgemotorclub.racing/race-calendar/","Stock car and dirt karting oval. Cross-check the MSA calendar (organiser DO4SA-GEORGE). 'Passion for Speed' 10 Oct 2026 appears only on a third-party directory, not on the club site or MSA, so it was not added."),
 ("Arnold de Jager Oval Track","Oudtshoorn","https://www.motorsport.co.za/organizer/do4sa-oudts/","Oudtshoorn Motor Club stock car oval. Events are on the MSA calendar (organiser DO4SA-OUDTS)."),
 ("Redrock Raceway","Oudtshoorn","https://www.motorsport.co.za/organizer/do4sa-oudts/","Named only in the MSA PDF calendar (01.10.2026) for the 31 Oct 2026 Oudtshoorn MC meeting. The MSA event page says Arnold de Jager Oval Track. No other listing found."),
 ("KKNK festival venues across Oudtshoorn","Oudtshoorn","https://www.kknk.co.za/","KKNK (Klein Karoo Nasionale Kunstefees), an annual arts festival at multiple venues. KKNK 2027: 23-27 Mar 2027 (official site). Watch for the programme and ticket launch, and for KKNK projects such as ReWOLusie and Klein Karoo Klassique."),
 ("Sky Lounge","Mossel Bay","https://visitmosselbay.co.za/event/karaoke-night-sky-lounge-2/","Bar/lounge, 29 Essenhout St, Heiderand (per directory listings). Weekly Sunday karaoke with DJs on the Visit Mossel Bay calendar. Earlier DJ shows (Ice Flake Show Dec 2024, Birthday Bash Feb 2025) were also listed there. Phone 079 508 2412."),
 ("Bravo Lounge, Garden Route Casino","Mossel Bay","https://www.gardenroutecasino.co.za/dining/","Casino entertainment lounge, 1 Pinnacle Point Road: jazz, cabaret, comedy, live bands. Events show up on Webtickets/Quicket/Computicket and Visit Mossel Bay; the casino's own What's On page lists no dated shows."),
 ("Zeppelins Bar","Mossel Bay","https://www.zeppelinsrock.com/","Rock & roll pub with DJs, bands, quiz nights and dress-up parties, 9 Marsh St, open daily 09:00-02:00. Official events page is empty (only 2023/24 events). Latest Facebook posts (via Foodyas) are from Jan 2026, including NYE 25/26. Nothing upcoming as of 8 Oct 2026. FB via https://www.foodyas.com/ZA/Mossel-Bay/893208957368228/Zeppelins"),
 ("Die Kuiergat","Mossel Bay","https://webticket.co.za/v2/event.aspx?itemid=1578624402","Bar/restaurant with live music, 91 Marsh St (079 172 0973). Runs 'Live Lounge' shows on Webtickets (Dirk van der Westhuizen Jun 2025, Jaakie 5 Dec 2025). Reviews mention Sunday karaoke, bingo and quiz nights, but no official schedule was found. Official site diekuiergat.co.za returned 404 on 8 Oct 2026. Nothing upcoming."),
 ("Koze Kuse Lounge","Mossel Bay","https://www.foodyas.com/ZA/Mossel-Bay/115062648135355/Koze-Kuse-Lounge-Reloaded","Lounge/club at 52 Scholtz St, KwaNonqaba (073 366 6363). DJ nights and 'The Plug Fridays' were announced in May-Jun 2026, but there have been no posts since early June 2026, so nothing was added."),
 ("Patrick's Pub and Restaurant","Mossel Bay","https://visitmosselbay.co.za/listing/patricks-pub-and-restaurant/","Irish-style pub, 19 Marsh St (044 691 0077): pool tables, slots, satellite TV. No events or music nights listed."),
 ("The Beach Bar","Mossel Bay","https://www.quicket.co.za/events/401482-real-nice-presents-mossel-biza/","Diaz Beach / Die Voor Bay, 26 Beach East Blvd. REAL NICE parties on 4, 11 and 12 Dec 2026 are in the app (Quicket). No weekly DJ or live-music nights published. FB: facebook.com/TheBeachBarDiaz"),
 ("GardenRoute.com events listing","George","https://www.gardenroute.com/event/","Source: regional events listing (6 pages, incl. weekly markets). Re-scan for new dated events."),
 ("Garden Route Guide events page","George","https://www.gardenrouteguide.co.za/garden-route-events/","Source: single-page guide of annual/weekly events by town; many 'to be confirmed' dates. Re-scan for confirmed dates."),
 ("Visit Mossel Bay events calendar","Mossel Bay","https://visitmosselbay.co.za/events/","Source: tourism calendar (The Events Calendar; JSON at /wp-json/tribe/events/v1/events). Re-scan all pages."),
 ("On The Route events calendar & weekly guide","George","https://www.ontheroute.co.za/events-calendar/","Source: Garden Route events calendar plus weekly 'Your Garden Route event guide' posts (see /rss/). Calendar data is an inline JS array."),
 ("Karoo 62 Escape","Ladismith","https://www.quicket.co.za/events/386068-vortex-open-source-2026","Festival venue on Route 62 near Ladismith (Universal Frequencies, Vortex Open Source)."),
 ("The Blue Shed (Open Plan Pictures)","Mossel Bay","https://openplanpictures.co.za/","Film screenings at 33 Bland St, listed on the Visit Mossel Bay calendar."),
 ("Simola Hillclimb (Old Cape Road, Simola)","Knysna","https://www.speedfestival.co.za/","Simola Hillclimb / Knysna Speed Festival, every late April-early May. 2027: 29 Apr-2 May. Future dates: 27-30 Apr 2028, 26-29 Apr 2029, 2-5 May 2030."),
 ("Simola Hotel, Country Club & Spa","Knysna","https://www.quicket.co.za/events/392031-woodstock-beyond-1965-1975-live-in-knysna/","Hotel hosting regular tribute shows and comedy (mostly on Quicket; search 'Simola'). simola.co.za has no events page."),
 ("parkrun (Garden Route & Kouga events)","George","https://www.parkrun.co.za/events/","Source: all parkruns from Witsand to Jeffreys Bay are added as weekly series (event list: images.parkrun.com/events.json). Re-check for new events or start-time changes."),
 ("The Galileo Open Air Cinema","Cape Town","https://thegalileo.co.za/movies/","Source: open-air cinema season (15 Oct 2026 - 15 May 2027) at Kirstenbosch, the V&A, Century City, Norval Foundation and Winelands estates. Show pages are at /movie/<slug>/ (list: /wp-json/wp/v2/movie). Tickets: Webtickets itemid 1600185548. No Garden Route venues."),
 ("Open Plan Pictures (Garden Route outdoor & indoor cinema)","Plettenberg Bay","https://www.quicket.co.za/events/394767-halloween-old-nick/","Source: runs the Garden Route's outdoor movies (summer beach nights at Lookout/Hobie Beach and Sky Villa in Plett, Santos Beach in Mossel Bay), winter indoor shows at Global Village, and the Blue Shed (Mossel Bay). Tickets on Quicket (organiser 'Open Plan Pictures'); also openplanpictures.co.za, WhatsApp 072 896 1034. Re-check from November for the summer beach line-up."),
 ("In Toto Retreat","Sedgefield","https://intotoretreat.co.za/","Community hub at 55 Jan van Riebeeck St, The Island, Sedgefield; hosts film screenings (Quicket)."),
 ("Die Bush Lapa (Herold's Bay Eco Resort)","George","https://visitgeorge.co.za/event/big-screen-bok-rugby/","'Bush Lapa': concert venue at Herold's Bay Eco Resort, Oubaai Road, George (contact Byron Minnie 079 404 5875). Afrikaans and SA music shows, usually Doors 18:00, pre-acts 19:00, main act 21:00, from about R250, sold on Webtickets ('... @ Bush Lapa'). Annual December Musiekfees (2025: 16 Dec-2 Jan). Bandsintown lists Juanita du Plessis 6 Nov, Demi Lee Moore 14 Nov and Ryno Velvet 17 Dec 2026, but these aren't confirmed on Webtickets or official channels yet; re-check."),
 ("Elvis Brew Padstal","George","https://www.quicket.co.za/organisers/74130-elvis-brew","'Elvis Brue' = Elvis Brew, Elvis Blue's coffee shop / padstal chain. Padstal on the R404 opposite George Airport, next to Bargain Nursery (061 548 5155); open Mon-Sat 07:30-17:00, Sun 08:00-15:00. Other branches: 131 York St George, Kleine Elvis Brew at ATKV Strandverhoog Hartenbos, and Market Square in Oudtshoorn. Hosts occasional Elvis Blue shows (Padstal Piekniek, acoustic sets) on Quicket; no public upcoming events as of 8 Oct 2026."),
 ("Stowaway Hideout (Stanley Island)","Plettenberg Bay","https://www.foodyas.com/ZA/Plettenberg-Bay/109413645275891/Stowaway-Hideout","Specials seen are from 2025.")]:
    put(n,t,_TW.get(t,("","Garden Route"))[1],True,"venue (no listing)",[u],note)
out=sorted(rows.values(),key=lambda r:(not r["garden_route"],r["region"],r["town"],r["name"].lower()))
with open(f"{R0}/tools/venues.csv","w",newline="") as f:
    w=csv.writer(f);w.writerow(["name","town","region","garden_route","type","events_listed","urls","notes"])
    for r in out: w.writerow([r["name"],r["town"],r["region"],r["garden_route"],"; ".join(sorted(r["types"])),r["events"]," | ".join(sorted(r["urls"])[:4])," ".join(r["notes"])])
print(len(out),sum(r["garden_route"] for r in out))
