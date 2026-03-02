const CACHE = 'teknocek-v1';
const urls = [
    '/', '/index.html', '/manifest.json',
    '/icons/icon-32.png', '/icons/icon-48.png', '/icons/icon-64.png',
    '/icons/icon-72.png', '/icons/icon-96.png', '/icons/icon-128.png',
    '/icons/icon-144.png', '/icons/icon-152.png', '/icons/icon-192.png',
    '/icons/icon-256.png', '/icons/icon-384.png', '/icons/icon-512.png',
    '/icons/icon-1024.png', '/icons/icon-2048.png', '/icons/icon-4096.png'
];
self.addEventListener('install', e => e.waitUntil(caches.open(CACHE).then(c => c.addAll(urls))));
self.addEventListener('fetch', e => e.respondWith(caches.match(e.request).then(r => r || fetch(e.request))));
