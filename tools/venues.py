"""Build tools/venues.csv: one row per venue from data/events.json + data/restaurants.json."""
import json,re,csv,os,collections
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
 ("Stowaway Hideout (Stanley Island)","Plettenberg Bay","https://www.foodyas.com/ZA/Plettenberg-Bay/109413645275891/Stowaway-Hideout","Specials seen are from 2025.")]:
    put(n,t,"Garden Route",True,"venue (no listing)",[u],note)
out=sorted(rows.values(),key=lambda r:(not r["garden_route"],r["region"],r["town"],r["name"].lower()))
with open(f"{R0}/tools/venues.csv","w",newline="") as f:
    w=csv.writer(f);w.writerow(["name","town","region","garden_route","type","events_listed","urls","notes"])
    for r in out: w.writerow([r["name"],r["town"],r["region"],r["garden_route"],"; ".join(sorted(r["types"])),r["events"]," | ".join(sorted(r["urls"])[:4])," ".join(r["notes"])])
print(len(out),sum(r["garden_route"] for r in out))
