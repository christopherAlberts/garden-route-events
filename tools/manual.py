# Hand-curated entries. Every entry's details were read on source_url (and alt_sources).
# Fields not shown on the source are left empty.
OTR="https://www.ontheroute.co.za/your-garden-route-event-guide-1-october/"
MB="https://visitmosselbay.co.za/event/"
M=[]
def add(**k): M.append(k)

# ---------------- Garden Route / Mossel Bay / Oudtshoorn ----------------
add(title="Wilderness Arts Festival",category="festival",start_date="2026-10-08",end_date="2026-10-11",time="09:00-17:00",town="Wilderness",venue="Fairy Knowe Hotel & venues across the village",venue_address="1 Dumbleton Road, Wilderness",price_from="",ticket_url="",source_url=OTR,source_name="On The Route (Garden Route event guide)",alt_sources=["https://www.wildernessartfestival.co.za/"],notes="Visual art, music, performance and literature; open to the public.")
add(title="Hemelruim – desert disco open-air concert (Spoegwolf, Tasché, Noemwoord)",category="concert",start_date="2026-10-10",time="Gates 17:00, music 18:00",town="Oudtshoorn",venue="Oudtshoorn Sports Grounds (REC)",price_from="R295",ticket_url="",source_url=OTR,source_name="On The Route (Garden Route event guide)",alt_sources=["https://www.diehoorn.com/nuus/hemelruim-bring-woestyn-disko/"],notes="Tickets at Computicket, Checkers, Shoprite, Usave; cheaper in advance. Klein Karoo, listed in Garden Route guide.")
add(title="Knysna RnB, Soul and Afro-Pop 2026",category="festival",start_date="2026-10-10",time="10:00-22:00",town="Knysna",venue="Loerie Park",venue_address="",price_from="R150",ticket_url="",source_url="https://www.toodoo.co.za/knysna-rnb-soul-and-afro-pop-2026/",source_name="toodoo.co.za",alt_sources=[],notes="Full-day R&B/soul/Afro-pop festival; tickets via Computicket per listing.")
add(title="RE/MAX 10th Garden Route Kite Festival",category="festival",start_date="2026-10-18",time="09:30",town="Sedgefield",venue="Scarab Village",venue_address="",price_from="",ticket_url="",source_url="https://www.visitknysna.co.za/whats-on/events/garden-route-kite-festival-3/",source_name="Visit Knysna",alt_sources=[OTR,"https://www.toodoo.co.za/garden-route-kite-festival-2026/"],notes="International kite flyers, family day.")
add(title="Magnificent Movie Music – Carpe Musicam! Concert Orchestra & Choir",category="concert",start_date="2026-10-11",time="15:30-19:00",town="Mossel Bay",venue="Dias Museum",venue_address="1 Market Street, Mossel Bay",price_from="",ticket_url="https://paystack.com/buy/11oct-mmm",source_url=MB+"magnificent-movie-music/",source_name="Visit Mossel Bay (tourism calendar)",alt_sources=[],notes="Film scores performed live (the Sedgefield show on 4 Oct was R180).")
for d in ["2026-10-10","2026-10-17","2026-10-24","2026-10-31"]:
    add(title="Misty Valley Octoberfest",category="festival",start_date=d,time="09:00",town="Mossel Bay",venue="Misty Valley Farm",venue_address="Misty Valley Farm, Brandwacht, Mossel Bay",price_from="Free entry",ticket_url="",source_url=MB+"misty-valley-octoberfest/"+d+"/",source_name="Visit Mossel Bay (tourism calendar)",alt_sources=[OTR],notes="Craft beer, food, live music; runs on Saturdays in October.")
add(title="Louvain Burn Music & Arts Festival",category="festival",start_date="2026-11-06",end_date="2026-11-09",time="",town="Oudtshoorn",venue="Louvain Guest Farm",price_from="R1380",ticket_url="https://louvainburnkaroo.com/buytickets/",source_url="https://louvainburnkaroo.com/buytickets/",source_name="Louvain Burn (official site)",alt_sources=[OTR],notes="Camping festival; full passes incl. 3 nights camping (Round 2 price). No day passes.")
add(title="Leisure Isle Festival 2026",category="festival",start_date="2026-11-07",end_date="2026-11-08",time="Sat 09:00-17:00, Sun 10:00-15:00",town="Knysna",venue="Leisure Isle",venue_address="",price_from="",ticket_url="",source_url="https://www.visitknysna.co.za/whats-on/events/2026-leisure-isle-festival/",source_name="Visit Knysna",alt_sources=[OTR,"https://www.leisureisleknysna.co.za/the-leisure-isle-festival/"],notes="21st charity festival: stalls, food, family fun, fun run/walk.")
add(title="Eden Fest 2026",category="festival",start_date="2026-11-07",time="08:00-19:00",town="Mossel Bay",venue="Die Gat",venue_address="Mayixhale Street, KwaNonqaba, Mossel Bay",price_from="",ticket_url="",source_url=MB+"eden-fest-2026/",source_name="Visit Mossel Bay (tourism calendar)",alt_sources=[],notes="Music, sport, vehicles and food festival.")
add(title="MosJazz 2026",category="festival",start_date="2026-11-26",end_date="2026-11-29",time="All day",town="Mossel Bay",venue="Santos Beach (De Bakke Santos Beach Resort)",venue_address="Santos Beach, Mossel Bay",price_from="",ticket_url="",source_url=MB+"mosjazz-2026/",source_name="Visit Mossel Bay (tourism calendar)",alt_sources=[OTR],notes="11th year: jazz, Afrobeat, soul and R&B on the beachfront.")
add(title="Plett Rage 2026",category="festival",start_date="2026-11-27",end_date="2026-12-03",time="",town="Plettenberg Bay",venue="Plettenberg Bay Main Beach",price_from="R1900",ticket_url="https://plettrage.howler.co.za/plettrage26",source_url="https://plettrage.howler.co.za/plettrage26",source_name="Howler",alt_sources=["https://www.plett-tourism.co.za/events/plett-rage-2026/",OTR],notes="School-leavers' festival.")
add(title="Matriekbaai 2026",category="festival",start_date="2026-11-27",end_date="2026-12-05",time="",town="Mossel Bay",venue="Diaz Hotel and Resort",venue_address="1 Beach East Blvd, Die Voor Bay, Mossel Bay",price_from="Free (registration)",ticket_url="https://www.howler.co.za/matriekbaai2026",source_url=MB+"matriekbaai-2026/",source_name="Visit Mossel Bay (tourism calendar)",alt_sources=["https://www.howler.co.za/matriekbaai2026",OTR],notes="School-leavers' festival, ages 18-22.")
add(title="AmfiHart 2026 (incl. Spoegwolf)",category="festival",start_date="2026-12-04",end_date="2026-12-05",time="",town="Hartenbos",venue="ATKV Hartenbos Amphitheatre",venue_address="169 Majuba Avenue, Hartenbos",price_from="R175",ticket_url="https://www.howler.co.za/AmfiHart26",source_url="https://www.howler.co.za/AmfiHart26",source_name="Howler",alt_sources=[MB+"amfihart-2026/",OTR],notes="5th AmfiHart: artists over 4-5 Dec, funfair, food stalls, market.")
add(title="Garden Route Rare Plant Festival",category="festival",start_date="2026-12-12",end_date="2026-12-13",time="",town="George",venue="Garden Route Botanical Garden",venue_address="",price_from="",ticket_url="",source_url=OTR,source_name="On The Route (Garden Route event guide)",alt_sources=[],notes="Third annual gathering for collectors of rare plants (not a music event).")
add(title="Float Fest SA – Groot Brak 2026",category="festival",start_date="2026-12-18",time="09:00-20:00",town="Groot Brak",venue="Suiderkruis Beach picnic area",venue_address="Suiderkruis Beach, Great Brak River",price_from="R250",ticket_url="https://weticket.co.za/event/details/1000189-float-fest-groot-brak",source_url=MB+"float-festival-grootbrak/",source_name="Visit Mossel Bay (tourism calendar)",alt_sources=["https://www.toodoo.co.za/float-fest-groot-brak-2026/",OTR],notes="River floating, live music and DJs. Price per adult as listed on toodoo.")
add(title="Hartenbos GrootFees: AiG-Buitelug",category="festival",start_date="2026-12-19",time="19:00-23:00 (gates 17:00)",town="Hartenbos",venue="ATKV Hartenbos Amphitheatre",venue_address="169 Majuba Avenue, Hartenbos",price_from="R295",ticket_url="https://itickets.co.za/events/486560",source_url="https://itickets.co.za/events/486560",source_name="iTickets",alt_sources=[MB+"aig-buitelug-hartenbos-grootfees/","https://afrmusieknuus.co.za/2026/08/27/betify-hartenbos-grootfees-2026-nog-groter-die-jaar/"],notes="Demi Lee Moore, Ruhan du Toit, Ricus Nel, Jo Black, Refentse, Barto, Juanita du Plessis, JACOBUS, Juan Boucher. Kids under 13 R150.")
add(title="Hartenbos GrootFees: Alternatief is Groot",category="festival",start_date="2026-12-29",time="16:00",town="Hartenbos",venue="ATKV Hartenbos Amphitheatre",venue_address="169 Majuba Avenue, Hartenbos",price_from="R295",ticket_url="",source_url=MB+"alternatief-is-groot-hartenbos-groot-fees/",source_name="Visit Mossel Bay (tourism calendar)",alt_sources=["https://afrmusieknuus.co.za/2026/08/27/betify-hartenbos-grootfees-2026-nog-groter-die-jaar/"],notes="JACOBUS, ONS, Die Heuwels Fantasties, Francois van Coke, Spoegwolf, Droomsindroom, G-String. Price per afrmusieknuus (general access).")
add(title="Hartenbos GrootFees: GrootJol (New Year's Eve)",category="festival",start_date="2026-12-31",time="19:00-23:00 (gates 17:00)",town="Hartenbos",venue="ATKV Hartenbos Amphitheatre",venue_address="169 Majuba Avenue, Hartenbos",price_from="R295",ticket_url="https://itickets.co.za/register/new/486562",source_url="https://itickets.co.za/register/new/486562",source_name="iTickets",alt_sources=[MB+"groot-jol-hartenbos-groot-fees/","https://afrmusieknuus.co.za/2026/08/27/betify-hartenbos-grootfees-2026-nog-groter-die-jaar/"],notes="Brendan Peyper, Robbie Wessels, Appel, Bernice West, Monique Steyn, Liezel Pieters, Danny Smoke, Chris Steyn.")
add(title="Punt in die Wind Kunste-Week (arts festival)",category="festival",start_date="2026-12-19",end_date="2026-12-26",time="",town="Mossel Bay",venue="Mossel Bay Stadsaal (Town Hall)",venue_address="Mossel Bay Town Hall, Mossel Bay",price_from="",ticket_url="https://itickets.co.za/events/486614",source_url="https://itickets.co.za/events/486614",source_name="iTickets",alt_sources=[],notes="Multi-day access; Afrikaans music, theatre and kids' shows.")
for iid,title,d,t in [("486591x","",None,None)]: pass
for iid,title,d,t in [("486199","Steve Hofmeyr – Punt in die Wind","2026-12-20","20:00"),("486200","Marion Holm – Punt in die Wind","2026-12-21","10:00"),("486592","Bobby van Jaarsveld – Punt in die Wind","2026-12-23","20:00"),("486213","Magda & Erhard Louw – Punt in die Wind","2026-12-24","13:00"),("486215","Klipwerf (langarm dance) – Punt in die Wind","2026-12-26","20:00")]:
    add(title=title,category="concert",start_date=d,time=t,town="Mossel Bay",venue="Mossel Bay Stadsaal (Town Hall)",venue_address="Mossel Bay Town Hall, Mossel Bay",price_from="",ticket_url="https://itickets.co.za/events/"+iid,source_url="https://itickets.co.za/events/"+iid,source_name="iTickets",alt_sources=[],notes="Part of Punt in die Wind Kunste-Week.")
# ReedValley concerts (Visit Mossel Bay calendar)
RV=dict(town="Mossel Bay",venue="ReedValley",venue_address="ReedValley Farm, R327, Mossel Bay",source_name="Visit Mossel Bay (tourism calendar)",ticket_url="",alt_sources=[])
for slug,title,d,price in [("jo-black-live-at-reedvalley","Jo Black Live at ReedValley","2026-10-10","R220"),("the-rivertones-at-reedvalley","The Rivertones at ReedValley","2026-10-30","R250"),("jakkie-louw-live-at-reedvalley","Jakkie Louw Live at ReedValley","2026-11-07",""),("dozi-live","Dozi Live at ReedValley","2026-11-13",""),("christia-visser-live","Christia Visser Live at ReedValley","2026-11-14",""),("amy-winehouse-tribute-at-reedvalley","Amy Winehouse Tribute at ReedValley","2026-11-27","R200"),("see-sand-live","See & Sand Live at ReedValley","2026-12-14",""),("chera-lee-live","Chera Lee Live at ReedValley","2026-12-15",""),("ballyhoo-live","Ballyhoo Live at ReedValley","2026-12-17",""),("mathys-roets-live-at-reedvalley","Mathys Roets Live at ReedValley","2026-12-19","R250"),("refentse-live-at-reedvalley","Refentse Live at ReedValley","2026-12-20","R295"),("roan-ash-live-at-reedvalley","Roan Ash Live at ReedValley","2026-12-21","R350"),("tribute-to-elvis-at-reedvalley","Tribute to Elvis Presley (James Marais & Monique Cassells) at ReedValley","2026-12-22","R200"),("joshua-na-die-reen-live-at-reedvalley","Joshua na die Reën Live at ReedValley","2026-12-23","R270"),("jaun-boucher-live-at-reedvalley","Juan Boucher Live at ReedValley","2026-12-26","R350"),("glaskas-live-at-reedvalley","Glaskas Live at ReedValley","2026-12-28","R280"),("masters-of-rock-mark-haze-group","Masters of Rock – Mark Haze & Group (NYE) at ReedValley","2026-12-31","R450"),("tribute-to-neil-diamond-at-reedvalley-2","Tribute to Neil Diamond at ReedValley","2027-01-04","R300"),("tribute-to-neil-diamond-at-reedvalley-3","Tribute to Neil Diamond at ReedValley","2027-01-05","R300")]:
    add(title=title,category="concert",start_date=d,time="20:00",price_from=price,source_url=MB+slug+"/",notes="",**RV)
# Howler – Garden Route
H="Howler"
add(title="Get Lucky Summer (Beacon Isle) Plett – Matthew Mole & friends (Edition 1)",category="concert",start_date="2026-12-20",time="",town="Plettenberg Bay",venue="Beacon Isle Resort",venue_address="Beacon Island Crescent, Plettenberg Bay",price_from="R180",ticket_url="https://www.howler.co.za/GLSBI1",source_url="https://www.howler.co.za/GLSBI1",source_name=H,alt_sources=[],notes="")
add(title="Get Lucky Summer (Beacon Isle) Plett – Prime Circle & Lee Cole (Edition 2)",category="concert",start_date="2026-12-27",time="15:00-21:00",town="Plettenberg Bay",venue="Beacon Isle Resort",venue_address="Beacon Island Crescent, Plettenberg Bay",price_from="R180",ticket_url="https://www.howler.co.za/GLSBI2",source_url="https://new-ux.howler.co.za/events/get-lucky-summer-beacon-isle-plett-ft-prime-circle-lee-cole-edition-2-1074",source_name=H,alt_sources=["https://www.howler.co.za/GLSBI2"],notes="Lawns at Beacon Island.")
add(title="Get Lucky Summer (Beacon Isle) Plett – Will Linley & friends (Edition 3)",category="concert",start_date="2027-01-03",time="",town="Plettenberg Bay",venue="Beacon Isle Resort",venue_address="Beacon Island Crescent, Plettenberg Bay",price_from="R180",ticket_url="https://www.howler.co.za/GLSBI3",source_url="https://www.howler.co.za/GLSBI3",source_name=H,alt_sources=[],notes="")
add(title="Get Lucky Summer Plett (Beacon Isle) – GoodLuck, Veranda Panda & Amy Tjasink (Edition 4)",category="concert",start_date="2027-01-10",time="",town="Plettenberg Bay",venue="Beacon Isle Resort",venue_address="Beacon Island Crescent, Plettenberg Bay",price_from="R180",ticket_url="https://www.howler.co.za/GLSBI4",source_url="https://www.howler.co.za/GLSBI4",source_name=H,alt_sources=["https://new-ux.howler.co.za/events/get-lucky-summer-plett-beacon-isle-goodluck-veranda-panda-amy-tjasink-edition-4-9d88"],notes="")
add(title="Plett NYE Festival – GoodLuck, The Parlotones, Booshle G & Saxby Twins (Get Lucky Summer NYE)",category="festival",start_date="2026-12-31",end_date="2027-01-01",time="Gates 17:00, music until 01:00",town="Plettenberg Bay",venue="Plett Rugby Club",price_from="R320",ticket_url="https://www.howler.co.za/GLSNYE26",source_url="https://www.howler.co.za/GLSNYE26",source_name=H,alt_sources=["https://www.plett-tourism.co.za/events/get-lucky-summer-nye-2026/"],notes="Under 18s must be accompanied by an adult.")
add(title="Get Lucky Summer Knysna – GoodLuck, The Parlotones, Booshle G, Veranda Panda & Lee Cole",category="concert",start_date="2026-12-29",time="15:00-21:30",town="Knysna",venue="Loerie Park Sports Grounds",venue_address="George Rex Drive, Knysna",price_from="R180",ticket_url="https://www.howler.co.za/glsknysna26",source_url="https://www.howler.co.za/events/get-lucky-summer-knsyna-ft-goodluck-the-parlotones-booshle-g-veranda-panda-lee-cole-72a0",source_name=H,alt_sources=["https://www.howler.co.za/glsknysna26"],notes="Kids U12 R180; family of 4 R280; early bird R300.")
add(title="Wanderbay NYE 2026 (Zakes Bantwini & more)",category="festival",start_date="2026-12-31",end_date="2027-01-01",time="17:00",town="Plettenberg Bay",venue="Cairnbrogie",venue_address="Plettenberg Bay Airport Road, Kranshoek, Plettenberg Bay",price_from="R575",ticket_url="https://www.howler.co.za/wanderbaynye2026",source_url="https://www.howler.co.za/wanderbaynye2026",source_name=H,alt_sources=["https://www.plett-tourism.co.za/events/wanderbay-nye-2026/","http://wanderbay.co.za/","https://festival101.co.za/events/wanderbay-nye-festival-2026-plettenberg-bay/"],notes="Electronic music (Afro house to disco), 18+.")
add(title="Wanderbay: Sexy Groovy Love showcase",category="festival",start_date="2026-12-28",time="",town="Plettenberg Bay",venue="Cairnbrogie",venue_address="Plettenberg Bay Airport Road, Kranshoek, Plettenberg Bay",price_from="",ticket_url="http://wanderbay.co.za/",source_url="http://wanderbay.co.za/",source_name="Wanderbay (official site)",alt_sources=[],notes="Season pass covers 28 Dec showcase and NYE.")
add(title="Wild Spirit Festival of Friends",category="festival",start_date="2026-12-28",end_date="2027-01-02",time="Gates 12:00-17:00 on 28 Dec",town="Nature's Valley",venue="Wild Spirit Lodge & Backpackers",venue_address="R102 Nature's Valley Road, The Crags",price_from="",ticket_url="https://www.wildspiritfestival.co.za/apply",source_url="https://www.wildspiritfestival.co.za/",source_name="Wild Spirit Festival (official site)",alt_sources=[OTR],notes="11th annual 5-day New Year camping festival: music, art, workshops. Line-up due Nov 2026.")

add(title="Bundu Bashers – psychedelic underground festival",category="festival",start_date="2026-12-30",end_date="2027-01-02",time="12:00 30 Dec – 19:00 2 Jan",town="Tsitsikamma",venue="Tannehof Guest farm",venue_address="Farm Rd, Bluelilliesbush, Tsitsikamma, 6308",price_from="R270",ticket_url="https://www.howler.co.za/BUNDUBASHERS",source_url="https://www.howler.co.za/BUNDUBASHERS",source_name="Howler",alt_sources=[],notes="Psytrance camping festival, 18+. Map pin is approximate (Tsitsikamma area, placed at Storms River).")

# ---------------- Markets & local finds (added 6 Oct 2026) ----------------
import datetime as _dt
def _dates(start,end,weekdays,skip=()):
    d=_dt.date.fromisoformat(start); e=_dt.date.fromisoformat(end); out=[]
    while d<=e:
        if d.weekday() in weekdays and d.isoformat() not in skip: out.append(d.isoformat())
        d+=_dt.timedelta(days=1)
    return out
SAT,WED,SUN=5,2,6
OEV="https://www.oev.co.za/wp-content/uploads/Night-Markets-Application-for-Stall-Space-December-2026-15.09.26.pdf"

occ=_dates("2026-10-10","2027-02-27",[SAT])
add(title="Wild Oats Community Farmers' Market",category="market",start_date=occ[0],end_date=occ[-1],occurrences=occ,recurrence="Every Saturday, 07:30-12:00 (summer hours)",
    time="07:30-12:00",town="Sedgefield",venue="Wild Oats Community Farmers' Market",venue_address="Western outskirts of Sedgefield, cnr N2 & Jan van Riebeeck St (at Swartvlei)",
    price_from="Free entry",ticket_url="",source_url="https://www.wildoatsmarket.co.za/",source_name="Wild Oats Market (official site)",
    alt_sources=["https://www.georgeherald.com/Whatson","https://www.toodoo.co.za/wild-oats-community-farmers-market/"],
    notes="Producer-only farmers' market since 1999: fresh produce, meats, cheeses, breads, breakfast. Open rain or shine; Facebook page confirms high-season hours.",
    lat=-34.009806,lng=22.778306,geo_source="event page")
occ=_dates("2026-10-10","2027-02-27",[SAT])
add(title="Sedgefield Mosaic Market",category="market",start_date=occ[0],end_date=occ[-1],occurrences=occ,recurrence="Every Saturday from 08:00",
    time="08:00",town="Sedgefield",venue="Mosaic Village & Outdoor Market",venue_address="1.5 km west of Sedgefield at the Engen petrol station, N2",
    price_from="Free entry",ticket_url="",source_url="https://www.toodoo.co.za/the-sedgefield-mosaic-market/",source_name="toodoo.co.za",
    alt_sources=["https://www.visitknysna.co.za/experiences/food-drink/discover-the-markets-of-the-greater-knysna-area/"],
    notes="Crafts, art, food stalls, coffee and live music next to Wild Oats. Pet friendly (on lead).")
occ=_dates("2026-10-10","2026-12-31",[SAT])
add(title="Harkerville Saturday Market",category="market",start_date=occ[0],end_date=occ[-1],occurrences=occ,recurrence="Every Saturday, 08:00-12:00",
    time="08:00-12:00",town="Plettenberg Bay",venue="Harkerville Saturday Market",venue_address="N2 between Plettenberg Bay and Knysna (Harkerville)",
    price_from="Free entry",ticket_url="",source_url="https://showme.co.za/plett/event/harkerville-saturday-market/",source_name="ShowMe Plettenberg Bay",
    alt_sources=["https://www.harkervillemarket.co.za/","https://www.visitknysna.co.za/experiences/food-drink/discover-the-markets-of-the-greater-knysna-area/"],
    notes="Weekly country market: artisan breads, farm produce, cheeses, crafts, breakfast. ShowMe lists Saturdays to 31 Dec 2026.")
occ=_dates("2026-10-07","2027-02-24",[WED])
add(title="The Wednesday Market at Old Nick Village",category="market",start_date=occ[0],end_date=occ[-1],occurrences=occ,recurrence="Every Wednesday, 09:00-14:00",
    time="09:00-14:00",town="Plettenberg Bay",venue="Old Nick Village",venue_address="N2, 3 km east of Plettenberg Bay",
    price_from="Free entry",ticket_url="",source_url="https://oldnickvillage.co.za/merchants/the-old-nick-midweek-market/",source_name="Old Nick Village (official site)",
    alt_sources=["https://showme.co.za/plett/event/mid-week-market-at-old-nick-village/"],
    notes="Farmers, bakers and artisans: organic produce, meat and dairy, breads, crafts.")
occ=_dates("2026-10-10","2027-02-27",[SAT])
add(title="Outeniqua Family Market",category="market",start_date=occ[0],end_date=occ[-1],occurrences=occ,recurrence="Every Saturday, 08:00-14:00",
    time="08:00-14:00",town="George",venue="Outeniqua Family Market",venue_address="Outeniqua Farm, N2 opposite Garden Route Mall, George",
    price_from="Free entry",ticket_url="",source_url="https://www.outeniquafamilymarket.co.za/",source_name="Outeniqua Family Market (official site)",
    alt_sources=["https://visitgeorge.co.za/directory/outeniqua-family-market/"],
    notes="130+ food and craft stalls, live entertainment, nursery and kids' play park. Car boot sale every first Saturday of the month.")
occ=["2026-10-10","2026-10-24","2026-11-07","2026-11-21","2026-12-05","2026-12-19"]
add(title="Saturday Market at Johnson's Post",category="market",start_date=occ[0],end_date=occ[-1],occurrences=occ,recurrence="Every second Saturday, 08:00-12:00",
    time="08:00-12:00",town="Mossel Bay",venue="Johnson's Post, Voelvlei",venue_address="Between Vleesbaai and Gouritsmond, Mossel Bay district",
    price_from="",ticket_url="",source_url=MB+"saturday-market-at-johnsons-post-2/2026-10-10/",source_name="Visit Mossel Bay (tourism calendar)",
    notes="Country market at a family store: coffee, cakes, pancakes, wors, gifts and shopping stalls. Map pin approximate (Mossel Bay).")
occ=["2026-10-14","2026-10-28"]
add(title="DanaBay Arts & Crafts Mini Market",category="market",start_date=occ[0],end_date=occ[-1],occurrences=occ,recurrence="14 & 28 October (Mossel Bay Arts Month)",
    time="09:00-16:00",town="Mossel Bay",venue="DanaBay Community Hall",venue_address="Distans Street, DanaBay, Mossel Bay",
    price_from="",ticket_url="",source_url=MB+"arts-craft-mini-market/2026-10-14/",source_name="Visit Mossel Bay (tourism calendar)",
    notes="Local artists' work for sale plus food vendors.")
occ=["2026-10-30","2026-10-31","2026-11-27","2026-11-28"]
add(title="Kaia Market Collective – Monthly Makers Market",category="market",start_date=occ[0],end_date=occ[-1],occurrences=occ,recurrence="Monthly (last Friday & Saturday): 30-31 Oct, 27-28 Nov",
    time="Fri 15:00-20:00",town="Mossel Bay",venue="Market Café",venue_address="8 Market Street, Mossel Bay",
    price_from="",ticket_url="",source_url=MB+"kaia-market-collective/",source_name="Visit Mossel Bay (tourism calendar)",
    alt_sources=[MB+"kaia-market-collective-2/",MB+"kaia-market-collective-3/",MB+"kiara-market-collective-2/"],
    notes="Local makers, artisanal products, fresh produce, live music and family fun.")
add(title="Hart van Harte Kersmark 2026 (Christmas Market)",category="market",start_date="2026-11-27",end_date="2027-01-02",time="09:00-17:00",
    town="Hartenbos",venue="Hart van Harte Kersmark",venue_address="Cnr Louis Fourie Rd & Kaap de Goede Hoop St, Hartenbos",
    price_from="",ticket_url="",source_url=MB+"hart-van-harte-kersmark-2026/",source_name="Visit Mossel Bay (tourism calendar)",
    notes="Festive seaside Christmas market: handmade gifts, local treasures, festive treats.")
add(title="Garden Route Festive Gift Market (Hartenbos)",category="market",start_date="2026-12-05",end_date="2027-01-03",time="09:00-18:00",
    town="Hartenbos",venue="Garden Route Gift Market",venue_address="Cnr Onderbos & Witteboom Streets, Hartenbos",
    price_from="",ticket_url="",source_url=MB+"garden-route-festive-market/",source_name="Visit Mossel Bay (tourism calendar)",
    notes="Holiday gift market for local products and brands during the December season.")
add(title="Mossel Bay Street Market (December night market)",category="market",start_date="2026-12-16",time="",town="Mossel Bay",
    venue="Marsh Street",venue_address="Marsh Street, Mossel Bay",price_from="",ticket_url="",source_url=OEV,source_name="Mossel Bay festive markets (stall application, oev.co.za)",
    notes="One of the municipal December night markets. Trading times not published on the source.")
add(title="Hartenbos Night Market 1",category="market",start_date="2026-12-18",time="",town="Hartenbos",
    venue="Joubert Park",venue_address="Joubert Park & Kaap de Goede Hoop Street, Hartenbos",price_from="",ticket_url="",source_url=OEV,source_name="Mossel Bay festive markets (stall application, oev.co.za)",
    alt_sources=["https://www.oev.co.za/wp-content/uploads/AANDMARKTE-Besprekingsaansoek-DESEMBER-2026.pdf"],
    notes="Hartenbos Aandmark: all of Joubert Park plus street stalls. Trading times not published on the source.")
add(title="The Goods Shed December Market",category="market",start_date="2026-12-19",time="",town="Mossel Bay",
    venue="The Goods Shed",venue_address="",price_from="",ticket_url="",source_url=OEV,source_name="Mossel Bay festive markets (stall application, oev.co.za)",
    notes="Listed with the December night markets. Trading times not published on the source.")
add(title="Hartenbos Night Market 2",category="market",start_date="2026-12-23",time="",town="Hartenbos",
    venue="Joubert Park",venue_address="Joubert Park & Kaap de Goede Hoop Street, Hartenbos",price_from="",ticket_url="",source_url=OEV,source_name="Mossel Bay festive markets (stall application, oev.co.za)",
    alt_sources=["https://www.oev.co.za/wp-content/uploads/AANDMARKTE-Besprekingsaansoek-DESEMBER-2026.pdf"],
    notes="Hartenbos Aandmark: all of Joubert Park plus street stalls. Trading times not published on the source.")
occ=_dates("2026-12-12","2027-01-02",[0,1,2,3,4,5],skip=("2026-12-25",))
add(title="Let's Love Local Gift Market at Redberry Farm",category="market",start_date="2026-12-12",end_date="2027-01-02",occurrences=occ,
    recurrence="Mon-Sat 09:00-16:00, 12 Dec 2026 - 2 Jan 2027 (closed Sundays & Christmas Day)",time="09:00-16:00",
    town="George",venue="Redberry Farm (marquee)",venue_address="Geelhoutboom Road, Blanco, George",price_from="",ticket_url="",
    source_url="https://letslovelocal.co.za/",source_name="Let's Love Local Gift Market (official site)",
    notes="One of SA's largest holiday markets: 220+ vendors of handmade SA gifts, decor and crafts, hosted by Boerevintage at Redberry Farm.")
occ=_dates("2026-12-05","2026-12-19",[0,1,2,3,4,5])
add(title="Outeniqua Kersmark 2026 (Christmas Market)",category="market",start_date="2026-12-05",end_date="2026-12-19",occurrences=occ,
    recurrence="Daily 09:00-18:00, 5-19 Dec (closed Sundays)",time="09:00-18:00",
    town="George",venue="NG Moedergemeente Kerksaal",venue_address="Courtenay Street, George",price_from="Free entry",ticket_url="",
    source_url="https://allevents.in/george/outeniqua-kersmark/200030596855013",source_name="AllEvents (Facebook-indexed event)",
    notes="One of the Garden Route's popular annual Christmas markets: handmade gifts, decorations, treats, jewellery and fashion.")
add(title="SPOILT Knysna Gift Fair 2026",category="market",start_date="2026-11-20",end_date="2026-11-21",time="Fri 09:00-18:00, Sat 09:00-16:00",
    town="Knysna",venue="Villa Castollini",venue_address="Brenton-on-Sea, Knysna",price_from="R50",ticket_url="https://www.quicket.co.za/events/375254-spoilt-knysna-gift-fair-2026/",
    source_url="https://www.visitknysna.co.za/whats-on/events/spoilt-knysna-gift-fair-2026/",source_name="Visit Knysna",
    notes="Summer gift fair: local brands, boutique fashion, festive gifts; coffee by Ile de Pain and ESCAPE Wine tastings. Kids under 12 free.")
add(title="Carpe Musicam! Magnificent Movie Music (George)",category="concert",start_date="2026-10-09",time="19:00",town="George",
    venue="Laerskool George-Suid",venue_address="",price_from="R180",ticket_url="https://carpemusicam.co.za/",
    source_url="https://www.georgeherald.com/Whatson",source_name="George Herald (What's On)",
    notes="Concert orchestra & choir play film music. Adults R180, scholars R60.")
import json as _json, os as _os
HER=_json.load(open(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)),"herald_data.json")))
_eo=HER["occ"]["Etensuurkonsert in Moederkerk"]
add(title="Etensuurkonserte: weekly lunch-hour concerts in the Moederkerk",category="concert",start_date=_eo[0],end_date=_eo[-1],occurrences=_eo,
    recurrence="Every Wednesday, 13:10 (about 50 minutes)",time="13:10",town="George",
    venue="NG Moedergemeente (Moederkerk)",venue_address="Courtenay Street, George",price_from="Free entry (donations welcome)",ticket_url="",
    source_url="https://www.georgeherald.com/Whatson",source_name="George Herald (What's On)",
    notes="Weekly lunch-hour concert series. The spring season opens on 7 Oct with organist Gerrit Jordaan and the NG Kerk Hartenbos choir (cond. Marianne Rust). Dates as listed in the George Herald diary.",
    _img=HER["img"]["Etensuurkonserte lente reeks skop af"])

# ---------------- Fun runs & walks (added 6 Oct 2026) ----------------
add(title="MossMarch 2026 – community walk",category="funrun",start_date="2026-10-10",time="Registration from 07:00",town="Hartenbos",
    venue="Hartenbos Seefront",venue_address="156 Paardekraal Ave, Hartenbos",price_from="Free (bring a food/sock donation)",ticket_url="",
    source_url=MB+"moss-march-2026/",source_name="Visit Mossel Bay (tourism calendar)",
    notes="Walk with purpose, part of the Mossel Bay Sport and Recreation Festival; open to all. Donations of non-perishable food and socks instead of an entry fee.")
add(title="Redberry Farm Trail Run (5 km / 9 km) for Up with Down's",category="funrun",start_date="2026-10-17",time="Entry from 07:15, start 08:00",town="George",
    venue="Redberry Farm",venue_address="Geelhoutboom Road, Blanco, George",price_from="R30",ticket_url="",
    source_url="https://www.redberryfarm.co.za/whats-on/",source_name="Redberry Farm (official site)",
    notes="Fun trail run through strawberry and kiwi fields; not timed or accredited. 5 km R30, 9 km R50, entry on the day. No dogs.")
add(title="Eden Meander 10 km / 5 km Fun Run & Walk",category="funrun",start_date="2026-10-24",time="07:00",town="George",
    venue="Eden Meander Shopping Centre",venue_address="Eden Meander, George",price_from="R125",ticket_url="",
    source_url="https://www.toodoo.co.za/eden-meander-fun-run-walk-2026/",source_name="toodoo.co.za",
    notes="Fun run/walk in support of Carpe Diem School; entries via Entry Ninja.")
add(title="Firefly Night Run by Gracehill College (10 / 5 / 3 km)",category="funrun",start_date="2026-10-30",time="Evening",town="George",
    venue="Garden Route Botanical Garden – Lapa",venue_address="49 Caledon St, Campher's Drift, George",price_from="R50",ticket_url="https://www.entryninja.com/events/84531-firefly-night-run",
    source_url="https://www.entryninja.com/events/84531-firefly-night-run",source_name="Entry Ninja",
    notes="Family trail run/walk raising funds for a school bus; picnic in the gardens afterwards. 3 km run/walk from R50, 5 km R60-R80, 10 km R120.")
add(title="Steps of Courage Walk (4.1 km)",category="funrun",start_date="2026-10-31",time="08:00 (registration from 06:30)",town="Mossel Bay",
    venue="Milkwood Primary School grounds",venue_address="Muir Street, Mossel Bay",price_from="R50",ticket_url="",
    source_url=MB+"steps-of-courage-walk/",source_name="Visit Mossel Bay (tourism calendar)",
    notes="Relaxed, non-competitive community wellness walk; wear blue and pink. Children under 12 free.")
add(title="Rave Run 4 km with a live DJ (Gobi Hybrid Games)",category="funrun",start_date="2026-10-31",time="08:00",town="George",
    venue="Deja Vu Equestrian",venue_address="",price_from="R100",ticket_url="",
    source_url="https://www.toodoo.co.za/rave-run-4km-gobi-hybrid-games-george/",source_name="toodoo.co.za",
    alt_sources=["https://visitgeorge.co.za/events/"],
    notes="Run, walk and dance 4 km with a live DJ, part of the Gobi Hybrid Games; for runners, walkers and families.")
add(title="Knysna Waterfront Half Marathon & 5 km Fun Run",category="funrun",start_date="2026-11-14",time="21.1 km 07:00; 10 km & 5 km 07:15",town="Knysna",
    venue="Knysna Waterfront",venue_address="21 Waterfront Dr, Knysna",price_from="R65",ticket_url="https://www.entryninja.com/events/84135",
    source_url="https://www.entryninja.com/events/84135",source_name="Entry Ninja",
    alt_sources=["https://www.visitknysna.co.za/whats-on/events/waterfront-half-marathon/"],
    notes="Scenic road race with a 5 km fun run for friends and family (no temp licence needed); 10 km R125, 21.1 km R145.")
add(title="KMC Nite Race (10 km & 5 km fun run/walk)",category="funrun",start_date="2026-12-16",time="18:00",town="Knysna",
    venue="Knysna Marathon Club House, Loerie Park",venue_address="George Rex Drive, Knysna",price_from="R65",ticket_url="",
    source_url="https://runningcalendar.co.za/events/knysna-nite-race",source_name="RunningCalendar.co.za",
    alt_sources=["https://www.racespace.co.za/race/7237-kmc-nite-race"],
    notes="Festive-season evening race by Knysna Marathon Club; 5 km fun run/walk R65, 10 km R125. Entries via Entry Ninja.")
add(title="Monties Cycles MTB & Trail Run Challenge (incl. 6 km fun walk/run)",category="funrun",start_date="2026-12-26",time="Registration 05:00-06:30",town="Mossel Bay",
    venue="Misty Valley Farm (Laminin Agora venue)",venue_address="Erf 151, Outeniquabosch, Brandwacht, Hartenbos",price_from="R70",ticket_url="https://www.entryninja.com/events/83037",
    source_url="https://www.entryninja.com/events/83037",source_name="Entry Ninja",
    alt_sources=["https://startingline.co.za/events/monties-cycles-mtb-trail-run-challenge-a466e7dc"],
    notes="Post-Christmas family outing: 6 km fun walk/run (R70), 12 km trail run, MTB and gravel routes; deli, gin tasting and kids' play area.")
add(title="Sabrina Love Summer Challenge 2026 (beach walk & more)",category="funrun",start_date="2026-12-27",end_date="2026-12-30",time="06:00-11:00",town="Plettenberg Bay",
    venue="Central Beach & Kurland Estate",venue_address="Central Beach, Plettenberg Bay; Kurland Estate, The Crags",price_from="R150",ticket_url="",
    source_url="https://www.plett-tourism.co.za/events/sabrina-love-summer-challenge-2026/",source_name="Plett Tourism",
    alt_sources=["https://startingline.co.za/events/sabrina-love-foundation-beach-walk-surf-ski-challenge-48df92f5"],
    notes="Fun, inclusive family challenge (beach walk, trail running, MTB, swimming, paddling) raising funds for children in need. Adults R200, children R150.")
add(title="Groot Brak Grabadoo 2026 (MTB & 4.8 km fun walk)",category="funrun",start_date="2026-12-31",time="07:00-14:00",town="Groot Brak",
    venue="Groot Brak sport fields",venue_address="67 Long Street, Great Brak River",price_from="",ticket_url="",
    source_url=MB+"groot-brak-grabadoo-2026/",source_name="Visit Mossel Bay (tourism calendar)",
    notes="Iconic New Year's Eve cycling & walking event: four MTB routes or a scenic 4.8 km fun walk, plus a family fun day.")
add(title="Plett Games 2026",category="festival",start_date="2026-10-17",time="10:00-17:00",town="Plettenberg Bay",
    venue="Greenwood Bay College",venue_address="",price_from="R30",ticket_url="",
    source_url="https://www.plett-tourism.co.za/events/plett-games/",source_name="Plett Tourism",
    notes="Family-friendly team challenge festival with live music by the Bitou River Band, beer garden and kids' areas.")

# ---------------- Hope Church (Hope Family) George (added 6 Oct 2026) ----------------
HOPE="https://hopefamily.org/event/"
HOPE_VEN=dict(town="George",venue="Hope Church (Hope Family)",venue_address="Cnr Knysna Road & Fourth Street, Eastern Extension, George")
add(title="Hope Family Christmas Show",category="community",start_date="2026-12-06",time="",price_from="",ticket_url="",source_url=HOPE,source_name="Hope Family / Hope Church George (official site)",
    notes="Hope Church George's annual Christmas Show (Sunday). Times and details to be announced on the church's events page.",**HOPE_VEN)
add(title="Hope Family New Year's Eve Event",category="community",start_date="2026-12-31",time="",price_from="",ticket_url="",source_url=HOPE,source_name="Hope Family / Hope Church George (official site)",
    notes="New Year's Eve gathering at Hope Church George. Details to be announced on the church's events page.",**HOPE_VEN)
add(title="Hope Youth Summer Camp (Grade 7-12)",category="community",start_date="2027-01-06",end_date="2027-01-09",time="",price_from="",ticket_url="",source_url=HOPE,source_name="Hope Family / Hope Church George (official site)",
    notes="Summer camp for high-school youth (Grade 7-12) run by Hope Family George. Venue not published yet; pinned at the church.",**HOPE_VEN)
add(title="Hope Family Night Run 2027 (10 km forest run, 5 km & 3 km fun run/walk)",category="funrun",start_date="2027-01-22",time="18:30 (expected)",town="George",
    venue="Nelson Mandela University George Campus (expected)",venue_address="Madiba Rd, George",price_from="",ticket_url="",source_url=HOPE,source_name="Hope Family / Hope Church George (official site)",
    alt_sources=["https://runningcalendar.co.za/events/hope-church-night-trail-run","https://hopefamily.org/night-run/"],
    notes="Hope Church George's annual family night run. The church's events page lists Friday 22 January 2027. Venue and 18:30 start are RunningCalendar's estimate from the 2026 edition (NMU George; 10 km forest run with torches, 5 km fun forest run/walk, 3 km road run/walk for prams and small kids; food stalls, music, medals). Not yet confirmed.",
    lat=-33.960929,lng=22.534765,geo_source="event page")

# ---- club runs with a short social distance (RunningCalendar, verified listings) ----
RC="RunningCalendar.co.za"
add(title="Oujaarsdraffie New Year's Eve run (10 km & 4 km)",category="funrun",start_date="2026-12-31",time="06:00",town="Hartenbos",venue="ATKV Amphitheatre",venue_address="Hartenbos",
    price_from="R65 (4 km)",ticket_url="",source_url="https://runningcalendar.co.za/events/oujaarsdraffie",source_name=RC,
    notes="New Year's Eve morning 'draffie' (jog) in Hartenbos with a 4 km option alongside the 10 km. Listing verified by RunningCalendar; online entries open. The organiser doesn't label the 4 km a fun run.",
    lat=-34.122212,lng=22.117421,geo_source="event page")
add(title="Love Life Run, Wilderness (10 km & 5 km)",category="funrun",start_date="2026-11-04",time="18:00",town="Wilderness",venue="The Wilderness Common",venue_address="Wilderness",
    price_from="R40 (5 km)",ticket_url="",source_url="https://runningcalendar.co.za/events/love-life-run",source_name=RC,
    notes="Wednesday-evening community run in Wilderness with a 5 km option (R40). Listing verified by RunningCalendar; online entries open.",
    lat=-33.994418,lng=22.601261,geo_source="event page")
add(title="Moordkuil Race, Friemersheim (15 km & 4 km)",category="funrun",start_date="2026-12-19",time="06:30",town="Groot Brak",venue="Friemersheim Church",venue_address="Friemersheim (above Groot Brak River)",
    price_from="R35 (4 km)",ticket_url="",source_url="https://runningcalendar.co.za/events/moordkuil-race",source_name=RC,
    notes="Rural country-road race from Friemersheim church with a short 4 km option (R35). Listing verified by RunningCalendar.",
    lat=-33.952228,lng=22.143106,geo_source="event page")

# ---------------- Fancourt / Kingswood / George trail runs (added 6 Oct 2026) ----------------
add(title="Wild Mongoo Fashion Show (ladies' charity evening)",category="community",start_date="2026-12-02",time="18:30 for 19:00",town="George",venue="Fancourt",
    venue_address="Montagu St, Blanco, George",price_from="R350",ticket_url="https://www.quicket.co.za/events/397238-wild-mongoo-fashion-show/",
    source_url="https://www.quicket.co.za/events/397238-wild-mongoo-fashion-show/",source_name="Quicket",
    notes="Ladies' night at Fancourt with live entertainment by local singer Shaza, welcome drinks, goodie bags and a fashion show (Wild Mongoo apparel & Sam's Clothing). 100% of funds go to Wild Mongoo (anti-human-trafficking). Group discount for 10+.",
    lat=-33.9558525,lng=22.4142456,geo_source="event page",_img="https://images.quicket.co.za/0995293_0.png")
KW="https://www.estate-living.co.za/news/the-big-one-celebrating-our-community-centres-first-birthday/"
add(title="Kingswood Spring Fun Run/Walk for PDSA George",category="funrun",start_date="2026-10-10",time="08:00",town="George",venue="Kingswood Golf Estate",
    venue_address="Plattner Boulevard, George",price_from="",ticket_url="",source_url=KW,source_name="Kingswood BUZZard (Estate Living)",
    notes="First Kingswood Spring Fun Run/Walk, raising funds for PDSA George. Dress in spring colours/florals (best-dressed prize); kids welcome, one dog on a leash per person. Announced in the estate's homeowners' newsletter, so check with Kingswood whether non-residents can join.")
add(title="Kingswood Carols by Candlelight with Carpe Musicam",category="concert",start_date="2026-12-04",time="",town="George",venue="Kingswood Golf Estate (lawn in front of the Community Centre)",
    venue_address="Plattner Boulevard, George",price_from="",ticket_url="",source_url=KW,source_name="Kingswood BUZZard (Estate Living)",
    notes="Picnic-blanket carols evening with Carpe Musicam leading the singing. Announced in the estate's homeowners' newsletter, so check with Kingswood whether non-residents can attend.")
GT="GoTrail (trail running calendar)"
add(title="Montagu Pass Run (17 km, 10 km & 5 km trail)",category="funrun",start_date="2026-10-24",time="",town="George",venue="Herold (Montagu Pass)",venue_address="Herold, Montagu Pass, George",
    price_from="R80",ticket_url="",source_url="https://gotrail.run/en/event/montagu-pass-run",source_name=GT,alt_sources=["https://runningcalendar.co.za/races/city/george"],
    notes="Trail run on the historic Montagu Pass above George, with a 5 km option alongside the 10 km and 17 km. Entry from R80 (RunningCalendar). Map pin approximate.")
add(title="Run The Farm, Herold Wines (12-hour 5 km-loop challenge + 5 km fun run/walk)",category="funrun",start_date="2026-11-07",time="",town="George",venue="Herold Wines",venue_address="Herold, Montagu Pass, George",
    price_from="",ticket_url="",source_url="https://gotrail.run/en/event/run-the-farm-herold",source_name=GT,
    notes="12-hour trail endurance event on a 5 km mountain loop (individuals and teams of 2 or 4), plus a 5 km fun run/walk. Natural pool, vendor stalls and space for gazebos.")
add(title="Bergplaas Challenge (10 km & 7 km trail)",category="funrun",start_date="2026-11-28",time="",town="Wilderness",venue="Bergplaas, Wilderness",venue_address="",
    price_from="",ticket_url="",source_url="https://gotrail.run/en/event/bergplaas-challenge",source_name=GT,
    notes="Short trail run in the forest/mountain area above Wilderness with 7 km and 10 km options. Map pin approximate (Wilderness).")
add(title="Trail Girl Wilderness (2-day women's trail running tour)",category="funrun",start_date="2026-11-20",end_date="2026-11-22",time="Registration Fri 17:00",town="Wilderness",
    venue="Fairy Knowe Hotel",venue_address="Dumbleton Road, Wilderness",price_from="R5,800 pp sharing (incl. 2 nights & meals)",ticket_url="",
    source_url="https://trailgirl.co.za/tr-3-3-2/",source_name="Trail Girl (official site)",
    notes="Non-race trail running tour: day 1 15 km, day 2 16 km on SANParks/CapeNature trails, plus a sunset beach walk and Touw River canoeing. Limited to 50 entries; entries via Entry Ninja.")
add(title="Red Men Trail Run, Herold Wine Farm (18 km, 12 km & 5 km fun run)",category="funrun",start_date="2027-01-03",time="07:00 (5 km fun run 07:15)",town="George",venue="Herold Wines",venue_address="Herold, Montagu Pass, George",
    price_from="R120 (5 km)",ticket_url="",source_url="https://startingline.co.za/events/red-men-trail-run-2027-sun-3-jan-2027-george-municipality-western-cape-b44c4c0d",source_name="Starting Line",
    alt_sources=["https://gotrail.run/en/event/red-men-trail-run"],
    notes="Morning trail run in the Outeniqua Mountains followed by a picnic and wine tasting. 5 km fun run R120 (medal); 12 km and 18 km R450 (incl. custom-label Herold wine). Limited to 200 entries; picnic meals bookable.")

# ---------------- George Herald What's On diary (added 6 Oct 2026) ----------------
GH="https://www.georgeherald.com/Whatson"; GHN="George Herald (What's On)"
add(title="Grootbrak Leeskring: Morné Malan in conversation with Gerda Taljaard (Die grafdigter)",category="arts",start_date="2026-10-08",time="09:15 for 10:00",town="Groot Brak",
    venue="NG Kerk Groot-Brakrivier (church hall)",venue_address="Groot-Brakrivier",price_from="R100 members / R120 non-members",ticket_url="",source_url=GH,source_name=GHN,
    notes="Book club talk (Afrikaans): author Gerda Taljaard on her book Die grafdigter. Coffee and tea included. Enquiries: Etty Bosman 083 501 0845.",_img=HER["img"]["Grootbrak Leeskring"])
_o=HER["occ"]["Midbrak-mark"]
add(title="Midbrak-mark (Saturday market)",category="market",start_date=_o[0],end_date=_o[-1],occurrences=_o,recurrence="Every Saturday, 09:00-13:00",time="09:00-13:00",town="Groot Brak",
    venue="OpiSpoor Pub & Grill",venue_address="Groot-Brakrivier station",price_from="",ticket_url="",source_url=GH,source_name=GHN,
    notes="Weekly Saturday market at OpiSpoor Pub & Grill by the Great Brak River station.",_img=HER["img"]["Midbrak-mark"])
_o=HER["occ"]["Brinkleys-mark"]
add(title="Brinkleys-mark (Saturday market)",category="market",start_date=_o[0],end_date=_o[-1],occurrences=_o,recurrence="Every Saturday, 09:00-14:00",time="09:00-14:00",town="Klein Brak",
    venue="Brinkleys River Village",venue_address="Klein-Brakrivier",price_from="",ticket_url="",source_url=GH,source_name=GHN,
    notes="40+ stalls with fresh produce, handmade items, food and coffee every Saturday.",_img=HER["img"]["Brinkleys-mark"])
_o=HER["occ"]["Show Ground Sunday"]
add(title="Show Ground Sunday (market)",category="market",start_date=_o[0],end_date=_o[-1],occurrences=_o,recurrence="Every 2nd Sunday, 09:00-14:00",time="09:00-14:00",town="George",
    venue="George Show Ground",venue_address="R102 Airport Road, George",price_from="Free entry",ticket_url="",source_url=GH,source_name=GHN,
    notes="Local stalls, food and family fun; kids and dogs welcome. Fortnightly on Sundays (dates as listed in the Herald diary). Info: Etienne 061 044 1993.",_img=HER["img"]["Show Ground Sunday"])
add(title="Mossel Bay Mayor's Breakfast (October) with Dr Ivan Meyer",category="community",start_date="2026-10-15",time="08:30-11:00",town="Mossel Bay",
    venue="Mossel Bay Golf Club",venue_address="Mossel Bay Golf Club, Mossel Bay",price_from="",ticket_url="",source_url=GH,source_name=GHN,
    notes="Monthly mayoral breakfast; guest speaker is Western Cape Minister of Agriculture, Economic Development and Tourism Dr Ivan Meyer. Bookings: Aydn Parrott 079 149 4703 (WhatsApp) or mayoroffice@mosselbay.gov.za.",_img=HER["img"]["Oktober-burgemeestersontbyt"])
add(title="Posboom Philatelic Society 60th anniversary inter-club stamp exhibition",category="arts",start_date="2026-10-16",time="Public viewing 14:00-16:00",town="Mossel Bay",
    venue="Granary Hall, Bartolomeu Dias Museum",venue_address="Bartolomeu Dias Museum Complex, Market Street, Mossel Bay",price_from="Free",ticket_url="",source_url=GH,source_name=GHN,
    notes="Stamp clubs from Mossel Bay, George and Stilbaai meet (10:00-12:30); the exhibits are open to the public free of charge from 14:00 to 16:00.",_img=HER["img"]["Posboom-filatelistevereniging interklubbyeenkoms"])
add(title="Klein Karoo Dust 4 Glory Challenge (family obstacle & trail event)",category="funrun",start_date="2026-10-17",time="06:00",town="Oudtshoorn",
    venue="Wilgewandel Holiday Farm",venue_address="Wilgewandel Holiday Farm, Schoemanshoek, Oudtshoorn",price_from="",ticket_url="",source_url=GH,source_name=GHN,
    notes="Fitness challenge with a choice of distances, trail running routes and safe obstacle courses for kids and families; on-site catering. Entries via Entry Ninja (limited).",_img=HER["img"]["Join the Klein Karoo Dust 4 Glory Challenge at Wilgewandel!"])
add(title="Espectáculo: Marlise's School of Spanish Dance",category="arts",start_date="2026-10-17",time="18:30",town="George",
    venue="Market Community Theatre",venue_address="Market Community Theatre, George",price_from="R150",ticket_url="https://www.webtickets.co.za/v2/event.aspx?itemid=1598588884",
    source_url="https://www.webtickets.co.za/v2/event.aspx?itemid=1598588884",source_name="Webtickets",alt_sources=[GH],
    notes="An evening of colourful Spanish (flamenco) dance by Marlise's School of Spanish Dance.",lat=-33.9777839,lng=22.495311,geo_source="event page")
# Skipped: "Motion Art Academy: In The Beginning" (Herald lists 17 Oct 2026, but its poster reads 17-18 October 2025 with 2025 weekdays and
# the Herald ran the same item in Oct 2025, so it looks like a recycled listing; no 2026 confirmation found).
add(title="Oppi Pot: comedy with Johnnie Campher",category="arts",start_date="2026-10-18",time="18:00",town="Mossel Bay",
    venue="Mossel Bay Town Hall",venue_address="Marsh Street, Mossel Bay",price_from="",ticket_url="",source_url=GH,source_name=GHN,
    notes="Comedian Johnnie Campher's new show. Tickets on Webtickets or at Pick n Pay stores. Enquiries: 082 375 1910.",_img=HER["img"]["Oppi Pot with Johnnie Campher"])
add(title="Schalk Bezuidenhout: Hey Hey Divorcé (stand-up comedy)",category="arts",start_date="2026-10-21",end_date="2026-10-23",time="19:00",town="George",
    venue="George Arts Theatre",venue_address="125 York Street, George",price_from="R250",ticket_url="https://www.quicket.co.za/events/375531-hey-hey-divorc-21-23-october/",
    source_url="https://www.quicket.co.za/events/375531-hey-hey-divorc-21-23-october/",source_name="Quicket",alt_sources=[GH],
    notes="Raw, real stand-up about divorce. No under-16s.",lat=-33.9560661,lng=22.4579849,geo_source="event page",_img="https://images.quicket.co.za/0921787_0.jpeg")
add(title="Schalk Bezuidenhout: Hey Hey Divorcé at Fancourt (stand-up comedy)",category="arts",start_date="2026-10-19",time="19:00-21:00",town="George",
    venue="The Ballroom at Fancourt",venue_address="Montagu St, Blanco, George",price_from="",ticket_url="https://www.quicket.co.za/events/398647-schalk-bezuidenhout/",
    source_url="https://www.quicket.co.za/events/398647-schalk-bezuidenhout/",source_name="Quicket",alt_sources=["https://www.quicket.co.za/events/398017-hey-hey-divorc/","https://fancourt.co.za/events1/schalk-bezuidenhout/"],
    notes="An evening of comedy with a little Fancourt flair: Schalk brings Hey Hey Divorcé to the Fancourt Ballroom.",lat=-33.9558525,lng=22.4142456,geo_source="event page",_img="https://images.quicket.co.za/0991309_0.jpeg")
add(title="Herbertsdale Oktoberfees",category="festival",start_date="2026-10-24",time="From 09:00",town="Herbertsdale",
    venue="Athlone Plaas",venue_address="Athlone farm, Herbertsdale",price_from="",ticket_url="",source_url=GH,source_name=GHN,
    notes="NG Kerk Herbertsdale's annual October fete on Athlone farm: local meat, vegetables and fruit, potjies, puddings and roosterkoek. Enquiries: Jan Labuschagne 082 555 1466.",_img=HER["img"]["Herbertsdale Oktoberfees"])
add(title="Eerste vir Alles: Frank Opperman & Margit Meyer-Rödenbeck (Afrikaans comedy play)",category="arts",start_date="2026-10-24",end_date="2026-10-25",time="19:00",town="George",
    venue="George Arts Theatre",venue_address="125 York Street, George",price_from="R250",ticket_url="https://www.webtickets.co.za/v2/event.aspx?itemid=1601879662",
    source_url="https://www.webtickets.co.za/v2/event.aspx?itemid=1601879662",source_name="Webtickets",alt_sources=[GH],
    notes="Romantic comedy play: two of SA's best storytellers play the original 'power couple' in a classic case of he said, she said.",lat=-33.9560661,lng=22.457985,geo_source="event page",_img=HER["img"]["Eerste vir alles met Frank Opperman en Margit Meyer-Rödenbeck"])

# ---- NSRI (National Sea Rescue Institute) fundraiser runs ----
add(title="Stilbaai NSRI 10 km & 6 km Fun Run (New Year's Eve)",category="funrun",start_date="2026-12-31",time="07:00",town="Stilbaai",
    venue="NSRI Station, Main Road",venue_address="National Sea Rescue Institute, Main Rd, Stilbaai",price_from="",ticket_url="",
    source_url="https://runningcalendar.co.za/events/stilbaai-10km/2026",source_name=RC,alt_sources=["https://racepass.com/za/races/stillbaai-10km"],
    notes="Annual New Year's Eve run in aid of NSRI Stilbaai: 10 km race and 6 km fun run/walk, start and finish at the NSRI building. The route runs along the Goukou River, the sea and dunes. The 2025 edition drew about 1,200 runners. RunningCalendar lists only basic details so far; entry fees are still to be confirmed.",
    lat=-34.3642194,lng=21.4335508,geo_source="event page")

# ---- restaurant listings (approved by Christopher, 6 Oct 2026) ----
import datetime as _dt
def _weekly(wds,start="2026-10-06",end="2027-02-28"):
    d=_dt.date.fromisoformat(start);e=_dt.date.fromisoformat(end);out=[]
    while d<=e:
        if d.weekday() in wds: out.append(d.isoformat())
        d+=_dt.timedelta(days=1)
    return out
add(title="Vinyl Krispies: Bassline Society rooftop vinyl session at Pili Pili",category="concert",start_date="2026-11-28",time="12:00-21:00",town="Sedgefield",
    venue="Pili Pili Sedgefield (rooftop)",venue_address="2 Claude Urban Drive, Myoli Beach, Sedgefield",price_from="R100",ticket_url="",
    source_url="https://www.toodoo.co.za/vinyl-krispies-sedgefield/",source_name="toodoo.co.za",
    notes="Afternoon of house music and vinyl culture on the Pili Pili rooftop: classic records (vinyl only), cold drinks and ocean views. Entry R100.",lat=-34.0348895,lng=22.8068601,geo_source="nominatim")
_tw=_weekly({2,4})
add(title="Live entertainment at Tapas & Oysters (Wednesday & Friday evenings)",category="concert",start_date=_tw[0],end_date=_tw[-1],occurrences=_tw,
    recurrence="Every Wednesday and Friday evening",time="Evenings",town="Knysna",venue="Tapas & Oysters, Thesen Island",venue_address="TH 29, Thesen Island, Knysna",
    price_from="",ticket_url="",source_url="https://tapasknysna.co.za/contact/",source_name="Tapas & Oysters (official site)",
    notes="The restaurant advertises live entertainment on Wednesday and Friday evenings. No artists or start times are listed; dates here are the weekly pattern within the window, so check with the restaurant (044 382 7196) before going.",
    lat=-34.048978,lng=23.048194,geo_source="event page")
_hn=_weekly({1});_hq=_weekly({3})
add(title="Noot vir Noot music quiz night at Hennie's George (Tuesdays)",category="quiz",start_date=_hn[0],end_date=_hn[-1],occurrences=_hn,
    recurrence="Every Tuesday, 19:00",time="19:00",town="George",venue="Hennie's George",venue_address="42 York Street, George",
    price_from="",ticket_url="",source_url="https://www.therealhennies.co.za/branches/hennies-george",source_name="Hennie's George (official branch page)",
    notes="Afrikaans music quiz night in the style of the TV show; prizes to be won, free entry (first come, first served). Hennie's October 2026 What's On poster says 'Every Tuesday 19:00'; dates after October follow that weekly pattern and are not yet confirmed. Enquiries: 062 579 8350.",alt_sources=["https://www.therealhennies.co.za/img/posters/whatson-oct-2026/george.jpg"],_img="https://www.therealhennies.co.za/img/posters/whatson-oct-2026/george.jpg",
    lat=-33.9658718,lng=22.4512367,geo_source="nominatim")
add(title="Quiz Night at Hennie's George (Thursdays)",category="quiz",start_date=_hq[0],end_date=_hq[-1],occurrences=_hq,
    recurrence="Every Thursday, 19:00",time="19:00",town="George",venue="Hennie's George",venue_address="42 York Street, George",
    price_from="",ticket_url="",source_url="https://www.therealhennies.co.za/branches/hennies-george",source_name="Hennie's George (official branch page)",
    notes="Pub quiz night; prizes to be won, free entry (first come, first served). Hennie's October 2026 What's On poster says 'Every Thursday 19:00'; dates after October follow that weekly pattern and are not yet confirmed. Enquiries: 062 579 8350.",alt_sources=["https://www.therealhennies.co.za/img/posters/whatson-oct-2026/george.jpg"],_img="https://www.therealhennies.co.za/img/posters/whatson-oct-2026/george.jpg",
    lat=-33.9658718,lng=22.4512367,geo_source="nominatim")

for _t,_d,_tm in [("John Masser live at Hennie's George","2026-10-17","18:00"),("Landman live at Hennie's George","2026-10-30","19:00")]:
    add(title=_t,category="concert",start_date=_d,time=_tm,town="George",venue="Hennie's George",venue_address="42 York Street, George",
        price_from="Free",ticket_url="",source_url="https://www.therealhennies.co.za/img/posters/whatson-oct-2026/george.jpg",source_name="Hennie's George (October 2026 What's On poster)",
        alt_sources=["https://www.therealhennies.co.za/branches/hennies-george"],
        notes="Live music at Hennie's George. Free entry, first come, first served (per the branch's October 2026 What's On poster).",
        lat=-33.9658718,lng=22.4512367,geo_source="nominatim",_img="https://www.therealhennies.co.za/img/posters/whatson-oct-2026/george.jpg")
_hk=_weekly({2})
add(title="Donkiekar Boere Orkes live at Hoeka Toeka Pub & Diner (Wednesdays)",category="concert",start_date=_hk[0],end_date=_hk[-1],occurrences=_hk,
    recurrence="Every Wednesday, 18:00-21:00",time="18:00-21:00",town="Hoekwil",venue="Hoeka Toeka Pub & Diner",venue_address="48 Church Road, Hoekwil",
    price_from="",ticket_url="",source_url="https://www.foodyas.com/ZA/Hoekwil/837657939628374/Hoeka-Toeka-Pub-%26-Diner",source_name="Hoeka Toeka Pub & Diner (Facebook posts, via Foodyas)",
    notes="Boere-orkes night with the Donkiekar Boere Orkes, fire and comfort food. The pub's Facebook posts (Aug-Sep 2026) say 'every Wednesday from 6 to 9'; later dates follow that pattern and aren't individually confirmed. Bookings essential: 079 917 2222.")

# ---- Quiz nights (added 2026-10-06) ----
def _nth(wd,nths,start="2026-10-06",end="2027-02-28"):
    """dates in window that are the n-th (1..5) or last (-1) given weekday of their month"""
    out=[]
    for d in _weekly({wd},start,end):
        x=_dt.date.fromisoformat(d); n=(x.day-1)//7+1; last=(x+_dt.timedelta(days=7)).month!=x.month
        if n in nths or (-1 in nths and last): out.append(d)
    return out
_HP="https://www.therealhennies.co.za/img/posters/whatson-oct-2026/%s.jpg"
_HB="https://www.therealhennies.co.za/branches/hennies-%s"
for _slug,_town,_name,_addr,_wd,_wdn,_ph,_price,_ll in [
    ("hartenbos","Hartenbos","Hennie's Hartenbos","156 Paardekraal Avenue, Hartenbos, Mossel Bay",2,"Wednesday","044 868 0677","Free",None),
    ("oudtshoorn","Oudtshoorn","Hennie's Oudtshoorn","114 Baron van Rheede Street, Oudtshoorn",3,"Thursday","078 884 7268","Free",None),
    ("durbanville","Cape Town","Hennie's Durbanville","7B Pampoenkraal Lane, Durbanville, Cape Town",1,"Tuesday","066 374 5732","Free",(-33.8327892,18.6479816,"nominatim (street)")),
    ("brackenfell","Cape Town","Hennie's Brackenfell","Shop 57, Brackenfell Shopping Centre, Old Paarl Road, Brackenfell, Cape Town",1,"Tuesday","068 924 7654","R30",(-33.8674704,18.7062255,"nominatim (street, approximate)")),
    ]:
    _d=_weekly({_wd})
    _free="free entry, first come, first served" if _price=="Free" else "tickets R30"
    add(title="Quiz Night at %s (%ss)"%(_name,_wdn),category="quiz",start_date=_d[0],end_date=_d[-1],occurrences=_d,
        recurrence="Every %s, 19:00"%_wdn,time="19:00",town=_town,venue=_name,venue_address=_addr,price_from=_price,ticket_url="",
        source_url=_HB%_slug,source_name="%s (official branch page)"%_name,alt_sources=[_HP%_slug],_img=_HP%_slug,
        notes="Pub quiz night with prizes to be won; %s. The branch's October 2026 What's On poster says 'Every %s 19:00' and the branch page lists the next quiz; dates after October follow that weekly pattern and are not yet confirmed. Enquiries: %s."%(_free,_wdn,_ph),
        **({"lat":_ll[0],"lng":_ll[1],"geo_source":_ll[2]} if _ll else {}))
_GRT="https://www.knysna.n2rs.com/knysna-diary-october.html"
_GRN=("Garden Route Trivia League team quiz run by Craft Quiz Nights: suitable for all ages, teams of 4 to 6 ideal (no minimum or maximum), prizes sponsored by the venue and Craft Quiz Nights. "
      "Listed in the Knysna Diary for October 2026 as '%s'; later dates follow that pattern and aren't individually confirmed. No start time published; contact 082 335 9406.")
for _t,_town,_ven,_addr,_dates,_rec,_ll in [
    ("Garden Route Trivia League quiz at Goose Valley Golf Club (Tuesdays)","Plettenberg Bay","Goose Valley Golf Club","Goose Valley Golf Club, Plettenberg Bay",_weekly({1}),"Tuesdays",None),
    ("Garden Route Trivia League quiz at Red Bridge Brewing Co. (1st Wednesday)","Knysna","Red Bridge Brewing Co.","Noble Street, Knysna Industria, Knysna",_nth(2,{1}),"1st Wednesday",(-34.04692,23.0772008,"nominatim")),
    ("Garden Route Trivia League quiz at Knysna Distillery (2nd-5th Wednesdays)","Knysna","Knysna Distillery","5 Uil Street, Knysna Industria, Knysna",_nth(2,{2,3,4,5}),"2nd, 3rd, 4th (+5th) Wednesdays",(-34.0448812,23.0727766,"nominatim")),
    ("Garden Route Trivia League quiz at Rocket, George (Thursdays)","George","Rocket","Arbour Road, Heatherlands, George",_weekly({3}),"Thursdays",(-33.946309,22.456057,"nominatim")),
    ]:
    add(title=_t,category="quiz",start_date=_dates[0],end_date=_dates[-1],occurrences=_dates,recurrence=_rec,time="",town=_town,venue=_ven,venue_address=_addr,
        price_from="",ticket_url="",source_url=_GRT,source_name="Knysna Diary (n2rs.com), October 2026",notes=_GRN%_rec,
        **({"lat":_ll[0],"lng":_ll[1],"geo_source":_ll[2]} if _ll else {}))
_bq=_nth(3,{-1})
add(title="Quiz Night at The Backyard Beer Garden (last Thursday of the month)",category="quiz",start_date=_bq[0],end_date=_bq[-1],occurrences=_bq,
    recurrence="Last Thursday of every month, 19:00-21:00",time="19:00-21:00",town="Jeffreys Bay",venue="The Backyard Beer Garden",venue_address="12 Oosterland Street, Jeffreys Bay",
    price_from="",ticket_url="",source_url="https://9ty9.co.za/events/quiz-night-a-the-backyard-2026-09-24/",source_name="9ty9.co.za (Jeffreys Bay what's on)",
    alt_sources=["https://9ty9.co.za/events/quiz-night-a-the-backyard-2026-08-27/"],
    notes="Monthly quiz night hosted by Brian C. Pyle, every last Thursday. Listings exist for 27 Aug and 24 Sep 2026; the dates here follow that monthly pattern and aren't individually confirmed.",
    lat=-34.051257,lng=24.921325,geo_source="nominatim (street)")

# ---- Festive dining: Christmas 2026 (added 2026-10-06). Only 2026-dated offers with a price, menu or booking page. ----
add(title="Christmas Day Lunch at Moody Lagoon, Benguela Cove",category="festive",start_date="2026-12-25",time="12:00",town="Hermanus",venue="Moody Lagoon restaurant, Benguela Cove Lagoon Wine Estate",
    venue_address="Benguela Cove Lagoon Wine Estate, Walker Bay, Hermanus",price_from="",ticket_url="https://benguelacove.co.za/products/christmas-lunch-2026",
    source_url="https://benguelacove.co.za/products/christmas-lunch-2026",source_name="Benguela Cove (official site)",
    notes="Multi-course Christmas lunch from 12:00: camembert milk-bun wreath to share; choice of honey-glazed gammon, stuffed chicken or smoked roast beef with sides; Amarula malva pudding or summer trifle. Kids' menu available. Christmas brunch 09:30-11:30 also offered. Price per person not published on the page; a 50% deposit secures the booking. Menu: on the booking page (downloadable). Bookings: 087 357 0637, info@benguelacove.co.za.",
    lat=-34.3459946,lng=19.1346456,geo_source="nominatim")
_LB="https://www.lagoonbeachhotel.co.za/dining/events/"
add(title="Christmas Day Lunch buffet at Lagoon Beach Hotel",category="festive",start_date="2026-12-25",time="12:00",town="Cape Town",venue="Lagoon Beach Hotel & Spa",
    venue_address="1 Lagoon Gate Drive, Milnerton, Cape Town",price_from="R850 pp",ticket_url=_LB+"christmas-day-lunch-a-spectacular-festive-feast",
    source_url=_LB+"christmas-day-lunch-a-spectacular-festive-feast",source_name="Lagoon Beach Hotel (official site)",
    notes="Christmas buffet with sushi station, turkey, sirloin, pork belly, linefish and dessert buffet; live entertainment, welcome drink, crackers and a festive gift. R850 per person; children under 12 half price, under 5 free. Full pre-payment required. Menu: on the event page. Bookings: events@lagoonbeachhotel.co.za, 021 528 2000.",
    lat=-33.8922946,lng=18.4826759,geo_source="nominatim")
add(title="Frugal & Festive Christmas Day buffet at Lagoon Beach Hotel",category="festive",start_date="2026-12-25",time="",town="Cape Town",venue="Lagoon Beach Hotel & Spa",
    venue_address="1 Lagoon Gate Drive, Milnerton, Cape Town",price_from="R500 pp",ticket_url=_LB+"frugal-festive-an-affordable-christmas-day-lunch-buffet",
    source_url=_LB+"frugal-festive-an-affordable-christmas-day-lunch-buffet",source_name="Lagoon Beach Hotel (official site)",
    notes="Lighter, budget Christmas Day lunch buffet: roast turkey, gammon, linefish, Christmas pudding, mince pies, sherry trifle. R500 per person including a welcome drink. Menu: on the event page. Bookings: events@lagoonbeachhotel.co.za, 021 528 2000.",
    lat=-33.8922946,lng=18.4826759,geo_source="nominatim")
_CG="https://www.capegrace.com/experiences/festive-season/"
for _t,_d,_tm,_p,_n in [
    ("Christmas Eve Dinner at Heirloom, Cape Grace","2026-12-24","18:30-20:00 (seatings)","R2,500 pp","Welcome drink and live pianist, festive starters table, choice of three mains and family-style desserts. R2,500 per person. Seatings from 18:30, final seating 20:00. Smart casual."),
    ("Christmas Day Lunch at Heirloom, Cape Grace","2026-12-25","12:00-15:00","R3,000 pp","Festive lunch with a classical live trio, overlooking the V&A Waterfront marina. R3,000 per person excluding beverages; under-12s may choose the festive or junior à la carte menu. Smart casual."),
    ("Christmas Day Dinner at Heirloom, Cape Grace","2026-12-25","18:30-21:30","R2,500 pp","Festive dinner with live pianist. R2,500 per person excluding beverages. Smart casual."),
    ]:
    add(title=_t,category="festive",start_date=_d,time=_tm,town="Cape Town",venue="Heirloom Restaurant, Cape Grace",venue_address="West Quay Road, V&A Waterfront, Cape Town",
        price_from=_p,ticket_url=_CG,source_url=_CG,source_name="Cape Grace (official site)",notes=_n+" Bookings: capegrace.reservations@fairmont.com.",
        lat=-33.9087013,lng=18.4204936,geo_source="nominatim")
add(title="Christmas Day Lunch at Quentin at Oakhurst, Hout Bay",category="festive",start_date="2026-12-25",time="Lunch",town="Cape Town",venue="Quentin at Oakhurst",
    venue_address="Oakhurst Farm, Main Road, Hout Bay",price_from="",ticket_url="https://oakhurstbarn.com/menu/christmas-day-lunch/",
    source_url="https://oakhurstbarn.com/menu/christmas-day-lunch/",source_name="Quentin at Oakhurst (official site)",
    notes="Published 'Christmas Menu 2026': Brut with gravadlax blinis, vichyssoise with Kalahari truffle, Cape seafood salad, goose liver terrine, buchu sorbet, roast duck with apricot and pecan stuffing, Christmas pudding and mince pies. Price not published. The restaurant is open for lunch only on 25 December. Bookings: 021 790 4888, bookings@oakhurstbarn.com.",
    lat=-34.0205556,lng=18.3747623,geo_source="nominatim (suburb)")

# ---- New Year's Eve 2026 (added 2026-10-06); real categories kept, the app tags them via the 'nye' flag ----
add(title="Great Gatsby New Year's Eve party at Benguela Cove",category="concert",start_date="2026-12-31",end_date="2027-01-01",time="19:30-01:00",town="Hermanus",
    venue="Benguela Cove Lagoon Wine Estate",venue_address="Benguela Cove Lagoon Wine Estate, Walker Bay, Hermanus",price_from="R850 pp",
    ticket_url="https://benguelacove.co.za/products/new-years-eve-2026",source_url="https://benguelacove.co.za/products/new-years-eve-2026",source_name="Benguela Cove (official site)",
    notes="Roaring Twenties NYE party by the Bot River Lagoon: live DJ, 360-degree video booth, midnight countdown; Gatsby / black-tie dress. Standard ticket R850 pp early bird (until 15 Nov), R950 after; with picnic basket R1,350 / R1,450; under-12 R450. Capped at 180 guests. Dinner at Moody Lagoon restaurant can be booked separately.",
    lat=-34.3459946,lng=19.1346456,geo_source="nominatim")
add(title="New Year's Eve White Marina Soirée at Cape Grace",category="festive",start_date="2026-12-31",end_date="2027-01-01",time="18:30-01:00",town="Cape Town",
    venue="Heirloom Restaurant, Cape Grace",venue_address="West Quay Road, V&A Waterfront, Cape Town",price_from="R6,500 pp",
    ticket_url="https://www.capegrace.com/experiences/festive-season/",source_url="https://www.capegrace.com/experiences/festive-season/",source_name="Cape Grace (official site)",
    notes="Canapés and Blanc de Blanc in the Library Lounge, dinner in Heirloom, dessert on the Pool Deck, live music. R6,500 per person, R3,500 under 12. Yacht-chic dress encouraged. Bookings: capegrace.reservations@fairmont.com.",
    lat=-33.9087013,lng=18.4204936,geo_source="nominatim")
add(title="New Year's Eve at Bascule Bar, Cape Grace",category="concert",start_date="2026-12-31",end_date="2027-01-01",time="12:00-02:00",town="Cape Town",
    venue="Bascule Bar, Cape Grace",venue_address="West Quay Road, V&A Waterfront, Cape Town",price_from="",
    ticket_url="",source_url="https://www.capegrace.com/experiences/festive-season/",source_name="Cape Grace (official site)",
    notes="Waterfront NYE at Bascule with a live jazz band, DJ, cocktails and the bar menu. Tables first come, first served (no reservations); no children. No entry price published.",
    lat=-33.9087013,lng=18.4204936,geo_source="nominatim")
add(title="New Year's Eve dinner at The Commodore Hotel (V&A Waterfront)",category="festive",start_date="2026-12-31",end_date="2027-01-01",time="19:30-02:00",town="Cape Town",
    venue="The Commodore Hotel",venue_address="Portswood Road, V&A Waterfront, Cape Town",price_from="R1,395 pp",
    ticket_url="https://www.legacyhotels.co.za/commodore-hotel/new-year-2026",source_url="https://www.legacyhotels.co.za/commodore-hotel/new-year-2026",source_name="The Commodore Hotel (Legacy Hotels)",
    notes="International buffet with live cooking stations and live entertainment; midnight toast on the terrace with views of the Waterfront fireworks. R1,395 per adult. Bookings essential: commodore@legacyhotels.com, 021 415 1000.",
    lat=-33.9050499,lng=18.4183932,geo_source="nominatim (street)")
add(title="MonteVista Community New Year's Eve Dinner Dance",category="community",start_date="2026-12-31",end_date="2027-01-01",time="19:00-01:00",town="Cape Town",
    venue="Edgemead Hall",venue_address="100 Edgemead Drive, Edgemead, Cape Town",price_from="R450 pp",
    ticket_url="https://www.quicket.co.za/events/390561-montevista-community-new-years-eve-dinner-dance/",source_url="https://www.quicket.co.za/events/390561-montevista-community-new-years-eve-dinner-dance/",source_name="Quicket",
    alt_sources=["https://www.findmy.co.za/entertainment/events_details/montevista-community-new-years-eve-dinner-dance/63411"],
    notes="Community dinner dance with live band 'Just Like That', lamb on the spit and braaied chicken; bring your own drinks. R450 pp early bird (to 30 Nov), R495 after; bookings close 18 Dec. Proceeds go to neighbourhood security cameras.",
    lat=-33.8802452,lng=18.5424385,geo_source="event page",_img="https://images.quicket.co.za/0977885_0.jpeg")
add(title="New Year's Fireworks 80's Lumo Party Cruise",category="concert",start_date="2026-12-31",end_date="2027-01-01",time="22:00-01:15",town="Cape Town",
    venue="Cape Town Cruises, V&A Waterfront",venue_address="Shop 8, Quay 5, V&A Waterfront, Cape Town",price_from="R1500",
    ticket_url="https://www.quicket.co.za/events/383158-new-years-fireworks-80s-lumo-party-cruise/",source_url="https://www.quicket.co.za/events/383158-new-years-fireworks-80s-lumo-party-cruise/",source_name="Quicket",
    notes="Three-hour 80s neon party cruise along the Cape Town coastline: boarding 22:00, departure 22:15, back 01:15; shared charcuterie boards and a bottle of bubbly per couple, fireworks at midnight. Listing says R1,899 per person; Quicket shows tickets from R1,500. Info: 066 428 9676.",
    lat=-33.9061852,lng=18.4209652,geo_source="event page",_img="https://images.quicket.co.za/0942732_0.jpeg")
