/* Garden Route Events: static app (no build step). Data: window.EVENTS from data/events.js */
(function(){
"use strict";
var GR_ORDER=["Mossel Bay","Hartenbos","Groot Brak","George","Oudtshoorn","Wilderness","Sedgefield","Knysna","Plettenberg Bay","The Crags","Nature's Valley","Storms River","Tsitsikamma"];
var WIDE_ORDER=["Cape Town","Somerset West","Kleinmond","Pringle Bay","Hermanus","Stanford","Gansbaai","Struisbaai","L'Agulhas","Riversdale","Stilbaai","Humansdorp","St Francis Bay","Jeffreys Bay"];
var MONTHS=["2026-10","2026-11","2026-12","2027-01","2027-02"];
var MN=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"];
var MNL=["January","February","March","April","May","June","July","August","September","October","November","December"];
var DOW=["Sun","Mon","Tue","Wed","Thu","Fri","Sat"];
var S={scope:"gr",q:"",town:"",cat:"",month:"",view:"list",calMonth:null,calDay:null};
var EV=[]; var map=null, layer=null;
var $=function(id){return document.getElementById(id)};
function esc(s){return String(s==null?"":s).replace(/[&<>"']/g,function(c){return {"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]})}
function pd(s){var p=s.split("-");return new Date(+p[0],+p[1]-1,+p[2])}
function iso(d){return d.getFullYear()+"-"+String(d.getMonth()+1).padStart(2,"0")+"-"+String(d.getDate()).padStart(2,"0")}
var TODAY=iso(new Date());
function endOf(e){return e.end_date||e.start_date}
function fmt(d,yr){return DOW[d.getDay()]+" "+d.getDate()+" "+MN[d.getMonth()]+(yr?" "+d.getFullYear():"")}
function when(e){var a=pd(e.start_date);if(!e.end_date||e.end_date===e.start_date)return fmt(a,true);var b=pd(e.end_date);return fmt(a,a.getFullYear()!==b.getFullYear())+" – "+fmt(b,true)}
function monthLabel(m){var p=m.split("-");return MNL[+p[1]-1]+" "+p[0]}
function catLabel(c){return {concert:"Concert",festival:"Festival",musical:"Musical"}[c]||c}
function hostOf(u){try{return new URL(u).hostname.replace(/^www\./,"")}catch(x){return u}}

function init(data){
  EV=(data||[]).slice().sort(function(a,b){return (b.garden_route-a.garden_route)||a.start_date.localeCompare(b.start_date)||a.title.localeCompare(b.title)});
  $("range").textContent="6 Oct 2026 – 28 Feb 2027";
  $("built").textContent=window.EVENTS_BUILT||(EV[0]&&EV[0].last_checked)||"";
  var mo='<option value="">All months</option>';MONTHS.forEach(function(m){mo+='<option value="'+m+'">'+monthLabel(m)+'</option>'});$("month").innerHTML=mo;
  buildTowns(); readHash(); syncControls(); render();
}
function buildTowns(){
  var have={};EV.forEach(function(e){have[e.town]=(have[e.town]||0)+(S.scope==="all"||e.garden_route?1:0)});
  function grp(label,order,isGR){var extra=Object.keys(have).filter(function(t){return order.indexOf(t)<0&&EV.some(function(e){return e.town===t&&!!e.garden_route===isGR})});
    var list=order.concat(extra).filter(function(t){return have[t]});if(!list.length)return "";
    return '<optgroup label="'+label+'">'+list.map(function(t){return '<option value="'+esc(t)+'">'+esc(t)+' ('+have[t]+')</option>'}).join("")+'</optgroup>'}
  var h='<option value="">All towns</option>'+grp("Garden Route",GR_ORDER,true);
  if(S.scope==="all")h+=grp("Rest of the coast",WIDE_ORDER,false);
  $("town").innerHTML=h;
  if(S.town&&!have[S.town])S.town="";
  $("town").value=S.town;
}
function matches(e,ignoreMonth){
  if(S.scope==="gr"&&!e.garden_route)return false;
  if(S.town&&e.town!==S.town)return false;
  if(S.cat&&e.category!==S.cat)return false;
  if(!ignoreMonth&&S.month){var ms=S.month+"-01",me=S.month+"-31";if(e.start_date>me||endOf(e)<ms)return false}
  if(S.q){var hay=(e.title+" "+e.venue+" "+e.town+" "+e.venue_address+" "+e.notes+" "+e.region+" "+e.category).toLowerCase();
    var ok=S.q.toLowerCase().split(/\s+/).every(function(w){return hay.indexOf(w)>=0});if(!ok)return false}
  return true;
}
function filtered(ignoreMonth,includePast){return EV.filter(function(e){return matches(e,ignoreMonth)&&(includePast||endOf(e)>=TODAY)})}

function card(e){
  var price=e.price_from?(/^\d/.test(e.price_from)?"From R"+e.price_from:esc(e.price_from)):"";
  var alts=(e.alt_sources||[]).map(function(u,i){return '<a href="'+esc(u)+'" target="_blank" rel="noopener">'+esc(hostOf(u))+'</a>'}).join(", ");
  return '<article class="card'+(e.garden_route?" isgr":"")+'">'+
    '<div class="badges"><span class="badge '+e.category+'">'+catLabel(e.category)+'</span>'+(e.garden_route&&S.scope==="all"?'<span class="badge grb">Garden Route</span>':'')+'</div>'+
    '<h4>'+esc(e.title)+'</h4>'+
    '<div class="when">'+when(e)+(e.time?" · "+esc(e.time):"")+'</div>'+
    '<div class="meta">'+esc(e.venue||"")+(e.venue?", ":"")+esc(e.town)+(price?" · "+price:"")+'</div>'+
    (e.notes&&!/^(Quicket|Webtickets) category/.test(e.notes)?'<div class="notes">'+esc(e.notes)+'</div>':'')+
    '<div class="actions">'+(e.ticket_url?'<a class="btn" href="'+esc(e.ticket_url)+'" target="_blank" rel="noopener">Tickets</a>':'')+
    '<a href="'+esc(e.source_url)+'" target="_blank" rel="noopener">Source: '+esc(e.source_name)+'</a>'+(alts?'<span class="meta">Also: '+alts+'</span>':'')+'</div>'+
  '</article>';
}
function renderList(){
  var L=filtered(false,false);
  $("count").textContent=L.length+" event"+(L.length===1?"":"s");
  if(!L.length){$("view-list").innerHTML='<div class="empty">No events match these filters.'+(S.scope==="gr"?' Try “All coast”.':'')+'</div>';return}
  var gr=L.filter(function(e){return e.garden_route}),wide=L.filter(function(e){return !e.garden_route});
  var h="";
  if(gr.length)h+=(S.scope==="all"?'<h3 class="sec gr">Garden Route · '+gr.length+'</h3>':'')+'<div class="grid">'+gr.map(card).join("")+'</div>';
  if(wide.length)h+='<h3 class="sec">Rest of the coast (Cape Town – Jeffreys Bay) · '+wide.length+'</h3><div class="grid">'+wide.map(card).join("")+'</div>';
  $("view-list").innerHTML=h;
}
function renderCal(){
  if(!S.calMonth)S.calMonth=S.month||(TODAY.slice(0,7)>=MONTHS[0]&&TODAY.slice(0,7)<=MONTHS[4]?TODAY.slice(0,7):MONTHS[0]);
  var L=filtered(true,true);
  var p=S.calMonth.split("-"),y=+p[0],m=+p[1]-1;
  $("calTitle").textContent=MNL[m]+" "+y;
  var i=MONTHS.indexOf(S.calMonth);$("calPrev").disabled=i<=0;$("calNext").disabled=i>=MONTHS.length-1;
  var first=new Date(y,m,1),start=(first.getDay()+6)%7,days=new Date(y,m+1,0).getDate();
  var h=["Mon","Tue","Wed","Thu","Fri","Sat","Sun"].map(function(d){return '<div class="dow">'+d+'</div>'}).join("");
  for(var k=0;k<start;k++)h+='<div class="day out"></div>';
  var cnt=0;
  for(var d=1;d<=days;d++){
    var ds=iso(new Date(y,m,d));
    var on=L.filter(function(e){return e.start_date<=ds&&endOf(e)>=ds});
    cnt+=on.filter(function(e){return e.start_date===ds||d===1}).length;
    var chips=on.slice(0,3).map(function(e){var multi=e.end_date&&e.end_date!==e.start_date;
      var cont=multi&&e.start_date<ds;
      return '<div class="chip '+e.category+(multi?" multi":"")+(e.garden_route?"":" wide")+'" title="'+esc(e.title)+'">'+(cont?"↳ ":"")+esc(e.title)+'</div>'}).join("");
    h+='<div class="day'+(on.length?" has":"")+(ds<TODAY?" past":"")+(S.calDay===ds?" sel":"")+'" data-d="'+ds+'"><span class="n">'+d+'</span>'+chips+(on.length>3?'<span class="more">+'+(on.length-3)+' more</span>':'')+'</div>';
  }
  $("calGrid").innerHTML=h;
  var inMonth=L.filter(function(e){return e.start_date<=S.calMonth+"-31"&&endOf(e)>=S.calMonth+"-01"});
  $("count").textContent=inMonth.length+" event"+(inMonth.length===1?"":"s")+" in "+MNL[m];
  renderDay(L);
}
function renderDay(L){
  if(!S.calDay||S.calDay.slice(0,7)!==S.calMonth){$("calDay").innerHTML='<p class="meta">Click a day to see its events.</p>';return}
  L=L||filtered(true,true);
  var on=L.filter(function(e){return e.start_date<=S.calDay&&endOf(e)>=S.calDay});
  $("calDay").innerHTML='<h3 class="sec">'+fmt(pd(S.calDay),true)+' · '+on.length+' event'+(on.length===1?"":"s")+'</h3>'+(on.length?'<div class="grid">'+on.map(card).join("")+'</div>':'<p class="meta">Nothing listed for this day.</p>');
}
function popup(group){
  return '<div class="pop">'+group.map(function(e){return '<div class="pe"><h5>'+esc(e.title)+'</h5><p>'+when(e)+(e.time?" · "+esc(e.time):"")+'<br>'+esc(e.venue||"")+(e.venue?", ":"")+esc(e.town)+'<br>'+catLabel(e.category)+(e.geo_source==="town centroid"?' · <i>approx. location</i>':'')+'</p>'+
    (e.ticket_url?'<a href="'+esc(e.ticket_url)+'" target="_blank" rel="noopener">Tickets</a> · ':'')+'<a href="'+esc(e.source_url)+'" target="_blank" rel="noopener">Source</a></div>'}).join("")+'</div>';
}
var COL={concert:"#2f6fb5",festival:"#d9622b",musical:"#8a3fb0"};
function renderMap(){
  var L=filtered(false,false).filter(function(e){return e.lat!=null&&e.lng!=null});
  $("count").textContent=L.length+" event"+(L.length===1?"":"s")+" on map";
  if(typeof window.L==="undefined"){$("map").innerHTML='<div class="empty">Map library could not load (offline?). The list and calendar still work.</div>';return}
  if(!map){map=window.L.map("map",{scrollWheelZoom:true}).fitBounds([[-33.55,21.95],[-34.2,24.0]]);
    window.L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",{maxZoom:18,attribution:'&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'}).addTo(map);
    layer=window.L.layerGroup().addTo(map)}
  layer.clearLayers();
  var groups={};L.forEach(function(e){var k=(+e.lat).toFixed(4)+","+(+e.lng).toFixed(4);(groups[k]=groups[k]||[]).push(e)});
  var wide=[],gr=[];
  Object.keys(groups).forEach(function(k){var g=groups[k];(g.some(function(e){return e.garden_route})?gr:wide).push(g)});
  function add(g){var isgr=g.some(function(e){return e.garden_route});var c=COL[g[0].category]||"#555";
    var mk=window.L.circleMarker([+g[0].lat,+g[0].lng],isgr?{radius:Math.min(9+g.length,16),color:"#fff",weight:2,fillColor:c,fillOpacity:.95}:{radius:5,color:"#7d8a84",weight:1,fillColor:"#9aa7a1",fillOpacity:.55});
    mk.bindPopup(popup(g),{maxHeight:300});if(g.length>1)mk.bindTooltip(g.length+" events");mk.addTo(layer)}
  wide.forEach(add);gr.forEach(add);
  setTimeout(function(){map.invalidateSize()},50);
}
function render(){
  ["list","cal","map"].forEach(function(v){$("view-"+v).hidden=S.view!==v});
  Array.prototype.forEach.call(document.querySelectorAll(".tabs button"),function(b){b.classList.toggle("on",b.dataset.view===S.view)});
  if(S.view==="list")renderList();else if(S.view==="cal")renderCal();else renderMap();
  writeHash();
}
function syncControls(){
  $("q").value=S.q;$("cat").value=S.cat;$("month").value=S.month;$("town").value=S.town;
  $("scopeGR").classList.toggle("on",S.scope==="gr");$("scopeAll").classList.toggle("on",S.scope==="all");
  $("scopeGR").setAttribute("aria-pressed",S.scope==="gr");$("scopeAll").setAttribute("aria-pressed",S.scope==="all");
}
function writeHash(){var p=[];if(S.view!=="list")p.push("view="+S.view);if(S.scope!=="gr")p.push("scope=all");
  ["town","cat","month","q"].forEach(function(k){if(S[k])p.push(k+"="+encodeURIComponent(S[k]))});
  var h=p.length?"#"+p.join("&"):"";if(location.hash!==h)history.replaceState(null,"",h||location.pathname+location.search)}
function readHash(){location.hash.replace(/^#/,"").split("&").forEach(function(kv){var a=kv.split("=");if(!a[0])return;var v=decodeURIComponent(a[1]||"");
  if(a[0]==="view"&&/^(list|cal|map)$/.test(v))S.view=v;else if(a[0]==="scope"&&v==="all")S.scope="all";else if(/^(town|cat|month|q)$/.test(a[0]))S[a[0]]=v});
  buildTowns()}
function bind(){
  $("q").addEventListener("input",function(){S.q=this.value.trim();render()});
  $("town").addEventListener("change",function(){S.town=this.value;render()});
  $("cat").addEventListener("change",function(){S.cat=this.value;render()});
  $("month").addEventListener("change",function(){S.month=this.value;if(S.month){S.calMonth=S.month;S.calDay=null}render()});
  $("scopeGR").addEventListener("click",function(){S.scope="gr";buildTowns();syncControls();render();if(map)map.fitBounds([[-33.55,21.95],[-34.2,24.0]])});
  $("scopeAll").addEventListener("click",function(){S.scope="all";buildTowns();syncControls();render();if(map)map.setView([-33.95,22.4],7)});
  $("reset").addEventListener("click",function(){S.q=S.town=S.cat=S.month="";S.calDay=null;buildTowns();syncControls();render()});
  Array.prototype.forEach.call(document.querySelectorAll(".tabs button"),function(b){b.addEventListener("click",function(){S.view=b.dataset.view;render()})});
  $("calPrev").addEventListener("click",function(){var i=MONTHS.indexOf(S.calMonth);if(i>0){S.calMonth=MONTHS[i-1];renderCal()}});
  $("calNext").addEventListener("click",function(){var i=MONTHS.indexOf(S.calMonth);if(i<MONTHS.length-1){S.calMonth=MONTHS[i+1];renderCal()}});
  $("calGrid").addEventListener("click",function(ev){var d=ev.target.closest(".day[data-d]");if(!d)return;S.calDay=d.dataset.d;renderCal();$("calDay").scrollIntoView({behavior:"smooth",block:"nearest"})});
}
bind();
init(window.EVENTS||[]);
// When served over http(s), prefer the JSON file (same data; lets you update events.json alone).
if(/^https?:/.test(location.protocol)){
  fetch("data/events.json",{cache:"no-cache"}).then(function(r){return r.ok?r.json():null}).then(function(d){
    if(Array.isArray(d)&&d.length&&(!window.EVENTS||JSON.stringify(d)!==JSON.stringify(window.EVENTS))){init(d)}
  }).catch(function(){});
}
})();
