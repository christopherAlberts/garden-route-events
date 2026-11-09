/* Garden Route Events: static app, no build step. Data comes from window.EVENTS (data/events.js). */
(function(){
"use strict";
var GR_ORDER=["Still Bay","Mossel Bay","Hartenbos","Groot Brak","George","Oudtshoorn","Wilderness","Hoekwil","Sedgefield","Knysna","Plettenberg Bay","The Crags","Nature's Valley","Storms River","Tsitsikamma"];
var WIDE_ORDER=["Cape Town","Somerset West","Kleinmond","Pringle Bay","Hermanus","Stanford","Gansbaai","Struisbaai","L'Agulhas","Riversdale","Humansdorp","St Francis Bay","Jeffreys Bay"];
var MONTHS=(function(){ // current month through the last month that has any event (open-ended)
  var d=new Date(),y=d.getFullYear(),m=d.getMonth()+1,last=y+"-"+String(m).padStart(2,"0");
  (window.EVENTS||[]).forEach(function(e){var x=((e.occurrences&&e.occurrences.length?e.occurrences[e.occurrences.length-1]:"")||e.end_date||e.start_date||"").slice(0,7);if(x>last)last=x});
  var out=[];while(true){var k=y+"-"+String(m).padStart(2,"0");out.push(k);if(k>=last||out.length>36)break;m++;if(m>12){m=1;y++}}return out})();
var MN=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"];
var MNL=["January","February","March","April","May","June","July","August","September","October","November","December"];
var DOW=["Sun","Mon","Tue","Wed","Thu","Fri","Sat"];
var CATS={concert:"Concert",festival:"Festival",musical:"Musical",market:"Market",funrun:"Run / walk / trail",community:"Church / community",arts:"Arts & culture",quiz:"Quiz night",festive:"Festive dining",nature:"Nature & outdoors",sport:"Sport & motorsport",film:"Film / outdoor cinema",restaurant:"Restaurant"};
var CATPL={concert:"concerts",festival:"festivals",musical:"musicals",market:"markets",funrun:"runs, walks & trails",community:"church & community",arts:"arts & culture",quiz:"quiz nights",festive:"festive dining",nature:"nature & outdoors",sport:"sport & motorsport",film:"film & outdoor cinema nights",restaurant:"restaurants & pubs"};
var ICON={
  film:'<svg viewBox="0 0 24 24"><path d="M4 10h16v10H4zm.3-2.2L3.6 5.4 18.9 1.8l.6 2.4zM7.2 4.6l1.9 2.6 2.2-.5-1.9-2.6zm4.4-1 1.9 2.6 2.2-.5-1.9-2.6z"/></svg>',
  sport:'<svg viewBox="0 0 24 24"><path d="M5 2h2v1h13v11H7v8H5zm2 3v2h2.6V5zm2.6 2v2.3h2.6V7zm2.6-2v2h2.6V5zm2.6 2v2.3h2.6V7zM7 9.3v2.4h2.6V9.3zm5.2 0v2.4h2.6V9.3zm-2.6 2.4V14h2.6v-2.3zm5.2 0V14H18v-2.3z"/></svg>',
  restaurant:'<svg viewBox="0 0 24 24"><path d="M11 9H9V2H7v7H5V2H3v7c0 2.12 1.66 3.84 3.75 3.97V22h2.5v-9.03C11.34 12.84 13 11.12 13 9V2h-2v7zm5-3v8h2.5v8H21V2c-2.76 0-5 2.24-5 4z"/></svg>',
  quiz:'<svg viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 17h-2v-2h2v2zm2.07-7.75l-.9.92C13.45 12.9 13 13.5 13 15h-2v-.5c0-1.1.45-2.1 1.17-2.83l1.24-1.26c.37-.36.59-.86.59-1.41 0-1.1-.9-2-2-2s-2 .9-2 2H8c0-2.21 1.79-4 4-4s4 1.79 4 4c0 .88-.36 1.68-.93 2.25z"/></svg>',
  festive:'<svg viewBox="0 0 24 24"><path d="M20 6h-2.18c.11-.31.18-.65.18-1 0-1.66-1.34-3-3-3-1.05 0-1.96.54-2.5 1.35l-.5.67-.5-.68C10.96 2.54 10.05 2 9 2 7.34 2 6 3.34 6 5c0 .35.07.69.18 1H4c-1.11 0-1.99.89-1.99 2L2 19c0 1.11.89 2 2 2h16c1.11 0 2-.89 2-2V8c0-1.11-.89-2-2-2zm-5-2c.55 0 1 .45 1 1s-.45 1-1 1-1-.45-1-1 .45-1 1-1zM9 4c.55 0 1 .45 1 1s-.45 1-1 1-1-.45-1-1 .45-1 1-1zm11 15H4v-2h16v2zm0-5H4V8h5.08L7 10.83 8.62 12 12 7.4l3.38 4.6L17 10.83 14.92 8H20v6z"/></svg>',
  concert:'<svg viewBox="0 0 24 24"><path d="M9 3v10.55A4 4 0 107 21a4 4 0 004-4V7h6V3H9z"/></svg>',
  festival:'<svg viewBox="0 0 24 24"><path d="M12 2l1 0v2.2l5-1.2v4l-5 1.2V8.9L21.5 21H15l-3-5-3 5H2.5L11 8.9V2z"/></svg>',
  musical:'<svg viewBox="0 0 24 24"><path d="M12 2l2.9 6.9 7.1.5-5.4 4.6 1.7 7L12 17.3 5.7 21l1.7-7L2 9.4l7.1-.5z"/></svg>',
  funrun:'<svg viewBox="0 0 24 24"><path d="M13.5 5.5a2 2 0 100-4 2 2 0 000 4zM9.8 8.9L7 23h2.1l1.8-8 2.1 2v6h2v-7.5l-2.1-2 .6-3A7.3 7.3 0 0019 13v-2a5 5 0 01-4.3-2.4l-1-1.6a2 2 0 00-1.7-1l-.8.1L6 8.3V13h2V9.6z"/></svg>',
  community:'<svg viewBox="0 0 24 24"><path d="M11 2h2v3h3v2h-3v3.2l7 4.1V22h-6v-4a2 2 0 00-4 0v4H4v-7.7l7-4.1V7H8V5h3z"/></svg>',
  arts:'<svg viewBox="0 0 24 24"><path d="M3 3h9v7.5A4.5 4.5 0 017.5 15 4.5 4.5 0 013 10.5zm2.2 4.3h1.6V6.2H5.2zm3.5 0h1.6V6.2H8.7zM5.6 10a2 2 0 003.8 0zM12.5 9H21v7.5a4.5 4.5 0 01-9 0V14a6 6 0 00.5-3.5zm2 3.3h1.6v-1.6h-1.6zm3.4 0h1.6v-1.6h-1.6zm-3.3 4.4a2 2 0 003.8 0z"/></svg>',
  nature:'<svg viewBox="0 0 24 24"><path d="M12 2l5 7h-2.5l4 5.5H15l3.5 4.5H13v3h-2v-3H5.5L9 14.5H5.5l4-5.5H7z"/></svg>',
  market:'<svg viewBox="0 0 24 24"><path d="M3 9h18l-1.8 11.2A1 1 0 0118.2 21H5.8a1 1 0 01-1-.8L3 9zm5.2-1L12 2.5 15.8 8h-2.4L12 5.9 10.6 8z"/></svg>'};
var PIN='<svg viewBox="0 0 24 24"><path d="M12 2a7 7 0 017 7c0 5-7 13-7 13S5 14 5 9a7 7 0 017-7zm0 4.5A2.5 2.5 0 1012 11.5 2.5 2.5 0 0012 6.5z"/></svg>';
var ARROW='<svg viewBox="0 0 24 24"><path d="M13 5l7 7-7 7-1.4-1.4 4.6-4.6H4v-2h12.2l-4.6-4.6z"/></svg>';
var S={gal:false,scope:"gr",q:"",town:"",cat:"",month:"",view:"list",calMonth:null,calDay:null,off:false,event:"",nye:false,xmas:false,starred:false};
/* restaurants are entries of category "restaurant": list cards, calendar days with recurring specials, map pins */
var LAST_DAY=(function(){var l="";(window.EVENTS||[]).forEach(function(e){var x=e.end_date||e.start_date||"";if(x>l)l=x});return l||"2099-12-31"})(),EVR={};
var RS=(window.RESTAURANTS||[]).map(function(r){var o={};for(var k in r)o[k]=r[k];
  o._r=1;o.rid=r.id;o.id=o.key="r:"+r.id;o.title=r.name;o.category="restaurant";o.venue=r.name;o.venue_address=r.address;
  var oc=r.occurrences||[];o.occurrences=oc;o.start_date=oc.length?oc[0]:TODAY0();o.end_date=oc.length?oc[oc.length-1]:LAST_DAY;
  o.source_url=r.website||(r.sources&&r.sources[0]?r.sources[0].url:"");o.source_name=r.sources&&r.sources[0]?r.sources[0].name:r.name;o.ticket_url="";o.status="scheduled";o.price_from="";o.time="";
  o.notes=r.blurb||"";o._hay=(r.specials||[]).map(function(x){return x.join(" ")}).join(" ")+" "+(r.music||[]).join(" ")+" restaurant pub";
  return o});
function TODAY0(){var d=new Date();return d.getFullYear()+"-"+String(d.getMonth()+1).padStart(2,"0")+"-"+String(d.getDate()).padStart(2,"0")}
function isOff(e){return e.status==="postponed"||e.status==="cancelled"}
var STL={"sold out":"Sold out",postponed:"Postponed",cancelled:"Cancelled"};
function stBadge(e){return STL[e.status]?'<span class="status '+(isOff(e)?"off":"soldout")+'">'+STL[e.status]+'</span>':""}
var EV=[],map=null,layer=null;
var $=function(id){return document.getElementById(id)};
function esc(s){return String(s==null?"":s).replace(/[&<>"']/g,function(c){return {"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]})}
function pd(s){var p=s.split("-");return new Date(+p[0],+p[1]-1,+p[2])}
function iso(d){return d.getFullYear()+"-"+String(d.getMonth()+1).padStart(2,"0")+"-"+String(d.getDate()).padStart(2,"0")}
var TODAY=iso(new Date());
function endOf(e){return e.end_date||e.start_date}
function occ(e){return e.occurrences&&e.occurrences.length?e.occurrences:null}
function nextDate(e){var o=occ(e);if(o){for(var i=0;i<o.length;i++)if(o[i]>=TODAY)return o[i];return o[o.length-1]}return e.start_date<TODAY&&endOf(e)>=TODAY?TODAY:e.start_date}
function onDay(e,ds){var o=occ(e);if(e._r&&!o)return false;return o?o.indexOf(ds)>=0:(e.start_date<=ds&&endOf(e)>=ds)}
function inMonth(e,m){var o=occ(e);if(o)return o.some(function(d){return d.slice(0,7)===m});return e.start_date.slice(0,7)<=m&&endOf(e).slice(0,7)>=m}
function fmt(d,yr){return DOW[d.getDay()]+" "+d.getDate()+" "+MN[d.getMonth()]+(yr?" "+d.getFullYear():"")}
function when(e){
  if(e._r)return e.recurrence?esc(e.recurrence.split(";")[0]):"Specials &amp; nights: see card";
  if(occ(e)){return "Next: "+fmt(pd(nextDate(e)),false)}
  var a=pd(e.start_date);if(!e.end_date||e.end_date===e.start_date)return fmt(a,true);
  var b=pd(e.end_date);return fmt(a,a.getFullYear()!==b.getFullYear())+" – "+fmt(b,true)}
function monthLabel(m){var p=m.split("-");return MNL[+p[1]-1]+" "+p[0]}
function toTop(){try{window.scrollTo({top:0,left:0,behavior:"instant"})}catch(x){window.scrollTo(0,0)}document.documentElement.scrollTop=0;document.body.scrollTop=0}
function link(e){return e.ticket_url||e.source_url}
function blab(e){if(e._r)return "Website";return e.ticket_url?(e.category==="festive"?"Book / menu":"Tickets"):"Event page"}
function priceTxt(p){if(!p)return "";if(/ pp$|per person/i.test(p))return p;return /^\d/.test(p)?"From R"+p:(/^R\d/.test(p)?"From "+p:p)}
function thumb(e,cls){
  if(e.image)return '<img src="'+esc(e.image)+'" alt="" loading="lazy" decoding="async">';
  return '<div class="ph '+e.category+'">'+ICON[e.category]+'</div>';
}
/* ---------- sharing & deep links ---------- */
var LIVE="https://christopheralberts.github.io/garden-route-events/";
var SHARE_ICON='<svg viewBox="0 0 24 24"><path d="M18 15.5a3 3 0 00-2.3 1.1l-6.8-3.4a3 3 0 000-2.4l6.8-3.4A3 3 0 1015 5.5l-6.8 3.4a3 3 0 100 6.2l6.8 3.4a3 3 0 103-3z"/></svg>';
var WA_ICON='<svg viewBox="0 0 24 24"><path d="M12 2a10 10 0 00-8.6 15.1L2 22l5-1.3A10 10 0 1012 2zm0 18.2a8.2 8.2 0 01-4.2-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1112 20.2zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8s-.4-.1-.6.1-.7.8-.8 1-.3.2-.5.1a6.7 6.7 0 01-3.3-2.9c-.3-.4.3-.4.7-1.3a.5.5 0 000-.5l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 00-.7.3 3 3 0 00-.9 2.2 5.2 5.2 0 001.1 2.7 11.8 11.8 0 004.5 4c1.7.7 2.3.8 3.2.6a2.7 2.7 0 001.8-1.2 2.2 2.2 0 00.1-1.2c0-.2-.2-.2-.5-.4z"/></svg>';
var LINK_ICON='<svg viewBox="0 0 24 24"><path d="M10.6 13.4a1 1 0 001.4 0l4-4a3 3 0 00-4.2-4.2l-1.5 1.5 1.4 1.4 1.5-1.5a1 1 0 011.4 1.4l-4 4a1 1 0 000 1.4zm2.8-2.8a1 1 0 00-1.4 0l-4 4a3 3 0 004.2 4.2l1.5-1.5-1.4-1.4-1.5 1.5a1 1 0 01-1.4-1.4l4-4a1 1 0 000-1.4z"/></svg>';
function base(){return /^https?:/.test(location.protocol)?location.origin+location.pathname:LIVE}
function deep(e){return base()+"#event="+encodeURIComponent(e.id)}
function byId(id){if(/^r:/.test(id)){for(var j=0;j<RS.length;j++)if(RS[j].key===id)return RS[j];return null}for(var i=0;i<EV.length;i++)if(EV[i].id===id)return EV[i];return null}
function datesTxt(e){
  if(occ(e)){var o=occ(e).filter(function(d){return d>=TODAY});return (e.recurrence||"Recurring")+(o.length?" · next "+fmt(pd(o[0]),true):"")}
  var a=pd(e.start_date);if(!e.end_date||e.end_date===e.start_date)return fmt(a,true);
  return fmt(a,a.getFullYear()!==pd(e.end_date).getFullYear())+" – "+fmt(pd(e.end_date),true)}
function shareText(e){
  if(e._r)return restText(e);
  var L=[e.title,"📅 "+datesTxt(e)+(e.time&&!occ(e)?" · "+e.time:""),"📍 "+[e.venue,e.town].filter(Boolean).join(", ")];
  var p=priceTxt(e.price_from);if(p)L.push("💰 "+p);
  if(STL[e.status])L.push("⚠️ "+STL[e.status]);
  L.push((e.ticket_url?(e.category==="festive"?"📖 Book / menu: ":"🎟️ Tickets: "):"🔗 Event page: ")+link(e));
  L.push("","More on Garden Route Events: "+deep(e));
  return L.join("\n")}
function restText(r){
  var L=[r.name,"📍 "+r.address];
  (r.specials||[]).slice(0,4).forEach(function(x){L.push("🍽️ "+x[0]+": "+x[1])});
  (r.music||[]).slice(0,3).forEach(function(x){L.push("🎵 "+x)});
  var up=restEvents(r).slice(0,3);up.forEach(function(e){L.push("📅 "+fmt(pd(nextDate(e)),false)+": "+e.title)});
  if(r.phone)L.push("📞 "+r.phone);
  if(r.website)L.push("🔗 "+r.website);
  L.push("","More on Garden Route Events: "+deep(r));
  return L.join("\n")}
function restEvents(r){return (r.event_ids||[]).map(byId).filter(function(e){return e&&endOf(e)>=TODAY&&!isOff(e)}).sort(function(a,b){return nextDate(a).localeCompare(nextDate(b))})}
function waUrl(e){return "https://wa.me/?text="+encodeURIComponent(shareText(e))}
function shareBtn(e){return '<button class="sharebtn" type="button" data-share="'+esc(e._r?e.key:e.id)+'" aria-haspopup="menu" aria-label="Share '+esc(e.title)+'">'+SHARE_ICON+'<span>Share</span></button>'}
function toast(msg){var t=$("toast");t.textContent=msg;t.classList.add("on");clearTimeout(toast._t);toast._t=setTimeout(function(){t.classList.remove("on")},2200)}
/* ---------- "want to attend" stars: per user, stored on the server (/api/stars), localStorage as optimistic cache/fallback ---------- */
var STAR_SVG='<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3.2l2.6 5.5 6 .7-4.4 4.1 1.2 5.9L12 16.5l-5.4 2.9 1.2-5.9-4.4-4.1 6-.7z"/></svg>';
/* Stars are strictly per logged-in user: the server (user_stars via /api/stars) is the only source of truth.
   The cache lives under gre_stars_<userId>, is only read after /api/me confirms that same user, and is wiped on logout (login page) or for any other user.
   No login (static copy, expired session) = no stars shown and no star buttons. */
var ME=null,STARS={};
/* ---------- running club: one per user, saved on the server (/api/club); events carry clubs:[club ids] (tools/clubs.py) ---------- */
var CLUBS=window.CLUBS||[],CLUBBY={};CLUBS.forEach(function(c){CLUBBY[c.id]=c});
var MYCLUB=null,MYASA=null;
function isMine(e){return !!(MYCLUB&&e&&!e._r&&(e.clubs||[]).indexOf(MYCLUB)>=0)}
function clubTag(e){return isMine(e)?'<span class="clubtag" title="Hosted by your club, '+esc(CLUBBY[MYCLUB].name)+'">\u25CF My club</span>':""}
function hostLine(e){var c=(e.clubs||[]).map(function(i){return CLUBBY[i]}).filter(Boolean);return c.length?'<div class="hostline'+(isMine(e)?" mine":"")+'">Hosted by '+c.map(function(x){return esc(x.name)+(x.id===MYCLUB?" (your club)":"")}).join(", ")+'</div>':""}
function syncClub(uid){return fetch("/api/club",{credentials:"same-origin",cache:"no-store",headers:{"Accept":"application/json"}}).then(function(r){return r.ok?r.json():null}).then(function(d){
  if(!d||ME!==uid)return;var c=d.club_id&&CLUBBY[d.club_id]?d.club_id:null,a=typeof d.asa_number==="string"&&d.asa_number?d.asa_number:null;if(c!==MYCLUB||a!==MYASA){MYCLUB=c;MYASA=a;render();refreshModal()}}).catch(function(){})}
function clearStarCaches(keep){try{for(var i=localStorage.length-1;i>=0;i--){var k=localStorage.key(i);if(k&&(/^gre_stars_/.test(k)&&k!==keep||k==="gre.stars"||k==="gre.starsPending"))localStorage.removeItem(k)}}catch(x){}}
function starKey(){return ME?"gre_stars_"+ME:null}
function saveStars(){var k=starKey();if(!k)return;try{localStorage.setItem(k,JSON.stringify(STARS))}catch(x){}}
function isStar(e){return !!(ME&&e&&!e._r&&STARS[e.id])}
function starBtn(e){if(e._r||!ME)return "";var on=isStar(e);
  return '<button type="button" class="starbtn'+(on?" on":"")+'" data-star="'+esc(e.id)+'" aria-pressed="'+on+'" aria-label="'+(on?"Starred: want to attend ":"Star: want to attend ")+esc(e.title)+'" title="'+(on?"Want to attend (tap to unstar)":"Want to attend")+'">'+STAR_SVG+'</button>'}
var API_OK=/^https?:/.test(location.protocol);
function paintStars(id){Array.prototype.forEach.call(document.querySelectorAll('.starbtn[data-star="'+(window.CSS&&CSS.escape?CSS.escape(id):id)+'"]'),function(b){var on=!!STARS[id];
  b.classList.toggle("on",on);b.setAttribute("aria-pressed",on);b.title=on?"Want to attend (tap to unstar)":"Want to attend"})}
function afterStar(){if(S.view==="cal")renderCal();else if(S.starred&&S.view!=="cinema")render()}
function setStar(id,on){if(on)STARS[id]=STARS[id]||Date.now();else delete STARS[id];saveStars();paintStars(id)}
function toggleStar(id){if(!ME)return;var uid=ME,on=!STARS[id];setStar(id,on);afterStar();toast(on?"★ Starred: want to attend":"Star removed");
  fetch("/api/stars/"+encodeURIComponent(id),{method:on?"PUT":"DELETE",credentials:"same-origin",headers:{"Accept":"application/json"}})
    .then(function(r){if(!r.ok)throw r}).catch(function(r){if(ME!==uid)return;setStar(id,!on);afterStar();
      if(r&&r.status===401){logoutStars();toast("Your session ended. Log in again to save stars.")}else toast("Couldn\u2019t save the star. Check your connection.")})}
function refreshModal(){var id=$("evBox").dataset.id,e=id&&byId(id);if($("evModal").hidden||!e)return;$("evBox").innerHTML='<button type="button" class="mclose" data-close aria-label="Close">×</button>'+detailHtml(e)}
function logoutStars(){ME=null;STARS={};MYCLUB=null;MYASA=null;clearStarCaches(null);document.body.classList.remove("signed-in");render();refreshModal()}
function syncStars(){if(!API_OK){logoutStars();return}
  fetch("/api/me",{credentials:"same-origin",cache:"no-store",headers:{"Accept":"application/json"}}).then(function(r){if(r.status===401)return "out";return r.ok?r.json():null}).then(function(me){
    if(me==="out"||(me&&!me.id)){if(ME)logoutStars();else clearStarCaches(null);return}
    if(!me)return; /* network blip: keep whatever is showing */
    var uid=String(me.id);if(ME!==uid){ME=uid;clearStarCaches("gre_stars_"+uid);try{STARS=JSON.parse(localStorage.getItem("gre_stars_"+uid)||"{}")||{}}catch(x){STARS={}}document.body.classList.add("signed-in");render();refreshModal()}
    syncClub(uid);
    return fetch("/api/stars",{credentials:"same-origin",cache:"no-store",headers:{"Accept":"application/json"}}).then(function(r){if(r.status===401){logoutStars();return null}return r.ok?r.json():null}).then(function(d){
      if(!d||!Array.isArray(d.stars)||ME!==uid)return;var srv={};d.stars.forEach(function(x){srv[x.event_id]=Date.parse((x.created_at||"").replace(" ","T")+"Z")||1});
      var changed=JSON.stringify(Object.keys(srv).sort())!==JSON.stringify(Object.keys(STARS).sort());STARS=srv;saveStars();if(changed){render();refreshModal()}})}).catch(function(){})}
function copy(txt){
  function fb(){var ta=document.createElement("textarea");ta.value=txt;ta.setAttribute("readonly","");ta.style.position="fixed";ta.style.opacity="0";document.body.appendChild(ta);ta.select();
    var ok=false;try{ok=document.execCommand("copy")}catch(x){}document.body.removeChild(ta);toast(ok?"Link copied":"Copy failed, long-press to copy: "+txt)}
  if(navigator.clipboard&&window.isSecureContext)navigator.clipboard.writeText(txt).then(function(){toast("Link copied")},fb);else fb()}
function nativeShare(e){
  if(!navigator.share)return false;
  navigator.share({title:e.title,text:shareText(e).replace(/\n\nMore on Garden Route Events: .*$/,""),url:deep(e)}).catch(function(){});return true}
function closeMenu(){var m=$("shareMenu");m.hidden=true;m.dataset.id=""}
function openMenu(btn,id){
  var e=byId(id);if(!e)return;var m=$("shareMenu");
  if(m.dataset.id===id&&!m.hidden){closeMenu();return}
  m.dataset.id=id;
  m.innerHTML=(navigator.share?'<button type="button" data-act="native">'+SHARE_ICON+'Share via…</button>':'')+
    '<a href="'+esc(waUrl(e))+'" target="_blank" rel="noopener" data-act="wa">'+WA_ICON+'WhatsApp</a>'+
    '<button type="button" data-act="copy">'+LINK_ICON+'Copy link</button>'+
    (S.event!==id?'<button type="button" data-act="details">'+ARROW+'Details</button>':'');
  m.hidden=false;m._y=window.scrollY;
  var r=btn.getBoundingClientRect(),w=m.offsetWidth,h=m.offsetHeight;
  var left=Math.min(Math.max(8,r.left+r.width/2-w/2),window.innerWidth-w-8),top=r.bottom+6;
  if(top+h>window.innerHeight-8)top=Math.max(8,r.top-h-6);
  m.style.left=left+"px";m.style.top=top+"px";
  var f=m.querySelector("button,a");if(f)f.focus({preventScroll:true});
}
function detailHtml(e){
  if(e._r)return restDetail(e);
  var o=occ(e),L=esc(link(e)),p=priceTxt(e.price_from);
  var od=o?o.filter(function(d){return d>=TODAY}):[];
  return '<div class="mhead">'+(e.image?'<img src="'+esc(e.image)+'" alt="">':'<div class="ph '+e.category+'">'+ICON[e.category]+'</div>')+
      '<span class="cat '+e.category+'">'+CATS[e.category]+'</span>'+stBadge(e)+'</div>'+
    '<div class="mbody">'+(e.garden_route?'<span class="grtag">Garden Route</span>':'')+clubTag(e)+
      '<div class="ttl"><h2 id="evTitle">'+esc(e.title)+'</h2>'+starBtn(e)+'</div>'+
      '<div class="when">'+esc(datesTxt(e))+(e.time?" · "+esc(e.time):"")+'</div>'+
      (od.length>1?'<div class="occ">'+od.length+' upcoming dates: '+od.slice(0,10).map(function(d){var x=pd(d);return x.getDate()+" "+MN[x.getMonth()]}).join(", ")+(od.length>10?", …":"")+'</div>':'')+
      (e.status_note?'<div class="stnote'+(isOff(e)?" off":"")+'">'+esc(e.status_note)+'</div>':'')+
      '<div class="where">'+PIN+'<span>'+esc(e.venue||"")+(e.venue?", ":"")+esc(e.town)+(e.venue_address&&e.venue_address!==e.venue?'<br><small>'+esc(e.venue_address)+'</small>':'')+'</span></div>'+
      (p?'<div class="price">'+esc(p)+'</div>':'')+atRest(e)+hostLine(e)+
      (e.notes&&!/^(Quicket|Webtickets) category/.test(e.notes)?'<p class="mnotes">'+esc(e.notes)+'</p>':'')+
      '<div class="mact"><a class="btn" href="'+L+'" target="_blank" rel="noopener">'+blab(e)+ARROW+'</a>'+
        (navigator.share?'<button type="button" class="btn ghostbtn" data-act-direct="native">'+SHARE_ICON+'Share</button>':'')+
        '<a class="btn wa" href="'+esc(waUrl(e))+'" target="_blank" rel="noopener">'+WA_ICON+'WhatsApp</a>'+
        '<button type="button" class="btn ghostbtn" data-act-direct="copy">'+LINK_ICON+'Copy link</button></div>'+
      '<p class="msrc">Source: <a href="'+esc(e.source_url)+'" target="_blank" rel="noopener">'+esc(e.source_name)+'</a>'+(e.alt_sources&&e.alt_sources.length?' · also listed on '+e.alt_sources.length+' other site'+(e.alt_sources.length>1?"s":""):'')+' · checked '+esc(e.last_checked||"")+'</p>'+
    '</div>';
}
function openEvent(id,push){
  var e=byId(id);if(!e){S.event="";writeHash();return}
  closeMenu();S.event=id;
  var m=$("evModal");$("evBox").innerHTML='<button type="button" class="mclose" data-close aria-label="Close">×</button>'+detailHtml(e);
  $("evBox").dataset.id=id;
  if(m.hidden){openEvent._last=document.activeElement}
  m.hidden=false;document.body.classList.add("modal-open");
  writeHash();setTimeout(function(){var c=m.querySelector(".mclose");if(c)c.focus({preventScroll:true})},30);
}
function closeEvent(){var m=$("evModal");if(m.hidden)return;m.hidden=true;document.body.classList.remove("modal-open");S.event="";writeHash();
  if(openEvent._last&&openEvent._last.focus&&!/^(INPUT|TEXTAREA|SELECT)$/.test(openEvent._last.tagName))try{openEvent._last.focus({preventScroll:true})}catch(x){}}

function init(data){
  EV=(data||[]).slice().concat(RS);calcFreq();EVR={};RS.forEach(function(r){(r.event_ids||[]).forEach(function(id){EVR[id]=r})});
  $("built").textContent=window.EVENTS_BUILT||(EV[0]&&EV[0].last_checked)||"";
  var mo='<option value="">Any month</option>';MONTHS.forEach(function(m){mo+='<option value="'+m+'">'+monthLabel(m)+'</option>'});$("month").innerHTML=mo;
  readHash();buildTowns();syncControls();render();
  if(S.event){if($("evModal").hidden||$("evBox").dataset.id!==S.event)openEvent(S.event)}
}
function scoped(){return EV.filter(function(e){return (S.scope==="all"||e.garden_route)&&endOf(e)>=TODAY&&(S.off||!isOff(e))})}
function buildTowns(){
  var have={};scoped().forEach(function(e){have[e.town]=(have[e.town]||0)+1});
  function grp(label,order,isGR){
    var extra=Object.keys(have).filter(function(t){return order.indexOf(t)<0&&EV.some(function(e){return e.town===t&&!!e.garden_route===isGR})});
    /* Always list GR_ORDER / WIDE_ORDER towns (even with 0 events) so places like Still Bay stay pickable */
    var list=order.concat(extra.filter(function(t){return order.indexOf(t)<0}));
    if(!list.length)return "";
    return '<optgroup label="'+label+'">'+list.map(function(t){var n=have[t]||0;return '<option value="'+esc(t)+'">'+esc(t)+(n?" ("+n+")":"")+'</option>'}).join("")+'</optgroup>'}
  var h='<option value="">All towns</option>'+grp("Garden Route",GR_ORDER,true);
  if(S.scope==="all")h+=grp("Rest of the coast",WIDE_ORDER,false);
  $("town").innerHTML=h;if(S.town&&!(S.town in have)&&GR_ORDER.indexOf(S.town)<0&&WIDE_ORDER.indexOf(S.town)<0)S.town="";$("town").value=S.town;
}
function matches(e,ignoreMonth,anyStatus){
  if(S.scope==="gr"&&!e.garden_route)return false;
  if(!anyStatus&&!S.off&&isOff(e))return false;
  if(S.town&&e.town!==S.town)return false;
  if(S.cat&&e.category!==S.cat)return false;
  if(S.nye&&!e.nye)return false;
  if(S.xmas&&!e.xmas)return false;
  if(S.starred&&ME&&!isStar(e))return false;
  if(!ignoreMonth&&S.month&&!inMonth(e,S.month))return false;
  if(S.q){var hay=(e.title+" "+e.venue+" "+e.town+" "+e.venue_address+" "+e.notes+" "+e.region+" "+e.category+" "+(e.recurrence||"")+" "+(e._hay||"")).toLowerCase();
    if(!S.q.toLowerCase().split(/\s+/).every(function(w){return hay.indexOf(w)>=0}))return false}
  return true;
}
function filtered(ignoreMonth,includePast){
  return EV.filter(function(e){return matches(e,ignoreMonth)&&(includePast||endOf(e)>=TODAY)})
    .sort(function(a,b){return (b.garden_route-a.garden_route)||nextDate(a).localeCompare(nextDate(b))||a.title.localeCompare(b.title)});
}

function card(e){
  if(e._r)return rcard(e);
  var nd=pd(nextDate(e)),multi=!occ(e)&&e.end_date&&e.end_date!==e.start_date;
  var badge='<div class="datebadge"><span class="d">'+nd.getDate()+'</span><span class="m">'+MN[nd.getMonth()]+'</span>'+(multi?'<span class="to">to '+pd(e.end_date).getDate()+' '+MN[pd(e.end_date).getMonth()]+'</span>':'')+'</div>';
  var L=esc(link(e)),price=priceTxt(e.price_from);
  return '<article class="card'+(isOff(e)?" is-off":"")+(isStar(e)?" starred":"")+(isMine(e)?" myclub":"")+'">'+
    '<a class="thumb" href="'+L+'" target="_blank" rel="noopener" aria-label="'+esc(e.title)+'">'+thumb(e)+badge+'<span class="cat '+e.category+'">'+CATS[e.category]+'</span>'+(e.recurrence?'<span class="recur">↻ '+esc(e.recurrence.split(",")[0])+'</span>':'')+stBadge(e)+(window._cinOd&&isIndoorSc(e)?'<span class="intag">Indoor</span>':'')+'</a>'+
    '<div class="body">'+(S.scope==="all"&&e.garden_route?'<span class="grtag">Garden Route</span>':'')+
      clubTag(e)+'<div class="ttl"><h3><a href="'+L+'" target="_blank" rel="noopener">'+esc(e.title)+'</a></h3>'+starBtn(e)+'</div>'+
      '<div class="when">'+when(e)+(e.time?" · "+esc(e.time):"")+'<button type="button" class="wx" data-wx-town="'+esc(e.town||"")+'" data-wx-date="'+esc(nextDate(e))+'" data-wx-cat="'+esc(e.category||"")+'" hidden></button></div>'+
      (e.status_note?'<div class="stnote'+(isOff(e)?" off":"")+'">'+esc(e.status_note)+'</div>':'')+
      '<div class="where">'+PIN+'<span>'+esc(e.venue||"")+(e.venue?", ":"")+esc(e.town)+'</span></div>'+atRest(e)+hostLine(e)+
      (e.recurrence?'<div class="notes">'+esc(e.recurrence)+'</div>':(e.notes&&!/^(Quicket|Webtickets) category/.test(e.notes)?'<div class="notes">'+esc(e.notes)+'</div>':''))+
      '<div class="foot"><a class="btn" href="'+L+'" target="_blank" rel="noopener">'+blab(e)+ARROW+'</a>'+(price?'<span class="price">'+esc(price)+'</span>':'')+
      shareBtn(e)+'<a class="src" href="'+esc(e.source_url)+'" target="_blank" rel="noopener" title="Source: '+esc(e.source_name)+'">via '+esc(e.source_name.replace(/\s*\(.*\)$/,""))+'</a></div>'+
    '</div></article>';
}
var HOL={};(window.HOLIDAYS||[]).forEach(function(h){(HOL[h.date]=HOL[h.date]||[]).push(h)});
function holName(ds){return (HOL[ds]||[]).map(function(h){return h.name}).join(" · ")}
function holMonth(m){var k=Object.keys(HOL).filter(function(d){return d.slice(0,7)===m&&d>=TODAY}).sort();
  return k.length?'<div class="holbar"><span class="holk">Public holiday'+(k.length>1?'s':'')+'</span>'+k.map(function(d){var x=pd(d);return '<span class="holi"><b>'+DOW[x.getDay()]+' '+x.getDate()+' '+MN[x.getMonth()]+'</b> '+esc(holName(d))+'</span>'}).join("")+'</div>':''}
/* ---------- List ordering by how often an event repeats (display only) ----------
   freq = upcoming-or-past dates in the dataset for this event: its occurrences[] for series, else how many
   entries share the same normalised title+venue (or title prefix before ":"/" – " + venue, e.g. Galileo nights).
   Bucketed so similar events still read chronologically: 0 one-off/rare (1-3 dates), 1 monthly-ish (4-12), 2 weekly/frequent (13+ or "every <day>"). */
var FQ={};
function fkey(t){return (t||"").toLowerCase().replace(/\([^)]*\)/g," ").replace(/\b(19|20)\d\d\b|\b\d{1,2}(st|nd|rd|th)?\b|\b(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)[a-z]*\b/g," ").replace(/[^a-z\u00c0-\u024f]+/g," ").trim()}
function calcFreq(){var c={},p={};FQ={};
  EV.forEach(function(e){if(e._r)return;var v=fkey(e.venue),k=fkey(e.title)+"|"+v,m=(e.title||"").split(/:| [\u2013\u2014-] /)[0],pk=fkey(m).length>=6&&m.length<(e.title||"").length?fkey(m)+"|"+v:null;
    var n=occ(e)?occ(e).length:1;e._fk=k;e._pk=pk;c[k]=(c[k]||0)+n;if(pk)p[pk]=(p[pk]||0)+n});
  EV.forEach(function(e){if(e._r){e._fb=2;return}var f=Math.max(c[e._fk]||1,e._pk?(p[e._pk]||1):1);
    if(/\b(every|weekly|daily|each)\b|\b(mon|tues|wednes|thurs|fri|satur|sun)days\b/i.test(e.recurrence||""))f=Math.max(f,13);
    FQ[e.id]=f;e._fb=f<=3?0:f<=12?1:2});window.GRE_FREQ=FQ}
function ftier(e){return e._fb||0}
function tkey(e){var t=(e.time||"").match(/\d{1,2}[:h]\d{2}/);return t?("0"+t[0].replace("h",":")).slice(-5):"99"}
function byFreqDay(a,b){return ftier(a)-ftier(b)||(a._r?1:0)-(b._r?1:0)||tkey(a).localeCompare(tkey(b))||(a.title||a.name||"").localeCompare(b.title||b.name||"")}
function byFreq(a,b){return ftier(a)-ftier(b)||nextDate(a).localeCompare(nextDate(b))||(a.time||"").localeCompare(b.time||"")||a.title.localeCompare(b.title)}
function grouped(list,keep){
  if(!keep){var by={},ms=[];list.forEach(function(e){var m=nextDate(e).slice(0,7);if(!by[m]){by[m]=[];ms.push(m)}by[m].push(e)});
  ms.sort();list=[];ms.forEach(function(m){list=list.concat(by[m].sort(byFreq))})}
  var h="",cur="";
  list.forEach(function(e){var m=nextDate(e).slice(0,7);if(m!==cur){if(cur)h+='</div>';cur=m;h+='<div class="month">'+monthLabel(m)+'</div>'+holMonth(m)+'<div class="grid">'}h+=card(e)});
  return h+(cur?'</div>':'');
}
function renderList(){
  var A=filtered(false,false),L=A.filter(function(e){return !e._r}),R=A.filter(function(e){return e._r});
  $("count").textContent=countTxt(L.length,R.length);
  if(!A.length){$("view-list").innerHTML='<div class="empty"><b>'+(S.starred&&!Object.keys(STARS).length?"No liked events yet":"Nothing matches those filters")+'</b>'+(S.starred&&!Object.keys(STARS).length?'Tap the ☆ on any event to mark it as one you want to attend.':(S.scope==="gr"?'Try “All coast”, or clear a filter.':'Try clearing a filter.'))+'</div>';return}
  var gr=L.filter(function(e){return e.garden_route}),wide=L.filter(function(e){return !e.garden_route});
  var h="";
  if(!S.q&&!S.month&&!S.town&&L.length){
    var lim=iso(new Date(Date.now()+9*864e5));
    var soon=L.filter(function(e){var n=nextDate(e);return n>=TODAY&&n<=lim}).sort(function(a,b){return (b.garden_route-a.garden_route)||ftier(a)-ftier(b)||nextDate(a).localeCompare(nextDate(b))}).slice(0,14);
    /* Cinema coming-soon cards are not star-able and bypass matches()/isStar — omit them under the Liked filter. */
    var mv=S.starred?[]:soonMovies(lim),mix=soon.map(function(e){return {e:e,d:nextDate(e),gr:e.garden_route?1:0}}).concat(mv.map(function(x){return {m:x._m,d:x._d,gr:1}}))
      .sort(function(a,b){return (b.gr-a.gr)||((a.e?ftier(a.e):0)-(b.e?ftier(b.e):0))||a.d.localeCompare(b.d)});
    if(mix.length>2)h+='<div class="sec"><h2>Happening soon</h2><span class="pill">next 10 days</span></div><div class="soon">'+mix.map(function(x){return x.m?mcard(x.m,true):card(x.e)}).join("")+'</div>';
  }
  if(S.cat==="funrun"&&!S.starred&&!S.nye&&!S.xmas)h=clubSection()+h;
  var rgr=R.filter(function(e){return e.garden_route}),rwide=R.filter(function(e){return !e.garden_route});
  if(gr.length)h+='<div class="sec"><h2>Garden Route</h2><span class="pill">'+gr.length+'</span></div>'+grouped(gr);
  if(rgr.length)h+=restSection(rgr,"Garden Route restaurants &amp; pubs");
  if(wide.length)h+='<div class="sec"><h2>Rest of the coast</h2><span class="pill">'+wide.length+' · Cape Town – Jeffreys Bay</span></div>'+grouped(wide);
  if(rwide.length)h+=restSection(rwide,"Restaurants &amp; pubs, rest of the coast");
  $("view-list").innerHTML=h;
}
/* Browser bar colour (Chrome / Samsung Internet top bar; installed-PWA status bar). Replacing the tag makes every browser repaint. */
function setThemeColor(c){var o=document.querySelector('meta[name="theme-color"]');if(o&&o.getAttribute("content")===c)return;var m=document.createElement("meta");m.name="theme-color";m.content=c;if(o)o.parentNode.replaceChild(m,o);else document.head.appendChild(m)}
function clubSection(){
  if(!MYCLUB){
    if(ME)return '<div class="clubjoin" role="region" aria-label="Join a running club"><b>No club selected yet</b><button type="button" class="clubjoinbtn" data-club-join>Join a running club ›</button></div>';
    return '<div class="clubjoin" role="region" aria-label="Sign in to join a club"><b>Running clubs</b><a class="clubsignin" href="/login">Sign in to join a running club</a></div>';
  }
  var c=CLUBBY[MYCLUB];if(!c)return "";
  var up=EV.filter(function(e){return isMine(e)&&endOf(e)>=TODAY&&!isOff(e)&&(!S.town||e.town===S.town)&&(!S.month||inMonth(e,S.month))}).sort(function(a,b){return nextDate(a).localeCompare(nextDate(b))});
  return '<div class="sec clubsec"><h2>'+(c.logo?'<img class="clublogo" src="'+esc(c.logo)+'" alt="" width="36" height="36">':'')+'My club: '+esc(c.name)+'</h2>'+(c.asa===true?'<span class="ast ok">ASA registered</span>':c.asa===false?'<span class="ast no">Not ASA registered</span>':'<span class="ast unk" title="ASA affiliation not confirmed from a source">ASA status unconfirmed</span>')+(MYASA?'<span class="asano">'+(c.asa===true?'ASA':'Running')+' no. '+esc(MYASA)+'</span>':'')+'<span class="pill">'+(up.length?up.length+' upcoming':'none listed')+'</span><button type="button" class="clubchg" data-club-join>Change</button></div>'+
    (up.length?'<div class="soon">'+up.map(card).join("")+'</div>':'<div class="empty clubempty"><b>No upcoming '+esc(c.name)+' events found yet</b>We only list races and club runs we can find on a real source. When the club publishes a dated event, it will show up here.</div>')}
function renderCal(){
  if(!S.calMonth)S.calMonth=S.month||(MONTHS.indexOf(TODAY.slice(0,7))>=0?TODAY.slice(0,7):MONTHS[0]);
  var L=filtered(true,true);
  var p=S.calMonth.split("-"),y=+p[0],m=+p[1]-1;
  $("calTitle").textContent=MNL[m]+" "+y;
  var i=MONTHS.indexOf(S.calMonth);$("calPrev").disabled=i<=0;$("calNext").disabled=i>=MONTHS.length-1;
  var first=new Date(y,m,1),start=first.getDay(),days=new Date(y,m+1,0).getDate(); /* week starts Sunday */
  var h=DOW.map(function(d){return '<div class="dow">'+d+'</div>'}).join("");
  for(var k=0;k<start;k++)h+='<div class="day out"></div>';
  for(var d=1;d<=days;d++){
    var ds=iso(new Date(y,m,d));
    var on=L.filter(function(e){return onDay(e,ds)}).sort(byFreqDay);
    on=on.filter(isStar).concat(on.filter(function(e){return !isStar(e)}));
    var chips=on.slice(0,3).map(function(e){var cont=!occ(e)&&e.end_date&&e.start_date<ds;
      return '<div class="chip '+e.category+(e.garden_route?"":" wide")+(isOff(e)?" off":"")+(isStar(e)?" starc":"")+(isMine(e)?" clubc":"")+'" title="'+esc(e.title)+(STL[e.status]?" ("+STL[e.status]+")":"")+'">'+(isStar(e)?"★ ":"")+(cont?"↳ ":"")+(STL[e.status]?"<b>"+STL[e.status]+":</b> ":"")+esc(e.title)+(e._r&&e.day_labels&&e.day_labels[ds]?": "+esc(e.day_labels[ds]):"")+'</div>'}).join("");
    var dots='<span class="dots">'+on.slice(0,6).map(function(e){return '<i class="dot '+e.category+'"></i>'}).join("")+'</span>';
    var hn=holName(ds),st=on.filter(isStar),mc=on.filter(isMine);
    h+='<div class="day'+(hn?" hol":"")+(st.length?" star":"")+(mc.length?" club":"")+(on.length?" has":"")+(ds<TODAY?" past":"")+(ds===TODAY?" today":"")+(S.calDay===ds?" sel":"")+'" data-d="'+ds+'"'+(hn||st.length?' title="'+[hn?"Public holiday: "+esc(hn):"",st.length?"Want to attend: "+st.map(function(e){return esc(e.title)}).join(" · "):""].filter(Boolean).join(" | ")+'"':'')+'><span class="n">'+d+'</span>'+(hn?'<span class="holl"><span class="hollong">'+esc(hn)+'</span><span class="holshort">Holiday</span></span>':'')+(st.length?'<span class="stl"><span class="stlong">★ Want to attend'+(st.length>1?" ("+st.length+")":"")+'</span><span class="stshort">★ Going</span></span>':'')+(mc.length?'<span class="cll" title="Your club: '+esc(mc.map(function(e){return e.title}).join(" · "))+'">\u25CF My club</span>':'')+chips+(on.length>3?'<span class="more">+'+(on.length-3)+' more</span>':'')+dots+'</div>';
  }
  $("calGrid").innerHTML=h;
  var inm=L.filter(function(e){return inMonth(e,S.calMonth)&&(!e._r||occ(e))});
  $("count").textContent=countTxt(inm.filter(function(e){return !e._r}).length,inm.filter(function(e){return e._r}).length)+" in "+MNL[m];
  renderDay(L);
}
function renderDay(L){
  if(!S.calDay||S.calDay.slice(0,7)!==S.calMonth){$("calDay").innerHTML='<p class="resultline">Tap a day to see what\u2019s on.</p>';return}
  L=L||filtered(true,true);
  var on=L.filter(function(e){return onDay(e,S.calDay)}).sort(byFreqDay);
  var hn=holName(S.calDay),st=on.filter(isStar);on=st.concat(on.filter(function(e){return !isStar(e)}));
  $("calDay").innerHTML=(st.length?'<div class="starbar"><span class="stk">'+STAR_SVG+'Want to attend</span>'+st.map(function(e){return '<span class="sti">'+esc(e.title)+'</span>'}).join("")+'</div>':'')+(hn?'<div class="holbar"><span class="holk">Public holiday</span><span class="holi">'+esc(hn)+'</span><a class="holsrc" href="'+esc(HOL[S.calDay][0].source)+'" target="_blank" rel="noopener">gov.za</a></div>':'')+'<h3>'+fmt(pd(S.calDay),true)+' · '+countTxt(on.filter(function(e){return !e._r}).length,on.filter(function(e){return e._r}).length)+'</h3>'+(on.length?'<div class="grid">'+on.map(card).join("")+'</div>':'<p class="resultline">Nothing listed for this day.</p>');
}
function popup(g){
  return '<div class="pop">'+g.map(function(e){return '<div class="pe"><a class="pt" href="'+esc(link(e))+'" target="_blank" rel="noopener">'+thumb(e)+'</a><div class="pbody">'+clubTag(e)+'<div class="ttl"><h4>'+esc(e.title)+'</h4>'+starBtn(e)+'</div><p>'+when(e)+(e.time?" · "+esc(e.time):"")+'<br>'+esc(e.venue||"")+(e.venue?", ":"")+esc(e.town)+'</p>'+
    '<span class="pc '+e.category+'">'+CATS[e.category]+'</span>'+(STL[e.status]?'<span class="pc st'+(isOff(e)?" off":"")+'">'+STL[e.status]+'</span>':'')+(e.geo_source==="town centroid"?'<span style="font-size:.7rem;color:#888">approx.</span> ':'')+'<br><a class="go" href="'+esc(link(e))+'" target="_blank" rel="noopener">'+blab(e)+' →</a> <button type="button" class="go gshare" data-share="'+esc(e.id)+'">Share</button> <button type="button" class="go gshare" data-open="'+esc(e.id)+'">Details</button></div></div>'}).join("")+'</div>';
}
var FORK='<svg viewBox="0 0 24 24"><path d="M11 9H9V2H7v7H5V2H3v7c0 2.12 1.66 3.84 3.75 3.97V22h2.5v-9.03C11.34 12.84 13 11.12 13 9V2h-2v7zm5-3v8h2.5v8H21V2c-2.76 0-5 2.24-5 4z"/></svg>';
var PHONE='<svg viewBox="0 0 24 24"><path d="M6.6 10.8a15 15 0 006.6 6.6l2.2-2.2a1 1 0 011-.25 11.4 11.4 0 003.6.6 1 1 0 011 1V20a1 1 0 01-1 1A17 17 0 013 4a1 1 0 011-1h3.5a1 1 0 011 1c0 1.25.2 2.45.6 3.6a1 1 0 01-.25 1z"/></svg>';
function countTxt(n,r){return n+" event"+(n===1?"":"s")+(r?" · "+r+" restaurant"+(r===1?"":"s"):"")}
function mapsUrl(r){return "https://www.google.com/maps/search/?api=1&query="+encodeURIComponent(r.name+", "+r.address)}
function atRest(e){var r=EVR[e.id];return r?'<div class="atrest">'+FORK+'<span>At </span><button type="button" class="rlink" data-open="'+esc(r.id)+'">'+esc(r.name)+'</button></div>':''}
function rSections(r,full){
  var up=restEvents(r);
  return (r.phone?'<div class="where">'+PHONE+'<a href="tel:'+esc(r.phone.replace(/[^+\d]/g,""))+'">'+esc(r.phone)+'</a></div>':'')+
    (full?'<p class="rblurb">'+esc(r.blurb)+'</p>':'')+
    (r.specials&&r.specials.length?'<h4 class="rh">Specials</h4><ul class="rlist">'+r.specials.map(function(x){return '<li><b>'+esc(x[0])+'</b> '+esc(x[1])+'</li>'}).join("")+'</ul>':(full?'<h4 class="rh">Specials</h4><p class="rnone">None published</p>':''))+
    (r.music&&r.music.length?'<h4 class="rh">Live music &amp; recurring nights</h4><ul class="rlist">'+r.music.map(function(x){return '<li>'+esc(x)+'</li>'}).join("")+'</ul>':'')+
    (up.length?'<h4 class="rh">Upcoming in the app</h4><ul class="rlist rev">'+up.slice(0,full?8:3).map(function(e){return '<li><button type="button" class="rlink" data-open="'+esc(e.id)+'"><b>'+esc(fmt(pd(nextDate(e)),false))+'</b> '+esc(e.title)+(e.recurrence?' <span class="rrec">↻ '+esc(e.recurrence.split(",")[0])+'</span>':'')+'</button></li>'}).join("")+'</ul>':(full?'<h4 class="rh">Upcoming in the app</h4><p class="rnone">No dated events found</p>':''))}
function rcard(r){
  var site=r.website||r.source_url;
  return '<article class="card rcard" id="rest-'+esc(r.rid)+'">'+
    '<a class="thumb" href="#" data-open="'+esc(r.id)+'" aria-label="'+esc(r.name)+'">'+(r.image?'<img src="'+esc(r.image)+'" alt="" loading="lazy" decoding="async">':'<div class="ph restaurant">'+FORK+'</div>')+'<span class="cat restaurant">Restaurant</span>'+(r.recurrence?'<span class="recur">↻ '+esc(r.recurrence.split(";")[0].split(":")[0])+'</span>':'')+'</a>'+
    '<div class="body">'+(S.scope==="all"&&r.garden_route?'<span class="grtag">Garden Route</span>':'')+
    '<h3><a href="#" data-open="'+esc(r.id)+'">'+esc(r.name)+'</a></h3>'+
    '<div class="where">'+PIN+'<a href="'+esc(mapsUrl(r))+'" target="_blank" rel="noopener">'+esc(r.address)+'</a></div>'+
    rSections(r,false)+
    '<div class="foot"><button type="button" class="btn" data-open="'+esc(r.id)+'">Details'+ARROW+'</button>'+(site?'<a class="btn ghostbtn" href="'+esc(site)+'" target="_blank" rel="noopener">Website</a>':'')+shareBtn(r)+'</div>'+
    '</div></article>'}
function restDetail(r){
  var site=r.website||r.source_url;
  return '<div class="mhead">'+(r.image?'<img src="'+esc(r.image)+'" alt="">':'<div class="ph restaurant">'+FORK+'</div>')+'<span class="cat restaurant">Restaurant</span></div>'+
    '<div class="mbody">'+(r.garden_route?'<span class="grtag">Garden Route</span>':'')+
    '<h2 id="evTitle">'+esc(r.name)+'</h2>'+
    '<div class="where">'+PIN+'<span>'+esc(r.town)+'<br><small><a href="'+esc(mapsUrl(r))+'" target="_blank" rel="noopener">'+esc(r.address)+'</a></small></span></div>'+
    rSections(r,true)+
    (r.notes?'<p class="rnote">'+esc(r.notes)+'</p>':'')+
    '<div class="mact">'+(site?'<a class="btn" href="'+esc(site)+'" target="_blank" rel="noopener">Website'+ARROW+'</a>':'')+
      (navigator.share?'<button type="button" class="btn ghostbtn" data-act-direct="native">'+SHARE_ICON+'Share</button>':'')+
      '<a class="btn wa" href="'+esc(waUrl(r))+'" target="_blank" rel="noopener">'+WA_ICON+'WhatsApp</a>'+
      '<button type="button" class="btn ghostbtn" data-act-direct="copy">'+LINK_ICON+'Copy link</button></div>'+
    '<p class="msrc">Checked '+esc(r.last_checked)+' · Sources: '+(r.sources||[]).map(function(x){return '<a href="'+esc(x.url)+'" target="_blank" rel="noopener">'+esc(x.name)+'</a>'}).join(" · ")+'</p>'+
    '</div>'}
function restSection(R,label){
  R=R.slice().sort(function(a,b){var O=GR_ORDER.concat(WIDE_ORDER),ia=O.indexOf(a.town),ib=O.indexOf(b.town);return ((ia<0?99:ia)-(ib<0?99:ib))||a.name.localeCompare(b.name)});
  return '<div class="sec"><h2>'+label+'</h2><span class="pill">'+R.length+'</span></div><p class="rintro">Specials, live music and recurring nights from each venue\u2019s own site and local listings (checked '+esc(R[0].last_checked)+'). Things change, so call ahead.</p><div class="grid rgrid">'+R.map(rcard).join("")+'</div>'}
/* ---------- Cinema tab: Ster-Kinekor Garden Route Mall (George) from data/cinema.js + outdoor screenings from the events data ---------- */
var CIN=window.CINEMA||null;
var PLAY='<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M8 5v14l11-7z"/></svg>';
var REEL='<svg viewBox="0 0 24 24"><path d="M18 4l2 4h-3l-2-4h-2l2 4h-3l-2-4H8l2 4H7L5 4H4a2 2 0 00-2 2v12a2 2 0 002 2h16a2 2 0 002-2V4z"/></svg>';
function relTxt(f){return f.release_date?fmt(pd(f.release_date),true):(f.date_label||"")}
function mmeta(f){return [f.age_rating,f.runtime,(f.genres||[]).join(", ")].filter(Boolean).map(esc).join(" · ")}
function mcard(f,soonTag){
  var d=f.release_date?pd(f.release_date):null,L=esc(f.url),cn=CIN&&CIN.cinema?CIN.cinema:{name:"Ster-Kinekor Garden Route Mall",town:"George"};
  var badge=d&&(soonTag||f.section==="soon")?'<div class="datebadge"><span class="d">'+d.getDate()+'</span><span class="m">'+MN[d.getMonth()]+'</span></div>':'';
  return '<article class="card mcard">'+
    '<div class="mtw"><a class="thumb" href="'+L+'" target="_blank" rel="noopener" aria-label="'+esc(f.title)+'">'+(f.poster?'<img src="'+esc(f.poster)+'" alt="" loading="lazy" decoding="async" referrerpolicy="no-referrer">':'<div class="ph film">'+ICON.film+'</div>')+badge+
      (soonTag?'<span class="cat film">New at the cinema</span>':'')+'</a>'+
      (soonTag?'':'<button type="button" class="minfo" data-film="'+f.id+'" aria-label="Film info: '+esc(f.title)+'"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2a10 10 0 100 20 10 10 0 000-20zm1 15h-2v-6h2zm0-8h-2V7h2z"/></svg></button><span class="mbadges"'+(rbadges(f)?' aria-label="'+esc(ratingsLabel(f))+'"':' aria-hidden="true"')+'>'+rbadges(f)+'</span>')+'</div>'+
    '<div class="body">'+
      '<h3><a href="'+L+'" target="_blank" rel="noopener">'+esc(f.title)+'</a></h3>'+
      '<div class="when">'+(f.section==="soon"||soonTag?"Opens "+esc(relTxt(f)):(f.release_date&&f.release_date>TODAY?"Opens "+esc(relTxt(f)):"Showing now"))+'</div>'+
      (mmeta(f)?'<div class="mmeta">'+mmeta(f)+'</div>':'')+
      (soonTag?'<div class="where">'+PIN+'<span>'+esc((f.cinemas&&f.cinemas[0])||cn.name)+', '+esc(cn.town)+'</span></div>':'')+
      '<div class="foot"><a class="btn" href="'+L+'" target="_blank" rel="noopener">'+(f.bookable?"Tickets":"Film page")+ARROW+'</a>'+(f.trailer?'<a class="btn trailerbtn" href="'+esc(f.trailer)+'" target="_blank" rel="noopener" aria-label="Trailer: '+esc(f.title)+'">'+PLAY+'Trailer</a>':'')+(soonTag?'<a class="src" href="'+L+'" target="_blank" rel="noopener" title="Source: Ster-Kinekor">via Ster-Kinekor</a>':'')+'</div>'+
    '</div></article>'}
function soonMovies(lim){ /* new releases opening at SK George inside the happening-soon window (List view only) */
  if(!CIN||(S.cat&&S.cat!=="film")||S.nye||S.xmas)return [];
  return (CIN.now_showing||[]).concat(CIN.coming_soon||[]).filter(function(f){return f.release_date&&f.release_date>=TODAY&&f.release_date<=lim})
    .map(function(f){return {_m:f,_d:f.release_date}})}
function isOpenPlan(e){return /open ?plan pictures/i.test(e.title+" "+(e.venue||"")+" "+(e.notes||"")+" "+(e.source_name||"")+" "+(e.organiser||"")+" "+(e.url||""))}
function isIndoorSc(e){return /^indoor/i.test(e.notes||"")||/blue shed/i.test(e.venue||"")}
function isOutdoor(e){if(isOpenPlan(e))return true;return e.category==="film"&&!/^indoor/i.test(e.notes||"")&&/open[- ]?air|outdoor|drive[- ]?in|under the stars|moonlight|starlight|galileo|picnic cinema|movies? (in|on) the (park|beach|lawn)/i.test(e.title+" "+(e.notes||"")+" "+(e.source_name||"")+" "+(e.venue||""))}
/* ---------- IMDb / Rotten Tomatoes badges (data: f.ratings from tools/ratings.py) ---------- */
var TOMATO='<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="13.5" r="8.5" fill="#fa320a"/><path d="M12 5.2c-.6-1.6-2-2.5-3.6-2.4 1 .5 1.7 1.3 2 2.3-1.3-.6-2.8-.5-4 .3 1.4.1 2.6.8 3.3 1.8L12 6l2.3 1.2c.7-1 1.9-1.7 3.3-1.8-1.2-.8-2.7-.9-4-.3.3-1 1-1.8 2-2.3-1.6-.1-3 .8-3.6 2.4z" fill="#00912d"/></svg>';
var SPLAT='<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2l1.8 4.6 4.6-2.4-1.6 4.9 5 .9-4.2 2.9 3.9 3.3-5.1.2.8 5-4.2-3-3 4.1-.9-5-4.9 1.2 2.6-4.4L2.3 12l4.9-1.3-2.4-4.5 4.8 1.6z" fill="#0ac855"/></svg>';
function rget(f,src){var r=(f.ratings||[]).filter(function(x){return x.source===src&&x.value})[0];return r?r.value:""}
function rtIcon(v){return parseInt(v,10)>=60?TOMATO:SPLAT}
function rbadges(f){var im=rget(f,"IMDb"),rt=rget(f,"Rotten Tomatoes");
  return (im?'<span class="bimdb"><b>IMDb</b>'+esc(im)+'</span>':'')+(rt?'<span class="brt">'+rtIcon(rt)+esc(rt)+'</span>':'')}
function ratingsLabel(f){var a=[],im=rget(f,"IMDb"),rt=rget(f,"Rotten Tomatoes");if(im)a.push("IMDb "+im);if(rt)a.push("Rotten Tomatoes "+rt);return a.join(", ")}
/* ---------- film detail overlay (ⓘ on Cinema posters) ---------- */
function filmById(id){if(!CIN)return null;var A=(CIN.now_showing||[]).concat(CIN.coming_soon||[]);for(var i=0;i<A.length;i++)if(String(A[i].id)===String(id))return A[i];return null}
function filmHtml(f){
  var cn=CIN&&CIN.cinema?CIN.cinema:{name:"Ster-Kinekor Garden Route Mall",town:"George"};
  var nu=/^No Under/i.test(f.age_rating||"")&&f.age,rt=(f.age_rating||"").replace(/^No Under \d+'s\s*-?\s*/i,"");
  var d=f.release_date?pd(f.release_date):null,opened=d&&f.release_date<=TODAY;
  var when=d?(opened?"Opened "+fmt(d,true)+(f.section==="now"?" · Showing now":""):"Opens "+fmt(d,true)):(f.section==="now"?"Showing now":"");
  var ratings=(f.ratings||[]).filter(function(r){return r&&r.value});
  return '<div class="fhero">'+(f.backdrop?'<img class="fbd" src="'+esc(f.backdrop)+'" alt="" referrerpolicy="no-referrer">':'<div class="fbd ph film">'+ICON.film+'</div>')+
      '<button type="button" class="fclose" data-fclose aria-label="Close">×</button></div>'+
    '<div class="fbody"><div class="ftop">'+(f.poster?'<img class="fposter" src="'+esc(f.poster)+'" alt="" referrerpolicy="no-referrer">':'')+
      '<div class="fmeta"><h2 id="filmTitle">'+esc(f.title)+'</h2>'+
      (f.age_rating?'<div class="frate">'+(nu?'<span class="fage">'+esc(f.age)+'</span>'+esc(f.age_rating.split(" - ")[0]):esc(f.age_rating.split(" - ")[0]))+'</div>':'')+
      '<div class="fline">'+[f.runtime,(f.genres||[]).map(function(g){return g.charAt(0).toUpperCase()+g.slice(1)}).join(", ")].filter(Boolean).map(esc).join(" · ")+'</div>'+
      (when?'<div class="fline">'+esc(when)+'</div>':'')+'</div></div>'+
      (ratings.length?'<div class="fratings">'+ratings.map(function(r){var rt=r.source==="Rotten Tomatoes";return '<div class="fr'+(rt?' frt':' fim')+'"><b>'+(rt?rtIcon(r.value):'')+esc(r.value)+'</b><span>'+esc(r.source)+'</span></div>'}).join("")+'</div>':'')+
      '<div class="fact"><a class="btn" href="'+esc(f.url)+'" target="_blank" rel="noopener">'+(f.bookable?"Tickets":"Film page")+ARROW+'</a>'+(f.trailer?'<a class="btn trailerbtn" href="'+esc(f.trailer)+'" target="_blank" rel="noopener">'+PLAY+'Trailer</a>':'')+'</div>'+
      (f.synopsis?'<h4 class="fh">Synopsis</h4>'+f.synopsis.split(/\n\n+/).map(function(p){return '<p class="fsyn">'+esc(p)+'</p>'}).join(""):'')+
      (f.director?'<h4 class="fh">Director</h4><p class="fp">'+esc(f.director)+'</p>':'')+
      (f.cast&&f.cast.length?'<h4 class="fh">Cast</h4><div class="fcast">'+f.cast.map(function(c){return '<span>'+esc(c)+'</span>'}).join("")+'</div>':'')+
      (rt?'<h4 class="fh">Classification</h4><p class="fp">'+esc(f.age_rating)+'</p>':'')+
      '<h4 class="fh">Showing at</h4><p class="fp">'+esc(cn.name)+', '+esc(cn.town)+'</p>'+
      '<p class="fsrc">Synopsis, cast, poster &amp; trailer: <a href="'+esc(f.url)+'" target="_blank" rel="noopener">Ster-Kinekor</a> · updated '+esc((CIN&&CIN.fetched_at)||"")+
        (ratings.length?' · Ratings: '+(f.imdb_id?'<a href="https://www.imdb.com/title/'+esc(f.imdb_id)+'/" target="_blank" rel="noopener">IMDb</a>':'IMDb')+', Rotten Tomatoes ('+esc((f.ratings_source||"").replace(/^.*?,\s*/,""))+')':'')+'</p>'+
    '</div>'}
function openFilm(id,noPush){
  var f=filmById(id);if(!f)return;var ov=$("filmOv");
  ov.innerHTML='<div class="fsheet" role="dialog" aria-modal="true" aria-labelledby="filmTitle">'+filmHtml(f)+'</div>';
  ov.hidden=false;ov.scrollTop=0;document.body.classList.add("modal-open");openFilm._open=String(id);
  if(!noPush){try{history.pushState({film:String(id)},"",location.href);openFilm._pushed=true}catch(x){openFilm._pushed=false}}
  setTimeout(function(){var c=ov.querySelector(".fclose");if(c)c.focus({preventScroll:true})},30)}
function hideFilm(){var ov=$("filmOv");if(ov.hidden)return;ov.hidden=true;ov.innerHTML="";openFilm._open="";if($("evModal").hidden)document.body.classList.remove("modal-open")}
function closeFilm(){if($("filmOv").hidden)return;if(openFilm._pushed&&history.state&&history.state.film){openFilm._pushed=false;history.back()}else hideFilm()}
window.openFilm=openFilm;window.closeFilm=closeFilm;
function bindFilm(){
  var ov=$("filmOv");
  ov.addEventListener("click",function(ev){if(ev.target.closest("[data-fclose]")||ev.target===ov)closeFilm()});
  window.addEventListener("popstate",function(){if(!$("filmOv").hidden)hideFilm()});
  document.addEventListener("keydown",function(ev){if(ev.key==="Escape"&&!$("filmOv").hidden){ev.stopImmediatePropagation();closeFilm()}},true);
  var y0=null,dy=0,sh=null;
  ov.addEventListener("touchstart",function(ev){sh=ov.querySelector(".fsheet");if(ov.scrollTop<=0&&ev.touches.length===1){y0=ev.touches[0].clientY;dy=0}else y0=null},{passive:true});
  ov.addEventListener("touchmove",function(ev){if(y0==null||!sh)return;dy=ev.touches[0].clientY-y0;if(dy>0){sh.style.transition="none";sh.style.transform="translateY("+dy+"px)";sh.style.opacity=String(Math.max(.4,1-dy/600))}},{passive:true});
  ov.addEventListener("touchend",function(){if(y0==null||!sh)return;sh.style.transition="";if(dy>110){sh.style.transform="translateY(100%)";setTimeout(closeFilm,180)}else{sh.style.transform="";sh.style.opacity=""}y0=null});
}
function loadCinema(){ /* fallback when data/cinema.js didn't load (old cache, blocked script): fetch the JSON once */
  if(CIN||loadCinema._busy)return;loadCinema._busy=true;
  fetch("data/cinema.json",{cache:"no-cache"}).then(function(r){return r.ok?r.json():null}).then(function(d){
    if(d&&(d.now_showing||d.coming_soon)){CIN=window.CINEMA=d;if(S.view==="cinema"||S.view==="list")render()}else loadCinema._failed=true
  }).catch(function(){loadCinema._failed=true;if(S.view==="cinema")renderCinema()}).then(function(){loadCinema._busy=false})}
function renderCinema(){
  try{renderCinema2()}catch(err){
    $("view-cinema").innerHTML='<div class="empty"><b>Couldn\u2019t show the cinema listings</b>Try reloading the page. <a href="https://www.sterkinekor.com/cinemas/garden-route" target="_blank" rel="noopener">Ster-Kinekor Garden Route Mall programme →</a></div>';
    if(window.console)console.error(err)}}
function renderCinema2(){
  if(!CIN)loadCinema();
  var h='',now=CIN?(CIN.now_showing||[]):[],cs=CIN?(CIN.coming_soon||[]).filter(function(f){return !f.release_date||f.release_date>=TODAY}):[];
  var od=EV.filter(function(e){return !e._r&&isOutdoor(e)&&endOf(e)>=TODAY&&(S.off||!isOff(e))});
  var odGR=od.filter(function(e){return e.garden_route}),odW=od.filter(function(e){return !e.garden_route});
  var showW=S.scope==="all"||S.gal,odL=(showW?odGR.concat(odW):odGR).sort(function(a,b){return (b.garden_route-a.garden_route)||nextDate(a).localeCompare(nextDate(b))||a.title.localeCompare(b.title)});
  var sub=renderCinema.sub||(function(){try{return localStorage.getItem("gre-cinsub")}catch(e){return null}})()||"sk";if(sub!=="sk"&&sub!=="od")sub="sk";renderCinema.sub=sub;
  h+='<div class="seg cinseg" role="tablist" aria-label="Cinema listings"><button type="button" role="tab" data-cinsub="sk" aria-selected="'+(sub==="sk")+'" class="'+(sub==="sk"?"on":"")+'">Ster-Kinekor</button><button type="button" role="tab" data-cinsub="od" aria-selected="'+(sub==="od")+'" class="'+(sub==="od"?"on":"")+'">Outdoor</button></div>';
  $("count").textContent=now.length+" now showing · "+cs.length+" coming soon · "+odL.length+" outdoor screening"+(odL.length===1?"":"s");
  if(sub==="sk"){
  if(CIN&&CIN.cinema){var c=CIN.cinema;
    h+='<details class="cinhead"'+(renderCinema._open?' open':'')+'><summary><span class="cinlogo">'+REEL+'</span><span class="cinname">'+esc(c.name)+'<span class="cintown">, '+esc(c.town||"George")+'</span></span><svg class="chev" viewBox="0 0 24 24" aria-hidden="true"><path d="M7.4 8.6L12 13.2l4.6-4.6L18 10l-6 6-6-6z"/></svg></summary>'+
      '<div class="cinmore"><p>'+esc(c.address)+(c.phone?' · <a href="tel:'+esc(c.phone.replace(/[^+\d]/g,""))+'">'+esc(c.phone)+'</a>':'')+'</p>'+
      '<p class="cinupd">Programme from <a href="'+esc(c.url)+'" target="_blank" rel="noopener">sterkinekor.com</a> · last updated '+esc(CIN.fetched_at||"")+'. Showtimes change daily, so check times and book on Ster-Kinekor.</p></div></details>'}
  else h+='<div class="empty cinempty"><b>'+(loadCinema._failed?'Cinema listings unavailable':'Loading Ster-Kinekor listings\u2026')+'</b>'+(loadCinema._failed?'Couldn\u2019t load the Ster-Kinekor programme. ':'')+'<a href="https://www.sterkinekor.com/cinemas/garden-route" target="_blank" rel="noopener">See it on sterkinekor.com →</a> Outdoor screenings are under the Outdoor tab.</div>';
  if(CIN){
    h+='<div class="sec"><h2>Now showing</h2><span class="pill">'+now.length+' · Ster-Kinekor George</span></div>'+(now.length?'<div class="grid mgrid">'+now.map(function(f){return mcard(f)}).join("")+'</div>':'<p class="rintro">No films listed right now.</p>');
    var g=cs.length?'<div class="grid mgrid">'+cs.map(function(f){return mcard(f)}).join("")+'</div>':'';
    h+='<div class="sec"><h2>Coming soon</h2><span class="pill">'+cs.length+' · with opening dates</span></div><p class="rintro">Opening dates at Ster-Kinekor Garden Route Mall, as listed on sterkinekor.com. Opera, ballet and concert screenings are usually one-off dates.</p>'+(g||'<p class="rintro">Nothing announced yet.</p>');
  }
  }else{
  h+='<div class="sec"><h2>Outdoor cinema</h2><span class="pill">'+odL.length+(showW?' · Garden Route + rest of coast':' · Garden Route')+'</span></div>'+
    '<p class="rintro">Open-air and drive-in screenings, plus every Open Plan Pictures night (indoor ones are tagged).'+(S.scope!=="all"&&odW.length?' <button type="button" class="ghost galtoggle" id="galToggle" aria-pressed="'+(S.gal?"true":"false")+'">'+(S.gal?"Hide":"Show")+' Cape Town (Galileo) · '+odW.length+'</button>':'')+
    ' <button type="button" class="rlink" id="filmChip">All film nights (incl. indoor) →</button></p>'+
    (odL.length?(window._cinOd=1,(function(x){window._cinOd=0;return x})(grouped(odL,1))):'<p class="rintro">No outdoor screenings listed for the Garden Route right now.</p>');
  }
  $("view-cinema").innerHTML=h;
}
var COL={concert:"#2a6f97",festival:"#a02a9a",musical:"#8e4ec6",market:"#5b8c2a",funrun:"#e5530a",community:"#b7791f",arts:"#0f766e",quiz:"#4f46e5",festive:"#b4233c",nature:"#15803d",sport:"#0e7490",film:"#374151",restaurant:"#5b2a86"};
var GRB=[[-33.55,21.95],[-34.2,24.0]];
function renderMap(){
  var L=filtered(false,false).filter(function(e){return e.lat!=null&&e.lng!=null});
  $("count").textContent=countTxt(L.filter(function(e){return !e._r}).length,L.filter(function(e){return e._r}).length)+" on the map";
  if(typeof window.L==="undefined"){$("map").innerHTML='<div class="empty"><b>Map unavailable offline</b>The list and calendar still work.</div>';return}
  if(!map){map=window.L.map("map",{scrollWheelZoom:true,zoomControl:true}).fitBounds(S.scope==="all"?[[-33.5,18.3],[-34.4,25.0]]:GRB);
    window.L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",{maxZoom:18,attribution:'&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'}).addTo(map);
    layer=window.L.layerGroup().addTo(map)}
  layer.clearLayers();
  var groups={};L.forEach(function(e){var k=(+e.lat).toFixed(4)+","+(+e.lng).toFixed(4);(groups[k]=groups[k]||[]).push(e)});
  var wide=[],gr=[];Object.keys(groups).forEach(function(k){var g=groups[k];(g.some(function(e){return e.garden_route})?gr:wide).push(g)});
  function add(g){var isgr=g.some(function(e){return e.garden_route});var c=COL[g[0].category]||"#555";
    var mk=window.L.circleMarker([+g[0].lat,+g[0].lng],isgr?{radius:Math.min(9+g.length,17),color:"#fff",weight:2.5,fillColor:c,fillOpacity:.95}:{radius:5,color:"#6f817a",weight:1,fillColor:"#9aaba3",fillOpacity:.55});
    mk.bindPopup(popup(g),{maxWidth:300,minWidth:280});mk.bindTooltip(g.length>1?g.length+" events · "+esc(g[0].venue||g[0].town):esc(g[0].title));mk.addTo(layer)}
  wide.forEach(add);gr.forEach(add);
  setTimeout(function(){map.invalidateSize()},60);
}
function stats(){
  var L=scoped();var by={};L.forEach(function(e){by[e.category]=(by[e.category]||0)+1});var nev=L.length-(by.restaurant||0);
  $("stats").innerHTML='<span class="stat"><b>'+nev+'</b> '+(S.scope==="gr"?"Garden Route":"coastal")+' events</span>'+
    ["concert","festival","market","funrun","musical","arts","quiz","festive","nature","sport","film","community","restaurant"].filter(function(c){return by[c]}).map(function(c){return '<span class="stat"><b>'+by[c]+'</b> '+CATPL[c]+'</span>'}).join("");
}
function render(){
  ["list","cal","map","cinema"].forEach(function(v){$("view-"+v).hidden=S.view!==v});
  document.body.classList.toggle("view-cinema",S.view==="cinema");
  var run=S.cat==="funrun"&&S.view!=="cinema";document.body.classList.toggle("theme-run",run);setThemeColor(run?"#2a1206":"#0d3b2e");

  Array.prototype.forEach.call(document.querySelectorAll(".views button"),function(b){b.classList.toggle("on",b.dataset.view===S.view)});
  var ft=$("filtToggle");if(ft)ft.classList.toggle("has-active",document.body.classList.contains("filters-hidden")&&filtersActive());
  Array.prototype.forEach.call(document.querySelectorAll("#catChips button"),function(b){b.classList.toggle("on",b.dataset.starred?!!S.starred:b.dataset.nye?!!S.nye:b.dataset.xmas?!!S.xmas:b.dataset.cat===S.cat);if(b.dataset.starred)b.setAttribute("aria-pressed",!!S.starred)});
  stats();
  var af=[];if(S.starred)af.push("★ Liked");if(S.xmas)af.push("Christmas");if(S.nye)af.push("New Year's Eve");if(S.town)af.push(S.town);if(S.month)af.push(monthLabel(S.month));if(S.q)af.push("“"+S.q+"”");
  $("activeFilters").textContent=af.length?"· "+af.join(" · "):"";
  var hid=EV.filter(function(e){return isOff(e)&&endOf(e)>=TODAY&&matches(e,S.view==="cal",true)}).length;
  $("offToggle").hidden=!hid;$("offToggle").textContent=S.off?"Hide postponed/cancelled ("+hid+")":hid+" postponed/cancelled hidden · show";
  if(S.view==="list")renderList();else if(S.view==="cal")renderCal();else if(S.view==="cinema")renderCinema();else renderMap();
  if(S.view!=="cal")wxHydrate();
  writeHash();
}
function syncControls(){
  if($("q").value!==S.q)$("q").value=S.q;$("month").value=S.month;$("town").value=S.town;
  $("scopeGR").classList.toggle("on",S.scope==="gr");$("scopeAll").classList.toggle("on",S.scope==="all");
  $("scopeGR").setAttribute("aria-pressed",S.scope==="gr");$("scopeAll").setAttribute("aria-pressed",S.scope==="all");
}
function writeHash(){var p=[];if(S.view!=="list")p.push("view="+S.view);if(S.scope!=="gr")p.push("scope=all");if(S.off)p.push("off=1");if(S.gal)p.push("gal=1");if(S.nye)p.push("nye=1");if(S.xmas)p.push("xmas=1");if(S.starred)p.push("starred=1");if(S.event)p.push("event="+encodeURIComponent(S.event));
  ["town","cat","month","q"].forEach(function(k){if(S[k])p.push(k+"="+encodeURIComponent(S[k]))});
  var h=p.length?"#"+p.join("&"):"";if(location.hash!==h)history.replaceState(null,"",h||location.pathname+location.search)}
function readHash(){location.hash.replace(/^#/,"").split("&").forEach(function(kv){var a=kv.split("=");if(!a[0])return;var v=decodeURIComponent(a[1]||"");
  if(a[0]==="view"&&/^(list|cal|map|cinema)$/.test(v))S.view=v;else if(a[0]==="gal"&&v==="1")S.gal=true;else if(a[0]==="view"&&v==="rest")S.cat="restaurant";else if(a[0]==="rest")S.event="r:"+v;else if(a[0]==="scope"&&v==="all")S.scope="all";else if(a[0]==="off"&&v==="1")S.off=true;else if(a[0]==="nye"&&v==="1")S.nye=true;else if(a[0]==="xmas"&&v==="1")S.xmas=true;else if(a[0]==="starred"&&v==="1")S.starred=true;else if(a[0]==="event")S.event=v;else if(/^(town|cat|month|q)$/.test(a[0]))S[a[0]]=v})}
function setScope(s){S.scope=s;buildTowns();syncControls();render();if(map)map.fitBounds(s==="all"?[[-33.5,18.3],[-34.4,25.0]]:GRB)}
var INTRO_KEY="gre.hideIntro";
function setIntroHidden(hide){
  document.body.classList.toggle("intro-hidden",!!hide);
  var b=$("introToggle");if(!b)return;
  b.setAttribute("aria-expanded",hide?"false":"true");
  b.title=hide?"Show intro":"Hide intro";
  var lbl=b.querySelector(".introlbl");if(lbl)lbl.textContent=hide?"Intro":"Hide intro";
  try{localStorage.setItem(INTRO_KEY,hide?"1":"0")}catch(e){}
}
function initIntroToggle(){
  var hide=false;
  try{hide=localStorage.getItem("gre.introSeen")==="1";localStorage.setItem("gre.introSeen","1")}catch(e){}
  setIntroHidden(hide);
  $("introToggle").addEventListener("click",function(){setIntroHidden(!document.body.classList.contains("intro-hidden"))});
}
var FILT_KEY="gre.hideFilters2";
function filtersActive(){return !!(S.q||S.town||S.cat||S.month||S.nye||S.xmas||S.starred||S.scope!=="gr"||S.off)}
function setFiltersHidden(hide){
  document.body.classList.toggle("filters-hidden",!!hide);
  var b=$("filtToggle");if(!b)return;
  b.setAttribute("aria-expanded",hide?"false":"true");
  b.title=hide?"Show filters":"Hide filters";
  var lbl=b.querySelector(".filtlbl");if(lbl)lbl.textContent=hide?"Filters":"Hide filters";
  b.classList.toggle("has-active",!!hide&&filtersActive());
  try{localStorage.setItem(FILT_KEY,hide?"1":"0")}catch(e){}
}
function initFiltersToggle(){
  var hide=true;
  try{hide=localStorage.getItem(FILT_KEY)!=="0"}catch(e){}
  setFiltersHidden(hide);
  $("filtToggle").addEventListener("click",function(){setFiltersHidden(!document.body.classList.contains("filters-hidden"))});
}
function bind(){
  var t;$("q").addEventListener("input",function(){var v=this.value.trim();clearTimeout(t);t=setTimeout(function(){S.q=v;render()},120)});
  $("town").addEventListener("change",function(){S.town=this.value;render()});
  $("month").addEventListener("change",function(){S.month=this.value;if(S.month){S.calMonth=S.month;S.calDay=null}render()});
  $("scopeGR").addEventListener("click",function(){setScope("gr")});
  $("scopeAll").addEventListener("click",function(){setScope("all")});
  $("offToggle").addEventListener("click",function(){S.off=!S.off;buildTowns();syncControls();render()});
  $("reset").addEventListener("click",function(){S.q=S.town=S.cat=S.month="";S.nye=false;S.xmas=false;S.starred=false;S.calDay=null;buildTowns();syncControls();render()});
  Array.prototype.forEach.call(document.querySelectorAll("#catChips button"),function(b){b.addEventListener("click",function(){if(b.dataset.starred)S.starred=!S.starred;else if(b.dataset.nye)S.nye=!S.nye;else if(b.dataset.xmas)S.xmas=!S.xmas;else S.cat=b.dataset.cat;render()})});
  Array.prototype.forEach.call(document.querySelectorAll(".views button"),function(b){b.addEventListener("click",function(){S.view=b.dataset.view;render();toTop();requestAnimationFrame(toTop)})});
  $("calPrev").addEventListener("click",function(){var i=MONTHS.indexOf(S.calMonth);if(i>0){S.calMonth=MONTHS[i-1];renderCal()}});
  $("calNext").addEventListener("click",function(){var i=MONTHS.indexOf(S.calMonth);if(i<MONTHS.length-1){S.calMonth=MONTHS[i+1];renderCal()}});
  $("calGrid").addEventListener("click",function(ev){var d=ev.target.closest(".day[data-d]");if(!d)return;S.calDay=d.dataset.d;renderCal();$("calDay").scrollIntoView({behavior:"smooth",block:"nearest"})});
  /* never leave a text field focused after tapping something else (stops the phone keyboard re-opening on tab/calendar taps) */
  function isText(el){return el&&(el.tagName==="INPUT"&&!/^(button|submit|checkbox|radio|range|color|file|reset)$/i.test(el.type)||el.tagName==="TEXTAREA"||el.isContentEditable)}
  document.addEventListener("pointerdown",function(ev){var a=document.activeElement;if(isText(a)&&!isText(ev.target)&&!(ev.target.closest&&ev.target.closest("label")))a.blur()},true);
  $("q").addEventListener("keydown",function(ev){if(ev.key==="Enter")this.blur()});
  document.addEventListener("click",function(ev){
    var sb=ev.target.closest&&ev.target.closest("[data-star]");
    if(sb){ev.preventDefault();ev.stopPropagation();toggleStar(sb.dataset.star);return}
    var t=ev.target.closest("[data-share],[data-open],[data-act],[data-act-direct],[data-close]");
    if(!t){if(!ev.target.closest("#shareMenu"))closeMenu();if(ev.target.id==="evModal")closeEvent();return}
    if(t.hasAttribute("data-close")){closeEvent();return}
    if(t.dataset.share){ev.preventDefault();ev.stopPropagation();openMenu(t,t.dataset.share);return}
    if(t.dataset.open){ev.preventDefault();if(map)map.closePopup();openEvent(t.dataset.open);return}
    var id=t.dataset.actDirect?$("evBox").dataset.id:$("shareMenu").dataset.id,e=byId(id);if(!e)return;
    var act=t.dataset.act||t.dataset.actDirect;
    if(act==="native"){if(!nativeShare(e))copy(deep(e))}
    else if(act==="copy")copy(deep(e));
    else if(act==="details"){if(map)map.closePopup();openEvent(id)}
    if(t.dataset.act)closeMenu();
  },true);
  $("view-cinema").addEventListener("click",function(ev){
    var fi=ev.target.closest("[data-film]");if(fi){ev.preventDefault();openFilm(fi.dataset.film);return}
    var cs=ev.target.closest("[data-cinsub]");if(cs){renderCinema.sub=cs.dataset.cinsub;try{localStorage.setItem("gre-cinsub",cs.dataset.cinsub)}catch(e){}renderCinema();return}
    if(ev.target.closest("#galToggle")){S.gal=!S.gal;render();return}
    var sm=ev.target.closest(".cinhead summary");if(sm)setTimeout(function(){renderCinema._open=sm.parentNode.open},0);
    if(ev.target.closest("#filmChip")){S.cat="film";S.view="list";render();toTop();requestAnimationFrame(toTop)}});
  document.addEventListener("keydown",function(ev){if(ev.key==="Escape"){if(!$("shareMenu").hidden)closeMenu();else closeEvent()}});
  window.addEventListener("resize",function(){var m=$("shareMenu");if(!m.hidden&&window.innerWidth!==(closeMenu._w||0))closeMenu();closeMenu._w=window.innerWidth});closeMenu._w=window.innerWidth;window.addEventListener("scroll",function(){var m=$("shareMenu");if(!m.hidden&&Math.abs(window.scrollY-(m._y||0))>40)closeMenu()},{passive:true});
  window.addEventListener("hashchange",function(){var rm=/(?:^#|&)rest=([^&]+)/.exec(location.hash);if(rm){openEvent("r:"+decodeURIComponent(rm[1]));return}var m=/(?:^#|&)event=([^&]+)/.exec(location.hash);if(m){var id=decodeURIComponent(m[1]);if(id!==S.event)openEvent(id)}else if(S.event)closeEvent()});
  var bar=$("bar");window.addEventListener("scroll",function(){bar.classList.toggle("stuck",bar.getBoundingClientRect().top<=0)},{passive:true});
  initFiltersToggle();
  initIntroToggle();
  bindFilm();
}
bind();

/* ---------- Join / change running club sheet (reuses profile picker UX) ---------- */
var CLUB_PICK="";
function clubIni(name){var w=String(name||"").split(/\s+/).filter(Boolean),GEN=/^(club|athletic|athletics|running|runners|rc|ac|sc|swd|sports|sport|the|for|of|and|&)$/i,out=[];
  for(var i=0;i<w.length&&out.length<3;i++){if(!GEN.test(w[i]))out.push(w[i][0].toUpperCase())}
  return out.join("")||"–"}
function clubLogoHtml(c){return c&&c.logo?'<img class="clogo" src="'+esc(c.logo)+'" alt="" width="44" height="44" decoding="async">':'<span class="clogo cini" aria-hidden="true">'+esc(c?clubIni(c.name):"–")+'</span>'}
function clubAsaBadge(c){return c&&c.asa===true?'<span class="asab" title="Affiliated to Athletics South Africa">ASA</span>':""}
function clubAst(c){return c.asa===true?'<span class="ast ok">ASA registered</span>':c.asa===false?'<span class="ast no">Not ASA registered</span>':'<span class="ast unk" title="ASA affiliation not confirmed from a source">ASA status unconfirmed</span>'}
function clubNorm(s){return String(s||"").toLowerCase().replace(/[^a-z0-9]+/g,"")}
function clubCardHtml(c,pick){var id=c?c.id:"";
  return '<button type="button" class="ccard'+(pick===id?" on":"")+'" data-id="'+esc(id)+'" data-q="'+esc(c?clubNorm(c.name):"noclub")+'" aria-pressed="'+(pick===id)+'">'+(c?clubLogoHtml(c)+'<span class="cn">'+esc(c.name)+'</span><span class="ct">'+esc(c.town)+(c.asa===true?" "+clubAsaBadge(c):"")+'</span>':'<span class="clogo cini" aria-hidden="true">–</span><span class="cn">No club</span><span class="ct">Nothing marked</span>')+'</button>'}
function clubGridHtml(pick){var list=(CLUBS||[]).slice().sort(function(a,b){return a.name.localeCompare(b.name)});
  var gr=list.filter(function(c){return c.garden_route}),wide=list.filter(function(c){return !c.garden_route});
  var h='<div class="cgrp"><div class="cgh">Garden Route</div><div class="cg">'+clubCardHtml(null,pick)+gr.map(function(c){return clubCardHtml(c,pick)}).join("")+'</div></div>';
  if(wide.length)h+='<div class="cgrp"><div class="cgh">Further afield</div><div class="cg">'+wide.map(function(c){return clubCardHtml(c,pick)}).join("")+'</div></div>';
  return h}
function clubJoinHtml(){var pick=CLUB_PICK||MYCLUB||"";
  var c=pick&&CLUBBY[pick]?CLUBBY[pick]:null;
  var html='<button type="button" class="mclose" data-club-close aria-label="Close">×</button>';
  html+='<h2 id="clubJoinTitle">'+(MYCLUB?"Change running club":"Join a running club")+'</h2>';
  html+='<p class="lede">Pick your club — its races and club runs are marked My club in the app. Same picker as in your profile.</p>';
  html+='<p class="lbl" id="clubJoinLbl">Your club</p>';
  html+='<details class="clubdd" id="clubJoinDd"><summary aria-labelledby="clubJoinLbl"><span class="cdsel" id="clubJoinSel">'+(c?clubLogoHtml(c)+'<span class="cdt"><b>'+esc(c.name)+'</b><small>'+esc(c.town)+" "+clubAst(c)+"</small></span>":'<span class="cdt"><b>Choose a running club</b></span>')+'</span><svg class="chev" viewBox="0 0 24 24" aria-hidden="true"><path d="M7.4 8.6L12 13.2l4.6-4.6L18 10l-6 6-6-6z"/></svg></summary>';
  html+='<div class="cdbody"><input id="clubJoinQ" type="search" placeholder="Search clubs" autocomplete="off" spellcheck="false" aria-label="Search clubs"><div id="clubJoinGrid">'+clubGridHtml(pick)+'</div><p class="cnone" id="clubJoinNone" hidden>No clubs match</p></div></details>';
  html+='<div id="clubJoinAsaWrap"'+(c?"":" hidden")+'><label for="clubJoinAsa">Running / ASA number (optional)</label><input id="clubJoinAsa" maxlength="20" autocomplete="off" autocapitalize="characters" spellcheck="false" pattern="[A-Za-z0-9 /\\-]*" placeholder="Your licence / running number" value="'+esc(MYASA||"")+'"></div>';
  html+='<p class="clubinfo" id="clubJoinInfo">'+(c?((c.asa===true&&c.asa_source?'<a href="'+esc(c.asa_source)+'" target="_blank" rel="noopener">ASA source</a> · ':"")+(c.events?c.events+" upcoming event"+(c.events>1?"s":"")+" listed":"No upcoming dated events found yet")+' · <a href="'+esc(c.source_url)+'" target="_blank" rel="noopener">source: '+esc(c.source_name)+"</a>"):"No club: nothing is marked as My club.")+'</p>';
  html+='<div class="clubactions"><button type="button" id="clubJoinSave">Save club</button><button type="button" class="clubcancel" data-club-close>Cancel</button></div>';
  html+='<p class="clubmsg" id="clubJoinMsg" role="status"></p>';
  return html}
function clubJoinSyncSel(){var pick=CLUB_PICK,c=pick&&CLUBBY[pick]?CLUBBY[pick]:null,sel=$("clubJoinSel"),wrap=$("clubJoinAsaWrap"),info=$("clubJoinInfo");
  if(sel)sel.innerHTML=c?clubLogoHtml(c)+'<span class="cdt"><b>'+esc(c.name)+'</b><small>'+esc(c.town)+" "+clubAst(c)+"</small></span>":'<span class="cdt"><b>Choose a running club</b></span>';
  if(wrap)wrap.hidden=!c; /* number field for any selected club — matches profile */
  if(info)info.innerHTML=c?((c.asa===true&&c.asa_source?'<a href="'+esc(c.asa_source)+'" target="_blank" rel="noopener">ASA source</a> · ':"")+(c.events?c.events+" upcoming event"+(c.events>1?"s":"")+" listed":"No upcoming dated events found yet")+' · <a href="'+esc(c.source_url)+'" target="_blank" rel="noopener">source: '+esc(c.source_name)+"</a>"):"No club: nothing is marked as My club."}
function clubJoinOpen(){if(!ME){location.href="/login";return}
  var m=$("clubModal"),box=$("clubBox");if(!m||!box)return;
  CLUB_PICK=MYCLUB||"";
  box.innerHTML=clubJoinHtml();m.hidden=false;document.body.classList.add("modal-open");
  try{box.focus({preventScroll:true})}catch(e){}
  var q=$("clubJoinQ"),grid=$("clubJoinGrid"),none=$("clubJoinNone"),dd=$("clubJoinDd");
  if(q)q.addEventListener("input",function(){var n=clubNorm(q.value),hit=0;
    Array.prototype.forEach.call(grid.querySelectorAll(".ccard"),function(b){var ok=!n||(b.getAttribute("data-q")||"").indexOf(n)>=0;b.hidden=!ok;if(ok&&b.getAttribute("data-id"))hit++});
    Array.prototype.forEach.call(grid.querySelectorAll(".cgrp"),function(g){g.hidden=!Array.prototype.some.call(g.querySelectorAll(".ccard"),function(b){return !b.hidden})});
    if(none)none.hidden=!n||hit>0});
  if(grid)grid.addEventListener("click",function(ev){var b=ev.target.closest(".ccard");if(!b)return;
    CLUB_PICK=b.getAttribute("data-id")||"";
    Array.prototype.forEach.call(grid.querySelectorAll(".ccard"),function(x){var on=x===b;x.classList.toggle("on",on);x.setAttribute("aria-pressed",on)});
    clubJoinSyncSel();if(dd)dd.open=false;
    var msg=$("clubJoinMsg");if(msg){msg.textContent=CLUB_PICK!==(MYCLUB||"")?"Tap Save club to keep this choice.":"";msg.className="clubmsg"}});
  var save=$("clubJoinSave");if(save)save.addEventListener("click",clubJoinSave)}
function clubJoinClose(){var m=$("clubModal");if(!m||m.hidden)return;m.hidden=true;
  if($("evModal").hidden&&$("wxModal").hidden&&$("filmOv").hidden&&(!$("clubModal")||$("clubModal").hidden))document.body.classList.remove("modal-open");
  var box=$("clubBox");if(box)box.innerHTML=""}
function clubJoinSave(){var save=$("clubJoinSave"),msg=$("clubJoinMsg"),asa=$("clubJoinAsa");if(!save)return;
  save.disabled=true;if(msg){msg.textContent="";msg.className="clubmsg"}
  var body={club_id:CLUB_PICK||null};if(asa&&!$("clubJoinAsaWrap").hidden)body.asa_number=asa.value.trim();
  fetch("/api/club",{method:"PUT",credentials:"same-origin",headers:{"Content-Type":"application/json","Accept":"application/json"},body:JSON.stringify(body)})
    .then(function(r){return r.json().then(function(d){return {ok:r.ok,status:r.status,d:d}})})
    .then(function(x){
      if(x.status===401){location.href="/login";return}
      if(!x.ok){if(msg){msg.textContent=(x.d&&x.d.error)||"Could not save.";msg.className="clubmsg bad"}save.disabled=false;return}
      MYCLUB=x.d.club_id&&CLUBBY[x.d.club_id]?x.d.club_id:null;
      MYASA=typeof x.d.asa_number==="string"&&x.d.asa_number?x.d.asa_number:null;
      clubJoinClose();render();toast(MYCLUB?"✓ Club saved":"✓ Club cleared");
    }).catch(function(){if(msg){msg.textContent="Network error.";msg.className="clubmsg bad"}save.disabled=false})}
function clubJoinBind(){
  document.addEventListener("click",function(ev){
    if(ev.target.closest("[data-club-close]")||ev.target.id==="clubModal"){ev.preventDefault();clubJoinClose();return}
    var j=ev.target.closest("[data-club-join]");if(j){ev.preventDefault();ev.stopPropagation();clubJoinOpen()}
  },true);
  document.addEventListener("keydown",function(ev){if(ev.key==="Escape"&&$("clubModal")&&!$("clubModal").hidden){ev.preventDefault();clubJoinClose()}});
}
clubJoinBind();

/* ---------- Weather (Open-Meteo) — list cards only ---------- */
var WX={TTL:2*60*60*1000,KEY:"gre.wx.v9",mem:{},pend:{},unit:"C"};
var WX_UNIT_KEY="gre.tempUnit";
function wxLoadUnit(){try{var u=localStorage.getItem(WX_UNIT_KEY);if(u==="F"||u==="C")WX.unit=u}catch(e){} }
function wxSaveUnit(u){WX.unit=(u==="F"?"F":"C");try{localStorage.setItem(WX_UNIT_KEY,WX.unit)}catch(e){} }
function wxTemp(c){if(c==null||isNaN(+c))return null;c=+c;return WX.unit==="F"?c*9/5+32:c}
function wxUnit(){return WX.unit==="F"?"°F":"°C"}
/* Always include unit: 24°C / 75°F. Pass bare:true for the number+degree only (pair helper). */
function wxTempStr(c,bare){var t=wxTemp(c);if(t==null)return"—";var s=String(Math.round(t))+"°";return bare?s:s+(WX.unit==="F"?"F":"C")}
/* Compact hi/lo with unit once: 24°/15°C */
function wxTempPair(hi,lo){var a=wxTempStr(hi,true),b=wxTempStr(lo,true);if(a==="—"&&b==="—")return"—";return a+"/"+b+wxUnit().slice(1)}
/* Colourful emoji presentation (\uFE0F) — do not strip or restyle these as text glyphs */
function wxCond(c){c=+c;
  if(c===0)return{icon:"☀️",label:"Sunny"};
  if(c===1)return{icon:"🌤️",label:"Mostly clear"};
  if(c===2)return{icon:"⛅",label:"Partly cloudy"};
  if(c===3)return{icon:"☁️",label:"Cloudy"};
  if(c===45||c===48)return{icon:"🌫️",label:"Fog"};
  if(c>=51&&c<=57)return{icon:"🌦️",label:"Drizzle"};
  if(c>=61&&c<=67||c>=80&&c<=82)return{icon:"🌧️",label:"Rain"};
  if(c>=71&&c<=77||c>=85&&c<=86)return{icon:"❄️",label:"Snow"};
  if(c>=95)return{icon:"⛈️",label:"Thunderstorms"};
  return{icon:"☁️",label:"Cloudy"}}
function wxDir(deg){if(deg==null||isNaN(+deg))return"";var d=["N","NE","E","SE","S","SW","W","NW"];return d[Math.round(((+deg)%360)/45)%8]}
function wxUvBand(u){if(u==null||isNaN(+u))return null;u=+u;if(u<3)return"Low";if(u<6)return"Moderate";if(u<8)return"High";if(u<11)return"Very high";return"Extreme"}
function wxTimeLabel(iso){if(!iso)return"";var m=/T(\d{2}):(\d{2})/.exec(String(iso));return m?m[1]+":"+m[2]:""}
function wxIsRunCat(cat){return cat==="funrun"}
/*
 * Good-for-running score (0–100) per hour — similar spirit to Android outdoor/running
 * suggestions. Thresholds (documented here, tweak carefully):
 *   apparent_temperature (°C): ideal 12–20 → 40 pts; 8–12 or 20–24 → 30; 5–8 or 24–28 → 15; else 0
 *   precipitation_probability (%): <10 → 25; <30 → 18; <50 → 8; else 0
 *   wind_speed_10m (km/h): <15 → 20; <25 → 14; <35 → 6; else 0
 *   uv_index (daytime only): <6 → 15; <8 → 10; <11 → 5; else 2; twilight → 10
 *   hour-of-day: 00–04 and 21–23 score 0; 05–08 and 16–19 get +8
 * Daily rating from best 2h window average: ≥80 Great, ≥65 Good, ≥45 Fair, else Poor.
 */
function wxHourScore(h){if(!h)return 0;var at=h.at!=null?h.at:h.t,s=0,hh=h.hh|0;
  if(hh<5||hh>=21)return 0;
  if(at!=null){if(at>=12&&at<=20)s+=40;else if(at>=8&&at<12||at>20&&at<=24)s+=30;else if(at>=5&&at<8||at>24&&at<=28)s+=15}
  var p=h.pop;if(p==null||p<10)s+=25;else if(p<30)s+=18;else if(p<50)s+=8;
  var w=h.wind;if(w==null||w<15)s+=20;else if(w<25)s+=14;else if(w<35)s+=6;
  if(!h.day)s+=10;else{var u=h.uv;if(u==null||u<6)s+=15;else if(u<8)s+=10;else if(u<11)s+=5;else s+=2}
  if(hh>=5&&hh<=8||hh>=16&&hh<=19)s+=8;
  return s}
function wxWinLabel(from,to){return (from<10?"0":"")+from+":00 – "+(to>=24?"24":(to<10?"0":"")+to)+":00"}
function wxWinDetail(hours,win){var slice=hours.filter(function(h){return h.hh>=win.from&&h.hh<win.to});if(!slice.length)return wxWinLabel(win.from,win.to);
  var n=slice.length,t=0,p=0,w=0,u=0,i;for(i=0;i<n;i++){t+=(slice[i].at!=null?slice[i].at:slice[i].t)||0;p+=slice[i].pop||0;w+=slice[i].wind||0;u+=slice[i].uv||0}
  t/=n;p/=n;w/=n;u/=n;
  return wxWinLabel(win.from,win.to)+" ("+wxTempStr(t)+", "+Math.round(p)+"% rain, wind "+Math.round(w)+" km/h)"}
function wxDayWhy(hours,rating){if(!hours||!hours.length)return"";
  var day=hours.filter(function(h){return h.hh>=6&&h.hh<=18});if(!day.length)day=hours;
  var n=day.length,tmin=999,tmax=-999,p=0,w=0,u=0,i,at;
  for(i=0;i<n;i++){at=day[i].at!=null?day[i].at:day[i].t;if(at!=null){if(at<tmin)tmin=at;if(at>tmax)tmax=at}p+=day[i].pop||0;w+=day[i].wind||0;u+=day[i].uv||0}
  p/=n;w/=n;u/=n;var bits=[];
  if(tmin!==999)bits.push((tmin<=14?"Cool":tmax>=26?"Warm":"Mild")+" "+Math.round(wxTemp(tmin))+"–"+Math.round(wxTemp(tmax))+wxUnit());
  if(w<15)bits.push("light wind");else if(w<25)bits.push("breezy");else bits.push("windy");
  if(p<15)bits.push("low rain chance");else if(p<40)bits.push("some rain chance");else bits.push("rain likely");
  if(u>=8)bits.push("high UV midday");else if(u<3)bits.push("low UV");
  return bits.slice(0,3).join(", ")}
function wxAvoid(hours){if(!hours)return null;var bad=[],i,h,sc;
  for(i=0;i<hours.length;i++){h=hours[i];if(h.hh<10||h.hh>17)continue;sc=wxHourScore(h);
    if((h.uv!=null&&h.uv>=8)||(h.at!=null&&h.at>=28)||(h.pop!=null&&h.pop>=60)||sc&&sc<35)bad.push(h)}
  if(bad.length<2)return null;
  var from=bad[0].hh,to=bad[bad.length-1].hh+1,mid=bad[Math.floor(bad.length/2)],why=[];
  if(mid.uv!=null&&mid.uv>=8)why.push("UV "+(Math.round(mid.uv*10)/10)+", "+(wxUvBand(mid.uv)||"high"));
  if(mid.at!=null&&mid.at>=28)why.push("hot "+wxTempStr(mid.at));
  if(mid.pop!=null&&mid.pop>=50)why.push(Math.round(mid.pop)+"% rain");
  return{from:from,to:to,label:wxWinLabel(from,to)+(why.length?" ("+why.join(", ")+")":"")}}
function wxRunDay(hours){if(!hours||!hours.length)return null;
  var wins=[],i,a,b,sc;for(i=0;i<hours.length-1;i++){a=hours[i];b=hours[i+1];if(!a||!b)continue;
    sc=(wxHourScore(a)+wxHourScore(b))/2;if(sc>=45)wins.push({sc:sc,from:a.hh,to:(b.hh+1>23?24:b.hh+1)})}
  wins.sort(function(x,y){return y.sc-x.sc||x.from-y.from});
  var best=wins[0]?wins[0].sc:Math.max.apply(null,hours.map(wxHourScore).concat([0]));
  var rating=best>=80?"Great":best>=65?"Good":best>=45?"Fair":"Poor";
  var picked=[];wins.forEach(function(w){if(picked.length>=2)return;if(!picked.some(function(p){return w.from<p.to&&w.to>p.from}))picked.push(w)});
  return{rating:rating,best:best,windows:picked,why:wxDayWhy(hours,rating),avoid:wxAvoid(hours)}}
function wxLoadCache(){try{var r=JSON.parse(localStorage.getItem(WX.KEY)||"{}");if(r&&typeof r==="object")WX.mem=r}catch(e){WX.mem={}}}
function wxSaveCache(){try{var now=Date.now(),o={},k;for(k in WX.mem){if(WX.mem[k]&&WX.mem[k].exp>now)o[k]=WX.mem[k]}localStorage.setItem(WX.KEY,JSON.stringify(o));WX.mem=o}catch(e){}}
function wxTownCoords(town){var t=(window.TOWNS||{})[town];return t&&t.lat!=null&&t.lng!=null?t:null}
function wxInWindow(ds){if(!ds||ds<TODAY)return false;var lim=pd(TODAY);lim.setDate(lim.getDate()+15);var y=lim.getFullYear(),m=String(lim.getMonth()+1).padStart(2,"0"),d=String(lim.getDate()).padStart(2,"0");return ds<=y+"-"+m+"-"+d}
function wxGetDay(town,ds){var c=WX.mem[town];if(!c||c.exp<Date.now()||!c.days)return null;var d=c.days[ds]||null;if(d&&!(d.hours&&d.hours.length))return null;return d}
function wxFetchTown(town){if(WX.pend[town])return WX.pend[town];var co=wxTownCoords(town);if(!co)return Promise.resolve(null);
  var url="https://api.open-meteo.com/v1/forecast?latitude="+co.lat+"&longitude="+co.lng
    +"&daily=weather_code,temperature_2m_max,temperature_2m_min,precipitation_probability_max,precipitation_sum,wind_speed_10m_max,wind_gusts_10m_max,wind_direction_10m_dominant,uv_index_max,sunrise,sunset"
    +"&hourly=weather_code,temperature_2m,apparent_temperature,precipitation_probability,wind_speed_10m,uv_index,is_day"
    +"&timezone=Africa%2FJohannesburg&forecast_days=16";
  WX.pend[town]=fetch(url,{credentials:"omit",mode:"cors"}).then(function(r){return r.ok?r.json():null}).then(function(j){
    delete WX.pend[town];if(!j||!j.daily||!j.daily.time)return null;
    var days={},i,t=j.daily.time;
    var code=j.daily.weather_code||[],tmax=j.daily.temperature_2m_max||[],tmin=j.daily.temperature_2m_min||[];
    var pop=j.daily.precipitation_probability_max||[],psum=j.daily.precipitation_sum||[];
    var wmax=j.daily.wind_speed_10m_max||[],gust=j.daily.wind_gusts_10m_max||[],wdir=j.daily.wind_direction_10m_dominant||[];
    var uv=j.daily.uv_index_max||[],sr=j.daily.sunrise||[],ss=j.daily.sunset||[];
    for(i=0;i<t.length;i++)days[t[i]]={code:code[i],tmax:tmax[i],tmin:tmin[i],pop:pop[i],rain:psum[i],wind:wmax[i],gust:gust[i],dir:wdir[i],uv:uv[i],sunrise:sr[i],sunset:ss[i],hours:[]};
    var ht=(j.hourly&&j.hourly.time)||[];
    var hC=j.hourly.weather_code||[],hT=j.hourly.temperature_2m||[],hA=j.hourly.apparent_temperature||[],hP=j.hourly.precipitation_probability||[];
    var hW=j.hourly.wind_speed_10m||[],hU=j.hourly.uv_index||[],hD=j.hourly.is_day||[];
    for(i=0;i<ht.length;i++){
      var raw=String(ht[i]||""),ds=raw.slice(0,10),hm=/[T ](\d{2})(?::\d{2})?/.exec(raw),hh=hm?+hm[1]:NaN;
      if(!days[ds]||isNaN(hh))continue;
      days[ds].hours.push({hh:hh,code:hC[i],t:hT[i],at:hA[i],pop:hP[i],wind:hW[i],uv:hU[i],day:!!hD[i]});
    }
    for(i=0;i<t.length;i++){var day=days[t[i]];day.hours.sort(function(a,b){return a.hh-b.hh});
      var ats=day.hours.map(function(h){return h.at}).filter(function(x){return x!=null});
      if(ats.length){day.feelMax=Math.max.apply(null,ats);day.feelMin=Math.min.apply(null,ats)}
      var run=wxRunDay(day.hours);if(run){day.run=run.rating;day.runBest=run.best;day.windows=run.windows;day.why=run.why;day.avoid=run.avoid}}
    WX.mem[town]={exp:Date.now()+WX.TTL,days:days};wxSaveCache();return days;
  }).catch(function(){delete WX.pend[town];return null});
  return WX.pend[town]}
function wxCompact(d,runCat){if(!d||d.tmax==null||d.tmin==null)return"";
  var c=wxCond(d.code),s='<span class="wxi" aria-hidden="true">'+c.icon+'</span><span class="wxtemp">'+wxTempPair(d.tmax,d.tmin)+"</span>";
  if(d.pop!=null&&d.pop>=30)s+='<span class="wxchip rain">'+Math.round(d.pop)+"%</span>";
  if(d.wind!=null&&d.wind>=20)s+='<span class="wxchip wind">'+Math.round(d.wind)+" km/h</span>";
  var band=wxUvBand(d.uv);if(band&&d.uv>=6)s+='<span class="wxchip uv">UV '+band+'</span>';
  if(runCat&&d.run)s+='<span class="wxchip run '+d.run.toLowerCase()+'">'+d.run+' running conditions</span>';
  return s}
/* Compact badge for Happening-soon strip: icon + hi/lo with unit once — never overflow the pill */
function wxCompactMini(d){if(!d||d.tmax==null)return"";
  var c=wxCond(d.code);
  if(d.tmin==null)return'<span class="wxi" aria-hidden="true">'+c.icon+'</span><span class="wxtemp">'+wxTempStr(d.tmax)+'</span>';
  return'<span class="wxi" aria-hidden="true">'+c.icon+'</span><span class="wxtemp">'+wxTempPair(d.tmax,d.tmin)+'</span>'}
function wxSunFrac(iso){if(!iso)return null;var m=/T(\d{2}):(\d{2})/.exec(String(iso));if(!m)return null;return +m[1]+(+m[2])/60}
function wxHourStrip(d,ds,runCat){if(!d||!d.hours||!d.hours.length)return'<p class="wxnostrip">Hourly forecast unavailable</p>';
  var startH=4,endH=22,nowH=(new Date()).getHours(),srF=wxSunFrac(d.sunrise),ssF=wxSunFrac(d.sunset);
  if(srF!=null)startH=Math.min(startH,Math.floor(srF));
  if(ssF!=null)endH=Math.max(endH,Math.ceil(ssF));
  if(startH<0)startH=0;if(endH>23)endH=23;
  /* Keep full 04:00–22:00 range even today — wxScrollHourly jumps to the current hour */
  var byH={},i,x;for(i=0;i<d.hours.length;i++)byH[d.hours[i].hh]=d.hours[i];
  var h=[];for(i=startH;i<=endH;i++){if(byH[i])h.push(byH[i])}
  if(!h.length){h=d.hours.filter(function(x){return x.hh>=4&&x.hh<=22});if(!h.length)h=d.hours.slice()}
  if(!h.length)return'<p class="wxnostrip">Hourly forecast unavailable</p>';
  var n=h.length,colW=56,chartW=Math.max(n*colW,n*40),padL=8,padR=8,topPad=22,curveH=78,iconY=topPad+curveH+6,rainH=28,baseY=iconY+36,svgH=baseY+rainH+18;
  var temps=h.map(function(x){return wxTemp(x.t)}).filter(function(t){return t!=null});
  var tMin=temps.length?Math.min.apply(null,temps):0,tMax=temps.length?Math.max.apply(null,temps):1;
  if(tMax-tMin<2){var mid=(tMax+tMin)/2;tMin=mid-1;tMax=mid+1}
  function xAt(i){return padL+(i+0.5)*((chartW-padL-padR)/n)}
  function xAtFrac(fracH){var first=h[0].hh,last=h[n-1].hh,span=Math.max(1,last-first);return padL+((fracH-first)/span)*(chartW-padL-padR)}
  function yAt(t){var v=wxTemp(t);if(v==null)return topPad+curveH/2;return topPad+curveH-((v-tMin)/(tMax-tMin))*curveH}
  /* Smooth cubic path through hour points */
  var pts=[];for(i=0;i<n;i++)pts.push({x:xAt(i),y:yAt(h[i].t),t:h[i].t,pop:h[i].pop,hh:h[i].hh,code:h[i].code});
  function smoothPath(pts){if(pts.length<2)return"";var d="M"+pts[0].x.toFixed(1)+","+pts[0].y.toFixed(1),j,p0,p1,p2,p3,cp1x,cp1y,cp2x,cp2y;
    for(j=0;j<pts.length-1;j++){p0=pts[j===0?j:j-1];p1=pts[j];p2=pts[j+1];p3=pts[j+2<pts.length?j+2:j+1];
      cp1x=p1.x+(p2.x-p0.x)/6;cp1y=p1.y+(p2.y-p0.y)/6;cp2x=p2.x-(p3.x-p1.x)/6;cp2y=p2.y-(p3.y-p1.y)/6;
      d+=" C"+cp1x.toFixed(1)+","+cp1y.toFixed(1)+" "+cp2x.toFixed(1)+","+cp2y.toFixed(1)+" "+p2.x.toFixed(1)+","+p2.y.toFixed(1)}
    return d}
  var path=smoothPath(pts),area=path?path+" L"+pts[pts.length-1].x.toFixed(1)+","+(topPad+curveH)+" L"+pts[0].x.toFixed(1)+","+(topPad+curveH)+" Z":"";
  var svg='<svg class="wxcurve" viewBox="0 0 '+chartW+" "+svgH+'" width="'+chartW+'" height="'+svgH+'" preserveAspectRatio="none" aria-hidden="true">';
  /* Night shading before sunrise / after sunset */
  if(srF!=null&&srF>=h[0].hh&&srF<=h[n-1].hh){var sx=xAtFrac(srF);svg+='<rect class="wxnight" x="0" y="0" width="'+sx.toFixed(1)+'" height="'+svgH+'" />'}
  else if(srF!=null&&srF>h[n-1].hh){svg+='<rect class="wxnight" x="0" y="0" width="'+chartW+'" height="'+svgH+'" />'}
  if(ssF!=null&&ssF>=h[0].hh&&ssF<=h[n-1].hh){var ex=xAtFrac(ssF);svg+='<rect class="wxnight" x="'+ex.toFixed(1)+'" y="0" width="'+(chartW-ex).toFixed(1)+'" height="'+svgH+'" />'}
  else if(ssF!=null&&ssF<h[0].hh){svg+='<rect class="wxnight" x="0" y="0" width="'+chartW+'" height="'+svgH+'" />'}
  /* Best-run green bands (funrun only) */
  if(runCat&&d.windows&&d.windows.length){d.windows.forEach(function(w){var a=Math.max(w.from,h[0].hh),b=Math.min(w.to,h[n-1].hh+1);if(b<=a)return;
    var x1=xAtFrac(a),x2=xAtFrac(b),bw=x2-x1;
    svg+='<rect class="wxrunband" x="'+x1.toFixed(1)+'" y="'+topPad+'" width="'+bw.toFixed(1)+'" height="'+curveH+'" rx="6" />';
    if(bw>=48)svg+='<text class="wxrunbandlbl" x="'+(x1+bw/2).toFixed(1)+'" y="'+(topPad+12)+'">Best run</text>'})}
  if(area)svg+='<path class="wxarea" d="'+area+'" />';
  if(path)svg+='<path class="wxline" d="'+path+'" fill="none" />';
  /* Sunrise / sunset markers at exact fractional x */
  function sunMark(frac,label,cls,icon){if(frac==null||frac<h[0].hh-0.01||frac>h[n-1].hh+0.01)return"";var x=xAtFrac(frac),tl=wxTimeLabel(label)||"";
    return '<line class="'+cls+'line" x1="'+x.toFixed(1)+'" y1="0" x2="'+x.toFixed(1)+'" y2="'+svgH+'" />'
      +'<text class="'+cls+'ico" x="'+x.toFixed(1)+'" y="'+(topPad+2)+'">'+icon+'</text>'
      +'<text class="'+cls+'lbl" x="'+x.toFixed(1)+'" y="'+(topPad+16)+'">'+tl+'</text>'}
  svg+=sunMark(srF,d.sunrise,"wxsr","🌅");svg+=sunMark(ssF,d.sunset,"wxss","🌇");
  /* Temp labels + dots on curve */
  for(i=0;i<pts.length;i++){svg+='<circle class="wxdot" cx="'+pts[i].x.toFixed(1)+'" cy="'+pts[i].y.toFixed(1)+'" r="3" />';
    svg+='<text class="wxtlbl" x="'+pts[i].x.toFixed(1)+'" y="'+(pts[i].y-8).toFixed(1)+'">'+wxTempStr(pts[i].t)+'</text>'}
  /* Rain bars under baseline */
  for(i=0;i<pts.length;i++){var pop=pts[i].pop||0,bh=Math.max(2,(pop/100)*rainH),bx=pts[i].x-6;
    svg+='<rect class="wxrainbar" x="'+bx.toFixed(1)+'" y="'+(baseY+rainH-bh).toFixed(1)+'" width="12" height="'+bh.toFixed(1)+'" rx="2" />'
    if(pop>=20)svg+='<text class="wxrainlbl" x="'+pts[i].x.toFixed(1)+'" y="'+(baseY+rainH+12)+'">'+Math.round(pop)+'%</text>'}
  svg+='</svg>';
  var cols=h.map(function(x,idx){var c=wxCond(x.code!=null?x.code:d.code),nowCls=(ds===TODAY&&x.hh===nowH)?" now":"";
    return '<div class="wxh'+nowCls+'" role="listitem" data-hh="'+x.hh+'" style="width:'+(100/n)+'%"><span class="wxht">'+(x.hh<10?"0":"")+x.hh+':00</span><span class="wxhi" aria-hidden="true">'+c.icon+'</span></div>'}).join("");
  var legend='<ul class="wxlegend" aria-label="Chart legend">';
  if(runCat&&d.windows&&d.windows.length)legend+='<li><span class="wxlegsw wxleg-run" aria-hidden="true"></span>Best times to run</li>';
  legend+='<li><span class="wxlegsw wxleg-night" aria-hidden="true"></span>Night</li>';
  legend+='<li><span class="wxlegsw wxleg-rain" aria-hidden="true"></span>Rain chance %</li>';
  legend+='<li><span class="wxlegico" aria-hidden="true">🌅🌇</span>Sunrise / sunset</li></ul>';
  return '<div class="wxhourly" data-wx-n="'+n+'"><div class="wxscroll" data-wx-scroll><div class="wxscroll-inner" style="min-width:100%;width:'+chartW+'px">'+svg+'<div class="wxstrip" role="list" aria-label="Hourly forecast">'+cols+'</div></div></div>'+legend+'</div>'}
function wxModalHtml(town,ds,d,runCat){if(!d)return'<button type="button" class="mclose" data-wx-close aria-label="Close">×</button><p class="wxempty">Forecast unavailable</p>';
  var c=wxCond(d.code),dateLbl="";try{dateLbl=fmt(pd(ds),true)}catch(e){dateLbl=ds}
  var html='<button type="button" class="mclose" data-wx-close aria-label="Close">×</button>';
  html+='<header class="wxhead"><p class="wxeyebrow">Weather</p><h2 id="wxTitle">'+esc(town)+'</h2><p class="wxdate">'+esc(dateLbl)+'</p>';
  html+='<div class="wxhero"><span class="wxheroi" aria-hidden="true">'+c.icon+'</span><div class="wxherotxt"><div class="wxcond">'+c.label+'</div><div class="wxhtemp">'+wxTempPair(d.tmax,d.tmin)+'</div>';
  if(d.feelMax!=null&&d.feelMin!=null)html+='<div class="wxfeel">Feels like '+wxTempPair(d.feelMax,d.feelMin)+'</div>';
  html+='</div></div></header>';
  html+='<section class="wxsec"><h3 class="wxsech">Hour by hour</h3>'+wxHourStrip(d,ds,runCat)+'</section>';
  html+='<section class="wxsec"><h3 class="wxsech">Details</h3><div class="wxgrid">';
  if(d.pop!=null||d.rain!=null){var rain=[];if(d.pop!=null)rain.push(Math.round(d.pop)+"% chance");if(d.rain!=null)rain.push((Math.round(d.rain*10)/10)+" mm");html+='<div class="wxcell"><span>Rain</span><b>'+rain.join("<br>")+'</b></div>'}
  if(d.wind!=null){var w=Math.round(d.wind)+" km/h";var dir=wxDir(d.dir);if(dir)w+=" "+dir;html+='<div class="wxcell"><span>Wind</span><b>'+w+'</b></div>'}
  if(d.gust!=null)html+='<div class="wxcell"><span>Gusts</span><b>'+Math.round(d.gust)+' km/h</b></div>';
  var band=wxUvBand(d.uv);if(d.uv!=null&&band)html+='<div class="wxcell"><span>UV index</span><b>'+(Math.round(d.uv*10)/10)+'<br>'+band+'</b></div>';
  if(d.sunrise)html+='<div class="wxcell"><span>🌅 Sunrise</span><b>'+(wxTimeLabel(d.sunrise)||"—")+'</b></div>';
  if(d.sunset)html+='<div class="wxcell"><span>🌇 Sunset</span><b>'+(wxTimeLabel(d.sunset)||"—")+'</b></div>';
  if(d.feelMax!=null&&d.feelMin!=null)html+='<div class="wxcell"><span>Feels like</span><b>'+wxTempPair(d.feelMax,d.feelMin)+'</b></div>';
  html+='</div></section>';
  if(runCat&&d.run){html+='<section class="wxsec wxrunbox '+d.run.toLowerCase()+'"><h3 class="wxsech">Running conditions</h3>';
    html+='<p class="wxrunh">Overall for the day: <b>'+d.run+'</b></p>';
    if(d.why)html+='<p class="wxrunr">'+esc(d.why)+'</p>';
    if(d.windows&&d.windows.length){html+='<p class="wxrunw"><b>Best times to run:</b></p><ul class="wxrunlist">'+d.windows.map(function(w){return '<li>'+esc(wxWinDetail(d.hours,w))+'</li>'}).join("")+'</ul>'}
    if(d.avoid)html+='<p class="wxavoid"><b>Avoid:</b> '+esc(d.avoid.label)+'</p>';
    html+='</section>'}
  html+='<p class="wxcredit">Forecast: Open-Meteo · Times SAST · '+wxUnit()+'</p>';
  return html}
function wxScrollHourly(box,ds){var sc=box&&box.querySelector("[data-wx-scroll]");if(!sc)return;
  var nowEl=sc.querySelector(".wxh.now")||sc.querySelector('.wxh[data-hh]');
  if(!nowEl)return;var left=nowEl.offsetLeft-Math.max(0,(sc.clientWidth-nowEl.offsetWidth)/3);
  try{sc.scrollTo({left:Math.max(0,left),behavior:"smooth"})}catch(e){sc.scrollLeft=Math.max(0,left)}}
function wxOpen(town,ds,cat){var m=$("wxModal"),box=$("wxBox");if(!m||!box)return;
  function show(d){box.innerHTML=wxModalHtml(town,ds,d,wxIsRunCat(cat));m.hidden=false;document.body.classList.add("modal-open");try{box.focus({preventScroll:true})}catch(e){}
    requestAnimationFrame(function(){wxScrollHourly(box,ds)})}
  var d=wxGetDay(town,ds);if(d&&d.hours&&d.hours.length){show(d);return}
  box.innerHTML='<button type="button" class="mclose" data-wx-close aria-label="Close">×</button><p class="wxempty">Loading hourly forecast…</p>';
  m.hidden=false;document.body.classList.add("modal-open");
  /* Drop stale daily-only cache entry for this town, then refetch */
  try{if(WX.mem[town])delete WX.mem[town];wxSaveCache()}catch(e){}
  wxFetchTown(town).then(function(){show(wxGetDay(town,ds))}).catch(function(){show(null)})}
function wxClose(){var m=$("wxModal");if(!m||m.hidden)return;m.hidden=true;if($("evModal").hidden&&$("filmOv").hidden&&(!$("clubModal")||$("clubModal").hidden))document.body.classList.remove("modal-open");
  var box=$("wxBox");if(box)box.innerHTML=""}
function wxApply(){Array.prototype.forEach.call(document.querySelectorAll(".wx[data-wx-town][data-wx-date]"),function(el){
  var town=el.getAttribute("data-wx-town"),ds=el.getAttribute("data-wx-date"),cat=el.getAttribute("data-wx-cat")||"";
  if(!town||!ds||!wxInWindow(ds)){el.hidden=true;el.innerHTML="";el.removeAttribute("title");el.classList.remove("wxmini");return}
  var d=wxGetDay(town,ds);if(!d||d.tmax==null||d.tmin==null){el.hidden=true;el.innerHTML="";el.classList.remove("wxmini");return}
  var c=wxCond(d.code),label=c.label+", "+wxTempPair(d.tmax,d.tmin)+". Tap for forecast.";
  var mini=!!(el.closest&&el.closest(".soon"));
  el.hidden=false;el.classList.toggle("wxmini",mini);
  el.innerHTML=mini?wxCompactMini(d):wxCompact(d,wxIsRunCat(cat));
  el.title=label;el.setAttribute("aria-label",label);
})}
function wxHydrate(){if(S.view==="cal")return;
  var need={},els=document.querySelectorAll(".wx[data-wx-town][data-wx-date]");
  Array.prototype.forEach.call(els,function(el){var town=el.getAttribute("data-wx-town"),ds=el.getAttribute("data-wx-date");
    if(town&&ds&&wxInWindow(ds)&&wxTownCoords(town)&&!wxGetDay(town,ds))need[town]=1});
  var towns=Object.keys(need),i=0;
  function next(){if(i>=towns.length){wxApply();return}var t=towns[i++];wxFetchTown(t).then(function(){wxApply();next()}).catch(function(){next()})}
  wxApply();if(towns.length)next()}
function wxBind(){
  document.addEventListener("click",function(ev){
    var close=ev.target.closest("[data-wx-close]");if(close){ev.preventDefault();ev.stopPropagation();wxClose();return}
    if(ev.target.id==="wxModal"){wxClose();return}
    var b=ev.target.closest("button.wx");if(!b||!b.getAttribute("data-wx-town"))return;
    ev.preventDefault();ev.stopPropagation();
    wxOpen(b.getAttribute("data-wx-town"),b.getAttribute("data-wx-date"),b.getAttribute("data-wx-cat")||"");
  },true);
  document.addEventListener("keydown",function(ev){if(ev.key==="Escape"&&!$("wxModal").hidden){ev.preventDefault();wxClose()}});
}
function wxSyncUnitFromMe(){fetch("/api/me",{credentials:"same-origin",cache:"no-store"}).then(function(r){return r.ok?r.json():null}).then(function(me){
  if(me&&(me.temp_unit==="C"||me.temp_unit==="F")){wxSaveUnit(me.temp_unit);wxApply();
    var open=$("wxModal");if(open&&!open.hidden){var box=$("wxBox"),t=box&&box.querySelector("#wxTitle");/* leave open as-is until next open */} }
}).catch(function(){})}
wxLoadUnit();
wxLoadCache();
wxBind();
wxSyncUnitFromMe();


init(window.EVENTS||[]);
syncStars();
document.addEventListener("visibilitychange",function(){if(document.visibilityState==="visible")syncStars()});
if(/^https?:/.test(location.protocol)){
  fetch("data/events.json",{cache:"no-cache"}).then(function(r){return r.ok?r.json():null}).then(function(d){
    if(Array.isArray(d)&&d.length&&JSON.stringify(d)!==JSON.stringify(window.EVENTS||[]))init(d);
  }).catch(function(){});
  fetch("data/cinema.json",{cache:"no-cache"}).then(function(r){return r.ok?r.json():null}).then(function(d){
    if(d&&d.fetched_at&&(!CIN||d.fetched_at!==CIN.fetched_at)){CIN=window.CINEMA=d;if(S.view==="cinema"||S.view==="list")render()}
  }).catch(function(){});
}
})();
