const menuToggle = document.getElementById('menuToggle');
const mobileMenu = document.getElementById('mobileMenu');
const menuIcon = menuToggle.querySelector('i');

menuToggle.addEventListener('click', function() {
    mobileMenu.classList.toggle('active');
    menuIcon.className = mobileMenu.classList.contains('active') ? 'fas fa-times' : 'fas fa-bars';
});

document.querySelectorAll('.mobile-link').forEach(link => {
    link.addEventListener('click', function() {
        mobileMenu.classList.remove('active');
        menuIcon.className = 'fas fa-bars';
    });
});
