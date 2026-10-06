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
add(title="Etensuurkonsert: organ & choir (spring lunch-hour series opener)",category="concert",start_date="2026-10-07",time="13:10",town="George",
    venue="NG Moedergemeente (Moederkerk)",venue_address="Courtenay Street, George",price_from="Free entry",ticket_url="",
    source_url="https://www.georgeherald.com/Whatson",source_name="George Herald (What's On)",
    notes="Organist Gerrit Jordaan with the NG Kerk Hartenbos choir (cond. Marianne Rust); about 50 minutes, donations welcome.")

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
