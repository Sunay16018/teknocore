if('serviceWorker' in navigator){
    window.addEventListener('load', ()=>{
        navigator.serviceWorker.register('/sw.js')
            .then(r=> console.log('SW kayıtlı'))
            .catch(e=> console.log('SW hata'));
    });
}
