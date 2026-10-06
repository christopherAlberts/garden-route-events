/* Garden Route Events: static app, no build step. Data comes from window.EVENTS (data/events.js). */
(function(){
"use strict";
var GR_ORDER=["Mossel Bay","Hartenbos","Groot Brak","George","Oudtshoorn","Wilderness","Hoekwil","Sedgefield","Knysna","Plettenberg Bay","The Crags","Nature's Valley","Storms River","Tsitsikamma"];
var WIDE_ORDER=["Cape Town","Somerset West","Kleinmond","Pringle Bay","Hermanus","Stanford","Gansbaai","Struisbaai","L'Agulhas","Riversdale","Stilbaai","Humansdorp","St Francis Bay","Jeffreys Bay"];
var MONTHS=["2026-10","2026-11","2026-12","2027-01","2027-02"];
var MN=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"];
var MNL=["January","February","March","April","May","June","July","August","September","October","November","December"];
var DOW=["Sun","Mon","Tue","Wed","Thu","Fri","Sat"];
var CATS={concert:"Concert",festival:"Festival",musical:"Musical",market:"Market",funrun:"Run / walk / trail",community:"Church / community",arts:"Arts & culture",quiz:"Quiz night",festive:"Festive dining",restaurant:"Restaurant"};
var CATPL={concert:"concerts",festival:"festivals",musical:"musicals",market:"markets",funrun:"runs, walks & trails",community:"church & community",arts:"arts & culture",quiz:"quiz nights",festive:"festive dining",restaurant:"restaurants & pubs"};
var ICON={
  restaurant:'<svg viewBox="0 0 24 24"><path d="M11 9H9V2H7v7H5V2H3v7c0 2.12 1.66 3.84 3.75 3.97V22h2.5v-9.03C11.34 12.84 13 11.12 13 9V2h-2v7zm5-3v8h2.5v8H21V2c-2.76 0-5 2.24-5 4z"/></svg>',
  quiz:'<svg viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 17h-2v-2h2v2zm2.07-7.75l-.9.92C13.45 12.9 13 13.5 13 15h-2v-.5c0-1.1.45-2.1 1.17-2.83l1.24-1.26c.37-.36.59-.86.59-1.41 0-1.1-.9-2-2-2s-2 .9-2 2H8c0-2.21 1.79-4 4-4s4 1.79 4 4c0 .88-.36 1.68-.93 2.25z"/></svg>',
  festive:'<svg viewBox="0 0 24 24"><path d="M20 6h-2.18c.11-.31.18-.65.18-1 0-1.66-1.34-3-3-3-1.05 0-1.96.54-2.5 1.35l-.5.67-.5-.68C10.96 2.54 10.05 2 9 2 7.34 2 6 3.34 6 5c0 .35.07.69.18 1H4c-1.11 0-1.99.89-1.99 2L2 19c0 1.11.89 2 2 2h16c1.11 0 2-.89 2-2V8c0-1.11-.89-2-2-2zm-5-2c.55 0 1 .45 1 1s-.45 1-1 1-1-.45-1-1 .45-1 1-1zM9 4c.55 0 1 .45 1 1s-.45 1-1 1-1-.45-1-1 .45-1 1-1zm11 15H4v-2h16v2zm0-5H4V8h5.08L7 10.83 8.62 12 12 7.4l3.38 4.6L17 10.83 14.92 8H20v6z"/></svg>',
  concert:'<svg viewBox="0 0 24 24"><path d="M9 3v10.55A4 4 0 107 21a4 4 0 004-4V7h6V3H9z"/></svg>',
  festival:'<svg viewBox="0 0 24 24"><path d="M12 2l1 0v2.2l5-1.2v4l-5 1.2V8.9L21.5 21H15l-3-5-3 5H2.5L11 8.9V2z"/></svg>',
  musical:'<svg viewBox="0 0 24 24"><path d="M12 2l2.9 6.9 7.1.5-5.4 4.6 1.7 7L12 17.3 5.7 21l1.7-7L2 9.4l7.1-.5z"/></svg>',
  funrun:'<svg viewBox="0 0 24 24"><path d="M13.5 5.5a2 2 0 100-4 2 2 0 000 4zM9.8 8.9L7 23h2.1l1.8-8 2.1 2v6h2v-7.5l-2.1-2 .6-3A7.3 7.3 0 0019 13v-2a5 5 0 01-4.3-2.4l-1-1.6a2 2 0 00-1.7-1l-.8.1L6 8.3V13h2V9.6z"/></svg>',
  community:'<svg viewBox="0 0 24 24"><path d="M11 2h2v3h3v2h-3v3.2l7 4.1V22h-6v-4a2 2 0 00-4 0v4H4v-7.7l7-4.1V7H8V5h3z"/></svg>',
  arts:'<svg viewBox="0 0 24 24"><path d="M3 3h9v7.5A4.5 4.5 0 017.5 15 4.5 4.5 0 013 10.5zm2.2 4.3h1.6V6.2H5.2zm3.5 0h1.6V6.2H8.7zM5.6 10a2 2 0 003.8 0zM12.5 9H21v7.5a4.5 4.5 0 01-9 0V14a6 6 0 00.5-3.5zm2 3.3h1.6v-1.6h-1.6zm3.4 0h1.6v-1.6h-1.6zm-3.3 4.4a2 2 0 003.8 0z"/></svg>',
  market:'<svg viewBox="0 0 24 24"><path d="M3 9h18l-1.8 11.2A1 1 0 0118.2 21H5.8a1 1 0 01-1-.8L3 9zm5.2-1L12 2.5 15.8 8h-2.4L12 5.9 10.6 8z"/></svg>'};
var PIN='<svg viewBox="0 0 24 24"><path d="M12 2a7 7 0 017 7c0 5-7 13-7 13S5 14 5 9a7 7 0 017-7zm0 4.5A2.5 2.5 0 1012 11.5 2.5 2.5 0 0012 6.5z"/></svg>';
var ARROW='<svg viewBox="0 0 24 24"><path d="M13 5l7 7-7 7-1.4-1.4 4.6-4.6H4v-2h12.2l-4.6-4.6z"/></svg>';
var S={scope:"gr",q:"",town:"",cat:"",month:"",view:"list",calMonth:null,calDay:null,off:false,event:"",nye:false};
/* restaurants are entries of category "restaurant": list cards, calendar days with recurring specials, map pins */
var LAST_DAY="2027-02-28",EVR={};
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
    '<div class="mbody">'+(e.garden_route?'<span class="grtag">Garden Route</span>':'')+
      '<h2 id="evTitle">'+esc(e.title)+'</h2>'+
      '<div class="when">'+esc(datesTxt(e))+(e.time?" · "+esc(e.time):"")+'</div>'+
      (od.length>1?'<div class="occ">'+od.length+' upcoming dates: '+od.slice(0,10).map(function(d){var x=pd(d);return x.getDate()+" "+MN[x.getMonth()]}).join(", ")+(od.length>10?", …":"")+'</div>':'')+
      (e.status_note?'<div class="stnote'+(isOff(e)?" off":"")+'">'+esc(e.status_note)+'</div>':'')+
      '<div class="where">'+PIN+'<span>'+esc(e.venue||"")+(e.venue?", ":"")+esc(e.town)+(e.venue_address&&e.venue_address!==e.venue?'<br><small>'+esc(e.venue_address)+'</small>':'')+'</span></div>'+
      (p?'<div class="price">'+esc(p)+'</div>':'')+atRest(e)+
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
  if(openEvent._last&&openEvent._last.focus)try{openEvent._last.focus({preventScroll:true})}catch(x){}}

function init(data){
  EV=(data||[]).slice().concat(RS);EVR={};RS.forEach(function(r){(r.event_ids||[]).forEach(function(id){EVR[id]=r})});
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
    var list=order.concat(extra).filter(function(t){return have[t]});if(!list.length)return "";
    return '<optgroup label="'+label+'">'+list.map(function(t){return '<option value="'+esc(t)+'">'+esc(t)+' ('+have[t]+')</option>'}).join("")+'</optgroup>'}
  var h='<option value="">All towns</option>'+grp("Garden Route",GR_ORDER,true);
  if(S.scope==="all")h+=grp("Rest of the coast",WIDE_ORDER,false);
  $("town").innerHTML=h;if(S.town&&!have[S.town])S.town="";$("town").value=S.town;
}
function matches(e,ignoreMonth,anyStatus){
  if(S.scope==="gr"&&!e.garden_route)return false;
  if(!anyStatus&&!S.off&&isOff(e))return false;
  if(S.town&&e.town!==S.town)return false;
  if(S.cat&&e.category!==S.cat)return false;
  if(S.nye&&!e.nye)return false;
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
  return '<article class="card'+(isOff(e)?" is-off":"")+'">'+
    '<a class="thumb" href="'+L+'" target="_blank" rel="noopener" aria-label="'+esc(e.title)+'">'+thumb(e)+badge+'<span class="cat '+e.category+'">'+CATS[e.category]+'</span>'+(e.recurrence?'<span class="recur">↻ '+esc(e.recurrence.split(",")[0])+'</span>':'')+stBadge(e)+'</a>'+
    '<div class="body">'+(S.scope==="all"&&e.garden_route?'<span class="grtag">Garden Route</span>':'')+
      '<h3><a href="'+L+'" target="_blank" rel="noopener">'+esc(e.title)+'</a></h3>'+
      '<div class="when">'+when(e)+(e.time?" · "+esc(e.time):"")+'</div>'+
      (e.status_note?'<div class="stnote'+(isOff(e)?" off":"")+'">'+esc(e.status_note)+'</div>':'')+
      '<div class="where">'+PIN+'<span>'+esc(e.venue||"")+(e.venue?", ":"")+esc(e.town)+'</span></div>'+atRest(e)+
      (e.recurrence?'<div class="notes">'+esc(e.recurrence)+'</div>':(e.notes&&!/^(Quicket|Webtickets) category/.test(e.notes)?'<div class="notes">'+esc(e.notes)+'</div>':''))+
      '<div class="foot"><a class="btn" href="'+L+'" target="_blank" rel="noopener">'+blab(e)+ARROW+'</a>'+(price?'<span class="price">'+esc(price)+'</span>':'')+
      shareBtn(e)+'<a class="src" href="'+esc(e.source_url)+'" target="_blank" rel="noopener" title="Source: '+esc(e.source_name)+'">via '+esc(e.source_name.replace(/\s*\(.*\)$/,""))+'</a></div>'+
    '</div></article>';
}
function grouped(list){
  var h="",cur="";
  list.forEach(function(e){var m=nextDate(e).slice(0,7);if(m!==cur){if(cur)h+='</div>';cur=m;h+='<div class="month">'+monthLabel(m)+'</div><div class="grid">'}h+=card(e)});
  return h+(cur?'</div>':'');
}
function renderList(){
  var A=filtered(false,false),L=A.filter(function(e){return !e._r}),R=A.filter(function(e){return e._r});
  $("count").textContent=countTxt(L.length,R.length);
  if(!A.length){$("view-list").innerHTML='<div class="empty"><b>Nothing matches those filters</b>'+(S.scope==="gr"?'Try “All coast”, or clear a filter.':'Try clearing a filter.')+'</div>';return}
  var gr=L.filter(function(e){return e.garden_route}),wide=L.filter(function(e){return !e.garden_route});
  var h="";
  if(!S.q&&!S.month&&!S.town&&L.length){
    var lim=iso(new Date(Date.now()+9*864e5));
    var soon=L.filter(function(e){var n=nextDate(e);return n>=TODAY&&n<=lim}).sort(function(a,b){return (b.garden_route-a.garden_route)||nextDate(a).localeCompare(nextDate(b))}).slice(0,14);
    if(soon.length>2)h+='<div class="sec"><h2>Happening soon</h2><span class="pill">next 10 days</span></div><div class="soon">'+soon.map(card).join("")+'</div>';
  }
  var rgr=R.filter(function(e){return e.garden_route}),rwide=R.filter(function(e){return !e.garden_route});
  if(gr.length)h+='<div class="sec"><h2>Garden Route</h2><span class="pill">'+gr.length+'</span></div>'+grouped(gr);
  if(rgr.length)h+=restSection(rgr,"Garden Route restaurants &amp; pubs");
  if(wide.length)h+='<div class="sec"><h2>Rest of the coast</h2><span class="pill">'+wide.length+' · Cape Town – Jeffreys Bay</span></div>'+grouped(wide);
  if(rwide.length)h+=restSection(rwide,"Restaurants &amp; pubs, rest of the coast");
  $("view-list").innerHTML=h;
}
function renderCal(){
  if(!S.calMonth)S.calMonth=S.month||(MONTHS.indexOf(TODAY.slice(0,7))>=0?TODAY.slice(0,7):MONTHS[0]);
  var L=filtered(true,true);
  var p=S.calMonth.split("-"),y=+p[0],m=+p[1]-1;
  $("calTitle").textContent=MNL[m]+" "+y;
  var i=MONTHS.indexOf(S.calMonth);$("calPrev").disabled=i<=0;$("calNext").disabled=i>=MONTHS.length-1;
  var first=new Date(y,m,1),start=(first.getDay()+6)%7,days=new Date(y,m+1,0).getDate();
  var h=["Mon","Tue","Wed","Thu","Fri","Sat","Sun"].map(function(d){return '<div class="dow">'+d+'</div>'}).join("");
  for(var k=0;k<start;k++)h+='<div class="day out"></div>';
  for(var d=1;d<=days;d++){
    var ds=iso(new Date(y,m,d));
    var on=L.filter(function(e){return onDay(e,ds)});
    var chips=on.slice(0,3).map(function(e){var cont=!occ(e)&&e.end_date&&e.start_date<ds;
      return '<div class="chip '+e.category+(e.garden_route?"":" wide")+(isOff(e)?" off":"")+'" title="'+esc(e.title)+(STL[e.status]?" ("+STL[e.status]+")":"")+'">'+(cont?"↳ ":"")+(STL[e.status]?"<b>"+STL[e.status]+":</b> ":"")+esc(e.title)+(e._r&&e.day_labels&&e.day_labels[ds]?": "+esc(e.day_labels[ds]):"")+'</div>'}).join("");
    var dots='<span class="dots">'+on.slice(0,6).map(function(e){return '<i class="dot '+e.category+'"></i>'}).join("")+'</span>';
    h+='<div class="day'+(on.length?" has":"")+(ds<TODAY?" past":"")+(ds===TODAY?" today":"")+(S.calDay===ds?" sel":"")+'" data-d="'+ds+'"><span class="n">'+d+'</span>'+chips+(on.length>3?'<span class="more">+'+(on.length-3)+' more</span>':'')+dots+'</div>';
  }
  $("calGrid").innerHTML=h;
  var inm=L.filter(function(e){return inMonth(e,S.calMonth)&&(!e._r||occ(e))});
  $("count").textContent=countTxt(inm.filter(function(e){return !e._r}).length,inm.filter(function(e){return e._r}).length)+" in "+MNL[m];
  renderDay(L);
}
function renderDay(L){
  if(!S.calDay||S.calDay.slice(0,7)!==S.calMonth){$("calDay").innerHTML='<p class="resultline">Tap a day to see what\u2019s on.</p>';return}
  L=L||filtered(true,true);
  var on=L.filter(function(e){return onDay(e,S.calDay)});
  $("calDay").innerHTML='<h3>'+fmt(pd(S.calDay),true)+' · '+countTxt(on.filter(function(e){return !e._r}).length,on.filter(function(e){return e._r}).length)+'</h3>'+(on.length?'<div class="grid">'+on.map(card).join("")+'</div>':'<p class="resultline">Nothing listed for this day.</p>');
}
function popup(g){
  return '<div class="pop">'+g.map(function(e){return '<div class="pe"><a class="pt" href="'+esc(link(e))+'" target="_blank" rel="noopener">'+thumb(e)+'</a><div><h4>'+esc(e.title)+'</h4><p>'+when(e)+(e.time?" · "+esc(e.time):"")+'<br>'+esc(e.venue||"")+(e.venue?", ":"")+esc(e.town)+'</p>'+
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
var COL={concert:"#2a6f97",festival:"#e76f51",musical:"#8e4ec6",market:"#5b8c2a",funrun:"#d63384",community:"#b7791f",arts:"#0f766e",quiz:"#4f46e5",festive:"#b4233c",restaurant:"#c2410c"};
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
    ["concert","festival","market","funrun","musical","arts","quiz","festive","community","restaurant"].filter(function(c){return by[c]}).map(function(c){return '<span class="stat"><b>'+by[c]+'</b> '+CATPL[c]+'</span>'}).join("");
}
function render(){
  ["list","cal","map"].forEach(function(v){$("view-"+v).hidden=S.view!==v});
  Array.prototype.forEach.call(document.querySelectorAll(".views button"),function(b){b.classList.toggle("on",b.dataset.view===S.view)});
  Array.prototype.forEach.call(document.querySelectorAll("#catChips button"),function(b){b.classList.toggle("on",b.dataset.nye?!!S.nye:b.dataset.cat===S.cat)});
  stats();
  var af=[];if(S.nye)af.push("New Year's Eve");if(S.town)af.push(S.town);if(S.month)af.push(monthLabel(S.month));if(S.q)af.push("“"+S.q+"”");
  $("activeFilters").textContent=af.length?"· "+af.join(" · "):"";
  var hid=EV.filter(function(e){return isOff(e)&&endOf(e)>=TODAY&&matches(e,S.view==="cal",true)}).length;
  $("offToggle").hidden=!hid;$("offToggle").textContent=S.off?"Hide postponed/cancelled ("+hid+")":hid+" postponed/cancelled hidden · show";
  if(S.view==="list")renderList();else if(S.view==="cal")renderCal();else renderMap();
  writeHash();
}
function syncControls(){
  $("q").value=S.q;$("month").value=S.month;$("town").value=S.town;
  $("scopeGR").classList.toggle("on",S.scope==="gr");$("scopeAll").classList.toggle("on",S.scope==="all");
  $("scopeGR").setAttribute("aria-pressed",S.scope==="gr");$("scopeAll").setAttribute("aria-pressed",S.scope==="all");
}
function writeHash(){var p=[];if(S.view!=="list")p.push("view="+S.view);if(S.scope!=="gr")p.push("scope=all");if(S.off)p.push("off=1");if(S.nye)p.push("nye=1");if(S.event)p.push("event="+encodeURIComponent(S.event));
  ["town","cat","month","q"].forEach(function(k){if(S[k])p.push(k+"="+encodeURIComponent(S[k]))});
  var h=p.length?"#"+p.join("&"):"";if(location.hash!==h)history.replaceState(null,"",h||location.pathname+location.search)}
function readHash(){location.hash.replace(/^#/,"").split("&").forEach(function(kv){var a=kv.split("=");if(!a[0])return;var v=decodeURIComponent(a[1]||"");
  if(a[0]==="view"&&/^(list|cal|map)$/.test(v))S.view=v;else if(a[0]==="view"&&v==="rest")S.cat="restaurant";else if(a[0]==="rest")S.event="r:"+v;else if(a[0]==="scope"&&v==="all")S.scope="all";else if(a[0]==="off"&&v==="1")S.off=true;else if(a[0]==="nye"&&v==="1")S.nye=true;else if(a[0]==="event")S.event=v;else if(/^(town|cat|month|q)$/.test(a[0]))S[a[0]]=v})}
function setScope(s){S.scope=s;buildTowns();syncControls();render();if(map)map.fitBounds(s==="all"?[[-33.5,18.3],[-34.4,25.0]]:GRB)}
function bind(){
  var t;$("q").addEventListener("input",function(){var v=this.value.trim();clearTimeout(t);t=setTimeout(function(){S.q=v;render()},120)});
  $("town").addEventListener("change",function(){S.town=this.value;render()});
  $("month").addEventListener("change",function(){S.month=this.value;if(S.month){S.calMonth=S.month;S.calDay=null}render()});
  $("scopeGR").addEventListener("click",function(){setScope("gr")});
  $("scopeAll").addEventListener("click",function(){setScope("all")});
  $("offToggle").addEventListener("click",function(){S.off=!S.off;buildTowns();syncControls();render()});
  $("reset").addEventListener("click",function(){S.q=S.town=S.cat=S.month="";S.nye=false;S.calDay=null;buildTowns();syncControls();render()});
  Array.prototype.forEach.call(document.querySelectorAll("#catChips button"),function(b){b.addEventListener("click",function(){if(b.dataset.nye)S.nye=!S.nye;else S.cat=b.dataset.cat;render()})});
  Array.prototype.forEach.call(document.querySelectorAll(".views button"),function(b){b.addEventListener("click",function(){S.view=b.dataset.view;render();toTop();requestAnimationFrame(toTop)})});
  $("calPrev").addEventListener("click",function(){var i=MONTHS.indexOf(S.calMonth);if(i>0){S.calMonth=MONTHS[i-1];renderCal()}});
  $("calNext").addEventListener("click",function(){var i=MONTHS.indexOf(S.calMonth);if(i<MONTHS.length-1){S.calMonth=MONTHS[i+1];renderCal()}});
  $("calGrid").addEventListener("click",function(ev){var d=ev.target.closest(".day[data-d]");if(!d)return;S.calDay=d.dataset.d;renderCal();$("calDay").scrollIntoView({behavior:"smooth",block:"nearest"})});
  document.addEventListener("click",function(ev){
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
  document.addEventListener("keydown",function(ev){if(ev.key==="Escape"){if(!$("shareMenu").hidden)closeMenu();else closeEvent()}});
  window.addEventListener("resize",function(){var m=$("shareMenu");if(!m.hidden&&window.innerWidth!==(closeMenu._w||0))closeMenu();closeMenu._w=window.innerWidth});closeMenu._w=window.innerWidth;window.addEventListener("scroll",function(){var m=$("shareMenu");if(!m.hidden&&Math.abs(window.scrollY-(m._y||0))>40)closeMenu()},{passive:true});
  window.addEventListener("hashchange",function(){var rm=/(?:^#|&)rest=([^&]+)/.exec(location.hash);if(rm){openEvent("r:"+decodeURIComponent(rm[1]));return}var m=/(?:^#|&)event=([^&]+)/.exec(location.hash);if(m){var id=decodeURIComponent(m[1]);if(id!==S.event)openEvent(id)}else if(S.event)closeEvent()});
  var bar=$("bar");window.addEventListener("scroll",function(){bar.classList.toggle("stuck",bar.getBoundingClientRect().top<=0)},{passive:true});
}
bind();
init(window.EVENTS||[]);
if(/^https?:/.test(location.protocol)){
  fetch("data/events.json",{cache:"no-cache"}).then(function(r){return r.ok?r.json():null}).then(function(d){
    if(Array.isArray(d)&&d.length&&JSON.stringify(d)!==JSON.stringify(window.EVENTS||[]))init(d);
  }).catch(function(){});
}
})();
