document.addEventListener('DOMContentLoaded', ()=>{
    const toggle = document.getElementById('menuToggle');
    const menu = document.getElementById('mobileMenu');
    const icon = toggle?.querySelector('i');
    if(!toggle || !menu) return;
    
    toggle.addEventListener('click', ()=>{
        menu.classList.toggle('active');
        icon.className = menu.classList.contains('active') ? 'fas fa-times' : 'fas fa-bars';
    });
    
    document.querySelectorAll('.mobile-link').forEach(link=>{
        link.addEventListener('click', ()=>{
            menu.classList.remove('active');
            if(icon) icon.className = 'fas fa-bars';
        });
    });
});
