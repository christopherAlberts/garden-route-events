// Service worker. Network-first for pages, JS, CSS and data (so a new deploy is picked up on the next load,
// even from an installed PWA); cache is only the offline fallback. Images/fonts: cache-first with background refresh.
var C='gre-v6';
var SHELL=['./','index.html','css/style.css','js/app.js','data/events.js','data/restaurants.js','data/cinema.js','data/cinema.json','site.webmanifest'];
self.addEventListener('install',function(e){
  // cache:'reload' bypasses the browser HTTP cache so the new shell is fetched fresh from the server
  e.waitUntil(caches.open(C).then(function(c){return Promise.all(SHELL.map(function(u){return fetch(new Request(u,{cache:'reload'})).then(function(r){if(r.ok)return c.put(u,r)}).catch(function(){})}))}).then(function(){return self.skipWaiting()}));
});
self.addEventListener('activate',function(e){e.waitUntil(caches.keys().then(function(k){return Promise.all(k.filter(function(n){return n!==C}).map(function(n){return caches.delete(n)}))}).then(function(){return self.clients.claim()}))});
function netFirst(r){
  return fetch(r,{cache:'no-cache'}).then(function(res){if(res&&res.ok){var cp=res.clone();caches.open(C).then(function(c){c.put(r,cp)})}return res})
    .catch(function(){return caches.match(r,{ignoreSearch:true}).then(function(hit){return hit||caches.match('index.html')})});
}
self.addEventListener('fetch',function(e){
  var r=e.request;if(r.method!=='GET')return;
  var u=new URL(r.url);
  if(u.origin===location.origin&&(r.mode==='navigate'||/\.(js|css|json|webmanifest|html)$/.test(u.pathname)||u.pathname.endsWith('/'))){e.respondWith(netFirst(r));return}
  e.respondWith(caches.open(C).then(function(c){return c.match(r).then(function(hit){
    var net=fetch(r).then(function(res){if(res&&(res.ok||res.type==='opaque'))c.put(r,res.clone());return res}).catch(function(){return hit});
    return hit||net})}));
});
