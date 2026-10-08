# Hand-curated entries. Every entry's details were read on source_url (and alt_sources).
# Fields not shown on the source are left empty.
OTR="https://www.ontheroute.co.za/your-garden-route-event-guide-1-october/"
MB="https://visitmosselbay.co.za/event/"
M=[]
def add(**k): M.append(k)
import datetime as _dtm
HORIZON=(_dtm.date.today()+_dtm.timedelta(days=183)).isoformat()  # rolling end for weekly/recurring series

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

occ=_dates("2026-10-10",HORIZON,[SAT])
add(title="Wild Oats Community Farmers' Market",category="market",start_date=occ[0],end_date=occ[-1],occurrences=occ,recurrence="Every Saturday, 07:30-12:00 (summer hours)",
    time="07:30-12:00",town="Sedgefield",venue="Wild Oats Community Farmers' Market",venue_address="Western outskirts of Sedgefield, cnr N2 & Jan van Riebeeck St (at Swartvlei)",
    price_from="Free entry",ticket_url="",source_url="https://www.wildoatsmarket.co.za/",source_name="Wild Oats Market (official site)",
    alt_sources=["https://www.georgeherald.com/Whatson","https://www.toodoo.co.za/wild-oats-community-farmers-market/"],
    notes="Producer-only farmers' market since 1999: fresh produce, meats, cheeses, breads, breakfast. Open rain or shine; Facebook page confirms high-season hours.",
    lat=-34.009806,lng=22.778306,geo_source="event page")
occ=_dates("2026-10-10",HORIZON,[SAT])
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
occ=_dates("2026-10-07",HORIZON,[WED])
add(title="The Wednesday Market at Old Nick Village",category="market",start_date=occ[0],end_date=occ[-1],occurrences=occ,recurrence="Every Wednesday, 09:00-14:00",
    time="09:00-14:00",town="Plettenberg Bay",venue="Old Nick Village",venue_address="N2, 3 km east of Plettenberg Bay",
    price_from="Free entry",ticket_url="",source_url="https://oldnickvillage.co.za/merchants/the-old-nick-midweek-market/",source_name="Old Nick Village (official site)",
    alt_sources=["https://showme.co.za/plett/event/mid-week-market-at-old-nick-village/"],
    notes="Farmers, bakers and artisans: organic produce, meat and dairy, breads, crafts.")
occ=_dates("2026-10-10",HORIZON,[SAT])
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
import json as _json, os as _os, re
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
def _weekly(wds,start="2026-10-06",end=None):
    end=end or HORIZON
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
def _nth(wd,nths,start="2026-10-06",end=None):
    end=end or HORIZON
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
for _t,_town,_ven,_addr,_dl,_rec,_ll in [
    ("Garden Route Trivia League quiz at Goose Valley Golf Club (Tuesdays)","Plettenberg Bay","Goose Valley Golf Club","Goose Valley Golf Club, Plettenberg Bay",_weekly({1}),"Tuesdays",None),
    ("Garden Route Trivia League quiz at Red Bridge Brewing Co. (1st Wednesday)","Knysna","Red Bridge Brewing Co.","Noble Street, Knysna Industria, Knysna",_nth(2,{1}),"1st Wednesday",(-34.04692,23.0772008,"nominatim")),
    ("Garden Route Trivia League quiz at Knysna Distillery (2nd-5th Wednesdays)","Knysna","Knysna Distillery","5 Uil Street, Knysna Industria, Knysna",_nth(2,{2,3,4,5}),"2nd, 3rd, 4th (+5th) Wednesdays",(-34.0448812,23.0727766,"nominatim")),
    ("Garden Route Trivia League quiz at Rocket, George (Thursdays)","George","Rocket","Arbour Road, Heatherlands, George",_weekly({3}),"Thursdays",(-33.946309,22.456057,"nominatim")),
    ]:
    add(title=_t,category="quiz",start_date=_dl[0],end_date=_dl[-1],occurrences=_dl,recurrence=_rec,time="",town=_town,venue=_ven,venue_address=_addr,
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

# ---- Nature & outdoors / community groups (added 2026-10-06) ----
_BLP="BirdLife Plettenberg Bay (official site)"
add(title="BirdLife Plett talk & dinner: Chanel Visser – Seabirds in Need: Rescue, Research and Recovery",category="nature",start_date="2026-10-12",
    time="17:45 arrival, 18:00 talk, 19:30 dinner",town="Plettenberg Bay",venue="Plettenberg Bay Country Club",venue_address="Piesang Valley Road, Plettenberg Bay",
    price_from="R50",ticket_url="https://birdlife-plett.co.za/event/dinner-presentation-talk-chanel-visser-seabirds-in-need/",
    source_url="https://birdlife-plett.co.za/event/dinner-presentation-talk-chanel-visser-seabirds-in-need/",source_name=_BLP,
    notes="CapeNature marine ranger Chanel Visser, coordinator of the Plett Marine Stranding Network, on seabird strandings along the Garden Route: which species strand and why, how to tell a resting bird from one in distress, and how to respond safely. Talk and dinner R200 members / R220 non-members (dinner bookings close Thu 8 Oct); talk only R50 members / R60 non-members. Bookings via Quicket only (link on the club's event page); enquiries Jenny Wilson 083 388 5006. Cash bar.",
    lat=-34.0651111,lng=23.3505023,geo_source="nominatim",_img="https://birdlife-plett.co.za/wp-content/uploads/2026/02/ChannelSeabirdTalkPoster-845x321.jpeg")
add(title="BirdLife Plett birding walk (October)",category="nature",start_date="2026-10-17",time="07:30-11:00",town="Plettenberg Bay",
    venue="Venue to be confirmed",venue_address="Plettenberg Bay area",price_from="",ticket_url="",
    source_url="https://birdlife-plett.co.za/event/birding-walk-october-venue-to-be-confirmed/",source_name=_BLP,
    notes="Monthly morning birding walk by BirdLife Plettenberg Bay. The venue is still to be confirmed on the club's event page; contact info@birdlife-plett.co.za or 082 878 6662 to join. The club notes that Garden Route weather can force last-minute changes.",
    lat=-34.052778,lng=23.369444,geo_source="town centroid (venue to be confirmed)",_img="https://birdlife-plett.co.za/wp-content/uploads/2025/03/IMG_1835-845x321.jpg")
add(title="BirdLife Plett Feather Chase & year-end braai",category="nature",start_date="2026-11-14",time="07:00-14:00",town="Plettenberg Bay",
    venue="Venue to be confirmed",venue_address="Plettenberg Bay area",price_from="",ticket_url="",
    source_url="https://birdlife-plett.co.za/event/feather-chase-and-year-end-braai-2026/",source_name=_BLP,
    notes="The club's annual Feather Chase (a morning of birding to tick as many species as possible) followed by the year-end braai. Venue still to be confirmed on the club's event page; contact info@birdlife-plett.co.za or 082 878 6662.",
    lat=-34.052778,lng=23.369444,geo_source="town centroid (venue to be confirmed)",_img="https://birdlife-plett.co.za/wp-content/uploads/2025/12/PHOTO-2025-11-21-14-59-05-845x321.jpg")
add(title="Great Southern Bioblitz 2026 – Garden Route (iNaturalist citizen science)",category="nature",start_date="2026-11-27",end_date="2026-11-30",
    time="All day; Wild Rescue iNaturalist workshops Sat 28 & Sun 29 Nov",town="Stilbaai",venue="Anywhere in the Garden Route; workshops at Wild Rescue nature reserve",
    venue_address="Wild Rescue nature reserve, Stilbaai (Hessequa)",price_from="Free",ticket_url="https://www.inaturalist.org/projects/great-southern-bioblitz-2026-garden-route",
    source_url="https://www.knysnaplettherald.com/News/Article/Local-News/wild-rescue-nature-reserve-champions-the-great-southern-bioblitz-2026-for-garden-route-district-202609211200",
    source_name="Knysna-Plett Herald",alt_sources=["https://wildrescue.co.za/wild-rescue-nature-reserve-champions-the-great-southern-bioblitz-2026-for-garden-route-district/","https://www.inaturalist.org/projects/great-southern-bioblitz-2026-garden-route","https://www.knysna.n2rs.com/knysna-diary-november.html"],
    notes="Four-day Southern Hemisphere biodiversity survey: photograph any wild plant, animal or fungus and upload it to the free iNaturalist app, linked to the 'Great Southern Bioblitz 2026 - Garden Route' project. Free, no expertise needed; 14 days afterwards to finish uploads and IDs. Wild Rescue (Garden Route organiser) runs practical iNaturalist workshops and trail walks at its reserve on 28 and 29 November; times and bookings to be announced on its social media.",
    lat=-34.368333,lng=21.411111,geo_source="town centroid (reserve near Stilbaai)",_img="https://wildrescue.co.za/wp_2023/wp-content/uploads/2026/09/GSBB-2026-Garden-Route-1024x429.png")
add(title="Garden Route Indigenous Plant Fair",category="market",start_date="2026-10-30",end_date="2026-11-01",time="",town="George",
    venue="Garden Route Botanical Garden",venue_address="49 Caledon Street, George",price_from="",ticket_url="",
    source_url="https://www.knysna.n2rs.com/knysna-diary-october.html",source_name="Knysna Diary (n2rs.com), October 2026",
    alt_sources=["https://botanicalgarden.org.za/","https://www.facebook.com/GRBotanical/"],
    notes="Annual plant fair (the garden says it is usually on the first weekend of November): 5,000+ indigenous plants of 400+ species for sale, gardening talks and indigenous-focused presentations, creative art workshops, food and craft stalls and a kids zone. Times not yet published; Garden Route Botanical Garden 044 874 1558.",
    lat=-33.9442967,lng=22.4627937,geo_source="nominatim",_img="https://botanicalgarden.org.za/wp-content/uploads/2022/03/GBGC-Front-Page.jpg")
add(title="Art & Flowers exhibition for Hospice Knysna Sedgefield",category="community",start_date="2026-10-27",end_date="2026-10-28",
    time="Tue 13:00-17:00; Wed 09:30-15:00",town="Knysna",venue="Amble Ridge",venue_address="Sunninghill Drive, Hunters Home, Knysna",price_from="",ticket_url="",
    source_url="https://www.hospiceknysna.org.za/news-and-events/up-and-coming-events/",source_name="Hospice Knysna Sedgefield (official site)",
    notes="Hospice fundraiser: floral art interpretations of local paintings, with selected paintings on sale. Hospice 044 384 0593.",
    lat=-34.0518308,lng=23.0785323,geo_source="nominatim (suburb)",_img="https://www.hospiceknysna.org.za/wp-content/uploads/2021/11/feature_events.jpg")
_SS="https://www.iloveboobies.co.za/pages/2026-secret-swim"
for _t,_ll in (("Sedgefield",(-34.015606,22.802768)),("Plettenberg Bay",(-34.052778,23.369444))):
    add(title=f"ILoveBoobies Secret Swim 2026 – {_t}",category="community",start_date="2026-10-10",time="Gather 07:30, briefing 08:00",town=_t,
        venue="Secret beach location (pin sent at 21:00 the night before)",venue_address=_t,price_from="R200",
        ticket_url="https://www.iloveboobies.co.za/products/secret-swim-2026-choose-your-location",source_url=_SS,source_name="ILoveBoobies ZA NPC (official site)",
        alt_sources=["https://www.knysna.n2rs.com/knysna-diary-october.html"],
        notes="Women-only, phone-free 90-minute sea dip (not a race) honouring breast-cancer fighters, survivors and those lost; female lifesavers at every venue. R200 donation funds free breast screenings in underserved communities. Register online; the exact spot is emailed and messaged at 21:00 on 9 October. Bring a plate or snacks to share afterwards.",
        lat=_ll[0],lng=_ll[1],geo_source="town centroid (exact spot kept secret)",_img="https://www.iloveboobies.co.za/cdn/shop/files/Blue_pink_horizontal_911750e1-2f9a-4f40-91db-b5748e83bd6b_1200x1200.jpg?v=1777311214")
add(title="George Festival 2026 (sport, culture & music)",category="festival",start_date="2026-12-12",end_date="2026-12-16",time="",town="George",
    venue="Various venues across George",venue_address="George",price_from="",ticket_url="",
    source_url="https://www.george.gov.za/planning-development/local-economic-development/tourism/george-festival-2025-culture-sport-art/",source_name="George Municipality",
    alt_sources=["https://www.george.gov.za/george-festival-2026-set-to-be-bigger-and-better/","https://www.georgeherald.com/News/Article/Local-News/george-festival-2026-expands-with-more-sport-beach-activities-and-entertainment-202608260841"],
    notes="Second George Festival, 12-16 December 2026: 10s rugby, soccer, athletics, vlakkie cricket, beach volleyball, table tennis, netball, disability sport, a 10 km road race, and gospel and jazz music festivals. Programme, venues and times still to be announced. In 2025 the municipality's Annual Lights Festival (Christmas lights switch-on at Unity Park, York Street) opened the festival; the 2026 lights date is not yet published.",
    lat=-33.963,lng=22.4617,geo_source="town centroid (multiple venues)",_img="https://cms.groupeditors.com/img/2026/Aug/7ef5396d-7ede-4bad-9787-f398172de717.JPG")

# ---- Christmas 2026 (carols / Christmas concerts) ----
add(title="Die Heilige Nag – Petronel Baard & Mathys Roets Christmas concert",category="concert",start_date="2026-12-22",time="19:00-21:00",town="Hartenbos",
    venue="NG Gemeente Hartenbos",venue_address="4 Majuba Avenue, Hartenbos",price_from="R200",
    ticket_url="https://www.quicket.co.za/events/392041-die-heilige-nag/",source_url="https://www.quicket.co.za/events/392041-die-heilige-nag/",source_name="Quicket",
    notes="One-night Christmas show: Petronel Baard and her orchestra with singer Mathys Roets, Christmas favourites on violin, percussion, guitars, cello and piano, plus Christmas stories. Tickets from R200 via Quicket or the church office 044 695 0440; WhatsApp Petronel 082 737 8416.",
    lat=-34.1227323,lng=22.1178284,geo_source="nominatim (street)",_img="https://images.quicket.co.za/0989377_0.jpeg")
add(title="Christmas Eve Carols by Candlelight & buffet at St Francis Links",category="festive",start_date="2026-12-24",time="18:00-21:00",town="St Francis Bay",
    venue="St Francis Links Clubhouse",venue_address="1 Jack Nicklaus Drive, St Francis Links, St Francis Bay",price_from="R295",
    ticket_url="https://www.quicket.co.za/events/392121-christmas-eve-buffet/",source_url="https://www.quicket.co.za/events/392121-christmas-eve-buffet/",source_name="Quicket",
    alt_sources=["https://9ty9.co.za/events/christmas-eve-buffet/","https://www.findmy.co.za/entertainment/events_details/christmas-eve-buffet/62204"],
    notes="Carols by Candlelight from 18:00, then a Christmas Eve buffet with live entertainment by Nádine from 19:00. Kids can decorate gingerbread houses and reindeer cookies; parents can drop off gifts for Santa to hand out. From R295.",
    lat=-34.1620331,lng=24.8150387,geo_source="event page",_img="https://images.quicket.co.za/0970950_0.jpeg")

# ---- Running Guy races merge (added 2026-10-06): missing fun runs / marathons / trails from the 6 Oct 2026–28 Feb 2027 export ----
RG_SRC="Running Guy races dashboard"
add(title="Sleeping Beauty Race, Riversdale (10 km & 5 km)",category="funrun",start_date="2026-10-10",town="Riversdale",venue="Riversdale Town Square",venue_address="Riversdale Town Square, Riversdale",price_from="",ticket_url="https://entrytickets.net/sleepingbeautyrace/enter",source_url="https://entrytickets.net/sleepingbeautyrace/enter",source_name="EntryTickets",notes="Small-town road 10/5 km from Riversdale Town Square, 07:00 start. About 1h45 west of George; same day as Meiringspoort Half. Online entries open on EntryTickets (10 km R115, 5 km R60; temp licence R50); close 7 Oct. Price hint from Running Guy (unverified): R115, 5; R60; R50 — confirm on the entry page. Listed by Running Guy (Garden Route races dashboard).",alt_sources=["https://dash.streblainnovations.com/races/"])
add(title="Fancourt Marathon (42.2 km & 21.1 km)",category="funrun",start_date="2026-10-17",town="George",venue="The Ridge at Fancourt",venue_address="Fancourt, George",price_from="",ticket_url="https://www.entryninja.com/events/83786-fancourt-marathon",source_url="https://www.entryninja.com/events/83786-fancourt-marathon",source_name="Entry Ninja",notes="Home-soil marathon from The Ridge at Fancourt. Mix of tar, dirt tracks and farm roads — gravel shoes optional. Entries close 10 Oct. Excellent local A-race. Price hint from Running Guy (unverified): R350 — confirm on the entry page. Optional paid race t-shirts (Half/Full Marathon editions) available via Entry Ninja shop at R350 — not included with entry. Medals included. Listed by Running Guy (Garden Route races dashboard).",lat=-33.9679097,lng=22.4106706,geo_source="nominatim",alt_sources=["https://dash.streblainnovations.com/races/"],_img="https://d1zwi51l39apzt.cloudfront.net/uploads/events/83786/NRRm87oZGnkCGskwX81D2ADqon88KhBO8CZwKOqG.jpg")
add(title="George Used Car Parts 10 km Race (10 km & 5 km)",category="funrun",start_date="2026-11-07",town="George",venue="George",venue_address="George",price_from="",ticket_url="",source_url="https://runningcalendar.co.za/races/city/george",source_name="RunningCalendar.co.za",notes="Local Saturday 10/5 km. Same day as Winelands if staying home. Listed by Running Guy (Garden Route races dashboard).",alt_sources=["https://dash.streblainnovations.com/races/"])
add(title="Vlakte Marathon (Heidelberg to Witsand; 42.2 / 21.1 / 10.4 / 5 km)",category="funrun",start_date="2026-11-20",end_date="2026-11-21",town="Witsand",venue="Heidelberg to Witsand Beach",venue_address="Heidelberg / Witsand, Western Cape",price_from="",ticket_url="",source_url="https://runningcalendar.co.za/events/vlakte-marathon/2026",source_name="RunningCalendar.co.za",notes="Point-to-point from Heidelberg to Witsand Beach. Comrades/Two Oceans qualifier. Entries via EntryNinja close 16 Nov. ~1.5h west of George. Price hint from Running Guy (unverified): R255; R150 — confirm on the entry page. T-shirt R255 and socks R150 listed as paid add-ons on RunningCalendar. Listed by Running Guy (Garden Route races dashboard).",lat=-34.394444,lng=20.846111,geo_source="nominatim (finish town)",alt_sources=["https://dash.streblainnovations.com/races/"])
add(title="Palm Tyres Half Marathon (21.1 / 10 / 5 km)",category="funrun",start_date="2026-12-05",town="George",venue="Palm Tyres, Courtenay Street",venue_address="Courtenay Street, George",price_from="",ticket_url="",source_url="https://runningcalendar.co.za/events/palm-tyres-half-marathon/2026",source_name="RunningCalendar.co.za",notes="Grasshoppers / Outeniqua Harriers staple from Palm Tyres, Courtenay Street. Walkers welcome. Watch for entry opening. Date, time and venue confirmed. Fees and entry link not yet published (assumed from 2025). Listed by Running Guy (Garden Route races dashboard).",lat=-33.963,lng=22.4617,geo_source="town centroid",alt_sources=["https://dash.streblainnovations.com/races/"])
add(title="Somerson Half Marathon, Hartenbos (21.1 / 10 / 5 km)",category="funrun",start_date="2026-12-12",town="Hartenbos",venue="Hartenbos",venue_address="Hartenbos",price_from="",ticket_url="",source_url="https://runningcalendar.co.za/races/city/george",source_name="RunningCalendar.co.za",notes="Hartenbos half in the December holiday cluster. Local, flat-ish coastal roads. Listed by Running Guy (Garden Route races dashboard).",alt_sources=["https://dash.streblainnovations.com/races/"])
add(title="Louis Massyn Rocket Run (10 km & 5 km)",category="funrun",start_date="2026-12-14",town="George",venue="George",venue_address="George",price_from="",ticket_url="",source_url="https://runningcalendar.co.za/races/city/george",source_name="RunningCalendar.co.za",notes="Monday local 10/5 km in George. Festive-season club race. Listed by Running Guy (Garden Route races dashboard).",alt_sources=["https://dash.streblainnovations.com/races/"])
add(title="Fancourt 10 km",category="funrun",start_date="2026-12-18",town="George",venue="Fancourt",venue_address="Fancourt, George",price_from="",ticket_url="",source_url="https://runningcalendar.co.za/races/city/george",source_name="RunningCalendar.co.za",notes="Estate 10 km at Fancourt. Fast, scenic, local. Listed by Running Guy (Garden Route races dashboard).",lat=-33.9679097,lng=22.4106706,geo_source="nominatim",alt_sources=["https://dash.streblainnovations.com/races/"],_img="https://d1zwi51l39apzt.cloudfront.net/uploads/events/83786/NRRm87oZGnkCGskwX81D2ADqon88KhBO8CZwKOqG.jpg")
add(title="Lappiesbaai 10 km on the Beach (10 km & 5 km)",category="funrun",start_date="2026-12-20",town="Stilbaai",venue="Lappiesbaai Beach",venue_address="Lappiesbaai, Still Bay West, Stilbaai",price_from="",ticket_url="",source_url="https://runningcalendar.co.za/events/lappiesbaai-10km/2026",source_name="RunningCalendar.co.za",notes="Date is provisional (Running Guy estimate — often from the prior year); confirm before travelling. Beach run at Lappiesbaai, Still Bay West. Clashes with Tower-2-Sea. Confirm before travelling. RunningCalendar lists 20 Dec 2026 as estimated from the previous year — not yet confirmed by organiser. Listed by Running Guy (Garden Route races dashboard).",lat=-34.3719444,lng=21.4302778,geo_source="nominatim",alt_sources=["https://dash.streblainnovations.com/races/"])
add(title="Tower-2-Sea Trail Run (56 / 50 / 42 / 33 km)",category="funrun",start_date="2026-12-20",town="Knysna",venue="Buffelsnek Fire Tower → Thesen Island",venue_address="Buffelsnek / Thesen Island, Knysna",price_from="",ticket_url="https://entrytickets.co.za/tower2sea",source_url="https://www.wannado.co.za/t2s",source_name="WannaDo / Tower-2-Sea (official site)",notes="Sunrise start at Buffelsnek Fire Tower, descend through Knysna Forest (Outeniqua Hiking Trail / elephant paths) to Thesen Island. Distances 33–56 km (no short fun-run option). Listed by Running Guy (Garden Route races dashboard).",lat=-34.0477753,lng=23.0537836,geo_source="nominatim (finish)",alt_sources=["https://entrytickets.co.za/tower2sea","https://dash.streblainnovations.com/races/"],_img="https://static.wixstatic.com/media/b877ad_7f3f771780fb4c59a5b86f2d957ac913~mv2.jpg")
add(title="Chasing Cheese Burgers (10 km & 5 km)",category="funrun",start_date="2027-01-13",town="George",venue="George",venue_address="George",price_from="",ticket_url="",source_url="https://runningcalendar.co.za/races/city/george",source_name="RunningCalendar.co.za",notes="Date is provisional (Running Guy estimate — often from the prior year); confirm before travelling. Quirky local midweek 10/5 km. Confirm closer to January. George city calendar lists Wed 13 Jan 2027 as date TBC. Listed by Running Guy (Garden Route races dashboard).",alt_sources=["https://dash.streblainnovations.com/races/"])
add(title="Two Lagoons (30 km & 10 km)",category="funrun",start_date="2027-01-30",town="Hoekwil",venue="Hoekwil / Wilderness lakes",venue_address="Hoekwil",price_from="",ticket_url="",source_url="https://runningcalendar.co.za/events/two-lagoons/2026",source_name="RunningCalendar.co.za",notes="Date is provisional (Running Guy estimate — often from the prior year); confirm before travelling. Point-to-point / lake-country roads between Wilderness lakes. Organised by Cape Multisport Eden. Beautiful local long run. 2026 edition was 31 Jan at Libertas Guest Farm, Hoekwil (30/10 km). George calendar lists Sat 30 Jan 2027 — not yet independently verified. Listed by Running Guy (Garden Route races dashboard).",alt_sources=["https://dash.streblainnovations.com/races/"])
add(title="De Dekke Spar Run, Great Brak (21.1 / 10 / 5 km)",category="funrun",start_date="2027-02-06",town="Groot Brak",venue="Great Brak River",venue_address="Great Brak River",price_from="",ticket_url="",source_url="https://runningcalendar.co.za/races/city/george",source_name="RunningCalendar.co.za",notes="Date is provisional (Running Guy estimate — often from the prior year); confirm before travelling. Great Brak half. Coastal village roads between Mossel Bay and George. George city calendar lists Sat 6 Feb 2027 as date TBC. Listed by Running Guy (Garden Route races dashboard).",alt_sources=["https://dash.streblainnovations.com/races/"])
add(title="Knysna Heads Marathon (42.2 / 21.1 / 10 / 5 km)",category="funrun",start_date="2027-02-13",town="Knysna",venue="Thesen Islands",venue_address="Thesen Island, Knysna",price_from="",ticket_url="",source_url="https://runningcalendar.co.za/events/knysna-heads-marathon",source_name="RunningCalendar.co.za",notes="Date is provisional (Running Guy estimate — often from the prior year); confirm before travelling. Comrades & Two Oceans qualifier around the Knysna lagoon and Heads. Flagship local marathon of February if confirmed. RunningCalendar estimates Saturday 13 Feb 2027 from prior years — not yet confirmed by Knysna Marathon Club. Listed by Running Guy (Garden Route races dashboard).",lat=-34.0477753,lng=23.0537836,geo_source="nominatim",alt_sources=["https://dash.streblainnovations.com/races/"])
add(title="Van Kervel School 10 km Night Race (10 km & 5 km)",category="funrun",start_date="2027-02-17",town="George",venue="Van Kervel School",venue_address="3rd Street, George East, George",price_from="",ticket_url="",source_url="https://runningcalendar.co.za/organisers/outeniqua-harriers",source_name="RunningCalendar.co.za",notes="Local midweek night race from Van Kervel School. Easy George option in the February cluster. Listed on Outeniqua Harriers / RunningCalendar organiser page for Wed 17 Feb 2027. Listed by Running Guy (Garden Route races dashboard).",lat=-33.9581121,lng=22.4784664,geo_source="nominatim",alt_sources=["https://dash.streblainnovations.com/races/"])
add(title="Outeniqua Chair Challenge (42.2 / 21.1 / 10 / 5 km)",category="funrun",start_date="2027-02-20",town="George",venue="George",venue_address="George",price_from="",ticket_url="",source_url="https://runningcalendar.co.za/events/occ-chair-challenge",source_name="RunningCalendar.co.za",notes="Date is provisional (Running Guy estimate — often from the prior year); confirm before travelling. George marathon/half from Carpe Diem School (Bos en Dal), 07:00 start. Hilly Outeniqua course; ASWD-sanctioned. RunningCalendar estimate from previous year; 2027 date not confirmed. Listed by Running Guy (Garden Route races dashboard).",alt_sources=["https://dash.streblainnovations.com/races/"])
add(title="Infantry School Cango Marathon (42.2 / 21.1 / 4 km)",category="funrun",start_date="2027-02-26",end_date="2027-02-27",town="Oudtshoorn",venue="Cango Caves / Ou Tol",venue_address="Cango Caves, R328, Oudtshoorn",price_from="",ticket_url="",source_url="https://runningcalendar.co.za/events/cango-marathon",source_name="RunningCalendar.co.za",notes="Date is provisional (Running Guy estimate — often from the prior year); confirm before travelling. Downhill-leaning marathon from Cango Caves / Ou Tol. Comrades/Two Oceans qualifier. ~1h over the Outeniqua from George. Clashes with Hermanus Trail Run. Estimated from previous years. Not yet confirmed. Listed by Running Guy (Garden Route races dashboard).",lat=-33.3922844,lng=22.2143761,geo_source="nominatim",alt_sources=["https://dash.streblainnovations.com/races/"])
add(title="Meiringspoort Half Marathon (21.1 km & 12.5 km)",category="funrun",start_date="2026-10-10",town="De Rust",venue="Meiringspoort",venue_address="Meiringspoort, De Rust",price_from="",ticket_url="https://www.entryninja.com/events/83907-32nd-meiringspoort-2026",source_url="https://www.entryninja.com/events/83907-32nd-meiringspoort-2026",source_name="Entry Ninja",notes="Spectacular poort road race through the Swartberg. Day-trip from George via the Outeniqua Pass / N12. Listed by Running Guy (Garden Route races dashboard).",lat=-33.4527786,lng=22.5593648,geo_source="nominatim",alt_sources=["https://dash.streblainnovations.com/races/"])
add(title="Crusaders 21.1 km & 10 km (plus 5 km fun run/walk), Gqeberha",category="funrun",start_date="2026-10-17",town="Gqeberha",venue="Crusaders, Gqeberha",venue_address="Gqeberha",price_from="",ticket_url="https://startingline.co.za/events/crusaders-211km-10km-race-5km-fun-runwalk-cc2aecd5",source_url="https://startingline.co.za/events/crusaders-211km-10km-race-5km-fun-runwalk-cc2aecd5",source_name="Starting Line",notes="Classic PE club half and 10 km with fun run. Same weekend as Fancourt — choose George or a PE road trip. Listed by Running Guy (Garden Route races dashboard).",lat=-33.9618598,lng=25.6186731,geo_source="town centroid",alt_sources=["https://dash.streblainnovations.com/races/"])
add(title="Cape Cobra Trail Marathon (42 / 33 / 21 / 10 km)",category="funrun",start_date="2026-10-24",town="Cape Town",venue="Table Mountain / Constantia (TMNP)",venue_address="Table Mountain National Park, Cape Town",price_from="",ticket_url="https://www.capecobratrail.com/",source_url="https://www.capecobratrail.com/",source_name="Cape Cobra Trail (official site)",notes="Wild TMNP ridgelines: 42 km ~2,000 m, 33 km ~1,800 m, 21 km ~1,000 m. Technical, prestige trail marathon. Finish-line festival at Constantia Uitsig. Limited-edition technical starters tee included in every entry, plus a branded bag and collectible patch. Listed by Running Guy (Garden Route races dashboard).",lat=-33.987,lng=18.41,geo_source="town centroid (TMNP)",alt_sources=["https://dash.streblainnovations.com/races/"],_img="http://static1.squarespace.com/static/67e5bd6f1f64ea0bc9a7450e/t/6822b772e836fd0ec7c860c1/1747105650/og.jpg")
add(title="Two Views Challenge, Gqeberha (10 km & 5 km)",category="funrun",start_date="2026-10-24",town="Gqeberha",venue="Italian Social Club, Broadwood",venue_address="Broadwood, Gqeberha",price_from="",ticket_url="",source_url="https://runningcalendar.co.za/events/two-views-challenge",source_name="RunningCalendar.co.za",notes="Charlo AC 10/5 km from the Italian Social Club, Broadwood. Entries via Webtickets until 21 Oct. On-the-day entries from 05:00. Listed by Running Guy (Garden Route races dashboard).",lat=-33.9618598,lng=25.6186731,geo_source="town centroid",alt_sources=["https://dash.streblainnovations.com/races/"])
add(title="Sportsmans Warehouse Winelands Marathon (42.2 / 21.1 / 10 km)",category="funrun",start_date="2026-11-07",town="Stellenbosch",venue="Stellenbosch / Somerset West",venue_address="Stellenbosch",price_from="",ticket_url="",source_url="https://runningcalendar.co.za/events/winelands-marathon/2026",source_name="RunningCalendar.co.za",notes="47th Helderberg Harriers showpiece through Stellenbosch/Somerset West. Comrades & Two Oceans 2027 qualifier. Sold out. Entry includes a pair of Balega socks. No race t-shirt listed. Listed by Running Guy (Garden Route races dashboard).",lat=-33.934444,lng=18.869167,geo_source="nominatim",alt_sources=["https://dash.streblainnovations.com/races/"])
add(title="RMB Ultra-trail Cape Town (100 mile / 100 / 55 / 35 / 23 / 16 km)",category="funrun",start_date="2026-11-20",end_date="2026-11-22",town="Cape Town",venue="Table Mountain / Cape Peninsula",venue_address="Cape Town",price_from="",ticket_url="https://www.ultratrailcapetown.com/",source_url="https://www.ultratrailcapetown.com/",source_name="Ultra-trail Cape Town (official site)",notes="SA's premier mountain ultra festival on Table Mountain / Peninsula. 100 miler ~7,000 m+. International field. Book travel early. Clashes with Vlakte Marathon. Listed by Running Guy (Garden Route races dashboard).",lat=-33.9249,lng=18.4241,geo_source="town centroid",alt_sources=["https://dash.streblainnovations.com/races/"],_img="https://static.wixstatic.com/media/1576ea_decfb2ed86c14c9cadafa9325df39a92%7Emv2.jpg")
add(title="NMB 1City Marathon (42.2 / 21.1 / 10 / 5 km)",category="funrun",start_date="2026-12-06",town="Gqeberha",venue="Baywest Mall",venue_address="Baywest Mall, Gqeberha",price_from="",ticket_url="",source_url="https://runningcalendar.co.za/events/nmb-1-city-marathon/2026",source_name="RunningCalendar.co.za",notes="EP Athletics Comrades & Two Oceans qualifier from Baywest Mall. Marathon and half listed as free; 10/5 km R50. Entries via Webtickets. Strong PE destination race. Price hint from Running Guy (unverified): R50; r 21; r 10 — confirm on the entry page. Listed by Running Guy (Garden Route races dashboard).",lat=-33.9519318,lng=25.4606019,geo_source="nominatim",alt_sources=["https://dash.streblainnovations.com/races/"])
add(title="Central Athletics 10 km Nature Run (10 km & 5 km)",category="funrun",start_date="2026-12-20",town="Cape Town",venue="False Bay Nature Reserve (Zeekoevlei)",venue_address="Zeekoevlei, Cape Town",price_from="",ticket_url="",source_url="https://runningcalendar.co.za/events/central-athletics-nature-run",source_name="RunningCalendar.co.za",notes="False Bay Nature Reserve. Flat reserve roads. Cape Town holiday 10 km. Date/venue confirmed; fees not yet published. Listed by Running Guy (Garden Route races dashboard).",lat=-34.0620199,lng=18.508325,geo_source="nominatim",alt_sources=["https://dash.streblainnovations.com/races/"])
add(title="First Choice Race, Jeffreys Bay (21.1 / 10 / 5 km)",category="funrun",start_date="2027-01-02",town="Jeffreys Bay",venue="Jeffreys Bay",venue_address="Jeffreys Bay",price_from="",ticket_url="https://racepass.com/za/races/first-choice-race",source_url="https://racepass.com/za/races/first-choice-race",source_name="RacePass",notes="Date is provisional (Running Guy estimate — often from the prior year); confirm before travelling. Holiday coastal race in JBay. ~2.5h east of George. Confirm 2027 listing before planning. Traditionally early January in JBay (2025 was 4 Jan). 2027 date not confirmed. Listed by Running Guy (Garden Route races dashboard).",alt_sources=["https://dash.streblainnovations.com/races/"])
add(title="Balwin Sport Peninsula Marathon (42.2 km & 21.1 km)",category="funrun",start_date="2027-02-21",town="Cape Town",venue="Simon's Town / False Bay coastline",venue_address="Simon's Town, Cape Town",price_from="",ticket_url="",source_url="https://runningcalendar.co.za/events/cape-peninsula-marathon",source_name="RunningCalendar.co.za",notes="Date is provisional (Running Guy estimate — often from the prior year); confirm before travelling. Point-to-point along the False Bay coastline. One of SA's most scenic road marathons. Confirm official 2027 date with Celtic Harriers. Celtic Harriers / RunningCalendar list ~21 Feb 2027. Some third-party sites said 14 Feb — treat as unconfirmed late-February. Listed by Running Guy (Garden Route races dashboard).",lat=-34.193181,lng=18.433266,geo_source="nominatim",alt_sources=["https://dash.streblainnovations.com/races/"])
add(title="Hermanus Trail Run (35 / 25 / 15 km + 18 km beach)",category="funrun",start_date="2027-02-26",end_date="2027-02-28",town="Hermanus",venue="Fernkloof Nature Reserve / Walker Bay",venue_address="Fernkloof Nature Reserve, Hermanus",price_from="",ticket_url="https://energyevents.co.za/hermanus-trail-run/",source_url="https://energyevents.co.za/hermanus-trail-run/",source_name="Energy Events (official site)",notes="Energy Events: Sat Fernkloof Nature Reserve (35/25/15 km, up to 1,500 m), Sun Walker Bay 18 km beach. Compulsory kit. Whale-coast trails. ~4h from George / easy Overberg weekend. Listed by Running Guy (Garden Route races dashboard).",lat=-34.3913049,lng=19.2797882,geo_source="nominatim",alt_sources=["https://dash.streblainnovations.com/races/"],_img="https://energyevents.co.za/wp-content/uploads/2026/07/BRAND-NEW-600-x-400-px-6.png")

# ---------------- Plett venues: Barrington's, Stanley Island, Slops (added 7 Oct 2026) ----------------
BAR=dict(town="Plettenberg Bay",venue="Barrington's",venue_address="Piesang Valley Road, Plettenberg Bay",source_name="Barrington's (official site)")
add(title="Barrington's Oktoberfest 2026",category="festival",start_date="2026-10-31",time="",price_from="",ticket_url="https://account.dineplan.com/widgetframe/HFBQCc9v?date=2026-10-31",source_url="https://www.barringtonsplett.co.za/events-news/",alt_sources=["https://www.barringtonsplett.co.za/oktoberfest-25/"],notes="Second Barrington's Oktoberfest; tickets live via the venue's booking page. 2025 edition had live bands, Barrington's brews on tap and German fare.",**BAR)
add(title="Barrington's Wine Festival 2026",category="festival",start_date="2026-12-16",time="",price_from="",ticket_url="",source_url="https://www.barringtonsplett.co.za/barringtons-wine-festival-25/",alt_sources=[],notes="Save-the-date announced by Barrington's (9th edition). 2025 had 20 SA estates, 100+ wines and live jazz; tickets not yet listed.",**BAR)
add(title="New Year's Eve at Barrington's (DJ Mike)",category="restaurant",start_date="2026-12-31",time="",price_from="",ticket_url="https://calendar.dineplan.com/HFBQCc9v/guests?guests=1&date=2026-12-31",source_url="https://www.barringtonsplett.co.za/events-news/",alt_sources=[],notes="NYE party with DJ Mike and bubbly; book via Dineplan.",**BAR)
add(title="Paradisco – On The Island",category="festival",start_date="2026-12-27",time="12:00-21:00",town="Plettenberg Bay",venue="Stanley Island",venue_address="Stanley Island, Keurbooms River, Plettenberg Bay",price_from="",ticket_url="",source_url="https://allevents.in/plettenberg-bay/paradisco-on-the-island-27-december-2026/80002348646276",source_name="AllEvents (organiser: Anything Goes)",alt_sources=[],notes="Disco party on Stanley Island by Anything Goes. Tickets & tables 'coming soon'. Listing shows both 12:00 and 14:00 start.")
occ=[d for d in _dates("2026-11-01",HORIZON,[4]) if int(d[8:])<=7]
add(title="First Fridays at Slops (monthly)",category="restaurant",start_date=occ[0],end_date=occ[-1],occurrences=occ,recurrence="First Friday of every month",time="",town="Plettenberg Bay",venue="Slops Plett",venue_address="Shop 5, Melville's Centre, 9 Main Street, Plettenberg Bay",price_from="Free entry",ticket_url="",source_url="https://plettrestaurants.com/2026/03/05/slops-plett-3/",source_name="Plett Restaurants",alt_sources=["https://www.foodyas.com/ZA/Plettenberg-Bay/262885126912508/SLOPS--Plett"],notes="10% off food & drinks bill and merch, DJ all night, free kiddies margarita pizza for under-12s. Announced as every month from March 2026; later dates follow that pattern and aren't individually confirmed.")

# ---------------- Knysna December (added 7 Oct 2026) ----------------
add(title="Kevin Fraser – DECADANCE comedy tour, live in Knysna",category="musical",start_date="2026-12-12",time="Doors 18:00, show 20:00",town="Knysna",venue="34 Waenhout – Live Venue",venue_address="11 Hadeda St, Knysna Industrial, Knysna",price_from="",ticket_url="https://kevinfraserofficial.com/worlds/stage",source_url="https://34waenhout.co.za/upcoming-events/",source_name="34 Waenhout (official site)",alt_sources=["https://kevinfraserofficial.com/worlds/stage","https://allevents.in/knysna/kevin-fraser-live-in-knysna-2026/200030644166524"],notes="Stand-up comedy: 10 years of Kevin Fraser. Tickets via kevinfraserofficial.com.")
add(title="MATTHEW MOLE live in Knysna",category="concert",start_date="2026-12-22",time="15:00 (gates 13:30)",town="Knysna",venue="Blend Country Restaurant & Pub",venue_address="George Rex Dr, Knysna",price_from="R320",ticket_url="https://www.quicket.co.za/events/401549-matthew-mole-live-in-knysna/",source_url="https://www.quicket.co.za/events/401549-matthew-mole-live-in-knysna/",source_name="Quicket",alt_sources=[],notes="Phase 1 R320 until 22 Nov, Phase 2 R360, gate R400. Kids 5 and under free.")

# ---------------- George (added 7 Oct 2026) ----------------
add(title="Cula presents David vs Goliath – Ultimate Wine Battle (Cederberg vs De Grendel)",category="restaurant",start_date="2026-10-14",time="",town="George",venue="Cula Restaurant & Bar",venue_address="Shop 22, Outeniqua Village, Saint George's Rd, George",price_from="R695",ticket_url="https://cula.co.za/reservations/",source_url="https://www.cula.co.za/",source_name="Cula (official site, specials poster)",alt_sources=[],notes="Wine pairing evening with David Nieuwoudt (Cederberg) and Charles Hopkins (De Grendel). R695 pp. Book: 044 630 0701 / reservations@cula.co.za. Start time not published.")

# ---------------- Wilderness: Beach House (added 7 Oct 2026) ----------------
BH=dict(town="Wilderness",venue="Beach House Bar & Kitchen (Wilderness Beach House Backpackers)",venue_address="Sands Road, Leentjiesklip, Wilderness",price_from="Free entry",ticket_url="",source_name="Wilderness Beach House (official site)")
occ=_dates("2026-10-11",HORIZON,{SUN})
add(title="Sunday Sessions – live music at Beach House Wilderness",category="concert",start_date=occ[0],end_date=occ[-1],occurrences=occ,recurrence="Every Sunday, 15:00-18:00",time="15:00-18:00",source_url="https://wildernessbeachhouse.com/live-music/",alt_sources=["https://www.toodoo.co.za/sunday-sessions-live-music/"],notes="Local and touring acts on the ocean-view deck, wood-fired pizza. Walk-in only (no table bookings). Weekly series; individual acts for upcoming dates not yet announced.",**BH)
occ=_dates("2026-10-08",HORIZON,{3})
add(title="Open Mic Night at Beach House Wilderness (Thursdays)",category="concert",start_date=occ[0],end_date=occ[-1],occurrences=occ,recurrence="Every Thursday, 18:00-22:00",time="18:00-22:00",source_url="https://wildernessbeachhouse.com/bar-kitchen/",alt_sources=["https://wildernessbeachhouse.com/"],notes="Run with One Two Sound Solutions; sign up at the bar from 18:00, house PA and amps available.",**BH)

# ---------------- Venue sweep 7 Oct 2026: new Quicket listings (Garden Route) ----------------
QU="https://www.quicket.co.za/events/"
BB=dict(town="Mossel Bay",venue="The Beach Bar",venue_address="26 Beach East Boulevard, Die Voor Bay, Mossel Bay",source_name="Quicket",alt_sources=[])
add(title="REAL NICE presents HIGH TIDE (KLINX)",category="concert",start_date="2026-12-04",time="18:00-00:00",price_from="R80",ticket_url=QU+"401475-real-nice-presents-high-tide/",source_url=QU+"401475-real-nice-presents-high-tide/",notes="House/Afro house DJ night opening the REAL NICE summer. 18+, cashless.",**BB)
add(title="REAL NICE presents DAY DREAMING",category="concert",start_date="2026-12-11",time="18:00-00:00",price_from="R80",ticket_url=QU+"401479-real-nice-presents-day-dreaming/",source_url=QU+"401479-real-nice-presents-day-dreaming/",notes="Warm-up party with REAL NICE resident DJs. 18+.",**BB)
add(title="REAL NICE presents MOSSEL-BIZA (SICKLUV)",category="festival",start_date="2026-12-12",time="14:00-00:00",price_from="R120",ticket_url=QU+"401482-real-nice-presents-mossel-biza/",source_url=QU+"401482-real-nice-presents-mossel-biza/",notes="Main REAL NICE summer event: 2 dancefloors, 6 DJs. 18+.",**BB)
add(title="Groove Ritual & Friends – Outdoor Edition",category="concert",start_date="2026-11-08",time="13:00",town="Mossel Bay",venue="Tau Lifestyle Cafe (TLC)",venue_address="Crotz Road, Asla, Mossel Bay",price_from="R60",ticket_url=QU+"400787-groove-ritual-and-friendsoutdoor-edition/",source_url=QU+"400787-groove-ritual-and-friendsoutdoor-edition/",source_name="Quicket",alt_sources=[],notes="Outdoor DJ day (DJ Ermy headlining). Pre-sale R60, gate R80. Denim & white theme.")
add(title="Vinyl Krispies – Bassline Society rooftop session",category="concert",start_date="2026-11-28",time="12:00-21:00",town="Sedgefield",venue="Pili Pili Sedgefield",venue_address="2 Claude Urban Drive, Myoli Beach, Sedgefield",price_from="R100",ticket_url=QU+"400823-vinyl-krispies-pili-pili-sedgefield/",source_url=QU+"400823-vinyl-krispies-pili-pili-sedgefield/",source_name="Quicket",alt_sources=[],notes="Vinyl house music on the Pili Pili rooftop. Pre-sold tickets only, no door sales.")
add(title="Andrew Young Picnic Concert",category="concert",start_date="2027-01-17",time="15:30",town="Wilderness",venue="Fairy Knowe Hotel",venue_address="1 Dumbleton Road, Wilderness",price_from="",ticket_url=QU+"399052-andrew-young-picnic-concert/",source_url=QU+"399052-andrew-young-picnic-concert/",source_name="Quicket",alt_sources=[],notes="Saxophonist Andrew Young in the hotel gardens; bring a picnic.")

# ---------------- GTR (Garden Route Trail Running) weekly runs + padel/paddling (added 7 Oct 2026) ----------------
GTR="https://gtrtrails.run/gtr-runs/"
occ=_dates("2026-10-12",HORIZON,[0])
add(title="GTR Monday Social Trail Run (~8 km)",category="funrun",start_date=occ[0],end_date=occ[-1],occurrences=occ,recurrence="Every Monday, 17:40",time="17:40",town="George",venue="Garden Route Trail Running (route varies)",venue_address="George (route posted on GTR WhatsApp group before 12:00 on the day)",price_from="",ticket_url="",source_url=GTR+"monday-social-runs/",source_name="GTR (official site)",alt_sources=["https://www.strava.com/clubs/GTRtrails"],notes="Social group trail run, ~8 km circular, 1-2 h; nobody left behind. Route & start announced on the GTR WhatsApp group. Dogs on leash. No cost published.")
occ=_dates("2026-10-08",HORIZON,[3])
add(title="GTR Thursday Time Trial (5 km / 3 km trail)",category="funrun",start_date=occ[0],end_date=occ[-1],occurrences=occ,recurrence="Every Thursday, runners 17:30 / walkers 17:15",time="17:30 (walkers 17:15)",town="George",venue="Camphersdrift Road (in the dip)",venue_address="Camphersdrift Road, George",price_from="",ticket_url="",source_url=GTR+"thursday-gtr-time-trial/",source_name="GTR (official site)",alt_sources=["https://www.strava.com/clubs/GTRtrails"],notes="Weekly time trial, rain or shine. Join the GTR Strava club; first-timers get a number via 081 366 4394. Site also lists a 5 km Garden Route Dam route. Dogs on leash; kids under 12 accompanied. No cost published.")
occ=_dates("2026-10-13",HORIZON,[1])
add(title="GTR Tuesday Time Trial Mossel Bay (5 km / 3 km)",category="funrun",start_date=occ[0],end_date=occ[-1],occurrences=occ,recurrence="Every Tuesday, runners 17:30 / walkers 17:15",time="17:30 (walkers 17:15)",town="Mossel Bay",venue="Mossel Bay Sports Ground (Bruns Street entrance)",venue_address="Bruns Street, Mossel Bay",price_from="",ticket_url="",source_url="https://www.strava.com/clubs/GTRtrails",source_name="GTR club page on Strava (official)",alt_sources=[],notes="Listed on GTR's official Strava club page; not on the GTR website itself.")
# Padel
for d1,d2,div in [("2026-10-09","2026-10-11","age-group divisions"),("2026-10-16","2026-10-18","Open Division")]:
    add(title=f"Growthpoint SA National Padel Championships 2026 – {div}",category="sport",start_date=d1,end_date=d2,time="",town="Cape Town",venue="Padel365 Century City & Padel365 Richmond Park",venue_address="Century City, Cape Town",price_from="",ticket_url="",source_url="https://ctnews.co.za/south-africas-first-padel-nationals-coming-to-cape-town-with-r125000-prize-pool/",source_name="CT News",alt_sources=["https://everydaymzansi.co.za/padel-nationals-south-africa-2026/"],notes="Padel (racket sport): South Africa's first official national padel championships, R125,000 prize pool, organised by Padel365 with SAPA. Spectator/entry details not published.")
# Paddling
add(title="Cape Point Challenge 2026 – 52 km surfski race",category="sport",start_date="2026-12-19",end_date="2026-12-20",time="",town="Cape Town",venue="Scarborough/Witsand → Fish Hoek Beach",venue_address="Fish Hoek Beach, Cape Town",price_from="",ticket_url="https://capepointchallenge.com/",source_url="https://capepointchallenge.com/",source_name="Cape Point Challenge (official site)",alt_sources=[],notes="Paddling (surfski) race around Cape Point; race weekend 19/20 Dec (date set by conditions).")

# ---------------- MUT – Mountain Ultra Trail by UTMB (added 7 Oct 2026) ----------------
add(title="MUT – Mountain Ultra Trail by UTMB (163 / 98 / 58 / 44 / 25 / 11 km)",category="funrun",start_date="2027-05-28",end_date="2027-05-30",time="Miler Fri 12:00; MUT 100 Sat 05:00",town="George",venue="Outeniqua Park Stadium",venue_address="Outeniqua Park Stadium, George",price_from="",ticket_url="https://mut.utmb.world/registration",source_url="https://mut.utmb.world/races/mut100",source_name="MUT by UTMB (official site)",alt_sources=["https://mut.utmb.world/registration"],notes="Start/finish at Outeniqua Park Stadium. Miler (163 km) Fri 28 May 12:00; MUT 100 (98 km) Sat 29 May 05:00; MUT 60 and Marathon on Saturday; Challenge & Lite on Sun 30 May, starting at the Trail Kiosk. Registration open until 15 May 2027 or sold out.")

# ---------------- 2027 beyond February (Quicket sweep 7 Oct 2026) ----------------
QU="https://www.quicket.co.za/events/"
MV=dict(town="Cape Town",venue="Maynardville Open-Air Theatre",venue_address="Maynardville Park, Piers Rd, Wynberg, Cape Town",source_name="Quicket",alt_sources=[])
add(title="Maynardville 2027: Shakespeare's Macbeth",category="musical",start_date="2027-02-05",end_date="2027-03-13",time="20:15",price_from="R213",ticket_url=QU+"381057-maynardville-2027-shakespeares-macbeth/",source_url=QU+"381057-maynardville-2027-shakespeares-macbeth/",notes="Open-air Shakespeare (theatre, not a musical). Price as shown on Quicket.",**MV)
add(title="Maynardville 2027: Cape Town Opera – Vienna in the Park",category="concert",start_date="2027-03-07",end_date="2027-03-14",time="18:30",price_from="R298",ticket_url=QU+"382437-maynardville-2027-cape-town-opera-vienna-in-the-park/",source_url=QU+"382437-maynardville-2027-cape-town-opera-vienna-in-the-park/",**MV)
add(title="André & Tiaan – Vat My Saam",category="concert",start_date="2027-03-06",end_date="2027-03-07",time="19:00",town="Cape Town",venue="Ou Skip Holiday Resort",venue_address="1 Ou Skip Street, Melkbosstrand",price_from="R100",ticket_url=QU+"379665-andr-tiaan-vat-my-saam/",source_url=QU+"379665-andr-tiaan-vat-my-saam/",source_name="Quicket",alt_sources=[])
add(title="Anacy LIVE! at Café Roux",category="concert",start_date="2027-03-18",time="18:00",town="Cape Town",venue="Cafe Roux",venue_address="Chapmans Peak Dr, Noordhoek",price_from="R120",ticket_url=QU+"398685-anacy-live-caf-roux/",source_url=QU+"398685-anacy-live-caf-roux/",source_name="Quicket",alt_sources=[])
add(title="Cape Town Camerata Easter Concert",category="concert",start_date="2027-04-11",time="16:00",town="Cape Town",venue="Cape Town City Hall",venue_address="Darling Street, Cape Town City Centre",price_from="R120",ticket_url=QU+"393957-cape-town-camerata-easter-concert-at-the-cape-town-city-hall/",source_url=QU+"393957-cape-town-camerata-easter-concert-at-the-cape-town-city-hall/",source_name="Quicket",alt_sources=[])
add(title="Anna Davel – DIAMONDS: A Shirley Bassey Tribute",category="concert",start_date="2027-04-30",time="19:00",town="Jeffreys Bay",venue="Oase JBay (AGS)",venue_address="Dolly Varden Street, C-Place, Jeffreys Bay",price_from="R150",ticket_url=QU+"399102-anna-davel-diamonds-a-shirley-bassey-tribute/",source_url=QU+"399102-anna-davel-diamonds-a-shirley-bassey-tribute/",source_name="Quicket",alt_sources=[])
add(title="Totalsports Two Oceans Trail Run (24 / 18 / 12 km)",category="funrun",start_date="2027-04-02",time="24 km 07:00, 18 km 08:00, 12 km 08:30",town="Cape Town",venue="UCT Rugby Fields",venue_address="UCT Upper Campus, Rondebosch, Cape Town",price_from="R550",ticket_url="https://www.twooceansmarathon.org.za/",source_url="https://www.twooceansmarathon.org.za/qualifying-and-seeding-dates-confirmed-for-totalsports-two-oceans-marathon-powered-by-byd/",source_name="Two Oceans Marathon (official site)",alt_sources=["https://marathontours.com/en-gb/events/two-oceans-marathon/"],notes="Part of Two Oceans Event Week (31 Mar-4 Apr 2027). SA entry: 24 km R950, 18 km R750, 12 km R550. Entries open; capacity 1,500. Start times per Marathon Tours.")
add(title="Up The Creek Music Festival 2027",category="festival",start_date="2027-02-11",end_date="2027-02-14",time="",town="Swellendam",venue="Up the Creek venue camp (Breede River)",venue_address="Breede River, near Swellendam",price_from="R1,705",ticket_url="https://utc.howler.co.za/events/up-the-creek-music-festival-2027-d4d7",source_url="https://utc.howler.co.za/events/up-the-creek-music-festival-2027-d4d7",source_name="Howler",alt_sources=["https://www.upthecreek.co.za"],notes="Riverside camping music festival: 4 stages, 50+ bands. 18+. From R1,705 (Patron and Early tiers sold out).",lat=-34.1785,lng=20.4900,geo_source="event page")

# ---------------- Outeniqua Powervan (George) & Powervan Mossel Bay / ex Diaz Express (added 8 Oct 2026) ----------------
PVG="https://www.powervan.co.za/index.php/george/"; PVM="https://www.powervan.co.za/index.php/mosselbay/"
_all=_dates("2026-10-08",HORIZON,[0,1,2,3,4,5])
_sum=lambda d: not ("05"<=d[5:7]<="08")   # 1 Sep - 30 Apr timetable
PVGD=dict(town="George",venue="Outeniqua Transport Museum (Powervan George)",venue_address="2 Mission Road, George",price_from="R250 (child R220)",ticket_url=PVG,source_url=PVG,source_name="Outeniqua Powervan (official site)",alt_sources=["https://visitgeorge.co.za/directory/outeniqua-power-van/"])
_n="Rail-trolley trip up the Outeniqua Mountains to 'Topping' and back, ~2.5 h incl. ~30 min picnic stop at Power (bring a picnic). Bookings essential; report 30 min before departure. Fares R250 adult / R220 child 3-15 (valid 1 May-30 Nov 2026; later fares not yet published). Wednesday pensioner discount (not in school holidays). Public holidays use Saturday times. Departure point was temporarily moved to George Station during the 2026 museum closure - confirm when booking. WhatsApp 082 490 5627."
for wd,lab,tS,tW in [([0,1,2,3,4],"Mon-Fri","09:00 & 12:00","09:30 & 12:30"),([5],"Saturdays","08:30, 09:00, 12:00 & 12:30","09:00, 09:30, 12:30 & 13:00")]:
    for summer,t,season in [(True,tS,"1 Sep-30 Apr"),(False,tW,"1 May-31 Aug")]:
        occ=[d for d in _all if _dt.date.fromisoformat(d).weekday() in wd and _sum(d)==summer]
        if not occ: continue
        add(title=f"Outeniqua Powervan mountain rail trip, George ({lab})",category="nature",start_date=occ[0],end_date=occ[-1],occurrences=occ,recurrence=f"{lab}, departures {t} ({season} timetable)",time=t,notes=_n,**PVGD)
PVMD=dict(town="Hartenbos",venue="Hartenbos Station (Powervan Mossel Bay, ex Diaz Express)",venue_address="Port Natal Avenue, Hartenbos",ticket_url=PVM,source_url=PVM,source_name="Outeniqua Powervan – Mossel Bay (official site)",alt_sources=["https://www.transplo.com/ZA/Hartenbos/775998325815871/Diaz-Express"])
_m="Rail-trolley excursion Hartenbos → Glentana / Great Brak along the coast, ~2.5 h. Bookings close at midnight the day before. Times are from Powervan Mossel Bay's Facebook posts (the website gives days and fares only). Its posts say trips run all year except the December school holidays - check before booking. Pensioner (Wed) and ATKV-guest rates R220. Tel 083 260 5716 / 082 450 7778."
occ=_dates("2026-10-08",HORIZON,[0,2,4])
add(title="Powervan Mossel Bay breakfast/lunch rail excursion (Hartenbos → Glentana)",category="nature",start_date=occ[0],end_date=occ[-1],occurrences=occ,recurrence="Mon, Wed & Fri: breakfast 08:30 (lunch trip time not published)",time="08:30 (breakfast trip)",price_from="R250 (child R220)",notes="Breakfast at Seeplaas; lunch at Santos Express from 1 Oct 2026. "+_m,**PVMD)
occ=_dates("2026-10-08",HORIZON,[1,3,5])
add(title="Powervan Mossel Bay picnic rail trip (Hartenbos → Glentana)",category="nature",start_date=occ[0],end_date=occ[-1],occurrences=occ,recurrence="Tue, Thu & Sat: 09:00, 12:00 & 15:00",time="09:00, 12:00 & 15:00",price_from="R250 (child R220)",notes=_m,**PVMD)

# ---------------- Stock car / oval dirt racing + George Showgrounds (added 7 Oct 2026) ----------------
_MSA="https://www.motorsport.co.za/wp-content/uploads/2026/10/2026-MSA-Annual-Events-Calendar-01.10.2026.pdf"
add(title="George Motor Club: Champion of Champions – WC Regional & club oval dirt (stock car) championships",category="sport",
    start_date="2026-12-18",end_date="2026-12-19",time="17:00-23:00",town="George",venue="George Motor Club oval track, George Showgrounds",
    venue_address="George Showgrounds, R102 (Old Airport Road), Groeneweide Park, George",price_from="",
    ticket_url="https://georgemotorclub.racing/race-calendar/",
    source_url="https://www.motorsport.co.za/event/wc-regional-george-mc-club-oval-dirt-championships-champion-of-champions/",source_name="Motorsport South Africa",
    alt_sources=[_MSA,"https://georgemotorclub.racing/race-calendar/","https://www.motorsport.co.za/venue/george-showgrounds-george/"],
    notes="Stock car oval dirt racing, WC regional & George MC club championships. Times 17:00-23:00 from the MSA 2026 events calendar (01.10.2026). Spectator prices for 2026 not yet published for this meeting (earlier 2026 George MC meetings: adults R100, kids under 12 R50). Info: Antoinette 073 455 8944, georgemotorklub@gmail.com.")
for _d,_n in [("2026-10-31","Sat 31 Oct. The MSA PDF calendar (01.10.2026) lists the venue as 'Redrock Raceway, Oudtshoorn'; the MSA event page says Arnold de Jager Oval Track, so check with the club before going."),
              ("2026-11-29","Listed as Sunday 29 Nov on MSA.")]:
    add(title="Oudtshoorn Motor Club – WC Regional & club oval dirt (stock car) championships",category="sport",
        start_date=_d,time="17:00-23:00",town="Oudtshoorn",venue="Arnold de Jager Oval Track",venue_address="Arnold de Jager Oval Track, Oudtshoorn",price_from="",
        ticket_url="",source_url="https://www.motorsport.co.za/event/wc-regional-oudtshoorn-motor-club-oval-dirt-championships-"+("3/" if _d<"2026-11" else "4/"),
        source_name="Motorsport South Africa",alt_sources=[_MSA,"https://www.motorsport.co.za/organizer/do4sa-oudts/"],
        notes="Stock car oval dirt racing. Times 17:00-23:00 from the MSA 2026 events calendar. "+_n+" Organiser: Oudtshoorn Motor Club (Ina Barnard 082 829 1090, secretaryodnmc@gmail.com). Spectator prices not published.")
add(title="George Agricultural Show 2027 (George Landbouskou)",category="festival",start_date="2027-08-26",end_date="2027-08-28",time="",
    town="George",venue="George Showgrounds",venue_address="George Skougronde, R102, Groeneweide Park, George",price_from="",
    ticket_url="https://georgelandbouskou.co.za/",source_url="https://georgelandbouskou.co.za/",source_name="George Landbouskou (official)",
    notes="Annual agricultural show by the Outeniqua Agricultural Society: livestock, equestrian, machinery, crafts, food, music and sport. 2027 dates are from the official site; programme and tickets not yet published. Info: 044 873 4165, info@georgelandbouskou.co.za.")

# ---------------- KKNK 2027 (added 8 Oct 2026) ----------------
add(title="KKNK 2027 – Klein Karoo Nasionale Kunstefees (31st edition)",category="festival",start_date="2027-03-23",end_date="2027-03-27",time="",
    town="Oudtshoorn",venue="KKNK festival venues across Oudtshoorn",venue_address="KKNK office: 217 Jan van Riebeeck Road, Oudtshoorn",price_from="",
    ticket_url="https://www.kknk.co.za/",source_url="https://www.kknk.co.za/en/kknk-programaansoeke/",source_name="KKNK (official site)",
    alt_sources=["https://www.kknk.co.za/en/","https://www.kknk.co.za/kknk-programaansoeke/"],
    notes="South Africa's biggest Afrikaans arts festival: theatre, music, visual art, family entertainment and the free Kuierkol. The 31st KKNK runs Tue 23 to Sat 27 Mar 2027, five days (2026 ran eight days). Programme, prices and tickets not yet published (checked 8 Oct 2026). Info: 044 203 8600, info@kunste.org.za.")

# ---------------- Mossel Bay clubs / nightlife (added 8 Oct 2026) ----------------
# Sky Lounge karaoke: weekly Sunday series on the Visit Mossel Bay calendar (dates listed there 11 Oct 2026 - 28 Feb 2027).
occ=[d for d in _dates("2026-10-11","2027-02-28",[SUN])]
add(title="Karaoke Night @ Sky Lounge (DJ Melly D & DJ KCG)",category="concert",start_date=occ[0],end_date=occ[-1],occurrences=occ,
    recurrence="Every Sunday, 18:00-23:30",time="18:00-23:30",town="Mossel Bay",venue="Sky Lounge",
    venue_address="29 Essenhout Street, Heiderand, Mossel Bay",price_from="",ticket_url="",
    source_url=MB+"karaoke-night-sky-lounge-2/2026-10-11/",source_name="Visit Mossel Bay (tourism calendar)",
    notes="Karaoke with DJs. No under-18s, no boot parties. Weekly dates are listed on Visit Mossel Bay to 28 Feb 2027. The venue street address comes from directory listings (the tourism listing says only 'Mossel Bay'). Info: 079 508 2412.")
add(title="AMA-1K Comedy Night (Vusi Oulik, Phanjile, Lukhanyo, Dabane; host Moola)",category="arts",start_date="2026-10-30",time="18:00",
    town="Mossel Bay",venue="Bravo Lounge, Garden Route Casino",venue_address="1 Pinnacle Point Road, Mossel Bay",price_from="R150",
    ticket_url="https://www.webtickets.co.za/v2/event.aspx?itemid=1602614247",source_url="https://www.webtickets.co.za/v2/event.aspx?itemid=1602614247",
    source_name="Webtickets",notes="South African stand-up comedy night in the casino's entertainment lounge. Tickets via Webtickets / Pick n Pay.")
add(title="Chapter One – Day One live music experience",category="concert",start_date="2026-11-08",time="18:00-21:00",
    town="Mossel Bay",venue="Bravo Lounge, Garden Route Casino",venue_address="1 Pinnacle Point Road, Mossel Bay",price_from="",ticket_url="",
    source_url=MB+"chapter-one/",source_name="Visit Mossel Bay (tourism calendar)",
    notes="Day One's first live-music show in Mossel Bay: independent South African artists with live performances, artist stories and audience interaction, plus an online stream. Organiser Day One: 061 292 3810. Venue: 044 606 7777.")

# ---------------- Listing sites sweep (8 Oct 2026): gardenroute.com/event, gardenrouteguide.co.za, visitmosselbay.co.za/events, ontheroute.co.za ----------------
GRC="https://www.gardenroute.com/"
GRG="https://www.gardenrouteguide.co.za/garden-route-events/"
OTR8="https://www.ontheroute.co.za/your-garden-route-event-guide-8-october/"
_S_GRC="GardenRoute.com (events listing)"; _S_MB="Visit Mossel Bay (tourism calendar)"; _S_OTR="On The Route (Garden Route event guide)"; _S_GRG="Garden Route Guide (events page)"
# --- one-off events ---
add(title="Atlantic Rail Trip – SC Rail steam train 'Sylvia' (Hartenbos → Santos)",category="nature",start_date="2026-10-09",time="09:00 and 12:00 departures",
    town="Hartenbos",venue="Hartenbos old train station (Hennie's)",venue_address="Port Natal Avenue, Hartenbos",price_from="R195",ticket_url="https://scrail.co.za/list-view/",
    source_url=MB+"atlantic-rail-trip-11/2026-10-09/1/",source_name=_S_MB,alt_sources=["https://scrail.co.za/list-view/"],notes="Coastal steam-train trip along the bay. Two departures. Book via SC Rail.")
add(title="Blithe Spirit (Noël Coward comedy)",category="arts",start_date="2026-10-06",end_date="2026-10-10",time="19:30",town="Plettenberg Bay",venue="St Peter's Church",
    venue_address="Church Street, Plettenberg Bay",price_from="R350",ticket_url="",source_url=OTR8,source_name=_S_OTR,alt_sources=[OTR],notes="Nightly 6-10 Oct. Tickets at Barney's Kiosk or Quicket.")
add(title="Southern Cape Coin Show",category="community",start_date="2026-10-10",time="10:00-16:00",town="Mossel Bay",venue="Bahia Bleu",venue_address="Diaz Beach, Mossel Bay",
    price_from="",ticket_url="",source_url=MB+"southern-cape-coin-show/",source_name=_S_MB,alt_sources=[OTR8],notes="Mossel Bay's first coin show: dealer tables, displays and free valuations.")
add(title="Country Sokkie Evening at La Bosca",category="concert",start_date="2026-10-10",time="19:00-23:00",town="Sedgefield",venue="La Bosca, Luna Verde Farm",
    venue_address="Barrington Road, Sedgefield",price_from="R80",ticket_url="",source_url=OTR8,source_name=_S_OTR,alt_sources=[OTR],notes="Country sokkie dance night on the farm. R80 adults, R40 children 6-12.")
add(title="Garden Route Armwrestling Tournament",category="sport",start_date="2026-10-10",time="Weigh-ins from 08:30, tournament 10:00",town="Klein Brak",
    venue="Mooiuitsig Restaurant, Brinkley's River Village",venue_address="1 Old George Road, Klein Brak River",price_from="R100",ticket_url="",source_url=OTR8,source_name=_S_OTR,
    alt_sources=[OTR],notes="Entry R100/R150 per competitor; spectators R100.")
add(title="MRC Rugby Expo",category="sport",start_date="2026-10-10",end_date="2026-10-11",time="From 09:00",town="George",venue="Pacaltsdorp Sportgronde",
    venue_address="66 Olympic Street, Pacaltsdorp, George",price_from="R50",ticket_url="",source_url=OTR8,source_name=_S_OTR,notes="Two-day rugby expo. R50 adults.")
add(title="Wilderness Chess Club Freestyle Chess960 Tournament",category="sport",start_date="2026-10-11",time="",town="Wilderness",venue="Fairy Knowe Hotel",
    venue_address="1 Dumbleton Road, Wilderness",price_from="R200",ticket_url="https://www.toodoo.co.za/wilderness-chess960/",source_url="https://www.toodoo.co.za/wilderness-chess960/",
    source_name="toodoo.co.za",alt_sources=[GRC+"wilderness-chess-club-freestyle-chess960-tournament-from-11th-oct-2026-till_event_op_view_id_3932",OTR8],
    notes="Five-round unrated Chess960 tournament, 25 min + 5 s. Registration closes 23:59 Thu 8 Oct (or when full).")
add(title="Studietrust Gholfdag (golf day)",category="sport",start_date="2026-10-16",time="11:00-14:00",town="Mossel Bay",venue="Mossel Bay Golf Club",price_from="",ticket_url="",
    source_url=MB+"studietrust-gholfdag/",source_name=_S_MB,notes="Fundraising golf day for Studietrust.")
for slug,t,d,tm in [("song-sung-blue","Song Sung Blue","2026-10-16","19:00"),("hamnet-at-the-blue-shed","Hamnet","2026-10-23","19:15"),
                    ("beetlejuice","Beetlejuice","2026-10-30","19:15"),("bakgat","Bakgat","2026-11-13","19:30")]:
    add(title=f"Blue Shed spring movies: {t}",category="film",start_date=d,time=tm,town="Mossel Bay",venue="The Blue Shed (Open Plan Pictures)",venue_address="33 Bland Street, Mossel Bay",
        price_from="R100",ticket_url="https://openplanpictures.co.za/",source_url=MB+slug+"/",source_name=_S_MB,alt_sources=["https://openplanpictures.co.za/"]+([OTR8] if slug=="song-sung-blue" else []),
        notes="Indoor film screening in Open Plan Pictures' spring season at the Blue Shed Coffee Roastery.")
add(title="Blue Shed spring movies: The Secret Life of Pets (bring your pet)",category="film",start_date="2026-11-06",time="19:15",town="Mossel Bay",venue="The Blue Shed (Open Plan Pictures)",
    venue_address="33 Bland Street, Mossel Bay",price_from="R100",ticket_url="https://www.quicket.co.za/events/394628/",source_url="https://www.quicket.co.za/events/394628/",source_name="Quicket",
    alt_sources=[MB+"secret-life-of-pets/"],notes="Pet-friendly screening. Date and time per Quicket; Visit Mossel Bay lists Tue 3 Nov 19:30, so check before you go.")
add(title="Prince George Monumental (100-miler trail run)",category="funrun",start_date="2026-10-17",time="",town="Oudtshoorn",venue="Highgate Ostrich Show Farm",price_from="",
    ticket_url="https://www.princegeorge.co.za/",source_url="https://www.princegeorge.co.za/",source_name="Prince George (official site)",alt_sources=[GRG],notes="Ultra trail race (100 miles) in the Klein Karoo.")
add(title="Topper Nationals (sailing)",category="sport",start_date="2026-10-17",end_date="2026-10-18",time="10:00-17:00",town="Mossel Bay",venue="Santos Beach",venue_address="Santos Road, Mossel Bay",
    price_from="",ticket_url="",source_url=MB+"the-topper-nationals-in-mosselbay/2026-10-17/",source_name=_S_MB,alt_sources=[OTR8],notes="National championship for Topper dinghies, hosted with the Mossel Bay Sailing Club / Skipper Foundation. Spectators welcome on the beachfront.")
add(title="Schalk Bezuidenhout: Hey Hey Divorcé at Simola (stand-up comedy)",category="arts",start_date="2026-10-20",time="20:00 (doors 19:00)",town="Knysna",venue="Simola Hotel, Country Club & Spa",
    venue_address="Simola, Knysna",price_from="R300",ticket_url="https://www.quicket.co.za/events/375253-hey-hey-divorce-schalk-bezuidenhout-knysna/",source_url=OTR8,source_name=_S_OTR,alt_sources=["https://www.quicket.co.za/events/375253-hey-hey-divorce-schalk-bezuidenhout-knysna/"],notes="Knysna date of the tour; separate from the 19 Oct Fancourt and 21-23 Oct George shows.")
_fw=["2026-10-23","2026-11-27"]
add(title="Food & Wine Pairing Evening at Chefs Emporium",category="community",start_date=_fw[0],end_date=_fw[-1],occurrences=_fw,recurrence="23 Oct 18:00-20:00; 27 Nov 20:00",
    time="23 Oct 18:00-20:00; 27 Nov 20:00",town="Mossel Bay",venue="Chefs Emporium (Bahia Bleu)",venue_address="1 Beach Road, E Blvd, Diaz Beach, Mossel Bay",price_from="R350",ticket_url="",
    source_url=MB+"food-wine-pairing-evening/",source_name=_S_MB,notes="Paired dinner with Jordan Chameleon wines. Bookings via WhatsApp 063 298 4448.")
add(title="Art Workshop with Maria",category="arts",start_date="2026-10-24",time="09:00-14:00",town="Mossel Bay",venue="House of Maria",venue_address="29 Marsh Street, Mossel Bay",price_from="R3600",
    ticket_url="",source_url=MB+"art-workshop-with-maria-2026/2026-10-24/",source_name=_S_MB,notes="Day-long art workshop.")
add(title="SACBW Gala Awards 2026",category="community",start_date="2026-10-24",time="18:30-22:00",town="Mossel Bay",venue="Diaz Hotel and Resort",venue_address="1 Beach East Blvd, Die Voor Bay, Mossel Bay",
    price_from="",ticket_url="",source_url=MB+"sacbw-gala-awards-2026/",source_name=_S_MB,alt_sources=["https://www.facebook.com/sacbwWC"],notes="SA Council for Business Women gala awards evening. The listing doesn't say whether tickets are public.")
add(title="The Complete Works of William Shakespeare (Abridged)",category="arts",start_date="2026-10-24",end_date="2026-10-25",time="From 15:00",town="Knysna",venue="St George's Anglican Church",
    venue_address="10 Main Road, Knysna",price_from="",ticket_url="https://www.quicket.co.za/events/390568-the-complete-works-of-william-shakespeare-abridged/",
    source_url="https://www.quicket.co.za/events/390568-the-complete-works-of-william-shakespeare-abridged/",source_name="Quicket",
    alt_sources=[GRC+"complete-works-of-william-shakespeare-abridged-from-24th-oct-2026-till-25th-oct-2026_event_op_view_id_3917"],notes="Comedy romp through all of Shakespeare's plays.")
add(title="Night of 1000 Owls – Raptor Rescue art exhibition & fundraiser",category="arts",start_date="2026-10-27",end_date="2026-10-30",time="",town="Plettenberg Bay",venue="The Heath, Harkerville",
    price_from="",ticket_url="",source_url=OTR8,source_name=_S_OTR,notes="Owl-inspired art exhibition and fundraiser for Raptor Rescue, part of the birding festival.")
add(title="Rhodes Dryland Traverse (multi-day trail run)",category="funrun",start_date="2026-10-29",end_date="2026-11-01",time="",town="Oudtshoorn",venue="Cango Caves into the Swartberg",
    price_from="",ticket_url="",source_url=OTR8,source_name=_S_OTR,notes="Multi-day trail run from the Cango Caves into the Swartberg.")
add(title="SA National Criterium Championships (road cycling)",category="sport",start_date="2026-10-30",end_date="2026-11-01",time="",town="George",venue="Cornerstone Lifestyle Centre",
    price_from="",ticket_url="",source_url=OTR8,source_name=_S_OTR,notes="National road-cycling criterium championships.")
add(title="Woord in Waarheid Damestee (ladies' tea)",category="community",start_date="2026-10-31",time="10:00-12:00",town="Mossel Bay",venue="Mossel Bay Town Hall",venue_address="Wassung Street, Mossel Bay",
    price_from="R200",ticket_url="",source_url=MB+"woord-in-waarheid-damestee/",source_name=_S_MB,notes="R200 per person; table of 10 R1,800.")
add(title="Asanda Bam live at The White House Theatre (jazz)",category="concert",start_date="2026-10-31",time="18:00",town="Plettenberg Bay",venue="The White House Theatre",price_from="R250",ticket_url="",
    source_url=GRC+"asanda-bam-at-white-house-theatre-from-31st-oct-2026-till_event_op_view_id_3924",source_name=_S_GRC,notes="Tickets via Quicket or The Old House Shop.")
add(title="Bassline Society – Trick or Treat Halloween party",category="concert",start_date="2026-10-31",time="",town="Wilderness",venue="Beach House Bar & Kitchen (Wilderness Beach House Backpackers)",price_from="R100",ticket_url="",
    source_url=GRC+"bassline-society---trick-or-treat-from-31st-oct-2026-till_event_op_view_id_3922",source_name=_S_GRC,notes="Halloween vinyl house-music party with best-dressed prizes. R100 entry. Line-up and time still to be announced.")
add(title="Dirk van der Westhuizen at ReedValley",category="concert",start_date="2026-11-06",time="20:00",town="Mossel Bay",venue="ReedValley",price_from="",
    ticket_url="https://www.reedvalley.com/ots/order.php?vendor=1&show=902",source_url="https://www.reedvalley.com/ots/order.php?vendor=1&show=902",source_name="ReedValley (tickets)",
    alt_sources=[GRC+"dirk-van-der-westhuizen-by-reedvalley-from-6th-nov-2026-till_event_op_view_id_3952"],notes="Afrikaans party music, his first show at ReedValley. Wine and food on site.")
add(title="A Night of Comedy with Alan Committie",category="arts",start_date="2026-11-07",time="20:00",town="Knysna",venue="Simola Hotel, Country Club & Spa",venue_address="Simola, Knysna",price_from="",
    ticket_url="https://www.quicket.co.za/events/377526-a-night-of-comedy-with-alan-committie-knysna/",source_url="https://www.quicket.co.za/events/377526-a-night-of-comedy-with-alan-committie-knysna/",
    source_name="Quicket",alt_sources=[GRC+"night-of-comedy-with-alan-committie-from-7th-nov-2026-till_event_op_view_id_3919"],notes="All-new stand-up show.")
add(title="Holistic (Wellness) Expo Plettenberg Bay",category="community",start_date="2026-11-07",end_date="2026-11-08",time="",town="Plettenberg Bay",venue="Plettenberg Bay (venue per organiser)",
    price_from="Free entry",ticket_url="",source_url="https://plett.wellnessexpo-sa.co.za/",source_name="Wellness Expo SA",alt_sources=[GRC+"holistic-expo-plettenberg-bay-from-7th-nov-2026-till-8th-nov-2026_event_op_view_id_3898",OTR8],
    notes="Wellness practitioners, healers and makers. First expo outside Mossel Bay. Free for the public.")
add(title="Knysna Extreme Triathlon",category="sport",start_date="2026-11-07",time="",town="Knysna",venue="Knysna estuary and surrounds",price_from="R5750",ticket_url="https://entrytickets.net/knysnaextreme",
    source_url="https://entrytickets.net/knysnaextreme",source_name="Entrytickets",alt_sources=[GRC+"knysna-extreme-triathlon-from-7th-nov-2026-till_event_op_view_id_3827",GRG,OTR8],
    notes="5 km swim, 174 km cycle, 50 km run. Individual entry R5,750; entries close 14 Oct.")
add(title="Rest and Restore – women's retreat",category="community",start_date="2026-11-20",end_date="2026-11-22",time="",town="The Crags",venue="Good Earth Farm",price_from="",ticket_url="",
    source_url=OTR8,source_name=_S_OTR,notes="Three-day women's retreat on a sustainability farm.")
add(title="Dance Through the Decades (Elle Dance Academy)",category="arts",start_date="2026-11-21",end_date="2026-11-22",time="",town="Sedgefield",venue="Elle Dance Academy show (Sedgefield)",price_from="",ticket_url="",
    source_url=GRC+"dance-through-decades-from-21st-nov-2026-till-22nd-nov-2026_event_op_view_id_3930",source_name=_S_GRC,notes="Dance show covering 1960-2010. Times and prices still to be announced. Enquiries: Rezelle 072 381 8720.")
add(title="ISUZU IRONMAN 70.3 Mossel Bay",category="sport",start_date="2026-11-22",time="06:00",town="Mossel Bay",venue="Santos Beach",venue_address="Santos Road, Mossel Bay",price_from="",
    ticket_url="https://www.ironman.com/races/im703-mossel-bay",source_url=MB+"ironman-70-3-mossel-bay/",source_name=_S_MB,alt_sources=["https://www.ironman.com/races/im703-mossel-bay",GRG,OTR8],
    notes="Half-distance triathlon: sea swim, coastal cycle and run through town. Spectating is free.")
add(title="MossJazz Golf Day",category="sport",start_date="2026-11-26",time="08:00",town="Mossel Bay",venue="Pinnacle Point Golf Estate",venue_address="1 Pinnacle Road, Pinnacle Point Estate, Mossel Bay",
    price_from="",ticket_url="",source_url=MB+"mossjazz-golf-day/",source_name=_S_MB,notes="Golf day linked to MosJazz week.")
add(title="Universal Frequencies 2026 (psytrance festival)",category="festival",start_date="2026-11-27",end_date="2026-11-29",time="Fri 12:00 – Sun 18:00",town="Ladismith",venue="Karoo 62 Escape",
    venue_address="Route 62, Ladismith",price_from="",ticket_url="https://www.quicket.co.za/events/342747-universal-frequencies-2026/",source_url="https://www.quicket.co.za/events/342747-universal-frequencies-2026/",
    source_name="Quicket",alt_sources=[GRC+"universal-frequencies-2026-from-27th-nov-2026-till-29th-nov-2026_event_op_view_id_3918"],notes="Psytrance camping festival in aid of Global Reboot. Klein Karoo.")
add(title="Ochre Origins – opening exhibition at Ochre Contemporary (Diane Victor)",category="arts",start_date="2026-12-11",end_date="2026-12-16",time="",town="Mossel Bay",venue="WayOut Studios",
    venue_address="Unit 6&7, Trimenco Park, 11 Parson Lane, Mossel Bay",price_from="",ticket_url="",source_url=MB+"ochre-origins-opening-exhibition-at-ochre-contemporary/",source_name=_S_MB,notes="Opening exhibition of the new Ochre Contemporary gallery.")
for d,town,nm in [("2026-12-14","George","George Street Mile"),("2026-12-16","Oudtshoorn","Klein Karoo Street Mile"),("2026-12-18","Hartenbos","ATKV Street Mile")]:
    add(title=f"Eden Street Mile Series: {nm}",category="funrun",start_date=d,time="",town=town,venue=f"Street course, {town}",price_from="",ticket_url="",
        source_url="https://www.facebook.com/events/1676645959942885/",source_name="Eden Street Mile Series (Facebook)",alt_sources=[GRC+"atkv-street-mile-from-18th-dec-2026-till_event_op_view_id_3861"],
        notes="1-mile road race; part of a three-race series (George 14 Dec, Oudtshoorn 16 Dec, Hartenbos 18 Dec). Elite, university, school and social runners. Prize purse over R60,000.")
add(title="Vortex Open Source 2026 (trance festival)",category="festival",start_date="2026-12-18",end_date="2026-12-20",time="Fri 10:00 – Sun 16:00",town="Ladismith",venue="Karoo 62 Escape",
    venue_address="Route 62, Ladismith",price_from="",ticket_url="https://www.quicket.co.za/events/386068-vortex-open-source-2026",source_url="https://www.quicket.co.za/events/386068-vortex-open-source-2026",
    source_name="Quicket",alt_sources=[GRC+"vortex-open-source-2026-from-18th-dec-2026-till-20th-dec-2026_event_op_view_id_3923"],notes="Summer-solstice Open Source gathering (since 1995), Vortex's 30th year. Klein Karoo.")
# Punt in die Wind (Mossel Bay) individual shows from the Visit Mossel Bay calendar
for slug,t,d,tm,ven,tix in [
  ("meerkat-petra-at-punt-in-die-wind-festival","Meerkat Petra","2026-12-19","20:00","Mossel Bay Stadsaal (Town Hall)","https://itickets.co.za/events/486591"),
  ("ouma-die-ou-koeie-met-margit-meyer-rodenbeck","Ouma & die Ou Koeie (Margit Meyer-Rödenbeck)","2026-12-21","","Punt in die Wind venue (see listing)",""),
  ("mel-die-storieverteller-2","Mel die Storieverteller","2026-12-21","20:00","Mossel Bay Stadsaal (Town Hall)",""),
  ("liewe-heksie-with-margit-meyer-rodenbeck","Liewe Heksie (Margit Meyer-Rödenbeck)","2026-12-22","10:00","Mossel Bay Stadsaal (Town Hall)",""),
  ("geagte-kampeerders-2","Geagte Kampeerders (Wynand van Vollenstee & Thiart Li)","2026-12-22","15:00","Mossel Bay Town Hall","https://itickets.co.za/events/486204"),
  ("tillie-matilda","Tillie / Mathilda (Amanda Strydom & Je-Ani Swiegelaar)","2026-12-22","20:00","Mossel Bay Town Hall","https://itickets.co.za/events/486202"),
  ("sielskos-dames-oggend","SielsKos Dames Oggend (Hannes van Wyk)","2026-12-24","10:00","Mossel Bay Town Hall","https://itickets.co.za/events/486212")]:
    add(title=t,category="arts",start_date=d,time=tm,town="Mossel Bay",venue=ven,venue_address=("101 Marsh Street, Mossel Bay" if "Stadsaal" in ven else ("Wassung Street, Mossel Bay" if "Town Hall" in ven else "")),
        price_from="",ticket_url=tix,source_url=MB+slug+"/",source_name=_S_MB,alt_sources=([tix] if tix else [])+([OTR8] if "Tillie" in t else []),notes="Show at the Punt in die Wind Kunste-Week (19-26 Dec).")
# 2027
add(title="Attakwas Extreme (MTB)",category="sport",start_date="2027-01-16",time="",town="Oudtshoorn",venue="Oudtshoorn to the coast (route)",price_from="",ticket_url="",source_url=OTR8,source_name=_S_OTR,
    notes="One-day extreme mountain-bike race from the Klein Karoo to the coast.")
add(title="PE Plett MTB stage race",category="sport",start_date="2027-02-17",end_date="2027-02-21",time="Registration 17 Feb; stage 1 starts 18 Feb 08:00",town="Nature's Valley",venue="St Francis Links → Nature's Valley Rest Camp",
    price_from="",ticket_url="https://www.peplett.co.za/",source_url="https://www.peplett.co.za/",source_name="PE Plett (official site)",alt_sources=[OTR8],notes="Four-stage mountain-bike race from St Francis Bay to Nature's Valley (finish).")
add(title="Rattle and Rust Rally 2027",category="sport",start_date="2027-04-22",end_date="2027-04-25",time="08:00-17:00",town="Mossel Bay",venue="Bartelsfontein Farm",venue_address="Route R327, Bartelsfontein, Mossel Bay",
    price_from="",ticket_url="https://rattleandrustrally.co.za/",source_url=MB+"rattle-and-rust-rally-2027/",source_name=_S_MB,alt_sources=["https://rattleandrustrally.co.za/"],notes="Vintage and classic vehicle rally weekend.")
add(title="Knysna Oyster Festival 2027",category="festival",start_date="2027-07-02",end_date="2027-07-11",time="",town="Knysna",venue="Venues across greater Knysna",price_from="",ticket_url="https://www.knysnaoysterfestival.co.za/",
    source_url="https://www.knysnaoysterfestival.co.za/",source_name="Knysna Oyster Festival (official site)",alt_sources=[GRG],notes="Ten-day festival of food, sport and family events.")
add(title="Storms River Traverse 2027 (3-day MTB)",category="sport",start_date="2027-07-30",end_date="2027-08-01",time="",town="Storms River",venue="Tsitsikamma Village Inn",price_from="",
    ticket_url="https://www.stormsrivertraverse.co.za/",source_url="https://www.stormsrivertraverse.co.za/",source_name="Storms River Traverse (official site)",alt_sources=[GRG],notes="Three-day mountain-bike stage race.")
# Ongoing town-wide programmes (Mossel Bay), listed on ontheroute.co.za
add(title="Mossel Bay Sport and Recreation Festival",category="sport",start_date="2026-09-16",end_date="2026-10-18",time="Daily 08:00-17:00",town="Mossel Bay",venue="Various venues",price_from="",ticket_url="",
    source_url="https://www.ontheroute.co.za/events-calendar/",source_name="On The Route (events calendar)",notes="Town-wide programme of more than fifty sports and recreation activities: rugby, cycling, athletics, water sports and more.")
add(title="Mossel Bay Arts Festival (Arts Month)",category="festival",start_date="2026-09-23",end_date="2026-11-08",time="Times vary by programme",town="Mossel Bay",venue="Various venues",price_from="",ticket_url="",
    source_url="https://www.ontheroute.co.za/events-calendar/",source_name="On The Route (events calendar)",notes="Six weeks of exhibitions, performances and workshops across town.")
# --- weekly series ---
# All parkruns in the Garden Route district + Kouga (Jeffreys Bay / St Francis), from parkrun.co.za event pages; coordinates from parkrun's event map (images.parkrun.com/events.json).
# parkrun South Africa lists no junior (2 km Sunday) events.
_PR=[("hartenboschvillage","Hart & Bosch Village parkrun","Hartenbos","Hart & Bosch Village","R102, Hartenbos",-34.1126,22.1062,""),
    ("curromosselbayschool","Curro Mossel Bay School parkrun","Mossel Bay","Curro Mossel Bay School","2 Seemeeu Street, Heiderand, Mossel Bay",-34.1927,22.1103,""),
    ("bongamereserve","Bon Game Reserve parkrun","Mossel Bay","Bon Game Reserve","Near the Gourits River Bridge (N2)",-34.182,21.7528,""),
    ("george","George parkrun","George","Garden Route Botanical Garden","49 Caledon Street, George",-33.9454,22.4648,""),
    ("knysna","Knysna parkrun","Knysna","George Rex Drive","George Rex Drive, Knysna",-34.0459,23.0693,""),
    ("harkerville","Harkerville parkrun","Plettenberg Bay","Harkerville Market","N2, opposite Airport Road, Plettenberg Bay",-34.0384,23.2413," No dogs."),
    ("stilbaaiwestbeach","Stilbaai West Beach parkrun","Stilbaai","Stilbaai West Beach","Waterkant Street, Stilbaai",-34.3838,21.4227,""),
    ("hopkinsland","Hopkins Land parkrun","Witsand","Hopkins Land","End of Moodie Street, Witsand / Port Beaufort",-34.3921,20.8384," June to October fog is common, and the Malgas pont can cause delays: allow extra driving time."),
    ("stormsriver","Storms River parkrun","Storms River","MTO Lottering plantation (Block L)","North of the N2, opposite the Storms River Village entrance",-33.966,23.8868,""),
    ("stfrancis","St Francis parkrun","St Francis Bay","St Francis Links","St Francis Links, St Francis Bay",-34.1623,24.8154,""),
    ("mentorscountryestate","Mentors Country Estate parkrun","Jeffreys Bay","Mentors Country Estate","Corner of N2 Jeffreys Bay main off-ramp and St Francis Road, Jeffreys Bay",-34.017,24.8929,"")]
for slug,nm,town,venue,addr,la,lo,extra in _PR:
    occ=_dates("2026-10-10",HORIZON,[SAT])
    add(title=nm,category="funrun",start_date=occ[0],end_date=occ[-1],occurrences=occ,recurrence="Every Saturday, 08:00",time="08:00",town=town,venue=venue,venue_address=addr,
        lat=la,lng=lo,geo_source="parkrun event map",price_from="Free (register once)",ticket_url="",source_url=f"https://www.parkrun.co.za/{slug}/",source_name="parkrun",
        alt_sources=([MB+"bon-game-reserve-park-run/2026-10-10/"] if slug=="bongamereserve" else ([GRG] if slug in ("hartenboschvillage","curromosselbayschool","george","knysna","harkerville") else [])),
        notes="Free weekly 5 km walk/run. Register with parkrun once and bring your barcode."+extra)
# Oudtshoorn parkrun starts 07:00 October-March and 08:00 April-September (per its parkrun page).
_o=_dates("2026-10-10",HORIZON,[SAT])
for occ,tm in [([d for d in _o if d[5:7] in ("10","11","12","01","02","03")],"07:00"),([d for d in _o if d[5:7] in ("04","05","06","07","08","09")],"08:00")]:
    if not occ: continue
    add(title="Oudtshoorn parkrun"+(" (summer start 07:00)" if tm=="07:00" else " (winter start 08:00)"),category="funrun",start_date=occ[0],end_date=occ[-1],occurrences=occ,
        recurrence=f"Every Saturday, {tm} ({'October-March' if tm=='07:00' else 'April-September'})",time=tm,town="Oudtshoorn",venue="Surval Boutique Olive Estate",
        venue_address="R328, Cango Caves / Buffelsdrift Road, Oudtshoorn",lat=-33.5345,lng=22.2343,geo_source="parkrun event map",price_from="Free (register once)",ticket_url="",
        source_url="https://www.parkrun.co.za/oudtshoorn/",source_name="parkrun",notes="Free weekly 5 km walk/run; starts 07:00 Oct-Mar and 08:00 Apr-Sep. No dogs. Register with parkrun once and bring your barcode.")
occ=_dates("2026-10-10",HORIZON,[SAT])
add(title="Scarab Village Craft Market",category="market",start_date=occ[0],end_date=occ[-1],occurrences=occ,recurrence="Every Saturday, 08:30-12:30",time="08:30-12:30",town="Sedgefield",venue="Scarab Village",
    price_from="",ticket_url="",source_url=GRC+"scarab-village-craft-market-from-all-year-every-saturday-till_event_op_view_id_453",source_name=_S_GRC,alt_sources=["https://scarabvillage.co.za/craft-market/",GRG],
    notes="Handmade crafts, demonstrations, kids' play area.")
add(title="Hermanus Country Market",category="market",start_date=occ[0],end_date=occ[-1],occurrences=occ,recurrence="Every Saturday, 09:00-13:00",time="09:00-13:00",town="Hermanus",venue="Hermanus Country Market",
    price_from="",ticket_url="",source_url=GRC+"hermanus-country-market-from-all-year-every-saturday-till_event_op_view_id_2087",source_name=_S_GRC,alt_sources=["https://hermanuscountrymarket.co.za/"],
    notes="Fresh produce, artisan food, crafts and live music. Child- and dog-friendly.")
add(title="Stilbaai Brugmark (Saturday market)",category="market",start_date=occ[0],end_date=occ[-1],occurrences=occ,recurrence="Every Saturday",time="",town="Stilbaai",venue="Stilbaai Brugmark",
    price_from="",ticket_url="",source_url=GRG,source_name=_S_GRG,alt_sources=["https://www.facebook.com/stilbaaibrugmark"],notes="Weekly Saturday market. Times aren't listed; check the Facebook page.")
occ=_dates("2026-10-11",HORIZON,[SUN])
add(title="Milkwood Village Sunday Market",category="market",start_date=occ[0],end_date=occ[-1],occurrences=occ,recurrence="Every Sunday morning",time="Sunday mornings",town="Wilderness",venue="Milkwood Village",
    venue_address="Beacon Road, Wilderness",price_from="",ticket_url="",source_url="https://milkwoodvillage.co.za/",source_name="Milkwood Village (official site)",alt_sources=[GRG],
    notes="Craft market with live music and a kids' zone.")
occ=[d for d in _dates("2026-10-14",HORIZON,[WED]) if d[5:7] not in ("06","07","08")]
add(title="Mosaic Food Fare (Wednesday evenings)",category="market",start_date=occ[0],end_date=occ[-1],occurrences=occ,recurrence="Every Wednesday, 16:00-20:00 (September to May)",time="16:00-20:00",
    town="Sedgefield",venue="Mosaic Village & Outdoor Market",price_from="",ticket_url="",source_url=GRC+"mosaic-food-fare-from-all-year-every-wednesday-till_event_op_view_id_2739",source_name=_S_GRC,
    alt_sources=["http://mosaicmarket.co.za/welcome/",GRG],notes="International street food, live music and kids' activities. Runs September to May.")

# ---------------- Simola, Knysna (added 8 Oct 2026) ----------------
add(title="Simola Hillclimb 2027 (17th edition)",category="sport",start_date="2027-04-29",end_date="2027-05-02",
    time="Thu 29 Apr: car display at FanFest & parade; Fri 30 Apr: Classic Car Friday & King of the Hill display; Sat 1 - Sun 2 May: King of the Hill Shootout (from 09:05; prize-giving Sun 16:00)",
    town="Knysna",venue="Simola Hillclimb (Old Cape Road, Simola)",venue_address="Old Cape Road, Knysna (start line); FanFest at Hedge Street, Knysna",lat=-34.017299,lng=23.028515,geo_source="official site (start line)",
    price_from="R190",ticket_url="https://knysnaspeedfestival.howler.co.za/simolahillclimb2027",source_url="https://www.speedfestival.co.za/",source_name="Simola Hillclimb (official site)",
    alt_sources=["https://www.speedfestival.co.za/spectators/event-schedule/","https://www.speedfestival.co.za/spectators/ticket-information/","https://www.speedfestival.co.za/info/future-dates/"],
    notes="South Africa's premier hillclimb motorsport weekend. Adult general entry R190/day or R465 for 3 days (Tier 1, to 30 Nov); prices rise to R220 (Dec-Mar), R250 (from Apr) and R290 at the gate. Pensioners R190; children 12 and under free online. Le Mans VIP from R2,950. The schedule is provisional. Future dates: 27-30 Apr 2028.")
add(title="Christmas Pilates on the Simola helipad",category="community",start_date="2026-12-20",time="07:00-09:00",town="Knysna",venue="Simola Hotel, Country Club & Spa",
    venue_address="1 Old Cape Road, Simola, Knysna",price_from="",ticket_url="https://www.quicket.co.za/events/399557-christmas-pilates/",source_url="https://www.quicket.co.za/events/399557-christmas-pilates/",
    source_name="Quicket",notes="All-levels full-body Pilates flow led by Pure Posture Pilates on the hotel helipad overlooking the Knysna Heads.")

# ---------------- Film & outdoor cinema (added 8 Oct 2026) ----------------
add(title="Halloween @ Old Nick – open-air movie: Encanto",category="film",start_date="2026-10-31",time="Doors 16:00 (until 20:30)",town="Plettenberg Bay",venue="Old Nick Village",
    venue_address="N2, 3 km east of Plettenberg Bay",price_from="R100",ticket_url="https://www.quicket.co.za/events/394767-halloween-old-nick/",source_url="https://www.quicket.co.za/events/394767-halloween-old-nick/",
    source_name="Quicket",alt_sources=["https://openplanpictures.co.za/"],notes="Open Plan Pictures' 6th annual Halloween outdoor movie (Encanto, PG, 1h49). Dress up, trick-or-treat around the village, best-dressed competition for all ages, pop-up food market and a Nice Neighbour cash bar. R100 per person (R120 at the door).")
add(title="Out of Mined – documentary screening, Sedgefield",category="film",start_date="2026-10-11",time="19:00 (arrive from 18:30)",town="Sedgefield",venue="In Toto Retreat",
    venue_address="55 Jan van Riebeeck Street, The Island, Sedgefield",price_from="",ticket_url="https://www.quicket.co.za/events/401246-out-of-mined-sedgefield-screening/",
    source_url="https://www.quicket.co.za/events/401246-out-of-mined-sedgefield-screening/",source_name="Quicket",alt_sources=["https://intotoretreat.co.za/"],
    notes="Indoor screening of the award-winning 2026 West Coast mining documentary, followed by a short discussion. Hosted by In Our Nature, In Toto Retreat and Protect the West Coast NPC; 50% of ticket sales go to Protect the West Coast.")
# The Galileo Open Air Cinema 2026/27 season (15 Oct 2026 - 15 May 2027): every screening from thegalileo.co.za/movies (movie pages parsed into tools/galileo_2026_27.json).
import json as _json, os as _os, re
_GV={ # Galileo venue -> (venue name, town, address)
 "Kirstenbosch Garden":("Kirstenbosch National Botanical Garden","Cape Town","Rhodes Drive, Newlands, Cape Town"),
 "Battery Park, V&A Waterfront":("Battery Park, V&A Waterfront","Cape Town","Battery Park, V&A Waterfront, Cape Town"),
 "Central Park, Century City":("Central Park, Century City","Cape Town","Century City, Cape Town"),
 "Claremont Cricket Club":("Claremont Cricket Club","Cape Town","Claremont, Cape Town"),
 "German School (DSK)":("German International School Cape Town (DSK)","Cape Town","Tamboerskloof, Cape Town"),
 "Norval Foundation":("Norval Foundation","Cape Town","4 Steenberg Road, Tokai, Cape Town"),
 "Meerendal Wine Estate":("Meerendal Wine Estate","Cape Town","Meerendal, Durbanville, Cape Town"),
 "Zevenwacht Wine Estate":("Zevenwacht Wine Estate","Cape Town","Zevenwacht, Kuils River, Cape Town"),
 "Glenelly Estate":("Glenelly Estate","Stellenbosch","Glenelly Estate, Stellenbosch"),
 "Morgenhof Wine Estate":("Morgenhof Wine Estate","Stellenbosch","Morgenhof, Stellenbosch"),
 "Asara Wine Estate":("Asara Wine Estate","Stellenbosch","Asara, Stellenbosch"),
 "Blaauwklippen Wine Estate":("Blaauwklippen Wine Estate","Stellenbosch","Blaauwklippen, Stellenbosch"),
 "Jordan Wine Estate":("Jordan Wine Estate","Stellenbosch","Jordan Wine Estate, Stellenbosch"),
 "Nederburg Wine Farm":("Nederburg Wine Farm","Paarl","Nederburg, Paarl"),
 "Rhebokskloof Wine Estate":("Rhebokskloof Wine Estate","Paarl","Rhebokskloof, Paarl"),
 "Leopards Leap":("Leopard's Leap Family Vineyards","Franschhoek","Leopard's Leap, Franschhoek"),
 "Allée Bleue Wine Estate":("Allée Bleue Wine Estate","Franschhoek","Allée Bleue, Groot Drakenstein"),
 "Plaisir Wine Estate":("Plaisir Wine Estate","Franschhoek","Plaisir, Simondium"),
}
_GAL_TIX="https://www.webtickets.co.za/v2/event.aspx?itemid=1600185548"
for _m in _json.load(open(_os.path.join(_os.path.dirname(__file__),"galileo_2026_27.json"),encoding="utf-8")):
    _vn,_tw,_ad=_GV[_m["venue"]]
    _t=re.sub(r"\s+[–-]\s+(Kirstenbosch Garden|Kirstenbosch|Meerendal Wine Estate)$","",_m["title"]).replace(" at Meerendal","").replace(" at Kirstenbosch","")
    _ty=(_m["type"] or "PICNIC").upper()
    _tl=_t.lower()
    if _ty=="ROYALE": _pr="R350"
    elif "valentine" in _tl: _pr="R350"
    elif "christmas" in _tl: _pr="R225"
    elif _ty=="SPECIAL" or "easter" in _tl: _pr="R175"
    else: _pr="R155"
    _st=(_m["start"] or "").replace("h",":"); _dr=(_m["doors"] or "").replace("h",":")
    _age=_m["age"] if _m["age"] and not re.match(r"^\d\dh\d\d$",_m["age"]) else ""
    add(title=f"Galileo Open Air Cinema: {_t}",category="film",start_date=_m["iso"],time=(f"Doors {_dr}, movie {_st}" if _dr else f"Movie {_st}"),
        town=_tw,venue=_vn,venue_address=_ad,price_from=_pr,ticket_url=_GAL_TIX,source_url=f"https://thegalileo.co.za/movie/{_m['slug']}/",source_name="The Galileo Open Air Cinema (official site)",
        alt_sources=["https://thegalileo.co.za/movies/"],
        notes=("Galileo Royale (VIP). " if _ty=="ROYALE" else ("Galileo special show. " if _ty=="SPECIAL" else "Galileo picnic screening. "))+
              (f"Rated {_age}. " if _age else "")+(f"Runtime {_m['run']}. " if _m["run"] and _m["run"]!="TBC" else "")+
              "Open-air movie under the stars: bring a picnic (alcohol allowed) or buy from the food vendors and bar on site. Standard ticket R155 (R170 with backrest, R180 with backrest and blanket); specials and Royale cost more. Children under 4 free. Book on Webtickets (search the show date).")

# ---------------- Die Bush Lapa, Herold's Bay (added 8 Oct 2026) ----------------
add(title="Big Screen Bok Rugby at Die Bush Lapa",category="sport",start_date="2026-10-08",end_date="2026-11-21",time="Springbok match times",town="George",
    venue="Die Bush Lapa (Herold's Bay Eco Resort)",venue_address="Herold's Bay Eco Resort, Oubaai Road, Herold's Bay, George",price_from="",lat=-34.050556,lng=22.3975,geo_source="nominatim (Herolds Bay village)",ticket_url="",
    source_url="https://visitgeorge.co.za/event/big-screen-bok-rugby/",source_name="Visit George",
    notes="Springbok tests shown live on a big screen at the Bush Lapa (Visit George lists the series from 20 Jun to 21 Nov 2026). The listing gives no match dates, so check with the organiser (Byron Minnie, 079 404 5875) before going. Cash bar and meals at the venue.")

# ---------------- Cornerstone Creek (Hoekwil) & Cornerstone Lifestyle Centre (George), added 8 Oct 2026 ----------------
add(title="Date Night at Cornerstone Creek",category="restaurant",start_date="2026-10-09",time="18:00",town="Hoekwil",
    venue="Cornerstone Creek",venue_address="Cornerstone Creek, Hoekwil, Wilderness",price_from="R550 per couple",ticket_url="",
    source_url="https://www.toodoo.co.za/date-night-cornerstone-creek-hoekwil/",source_name="toodoo",
    notes="Candlelit dinner with music and dancing. R550 per couple covers a shared starter, a bottle of wine, a main each, a shared dessert and a surprise envelope. Bookings essential on WhatsApp 079 141 6151.")
add(title="C2C Harvest Ultra (multi-lap trail run, 6.7 km laps)",category="funrun",start_date="2026-10-17",time="15:00-22:00",town="George",
    venue="Cornerstone Lifestyle Centre",venue_address="The Cornerstone Lifestyle Centre, R404, Blanco, George",price_from="",ticket_url="https://racetoken.co.za/event_view.php?event_id=28",
    source_url="https://georgetrails.org.za/event/c2c-harvest-ultra/",source_name="George Trails",
    notes="Last-one-standing format on a 6.7 km loop, with a new lap starting every hour from 15:00. Pick 1 lap (Seed Dash), 3 (Sprout Challenge), 6 (Reap Quest) or 8 (Harvest Grind). Kids' 800 m Future Farmers Sprint at 20:00. Organised by Crank To Crown Cycles. The RaceToken entry page still said 'coming soon' on 8 Oct, so check there for entries and prices.")
