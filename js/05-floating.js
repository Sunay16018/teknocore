function createFloating(){
    const c = document.querySelector('.floating-icons');
    if(!c) return;
    const icons = ['fa-star','fa-atom','fa-globe','fa-cog','fa-dna','fa-infinity','fa-robot','fa-gem'];
    for(let i=0; i<12; i++){
        const el = document.createElement('i');
        el.className = `fas ${icons[i%icons.length]} floating-icon`;
        const dur = 15 + Math.random() * 20;
        const delay = Math.random() * 10;
        el.style.cssText = `
            top:${Math.random()*100}%; left:${Math.random()*100}%;
            animation:${dur}s float linear infinite;
            animation-delay:${delay}s;
        `;
        c.appendChild(el);
    }
}
document.addEventListener('DOMContentLoaded', createFloating);
