// Cache the app shell so installed-PWA launches paint from cache (short splash), refresh in background.
var C='gre-v3';
var SHELL=['./','index.html','css/style.css','js/app.js','data/events.js','data/restaurants.js','site.webmanifest'];
self.addEventListener('install',function(e){e.waitUntil(caches.open(C).then(function(c){return c.addAll(SHELL)}).then(function(){return self.skipWaiting()}))});
self.addEventListener('activate',function(e){e.waitUntil(caches.keys().then(function(k){return Promise.all(k.filter(function(n){return n!==C}).map(function(n){return caches.delete(n)}))}).then(function(){return self.clients.claim()}))});
self.addEventListener('fetch',function(e){
  var r=e.request;if(r.method!=='GET')return;
  if(r.mode==='navigate'||/webmanifest$/.test(new URL(r.url).pathname)){e.respondWith(fetch(r).then(function(res){caches.open(C).then(function(c){c.put(r,res.clone())});return res}).catch(function(){return caches.match(r,{ignoreSearch:true})}));return;}
  e.respondWith(caches.open(C).then(function(c){return c.match(r,{ignoreSearch:r.mode==='navigate'}).then(function(hit){
    var net=fetch(r).then(function(res){if(res&&(res.ok||res.type==='opaque'))c.put(r,res.clone());return res}).catch(function(){return hit});
    return hit||net})}));
});
