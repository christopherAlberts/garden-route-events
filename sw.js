// Retired: the app moved to https://gardenrouteevents.streblainnovations.com — this worker clears old caches and unregisters itself.
self.addEventListener('install',()=>self.skipWaiting());
self.addEventListener('activate',e=>e.waitUntil(caches.keys().then(k=>Promise.all(k.map(c=>caches.delete(c)))).then(()=>self.registration.unregister()).then(()=>self.clients.matchAll({type:'window'})).then(cs=>cs.forEach(c=>c.navigate(c.url)))));
self.addEventListener('fetch',()=>{});
