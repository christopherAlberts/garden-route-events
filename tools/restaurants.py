"""Restaurants tab data: facts from the 6 Oct 2026 check only. Writes data/restaurants.json + data/restaurants.js
and downloads one venue photo per restaurant (from its own site) to images/r-<id>.webp."""
import json,os,io,subprocess
from PIL import Image
R=os.path.join(os.path.dirname(os.path.abspath(__file__)),"..")
CHECKED="2026-10-06"
def S(name,url):return {"name":name,"url":url}
REST=[
 dict(id="pottery-george",name="The Pottery George",town="George",address="42 York Street, George",phone="",
   website="https://george.thepottery.co.za/",img="https://george.thepottery.co.za/wp-content/uploads/2023/11/Pottery-George-Banner-Slide-2.jpg",
   blurb="Creative café and social restaurant at the home of Wonki Ware: pottery painting, garden, kids' play area.",
   specials=[["Tuesday","Taco Tuesday: buy any taco and get 30% off any tequila-based cocktail"],["Wednesday","Burger special: 20% off"],["Thursday","Classic pizza special: R120 each"],["Friday","30% off pottery painting for kids under 12 (not during school holidays)"]],
   music=["“Vibey nightlife with funky DJs and bands” (no schedule published)"],
   notes="Name check: he said “The Pottery”; no George restaurant called “The Potter” was found.",
   sources=[S("The Pottery George (official site)","https://george.thepottery.co.za/")],match=[]),
 dict(id="tigers-milk-george",name="Tiger's Milk George",town="George",address="23 Courtenay Street, George",phone="044 001 2618",
   website="https://www.tigersmilk.co.za/",img="https://www.tigersmilk.co.za/wp-content/uploads/2024/07/tigers-milk-hero.jpg",
   blurb="Opened December 2025: elevated casual dining, craft beer, live music and DJs.",
   specials=[["Mon–Fri","Happy hour 16:00–18:00: 2-for-1 on house beer, wine and selected cocktails (T&Cs apply)"],["Tuesday","Pizza Tuesday"]],
   music=["DJ weekends, Soulful Sundays (from 18:00) and a Monday pool competition were listed May–Aug 2026; nothing newer listed as of Oct 2026"],
   notes="Photo is from the Tiger's Milk group site, not necessarily the George branch.",
   sources=[S("Local-Info: happy hour","https://local-info.co.za/event/happy-hour-specials-tigers-milk-george-2/"),S("George Herald: opening","https://www.georgeherald.com/Video/Video/inside-george-s-new-hotspot-tiger-s-milk-opens-with-huge-energy-local-leaders-202512041204"),S("Local-Info: Soulful Sundays (Aug 2026)","https://local-info.co.za/event/soulful-sundays-with-shinco-at-tigers-milk-in-george/")],match=[]),
 dict(id="hennies-george",name="Hennie's George",town="George",address="42 York Street, George South, George",phone="062 579 8350",
   website="https://www.therealhennies.co.za/branches/hennies-george",img="https://therealhennies.co.za/images/branches/george/hero-banner-june-2026.png",
   blurb="Restaurant & grill with live music, 4 beers on tap and 12 TVs. Free entry to events, first come first served.",
   specials=[["Mon–Thu","“Debriefing Specials” 13:00–17:00 (details not published)"]],
   music=["Every Tuesday 19:00: Noot vir Noot music quiz","Every Thursday 19:00: Quiz Night","Live acts on selected Fridays/Saturdays (see upcoming events)"],
   notes="“Henny's” and “Hemnies” both point to this venue; no other similarly named George/Garden Route restaurant was found.",
   sources=[S("Hennie's George branch page","https://www.therealhennies.co.za/branches/hennies-george"),S("What's On poster, October 2026","https://www.therealhennies.co.za/img/posters/whatson-oct-2026/george.jpg")],match=["Hennie's George"]),
 dict(id="terrace-george",name="The Terrace George",town="George",address="R404, Blanco, George",phone="+27 76 140 1980",
   website="https://www.theterracegeorge.co.za/",img="https://static.wixstatic.com/media/13723e_791b4dbf5bfd45bc81e749f992471dd6~mv2.jpeg",
   blurb="Wood-fired dining with Outeniqua mountain views. Open Wed–Sat 12:00–21:00, Sun 11:00–18:00; closed Mon & Tue.",
   specials=[],music=["A guest review on their site mentions live music; no schedule published"],
   notes="Most likely match for “The Terrace” in George (the other well-known Terrace is a rooftop venue in Cape Town). No specials or events found.",
   sources=[S("The Terrace George (official site)","https://www.theterracegeorge.co.za/")],match=[]),
 dict(id="clay-cafe-george",name="Clay Cafe George",town="George",address="R404, Blanco, George",phone="+27 44 868 0480",
   website="https://www.claycafegeorge.co.za/",img="https://static.wixstatic.com/media/13723e_a31eea1fbe8e476e907b84eef028154f~mv2.jpg",
   blurb="Ceramic painting family restaurant. Open Tue–Sat 09:00–17:00, Sun 09:00–16:00; closed Mondays.",
   specials=[["Any open day","Paint, Eat & Play Kids Combo: R265 per child (ceramic item up to R200, kids' meal, milkshake or slushie); booking recommended"]],
   music=[],notes="No Clay Cafe in Hartenbos could be found (searches only return the Cape Town branches). No events found in the window; the 3rd-anniversary party with live music was in Sept 2026.",
   sources=[S("Clay Cafe George (official site)","https://www.claycafegeorge.co.za/"),S("Visit George: Kids Combo","https://visitgeorge.co.za/clay-cafe-kids-combo/")],match=[]),
 dict(id="tapas-oysters-knysna",name="Tapas & Oysters",town="Knysna",address="TH 29, Thesen Island, Knysna",phone="+27 44 382 7196",
   website="https://tapasknysna.co.za/",img="https://tapasknysna.co.za/wp-content/uploads/2019/03/tapas-knysna-thesen15.jpg",
   blurb="Waterside tapas, oysters and sushi on Thesen Island. Six big-screen TVs, kids' play park, free boat jetties.",
   specials=[],music=["Live entertainment on Wednesday and Friday evenings (no artists listed)"],
   notes="He said “Tapas” in Knysna; this is the Thesen Island restaurant. Their specials page is currently empty.",
   sources=[S("Tapas & Oysters: contact page","https://tapasknysna.co.za/contact/"),S("Tapas & Oysters (official site)","https://tapasknysna.co.za/")],match=["Tapas & Oysters"]),
 dict(id="34-south-knysna",name="34 South (34° South)",town="Knysna",address="Shop 19, The Waterfront at the Knysna Quays, Waterfront Drive, Knysna",phone="044 382 7331",
   website="https://www.34south.biz/",img="https://b-cdn.springnest.com/media/img/18l/img_1912-editccb7ba9.jpg?aspect_ratio=1200%3A630&width=1200",
   blurb="Knysna waterfront restaurant, deli, bakery and wine shop; breakfast, lunch and dinner daily.",
   specials=[["Weekly","Sit-down restaurant specials that change weekly (last seen 28 Sep–4 Oct 2026); ask by phone"]],
   music=[],notes="No live music or events found. Not to be confused with 34 Waenhout, a separate Knysna live venue (ForestJAZZ, 7 Nov).",
   sources=[S("34 South (official site)","https://www.34south.biz/")],match=[]),
 dict(id="pili-pili-sedgefield",name="Pili Pili Sedgefield",town="Sedgefield",address="2 Claude Urban Drive, Myoli Beach, Sedgefield",phone="+27 44 343 3087",
   website="https://pilipili.co.za/pages/sedgefield",img="",
   blurb="Beach bar & restaurant on Myoli Beach: wood-fired pizzas, burgers, seafood, rooftop deck.",
   specials=[],music=["“Late-night live music” (no regular nights published)"],
   notes="No festive-season or New Year's Eve plans published yet. National Braai Day with Albert Frost (24 Sep) was before the window.",
   sources=[S("Pili Pili Sedgefield (official page)","https://pilipili.co.za/pages/sedgefield"),S("toodoo: Vinyl Krispies","https://www.toodoo.co.za/vinyl-krispies-sedgefield/"),S("Visit Knysna: Braai Day (Sep 2026)","https://www.visitknysna.co.za/whats-on/events/national-braai-day-at-pilipili/")],match=["Pili Pili"]),
 dict(id="hoeka-toeka-hoekwil",name="Hoeka Toeka Pub & Diner",town="Hoekwil",address="48 Church Road, Hoekwil",phone="079 917 2222",
   website="https://www.foodyas.com/ZA/Hoekwil/837657939628374/Hoeka-Toeka-Pub-%26-Diner",img="",
   blurb="Village pub & diner known for its ribs and its view. Open Wed 09:00–21:00, Thu–Sat 09:00–20:00, Sun 09:00–15:00.",
   specials=[["Rugby days","Beer & ribs special on big rugby match days (posted Sep 2026; book ahead)"]],
   music=["Every Wednesday 18:00–21:00: Donkiekar Boere Orkes (bookings essential)"],
   notes="No website; details come from the pub's Facebook posts as mirrored by Foodyas.",
   sources=[S("Hoeka Toeka Facebook posts (via Foodyas)","https://www.foodyas.com/ZA/Hoekwil/837657939628374/Hoeka-Toeka-Pub-%26-Diner")],match=["Hoeka Toeka"]),
 dict(id="cornerstone-creek-hoekwil",name="Cornerstone Creek",town="Hoekwil",address="Hoekwil, Wilderness",phone="",
   website="https://www.cornerstonecreek.co.za/",img="https://static.wixstatic.com/media/661dca_572f212aba0a4edca518d7f38c57df02~mv2.jpeg",
   blurb="Family restaurant and coffee bar in the countryside just outside Wilderness. Open Sat 09:00–22:00, Sun 09:00–16:00.",
   specials=[],music=["Their site lists “live music” among what they offer; no schedule published"],
   notes="No dated events found.",sources=[S("Cornerstone Creek (official site)","https://www.cornerstonecreek.co.za/")],match=[]),
 # ---- quiz-night venues (added 2026-10-06) ----
 dict(id="hennies-hartenbos",name="Hennie's Hartenbos",town="Hartenbos",address="156 Paardekraal Avenue, Hartenbos, Mossel Bay",phone="044 868 0677",
   website="https://www.therealhennies.co.za/branches/hennies-hartenbos",img="",
   blurb="Hartenbos branch of the Hennie's restaurant & grill chain. Free entry to events, first come first served.",
   specials=[],music=["Every Wednesday 19:00: Quiz Night, prizes to be won (October 2026 poster)"],
   notes="Also on 075 013 9458 / hartenbos@therealhennies.co.za.",
   sources=[S("Hennie's Hartenbos branch page","https://www.therealhennies.co.za/branches/hennies-hartenbos"),S("What's On poster, October 2026","https://www.therealhennies.co.za/img/posters/whatson-oct-2026/hartenbos.jpg")],match=["Hennie's Hartenbos"]),
 dict(id="hennies-oudtshoorn",name="Hennie's Oudtshoorn",town="Oudtshoorn",address="114 Baron van Rheede Street, Oudtshoorn",phone="078 884 7268",
   website="https://www.therealhennies.co.za/branches/hennies-oudtshoorn",img="",
   blurb="Oudtshoorn branch of the Hennie's restaurant & grill chain. Free entry to events, first come first served.",
   specials=[],music=["Every Thursday 19:00: Quiz Night, prizes to be won (October 2026 poster)"],notes="",
   sources=[S("Hennie's Oudtshoorn branch page","https://www.therealhennies.co.za/branches/hennies-oudtshoorn"),S("What's On poster, October 2026","https://www.therealhennies.co.za/img/posters/whatson-oct-2026/oudtshoorn.jpg")],match=["Hennie's Oudtshoorn"]),
 dict(id="rocket-george",name="Rocket",town="George",address="Arbour Road, Heatherlands, George",phone="",website="",img="",
   blurb="George venue that hosts the Garden Route Trivia League on Thursdays.",
   specials=[],music=["Thursdays: Garden Route Trivia League quiz (no start time published; 082 335 9406)"],
   notes="Address from OpenStreetMap. No website, menu or specials found.",
   sources=[S("Knysna Diary, October 2026","https://www.knysna.n2rs.com/knysna-diary-october.html")],match=["Rocket, George"]),
 dict(id="red-bridge-knysna",name="Red Bridge Brewing Co.",town="Knysna",address="5 Noble Street, Knysna Industria, Knysna",phone="083 997 2697",website="https://www.redbridgebrewing.co.za/",img="",
   blurb="Craft micro-brewery and taproom in Knysna Industria (not George). Taproom: Mon–Wed 08:00–16:00, Thu 11:00–21:00, Fri 08:00–21:00, closed weekends.",
   specials=[],music=["1st Wednesday of the month: Garden Route Trivia League quiz (no start time published; 082 335 9406)"],
   notes="Address from OpenStreetMap. No specials found.",
   sources=[S("Knysna Diary, October 2026","https://www.knysna.n2rs.com/knysna-diary-october.html")],match=["Red Bridge Brewing"]),
 dict(id="knysna-distillery",name="Knysna Distillery",town="Knysna",address="5 Uil Street, Knysna Industria, Knysna",phone="",website="",img="",
   blurb="Distillery and cocktail bar in Knysna Industria.",
   specials=[],music=["2nd, 3rd, 4th (+5th) Wednesdays: Garden Route Trivia League quiz (no start time published; 082 335 9406)"],
   notes="No specials found.",
   sources=[S("Knysna Diary, October 2026","https://www.knysna.n2rs.com/knysna-diary-october.html")],match=["Knysna Distillery"]),
 dict(id="hennies-durbanville",name="Hennie's Durbanville",town="Cape Town",address="7B Pampoenkraal Lane, Durbanville, Cape Town",phone="066 374 5732",
   website="https://www.therealhennies.co.za/branches/hennies-durbanville",img="",
   blurb="Durbanville branch of the Hennie's restaurant & grill chain. Free entry to events, first come first served.",
   specials=[],music=["Every Tuesday 19:00: Quiz Night","Live acts in October 2026 (20:30): Brandon Miles Fri 9 Oct, Byron Minnie Fri 23 Oct, Norra Sat 31 Oct"],notes="",
   sources=[S("Hennie's Durbanville branch page","https://www.therealhennies.co.za/branches/hennies-durbanville"),S("What's On poster, October 2026","https://www.therealhennies.co.za/img/posters/whatson-oct-2026/durbanville.jpg")],match=["Hennie's Durbanville"]),
 dict(id="hennies-brackenfell",name="Hennie's Brackenfell",town="Cape Town",address="Shop 57, Brackenfell Shopping Centre, Old Paarl Road, Brackenfell, Cape Town",phone="068 924 7654",
   website="https://www.therealhennies.co.za/branches/hennies-brackenfell",img="",
   blurb="Brackenfell branch of the Hennie's restaurant & grill chain.",
   specials=[],music=["Every Tuesday 19:00: Quiz Night, tickets R30"],notes="",
   sources=[S("Hennie's Brackenfell branch page","https://www.therealhennies.co.za/branches/hennies-brackenfell"),S("What's On poster, October 2026","https://www.therealhennies.co.za/img/posters/whatson-oct-2026/brackenfell.jpg")],match=["Hennie's Brackenfell"]),
 dict(id="backyard-jbay",name="The Backyard Beer Garden",town="Jeffreys Bay",address="12 Oosterland Street, Jeffreys Bay",phone="",website="",img="",
   blurb="Beer garden in Jeffreys Bay.",
   specials=[],music=["Last Thursday of the month 19:00–21:00: Quiz Night hosted by Brian C. Pyle"],
   notes="9ty9.co.za also lists live music at the venue; no dates in the window were checked for this card.",
   sources=[S("9ty9.co.za: Quiz Night at the Backyard (24 Sep 2026)","https://9ty9.co.za/events/quiz-night-a-the-backyard-2026-09-24/")],match=["Backyard Beer Garden"]),
 dict(id="cula-george",name="Cula Restaurant & Bar",town="George",address="Shop 22, Outeniqua Village (Outeniqua Lifestyle Centre), Knysna Rd & Saint George's Rd, George",phone="044 630 0701",
   website="https://www.cula.co.za/",img="",
   blurb="Pan-Asian restaurant (Wild Route group): Korean fried chicken, sushi, ramen and a robata coal grill. Book via Dineplan or reservations@cula.co.za.",
   specials=[["Monday","#SweetTooth Mondays: book on Dineplan with #SweetTooth in the comments for a free dessert after your main"],["Tuesday","Pensioner's Asian Day: over-60s get 20% off breakfast, lunch and dinner"],["Wednesday","Date Night: 3-course dinner + bottle of wine, R595 per couple"],["Thursday","50% off sushi from 16:00 (excl. specialities & platters, eat-in)"],["Friday","Friday Steak Night from 17:00: 200g sirloin dishes R149"],["Mon–Fri","Express Lunch 12:00–15:00: R105, served in 15 min or it's free"],["Sat & Sun","Kids eat free (1 child 12 and under per adult main, eat-in)"]],
   music=[],
   notes="Name check: “Cula” is correct. Specials read from the posters on cula.co.za (7 Oct 2026); posters are undated.",
   sources=[S("Cula (official site)","https://www.cula.co.za/"),S("Cula reservations","https://cula.co.za/reservations/"),S("Visit George","https://visitgeorge.co.za/directory/cula-restaurant-and-bar/")],match=["Cula"]),
 dict(id="beach-house-wilderness",name="Beach House Bar & Kitchen",town="Wilderness",address="Wilderness Beach House Backpackers, Sands Road, Leentjiesklip, Wilderness",phone="071 495 1814 (WhatsApp)",
   website="https://wildernessbeachhouse.com/",img="",
   blurb="Backpackers bar on the hillside above Leentjiesklip beach: wood-fired pizza from 11:00, craft beer, ocean-view deck. Walk-in only.",
   specials=[["Friday","Pool and darts night from 18:00"]],
   music=["Every Sunday 15:00–18:00: Sunday Sessions live music (free)","Every Thursday 18:00–22:00: Open Mic with One Two Sound Solutions (free)"],
   notes="Name check: “The Beach House” in Wilderness = Wilderness Beach House Backpackers. Not to be confused with Fairy Knowe.",
   sources=[S("Wilderness Beach House: Bar & Kitchen","https://wildernessbeachhouse.com/bar-kitchen/"),S("Wilderness Beach House: Live music","https://wildernessbeachhouse.com/live-music/")],match=["Beach House Wilderness"]),
 dict(id="fairy-knowe-backpackers",name="Fairy Knowe Backpackers",town="Wilderness",address="1 Dumbleton Road, Wilderness",phone="",
   website="https://www.fairyknowebackpackers.co.za/",img="",
   blurb="Bohemian backpackers with bar and restaurant; one of the oldest music venues on the Garden Route. Separate from the Fairy Knowe Hotel.",
   specials=[],music=["Live music gigs, open mic nights and a family market (no dates published)"],
   notes="No dated upcoming events found (checked Oct 2026); its May 2026 fundraiser festival has passed.",
   sources=[S("Fairy Knowe Backpackers: Entertainment","https://www.fairyknowebackpackers.co.za/entertainment")],match=[]),
 dict(id="seeplaas-groot-brak",name="Seeplaas Restaurant & Gallery",town="Groot Brak",address="Plot 60 Ottosrust, Groot Brakrivier (between George and Mossel Bay)",phone="044 620 2409 (restaurant bookings by phone only)",
   website="https://seeplaas.co.za/seeplaas-restaurant/",img="https://seeplaas.co.za/wp-content/uploads/2018/12/restaurant-seeplaas-food.jpg",
   blurb="Seasonal sea-view restaurant with a wine and gin bar, gift shop, Ken Maloney art gallery and guesthouse. Open Mon–Sun 08:00–17:00 (times vary by season). Breakfast 08:00–11:30, lunch from 11:30.",
   specials=[],music=[],
   notes="Location check: Groot Brakrivier, about 23 km from Mossel Bay and 27 km from George. The Powervan Mossel Bay breakfast trip from Hartenbos stops here for breakfast (already listed as an event). No upcoming events or weekly specials published (checked 8 Oct 2026). The site's only event, Sip & Sow on 9 Aug 2026, is past, and the 'Musiekpret @ Seeplaas' listing is from Dec 2022.",
   sources=[S("Seeplaas Restaurant (official site)","https://seeplaas.co.za/seeplaas-restaurant/"),S("Seeplaas Events (official site)","https://seeplaas.co.za/seeplaas-events/"),S("Seeplaas contact","https://seeplaas.co.za/contact/")],match=["Seeplaas"]),
 dict(id="de-vette-mossel-grootbrak",name="De Vette Mossel Grootbrak",town="Groot Brak",address="Souwesia Beach, between Klein- and Groot-Brakrivier (off the R102)",phone="079 339 0170 (phone/WhatsApp)",
   website="https://devettemossel.co.za/grootbrak/",img="https://devettemossel.co.za/wp-content/uploads/2024/11/Grootbrak-Header-Slider-1.jpg",
   blurb="Beach seafood restaurant with a 7-course, 13-dish rolling buffet cooked on open fires: pot bread, mussels, snoek, seafood and meat potjies. Kids' play area, beach bar. Booking essential.",
   specials=[["Any open day","Rolling seafood buffet. Sessions 12:00 for 12:30 and 18:30 for 19:00. R395 adult, R310 high school, R180 primary school, R70 pre-school, under-3s free. Extras: lobster R390, whole prawns R250 (400 g), oysters R150 for 5"]],
   music=[],
   notes="Name/location check: “Vette Mossel” = De Vette Mossel Grootbrak, the original branch (2004), on the beach near Great Brak River. Open every day in season and in school holidays; other times, check open dates on Dineplan (https://account.dineplan.com/widgetframe/KrNQjPXp) or Facebook. Prices change each year on 1 Dec. 2026 holiday prawn buffets (Easter, Father's Day, Women's Day, Heritage Day; R440 adult) are past. No festive or Dec 2026 special announced yet; year-end functions are being booked.",
   sources=[S("De Vette Mossel Grootbrak (official site)","https://devettemossel.co.za/grootbrak/"),S("De Vette Mossel bookings & prices","https://devettemossel.co.za/bookings/"),S("Facebook posts via Foodyas (to 6 Oct 2026)","https://www.foodyas.com/ZA/Great-Brak-River/427093387366316/De-Vette-Mossel---Grootbrak"),S("Food-Blog: Heritage Day 2026 prawn buffet","https://www.food-blog.co.za/all-you-can-eat-prawns-and-a-heritage-day-seafood-buffet-at-de-vette-mossel-grootbrak/")],match=["De Vette Mossel"]),
]
GR={"George","Knysna","Sedgefield","Hoekwil","Wilderness","Hartenbos","Oudtshoorn","Mossel Bay","Plettenberg Bay","Groot Brak"}
def fetch(url,out):
    if os.path.exists(out) and os.path.getsize(out)>0: return True
    try:
        b=subprocess.run(["curl","-sL","-m","40","-A","Mozilla/5.0",url],capture_output=True).stdout
        im=Image.open(io.BytesIO(b)).convert("RGB"); im.thumbnail((900,900)); im.save(out,"WEBP",quality=78); return True
    except Exception as e: print("img fail",url,e); return False
import sys,datetime as _dt
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from geo import geocode
from towns import TOWNS
# Coordinates: fixed where already verified for events, else Nominatim on the address, else town centroid.
COORD={"hennies-george":(-33.9658718,22.4512367,"nominatim"),"pottery-george":(-33.9658718,22.4512367,"nominatim"),
 "tapas-oysters-knysna":(-34.048978,23.048194,"event page"),"pili-pili-sedgefield":(-34.0348895,22.8068601,"nominatim"),
 "red-bridge-knysna":(-34.04692,23.0772008,"nominatim"),"knysna-distillery":(-34.0448812,23.0727766,"nominatim"),
 "rocket-george":(-33.946309,22.456057,"nominatim"),"hennies-durbanville":(-33.8327892,18.6479816,"nominatim (street)"),
 "hennies-brackenfell":(-33.8674704,18.7062255,"nominatim (street, approximate)"),"backyard-jbay":(-34.051257,24.921325,"nominatim (street)")}
GEOQ={"tigers-milk-george":"23 Courtenay Street, George","34-south-knysna":"Knysna Quays, Knysna","cornerstone-creek-hoekwil":"Cornerstone Creek, Wilderness"}
# Calendar days for recurring specials / nights. ev=True: already its own event card (quiz, live music), so it is only
# shown as a label, not as a second calendar entry. Weekdays: Mon=0.
CAL={"pottery-george":[("w",{1},"Taco Tuesday",0),("w",{2},"Burger special",0),("w",{3},"Pizza special R120",0),("w",{4},"Kids' pottery painting 30% off",0)],
 "tigers-milk-george":[("w",{0,1,2,3,4},"Happy hour 16:00-18:00",0),("w",{1},"Pizza Tuesday",0)],
 "hennies-george":[("w",{0,1,2,3},"Debriefing specials 13:00-17:00",0),("w",{1},"Noot vir Noot 19:00",1),("w",{3},"Quiz night 19:00",1)],
 "tapas-oysters-knysna":[("w",{2,4},"Live entertainment",1)],"hoeka-toeka-hoekwil":[("w",{2},"Boere-orkes 18:00-21:00",1)],
 "hennies-hartenbos":[("w",{2},"Quiz night 19:00",1)],"hennies-oudtshoorn":[("w",{3},"Quiz night 19:00",1)],
 "hennies-durbanville":[("w",{1},"Quiz night 19:00",1)],"hennies-brackenfell":[("w",{1},"Quiz night 19:00",1)],
 "rocket-george":[("w",{3},"Trivia League quiz",1)],"red-bridge-knysna":[("n",(2,{1}),"Trivia League quiz",1)],
 "knysna-distillery":[("n",(2,{2,3,4,5}),"Trivia League quiz",1)],"backyard-jbay":[("n",(3,{-1}),"Quiz night 19:00",1)]}
WD=["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
def _dates(kind,arg):
    d=max(_dt.date.fromisoformat(CHECKED),_dt.date.today());e=_dt.date.today()+_dt.timedelta(days=183);o=[]
    while d<=e:
        if kind=="w" and d.weekday() in arg: o.append(d.isoformat())
        if kind=="n" and d.weekday()==arg[0]:
            n=(d.day-1)//7+1; last=(d+_dt.timedelta(days=7)).month!=d.month
            if n in arg[1] or (-1 in arg[1] and last): o.append(d.isoformat())
        d+=_dt.timedelta(days=1)
    return o
ev=json.load(open(os.path.join(R,"data","events.json")))
out=[]
for r in REST:
    o={k:v for k,v in r.items() if k not in("img","match")}
    o["garden_route"]=r["town"] in GR; o["last_checked"]=CHECKED
    p="images/r-%s.webp"%r["id"]
    o["image"]=p if r["img"] and fetch(r["img"],os.path.join(R,p)) else ""
    o["image_source"]=r["img"] if o["image"] else ""
    o["event_ids"]=[e["id"] for e in ev if any(m.lower() in (e["title"]+" "+e["venue"]).lower() for m in r["match"])]
    c=COORD.get(r["id"])
    if not c and r["id"] in GEOQ:
        g=geocode(GEOQ[r["id"]]); c=(g[0],g[1],"nominatim") if g else None
    if not c:
        g=geocode(TOWNS[r["town"]][0]); c=(g[0],g[1],"town centroid")
    o["lat"],o["lng"],o["geo_source"]=c
    o["region"]=TOWNS[r["town"]][1]
    occ=set();labels={}
    for kind,arg,lab,isev in CAL.get(r["id"],[]):
        ds=_dates(kind,arg)
        if not isev: occ.update(ds)
        for d in ds: labels.setdefault(d,[]).append(lab)
    o["occurrences"]=sorted(occ)
    o["day_labels"]={d:" · ".join(v) for d,v in sorted(labels.items()) if d in occ}
    rec=[]
    for kind,arg,lab,isev in CAL.get(r["id"],[]):
        dd=("/".join(WD[i] for i in sorted(arg)) if kind=="w" else {1:"1st",2:"2nd",3:"3rd",4:"4th",5:"5th",-1:"last"}.get(min(arg[1]),"")+(" " if min(arg[1])==-1 or len(arg[1])==1 else "-5th ")+WD[arg[0]])
        rec.append(dd+": "+lab)
    o["recurrence"]="; ".join(rec)
    out.append(o)
json.dump(out,open(os.path.join(R,"data","restaurants.json"),"w"),ensure_ascii=False,indent=1)
open(os.path.join(R,"data","restaurants.js"),"w").write("window.RESTAURANTS = "+json.dumps(out,ensure_ascii=False)+";\n")
for o in out: print(o["id"],o["image"] or "-",o["event_ids"])
