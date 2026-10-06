/* Garden Route Events: static app, no build step. Data comes from window.EVENTS (data/events.js). */
(function(){
"use strict";
var GR_ORDER=["Mossel Bay","Hartenbos","Groot Brak","George","Oudtshoorn","Wilderness","Sedgefield","Knysna","Plettenberg Bay","The Crags","Nature's Valley","Storms River","Tsitsikamma"];
var WIDE_ORDER=["Cape Town","Somerset West","Kleinmond","Pringle Bay","Hermanus","Stanford","Gansbaai","Struisbaai","L'Agulhas","Riversdale","Stilbaai","Humansdorp","St Francis Bay","Jeffreys Bay"];
var MONTHS=["2026-10","2026-11","2026-12","2027-01","2027-02"];
var MN=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"];
var MNL=["January","February","March","April","May","June","July","August","September","October","November","December"];
var DOW=["Sun","Mon","Tue","Wed","Thu","Fri","Sat"];
var CATS={concert:"Concert",festival:"Festival",musical:"Musical",market:"Market",funrun:"Run / walk / trail",community:"Church / community"};
var CATPL={concert:"concerts",festival:"festivals",musical:"musicals",market:"markets",funrun:"runs, walks & trails",community:"church & community"};
var ICON={
  concert:'<svg viewBox="0 0 24 24"><path d="M9 3v10.55A4 4 0 107 21a4 4 0 004-4V7h6V3H9z"/></svg>',
  festival:'<svg viewBox="0 0 24 24"><path d="M12 2l1 0v2.2l5-1.2v4l-5 1.2V8.9L21.5 21H15l-3-5-3 5H2.5L11 8.9V2z"/></svg>',
  musical:'<svg viewBox="0 0 24 24"><path d="M12 2l2.9 6.9 7.1.5-5.4 4.6 1.7 7L12 17.3 5.7 21l1.7-7L2 9.4l7.1-.5z"/></svg>',
  funrun:'<svg viewBox="0 0 24 24"><path d="M13.5 5.5a2 2 0 100-4 2 2 0 000 4zM9.8 8.9L7 23h2.1l1.8-8 2.1 2v6h2v-7.5l-2.1-2 .6-3A7.3 7.3 0 0019 13v-2a5 5 0 01-4.3-2.4l-1-1.6a2 2 0 00-1.7-1l-.8.1L6 8.3V13h2V9.6z"/></svg>',
  community:'<svg viewBox="0 0 24 24"><path d="M11 2h2v3h3v2h-3v3.2l7 4.1V22h-6v-4a2 2 0 00-4 0v4H4v-7.7l7-4.1V7H8V5h3z"/></svg>',
  market:'<svg viewBox="0 0 24 24"><path d="M3 9h18l-1.8 11.2A1 1 0 0118.2 21H5.8a1 1 0 01-1-.8L3 9zm5.2-1L12 2.5 15.8 8h-2.4L12 5.9 10.6 8z"/></svg>'};
var PIN='<svg viewBox="0 0 24 24"><path d="M12 2a7 7 0 017 7c0 5-7 13-7 13S5 14 5 9a7 7 0 017-7zm0 4.5A2.5 2.5 0 1012 11.5 2.5 2.5 0 0012 6.5z"/></svg>';
var ARROW='<svg viewBox="0 0 24 24"><path d="M13 5l7 7-7 7-1.4-1.4 4.6-4.6H4v-2h12.2l-4.6-4.6z"/></svg>';
var S={scope:"gr",q:"",town:"",cat:"",month:"",view:"list",calMonth:null,calDay:null,off:false};
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
function onDay(e,ds){var o=occ(e);return o?o.indexOf(ds)>=0:(e.start_date<=ds&&endOf(e)>=ds)}
function inMonth(e,m){var o=occ(e);if(o)return o.some(function(d){return d.slice(0,7)===m});return e.start_date.slice(0,7)<=m&&endOf(e).slice(0,7)>=m}
function fmt(d,yr){return DOW[d.getDay()]+" "+d.getDate()+" "+MN[d.getMonth()]+(yr?" "+d.getFullYear():"")}
function when(e){
  if(occ(e)){return "Next: "+fmt(pd(nextDate(e)),false)}
  var a=pd(e.start_date);if(!e.end_date||e.end_date===e.start_date)return fmt(a,true);
  var b=pd(e.end_date);return fmt(a,a.getFullYear()!==b.getFullYear())+" – "+fmt(b,true)}
function monthLabel(m){var p=m.split("-");return MNL[+p[1]-1]+" "+p[0]}
function link(e){return e.ticket_url||e.source_url}
function priceTxt(p){if(!p)return "";return /^\d/.test(p)?"From R"+p:(/^R\d/.test(p)?"From "+p:p)}
function thumb(e,cls){
  if(e.image)return '<img src="'+esc(e.image)+'" alt="" loading="lazy" decoding="async">';
  return '<div class="ph '+e.category+'">'+ICON[e.category]+'</div>';
}

function init(data){
  EV=(data||[]).slice();
  $("built").textContent=window.EVENTS_BUILT||(EV[0]&&EV[0].last_checked)||"";
  var mo='<option value="">Any month</option>';MONTHS.forEach(function(m){mo+='<option value="'+m+'">'+monthLabel(m)+'</option>'});$("month").innerHTML=mo;
  readHash();buildTowns();syncControls();render();
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
  if(!ignoreMonth&&S.month&&!inMonth(e,S.month))return false;
  if(S.q){var hay=(e.title+" "+e.venue+" "+e.town+" "+e.venue_address+" "+e.notes+" "+e.region+" "+e.category+" "+(e.recurrence||"")).toLowerCase();
    if(!S.q.toLowerCase().split(/\s+/).every(function(w){return hay.indexOf(w)>=0}))return false}
  return true;
}
function filtered(ignoreMonth,includePast){
  return EV.filter(function(e){return matches(e,ignoreMonth)&&(includePast||endOf(e)>=TODAY)})
    .sort(function(a,b){return (b.garden_route-a.garden_route)||nextDate(a).localeCompare(nextDate(b))||a.title.localeCompare(b.title)});
}

function card(e){
  var nd=pd(nextDate(e)),multi=!occ(e)&&e.end_date&&e.end_date!==e.start_date;
  var badge='<div class="datebadge"><span class="d">'+nd.getDate()+'</span><span class="m">'+MN[nd.getMonth()]+'</span>'+(multi?'<span class="to">to '+pd(e.end_date).getDate()+' '+MN[pd(e.end_date).getMonth()]+'</span>':'')+'</div>';
  var L=esc(link(e)),price=priceTxt(e.price_from);
  return '<article class="card'+(isOff(e)?" is-off":"")+'">'+
    '<a class="thumb" href="'+L+'" target="_blank" rel="noopener" aria-label="'+esc(e.title)+'">'+thumb(e)+badge+'<span class="cat '+e.category+'">'+CATS[e.category]+'</span>'+(e.recurrence?'<span class="recur">↻ '+esc(e.recurrence.split(",")[0])+'</span>':'')+stBadge(e)+'</a>'+
    '<div class="body">'+(S.scope==="all"&&e.garden_route?'<span class="grtag">Garden Route</span>':'')+
      '<h3><a href="'+L+'" target="_blank" rel="noopener">'+esc(e.title)+'</a></h3>'+
      '<div class="when">'+when(e)+(e.time?" · "+esc(e.time):"")+'</div>'+
      (e.status_note?'<div class="stnote'+(isOff(e)?" off":"")+'">'+esc(e.status_note)+'</div>':'')+
      '<div class="where">'+PIN+'<span>'+esc(e.venue||"")+(e.venue?", ":"")+esc(e.town)+'</span></div>'+
      (e.recurrence?'<div class="notes">'+esc(e.recurrence)+'</div>':(e.notes&&!/^(Quicket|Webtickets) category/.test(e.notes)?'<div class="notes">'+esc(e.notes)+'</div>':''))+
      '<div class="foot"><a class="btn" href="'+L+'" target="_blank" rel="noopener">'+(e.ticket_url?"Tickets":"Event page")+ARROW+'</a>'+(price?'<span class="price">'+esc(price)+'</span>':'')+
      '<a class="src" href="'+esc(e.source_url)+'" target="_blank" rel="noopener" title="Source: '+esc(e.source_name)+'">via '+esc(e.source_name.replace(/\s*\(.*\)$/,""))+'</a></div>'+
    '</div></article>';
}
function grouped(list){
  var h="",cur="";
  list.forEach(function(e){var m=nextDate(e).slice(0,7);if(m!==cur){if(cur)h+='</div>';cur=m;h+='<div class="month">'+monthLabel(m)+'</div><div class="grid">'}h+=card(e)});
  return h+(cur?'</div>':'');
}
function renderList(){
  var L=filtered(false,false);
  $("count").textContent=L.length+" event"+(L.length===1?"":"s");
  if(!L.length){$("view-list").innerHTML='<div class="empty"><b>Nothing matches those filters</b>'+(S.scope==="gr"?'Try “All coast”, or clear a filter.':'Try clearing a filter.')+'</div>';return}
  var gr=L.filter(function(e){return e.garden_route}),wide=L.filter(function(e){return !e.garden_route});
  var h="";
  if(!S.q&&!S.month&&!S.town){
    var lim=iso(new Date(Date.now()+9*864e5));
    var soon=L.filter(function(e){var n=nextDate(e);return n>=TODAY&&n<=lim}).sort(function(a,b){return (b.garden_route-a.garden_route)||nextDate(a).localeCompare(nextDate(b))}).slice(0,14);
    if(soon.length>2)h+='<div class="sec"><h2>Happening soon</h2><span class="pill">next 10 days</span></div><div class="soon">'+soon.map(card).join("")+'</div>';
  }
  if(gr.length)h+='<div class="sec"><h2>Garden Route</h2><span class="pill">'+gr.length+'</span></div>'+grouped(gr);
  if(wide.length)h+='<div class="sec"><h2>Rest of the coast</h2><span class="pill">'+wide.length+' · Cape Town – Jeffreys Bay</span></div>'+grouped(wide);
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
      return '<div class="chip '+e.category+(e.garden_route?"":" wide")+(isOff(e)?" off":"")+'" title="'+esc(e.title)+(STL[e.status]?" ("+STL[e.status]+")":"")+'">'+(cont?"↳ ":"")+(STL[e.status]?"<b>"+STL[e.status]+":</b> ":"")+esc(e.title)+'</div>'}).join("");
    var dots='<span class="dots">'+on.slice(0,6).map(function(e){return '<i class="dot '+e.category+'"></i>'}).join("")+'</span>';
    h+='<div class="day'+(on.length?" has":"")+(ds<TODAY?" past":"")+(ds===TODAY?" today":"")+(S.calDay===ds?" sel":"")+'" data-d="'+ds+'"><span class="n">'+d+'</span>'+chips+(on.length>3?'<span class="more">+'+(on.length-3)+' more</span>':'')+dots+'</div>';
  }
  $("calGrid").innerHTML=h;
  var cnt=L.filter(function(e){return inMonth(e,S.calMonth)}).length;
  $("count").textContent=cnt+" event"+(cnt===1?"":"s")+" in "+MNL[m];
  renderDay(L);
}
function renderDay(L){
  if(!S.calDay||S.calDay.slice(0,7)!==S.calMonth){$("calDay").innerHTML='<p class="resultline">Tap a day to see what\u2019s on.</p>';return}
  L=L||filtered(true,true);
  var on=L.filter(function(e){return onDay(e,S.calDay)});
  $("calDay").innerHTML='<h3>'+fmt(pd(S.calDay),true)+' · '+on.length+' event'+(on.length===1?"":"s")+'</h3>'+(on.length?'<div class="grid">'+on.map(card).join("")+'</div>':'<p class="resultline">Nothing listed for this day.</p>');
}
function popup(g){
  return '<div class="pop">'+g.map(function(e){return '<div class="pe"><a class="pt" href="'+esc(link(e))+'" target="_blank" rel="noopener">'+thumb(e)+'</a><div><h4>'+esc(e.title)+'</h4><p>'+when(e)+(e.time?" · "+esc(e.time):"")+'<br>'+esc(e.venue||"")+(e.venue?", ":"")+esc(e.town)+'</p>'+
    '<span class="pc '+e.category+'">'+CATS[e.category]+'</span>'+(STL[e.status]?'<span class="pc st'+(isOff(e)?" off":"")+'">'+STL[e.status]+'</span>':'')+(e.geo_source==="town centroid"?'<span style="font-size:.7rem;color:#888">approx.</span> ':'')+'<br><a class="go" href="'+esc(link(e))+'" target="_blank" rel="noopener">'+(e.ticket_url?"Tickets":"Event page")+' →</a></div></div>'}).join("")+'</div>';
}
var COL={concert:"#2a6f97",festival:"#e76f51",musical:"#8e4ec6",market:"#5b8c2a",funrun:"#d63384",community:"#b7791f"};
var GRB=[[-33.55,21.95],[-34.2,24.0]];
function renderMap(){
  var L=filtered(false,false).filter(function(e){return e.lat!=null&&e.lng!=null});
  $("count").textContent=L.length+" event"+(L.length===1?"":"s")+" on the map";
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
  var L=scoped();var by={};L.forEach(function(e){by[e.category]=(by[e.category]||0)+1});
  $("stats").innerHTML='<span class="stat"><b>'+L.length+'</b> '+(S.scope==="gr"?"Garden Route":"coastal")+' events</span>'+
    ["concert","festival","market","funrun","musical","community"].filter(function(c){return by[c]}).map(function(c){return '<span class="stat"><b>'+by[c]+'</b> '+CATPL[c]+'</span>'}).join("");
}
function render(){
  ["list","cal","map"].forEach(function(v){$("view-"+v).hidden=S.view!==v});
  Array.prototype.forEach.call(document.querySelectorAll(".views button"),function(b){b.classList.toggle("on",b.dataset.view===S.view)});
  Array.prototype.forEach.call(document.querySelectorAll("#catChips button"),function(b){b.classList.toggle("on",b.dataset.cat===S.cat)});
  stats();
  var af=[];if(S.town)af.push(S.town);if(S.month)af.push(monthLabel(S.month));if(S.q)af.push("“"+S.q+"”");
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
function writeHash(){var p=[];if(S.view!=="list")p.push("view="+S.view);if(S.scope!=="gr")p.push("scope=all");if(S.off)p.push("off=1");
  ["town","cat","month","q"].forEach(function(k){if(S[k])p.push(k+"="+encodeURIComponent(S[k]))});
  var h=p.length?"#"+p.join("&"):"";if(location.hash!==h)history.replaceState(null,"",h||location.pathname+location.search)}
function readHash(){location.hash.replace(/^#/,"").split("&").forEach(function(kv){var a=kv.split("=");if(!a[0])return;var v=decodeURIComponent(a[1]||"");
  if(a[0]==="view"&&/^(list|cal|map)$/.test(v))S.view=v;else if(a[0]==="scope"&&v==="all")S.scope="all";else if(a[0]==="off"&&v==="1")S.off=true;else if(/^(town|cat|month|q)$/.test(a[0]))S[a[0]]=v})}
function setScope(s){S.scope=s;buildTowns();syncControls();render();if(map)map.fitBounds(s==="all"?[[-33.5,18.3],[-34.4,25.0]]:GRB)}
function bind(){
  var t;$("q").addEventListener("input",function(){var v=this.value.trim();clearTimeout(t);t=setTimeout(function(){S.q=v;render()},120)});
  $("town").addEventListener("change",function(){S.town=this.value;render()});
  $("month").addEventListener("change",function(){S.month=this.value;if(S.month){S.calMonth=S.month;S.calDay=null}render()});
  $("scopeGR").addEventListener("click",function(){setScope("gr")});
  $("scopeAll").addEventListener("click",function(){setScope("all")});
  $("offToggle").addEventListener("click",function(){S.off=!S.off;buildTowns();syncControls();render()});
  $("reset").addEventListener("click",function(){S.q=S.town=S.cat=S.month="";S.calDay=null;buildTowns();syncControls();render()});
  Array.prototype.forEach.call(document.querySelectorAll("#catChips button"),function(b){b.addEventListener("click",function(){S.cat=b.dataset.cat;render()})});
  Array.prototype.forEach.call(document.querySelectorAll(".views button"),function(b){b.addEventListener("click",function(){S.view=b.dataset.view;render()})});
  $("calPrev").addEventListener("click",function(){var i=MONTHS.indexOf(S.calMonth);if(i>0){S.calMonth=MONTHS[i-1];renderCal()}});
  $("calNext").addEventListener("click",function(){var i=MONTHS.indexOf(S.calMonth);if(i<MONTHS.length-1){S.calMonth=MONTHS[i+1];renderCal()}});
  $("calGrid").addEventListener("click",function(ev){var d=ev.target.closest(".day[data-d]");if(!d)return;S.calDay=d.dataset.d;renderCal();$("calDay").scrollIntoView({behavior:"smooth",block:"nearest"})});
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
