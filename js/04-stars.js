function createStars(){
    const container = document.getElementById('stars');
    if(!container) return;
    for(let i=0; i<100; i++){
        const s = document.createElement('div');
        s.className = 'star';
        const size = Math.random() * 3;
        const dur = 2 + Math.random() * 5;
        s.style.cssText = `
            width:${size}px; height:${size}px;
            left:${Math.random()*100}%; top:${Math.random()*100}%;
            animation:${dur}s twinkle infinite;
        `;
        container.appendChild(s);
    }
}
document.addEventListener('DOMContentLoaded', createStars);
