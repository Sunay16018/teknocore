document.addEventListener('DOMContentLoaded', ()=>{
    const btns = document.querySelectorAll('.filter-btn');
    const items = document.querySelectorAll('.gallery-item');
    if(!btns.length) return;
    
    btns.forEach(btn=>{
        btn.addEventListener('click', ()=>{
            btns.forEach(b=> b.classList.remove('active'));
            btn.classList.add('active');
            const filter = btn.dataset.filter;
            items.forEach(item=>{
                if(filter==='all' || item.classList.contains(filter)){
                    item.style.display = 'block';
                } else {
                    item.style.display = 'none';
                }
            });
        });
    });
});
